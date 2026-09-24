export interface RawLexiconItem {
  id: string;
  cyrillic: string;
  ipa: string;
  english: string;
  pos: 'noun' | 'verb' | 'adjective' | 'adverb' | 'pronoun' | 'numeral' | 'particle' | 'converb' | 'interjection' | 'idiom';
  cefr: 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';
  category: string;
  harmony: 'masculine' | 'feminine' | 'neutral';
  exampleCyrillic: string;
  exampleEnglish: string;
}

export interface RawGrammarConcept {
  id: string;
  title: string;
  cyrillicTitle: string;
  cefr: 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';
  category?: string;
  prerequisites?: string[];
  formula?: string;
  formationRules?: string[];
  summary: string;
  detailedExplanation?: string;
  vowelHarmonyNote?: string;
  commonMistakes?: string[];
  examples: {
    cyrillic: string;
    english: string;
    breakdown?: string;
  }[];
}

