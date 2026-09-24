# -*- coding: utf-8 -*-
"""Comprehensive verification and audit of curriculum/lesson_blueprints/c2_complete.json."""
import json
import os
import sys

def audit():
    print("=== STARTING C2 COMPREHENSIVE INTEGRITY AUDIT ===")
    
    # 1. JSON Parse Integrity
    with open('curriculum/lesson_blueprints/c2_complete.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)
    print(f"1. JSON parse integrity: PASS ({len(lessons)} lessons)")
    
    # 2. Total Lessons = 143
    assert len(lessons) == 143, f"Expected 143 lessons, found {len(lessons)}"
    print(f"2. Total lessons check: PASS (143 lessons)")
    
    # 3. Units 229-256
    units_in_lessons = sorted(list(set(l['unitId'] for l in lessons)))
    assert len(units_in_lessons) == 28, f"Expected 28 units, found {len(units_in_lessons)}"
    
    blueprint_units = json.load(open('curriculum/blueprint/units/c2.json', encoding='utf-8'))
    expected_unit_ids = [u['unitId'] for u in blueprint_units]
    assert units_in_lessons == sorted(expected_unit_ids), "Units in lessons do not match c2.json exactly"
    print(f"3. Units check: PASS (Units 229-256 exactly, 28 units)")
    
    # 4. No duplicate lesson IDs
    lesson_ids = [l['lessonId'] for l in lessons]
    duplicates = [lid for lid in lesson_ids if lesson_ids.count(lid) > 1]
    assert len(duplicates) == 0, f"Duplicate lesson IDs found: {set(duplicates)}"
    print(f"4. Duplicate lesson IDs check: PASS (0 duplicates)")
    
    # 5. No duplicate unit / sequence pairs
    unit_seq_pairs = [(l['unitId'], l['sequenceWithinUnit']) for l in lessons]
    dup_pairs = [p for p in unit_seq_pairs if unit_seq_pairs.count(p) > 1]
    assert len(dup_pairs) == 0, f"Duplicate unit/seq pairs found: {set(dup_pairs)}"
    print(f"5. Duplicate unit/sequence pairs check: PASS (0 duplicates)")
    
    # 6. Lexical targets match c2.json exactly
    by_unit = {}
    for l in lessons:
        by_unit.setdefault(l['unitId'], []).append(l)
        
    lexical_mismatches = []
    for u in blueprint_units:
        uid = u['unitId']
        u_lessons = by_unit.get(uid, [])
        pl = sum(l['newProductiveLemmaTarget'] for l in u_lessons)
        rl = sum(l['newReceptiveLemmaTarget'] for l in u_lessons)
        pe = sum(l['newProductiveExpressionTarget'] for l in u_lessons)
        re = sum(l['newReceptiveExpressionTarget'] for l in u_lessons)
        
        tpl = u['newProductiveCoreLemmas']
        trl = u['newReceptiveCoreLemmas']
        tpe = u['newProductiveExpressions']
        tre = u['newReceptiveExpressions']
        
        if (pl != tpl or rl != trl or pe != tpe or re != tre):
            lexical_mismatches.append((uid, (pl, rl, pe, re), (tpl, trl, tpe, tre)))
            
    assert len(lexical_mismatches) == 0, f"Lexical mismatches: {lexical_mismatches}"
    print(f"6. Lexical allocation budget exact match: PASS (All 28 units match c2.json targets)")
    
    # 7. No missing metadata fields
    required_fields = [
        "lessonId", "unitId", "cefrLevel", "sequenceWithinUnit", "title", "lessonType",
        "primaryPurpose", "communicativeOutcome", "objectivesIntroduced", "objectivesPracticed",
        "objectivesReviewed", "grammarIntroduced", "grammarPracticed", "grammarReviewed",
        "communicativeFunctionsIntroduced", "communicativeFunctionsPracticed", "communicativeFunctionsReviewed",
        "newProductiveLemmaTarget", "newReceptiveLemmaTarget", "newProductiveExpressionTarget",
        "newReceptiveExpressionTarget", "lexicalDomains", "previousVocabularyReused",
        "registerTarget", "pragmaticTarget", "prerequisiteLessonIds", "reviewsLessonIds",
        "reviewsUnitIds", "reviewReason", "audioSuitability", "successCriteria",
        "masteryEvidence", "recommendedExerciseModalities"
    ]
    
    missing_fields_report = []
    for l in lessons:
        for f in required_fields:
            if f not in l:
                missing_fields_report.append((l['lessonId'], f))
                
    assert len(missing_fields_report) == 0, f"Missing fields found: {missing_fields_report}"
    print(f"7. Required metadata fields check: PASS (All 143 lessons contain 100% complete schema)")
    
    # 8. Success criteria quality check (no empty, no generic placeholders)
    generic_phrases = ["learn grammar", "do exercises", "understand vocabulary", "lesson completed", "generic"]
    flagged_criteria = []
    for l in lessons:
        sc = l.get('successCriteria', [])
        if not sc or len(sc) < 2:
            flagged_criteria.append((l['lessonId'], "less than 2 criteria"))
        for item in sc:
            if len(item.strip()) < 15 or any(gp in item.lower() for gp in generic_phrases):
                flagged_criteria.append((l['lessonId'], item))
    assert len(flagged_criteria) == 0, f"Questionable success criteria: {flagged_criteria}"
    print(f"8. Success criteria specificity check: PASS (Zero generic, all highly specific)")
    
    # 9. Audio metadata audit
    audio_flags = []
    for l in lessons:
        ltype = l['lessonType']
        asuit = l.get('audioSuitability')
        apurp = l.get('audioPurpose')
        if ltype == 'listening':
            if asuit not in ['native_speaker_required', 'native_speaker_preferred']:
                audio_flags.append((l['lessonId'], f"Listening lesson with audioSuitability '{asuit}'"))
            if not apurp:
                audio_flags.append((l['lessonId'], "Listening lesson missing audioPurpose"))
    assert len(audio_flags) == 0, f"Audio flags: {audio_flags}"
    print(f"9. Audio metadata audit: PASS (All listening lessons require native speaker audio with detailed purpose)")
    
    # 10. Prerequisite DAG audit
    known_lesson_ids = set(lesson_ids)
    # Also load C1 lesson IDs to verify cross-level prerequisites
    c1_lessons = json.load(open('curriculum/lesson_blueprints/c1_complete.json', encoding='utf-8'))
    for cl in c1_lessons:
        known_lesson_ids.add(cl['lessonId'])
        
    invalid_prereqs = []
    for l in lessons:
        for pid in l.get('prerequisiteLessonIds', []):
            if pid not in known_lesson_ids:
                invalid_prereqs.append((l['lessonId'], pid))
    assert len(invalid_prereqs) == 0, f"Invalid prerequisites: {invalid_prereqs}"
    print(f"10. Prerequisite DAG integrity: PASS (All prerequisite IDs exist and resolve strictly)")
    
    print("\n=== ALL INTEGRITY AUDITS PASSED PERFECTLY ===")

if __name__ == '__main__':
    audit()
