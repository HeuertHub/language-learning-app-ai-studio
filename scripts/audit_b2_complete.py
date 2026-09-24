# -*- coding: utf-8 -*-
"""Aggregate B2 sections and run exhaustive forensic audit."""
import json
import os
from collections import Counter, defaultdict

# Load Section files
sec1 = json.load(open("curriculum/lesson_blueprints/b2_section_01.json", encoding="utf-8"))
sec2 = json.load(open("curriculum/lesson_blueprints/b2_section_02.json", encoding="utf-8"))
sec3 = json.load(open("curriculum/lesson_blueprints/b2_section_03.json", encoding="utf-8"))
sec4 = json.load(open("curriculum/lesson_blueprints/b2_section_04.json", encoding="utf-8"))

b2_complete = sec1 + sec2 + sec3 + sec4

with open("curriculum/lesson_blueprints/b2_complete.json", "w", encoding="utf-8") as f:
    json.dump(b2_complete, f, indent=2, ensure_ascii=False)

print(f"Aggregated B2 Complete: {len(b2_complete)} lessons.")
print(f"Sec 01: {len(sec1)}, Sec 02: {len(sec2)}, Sec 03: {len(sec3)}, Sec 04: {len(sec4)}")

# Authoritative B2 Units
b2_units = json.load(open("curriculum/blueprint/units/b2.json", encoding="utf-8"))
b2_unit_map = {u["unitId"]: u for u in b2_units}

# 1. Lesson ID Uniqueness & Count
lesson_ids = [l["lessonId"] for l in b2_complete]
assert len(lesson_ids) == len(set(lesson_ids)), "Duplicate lesson IDs found!"

# 2. Sequence position uniqueness per unit
unit_seq_pairs = [(l["unitId"], l["sequenceWithinUnit"]) for l in b2_complete]
assert len(unit_seq_pairs) == len(set(unit_seq_pairs)), "Duplicate (unitId, sequenceWithinUnit) pairs found!"

# 3. Sequence continuity per unit
unit_lessons = defaultdict(list)
for l in b2_complete:
    unit_lessons[l["unitId"]].append(l["sequenceWithinUnit"])

for uid, seqs in unit_lessons.items():
    seqs.sort()
    expected = list(range(1, len(seqs) + 1))
    assert seqs == expected, f"Sequence gap in {uid}: {seqs} != {expected}"

# 4. Units covered
covered_units = set(unit_lessons.keys())
expected_units = set(b2_unit_map.keys())
assert covered_units == expected_units, f"Unit coverage mismatch! Missing: {expected_units - covered_units}, Extra: {covered_units - expected_units}"
assert len(covered_units) == 42, f"Expected 42 units, got {len(covered_units)}"

# 5. Lexical reconciliation against units and lexicalAllocation.json
lex_alloc = json.load(open("curriculum/blueprint/lexicalAllocation.json", encoding="utf-8"))
b2_alloc = lex_alloc["byLevel"]["B2"]

tot_pl = sum(l["newProductiveLemmaTarget"] for l in b2_complete)
tot_rl = sum(l["newReceptiveLemmaTarget"] for l in b2_complete)
tot_pe = sum(l["newProductiveExpressionTarget"] for l in b2_complete)
tot_re = sum(l["newReceptiveExpressionTarget"] for l in b2_complete)

expected_pl = sum(u["newProductiveCoreLemmas"] for u in b2_units)
expected_rl = sum(u["newReceptiveCoreLemmas"] for u in b2_units)
expected_pe = sum(u["newProductiveExpressions"] for u in b2_units)
expected_re = sum(u["newReceptiveExpressions"] for u in b2_units)

print("--- LEXICAL RECONCILIATION ---")
print(f"Productive Core Lemmas: Actual={tot_pl}, UnitsSum={expected_pl}, AllocDoc={b2_alloc['productiveCoreLemmas']}")
print(f"Receptive Core Lemmas: Actual={tot_rl}, UnitsSum={expected_rl}, AllocDoc={b2_alloc['receptiveCoreLemmas']}")
print(f"Productive Expressions: Actual={tot_pe}, UnitsSum={expected_pe}")
print(f"Receptive Expressions: Actual={tot_re}, UnitsSum={expected_re}")
print(f"Total Multiword Expressions: Actual={tot_pe + tot_re}, AllocDoc={b2_alloc['multiwordExpressions']}")

assert tot_pl == b2_alloc['productiveCoreLemmas'] == expected_pl
assert tot_rl == b2_alloc['receptiveCoreLemmas'] == expected_rl
assert (tot_pe + tot_re) == b2_alloc['multiwordExpressions'] == (expected_pe + expected_re)

# Per unit lexical budget reconciliation
for uid, u in b2_unit_map.items():
    u_lessons = [l for l in b2_complete if l["unitId"] == uid]
    u_pl = sum(l["newProductiveLemmaTarget"] for l in u_lessons)
    u_rl = sum(l["newReceptiveLemmaTarget"] for l in u_lessons)
    u_pe = sum(l["newProductiveExpressionTarget"] for l in u_lessons)
    u_re = sum(l["newReceptiveExpressionTarget"] for l in u_lessons)
    assert u_pl == u["newProductiveCoreLemmas"], f"PL mismatch in {uid}"
    assert u_rl == u["newReceptiveCoreLemmas"], f"RL mismatch in {uid}"
    assert u_pe == u["newProductiveExpressions"], f"PE mismatch in {uid}"
    assert u_re == u["newReceptiveExpressions"], f"RE mismatch in {uid}"

# 6. Lesson types breakdown
type_counts = Counter(l["lessonType"] for l in b2_complete)
print("--- LESSON TYPES ---")
for t, c in type_counts.most_common():
    print(f"  {t}: {c}")

# 7. Grammar coverage: all 24 introduced grammar concepts must be introduced in lessons
all_intro_gram = []
for u in b2_units:
    all_intro_gram.extend(u.get("grammarIntroduced", []))

lesson_intro_gram = []
for l in b2_complete:
    lesson_intro_gram.extend(l.get("grammarIntroduced", []))

print(f"Authoritative B2 grammarIntroduced count: {len(all_intro_gram)}")
print(f"Lesson blueprints grammarIntroduced count: {len(lesson_intro_gram)}")
assert set(all_intro_gram) == set(lesson_intro_gram), f"Grammar introduced mismatch! Missing: {set(all_intro_gram) - set(lesson_intro_gram)}"

# 8. DAG Check: Prerequisites and Cycles
all_lesson_id_set = set(lesson_ids)
# Load B1 lessons to check external anchor prerequisites
b1_complete = json.load(open("curriculum/lesson_blueprints/b1_complete.json", encoding="utf-8"))
b1_lesson_ids = set(l["lessonId"] for l in b1_complete)

external_anchors = set()
internal_edges = 0
external_edges = 0

adj = defaultdict(list)
in_degree = defaultdict(int)
for l in b2_complete:
    lid = l["lessonId"]
    in_degree[lid] = 0

for l in b2_complete:
    lid = l["lessonId"]
    for prereq in l.get("prerequisiteLessonIds", []):
        if prereq in all_lesson_id_set:
            adj[prereq].append(lid)
            in_degree[lid] += 1
            internal_edges += 1
        elif prereq in b1_lesson_ids:
            external_anchors.add(prereq)
            external_edges += 1
        else:
            raise ValueError(f"Orphan prerequisite {prereq} in lesson {lid}")

# Topological sort check
queue = [lid for lid in b2_complete if in_degree[lid["lessonId"]] == 0]
visited_count = 0
q_ids = [l["lessonId"] for l in queue]

while q_ids:
    curr = q_ids.pop(0)
    visited_count += 1
    for neighbor in adj[curr]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            q_ids.append(neighbor)

print(f"DAG Topological sort: visited {visited_count}/{len(b2_complete)} nodes.")
assert visited_count == len(b2_complete), "Cycle detected in DAG!"
print(f"Internal edges: {internal_edges}, External B1 anchors: {len(external_anchors)} ({external_edges} edges)")

# 9. Audio metadata audit
audio_suitability_counts = Counter(l.get("audioSuitability") for l in b2_complete)
print("--- AUDIO SUITABILITY ---")
for k, v in audio_suitability_counts.items():
    print(f"  {k}: {v}")

for l in b2_complete:
    suit = l.get("audioSuitability")
    purp = l.get("audioPurpose")
    if suit == "none":
        assert purp is None or purp == "", f"Lesson {l['lessonId']} has suitability 'none' but non-empty audioPurpose: {purp}"
    else:
        assert purp and purp != "None" and len(purp.strip()) > 0, f"Lesson {l['lessonId']} has suitability '{suit}' but empty audioPurpose"

# 10. Cumulative check across all levels
pre_a1 = json.load(open("curriculum/lesson_blueprints/preA1.json", encoding="utf-8"))
a1 = json.load(open("curriculum/lesson_blueprints/a1_complete.json", encoding="utf-8"))
a2 = json.load(open("curriculum/lesson_blueprints/a2_complete.json", encoding="utf-8"))
b1 = json.load(open("curriculum/lesson_blueprints/b1_complete.json", encoding="utf-8"))

print("\n--- CUMULATIVE LESSON TOTALS ---")
print(f"Pre-A1: {len(pre_a1)} lessons (Units 1-15: 15 units)")
print(f"A1:     {len(a1)} lessons (Units 16-63: 48 units)")
print(f"A2:     {len(a2)} lessons (Units 233 lessons, Units 64-111: 48 units)")
print(f"B1:     {len(b1)} lessons (Units 112-155: 44 units)")
print(f"B2:     {len(b2_complete)} lessons (Units 156-197: 42 units)")
total_lessons = len(pre_a1) + len(a1) + len(a2) + len(b1) + len(b2_complete)
print(f"TOTAL CUMULATIVE FROZEN LESSONS: {total_lessons}")

assert len(pre_a1) == 73
assert len(a1) == 278
assert len(a2) == 233
assert len(b1) == 194
assert len(b2_complete) == 188
assert total_lessons == 966

print("\n>>> ALL AUDITS PASSED WITH ZERO ERRORS! <<<")
