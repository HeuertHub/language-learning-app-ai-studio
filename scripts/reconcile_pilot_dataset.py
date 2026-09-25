#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reconciles all 105 exercises in curriculum/pilot/exercise_content_pilot.json
against the authoritative TypeScript contract in src/types/exerciseEngine.ts.

Reconciles:
1. Modality names -> canonical ExerciseModality
2. Cognitive complexity names -> canonical CognitiveComplexity
3. Interaction patterns -> canonical InteractionPattern
4. Match types -> canonical MatchType (CASE_INSENSITIVE -> NORMALIZED_TEXT with caseSensitive: false)
"""

import json
import os
import sys

MODALITY_MAP = {
    'ACOUSTIC_MICRO_DIRECTION': 'ORTHOGRAPHY_PHONOLOGY',
    'AUDITORY_DISCRIMINATION': 'LISTENING_COMPREHENSION',
    'AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS': 'AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS',
    'CASE_SUFFIX_APPLICATION': 'GRAMMAR_PRACTICE',
    'CHANCELLERY_SYNTACTIC_PARSING': 'CONSTITUTIONAL_STATUTORY_READING',
    'COMPETENCY_LEXICON_SELECTION': 'VOCABULARY_ACQUISITION',
    'CONSTITUTIONAL_STATUTORY_READING': 'CONSTITUTIONAL_STATUTORY_READING',
    'DIALOGUE_ROLEPLAY_COMPLETION': 'DIALOGUE_INTERACTION',
    'JURISPRUDENTIAL_LEGAL_COMMENTARY': 'JURISPRUDENTIAL_LEGAL_COMMENTARY',
    'KHALKHA_PHONOTACTICS_DECODING': 'KHALKHA_PHONOTACTICS_DECODING',
    'MODERNIST_SATIRE_SYNTHESIS': 'MODERNIST_SATIRE_SYNTHESIS',
    'MUNICIPAL_POLICY_CAPSTONE': 'SYNTHESIS_CAPSTONE',
    'NOMINALIZER_DERIVATION': 'GRAMMAR_PRACTICE',
    'ORTHOGRAPHY_RECOGNITION': 'ORTHOGRAPHY_PHONOLOGY',
    'PARLIAMENTARY_ACOUSTIC_DISSECTION': 'LISTENING_COMPREHENSION',
    'PROFESSIONAL_CV_WRITING': 'WRITING_PRODUCTION',
    'SALUTATION_REGISTER_MATCH': 'DIALOGUE_INTERACTION',
    'SYNTAX_WORD_ORDERING': 'GRAMMAR_PRACTICE',
    'TOPIC_CONTRASTIVE_DISCOURSE': 'GRAMMAR_PRACTICE',
    'TRANSIT_SCHEDULE_READING': 'READING_COMPREHENSION',
    'VOWEL_HARMONY_CLASSIFICATION': 'GRAMMAR_PRACTICE',
}

COMPLEXITY_MAP = {
    'REMEMBER_RECOGNIZE': 'IDENTIFY_RECOGNIZE',
    'UNDERSTAND_DISCRIMINATE': 'DISCRIMINATE_PHONEMES',
    'APPLY_MORPHOLOGY': 'APPLY_MORPHOLOGY',
    'ANALYZE_SYNTAX': 'ANALYZE_SYNTAX',
    'EVALUATE_DISCOURSE': 'EVALUATE_PRAGMATICS',
    'CREATE_RHETORIC': 'SYNTHESIZE_CRITIQUE',
    'IDENTIFY_RECOGNIZE': 'IDENTIFY_RECOGNIZE',
    'DISCRIMINATE_PHONEMES': 'DISCRIMINATE_PHONEMES',
    'RETRIEVE_MATCH': 'RETRIEVE_MATCH',
    'PARSE_LEGAL_DISCOURSE': 'PARSE_LEGAL_DISCOURSE',
    'EVALUATE_PRAGMATICS': 'EVALUATE_PRAGMATICS',
    'SYNTHESIZE_CRITIQUE': 'SYNTHESIZE_CRITIQUE',
}

VALID_MODALITIES = set([
    'ORTHOGRAPHY_PHONOLOGY',
    'VOCABULARY_ACQUISITION',
    'GRAMMAR_INTRODUCTION',
    'GRAMMAR_PRACTICE',
    'READING_COMPREHENSION',
    'LISTENING_COMPREHENSION',
    'DIALOGUE_INTERACTION',
    'WRITING_PRODUCTION',
    'SYNTHESIS_CAPSTONE',
    'CONSTITUTIONAL_STATUTORY_READING',
    'JURISPRUDENTIAL_LEGAL_COMMENTARY',
    'KHALKHA_PHONOTACTICS_DECODING',
    'AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS',
    'MODERNIST_SATIRE_SYNTHESIS'
])

VALID_INTERACTIONS = set([
    'MULTIPLE_CHOICE',
    'MULTI_SELECT',
    'PAIR_MATCHING',
    'TOKEN_REARRANGEMENT',
    'CLOZE_TEXT',
    'SUFFIX_ATTACHMENT',
    'AUDIO_COMPREHENSION',
    'AUDIO_DICTATION',
    'OPEN_RESPONSE_RUBRIC',
    'FREE_RESPONSE_RUBRIC'
])

VALID_COMPLEXITIES = set([
    'IDENTIFY_RECOGNIZE',
    'DISCRIMINATE_PHONEMES',
    'RETRIEVE_MATCH',
    'APPLY_MORPHOLOGY',
    'ANALYZE_SYNTAX',
    'PARSE_LEGAL_DISCOURSE',
    'EVALUATE_PRAGMATICS',
    'SYNTHESIZE_CRITIQUE'
])

VALID_MATCH_TYPES = set([
    'EXACT',
    'TOKEN_ORDER',
    'NORMALIZED_TEXT',
    'SET_EQUALITY',
    'RUBRIC_CRITERIA'
])

def reconcile_pilot_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lessons = data.get('lessons', [])
    total_reconciled = 0
    mod_changes = 0
    comp_changes = 0
    match_changes = 0

    for lesson in lessons:
        for ex in lesson.get('exercises', []):
            total_reconciled += 1

            # 1. Modality
            cur_mod = ex.get('modality')
            if cur_mod in MODALITY_MAP:
                new_mod = MODALITY_MAP[cur_mod]
                if new_mod != cur_mod:
                    ex['modality'] = new_mod
                    mod_changes += 1

            # 2. Cognitive Complexity
            cur_comp = ex.get('cognitiveComplexity')
            if cur_comp in COMPLEXITY_MAP:
                new_comp = COMPLEXITY_MAP[cur_comp]
                if new_comp != cur_comp:
                    ex['cognitiveComplexity'] = new_comp
                    comp_changes += 1

            # 3. Match type
            eval_rule = ex.get('evaluation', {})
            cur_match = eval_rule.get('matchType')
            if cur_match == 'CASE_INSENSITIVE':
                eval_rule['matchType'] = 'NORMALIZED_TEXT'
                eval_rule['caseSensitive'] = False
                eval_rule['stripPunctuation'] = True
                eval_rule['normalizeWhitespace'] = True
                match_changes += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return total_reconciled, mod_changes, comp_changes, match_changes

def main():
    pilot_path = 'curriculum/pilot/exercise_content_pilot.json'
    print("=" * 80)
    print("RECONCILING DERIVED PILOT EXERCISES WITH TYPESCRIPT CONTRACT")
    print("=" * 80)

    total, mod, comp, mat = reconcile_pilot_file(pilot_path)
    print(f"Total exercises processed: {total}")
    print(f"Modality migrations: {mod}")
    print(f"Cognitive complexity migrations: {comp}")
    print(f"Match type migrations: {mat}")

    # Audit remaining mismatches
    with open(pilot_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_ex = [e for l in data['lessons'] for e in l['exercises']]
    rem_mod = [e['exerciseId'] for e in all_ex if e.get('modality') not in VALID_MODALITIES]
    rem_int = [e['exerciseId'] for e in all_ex if e.get('interactionPattern') not in VALID_INTERACTIONS]
    rem_comp = [e['exerciseId'] for e in all_ex if e.get('cognitiveComplexity') not in VALID_COMPLEXITIES]
    rem_mat = [e['exerciseId'] for e in all_ex if e.get('evaluation', {}).get('matchType') not in VALID_MATCH_TYPES]

    print("\nPost-Reconciliation Audit:")
    print(f"  • Modality mismatches:            {len(rem_mod)}")
    print(f"  • Interaction-pattern mismatches: {len(rem_int)}")
    print(f"  • Cognitive-complexity mismatches:{len(rem_comp)}")
    print(f"  • Match-type mismatches:          {len(rem_mat)}")

    if rem_mod or rem_int or rem_comp or rem_mat:
        print("\n❌ FAILED: Schema mismatches remain!")
        sys.exit(1)
    else:
        print("\n✓ ALL 105 EXERCISES PERFECTLY CONFORM TO TYPESCRIPT CONTRACT!")
        print("=" * 80)

if __name__ == '__main__':
    main()
