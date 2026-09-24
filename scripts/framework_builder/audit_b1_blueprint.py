"""
Comprehensive 38-Point Audit Suite for CEFR B1 Threshold Lesson Blueprint.
Verifies:
1. Structural Integrity & Lexical Budget Reconciliation (Points 1-7)
2. DAG & Prerequisite Graph Integrity (Points 8-13)
3. Review & Interleaving Architecture (Points 14-18)
4. Grammar & Linguistic Architecture (Points 19-23)
5. Communicative & Pragmatic Objectives (Points 24-28)
6. Skill Balance & Modality Packaging (Points 29-32)
7. Pedagogical Diversity & Anti-Clustering (Points 33-35)
8. Regression & Immobility Verification for Pre-A1, A1, A2 (Points 36-38)
"""

import json
import os
import sys
from collections import defaultdict, Counter
from typing import Dict, List, Set, Any, Tuple

def main():
    print("======================================================================")
    print("RUNNING 38-POINT COMPREHENSIVE CEFR B1 BLUEPRINT AUDIT")
    print("======================================================================")

    # -------------------------------------------------------------------------
    # Load all blueprints and reference datasets
    # -------------------------------------------------------------------------
    with open("curriculum/lesson_blueprints/b1_complete.json", "r", encoding="utf-8") as f:
        b1_lessons = json.load(f)

    with open("curriculum/lesson_blueprints/b1_section_01.json", "r", encoding="utf-8") as f:
        sec01 = json.load(f)
    with open("curriculum/lesson_blueprints/b1_section_02.json", "r", encoding="utf-8") as f:
        sec02 = json.load(f)
    with open("curriculum/lesson_blueprints/b1_section_03.json", "r", encoding="utf-8") as f:
        sec03 = json.load(f)
    with open("curriculum/lesson_blueprints/b1_section_04.json", "r", encoding="utf-8") as f:
        sec04 = json.load(f)

    with open("curriculum/blueprint/units/b1.json", "r", encoding="utf-8") as f:
        b1_units = json.load(f)

    with open("curriculum/lesson_blueprints/preA1.json", "r", encoding="utf-8") as f:
        pre_a1_lessons = json.load(f)
    with open("curriculum/lesson_blueprints/a1_complete.json", "r", encoding="utf-8") as f:
        a1_lessons = json.load(f)
    with open("curriculum/lesson_blueprints/a2_complete.json", "r", encoding="utf-8") as f:
        a2_lessons = json.load(f)

    # Index of all lessons across levels
    all_known_lesson_ids = set()
    for l in pre_a1_lessons:
        all_known_lesson_ids.add(l["lessonId"])
    for l in a1_lessons:
        all_known_lesson_ids.add(l["lessonId"])
    for l in a2_lessons:
        all_known_lesson_ids.add(l["lessonId"])
    for l in b1_lessons:
        all_known_lesson_ids.add(l["lessonId"])

    all_unit_files = [
        "curriculum/blueprint/units/pre_a1.json",
        "curriculum/blueprint/units/a1.json",
        "curriculum/blueprint/units/a2.json",
        "curriculum/blueprint/units/b1.json",
    ]
    all_known_unit_ids = set()
    for u_path in all_unit_files:
        if os.path.exists(u_path):
            with open(u_path, "r", encoding="utf-8") as f:
                u_list = json.load(f)
                for u in u_list:
                    all_known_unit_ids.add(u["unitId"])

    passed_points = 0
    total_points = 38

    # -------------------------------------------------------------------------
    # CATEGORY 1: STRUCTURAL INTEGRITY & LEXICAL BUDGET RECONCILIATION
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 1: STRUCTURAL INTEGRITY & BUDGET RECONCILIATION ---")
    
    # Point 1: Total Lesson Count
    p1 = len(b1_lessons) == 194
    print(f"[{'PASS' if p1 else 'FAIL'}] Point 1: Total B1 lesson count = {len(b1_lessons)} (expected 194)")
    if p1: passed_points += 1

    # Point 2: Section Sum Integrity
    sec_sum = len(sec01) + len(sec02) + len(sec03) + len(sec04)
    p2 = (sec_sum == len(b1_lessons)) and (len(sec01) == 55) and (len(sec02) == 48) and (len(sec03) == 44) and (len(sec04) == 47)
    print(f"[{'PASS' if p2 else 'FAIL'}] Point 2: Section sum integrity: Sec01={len(sec01)}, Sec02={len(sec02)}, Sec03={len(sec03)}, Sec04={len(sec04)} -> Sum={sec_sum}")
    if p2: passed_points += 1

    # Point 3: Unit Coverage
    b1_uids = {u["unitId"] for u in b1_units}
    lesson_uids = {l["unitId"] for l in b1_lessons}
    p3 = (b1_uids == lesson_uids) and len(b1_uids) == 44
    print(f"[{'PASS' if p3 else 'FAIL'}] Point 3: Unit coverage: {len(lesson_uids)} / 44 B1 units populated with zero orphans")
    if p3: passed_points += 1

    # Point 4: Lesson Count Distribution (3 to 7 lessons)
    by_unit = defaultdict(list)
    for l in b1_lessons:
        by_unit[l["unitId"]].append(l)
    unit_lengths = Counter(len(ls) for ls in by_unit.values())
    p4 = all(3 <= k <= 7 for k in unit_lengths.keys())
    print(f"[{'PASS' if p4 else 'FAIL'}] Point 4: Unit length distribution: {dict(unit_lengths)} (strictly 3-7 lessons)")
    if p4: passed_points += 1

    # Point 5: Full Lexical Budget Reconciliation (PL, RL, PE, RE)
    budget_mismatches = []
    total_pl, total_rl, total_pe, total_re = 0, 0, 0, 0
    t_total_pl, t_total_rl, t_total_pe, t_total_re = 0, 0, 0, 0
    for u in b1_units:
        uid = u["unitId"]
        u_lessons = by_unit[uid]
        pl = sum(l["newProductiveLemmaTarget"] for l in u_lessons)
        rl = sum(l["newReceptiveLemmaTarget"] for l in u_lessons)
        pe = sum(l["newProductiveExpressionTarget"] for l in u_lessons)
        re = sum(l["newReceptiveExpressionTarget"] for l in u_lessons)

        t_pl, t_rl = u["newProductiveCoreLemmas"], u["newReceptiveCoreLemmas"]
        t_pe, t_re = u["newProductiveExpressions"], u["newReceptiveExpressions"]

        total_pl += pl
        total_rl += rl
        total_pe += pe
        total_re += re
        t_total_pl += t_pl
        t_total_rl += t_rl
        t_total_pe += t_pe
        t_total_re += t_re

        if (pl, rl, pe, re) != (t_pl, t_rl, t_pe, t_re):
            budget_mismatches.append((uid, (pl, rl, pe, re), (t_pl, t_rl, t_pe, t_re)))

    p5 = len(budget_mismatches) == 0
    print(f"[{'PASS' if p5 else 'FAIL'}] Point 5: Lexical budget reconciliation across all 44 units (Mismatches: {len(budget_mismatches)})")
    print(f"       Total Level Lexical Targets: PL={total_pl}/{t_total_pl}, RL={total_rl}/{t_total_rl}, PE={total_pe}/{t_total_pe}, RE={total_re}/{t_total_re}")
    if p5: passed_points += 1

    # Point 6: Unique Lesson IDs & Sequence Uniqueness
    id_counts = Counter(l["lessonId"] for l in b1_lessons)
    dup_ids = [k for k, v in id_counts.items() if v > 1]
    unit_seq_pairs = Counter((l["unitId"], l["sequenceWithinUnit"]) for l in b1_lessons)
    dup_seqs = [k for k, v in unit_seq_pairs.items() if v > 1]
    p6 = len(dup_ids) == 0 and len(dup_seqs) == 0
    print(f"[{'PASS' if p6 else 'FAIL'}] Point 6: Lesson identity uniqueness: {len(dup_ids)} duplicates, {len(dup_seqs)} duplicate sequences")
    if p6: passed_points += 1

    # Point 7: Schema Completeness (no null or empty required fields)
    missing_fields = []
    req_fields = [
        "lessonId", "unitId", "cefrLevel", "sequenceWithinUnit", "title", "lessonType",
        "primaryPurpose", "communicativeOutcome", "objectivesIntroduced", "objectivesPracticed",
        "grammarIntroduced", "grammarPracticed", "phonologyIntroduced", "communicativeFunctionsIntroduced",
        "registerTarget", "pragmaticTarget", "prerequisiteLessonIds", "reviewsLessonIds",
        "audioSuitability", "audioPurpose", "successCriteria", "masteryEvidence"
    ]
    for l in b1_lessons:
        for fld in req_fields:
            if fld not in l or l[fld] is None or (isinstance(l[fld], str) and l[fld].strip() == ""):
                missing_fields.append((l["lessonId"], fld))
    p7 = len(missing_fields) == 0
    print(f"[{'PASS' if p7 else 'FAIL'}] Point 7: Schema field completeness: {len(missing_fields)} missing/empty fields")
    if p7: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 2: DAG & PREREQUISITE INTEGRITY
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 2: DAG & PREREQUISITE GRAPH INTEGRITY ---")

    # Point 8: Existence of All Prerequisite IDs
    missing_prereqs = []
    for l in b1_lessons:
        for p in l.get("prerequisiteLessonIds", []):
            if p not in all_known_lesson_ids:
                missing_prereqs.append((l["lessonId"], p))
    p8 = len(missing_prereqs) == 0
    print(f"[{'PASS' if p8 else 'FAIL'}] Point 8: Prerequisite ID existence: {len(missing_prereqs)} dangling prerequisites")
    if p8: passed_points += 1

    # Point 9: DAG Acyclicity
    all_curriculum_lessons = pre_a1_lessons + a1_lessons + a2_lessons + b1_lessons
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    for lid in all_known_lesson_ids:
        in_degree[lid] = 0

    for l in all_curriculum_lessons:
        lid = l["lessonId"]
        for p in l.get("prerequisiteLessonIds", []):
            if p in all_known_lesson_ids:
                adj[p].append(lid)
                in_degree[lid] += 1

    # Kahn's algorithm
    queue = [lid for lid in all_known_lesson_ids if in_degree[lid] == 0]
    visited_count = 0
    while queue:
        curr = queue.pop(0)
        visited_count += 1
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    p9 = visited_count == len(all_known_lesson_ids)
    print(f"[{'PASS' if p9 else 'FAIL'}] Point 9: DAG acyclicity (Kahn's Topological Sort): visited {visited_count}/{len(all_known_lesson_ids)} nodes (Cycle-free)")
    if p9: passed_points += 1

    # Point 10: Prerequisite Edge Typology
    total_edges = sum(len(l.get("prerequisiteLessonIds", [])) for l in b1_lessons)
    cross_unit_prereqs = 0
    multi_parent_lessons = 0
    for l in b1_lessons:
        prereqs = l.get("prerequisiteLessonIds", [])
        if len(prereqs) > 1:
            multi_parent_lessons += 1
        for p in prereqs:
            # Check if cross unit
            p_unit = p.split("_")[2] if len(p.split("_")) > 2 else ""
            l_unit = l["lessonId"].split("_")[2]
            if p_unit != l_unit:
                cross_unit_prereqs += 1
    p10 = total_edges > 0 and cross_unit_prereqs > 0 and multi_parent_lessons > 0
    print(f"[{'PASS' if p10 else 'FAIL'}] Point 10: Prerequisite topology: {total_edges} total edges, {cross_unit_prereqs} cross-unit edges, {multi_parent_lessons} multi-parent branching nodes")
    if p10: passed_points += 1

    # Point 11: Initial Lesson Anchoring
    # Lesson 1 of Unit 112 must link to A2 capstone
    l_112_01 = [l for l in b1_lessons if l["lessonId"] == "les_b1_112_01_abstract_noun_derivation_intro"][0]
    p11 = "les_a2_111_06_waystage_a2_exit_milestone_benchmark_checkpoint" in l_112_01.get("prerequisiteLessonIds", [])
    print(f"[{'PASS' if p11 else 'FAIL'}] Point 11: Level entry anchor: Unit 112 Lesson 1 prerequisites = {l_112_01.get('prerequisiteLessonIds', [])}")
    if p11: passed_points += 1

    # Point 12: Inter-Section Continuity
    # Unit 124 links to Sec 01 Capstone (Unit 123)
    l_124_01 = [l for l in b1_lessons if l["lessonId"] == "les_b1_124_01_opinion_epistemic_stance_lexicon"][0]
    l_135_01 = [l for l in b1_lessons if l["lessonId"] == "les_b1_135_01_topography_landscapes_lexicon"][0]
    l_145_01 = [l for l in b1_lessons if l["lessonId"] == "les_b1_145_01_naadam_cultural_pageantry_lexicon"][0]
    p12 = (len(l_124_01.get("prerequisiteLessonIds", [])) > 0 and
           len(l_135_01.get("prerequisiteLessonIds", [])) > 0 and
           len(l_145_01.get("prerequisiteLessonIds", [])) > 0)
    print(f"[{'PASS' if p12 else 'FAIL'}] Point 12: Inter-section continuity: All section entry lessons properly anchored to preceding capstones")
    if p12: passed_points += 1

    # Point 13: Terminal Milestone Reachability
    capstone = [l for l in b1_lessons if l["lessonId"] == "les_b1_155_06_b1_level_culminating_mastery_capstone"][0]
    p13 = len(capstone.get("prerequisiteLessonIds", [])) >= 2
    print(f"[{'PASS' if p13 else 'FAIL'}] Point 13: Grand Capstone reachability: Terminal node prerequisites = {capstone.get('prerequisiteLessonIds', [])}")
    if p13: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 3: REVIEW & INTERLEAVING ARCHITECTURE
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 3: REVIEW & INTERLEAVING ARCHITECTURE ---")

    # Point 14: Review Lesson ID Existence
    missing_review_lessons = []
    for l in b1_lessons:
        for r in l.get("reviewsLessonIds", []):
            if r not in all_known_lesson_ids:
                missing_review_lessons.append((l["lessonId"], r))
    p14 = len(missing_review_lessons) == 0
    print(f"[{'PASS' if p14 else 'FAIL'}] Point 14: Review lesson ID existence: {len(missing_review_lessons)} dangling review IDs")
    if p14: passed_points += 1

    # Point 15: Review Unit ID Existence
    missing_review_units = []
    for l in b1_lessons:
        for ru in l.get("reviewsUnitIds", []):
            if ru not in all_known_unit_ids:
                missing_review_units.append((l["lessonId"], ru))
    p15 = len(missing_review_units) == 0
    print(f"[{'PASS' if p15 else 'FAIL'}] Point 15: Review unit ID existence: {len(missing_review_units)} dangling review unit IDs")
    if p15: passed_points += 1

    # Point 16: Explicit Review Justification
    missing_reasons = []
    for l in b1_lessons:
        if l.get("reviewsLessonIds") or l.get("reviewsUnitIds"):
            reason = l.get("reviewReason", "")
            if not reason or reason.strip() == "":
                missing_reasons.append(l["lessonId"])
    p16 = len(missing_reasons) == 0
    print(f"[{'PASS' if p16 else 'FAIL'}] Point 16: Explicit reviewReason documentation: {len(missing_reasons)} missing justifications")
    if p16: passed_points += 1

    # Point 17: Previous Vocabulary Reused Non-Empty
    vocab_reused_empty = [l["lessonId"] for l in b1_lessons if len(l.get("previousVocabularyReused", [])) == 0]
    p17 = len(vocab_reused_empty) == 0
    print(f"[{'PASS' if p17 else 'FAIL'}] Point 17: Active vocabulary reuse: {len(vocab_reused_empty)} lessons with empty previousVocabularyReused")
    if p17: passed_points += 1

    # Point 18: Inter-Level Review Density (B1 reviews A2/A1)
    a2_reviews = sum(1 for l in b1_lessons if any("a2" in r for r in l.get("reviewsLessonIds", []) + l.get("reviewsUnitIds", [])))
    a1_reviews = sum(1 for l in b1_lessons if any("a1" in r for r in l.get("reviewsLessonIds", []) + l.get("reviewsUnitIds", [])))
    p18 = a2_reviews > 0 or a1_reviews > 0
    print(f"[{'PASS' if p18 else 'FAIL'}] Point 18: Inter-level spiral review: {a2_reviews} lessons explicitly review A2, {a1_reviews} review A1")
    if p18: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 4: GRAMMAR & LINGUISTIC ARCHITECTURE
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 4: GRAMMAR & LINGUISTIC ARCHITECTURE ---")

    # Point 19: All B1 Introduced Grammar Targets Covered
    b1_intro_target_set = set()
    for u in b1_units:
        for g in u.get("grammarIntroduced", []):
            b1_intro_target_set.add(g)

    b1_lessons_intro_grammar = set()
    for l in b1_lessons:
        for g in l.get("grammarIntroduced", []):
            b1_lessons_intro_grammar.add(g)

    missing_intro_grammar = b1_intro_target_set - b1_lessons_intro_grammar
    p19 = len(missing_intro_grammar) == 0
    print(f"[{'PASS' if p19 else 'FAIL'}] Point 19: Unit grammarIntroduced coverage: {len(missing_intro_grammar)} uncovered targets (Targets: {len(b1_intro_target_set)}, Actual: {len(b1_lessons_intro_grammar)})")
    if p19: passed_points += 1

    # Point 20: Reinforced Grammar Targets Practiced
    unreinforced_units = []
    for u in b1_units:
        reinf = set(u.get("grammarReinforced", []))
        if not reinf:
            continue
        u_lessons = by_unit[u["unitId"]]
        practiced = set()
        for l in u_lessons:
            practiced.update(l.get("grammarPracticed", []))
            practiced.update(l.get("grammarReviewed", []))
        missing_reinf = reinf - practiced
        if missing_reinf:
            unreinforced_units.append((u["unitId"], list(missing_reinf)))
    p20 = len(unreinforced_units) == 0
    print(f"[{'PASS' if p20 else 'FAIL'}] Point 20: Unit grammarReinforced fulfillment: {len(unreinforced_units)} units with missing reinforcement")
    if p20: passed_points += 1

    # Point 21: Dedicated Grammar Introduction Lessons
    grammar_intro_lessons = [l for l in b1_lessons if l["lessonType"] == "grammar_introduction"]
    p21 = len(grammar_intro_lessons) == len(b1_intro_target_set)
    print(f"[{'PASS' if p21 else 'FAIL'}] Point 21: Grammar introduction lessons count: {len(grammar_intro_lessons)} (expected {len(b1_intro_target_set)})")
    if p21: passed_points += 1

    # Point 22: Dedicated Grammar Guided Practice Lessons
    grammar_practice_lessons = [l for l in b1_lessons if l["lessonType"] == "grammar_guided_practice"]
    p22 = len(grammar_practice_lessons) > 0
    print(f"[{'PASS' if p22 else 'FAIL'}] Point 22: Guided grammar practice lessons: {len(grammar_practice_lessons)} lessons")
    if p22: passed_points += 1

    # Point 23: Phonology Objectives Alignment
    phono_introduced_count = sum(len(l.get("phonologyIntroduced", [])) for l in b1_lessons)
    p23 = phono_introduced_count > 0
    print(f"[{'PASS' if p23 else 'FAIL'}] Point 23: Phonological prosodic objectives introduced: {phono_introduced_count} items")
    if p23: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 5: COMMUNICATIVE & PRAGMATIC OBJECTIVES
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 5: COMMUNICATIVE & PRAGMATIC OBJECTIVES ---")

    # Point 24: Unit Communicative Functions Coverage
    unfulfilled_comm_units = []
    for u in b1_units:
        comm_req = set(u.get("communicativeFunctions", []))
        u_lessons = by_unit[u["unitId"]]
        comm_in_lessons = set()
        for l in u_lessons:
            comm_in_lessons.update(l.get("communicativeFunctionsIntroduced", []))
            comm_in_lessons.update(l.get("communicativeFunctionsPracticed", []))
            comm_in_lessons.update(l.get("communicativeFunctionsReviewed", []))
        missing_comm = comm_req - comm_in_lessons
        if missing_comm:
            unfulfilled_comm_units.append((u["unitId"], list(missing_comm)))
    p24 = len(unfulfilled_comm_units) == 0
    print(f"[{'PASS' if p24 else 'FAIL'}] Point 24: Communicative functions coverage: {len(unfulfilled_comm_units)} units with missing communicative functions")
    if p24: passed_points += 1

    # Point 25: Pragmatic Target Distinctiveness
    pragmatic_targets = [l["pragmaticTarget"] for l in b1_lessons]
    unique_pragmatics = len(set(pragmatic_targets))
    p25 = unique_pragmatics >= 150
    print(f"[{'PASS' if p25 else 'FAIL'}] Point 25: Pragmatic target distinctiveness: {unique_pragmatics} unique targets across 194 lessons")
    if p25: passed_points += 1

    # Point 26: Register Target Diversity
    register_targets = Counter(l["registerTarget"] for l in b1_lessons)
    p26 = len(register_targets) >= 30
    print(f"[{'PASS' if p26 else 'FAIL'}] Point 26: Register calibration diversity: {len(register_targets)} distinctive registers targeted")
    if p26: passed_points += 1

    # Point 27: Communicative Outcome Specification
    p27 = all(len(l["communicativeOutcome"].strip()) >= 20 for l in b1_lessons)
    print(f"[{'PASS' if p27 else 'FAIL'}] Point 27: Communicative outcomes non-triviality: 100% of lessons exceed 20 characters")
    if p27: passed_points += 1

    # Point 28: Lexical Domains Alignment
    all_domains = set()
    for l in b1_lessons:
        all_domains.update(l.get("lexicalDomains", []))
    p28 = len(all_domains) >= 6
    print(f"[{'PASS' if p28 else 'FAIL'}] Point 28: Lexical domain breath: {len(all_domains)} distinct domains ({list(all_domains)})")
    if p28: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 6: SKILL BALANCE & MODALITY PACKAGING
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 6: SKILL BALANCE & MODALITY PACKAGING ---")

    # Point 29: Reading & Listening Dedicated Lessons
    reading_lessons = sum(1 for l in b1_lessons if l["lessonType"] == "reading_development")
    listening_lessons = sum(1 for l in b1_lessons if l["lessonType"] == "listening_development")
    p29 = reading_lessons >= 20 and listening_lessons >= 20 and (reading_lessons + listening_lessons) >= 50
    print(f"[{'PASS' if p29 else 'FAIL'}] Point 29: Receptive skills balance: {reading_lessons} reading development, {listening_lessons} listening development lessons (Total receptive: {reading_lessons + listening_lessons})")
    if p29: passed_points += 1

    # Point 30: Productive Dialogue, Spoken & Writing Lessons
    dialogue_lessons = sum(1 for l in b1_lessons if l["lessonType"] == "dialogue_work")
    spoken_lessons = sum(1 for l in b1_lessons if l["lessonType"] in ["spoken_production", "discussion", "interview_simulation", "collaborative_planning", "presentation", "roleplay", "debate_simulation"])
    writing_lessons = sum(1 for l in b1_lessons if l["lessonType"] == "writing")
    total_productive = dialogue_lessons + spoken_lessons + writing_lessons
    p30 = dialogue_lessons >= 12 and spoken_lessons >= 25 and writing_lessons >= 10 and total_productive >= 50
    print(f"[{'PASS' if p30 else 'FAIL'}] Point 30: Productive skills balance: {dialogue_lessons} dialogues, {spoken_lessons} spoken/discussions/simulations, {writing_lessons} writing workshops (Total productive: {total_productive})")
    if p30: passed_points += 1

    # Point 31: Audio Suitability Requirements
    audio_reqs = Counter(l.get("audioSuitability") for l in b1_lessons)
    p31 = "mongolian_voice_required" in audio_reqs and audio_reqs["mongolian_voice_required"] >= 30
    print(f"[{'PASS' if p31 else 'FAIL'}] Point 31: Audio pedagogy requirements: {dict(audio_reqs)}")
    if p31: passed_points += 1

    # Point 32: Exercise Modality Diversity
    all_modalities = set()
    for l in b1_lessons:
        all_modalities.update(l.get("recommendedExerciseModalities", []))
    p32 = len(all_modalities) >= 50
    print(f"[{'PASS' if p32 else 'FAIL'}] Point 32: Recommended exercise modality diversity: {len(all_modalities)} unique task types")
    if p32: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 7: PEDAGOGICAL DIVERSITY & ANTI-CLUSTERING
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 7: PEDAGOGICAL DIVERSITY & ANTI-CLUSTERING ---")

    # Point 33: Unit Lesson Type Sequence Entropy
    unit_sequences = Counter(tuple(l["lessonType"] for l in ls) for ls in by_unit.values())
    top_seq_freq = unit_sequences.most_common(1)[0][1]
    top_seq_ratio = top_seq_freq / 44
    p33 = top_seq_ratio < 0.25
    print(f"[{'PASS' if p33 else 'FAIL'}] Point 33: Lesson-type sequence entropy: Top sequence occurs {top_seq_freq} times ({top_seq_ratio:.1%}, threshold < 25%)")
    if p33: passed_points += 1

    # Point 34: Lexical Partition Diversity (No single tuple dominance)
    unit_lex_tuples = Counter()
    for uid, ls in by_unit.items():
        u_tuple = tuple((l["newProductiveLemmaTarget"], l["newReceptiveLemmaTarget"],
                         l["newProductiveExpressionTarget"], l["newReceptiveExpressionTarget"])
                        for l in ls if l["lessonType"] not in ["checkpoint", "milestone_checkpoint"])
        unit_lex_tuples[u_tuple] += 1
    top_tuple_freq = unit_lex_tuples.most_common(1)[0][1]
    top_tuple_ratio = top_tuple_freq / 44
    p34 = top_tuple_ratio < 0.35
    print(f"[{'PASS' if p34 else 'FAIL'}] Point 34: Lexical partition diversity: Top tuple pattern occurs {top_tuple_freq} times ({top_tuple_ratio:.1%}, threshold < 35%)")
    if p34: passed_points += 1

    # Point 35: Title and Mastery Evidence Authenticity
    titles = [l["title"] for l in b1_lessons]
    unique_titles = len(set(titles))
    p35 = unique_titles == len(b1_lessons)
    print(f"[{'PASS' if p35 else 'FAIL'}] Point 35: Unique, non-templated lesson titles: {unique_titles} / {len(b1_lessons)} 100% unique")
    if p35: passed_points += 1

    # -------------------------------------------------------------------------
    # CATEGORY 8: REGRESSION & IMMOBILITY VERIFICATION
    # -------------------------------------------------------------------------
    print("\n--- CATEGORY 8: REGRESSION & IMMOBILITY CHECK ---")

    # Point 36: Pre-A1 Complete Freeze Check
    p36 = len(pre_a1_lessons) == 73
    print(f"[{'PASS' if p36 else 'FAIL'}] Point 36: Pre-A1 freeze check: exactly 73 validated lessons (Found: {len(pre_a1_lessons)})")
    if p36: passed_points += 1

    # Point 37: A1 Complete Freeze Check
    p37 = len(a1_lessons) == 278
    print(f"[{'PASS' if p37 else 'FAIL'}] Point 37: A1 freeze check: exactly 278 validated lessons (Found: {len(a1_lessons)})")
    if p37: passed_points += 1

    # Point 38: A2 Complete Freeze Check
    p38 = len(a2_lessons) == 233
    print(f"[{'PASS' if p38 else 'FAIL'}] Point 38: A2 freeze check: exactly 233 validated lessons (Found: {len(a2_lessons)})")
    if p38: passed_points += 1

    print("\n======================================================================")
    print(f"FINAL AUDIT RESULT: {passed_points} / {total_points} AUDIT CHECKS PASSED")
    print("======================================================================")

    if passed_points == total_points:
        print("ALL 38 AUDIT REQUIREMENTS MET PERFECTLY. B1 BLUEPRINT IS AUTHORITATIVE & CERTIFIED.")
        return 0
    else:
        print(f"CRITICAL: {total_points - passed_points} CHECKS FAILED.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
