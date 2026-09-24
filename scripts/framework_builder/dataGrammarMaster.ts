import { GrammarConceptSpec, grammarA1Data } from './dataGrammar_A1';
import { grammarA2Data } from './dataGrammar_A2';
import { grammarB1B2Data } from './dataGrammar_B1_B2';
import { grammarC1C2Data } from './dataGrammar_C1_C2';
import { grammarExtensionsData } from './dataGrammar_Extensions';

export const allGrammarConcepts: GrammarConceptSpec[] = [
  ...grammarA1Data,
  ...grammarA2Data,
  ...grammarB1B2Data,
  ...grammarC1C2Data,
  ...grammarExtensionsData
];
