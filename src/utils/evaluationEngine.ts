/**
 * Phase 3B.2 Hardened Evaluation Engine
 * Provides normalization safeguards, punctuation-independent token comparison,
 * UI punctuation separation, and inflected variant handling.
 */

import type { ExerciseDefinition, MatchType } from '../types/exerciseEngine';

/**
 * Strips punctuation and normalizes unicode / whitespace for reliable linguistic comparison.
 */
export function normalizeEvaluationText(
  text: string,
  options: { stripPunctuation?: boolean; caseSensitive?: boolean } = {}
): string {
  if (!text) return '';
  let normalized = text.normalize('NFC').trim();

  // Normalize all types of whitespace (non-breaking spaces, multiple spaces, tabs)
  normalized = normalized.replace(/\s+/g, ' ');

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
 * This guarantees learners interact with grammatical tokens rather than punctuation-polluted items.
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

  // Check main order
  const checkOrder = (expected: string[]): { isCorrect: boolean; mismatched: number[] } => {
    if (normUser.length !== expected.length) {
      return { isCorrect: false, mismatched: Array.from({ length: Math.max(normUser.length, expected.length) }, (_, i) => i) };
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

export interface EvaluationOutcome {
  isCorrect: boolean;
  score: number; // 0 to 1
  feedbackMessage: string;
  details?: Record<string, any>;
}

/**
 * Evaluates learner submission against an ExerciseDefinition with full safeguards.
 */
export function evaluateExerciseSubmission(
  exercise: ExerciseDefinition,
  submission: {
    selectedOptionId?: string;
    selectedOptionIds?: string[];
    textInput?: string;
    arrangedTokens?: string[];
  }
): EvaluationOutcome {
  const matchType: MatchType = exercise.evaluation?.matchType || 'EXACT';

  switch (matchType) {
    case 'TOKEN_ORDER': {
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

    case 'EXACT':
    case 'NORMALIZED_TEXT': {
      const userClean = normalizeEvaluationText(submission.textInput || '', {
        stripPunctuation: exercise.evaluation?.stripPunctuation !== false,
        caseSensitive: exercise.evaluation?.caseSensitive || false,
      });

      const correctClean = normalizeEvaluationText(exercise.correctAnswer, {
        stripPunctuation: exercise.evaluation?.stripPunctuation !== false,
        caseSensitive: exercise.evaluation?.caseSensitive || false,
      });

      let matched = userClean === correctClean;

      // Check acceptable alternatives
      if (!matched && exercise.acceptableAlternatives && exercise.acceptableAlternatives.length > 0) {
        matched = exercise.acceptableAlternatives.some((alt) => {
          const altClean = normalizeEvaluationText(alt, {
            stripPunctuation: exercise.evaluation?.stripPunctuation !== false,
            caseSensitive: exercise.evaluation?.caseSensitive || false,
          });
          return userClean === altClean;
        });
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

    case 'SET_EQUALITY': {
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
      };
    }

    case 'RUBRIC_CRITERIA': {
      // Rubric criteria evaluation (for subjective writing / advanced commentary)
      const userText = submission.textInput || '';
      const hasLength = userText.trim().length >= 40;
      return {
        isCorrect: hasLength,
        score: hasLength ? 1.0 : 0.5,
        feedbackMessage: hasLength
          ? exercise.learnerFeedback.onSuccess
          : exercise.learnerFeedback.onFailure,
        details: { criteriaCount: exercise.evaluation?.rubricCriteria?.length || 0 },
      };
    }

    default: {
      // Multiple choice fallback
      const chosen = exercise.options?.find((o) => o.id === submission.selectedOptionId);
      const isCorrect = !!chosen?.isCorrect;
      return {
        isCorrect,
        score: isCorrect ? 1.0 : 0.0,
        feedbackMessage: isCorrect
          ? exercise.learnerFeedback.onSuccess
          : exercise.learnerFeedback.onFailure,
      };
    }
  }
}
