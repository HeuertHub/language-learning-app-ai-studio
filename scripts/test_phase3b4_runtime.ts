/**
 * Phase 3B.4 Deterministic Runtime Correctness Test Suite
 *
 * Verifies:
 * 1. Genuine PAIR_MATCHING semantics:
 *    - Incomplete pairing fails
 *    - Incorrect pairing fails
 *    - Complete correct pairing passes
 * 2. Qualitative Rubric semantics:
 *    - Substantive response marked isCompleted: true
 *    - Substantive response MUST NOT be marked isCorrect: true
 *    - Score remains 0.0 (no fabricated score)
 * 3. Audio Fallback behavior:
 *    - Mongolian voice available
 *    - Mongolian voice unavailable for isolated phoneme (formant permitted)
 *    - Mongolian voice unavailable for sentence (formant prohibited, unavailable)
 *    - Native-speaker-required exercise without native asset (marked unavailable)
 */

import { evaluateExerciseSubmission } from '../src/utils/evaluationEngine';
import type { ExerciseDefinition } from '../src/types/exerciseEngine';
import { isIsolatedPhoneme, checkExerciseAudioAvailability } from '../src/utils/audio';

function assert(condition: boolean, message: string) {
  if (!condition) {
    console.error(`❌ ASSERTION FAILED: ${message}`);
    process.exit(1);
  }
  console.log(`  ✓ ${message}`);
}

console.log('================================================================================');
console.log('PHASE 3B.4 DETERMINISTIC RUNTIME CORRECTNESS TEST SUITE');
console.log('================================================================================\n');

// -----------------------------------------------------------------------------
// Test 1: PAIR_MATCHING Semantics
// -----------------------------------------------------------------------------
console.log('TEST SUITE 1: Genuine PAIR_MATCHING Verification');

const samplePairExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_pair_matching',
  sequenceInLesson: 1,
  exerciseTitle: 'Grapheme Case Matching',
  modality: 'ORTHOGRAPHY_PHONOLOGY',
  interactionPattern: 'PAIR_MATCHING',
  cognitiveComplexity: 'IDENTIFY_RECOGNIZE',
  skillTargets: ['grapheme_case_pairing'],
  grammarTargets: [],
  vocabularyTargets: ['Т', 'т', 'К', 'к', 'О', 'о', 'А', 'а'],
  prompt: 'Pair uppercase with lowercase Cyrillic letters.',
  matchingPairs: [
    { id: 'p1', left: 'Т', right: 'т' },
    { id: 'p2', left: 'К', right: 'к' },
    { id: 'p3', left: 'О', right: 'о' },
    { id: 'p4', left: 'А', right: 'а' },
  ],
  correctAnswer: 'Т-т, К-к, О-о, А-а',
  hint: 'Match letters with their smaller counterparts.',
  explanation: 'Uppercase and lowercase letters have identical forms in printed Cyrillic.',
  learnerFeedback: {
    onSuccess: 'All pairs match correctly.',
    onFailure: 'Check each pair carefully.',
  },
  evaluation: {
    matchType: 'EXACT',
  },
  lessonId: 'les_test_01',
  unitId: 'unit_test_01',
  cefrLevel: 'Pre-A1',
};

// 1a. Incomplete pairing fails
const incompleteSubmission = {
  matchedPairs: {
    'Т': 'т',
    'К': 'к',
    // Missing 'О' and 'А'
  },
};
const incompleteResult = evaluateExerciseSubmission(samplePairExercise, incompleteSubmission);
assert(incompleteResult.isCorrect === false, 'Incomplete pairing fails (isCorrect === false)');
assert(incompleteResult.details?.status === 'INCOMPLETE', 'Incomplete pairing flagged with status INCOMPLETE');
assert(incompleteResult.score < 1.0, 'Incomplete pairing has fractional score < 1.0');

// 1b. Incorrect pairing fails
const incorrectSubmission = {
  matchedPairs: {
    'Т': 'т',
    'К': 'к',
    'О': 'а', // Mismatch!
    'А': 'о', // Mismatch!
  },
};
const incorrectResult = evaluateExerciseSubmission(samplePairExercise, incorrectSubmission);
assert(incorrectResult.isCorrect === false, 'Incorrect pairing fails (isCorrect === false)');
assert(incorrectResult.details?.correctCount === 2, 'Incorrect pairing identifies exactly 2 correct matches out of 4');

// 1c. Complete correct pairing passes
const correctSubmission = {
  matchedPairs: {
    'Т': 'т',
    'К': 'к',
    'О': 'о',
    'А': 'а',
  },
};
const correctResult = evaluateExerciseSubmission(samplePairExercise, correctSubmission);
assert(correctResult.isCorrect === true, 'Complete correct pairing passes (isCorrect === true)');
assert(correctResult.score === 1.0, 'Complete correct pairing achieves score === 1.0');
assert(correctResult.details?.correctCount === 4, 'All 4 required pairs verified');

// 1d. Learner cannot pass by selecting single combined option
const optionSelectionOnly = {
  selectedOptionId: 'some_option',
};
const optionResult = evaluateExerciseSubmission(samplePairExercise, optionSelectionOnly);
assert(optionResult.isCorrect === false, 'Learner cannot pass PAIR_MATCHING by selecting single option');

console.log('✓ PAIR_MATCHING test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 2: Qualitative Rubric Semantics
// -----------------------------------------------------------------------------
console.log('TEST SUITE 2: Qualitative Rubric Semantics');

const sampleRubricExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_rubric',
  sequenceInLesson: 5,
  exerciseTitle: 'Sovereign Rights Critique',
  modality: 'WRITING_PRODUCTION',
  interactionPattern: 'OPEN_RESPONSE_RUBRIC',
  cognitiveComplexity: 'PARSE_LEGAL_DISCOURSE',
  skillTargets: ['discourse_synthesis'],
  grammarTargets: [],
  vocabularyTargets: [],
  prompt: 'Critique constitutional sovereignty articles in formal style.',
  correctAnswer: 'Substantive analytical essay matching academic rubric criteria.',
  hint: 'Address article structure and rhetorical framing.',
  explanation: 'Rubric evaluates rhetorical cohesion and terminology.',
  learnerFeedback: {
    onSuccess: 'Response Submitted — Review Against Rubric',
    onFailure: 'Please enter a substantive analytical response before submitting.',
  },
  evaluation: {
    matchType: 'RUBRIC_CRITERIA',
    rubricCriteria: [
      { criterionId: 'crit_1', criterion: 'Constitutional Lexicon', description: 'Accurate terminology', points: 5 },
      { criterionId: 'crit_2', criterion: 'Rhetorical Structure', description: 'Formal register syntax', points: 5 },
    ],
  },
  lessonId: 'les_test_c1',
  unitId: 'unit_test_c1',
  cefrLevel: 'C1',
};

// 2a. Short/empty input is incomplete
const shortRubricResult = evaluateExerciseSubmission(sampleRubricExercise, { textInput: 'short' });
assert(shortRubricResult.isCompleted === false, 'Short response is marked isCompleted: false');
assert(shortRubricResult.isCorrect === false, 'Short response is marked isCorrect: false');

// 2b. Substantive input is completed BUT MUST NOT be marked isCorrect: true
const substantiveRubricResult = evaluateExerciseSubmission(sampleRubricExercise, {
  textInput: 'Монгол Улсын Үндсэн хуулийн суурь зарчмууд нь тусгаар тогтнол, бүрэн эрхт байдлыг баталгаажуулдаг.',
});
assert(substantiveRubricResult.isCompleted === true, 'Substantive response is marked isCompleted: true');
assert(substantiveRubricResult.isCorrect === false, 'Substantive qualitative response MUST NOT be marked isCorrect: true');
assert(substantiveRubricResult.score === 0.0, 'No objective correctness score fabricated (score === 0.0)');
assert(substantiveRubricResult.isRubricQualitative === true, 'Flagged as isRubricQualitative: true');
assert(
  substantiveRubricResult.feedbackMessage === 'Response Submitted — Review Against Rubric',
  'Displays neutral feedback: "Response Submitted — Review Against Rubric"'
);

console.log('✓ Qualitative rubric semantics test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 3: Audio Fallback Behavior
// -----------------------------------------------------------------------------
console.log('TEST SUITE 3: Audio Safety & Fallback Behavior');

// 3a. Isolated phoneme vs sentence discrimination
assert(isIsolatedPhoneme('А') === true, 'Single vowel "А" recognized as isolated phoneme');
assert(isIsolatedPhoneme('Т, К, О, А') === true, 'Isolated letter set "Т, К, О, А" recognized as isolated phonemes');
assert(isIsolatedPhoneme('[œ]') === true, 'IPA transcription "[œ]" recognized as isolated phoneme');
assert(isIsolatedPhoneme('/t/') === true, 'IPA transcription "/t/" recognized as isolated phoneme');
assert(isIsolatedPhoneme('кино') === false, 'Full word "кино" NOT recognized as isolated phoneme');
assert(isIsolatedPhoneme('Сайн байна уу?') === false, 'Sentence "Сайн байна уу?" NOT recognized as isolated phoneme');

// 3b. Assessment in node/headless env (no browser synthesis)
const phonemeExercise = {
  audio: {
    requiresAudio: true,
    speechSynthesisText: 'А',
    ipaTranscription: '[a]',
  },
  modality: 'ORTHOGRAPHY_PHONOLOGY',
};
const sentenceExercise = {
  audio: {
    requiresAudio: true,
    speechSynthesisText: 'Сайн байна уу? Таны бие сайн уу?',
    ipaTranscription: '',
  },
  modality: 'DIALOGUE_INTERACTION',
};

// Isolated phoneme allows formant fallback
const phonemeAssessment = checkExerciseAudioAvailability(phonemeExercise);
assert(phonemeAssessment.isAvailable === true, 'Isolated phoneme exercise is available via acoustic formant fallback');
assert(phonemeAssessment.isFormantFallback === true, 'Phoneme audio flagged as formant fallback');

// Sentence prohibits formant fallback and marks audio unavailable
const sentenceAssessment = checkExerciseAudioAvailability(sentenceExercise);
assert(sentenceAssessment.isAvailable === false, 'Sentence exercise audio is UNAVAILABLE when no authentic Mongolian voice is present');
assert(sentenceAssessment.isFormantFallback === false, 'Sentence audio NEVER falls back to formant synthesizer');
assert(sentenceAssessment.requiresNativeAsset === true, 'Sentence audio flagged as requiresNativeAsset: true');

// 3c. Native-speaker-required exercise without native asset
const nativeRequiredExercise = {
  audio: {
    requiresAudio: true,
    speechSynthesisText: 'Парламентын асуулгын сонсгол',
  },
  modality: 'LISTENING_COMPREHENSION',
};
const nativeLesson = {
  audioSuitability: 'native_speaker_required',
};
const nativeAssessment = checkExerciseAudioAvailability(nativeRequiredExercise, nativeLesson);
assert(nativeAssessment.isAvailable === false, 'native_speaker_required exercise without native asset is marked UNAVAILABLE');
assert(nativeAssessment.requiresNativeAsset === true, 'Flagged with requiresNativeAsset: true');

// 3d. Native-speaker-required exercise WITH native asset
const nativeWithAssetExercise = {
  audio: {
    requiresAudio: true,
    speechSynthesisText: 'Парламентын асуулгын сонсгол',
    nativeAudioUrl: '/audio/native/b2_parliament_01.mp3',
  },
  modality: 'LISTENING_COMPREHENSION',
};
const nativeWithAssetAssessment = checkExerciseAudioAvailability(nativeWithAssetExercise, nativeLesson);
assert(nativeWithAssetAssessment.isAvailable === true, 'native_speaker_required exercise WITH native asset is AVAILABLE');
assert(nativeWithAssetAssessment.isFormantFallback === false, 'Native asset does not use formant fallback');

console.log('✓ Audio fallback behavior test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 4: TOKEN_REARRANGEMENT Interaction Pattern
// -----------------------------------------------------------------------------
console.log('TEST SUITE 4: TOKEN_REARRANGEMENT Pattern Verification');

const sampleTokenRearrangementExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_token_rearrange',
  sequenceInLesson: 2,
  exerciseTitle: 'SOV Sentence Syntax Rearrangement',
  modality: 'SYNTAX_MORPHOLOGY',
  interactionPattern: 'TOKEN_REARRANGEMENT',
  cognitiveComplexity: 'APPLY_RULE',
  skillTargets: ['sov_constituent_order'],
  grammarTargets: ['sov_sentence_structure'],
  vocabularyTargets: ['Би', 'ном', 'уншина'],
  prompt: 'Arrange tokens to form standard Subject-Object-Verb syntax.',
  tokens: ['уншина', 'Би', 'ном'],
  correctTokenOrder: ['Би', 'ном', 'уншина'],
  correctAnswer: 'Би ном уншина.',
  hint: 'In Mongolian, verbs occur clause-finally.',
  explanation: 'Mongolian follows strict SOV order: Subject (Би) + Object (ном) + Verb (уншина).',
  learnerFeedback: {
    onSuccess: 'Perfect syntax order!',
    onFailure: 'Check SOV position; verbs belong at the end.',
  },
  evaluation: {
    matchType: 'TOKEN_ORDER',
  },
  lessonId: 'les_test_a1',
  unitId: 'unit_test_a1',
  cefrLevel: 'A1',
};

// 4a. Exact correct token order passes
const correctTokenResult = evaluateExerciseSubmission(sampleTokenRearrangementExercise, {
  arrangedTokens: ['Би', 'ном', 'уншина'],
});
assert(correctTokenResult.isCorrect === true, 'TOKEN_REARRANGEMENT: Exact SOV token order passes (isCorrect === true)');
assert(correctTokenResult.score === 1.0, 'TOKEN_REARRANGEMENT: Exact token order achieves score === 1.0');

// 4b. Inverted / incorrect token order fails
const incorrectTokenResult = evaluateExerciseSubmission(sampleTokenRearrangementExercise, {
  arrangedTokens: ['уншина', 'ном', 'Би'],
});
assert(incorrectTokenResult.isCorrect === false, 'TOKEN_REARRANGEMENT: Inverted token order fails (isCorrect === false)');
assert(incorrectTokenResult.score < 1.0, 'TOKEN_REARRANGEMENT: Inverted token order receives penalty');

// 4c. Incomplete token order fails
const incompleteTokenResult = evaluateExerciseSubmission(sampleTokenRearrangementExercise, {
  arrangedTokens: ['Би', 'ном'],
});
assert(incompleteTokenResult.isCorrect === false, 'TOKEN_REARRANGEMENT: Missing verb token fails (isCorrect === false)');

console.log('✓ TOKEN_REARRANGEMENT test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 5: MULTI_SELECT Interaction Pattern
// -----------------------------------------------------------------------------
console.log('TEST SUITE 5: MULTI_SELECT Pattern Verification');

const sampleMultiSelectExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_multi_select',
  sequenceInLesson: 3,
  exerciseTitle: 'Back Vowel Identification',
  modality: 'ORTHOGRAPHY_PHONOLOGY',
  interactionPattern: 'MULTI_SELECT',
  cognitiveComplexity: 'IDENTIFY_RECOGNIZE',
  skillTargets: ['vowel_harmony_classification'],
  grammarTargets: ['vowel_harmony'],
  vocabularyTargets: ['а', 'о', 'у', 'э', 'ө'],
  prompt: 'Select all masculine (back) vowels in Mongolian.',
  options: [
    { id: 'opt_a', text: 'А', isCorrect: true, feedback: 'Masculine back vowel.' },
    { id: 'opt_o', text: 'О', isCorrect: true, feedback: 'Masculine back vowel.' },
    { id: 'opt_u', text: 'У', isCorrect: true, feedback: 'Masculine back vowel.' },
    { id: 'opt_e', text: 'Э', isCorrect: false, feedback: 'Feminine front vowel.' },
    { id: 'opt_oe', text: 'Ө', isCorrect: false, feedback: 'Feminine front vowel.' },
  ],
  correctAnswer: 'А, О, У',
  hint: 'Masculine vowels include А, О, У, Я, Ё, Ю(а).',
  explanation: 'А, О, У are back vowels.',
  learnerFeedback: {
    onSuccess: 'Identified all back vowels correctly.',
    onFailure: 'Remember masculine back vowels vs feminine front vowels.',
  },
  evaluation: {
    matchType: 'SET_EQUALITY',
  },
  lessonId: 'les_test_pre_a1',
  unitId: 'unit_test_pre_a1',
  cefrLevel: 'Pre-A1',
};

// 5a. Exactly all correct options selected passes
const correctMultiSelectResult = evaluateExerciseSubmission(sampleMultiSelectExercise, {
  selectedOptionIds: ['opt_a', 'opt_o', 'opt_u'],
});
assert(correctMultiSelectResult.isCorrect === true, 'MULTI_SELECT: All correct options selected passes (isCorrect === true)');
assert(correctMultiSelectResult.score === 1.0, 'MULTI_SELECT: All correct options receives score === 1.0');

// 5b. Missing one correct option fails
const partialMultiSelectResult = evaluateExerciseSubmission(sampleMultiSelectExercise, {
  selectedOptionIds: ['opt_a', 'opt_o'], // missing opt_u
});
assert(partialMultiSelectResult.isCorrect === false, 'MULTI_SELECT: Missing option fails (isCorrect === false)');

// 5c. Extra incorrect distractor option fails
const distractorMultiSelectResult = evaluateExerciseSubmission(sampleMultiSelectExercise, {
  selectedOptionIds: ['opt_a', 'opt_o', 'opt_u', 'opt_e'], // extra distractor
});
assert(distractorMultiSelectResult.isCorrect === false, 'MULTI_SELECT: Including distractor fails (isCorrect === false)');

console.log('✓ MULTI_SELECT test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 6: SUFFIX_ATTACHMENT Interaction Pattern
// -----------------------------------------------------------------------------
console.log('TEST SUITE 6: SUFFIX_ATTACHMENT Pattern Verification');

const sampleSuffixExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_suffix_attach',
  sequenceInLesson: 4,
  exerciseTitle: 'Instrumental Case Suffix Selection',
  modality: 'SYNTAX_MORPHOLOGY',
  interactionPattern: 'SUFFIX_ATTACHMENT',
  cognitiveComplexity: 'APPLY_RULE',
  skillTargets: ['instrumental_case_harmony'],
  grammarTargets: ['instrumental_case'],
  vocabularyTargets: ['ном', '-оор'],
  prompt: 'Attach the correct instrumental case suffix to "ном" (book).',
  baseWord: 'ном',
  options: [
    { id: 'suf_1', text: '-оор', isCorrect: true },
    { id: 'suf_2', text: '-ээр', isCorrect: false },
    { id: 'suf_3', text: '-аар', isCorrect: false },
    { id: 'suf_4', text: '-өөр', isCorrect: false },
  ],
  correctSuffix: '-оор',
  correctAnswer: 'номоор',
  hint: 'Base word has stem vowel "о", requiring rounded back vowel suffix.',
  explanation: 'Nominal stem "ном" has "о", requiring the labial back-vowel instrumental suffix "-оор" (номоор).',
  learnerFeedback: {
    onSuccess: 'Correctly applied labial vowel harmony: ном + оор = номоор.',
    onFailure: 'Stem "о" requires the rounded back harmonic allomorph "-оор".',
  },
  evaluation: {
    matchType: 'EXACT',
  },
  lessonId: 'les_test_a1_02',
  unitId: 'unit_test_a1_02',
  cefrLevel: 'A1',
};

// 6a. Correct selectedSuffix passes
const correctSuffixResult = evaluateExerciseSubmission(sampleSuffixExercise, {
  selectedSuffix: '-оор',
});
assert(correctSuffixResult.isCorrect === true, 'SUFFIX_ATTACHMENT: Correct harmonic suffix passes (isCorrect === true)');
assert(correctSuffixResult.score === 1.0, 'SUFFIX_ATTACHMENT: Correct suffix achieves score === 1.0');

// 6b. Correct combined textInput passes
const combinedTextResult = evaluateExerciseSubmission(sampleSuffixExercise, {
  textInput: 'номоор',
});
assert(combinedTextResult.isCorrect === true, 'SUFFIX_ATTACHMENT: Combined word "номоор" passes (isCorrect === true)');

// 6c. Incorrect vowel harmony suffix fails
const incorrectHarmonicSuffixResult = evaluateExerciseSubmission(sampleSuffixExercise, {
  selectedSuffix: '-ээр',
});
assert(incorrectHarmonicSuffixResult.isCorrect === false, 'SUFFIX_ATTACHMENT: Wrong harmonic suffix "-ээр" fails (isCorrect === false)');

// 6d. Incorrect unrounded vowel harmony suffix fails
const unroundedSuffixResult = evaluateExerciseSubmission(sampleSuffixExercise, {
  selectedSuffix: '-аар',
});
assert(unroundedSuffixResult.isCorrect === false, 'SUFFIX_ATTACHMENT: Unrounded harmonic suffix "-аар" fails (isCorrect === false)');

console.log('✓ SUFFIX_ATTACHMENT test suite passed successfully.\n');

// -----------------------------------------------------------------------------
// Test 7: NORMALIZED_TEXT Interaction Pattern
// -----------------------------------------------------------------------------
console.log('TEST SUITE 7: NORMALIZED_TEXT Pattern Verification');

const sampleNormalizedExercise: ExerciseDefinition = {
  exerciseId: 'ex_test_normalized_text',
  sequenceInLesson: 1,
  exerciseTitle: 'Cyrillic Dictation / Cloze Entry',
  modality: 'WRITING_PRODUCTION',
  interactionPattern: 'NORMALIZED_TEXT',
  cognitiveComplexity: 'APPLY_RULE',
  skillTargets: ['cloze_spelling'],
  grammarTargets: [],
  vocabularyTargets: ['Улаанбаатар'],
  prompt: 'Type the capital city of Mongolia in Cyrillic.',
  correctAnswer: 'Улаанбаатар',
  acceptableAlternatives: ['Улаанбаатар хот'],
  hint: 'Capital of Mongolia.',
  explanation: 'Улаанбаатар is the official name of the capital city.',
  learnerFeedback: {
    onSuccess: 'Correct spelling!',
    onFailure: 'Check spelling and Cyrillic glyphs.',
  },
  evaluation: {
    matchType: 'NORMALIZED_TEXT',
    stripPunctuation: true,
    caseSensitive: false,
    normalizeWhitespace: true,
  },
  lessonId: 'les_test_a1_03',
  unitId: 'unit_test_a1_03',
  cefrLevel: 'A1',
};

// 7a. Exact match passes
const exactNormResult = evaluateExerciseSubmission(sampleNormalizedExercise, {
  textInput: 'Улаанбаатар',
});
assert(exactNormResult.isCorrect === true, 'NORMALIZED_TEXT: Exact match passes (isCorrect === true)');

// 7b. Case-insensitive and punctuation/whitespace-tolerant match passes
const tolerantNormResult = evaluateExerciseSubmission(sampleNormalizedExercise, {
  textInput: '  улаанбаатар.  ',
});
assert(tolerantNormResult.isCorrect === true, 'NORMALIZED_TEXT: Tolerant whitespace/punctuation/case passes (isCorrect === true)');

// 7c. Acceptable alternative passes
const altNormResult = evaluateExerciseSubmission(sampleNormalizedExercise, {
  textInput: 'улаанбаатар хот',
});
assert(altNormResult.isCorrect === true, 'NORMALIZED_TEXT: Acceptable alternative "Улаанбаатар хот" passes (isCorrect === true)');

// 7d. Incorrect spelling / wrong lexical item fails
const wrongNormResult = evaluateExerciseSubmission(sampleNormalizedExercise, {
  textInput: 'Дархан хот',
});
assert(wrongNormResult.isCorrect === false, 'NORMALIZED_TEXT: Incorrect lexical entry fails (isCorrect === false)');

console.log('✓ NORMALIZED_TEXT test suite passed successfully.\n');

console.log('================================================================================');
console.log('ALL PHASE 3B.4 RUNTIME TESTS COMPLETED SUCCESSFULLY (100% PASS)');
console.log('================================================================================');
