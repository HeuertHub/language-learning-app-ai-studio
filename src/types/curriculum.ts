export type CEFRLevel = 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';

export type ExerciseType =
  | 'AUDIO_DICTATION'        // Listen to audio and transcribe in Cyrillic
  | 'AUDIO_COMPREHENSION'    // Listen to spoken Cyrillic dialogue/sentence and pick correct meaning
  | 'SENTENCE_CONSTRUCTION'  // Arrange word tokens into correct Mongolian SOV syntax
  | 'GRAMMAR_APPLICATION'    // Select or attach correct harmonic case or verbal suffix
  | 'TRANSLATION'            // Mongolian Cyrillic to English or English to Mongolian Cyrillic
  | 'PHONETIC_DISCRIMINATION'// Distinguish distinct phonemes (e.g., Ө vs Ү, Ц vs Ч)
  | 'VOCABULARY_MATCH';      // Match Mongolian term with definition

export interface ExerciseOption {
  id: string;
  text: string;
  cyrillic?: string;
  isCorrect: boolean;
  explanation?: string;
}

export interface Exercise {
  id: string;
  type: ExerciseType;
  prompt: string;
  audioText?: string;          // Cyrillic text to synthesize/pronounce
  slowAudioText?: string;
  cyrillicSentence?: string;   // Reference sentence in Cyrillic
  englishTranslation?: string; // English translation
  grammarPointId?: string;     // Reference to associated grammar rule
  options?: ExerciseOption[];  // For multiple choice / comprehension
  correctAnswer?: string;      // For text input / dictation
  wordTokens?: string[];       // For sentence building (scrambled tokens)
  correctTokenOrder?: string[];// Expected token order for sentence builder
  suffixOptions?: string[];    // E.g. ['-аас', '-ээс', '-оос', '-өөс']
  correctSuffix?: string;
  baseWord?: string;           // Root word to attach suffix to, e.g. 'гэр' -> 'гэрээс'
  detailedGrammarNote: string; // Scholarly pedagogical explanation shown upon answering
}

export interface VocabularyItem {
  id: string;
  cyrillic: string;
  ipa: string;
  english: string;
  partOfSpeech: 'noun' | 'verb' | 'adjective' | 'particle' | 'pronoun' | 'numeral' | 'postposition' | 'converb';
  genderHarmony: 'masculine' | 'feminine' | 'neutral';
  exampleSentenceCyrillic: string;
  exampleSentenceEnglish: string;
  notes?: string;
}

export interface GrammarRule {
  id: string;
  title: string;
  cyrillicTitle: string;
  summary: string;
  formula?: string;
  examples: {
    cyrillic: string;
    romanization?: string;
    english: string;
    breakdown: string;
  }[];
  explanation: string;
  exceptions?: string[];
}

export interface Lesson {
  id: string;
  title: string;
  cyrillicTitle: string;
  estimatedMinutes: number;
  grammarOverview: {
    summary: string;
    keyPoints: string[];
    rules: GrammarRule[];
  };
  vocabulary: VocabularyItem[];
  exercises: Exercise[];
}

export interface Unit {
  id: string;
  unitNumber: number;
  title: string;
  cyrillicTitle: string;
  description: string;
  cefrLevel: CEFRLevel;
  primaryGrammarTopic: string;
  lessons: Lesson[];
}

export interface LevelCurriculum {
  levelId: string;
  cefr: CEFRLevel;
  title: string;
  cyrillicTitle: string;
  description: string;
  targetCompetency: string;
  units: Unit[];
}

export interface LanguageCourse {
  id: string;
  name: string;
  cyrillicName: string;
  script: string;
  description: string;
  cefrRange: string;
  totalLevels: number;
  levels: LevelCurriculum[];
  masterGrammarReference: GrammarRule[];
}

export interface CourseCompletionStats {
  courseId: string;
  userId: string;
  completedLessonIds: string[];
  completedUnitIds: string[];
  masteredVocabCount: number;
  totalExercisesAttempted: number;
  totalExercisesCorrect: number;
  timeSpentMinutes: number;
  lastStudiedAt: string;
}

export interface UserStudyNote {
  id: string;
  userId: string;
  title: string;
  cyrillicSnippet?: string;
  content: string;
  tags: string[];
  createdAt: string;
  updatedAt?: string;
}
