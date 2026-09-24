export interface LessonBlueprint {
  lessonId: string;
  unitId: string;
  cefrLevel: string;
  sequenceWithinUnit: number;
  title: string;
  lessonType: string;
  primaryPurpose: string;
  communicativeOutcome: string;

  objectivesIntroduced: string[];
  objectivesPracticed: string[];
  objectivesReviewed: string[];

  grammarIntroduced: string[];
  grammarPracticed: string[];
  grammarReviewed: string[];
  grammarReinforced?: string[];

  phonologyIntroduced: string[];
  phonologyPracticed: string[];
  phonologyReviewed: string[];

  communicativeFunctionsIntroduced: string[];
  communicativeFunctionsPracticed: string[];
  communicativeFunctionsReviewed: string[];

  newProductiveLemmaTarget: number;
  newReceptiveLemmaTarget: number;
  newProductiveExpressionTarget: number;
  newReceptiveExpressionTarget: number;
  lexicalDomains: string[];
  previousVocabularyReused: string[];

  readingObjective: string;
  listeningObjective: string;
  writingObjective: string;
  spokenProductionObjective: string;

  registerTarget: string;
  pragmaticTarget: string;

  prerequisiteLessonIds: string[];
  reviewsLessonIds: string[];
  reviewsUnitIds: string[];
  reviewReason: string;

  audioSuitability: string;
  audioPurpose: string;

  successCriteria: string[];
  masteryEvidence: string;

  recommendedExerciseModalities: string[];
}
