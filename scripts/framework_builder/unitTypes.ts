export interface ReadingTargetSpec {
  genre: string;
  textLengthWords: string;
  targetSkills: string[];
}

export interface ListeningTargetSpec {
  genre: string;
  speechRate: string;
  audioSuitability: "standard_speech_synthesis_acceptable" | "mongolian_voice_required" | "native_speaker_preferred" | "native_speaker_required" | "standard_speech_synthesis" | "mongolian_speech_synthesis_only";
  targetSkills: string[];
}

export interface WritingTargetSpec {
  genre: string;
  targetLength: string;
  targetSkills: string[];
}

export interface SpokenProductionTargetSpec {
  genre: string;
  targetTask: string;
  targetSkills: string[];
}

export interface CulturalContextSpec {
  title: string;
  scopingMetadata: string;
  integrationDetails: string;
}

export interface LexicalBreakdownSpec {
  domainSpecificLemmas: number;
  generalPurposeLemmas: number;
  multiwordExpressions: number;
}

export interface UnitSpec {
  unitId: string;
  sectionId: string;
  cefrLevel: "Pre-A1" | "A1" | "A2" | "B1" | "B2" | "C1" | "C2";
  sequencePosition: number;
  title: string;
  communicativeTheme: string;
  primaryLearningPurpose: string;
  primaryCompetencyIds: string[];
  secondaryReviewCompetencyIds: string[];
  grammarIntroduced: string[];
  grammarReinforced: string[];
  phonologyTargets: string[];
  communicativeFunctions: string[];
  lexicalDomains: string[];
  newProductiveCoreLemmas: number;
  newReceptiveCoreLemmas: number;
  newProductiveExpressions: number;
  newReceptiveExpressions: number;
  estimatedNewCoreLemmas: number;
  estimatedNewMultiwordExpressions: number;
  lexicalBreakdown: LexicalBreakdownSpec;
  readingTarget: ReadingTargetSpec;
  listeningTarget: ListeningTargetSpec;
  writingTarget: WritingTargetSpec;
  spokenProductionTarget: SpokenProductionTargetSpec;
  registerTarget: string;
  culturalContext: CulturalContextSpec;
  prerequisiteUnitIds: string[];
  reviewOfUnitIds: string[];
  futureDependencyHints: string[];
  unitOutcome: string;
}
