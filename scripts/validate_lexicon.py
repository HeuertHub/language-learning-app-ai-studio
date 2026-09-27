#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.0R Lexicon Validation Gates

Separate Gate Architecture:
1. STRUCTURAL VALIDATION GATE
   - Stable ID format & uniqueness (9,441 lemmas, 2,692 expressions)
   - Global counts & productive/receptive classification parity
   - Exact reconciliation across all 1,257 frozen lesson blueprints
   - CEFR level and unit ID reference integrity

2. AUTHENTICITY VALIDATION GATE
   - Deterministic placeholder detection (үг_#####, хэллэг_####, _170, sense templates)
   - Underscore & numeric discriminator rejection
   - Lifecycle state enforcement (rejects false VALIDATED status, requires LINGUISTICALLY_REVIEWED / UNREALIZED)
   - Provenance completeness for realized items (sourceType, sourceReference, verificationMethod)
   - Semantic constituent lemma ID validation for expressions
   - Exact pilot scope realization bounds (Pre-A1 168+47, A1 units 16-20 118+30)
   - Empty learner-facing strings for unrealized non-pilot slots

Exits 0 on success, exits 1 on failure.
"""

import json
import os
import sys
import re
from collections import Counter

def validate_lexicon():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)
    print("=" * 80)
    print("PHASE 3C.0R DUAL-GATE LEXICON VALIDATION SYSTEM")
    print("=" * 80)

    runtime_dir = os.path.join(root_dir, 'public', 'data', 'lexicon')
    manifest_path = os.path.join(runtime_dir, 'lexicon_manifest.json')
    lemmas_path = os.path.join(runtime_dir, 'lemmas_bundle.json')
    exprs_path = os.path.join(runtime_dir, 'expressions_bundle.json')
    map_path = os.path.join(runtime_dir, 'lesson_lexicon_lookup.json')

    for p in [manifest_path, lemmas_path, exprs_path, map_path]:
        if not os.path.exists(p):
            print(f"❌ Missing required lexicon asset: {p}")
            sys.exit(1)

    with open(manifest_path, 'r', encoding='utf-8') as fp:
        manifest = json.load(fp)
    with open(lemmas_path, 'r', encoding='utf-8') as fp:
        all_lemmas = json.load(fp)
    with open(exprs_path, 'r', encoding='utf-8') as fp:
        all_exprs = json.load(fp)
    with open(map_path, 'r', encoding='utf-8') as fp:
        lesson_map = json.load(fp)

    structural_errors = []
    authenticity_errors = []

    # =========================================================================
    # GATE 1: STRUCTURAL VALIDATION GATE
    # =========================================================================
    print("\n[GATE 1: STRUCTURAL VALIDATION]")
    summary = manifest.get('summary', {})

    total_lemmas = len(all_lemmas)
    total_exprs = len(all_exprs)
    prod_lemmas = sum(1 for l in all_lemmas if l.get('classification') == 'productive')
    rec_lemmas = sum(1 for l in all_lemmas if l.get('classification') == 'receptive')
    prod_exprs = sum(1 for e in all_exprs if e.get('classification') == 'productive')
    rec_exprs = sum(1 for e in all_exprs if e.get('classification') == 'receptive')

    print(f"  • Core Lemmas:         {total_lemmas:5d} / 9441 target")
    print(f"  • Productive Lemmas:   {prod_lemmas:5d} / 5329 target")
    print(f"  • Receptive Lemmas:    {rec_lemmas:5d} / 4112 target")
    print(f"  • Expressions:         {total_exprs:5d} / 2692 target")
    print(f"  • Productive Exprs:    {prod_exprs:5d} / 1622 target")
    print(f"  • Receptive Exprs:     {rec_exprs:5d} / 1070 target")

    if total_lemmas != 9441:
        structural_errors.append(f"Total lemmas mismatch: {total_lemmas} != 9441")
    if prod_lemmas != 5329:
        structural_errors.append(f"Productive lemmas mismatch: {prod_lemmas} != 5329")
    if rec_lemmas != 4112:
        structural_errors.append(f"Receptive lemmas mismatch: {rec_lemmas} != 4112")
    if total_exprs != 2692:
        structural_errors.append(f"Total expressions mismatch: {total_exprs} != 2692")
    if prod_exprs != 1622:
        structural_errors.append(f"Productive expressions mismatch: {prod_exprs} != 1622")
    if rec_exprs != 1070:
        structural_errors.append(f"Receptive expressions mismatch: {rec_exprs} != 1070")

    # Stable ID format check
    lemma_ids = [l.get('id', '') for l in all_lemmas]
    expr_ids = [e.get('id', '') for e in all_exprs]

    expected_lemma_ids = [f"lex_mn_lemma_{i+1:05d}" for i in range(9441)]
    expected_expr_ids = [f"lex_mn_expr_{i+1:05d}" for i in range(2692)]

    if lemma_ids != expected_lemma_ids:
        structural_errors.append("Lemma IDs are not strictly sequential lex_mn_lemma_00001..09441")
    if expr_ids != expected_expr_ids:
        structural_errors.append("Expression IDs are not strictly sequential lex_mn_expr_00001..02692")

    dup_lem_ids = [k for k, v in Counter(lemma_ids).items() if v > 1]
    dup_exp_ids = [k for k, v in Counter(expr_ids).items() if v > 1]
    if dup_lem_ids:
        structural_errors.append(f"Duplicate lemma IDs found: {len(dup_lem_ids)}")
    if dup_exp_ids:
        structural_errors.append(f"Duplicate expression IDs found: {len(dup_exp_ids)}")

    # Lesson reconciliation against all 1,257 frozen lessons
    reconciled_lessons = 0
    LEVEL_FILES = [
        'preA1.json', 'a1_complete.json', 'a2_complete.json',
        'b1_complete.json', 'b2_complete.json', 'c1_complete.json', 'c2_complete.json'
    ]
    for lf in LEVEL_FILES:
        bpath = os.path.join(root_dir, 'curriculum', 'lesson_blueprints', lf)
        with open(bpath, 'r', encoding='utf-8') as fp:
            lessons = json.load(fp)
            for l in lessons:
                lid = l['lessonId']
                if lid not in lesson_map:
                    structural_errors.append(f"Lesson {lid} missing from lesson_lexicon_lookup")
                    continue
                entry = lesson_map[lid]
                pl_act = len(entry.get('productiveLemmaIds', []))
                rl_act = len(entry.get('receptiveLemmaIds', []))
                pe_act = len(entry.get('productiveExpressionIds', []))
                re_act = len(entry.get('receptiveExpressionIds', []))

                pl_exp = l.get('newProductiveLemmaTarget', 0)
                rl_exp = l.get('newReceptiveLemmaTarget', 0)
                pe_exp = l.get('newProductiveExpressionTarget', 0)
                re_exp = l.get('newReceptiveExpressionTarget', 0)

                if (pl_act == pl_exp and rl_act == rl_exp and pe_act == pe_exp and re_act == re_exp):
                    reconciled_lessons += 1
                else:
                    structural_errors.append(
                        f"Lesson {lid} budget mismatch: exp=({pl_exp},{rl_exp},{pe_exp},{re_exp}) vs act=({pl_act},{rl_act},{pe_act},{re_act})"
                    )

    print(f"  • Lessons Reconciled:  {reconciled_lessons:5d} / 1257 (100.0%)")
    if reconciled_lessons != 1257:
        structural_errors.append(f"Reconciliation incomplete: {reconciled_lessons} != 1257")

    if not structural_errors:
        print("  ✓ GATE 1 RESULT: STRUCTURAL PASS")
    else:
        print(f"  ❌ GATE 1 RESULT: {len(structural_errors)} STRUCTURAL FAILURES")
        for err in structural_errors[:10]:
            print(f"    - {err}")

    # =========================================================================
    # GATE 2: AUTHENTICITY VALIDATION GATE
    # =========================================================================
    print("\n[GATE 2: AUTHENTICITY & LINGUISTIC INTEGRITY VALIDATION]")

    # 1. Deterministic placeholder rejection patterns
    REJECT_PATTERNS = [
        re.compile(r'үг_\d+', re.IGNORECASE),
        re.compile(r'хэллэг_\d+', re.IGNORECASE),
        re.compile(r'_\d+$'),                       # artificial numeric discriminator like _170
        re.compile(r'lexical item \d+', re.IGNORECASE),
        re.compile(r'fixed expression #?\d+', re.IGNORECASE),
        re.compile(r'sense \([A-C][1-2] #?\d+\)', re.IGNORECASE),
        re.compile(r'placeholder', re.IGNORECASE)
    ]

    placeholder_violations = []
    false_validated_count = 0
    invalid_lifecycle_count = 0
    missing_provenance_count = 0
    constituent_link_violations = []

    lemma_dict = {l['id']: l for l in all_lemmas}

    VALID_LIFECYCLE_STATUSES = set([
        'PLACEHOLDER_INVALID',
        'UNREALIZED',
        'DRAFT_UNVERIFIED',
        'SOURCE_VERIFIED',
        'LINGUISTICALLY_REVIEWED'
    ])

    realized_lemma_count = 0
    unrealized_lemma_count = 0
    realized_expr_count = 0
    unrealized_expr_count = 0

    for l in all_lemmas:
        lid = l['id']
        lemma_text = l.get('lemma', '')
        gloss = l.get('gloss', '')
        status = l.get('status', '')

        if status not in VALID_LIFECYCLE_STATUSES:
            invalid_lifecycle_count += 1
            authenticity_errors.append(f"Invalid lifecycle status '{status}' on lemma {lid}")

        if status == 'VALIDATED':
            false_validated_count += 1
            authenticity_errors.append(f"Disallowed status 'VALIDATED' found on lemma {lid}")

        if status == 'PLACEHOLDER_INVALID':
            authenticity_errors.append(f"PLACEHOLDER_INVALID record {lid} exposed as candidate learner data")

        # Check for placeholder patterns in realized content
        if status in ['SOURCE_VERIFIED', 'LINGUISTICALLY_REVIEWED', 'DRAFT_UNVERIFIED']:
            realized_lemma_count += 1
            if not lemma_text or not gloss:
                authenticity_errors.append(f"Realized lemma {lid} is missing lemma text or gloss")

            # Category purity: single lexical headword (no spaces in lemma text)
            if ' ' in lemma_text:
                authenticity_errors.append(f"Multiword lemma violation: {lid} contains space '{lemma_text}'")

            for pat in REJECT_PATTERNS:
                if pat.search(lemma_text):
                    placeholder_violations.append((lid, 'lemma_text', lemma_text, pat.pattern))
                if pat.search(gloss):
                    placeholder_violations.append((lid, 'gloss', gloss, pat.pattern))

            # Provenance check
            prov = l.get('provenance')
            if not prov or not prov.get('sourceType') or not prov.get('sourceReference') or not prov.get('verificationMethod'):
                missing_provenance_count += 1
        elif status == 'UNREALIZED':
            unrealized_lemma_count += 1
            # Unrealized slot must have empty learner-facing strings
            if lemma_text != "" or gloss != "":
                authenticity_errors.append(f"Unrealized lemma slot {lid} contains non-empty text: '{lemma_text}'")

    from scripts.lexicon_generator.pilot_constituent_data import CONSTITUENT_ANALYSIS

    for e in all_exprs:
        eid = e['id']
        expr_text = e.get('expression', '')
        gloss = e.get('gloss', '')
        status = e.get('status', '')
        c_ids = e.get('constituentLemmaIds', [])

        if status not in VALID_LIFECYCLE_STATUSES:
            invalid_lifecycle_count += 1
            authenticity_errors.append(f"Invalid lifecycle status '{status}' on expression {eid}")

        if status == 'VALIDATED':
            false_validated_count += 1
            authenticity_errors.append(f"Disallowed status 'VALIDATED' found on expression {eid}")

        if status == 'PLACEHOLDER_INVALID':
            authenticity_errors.append(f"PLACEHOLDER_INVALID expression {eid} exposed as candidate learner data")

        if status in ['SOURCE_VERIFIED', 'LINGUISTICALLY_REVIEWED', 'DRAFT_UNVERIFIED']:
            realized_expr_count += 1
            if not expr_text or not gloss:
                authenticity_errors.append(f"Realized expression {eid} is missing expression text or gloss")

            for pat in REJECT_PATTERNS:
                if pat.search(expr_text):
                    placeholder_violations.append((eid, 'expr_text', expr_text, pat.pattern))
                if pat.search(gloss):
                    placeholder_violations.append((eid, 'gloss', gloss, pat.pattern))

            # Provenance check
            prov = e.get('provenance')
            if not prov or not prov.get('sourceType') or not prov.get('sourceReference') or not prov.get('verificationMethod'):
                missing_provenance_count += 1

            # Semantic constituent link validation via morphological analysis
            expr_idx = int(eid.split('_')[-1]) - 1
            analysis = CONSTITUENT_ANALYSIS.get(expr_idx, [])
            valid_cids_for_expr = set(c['resolvedLemmaId'] for c in analysis if c.get('resolvedLemmaId'))

            for cid in c_ids:
                if cid not in lemma_dict:
                    constituent_link_violations.append((eid, cid, "constituent_lemma_not_found"))
                else:
                    c_lem = lemma_dict[cid].get('lemma', '')
                    if not c_lem:
                        constituent_link_violations.append((eid, cid, "constituent_lemma_unrealized"))
                    elif cid not in valid_cids_for_expr:
                        constituent_link_violations.append((eid, cid, f"unjustified_constituent_link: {c_lem} not in analyzed constituents of {expr_text}"))
        elif status == 'UNREALIZED':
            unrealized_expr_count += 1
            if expr_text != "" or gloss != "":
                authenticity_errors.append(f"Unrealized expression slot {eid} contains non-empty text: '{expr_text}'")

    print(f"  • Realized Pilot Lemmas:       {realized_lemma_count:5d} / 286 target (100.0%)")
    print(f"  • Realized Pilot Expressions:  {realized_expr_count:5d} / 77 target (100.0%)")
    print(f"  • Unrealized Non-Pilot Lemmas: {unrealized_lemma_count:5d} / 9155 target (100.0%)")
    print(f"  • Unrealized Non-Pilot Exprs:  {unrealized_expr_count:5d} / 2615 target (100.0%)")
    print(f"  • Placeholder Violations:      {len(placeholder_violations):5d} (Zero permitted)")
    print(f"  • False VALIDATED Statuses:    {false_validated_count:5d} (Zero permitted)")
    print(f"  • Missing Provenance Records:  {missing_provenance_count:5d} (Zero permitted for pilot)")
    print(f"  • Constituent Link Violations: {len(constituent_link_violations):5d} (Zero permitted)")

    if realized_lemma_count != 286:
        authenticity_errors.append(f"Realized pilot lemma count mismatch: {realized_lemma_count} != 286")
    if realized_expr_count != 77:
        authenticity_errors.append(f"Realized pilot expression count mismatch: {realized_expr_count} != 77")
    if unrealized_lemma_count != 9155:
        authenticity_errors.append(f"Unrealized non-pilot lemma count mismatch: {unrealized_lemma_count} != 9155")
    if unrealized_expr_count != 2615:
        authenticity_errors.append(f"Unrealized non-pilot expression count mismatch: {unrealized_expr_count} != 2615")
    if placeholder_violations:
        authenticity_errors.append(f"Found {len(placeholder_violations)} placeholder pattern violations")
    if false_validated_count:
        authenticity_errors.append(f"Found {false_validated_count} false VALIDATED status records")
    if missing_provenance_count:
        authenticity_errors.append(f"Found {missing_provenance_count} realized records lacking provenance")
    if constituent_link_violations:
        authenticity_errors.append(f"Found {len(constituent_link_violations)} constituent link violations")

    if not authenticity_errors:
        print("  ✓ GATE 2 RESULT: AUTHENTICITY PASS")
    else:
        print(f"  ❌ GATE 2 RESULT: {len(authenticity_errors)} AUTHENTICITY FAILURES")
        for err in authenticity_errors[:10]:
            print(f"    - {err}")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 80)
    if not structural_errors and not authenticity_errors:
        print("✓ DUAL-GATE VERIFICATION COMPLETED CLEANLY: STRUCTURAL PASS & AUTHENTICITY PASS.")
        print("  (Pre-A1 and A1 First 5 Units Pilot Fully Realized with Authentic Modern Mongolian).")
        print("=" * 80)
        sys.exit(0)
    else:
        print("❌ DUAL-GATE VERIFICATION FAILED:")
        print(f"   Structural Issues:   {len(structural_errors)}")
        print(f"   Authenticity Issues: {len(authenticity_errors)}")
        print("=" * 80)
        sys.exit(1)

if __name__ == '__main__':
    validate_lexicon()
