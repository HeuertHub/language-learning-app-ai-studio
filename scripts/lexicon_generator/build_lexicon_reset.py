#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1A Evidence-Backed Authoritative Lexicon Builder (Pilot + Batch 1)
Constructs the authoritative lexical dataset:
- Preserves all 9,441 stable lemma IDs and 2,692 stable expression IDs
- Realizes 286 authentic pilot lemmas and 77 authentic pilot expressions (Pre-A1 + A1 Units 16-20)
- Realizes 117 authentic Batch 1 lemmas and 33 authentic Batch 1 expressions (A1 Units 21-25)
- Sets all non-pilot/non-batch slots to status UNREALIZED with NO synthetic strings
- Links constituent lemmas semantically based on actual expression tokens
- Populates genuine lexicographic provenance
"""

import json
import os
import sys
import re
from datetime import datetime, timezone
from collections import defaultdict

LEVEL_ORDER = [
    ('preA1', 'Pre-A1'),
    ('a1_complete', 'A1'),
    ('a2_complete', 'A2'),
    ('b1_complete', 'B1'),
    ('b2_complete', 'B2'),
    ('c1_complete', 'C1'),
    ('c2_complete', 'C2')
]

A1_PILOT_UNITS = set([
    'unit_a1_16_standard_salutations_time_of_day_gr',
    'unit_a1_17_personal_pronouns_direct_address_pr',
    'unit_a1_18_zero_copula_identity_origin_predica',
    'unit_a1_19_polar_inquiries_polar_question_part',
    'unit_a1_20_demonstrative_deixis_'
])

A1_BATCH1_UNITS = set([
    'unit_a1_21_negative_nominal_assertion_the_copu',
    'unit_a1_22_formal_departure_social_gratitude_f',
    'unit_a1_23_section_synthesis_social_reception_',
    'unit_a1_24_existential_assertion_vs_',
    'unit_a1_25_dative_locative_spatial_anchoring_s'
])

def load_frozen_lessons(root_dir):
    all_lessons = []
    for file_key, lvl_name in LEVEL_ORDER:
        fpath = os.path.join(root_dir, 'curriculum', 'lesson_blueprints', f'{file_key}.json')
        with open(fpath, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            all_lessons.extend(data)
    return all_lessons

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)

    from scripts.lexicon_generator.pilot_authentic_data import PILOT_LEMMAS, PILOT_EXPRESSIONS
    from scripts.lexicon_generator.pilot_provenance_data import (
        get_lemma_provenance_and_status,
        get_expression_provenance_and_status
    )
    from scripts.lexicon_generator.pilot_constituent_data import CONSTITUENT_ANALYSIS

    from scripts.lexicon_generator.batch1_authentic_data import BATCH1_LEMMAS, BATCH1_EXPRESSIONS
    from scripts.lexicon_generator.batch1_provenance_data import (
        get_batch1_lemma_provenance_and_status,
        get_batch1_expression_provenance_and_status
    )
    from scripts.lexicon_generator.batch1_constituent_data import BATCH1_CONSTITUENT_ANALYSIS

    print("=" * 80)
    print("PHASE 3C.1A EVIDENCE-BACKED AUTHORITATIVE LEXICON BUILDER (PILOT + BATCH 1)")
    print("=" * 80)

    lessons = load_frozen_lessons(root_dir)
    print(f"Loaded {len(lessons)} frozen lessons across 7 CEFR levels.")

    # 1. Prepare stable slots
    lemma_slots = []
    expr_slots = []

    lemma_counter = 0
    expr_counter = 0

    pilot_lemma_lookup_by_text = {} # text -> id

    # Pass 1: Allocate all 9,441 lemma slots and 2,692 expression slots
    for l in lessons:
        lid = l['lessonId']
        uid = l['unitId']
        lvl = l['cefrLevel']
        domains = l.get('lexicalDomains', ['lex_domain_general'])

        pl_target = l.get('newProductiveLemmaTarget', 0)
        rl_target = l.get('newReceptiveLemmaTarget', 0)
        pe_target = l.get('newProductiveExpressionTarget', 0)
        re_target = l.get('newReceptiveExpressionTarget', 0)

        is_pilot = (lvl == 'Pre-A1') or (lvl == 'A1' and uid in A1_PILOT_UNITS)
        is_batch1 = (lvl == 'A1' and uid in A1_BATCH1_UNITS)

        # Allocate productive lemmas
        for idx in range(pl_target):
            lemma_counter += 1
            lem_id = f"lex_mn_lemma_{lemma_counter:05d}"
            lemma_slots.append({
                'id': lem_id,
                'cefrLevel': lvl,
                'firstIntroducedUnitId': uid,
                'firstIntroducedLessonId': lid,
                'classification': 'productive',
                'domains': domains,
                'is_pilot': is_pilot,
                'is_batch1': is_batch1,
                'role': 'productive'
            })

        # Allocate receptive lemmas
        for idx in range(rl_target):
            lemma_counter += 1
            lem_id = f"lex_mn_lemma_{lemma_counter:05d}"
            lemma_slots.append({
                'id': lem_id,
                'cefrLevel': lvl,
                'firstIntroducedUnitId': uid,
                'firstIntroducedLessonId': lid,
                'classification': 'receptive',
                'domains': domains,
                'is_pilot': is_pilot,
                'is_batch1': is_batch1,
                'role': 'receptive'
            })

        # Allocate productive expressions
        for idx in range(pe_target):
            expr_counter += 1
            expr_id = f"lex_mn_expr_{expr_counter:05d}"
            expr_slots.append({
                'id': expr_id,
                'cefrLevel': lvl,
                'firstIntroducedUnitId': uid,
                'firstIntroducedLessonId': lid,
                'classification': 'productive',
                'domains': domains,
                'is_pilot': is_pilot,
                'is_batch1': is_batch1,
                'role': 'productive'
            })

        # Allocate receptive expressions
        for idx in range(re_target):
            expr_counter += 1
            expr_id = f"lex_mn_expr_{expr_counter:05d}"
            expr_slots.append({
                'id': expr_id,
                'cefrLevel': lvl,
                'firstIntroducedUnitId': uid,
                'firstIntroducedLessonId': lid,
                'classification': 'receptive',
                'domains': domains,
                'is_pilot': is_pilot,
                'is_batch1': is_batch1,
                'role': 'receptive'
            })

    print(f"Total stable lemma slots: {len(lemma_slots)} (Target: 9441)")
    print(f"Total stable expression slots: {len(expr_slots)} (Target: 2692)")
    assert len(lemma_slots) == 9441
    assert len(expr_slots) == 2692

    # 2. Realize Pilot & Batch 1 Lemmas
    realized_lemmas = []
    pilot_lemma_idx = 0
    batch1_lemma_idx = 0

    for slot in lemma_slots:
        lid = slot['firstIntroducedLessonId']
        if slot['is_pilot']:
            cyr_lemma, gloss, pos, reg, v_harmony, s_type, prov_type, usage_notes, sense_idx = PILOT_LEMMAS[pilot_lemma_idx]
            prov, st = get_lemma_provenance_and_status(pilot_lemma_idx, cyr_lemma, pos, lid)

            record = {
                "id": slot['id'],
                "lemma": cyr_lemma,
                "gloss": gloss,
                "pos": pos,
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": lid,
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": reg,
                "usageNotes": usage_notes,
                "morphology": {
                    "vowelHarmony": v_harmony,
                    "stemType": s_type,
                    "irregularity": "regular"
                },
                "senseIndex": sense_idx,
                "status": st,
                "provenance": prov
            }
            pilot_lemma_lookup_by_text[cyr_lemma] = slot['id']
            pilot_lemma_idx += 1
        elif slot['is_batch1']:
            cyr_lemma, gloss, pos, reg, v_harmony, s_type, prov_type, usage_notes, sense_idx = BATCH1_LEMMAS[batch1_lemma_idx]
            prov, st = get_batch1_lemma_provenance_and_status(batch1_lemma_idx, cyr_lemma, pos, lid)

            record = {
                "id": slot['id'],
                "lemma": cyr_lemma,
                "gloss": gloss,
                "pos": pos,
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": lid,
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": reg,
                "usageNotes": usage_notes,
                "morphology": {
                    "vowelHarmony": v_harmony,
                    "stemType": s_type,
                    "irregularity": "regular"
                },
                "senseIndex": sense_idx,
                "status": st,
                "provenance": prov
            }
            batch1_lemma_idx += 1
        else:
            record = {
                "id": slot['id'],
                "lemma": "",
                "gloss": "",
                "pos": "",
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": slot['firstIntroducedLessonId'],
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": "neutral",
                "status": "UNREALIZED"
            }
        realized_lemmas.append(record)

    # 3. Realize Pilot & Batch 1 Expressions
    realized_expressions = []
    pilot_expr_idx = 0
    batch1_expr_idx = 0

    for slot in expr_slots:
        lid = slot['firstIntroducedLessonId']
        if slot['is_pilot']:
            cyr_expr, gloss, exp_type, reg, constituent_indices, usage_notes = PILOT_EXPRESSIONS[pilot_expr_idx]
            prov, st = get_expression_provenance_and_status(pilot_expr_idx, cyr_expr, exp_type, lid)

            analysis = CONSTITUENT_ANALYSIS.get(pilot_expr_idx, [])
            constituent_ids = [c['resolvedLemmaId'] for c in analysis if c.get('resolvedLemmaId')]

            record = {
                "id": slot['id'],
                "expression": cyr_expr,
                "gloss": gloss,
                "expressionType": exp_type,
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": lid,
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": reg,
                "constituentLemmaIds": constituent_ids,
                "usageNotes": usage_notes,
                "status": st,
                "provenance": prov
            }
            pilot_expr_idx += 1
        elif slot['is_batch1']:
            cyr_expr, gloss, exp_type, reg, constituent_indices, usage_notes = BATCH1_EXPRESSIONS[batch1_expr_idx]
            prov, st = get_batch1_expression_provenance_and_status(batch1_expr_idx, cyr_expr, exp_type, lid)

            analysis = BATCH1_CONSTITUENT_ANALYSIS.get(batch1_expr_idx, [])
            constituent_ids = [c['resolvedLemmaId'] for c in analysis if c.get('resolvedLemmaId')]

            record = {
                "id": slot['id'],
                "expression": cyr_expr,
                "gloss": gloss,
                "expressionType": exp_type,
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": lid,
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": reg,
                "constituentLemmaIds": constituent_ids,
                "usageNotes": usage_notes,
                "status": st,
                "provenance": prov
            }
            batch1_expr_idx += 1
        else:
            record = {
                "id": slot['id'],
                "expression": "",
                "gloss": "",
                "expressionType": "collocation",
                "cefrLevel": slot['cefrLevel'],
                "firstIntroducedUnitId": slot['firstIntroducedUnitId'],
                "firstIntroducedLessonId": slot['firstIntroducedLessonId'],
                "classification": slot['classification'],
                "domains": slot['domains'],
                "register": "neutral",
                "constituentLemmaIds": [],
                "status": "UNREALIZED"
            }
        realized_expressions.append(record)

    # 4. Build Lesson Lexicon Map
    lesson_lexicon_map = {}
    for l in lessons:
        lid = l['lessonId']
        l_lemmas = [x for x in realized_lemmas if x['firstIntroducedLessonId'] == lid]
        l_exprs = [x for x in realized_expressions if x['firstIntroducedLessonId'] == lid]

        lesson_lexicon_map[lid] = {
            "lessonId": lid,
            "unitId": l['unitId'],
            "cefrLevel": l['cefrLevel'],
            "productiveLemmaIds": [x["id"] for x in l_lemmas if x['classification'] == 'productive'],
            "receptiveLemmaIds": [x["id"] for x in l_lemmas if x['classification'] == 'receptive'],
            "productiveExpressionIds": [x["id"] for x in l_exprs if x['classification'] == 'productive'],
            "receptiveExpressionIds": [x["id"] for x in l_exprs if x['classification'] == 'receptive'],
            "previousVocabularyReused": l.get("previousVocabularyReused", [])
        }

    # Summary counts
    total_realized_lemmas = sum(1 for x in realized_lemmas if x['status'] in ['LINGUISTICALLY_REVIEWED', 'SOURCE_VERIFIED', 'DRAFT_UNVERIFIED'])
    total_unrealized_lemmas = sum(1 for x in realized_lemmas if x['status'] == 'UNREALIZED')
    total_realized_exprs = sum(1 for x in realized_expressions if x['status'] in ['LINGUISTICALLY_REVIEWED', 'SOURCE_VERIFIED', 'DRAFT_UNVERIFIED'])
    total_unrealized_exprs = sum(1 for x in realized_expressions if x['status'] == 'UNREALIZED')

    sv_lemmas = sum(1 for x in realized_lemmas if x['status'] == 'SOURCE_VERIFIED')
    lr_lemmas = sum(1 for x in realized_lemmas if x['status'] == 'LINGUISTICALLY_REVIEWED')
    du_lemmas = sum(1 for x in realized_lemmas if x['status'] == 'DRAFT_UNVERIFIED')

    sv_exprs = sum(1 for x in realized_expressions if x['status'] == 'SOURCE_VERIFIED')
    lr_exprs = sum(1 for x in realized_expressions if x['status'] == 'LINGUISTICALLY_REVIEWED')
    du_exprs = sum(1 for x in realized_expressions if x['status'] == 'DRAFT_UNVERIFIED')

    print(f"\nRealization Summary:")
    print(f"  • Realized Lemmas:   {total_realized_lemmas} (Pre-A1: 168, A1 Units 16-20: 118, A1 Units 21-25: 117)")
    print(f"    - SOURCE_VERIFIED:         {sv_lemmas}")
    print(f"    - LINGUISTICALLY_REVIEWED: {lr_lemmas}")
    print(f"    - DRAFT_UNVERIFIED:        {du_lemmas}")
    print(f"  • Unrealized Lemmas: {total_unrealized_lemmas}")
    print(f"  • Realized Exprs:    {total_realized_exprs} (Pre-A1: 47, A1 Units 16-20: 30, A1 Units 21-25: 33)")
    print(f"    - SOURCE_VERIFIED:         {sv_exprs}")
    print(f"    - LINGUISTICALLY_REVIEWED: {lr_exprs}")
    print(f"    - DRAFT_UNVERIFIED:        {du_exprs}")
    print(f"  • Unrealized Exprs:  {total_unrealized_exprs}")

    assert total_realized_lemmas == 286 + 117
    assert total_realized_exprs == 77 + 33
    assert total_unrealized_lemmas == 9441 - (286 + 117)
    assert total_unrealized_exprs == 2692 - (77 + 33)

    # 5. Write Modular Source Files in curriculum/lexicon/
    lexicon_dir = os.path.join(root_dir, 'curriculum', 'lexicon')
    os.makedirs(os.path.join(lexicon_dir, 'lemmas'), exist_ok=True)
    os.makedirs(os.path.join(lexicon_dir, 'expressions'), exist_ok=True)
    os.makedirs(os.path.join(lexicon_dir, 'indexes'), exist_ok=True)

    lemmas_by_level = defaultdict(list)
    exprs_by_level = defaultdict(list)
    for lem in realized_lemmas:
        lemmas_by_level[lem['cefrLevel']].append(lem)
    for exp in realized_expressions:
        exprs_by_level[exp['cefrLevel']].append(exp)

    for file_key, lvl_name in LEVEL_ORDER:
        lem_file = os.path.join(lexicon_dir, 'lemmas', f"lemmas_{file_key}.json")
        with open(lem_file, 'w', encoding='utf-8') as fp:
            json.dump(lemmas_by_level[lvl_name], fp, ensure_ascii=False, indent=2)

        exp_file = os.path.join(lexicon_dir, 'expressions', f"expressions_{file_key}.json")
        with open(exp_file, 'w', encoding='utf-8') as fp:
            json.dump(exprs_by_level[lvl_name], fp, ensure_ascii=False, indent=2)

    # Indexes
    lemma_index = {l['id']: l for l in realized_lemmas}
    expr_index = {e['id']: e for e in realized_expressions}

    with open(os.path.join(lexicon_dir, 'indexes', 'lemma_index.json'), 'w', encoding='utf-8') as fp:
        json.dump(lemma_index, fp, ensure_ascii=False, indent=2)
    with open(os.path.join(lexicon_dir, 'indexes', 'expression_index.json'), 'w', encoding='utf-8') as fp:
        json.dump(expr_index, fp, ensure_ascii=False, indent=2)
    with open(os.path.join(lexicon_dir, 'indexes', 'lesson_lexicon_map.json'), 'w', encoding='utf-8') as fp:
        json.dump(lesson_lexicon_map, fp, ensure_ascii=False, indent=2)

    print("✓ Modular source files and indexes written successfully.")

    # 6. Compile Runtime Assets in public/data/lexicon/
    runtime_dir = os.path.join(root_dir, 'public', 'data', 'lexicon')
    os.makedirs(runtime_dir, exist_ok=True)

    manifest_data = {
        "manifestVersion": "1.1.0-batch1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "phase": "3C.1A",
        "summary": {
            "totalCoreLemmas": len(realized_lemmas),
            "totalProductiveLemmas": sum(1 for x in realized_lemmas if x['classification'] == 'productive'),
            "totalReceptiveLemmas": sum(1 for x in realized_lemmas if x['classification'] == 'receptive'),
            "totalExpressions": len(realized_expressions),
            "totalProductiveExpressions": sum(1 for x in realized_expressions if x['classification'] == 'productive'),
            "totalReceptiveExpressions": sum(1 for x in realized_expressions if x['classification'] == 'receptive'),
            "realizedLemmasCount": total_realized_lemmas,
            "realizedExpressionsCount": total_realized_exprs,
            "unrealizedLemmasCount": total_unrealized_lemmas,
            "unrealizedExpressionsCount": total_unrealized_exprs,
            "lessonsReconciled": len(lesson_lexicon_map),
            "reconciliationRate": 1.0,
            "levels": [lvl for _, lvl in LEVEL_ORDER]
        },
        "byLevel": {
            lvl: {
                "lemmas": len(lemmas_by_level[lvl]),
                "productiveLemmas": sum(1 for x in lemmas_by_level[lvl] if x['classification'] == 'productive'),
                "receptiveLemmas": sum(1 for x in lemmas_by_level[lvl] if x['classification'] == 'receptive'),
                "expressions": len(exprs_by_level[lvl]),
                "productiveExpressions": sum(1 for x in exprs_by_level[lvl] if x['classification'] == 'productive'),
                "receptiveExpressions": sum(1 for x in exprs_by_level[lvl] if x['classification'] == 'receptive'),
                "realizedLemmas": sum(1 for x in lemmas_by_level[lvl] if x['status'] in ['LINGUISTICALLY_REVIEWED', 'SOURCE_VERIFIED', 'DRAFT_UNVERIFIED']),
                "realizedExpressions": sum(1 for x in exprs_by_level[lvl] if x['status'] in ['LINGUISTICALLY_REVIEWED', 'SOURCE_VERIFIED', 'DRAFT_UNVERIFIED']),
                "sourceVerifiedLemmas": sum(1 for x in lemmas_by_level[lvl] if x['status'] == 'SOURCE_VERIFIED'),
                "linguisticallyReviewedLemmas": sum(1 for x in lemmas_by_level[lvl] if x['status'] == 'LINGUISTICALLY_REVIEWED'),
                "draftUnverifiedLemmas": sum(1 for x in lemmas_by_level[lvl] if x['status'] == 'DRAFT_UNVERIFIED'),
                "sourceVerifiedExpressions": sum(1 for x in exprs_by_level[lvl] if x['status'] == 'SOURCE_VERIFIED'),
                "linguisticallyReviewedExpressions": sum(1 for x in exprs_by_level[lvl] if x['status'] == 'LINGUISTICALLY_REVIEWED'),
                "draftUnverifiedExpressions": sum(1 for x in exprs_by_level[lvl] if x['status'] == 'DRAFT_UNVERIFIED'),
                "unrealizedLemmas": sum(1 for x in lemmas_by_level[lvl] if x['status'] == 'UNREALIZED'),
                "unrealizedExpressions": sum(1 for x in exprs_by_level[lvl] if x['status'] == 'UNREALIZED')
            }
            for _, lvl in LEVEL_ORDER
        },
        "realizedScope": {
            "preA1": {
                "units": 15,
                "lessons": 73,
                "realizedLemmas": 168,
                "realizedExpressions": 47
            },
            "a1PilotUnits": {
                "units": 5,
                "lessons": 30,
                "realizedLemmas": 118,
                "realizedExpressions": 30
            },
            "a1Batch1Units": {
                "units": 5,
                "lessons": 29,
                "realizedLemmas": 117,
                "realizedExpressions": 33
            }
        }
    }

    with open(os.path.join(runtime_dir, 'lexicon_manifest.json'), 'w', encoding='utf-8') as fp:
        json.dump(manifest_data, fp, ensure_ascii=False, indent=2)

    with open(os.path.join(runtime_dir, 'lemmas_bundle.json'), 'w', encoding='utf-8') as fp:
        json.dump(realized_lemmas, fp, ensure_ascii=False)

    with open(os.path.join(runtime_dir, 'expressions_bundle.json'), 'w', encoding='utf-8') as fp:
        json.dump(realized_expressions, fp, ensure_ascii=False)

    with open(os.path.join(runtime_dir, 'lesson_lexicon_lookup.json'), 'w', encoding='utf-8') as fp:
        json.dump(lesson_lexicon_map, fp, ensure_ascii=False)

    print(f"\n✓ Runtime assets compiled into {runtime_dir}:")
    print(f"  • lexicon_manifest.json: {os.path.getsize(os.path.join(runtime_dir, 'lexicon_manifest.json')) / 1024:.1f} KB")
    print(f"  • lemmas_bundle.json: {os.path.getsize(os.path.join(runtime_dir, 'lemmas_bundle.json')) / 1024:.1f} KB")
    print(f"  • expressions_bundle.json: {os.path.getsize(os.path.join(runtime_dir, 'expressions_bundle.json')) / 1024:.1f} KB")
    print(f"  • lesson_lexicon_lookup.json: {os.path.getsize(os.path.join(runtime_dir, 'lesson_lexicon_lookup.json')) / 1024:.1f} KB")
    print("=" * 80)
    print("LEXICON INTEGRITY & BATCH 1 REALIZATION COMPLETED SUCCESSFULLY.")
    print("=" * 80)

if __name__ == '__main__':
    main()
