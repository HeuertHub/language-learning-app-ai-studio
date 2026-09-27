/**
 * Authoritative Lexicon Contract for Mongolian Language Curriculum
 * Phase 3C.0R Lexicon Integrity Reset & Authenticity Pilot
 */

export type LexicalLifecycleStatus =
  | 'PLACEHOLDER_INVALID'
  | 'UNREALIZED'
  | 'DRAFT_UNVERIFIED'
  | 'SOURCE_VERIFIED'
  | 'LINGUISTICALLY_REVIEWED';

export type LexicalClassification = 'productive' | 'receptive';

export type LexicalRegister =
  | 'neutral'
  | 'formal'
  | 'informal'
  | 'literary'
  | 'archaic'
  | 'colloquial'
  | 'administrative'
  | 'legal'
  | 'academic'
  | 'marked';

export type ExpressionType =
  | 'formulaic_language'
  | 'collocation'
  | 'idiomatic_expression'
  | 'discourse_formula'
  | 'pragmatic_routine'
  | 'institutional_terminology';

export interface VerificationDimensions {
  orthographicForm: boolean;
  lexicalExistence: boolean;
  englishGloss: boolean;
  partOfSpeech: boolean;
  register: boolean;
  expressionNaturalness?: boolean;
  lessonSuitability: boolean;
}

export interface LexiconSourceProvenance {
  sourceType:
    | 'STANDARD_DICTIONARY'
    | 'ACADEMIC_GRAMMAR'
    | 'CONTEMPORARY_CORPUS'
    | 'EDUCATIONAL_STANDARDS'
    | 'CURRICULUM_BLUEPRINT';
  sourceName: string;
  sourceReference: string;
  searchedHeadword: string;
  sourceLocator?: string;
  verificationResult: 'VERIFIED' | 'UNVERIFIED' | 'PARTIALLY_VERIFIED';
  verifiedDimensions: VerificationDimensions;
  sourceNotes?: string;
  verificationMethod:
    | 'LEXICOGRAPHIC_CROSS_CHECK'
    | 'CORPUS_ATTESTATION'
    | 'CURRICULUM_BLUEPRINT_AUDIT'
    | 'MANUAL_EXPERT_REVIEW';
  verifiedAt?: string;
}

export interface ExpressionConstituent {
  token: string;
  rootLemma: string;
  resolvedLemmaId?: string;
  inflectionalSuffixes?: string[];
  isUnresolved?: boolean;
  notes?: string;
}

export interface LexicalLemmaMorphology {
  vowelHarmony?: 'masculine' | 'feminine' | 'neutral';
  stemType?: string;
  irregularity?: string;
}

export interface LexicalLemma {
  id: string; // e.g., 'lex_mn_lemma_00001'
  lemma: string; // Canonical Cyrillic lemma form (empty string if UNREALIZED)
  gloss: string; // Accurate English translation (empty string if UNREALIZED)
  pos: string;
  cefrLevel: string;
  firstIntroducedUnitId: string;
  firstIntroducedLessonId: string;
  classification: LexicalClassification;
  domains: string[];
  register: LexicalRegister;
  usageNotes?: string;
  morphology?: LexicalLemmaMorphology;
  senseIndex?: number;
  status: LexicalLifecycleStatus;
  provenance?: LexiconSourceProvenance;
}

export interface LexicalExpression {
  id: string; // e.g., 'lex_mn_expr_00001'
  expression: string; // Canonical Cyrillic multiword unit (empty string if UNREALIZED)
  gloss: string; // Natural English translation (empty string if UNREALIZED)
  expressionType: ExpressionType;
  cefrLevel: string;
  firstIntroducedUnitId: string;
  firstIntroducedLessonId: string;
  classification: LexicalClassification;
  domains: string[];
  register: LexicalRegister;
  constituentLemmaIds: string[];
  constituentBreakdown?: ExpressionConstituent[];
  usageNotes?: string;
  status: LexicalLifecycleStatus;
  provenance?: LexiconSourceProvenance;
}

export interface LessonLexiconLookupEntry {
  lessonId: string;
  unitId: string;
  cefrLevel: string;
  productiveLemmaIds: string[];
  receptiveLemmaIds: string[];
  productiveExpressionIds: string[];
  receptiveExpressionIds: string[];
  previousVocabularyReused: string[];
}

export interface LexiconManifestSummary {
  totalCoreLemmas: number;
  totalProductiveLemmas: number;
  totalReceptiveLemmas: number;
  totalExpressions: number;
  totalProductiveExpressions: number;
  totalReceptiveExpressions: number;
  realizedLemmasCount: number;
  realizedExpressionsCount: number;
  unrealizedLemmasCount: number;
  unrealizedExpressionsCount: number;
  lessonsReconciled: number;
  reconciliationRate: number;
  levels: string[];
}

export interface LexiconManifest {
  manifestVersion: string;
  generatedAt: string;
  phase: string;
  summary: LexiconManifestSummary;
  byLevel: Record<
    string,
    {
      lemmas: number;
      productiveLemmas: number;
      receptiveLemmas: number;
      expressions: number;
      productiveExpressions: number;
      receptiveExpressions: number;
      realizedLemmas: number;
      realizedExpressions: number;
      unrealizedLemmas: number;
      unrealizedExpressions: number;
    }
  >;
  pilotScope: {
    preA1: {
      units: number;
      lessons: number;
      realizedLemmas: number;
      realizedExpressions: number;
    };
    a1PilotUnits: {
      units: number;
      lessons: number;
      realizedLemmas: number;
      realizedExpressions: number;
    };
  };
}
