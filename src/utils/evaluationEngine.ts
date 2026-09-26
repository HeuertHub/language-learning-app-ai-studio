/**
 * Phase 3B.3 Hardened Evaluation Engine
 * Authoritative evaluation runtime for all 9 interaction patterns:
 * MULTIPLE_CHOICE, MULTI_SELECT, PAIR_MATCHING, TOKEN_REARRANGEMENT,
 * CLOZE_TEXT, SUFFIX_ATTACHMENT, AUDIO_COMPREHENSION, AUDIO_DICTATION,
 * OPEN_RESPONSE_RUBRIC / FREE_RESPONSE_RUBRIC.
 *
 * Implements:
 * - Normalization safeguards (Unicode NFC, whitespace collapsing, punctuation stripping)
 * - Punctuation-independent token order comparison
 * - Strict schema flag support (caseSensitive, stripPunctuation, normalizeWhitespace, allowInflectedVariants)
 * - Acceptable alternatives validation
 * - Dual-layer Rubric Evaluation (separates submission completion from qualitative assessment)
 * - Zero duplicate evaluation engines
 */

import type {
  ExerciseDefinition,
  MatchType,
  SubmissionPayload,
  EvaluationOutcome,
  RubricCriterionItem,
} from '../types/exerciseEngine';

export type { SubmissionPayload, EvaluationOutcome, RubricCriterionItem };

export interface EvaluationTextOptions {
  stripPunctuation?: boolean;
  caseSensitive?: boolean;
  normalizeWhitespace?: boolean;
}

/**
 * Strips punctuation and normalizes unicode / whitespace for reliable linguistic comparison.
 */
export function normalizeEvaluationText(
  text: string,
  options: EvaluationTextOptions = {}
): string {
  if (!text) return '';
  let normalized = text.normalize('NFC').trim();

  // Normalize all types of whitespace (non-breaking spaces, multiple spaces, tabs)
  if (options.normalizeWhitespace !== false) {
    normalized = normalized.replace(/\s+/g, ' ');
  }

  if (!options.caseSensitive) {
    normalized = normalized.toLowerCase();
  }

  if (options.stripPunctuation !== false) {
    // Strip Mongolian and standard punctuation marks
    // Preserves Cyrillic letters and alphanumerics
    normalized = normalized.replace(/[.,!?;:«»"“”—–()\[\]{}\/\\-]/g, ' ');
    // Re-collapse whitespace created by punctuation replacement
    normalized = normalized.replace(/\s+/g, ' ').trim();
  }

  return normalized;
}

/**
 * Separates UI punctuation (commas, periods, quotation marks) from core linguistic tokens.
 * Guarantees learners manipulate grammatical tokens rather than punctuation-polluted items.
 */
export function separateUiPunctuation(token: string): {
  cleanToken: string;
  leadingPunct: string;
  trailingPunct: string;
} {
  if (!token) return { cleanToken: '', leadingPunct: '', trailingPunct: '' };

  const match = token.match(/^([.,!?;:«»"“”—–()\[\]{}]*)(.*?)([.,!?;:«»"“”—–()\[\]{}]*)$/);
  if (!match) {
    return { cleanToken: token.trim(), leadingPunct: '', trailingPunct: '' };
  }

  return {
    leadingPunct: match[1] || '',
    cleanToken: (match[2] || '').trim(),
    trailingPunct: match[3] || '',
  };
}

/**
 * Compares two tokens ignoring casing and surrounding punctuation.
 */
export function compareTokensPunctuationIndependent(tokenA: string, tokenB: string): boolean {
  const normA = normalizeEvaluationText(tokenA, { stripPunctuation: true, caseSensitive: false });
  const normB = normalizeEvaluationText(tokenB, { stripPunctuation: true, caseSensitive: false });
  return normA === normB;
}

export interface TokenOrderEvaluationResult {
  isCorrect: boolean;
  matchScore: number; // 0 to 1
  mismatchedIndices: number[];
  normalizedUserTokens: string[];
  normalizedExpectedTokens: string[];
}

/**
 * Evaluates whether user token sequence matches expected token order,
 * with safeguards for punctuation separation and acceptable alternatives.
 */
export function evaluateTokenOrder(
  userTokens: string[],
  expectedTokens: string[],
  acceptableAlternativeOrders?: string[][]
): TokenOrderEvaluationResult {
  const normUser = userTokens.map((t) =>
    normalizeEvaluationText(t, { stripPunctuation: true, caseSensitive: false })
  );
  const normExpected = expectedTokens.map((t) =>
    normalizeEvaluationText(t, { stripPunctuation: true, caseSensitive: false })
  );

  const checkOrder = (expected: string[]): { isCorrect: boolean; mismatched: number[] } => {
    if (normUser.length !== expected.length) {
      return {
        isCorrect: false,
        mismatched: Array.from({ length: Math.max(normUser.length, expected.length) }, (_, i) => i),
      };
    }
    const mismatched: number[] = [];
    for (let i = 0; i < expected.length; i++) {
      if (normUser[i] !== expected[i]) {
        mismatched.push(i);
      }
    }
    return { isCorrect: mismatched.length === 0, mismatched };
  };

  const primaryResult = checkOrder(normExpected);
  if (primaryResult.isCorrect) {
    return {
      isCorrect: true,
      matchScore: 1.0,
      mismatchedIndices: [],
      normalizedUserTokens: normUser,
      normalizedExpectedTokens: normExpected,
    };
  }

  // Check acceptable alternatives if provided
  if (acceptableAlternativeOrders && acceptableAlternativeOrders.length > 0) {
    for (const alt of acceptableAlternativeOrders) {
      const normAlt = alt.map((t) =>
        normalizeEvaluationText(t, { stripPunctuation: true, caseSensitive: false })
      );
      const altResult = checkOrder(normAlt);
      if (altResult.isCorrect) {
        return {
          isCorrect: true,
          matchScore: 1.0,
          mismatchedIndices: [],
          normalizedUserTokens: normUser,
          normalizedExpectedTokens: normAlt,
        };
      }
    }
  }

  const matchCount = normExpected.filter((t, i) => normUser[i] === t).length;
  const matchScore = normExpected.length > 0 ? matchCount / normExpected.length : 0;

  return {
    isCorrect: false,
    matchScore,
    mismatchedIndices: primaryResult.mismatched,
    normalizedUserTokens: normUser,
    normalizedExpectedTokens: normExpected,
  };
}

/**
 * Evaluates learner submission against an ExerciseDefinition with full safeguards and contract adherence.
 */
export function evaluateExerciseSubmission(
  exercise: ExerciseDefinition,
  submission: SubmissionPayload
): EvaluationOutcome {
  const matchType: MatchType | string = exercise.evaluation?.matchType || 'EXACT';
  const pattern = exercise.interactionPattern;

  // 1. Token Rearrangement Pattern & Token Order Match
  if (pattern === 'TOKEN_REARRANGEMENT' || matchType === 'TOKEN_ORDER') {
    const userTokens = submission.arrangedTokens || [];
    const expected = exercise.correctTokenOrder || [];
    const res = evaluateTokenOrder(userTokens, expected);

    return {
      isCorrect: res.isCorrect,
      score: res.matchScore,
      feedbackMessage: res.isCorrect
        ? exercise.learnerFeedback.onSuccess
        : exercise.learnerFeedback.onFailure,
      details: {
        mismatchedIndices: res.mismatchedIndices,
        userTokens: res.normalizedUserTokens,
        expectedTokens: res.normalizedExpectedTokens,
      },
    };
  }

  // 2. Suffix Attachment Pattern
  if (pattern === 'SUFFIX_ATTACHMENT') {
    let isCorrect = false;
    if (submission.selectedSuffix && exercise.correctSuffix) {
      isCorrect =
        normalizeEvaluationText(submission.selectedSuffix, { stripPunctuation: true }) ===
        normalizeEvaluationText(exercise.correctSuffix, { stripPunctuation: true });
    } else if (submission.textInput) {
      const userClean = normalizeEvaluationText(submission.textInput, {
        stripPunctuation: true,
        caseSensitive: false,
      });
      const targetClean = normalizeEvaluationText(exercise.correctAnswer, {
        stripPunctuation: true,
        caseSensitive: false,
      });
      const combinedClean = normalizeEvaluationText(
        (exercise.baseWord || '') + (exercise.correctSuffix || ''),
        { stripPunctuation: true, caseSensitive: false }
      );
      isCorrect = userClean === targetClean || userClean === combinedClean;
    }

    return {
      isCorrect,
      score: isCorrect ? 1.0 : 0.0,
      feedbackMessage: isCorrect
        ? exercise.learnerFeedback.onSuccess
        : exercise.learnerFeedback.onFailure,
      details: {
        selectedSuffix: submission.selectedSuffix,
        expectedSuffix: exercise.correctSuffix,
        baseWord: exercise.baseWord,
      },
    };
  }

  // 3. Multi-Select / Set Equality Match
  if (pattern === 'MULTI_SELECT' || matchType === 'SET_EQUALITY') {
    const userOptions = new Set(submission.selectedOptionIds || []);
    const correctOptions = new Set(
      (exercise.options || []).filter((o) => o.isCorrect).map((o) => o.id)
    );

    const isSame =
      userOptions.size === correctOptions.size &&
      Array.from(userOptions).every((id) => correctOptions.has(id));

    return {
      isCorrect: isSame,
      score: isSame ? 1.0 : 0.0,
      feedbackMessage: isSame
        ? exercise.learnerFeedback.onSuccess
        : exercise.learnerFeedback.onFailure,
      details: {
        selectedCount: userOptions.size,
        requiredCount: correctOptions.size,
      },
    };
  }

  // 4. Qualitative Rubric Evaluation (Separates submission completion from qualitative linguistic scoring)
  if (pattern === 'OPEN_RESPONSE_RUBRIC' || pattern === 'FREE_RESPONSE_RUBRIC' || matchType === 'RUBRIC_CRITERIA') {
    const userText = submission.textInput || '';
    const trimmed = userText.trim();
    // Substantive completion requires minimal response content (e.g. 15 chars)
    const isCompleted = trimmed.length >= 15;
    const criteria = exercise.evaluation?.rubricCriteria || [];

    return {
      isCorrect: false, // Per Phase 3B.4: substantive response may be completed, but MUST NOT be marked isCorrect: true
      isCompleted,
      score: 0.0, // Objective correctness score must not be fabricated for unevaluated qualitative response
      isRubricQualitative: true,
      rubricCriteria: criteria,
      feedbackMessage: isCompleted
        ? 'Response Submitted — Review Against Rubric'
        : 'Please enter a substantive analytical response before submitting for rubric evaluation.',
      details: {
        characterCount: trimmed.length,
        criteriaCount: criteria.length,
        completionStatus: isCompleted ? 'SUBMITTED' : 'INCOMPLETE',
      },
    };
  }

  // 5. Genuine Pair Matching Pattern
  if (pattern === 'PAIR_MATCHING') {
    const requiredPairs = exercise.matchingPairs || [];
    if (requiredPairs.length === 0) {
      return {
        isCorrect: false,
        score: 0.0,
        feedbackMessage: 'Malformed exercise: no matching pairs defined.',
      };
    }

    const userPairs = submission.matchedPairs || {};
    const userMatchedKeys = Object.keys(userPairs).filter((k) => !!userPairs[k]);

    // Incomplete check: learner must construct all required pairs
    if (userMatchedKeys.length < requiredPairs.length) {
      return {
        isCorrect: false,
        score: requiredPairs.length > 0 ? userMatchedKeys.length / requiredPairs.length : 0.0,
        feedbackMessage: `Incomplete: You have constructed ${userMatchedKeys.length} of ${requiredPairs.length} required pairs.`,
        details: {
          matchedCount: userMatchedKeys.length,
          requiredCount: requiredPairs.length,
          status: 'INCOMPLETE',
        },
      };
    }

    // Verify every required pair
    const pairResults: { left: string; expectedRight: string; userRight: string; isMatch: boolean }[] = [];
    let correctMatches = 0;

    for (const p of requiredPairs) {
      const userVal = userPairs[p.left] ?? userPairs[p.id];
      const isMatch = !!userVal && (
        normalizeEvaluationText(userVal, { stripPunctuation: true, caseSensitive: false }) ===
        normalizeEvaluationText(p.right, { stripPunctuation: true, caseSensitive: false })
      );

      if (isMatch) correctMatches++;
      pairResults.push({
        left: p.left,
        expectedRight: p.right,
        userRight: userVal || '',
        isMatch,
      });
    }

    const isFullyCorrect = correctMatches === requiredPairs.length && userMatchedKeys.length === requiredPairs.length;

    return {
      isCorrect: isFullyCorrect,
      score: requiredPairs.length > 0 ? correctMatches / requiredPairs.length : 0.0,
      feedbackMessage: isFullyCorrect
        ? exercise.learnerFeedback.onSuccess
        : exercise.learnerFeedback.onFailure,
      details: {
        correctCount: correctMatches,
        requiredCount: requiredPairs.length,
        pairs: pairResults,
      },
    };
  }

  // 6. Text Entry / Normalized / Case-Insensitive / Exact Match
  if (
    pattern === 'CLOZE_TEXT' ||
    pattern === 'AUDIO_DICTATION' ||
    (submission.textInput !== undefined &&
      pattern !== 'MULTIPLE_CHOICE' &&
      pattern !== 'AUDIO_COMPREHENSION' &&
      (matchType === 'NORMALIZED_TEXT' ||
        matchType === 'CASE_INSENSITIVE' ||
        matchType === 'EXACT'))
  ) {
    const evalRule = exercise.evaluation || { matchType: 'NORMALIZED_TEXT' };
    const caseSensitive = evalRule.caseSensitive === true;
    const stripPunctuation = evalRule.stripPunctuation !== false;
    const normalizeWhitespace = evalRule.normalizeWhitespace !== false;

    const userClean = normalizeEvaluationText(submission.textInput || '', {
      stripPunctuation,
      caseSensitive,
      normalizeWhitespace,
    });

    const correctClean = normalizeEvaluationText(exercise.correctAnswer, {
      stripPunctuation,
      caseSensitive,
      normalizeWhitespace,
    });

    let matched = userClean === correctClean && userClean.length > 0;

    // Check acceptable alternatives
    if (!matched && exercise.acceptableAlternatives && exercise.acceptableAlternatives.length > 0) {
      matched = exercise.acceptableAlternatives.some((alt) => {
        const altClean = normalizeEvaluationText(alt, {
          stripPunctuation,
          caseSensitive,
          normalizeWhitespace,
        });
        return userClean === altClean;
      });
    }

    // Check inflected variants if enabled in schema
    if (!matched && evalRule.allowInflectedVariants && exercise.baseWord) {
      const baseClean = normalizeEvaluationText(exercise.baseWord, {
        stripPunctuation: true,
        caseSensitive: false,
      });
      if (userClean.startsWith(baseClean)) {
        matched = true;
      }
    }

    return {
      isCorrect: matched,
      score: matched ? 1.0 : 0.0,
      feedbackMessage: matched
        ? exercise.learnerFeedback.onSuccess
        : exercise.learnerFeedback.onFailure,
      details: { userClean, correctClean },
    };
  }

  // 7. Default Option Selection (Multiple Choice, Audio Comprehension)
  const chosen = exercise.options?.find((o) => o.id === submission.selectedOptionId);
  const isCorrect = !!chosen?.isCorrect;

  return {
    isCorrect,
    score: isCorrect ? 1.0 : 0.0,
    feedbackMessage: isCorrect
      ? exercise.learnerFeedback.onSuccess
      : exercise.learnerFeedback.onFailure,
    details: { selectedOptionId: submission.selectedOptionId },
  };
}
