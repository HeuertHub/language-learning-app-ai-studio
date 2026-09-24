/**
 * Core Exercise Engine TypeScript Definitions
 * Phase 3A: Exercise Engine Architecture
 * 
 * Strict schemas for learner-facing content generated from frozen lesson blueprints.
 * Does NOT modify any curriculum blueprints.
 */

export type CEFRLevel = 'Pre-A1' | 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';

export type ExerciseModality = 
  | 'vocabulary'
  | 'grammar_introduction'
  | 'grammar_practice'
  | 'reading'
  | 'listening'
  | 'speaking'
  | 'writing'
  | 'synthesis_capstone';

export type ExerciseTaxonomyType =
  // Phonological / Orthographic (Pre-A1 / A1)
  | 'phonemic_discrimination'
  | 'vowel_harmony_categorization'
  | 'cyrillic_grapheme_transcription'
  | 'syllabic_segmentation'
  | 'orthographic_spelling_drill'
  // Morphosyntactic (A1 - C2)
  | 'morpheme_attachment_drill'
  | 'case_government_selection'
  | 'converb_clause_linkage'
  | 'voice_valency_transformation'
  | 'modal_particle_insertion'
  | 'cloze_grammatical_matrix'
  | 'sov_syntactic_reordering'
  // Lexical & Idiomatic (A2 - C2)
  | 'collocational_pairing'
  | 'somatic_idiom_application'
  | 'synonym_nuance_ranking'
  | 'register_level_matching'
  // Receptive Comprehension (B1 - C2)
  | 'audio_dialogue_inference'
  | 'acoustic_dialect_discrimination'
  | 'intertextual_reading_analysis'
  | 'subtext_irony_decoding'
  | 'philological_gloss_exegesis'
  // Productive Expression (B2 - C2)
  | 'guided_epistolary_composition'
  | 'oratorical_framing_delivery'
  | 'ceremonial_blessing_formulation'
  | 'discourse_refutation_builder'
  | 'proverbial_clinching_synthesis';

export type SkillTargetDomain = 
  | 'listening'
  | 'reading'
  | 'spoken_production'
  | 'spoken_interaction'
  | 'written_production'
  | 'written_interaction'
  | 'linguistic_metacognition';

export type CognitiveLevel = 
  | 'remember' 
  | 'understand' 
  | 'apply' 
  | 'analyze' 
  | 'evaluate' 
  | 'create';

export type EvaluatorType =
  | 'exact_token_match'
  | 'normalized_cyrillic_text'
  | 'sov_permutation_evaluator'
  | 'morphological_slot_evaluator'
  | 'semantic_rubric_evaluator'
  | 'phonetic_acoustic_evaluator';

export type AudioRequirementTier =
  | 'none'
  | 'speech_synthesis_standard'
  | 'speech_synthesis_slow'
  | 'native_studio_required'
  | 'archival_authentic_required';

export interface DistractorAnalysis {
  optionId: string;
  text: string;
  cyrillicText?: string;
  errorCategory: 
    | 'vowel_harmony_violation'
    | 'incorrect_case_government'
    | 'semantic_false_friend'
    | 'register_clash'
    | 'syntactic_word_order_error'
    | 'collocational_mismatch'
    | 'distractor_plausible_contrasting';
  pedagogicalExplanation: string;
}

export interface ProgressiveHint {
  tier: 1 | 2 | 3;
  type: 'metalinguistic_nudge' | 'structural_scaffold' | 'near_solution_framing';
  contentCyrillic?: string;
  contentEnglish: string;
}

export interface ExerciseOptionItem {
  id: string;
  text: string;
  cyrillic?: string;
  isCorrect: boolean;
  explanation: string;
}

export interface ExercisePromptPayload {
  instructionCyrillic: string;
  instructionEnglish: string;
  stimulusType: 'text' | 'audio' | 'dialogue' | 'archival_quote' | 'philological_gloss' | 'none';
  stimulusTextCyrillic?: string;
  stimulusTextEnglish?: string;
  dialogueTurns?: Array<{
    speaker: string;
    textCyrillic: string;
    textEnglish?: string;
  }>;
  audioStimulusId?: string;
  culturalOrPragmaticContext?: string;
}

export interface ExerciseAnswerPayload {
  evaluatorType: EvaluatorType;
  // Multiple Choice / Sort
  options?: ExerciseOptionItem[];
  distractorAnalyses?: DistractorAnalysis[];
  // Syntactic Builder / Token Arrangement
  wordTokens?: string[];
  validTokenPermutations?: string[][];
  // Morphological Suffix Fill
  baseStemCyrillic?: string;
  targetMorpheme?: string;
  acceptableMorphemeVariants?: string[];
  // Free Text / Rubric
  canonicalAnswers?: string[];
  acceptableVariations?: string[];
  regexValidationPatterns?: string[];
  requiredKeywords?: string[];
  disallowedElements?: string[];
}

export interface ExerciseAudioMetadata {
  requirementTier: AudioRequirementTier;
  targetAudioTextCyrillic?: string;
  slowAudioTextCyrillic?: string;
  expectedSpeedWpm: number;
  speakerProfile: {
    dialect: 'standard_khalkha' | 'western_oirat' | 'buryat' | 'inner_mongolian';
    gender: 'female' | 'male' | 'unspecified';
    ageGroup: 'adult' | 'elderly' | 'youth';
    acousticEnvironment: 'studio_clean' | 'steppe_outdoor' | 'archival_analog';
  };
  audioPurpose: string;
}

export interface ExerciseEvaluationRules {
  ignorePunctuation: boolean;
  ignoreWhitespace: boolean;
  caseSensitive: boolean;
  enforceVowelLength: boolean;
  allowConsonantAssimilationAlternates: boolean;
  allowAlternativeWordOrderSOV: boolean;
  passingScorePercent: number;
}

export interface ExerciseItem {
  // Identity & Versioning
  exerciseId: string;
  version: string;
  status: 'draft' | 'validated' | 'active' | 'deprecated';
  checksumSha256: string;
  
  // Curriculum Linkage (Immutable Ground Truth)
  lessonId: string;
  unitId: string;
  sectionId: string;
  cefrLevel: CEFRLevel;
  exerciseModality: ExerciseModality;
  exerciseTaxonomy: ExerciseTaxonomyType;
  
  // Pedagogical Targets
  primarySkill: SkillTargetDomain;
  secondarySkills: SkillTargetDomain[];
  grammarTarget?: {
    ruleIdentifier: string;
    morphemeTarget: string;
    harmonicClass: 'masculine_back' | 'feminine_front' | 'neutral';
    pedagogicalSummary: string;
  };
  vocabularyTarget?: {
    productiveLemmas: string[];
    receptiveLemmas: string[];
    collocationsOrExpressions: string[];
  };
  objectiveReference: string;
  
  // Content & Interaction Payloads
  prompt: ExercisePromptPayload;
  answerSchema: ExerciseAnswerPayload;
  evaluationRules: ExerciseEvaluationRules;
  
  // Remediation & Pedagogy
  hints: ProgressiveHint[];
  detailedExplanations: {
    ruleCitation: string;
    primaryExplanation: string;
    etymologicalOrSociolinguisticNote?: string;
  };
  
  // Difficulty & Cognitive Calibrations
  difficulty: {
    cognitiveLevel: CognitiveLevel;
    estimatedSecondsToSolve: number;
    intrinsicComplexityRank: number; // 1 to 10
    distractorPlausibilityRating: number; // 0.0 to 1.0
  };
  
  // Audio Integration
  audio?: ExerciseAudioMetadata;
}

/**
 * Validator Result Signatures
 */
export interface ValidationIssue {
  code: string;
  severity: 'fatal' | 'warning' | 'advisory';
  message: string;
  fieldPath: string;
}

export interface ExerciseValidationReport {
  exerciseId: string;
  lessonId: string;
  isValid: boolean;
  issues: ValidationIssue[];
  validatedAt: string;
  validatorVersion: string;
}
