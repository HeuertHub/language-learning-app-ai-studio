/**
 * Phase 3A / 3B Exercise Engine Data Architecture & Schemas
 * Authoritative schema definitions for learner-facing exercise content
 * consuming frozen CEFR lesson blueprints.
 */

export type CEFRLevel = 'Pre-A1' | 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';

export type ExerciseModality =
  | 'ORTHOGRAPHY_PHONOLOGY'
  | 'VOCABULARY_ACQUISITION'
  | 'GRAMMAR_INTRODUCTION'
  | 'GRAMMAR_PRACTICE'
  | 'READING_COMPREHENSION'
  | 'LISTENING_COMPREHENSION'
  | 'DIALOGUE_INTERACTION'
  | 'WRITING_PRODUCTION'
  | 'SYNTHESIS_CAPSTONE'
  | 'CONSTITUTIONAL_STATUTORY_READING'
  | 'JURISPRUDENTIAL_LEGAL_COMMENTARY'
  | 'KHALKHA_PHONOTACTICS_DECODING'
  | 'AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS'
  | 'MODERNIST_SATIRE_SYNTHESIS';

export type InteractionPattern =
  | 'MULTIPLE_CHOICE'
  | 'MULTI_SELECT'
  | 'PAIR_MATCHING'
  | 'TOKEN_REARRANGEMENT'
  | 'CLOZE_TEXT'
  | 'SUFFIX_ATTACHMENT'
  | 'AUDIO_COMPREHENSION'
  | 'AUDIO_DICTATION'
  | 'OPEN_RESPONSE_RUBRIC'
  | 'FREE_RESPONSE_RUBRIC';

export type CognitiveComplexity =
  | 'IDENTIFY_RECOGNIZE'
  | 'DISCRIMINATE_PHONEMES'
  | 'RETRIEVE_MATCH'
  | 'APPLY_MORPHOLOGY'
  | 'ANALYZE_SYNTAX'
  | 'PARSE_LEGAL_DISCOURSE'
  | 'EVALUATE_PRAGMATICS'
  | 'SYNTHESIZE_CRITIQUE';

export type MatchType =
  | 'EXACT'
  | 'TOKEN_ORDER'
  | 'NORMALIZED_TEXT'
  | 'SET_EQUALITY'
  | 'RUBRIC_CRITERIA';

export interface EvaluationRule {
  matchType: MatchType;
  caseSensitive?: boolean;
  stripPunctuation?: boolean;
  normalizeWhitespace?: boolean;
  allowInflectedVariants?: boolean;
  rubricCriteria?: {
    criterionId?: string;
    criterion?: string;
    description: string;
    points: number;
  }[];
}

export interface ExerciseOption {
  id: string;
  text: string;
  cyrillic?: string;
  translation?: string;
  distractorRationale?: string;
  isCorrect: boolean;
  explanation?: string;
}

export interface AudioExerciseConfig {
  requiresAudio: boolean;
  speechSynthesisText?: string;
  slowSpeechSynthesisText?: string;
  ipaTranscription?: string;
  speakerRole?: 'narrator' | 'official' | 'disputant_a' | 'disputant_b' | 'elder';
  speechRate?: number;
}

export interface LearnerFeedback {
  onSuccess: string;
  onFailure: string;
}

export interface ExerciseDefinition {
  exerciseId: string;
  sequenceInLesson: number;
  exerciseTitle: string;
  modality: ExerciseModality;
  interactionPattern: InteractionPattern;
  cognitiveComplexity: CognitiveComplexity;
  skillTargets: string[];
  grammarTargets: string[];
  vocabularyTargets: string[];
  prompt: string;
  stimulusTextCyrillic?: string;
  stimulusTranslation?: string;
  contextSentence?: string;
  options?: ExerciseOption[];
  wordTokens?: string[];
  correctTokenOrder?: string[];
  baseWord?: string;
  suffixOptions?: string[];
  correctSuffix?: string;
  correctAnswer: string;
  acceptableAlternatives?: string[];
  hint: string;
  explanation: string;
  learnerFeedback: LearnerFeedback;
  detailedGrammarNote?: string;
  audio?: AudioExerciseConfig;
  evaluation: EvaluationRule;
  lessonId: string;
  unitId: string;
  cefrLevel: CEFRLevel;
}

export interface LessonExerciseBundle {
  lessonId: string;
  unitId: string;
  cefrLevel: CEFRLevel;
  lessonTitle: string;
  lessonType: string;
  primaryPurpose: string;
  communicativeOutcome: string;
  exerciseCount: number;
  exercises: ExerciseDefinition[];
}

export interface PilotManifest {
  manifestVersion: string;
  generatedAt: string;
  phase: string;
  totalLessons: number;
  totalExercises: number;
  lessonsByLevel: Record<CEFRLevel, number>;
  lessons: LessonExerciseBundle[];
}
