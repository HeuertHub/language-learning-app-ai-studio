# -*- coding: utf-8 -*-
"""Comprehensive forensic audit of C1 lesson blueprints."""

import json
from collections import Counter

def run_audit():
    with open('curriculum/lesson_blueprints/c1_complete.json', 'r', encoding='utf-8') as f:
        c1_lessons = json.load(f)

    with open('curriculum/blueprint/units/c1.json', 'r', encoding='utf-8') as f:
        c1_units = json.load(f)

    with open('curriculum/blueprint/lexicalAllocation.json', 'r', encoding='utf-8') as f:
        lex_alloc = json.load(f)

    with open('curriculum/lesson_blueprints/b2_complete.json', 'r', encoding='utf-8') as f:
        b2_lessons = json.load(f)

    b2_lesson_ids = set(l['lessonId'] for l in b2_lessons)
    c1_lesson_ids = set(l['lessonId'] for l in c1_lessons)
    all_known_lesson_ids = b2_lesson_ids.union(c1_lesson_ids)

    print("================================================================")
    print("                CEFR C1 COMPREHENSIVE AUDIT REPORT             ")
    print("================================================================")

    # 1. Structural Checks
    print("\n--- 1. STRUCTURAL & SCHEMA INTEGRITY ---")
    print(f"Total C1 lessons: {len(c1_lessons)} (Expected: 148)")
    assert len(c1_lessons) == 148, f"Expected 148 lessons, got {len(c1_lessons)}"

    # Check duplicates
    seen_ids = set()
    dup_ids = []
    seen_unit_seq = set()
    dup_unit_seq = []
    for l in c1_lessons:
        lid = l['lessonId']
        if lid in seen_ids:
            dup_ids.append(lid)
        seen_ids.add(lid)

        useq = (l['unitId'], l['sequenceWithinUnit'])
        if useq in seen_unit_seq:
            dup_unit_seq.append(useq)
        seen_unit_seq.add(useq)

    print(f"Duplicate lesson IDs: {len(dup_ids)}")
    print(f"Duplicate (unitId, sequenceWithinUnit): {len(dup_unit_seq)}")
    assert len(dup_ids) == 0, f"Found duplicate lesson IDs: {dup_ids}"
    assert len(dup_unit_seq) == 0, f"Found duplicate unit/seq: {dup_unit_seq}"

    # Verify unit coverage
    unit_map = {u['unitId']: u for u in c1_units}
    lessons_by_unit = {}
    for l in c1_lessons:
        lessons_by_unit.setdefault(l['unitId'], []).append(l)

    print(f"Distinct units covered: {len(lessons_by_unit)} (Expected: 31, Units 198-228)")
    assert len(lessons_by_unit) == 31, f"Expected 31 units, got {len(lessons_by_unit)}"
    for u in c1_units:
        assert u['unitId'] in lessons_by_unit, f"Unit {u['unitId']} missing from lessons"

    # Check contiguous sequence within units
    for uid, llist in lessons_by_unit.items():
        seqs = [l['sequenceWithinUnit'] for l in llist]
        expected_seqs = list(range(1, len(llist) + 1))
        assert seqs == expected_seqs, f"Unit {uid} sequences {seqs} != {expected_seqs}"

    print("All 31 units have contiguous 1-indexed sequences: PASS")

    # Check field completeness
    required_fields = [
        "lessonId", "unitId", "cefrLevel", "sequenceWithinUnit", "title",
        "lessonType", "primaryPurpose", "communicativeOutcome",
        "newProductiveLemmaTarget", "newReceptiveLemmaTarget",
        "newProductiveExpressionTarget", "newReceptiveExpressionTarget",
        "registerTarget", "pragmaticTarget", "prerequisiteLessonIds",
        "reviewsLessonIds", "audioSuitability", "successCriteria", "masteryEvidence"
    ]
    empty_fields = 0
    for l in c1_lessons:
        assert l['cefrLevel'] == 'C1', f"Lesson {l['lessonId']} has level {l['cefrLevel']}"
        for rf in required_fields:
            val = l.get(rf)
            if val is None or (isinstance(val, (str, list)) and len(val) == 0 and rf not in ["readingObjective", "listeningObjective", "writingObjective", "spokenProductionObjective"]):
                print(f"Empty field {rf} in {l['lessonId']}")
                empty_fields += 1
    print(f"Missing required fields: {empty_fields} (PASS)")
    assert empty_fields == 0

    # 2. Lexical Reconciliation
    print("\n--- 2. LEXICAL BUDGET RECONCILIATION ---")
    tot_pl = sum(l['newProductiveLemmaTarget'] for l in c1_lessons)
    tot_rl = sum(l['newReceptiveLemmaTarget'] for l in c1_lessons)
    tot_pe = sum(l['newProductiveExpressionTarget'] for l in c1_lessons)
    tot_re = sum(l['newReceptiveExpressionTarget'] for l in c1_lessons)

    unit_target_pl = sum(u['newProductiveCoreLemmas'] for u in c1_units)
    unit_target_rl = sum(u['newReceptiveCoreLemmas'] for u in c1_units)
    unit_target_pe = sum(u['newProductiveExpressions'] for u in c1_units)
    unit_target_re = sum(u['newReceptiveExpressions'] for u in c1_units)

    c1_lex_alloc = lex_alloc['byLevel']['C1']
    print(f"Productive Lemmas: Authored = {tot_pl}, Units Target = {unit_target_pl}, LexAlloc Target = {c1_lex_alloc['productiveCoreLemmas']}")
    print(f"Receptive Lemmas:  Authored = {tot_rl}, Units Target = {unit_target_rl}, LexAlloc Target = {c1_lex_alloc['receptiveCoreLemmas']}")
    print(f"Productive Expr:   Authored = {tot_pe}, Units Target = {unit_target_pe}")
    print(f"Receptive Expr:    Authored = {tot_re}, Units Target = {unit_target_re}")
    print(f"Total Expressions: Authored = {tot_pe + tot_re}, Units Target = {unit_target_pe + unit_target_re}, LexAlloc Target = {c1_lex_alloc['multiwordExpressions']}")

    assert tot_pl == unit_target_pl == c1_lex_alloc['productiveCoreLemmas']
    assert tot_rl == unit_target_rl == c1_lex_alloc['receptiveCoreLemmas']
    assert tot_pe == unit_target_pe
    assert tot_re == unit_target_re
    assert tot_pe + tot_re == unit_target_pe + unit_target_re == c1_lex_alloc['multiwordExpressions']
    print("Lexical Budget Reconciliation: EXACT 100% MATCH ACROSS ALL TIERS!")

    # 3. Lesson Type Diversity
    print("\n--- 3. LESSON TYPE DIVERSITY & MODALITY BALANCE ---")
    ltypes = Counter(l['lessonType'] for l in c1_lessons)
    for lt, count in ltypes.most_common():
        pct = (count / len(c1_lessons)) * 100
        print(f"  - {lt:25s}: {count:3d} ({pct:5.1f}%)")

    # 4. Grammar Introductions
    print("\n--- 4. GRAMMAR INTRODUCTIONS AUDIT ---")
    unit_grammar = {}
    for u in c1_units:
        for g in u['grammarIntroduced']:
            unit_grammar[g] = u['unitId']

    introduced_in_lessons = {}
    for l in c1_lessons:
        for g in l['grammarIntroduced']:
            introduced_in_lessons[g] = (l['lessonId'], l['unitId'])

    print(f"Grammar concepts defined in c1.json units: {len(unit_grammar)}")
    print(f"Grammar concepts introduced in lessons:   {len(introduced_in_lessons)}")
    for g, uid in unit_grammar.items():
        assert g in introduced_in_lessons, f"Grammar concept {g} in unit {uid} was NOT introduced in any lesson!"
        lid, l_uid = introduced_in_lessons[g]
        assert uid == l_uid, f"Grammar concept {g} introduced in {l_uid} instead of {uid}"
    print("All 16 C1 grammar concepts introduced in their designated units: PASS")

    # 5. DAG Topology & Cycles
    print("\n--- 5. DAG TOPOLOGY & GRAPH INTEGRITY ---")
    missing_prereqs = []
    edges = 0
    adj = {l['lessonId']: [] for l in c1_lessons}

    for l in c1_lessons:
        for p in l['prerequisiteLessonIds']:
            edges += 1
            if p not in all_known_lesson_ids:
                missing_prereqs.append((l['lessonId'], p))
            if p in adj:
                adj[p].append(l['lessonId'])

    print(f"Total prerequisite edges: {edges}")
    print(f"Missing prerequisite references: {len(missing_prereqs)}")
    assert len(missing_prereqs) == 0, f"Found missing prerequisites: {missing_prereqs}"

    # Cycle detection in C1
    in_degree = {lid: 0 for lid in c1_lesson_ids}
    c1_adj = {lid: [] for lid in c1_lesson_ids}
    for l in c1_lessons:
        lid = l['lessonId']
        for p in l['prerequisiteLessonIds']:
            if p in c1_lesson_ids:
                c1_adj[p].append(lid)
                in_degree[lid] += 1

    queue = [lid for lid, deg in in_degree.items() if deg == 0]
    visited_count = 0
    while queue:
        curr = queue.pop(0)
        visited_count += 1
        for nxt in c1_adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    print(f"Topological sort visited: {visited_count} / {len(c1_lesson_ids)} nodes")
    assert visited_count == len(c1_lesson_ids), "CYCLE DETECTED IN PREREQUISITE GRAPH!"
    print("DAG Topology: STRICT ACYCLIC DIRECTED GRAPH (0 CYCLES): PASS")

    # 6. Audio Scoping
    print("\n--- 6. AUDIO SCOPING ---")
    audio_counts = Counter(l['audioSuitability'] for l in c1_lessons)
    for ac, count in audio_counts.most_common():
        pct = (count / len(c1_lessons)) * 100
        print(f"  - {ac:25s}: {count:3d} ({pct:5.1f}%)")

    # 7. Reviews Verification
    print("\n--- 7. REVIEWS NETWORK AUDIT ---")
    missing_reviews = []
    for l in c1_lessons:
        for r in l['reviewsLessonIds']:
            if r not in all_known_lesson_ids:
                missing_reviews.append((l['lessonId'], r))
    print(f"Missing review lesson references: {len(missing_reviews)}")
    assert len(missing_reviews) == 0, f"Found missing review IDs: {missing_reviews}"
    print("Review network fully resolves to valid C1 or B2 lesson nodes: PASS")

    print("\n================================================================")
    print("   FINAL VERDICT: ALL C1 AUDIT CHECKS PASSED WITH 100% RIGOR   ")
    print("================================================================")

if __name__ == '__main__':
    run_audit()
