#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3B: Exercise Content Generation Pilot Builder & Validator
Consumes the frozen CEFR Pre-A1 through C2 lesson blueprints.
Generates authoritative learner-content pilot across 21 representative lessons.
"""

import json
import os
import re
import sys
from datetime import datetime

# Import level content modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'pilot_content'))
from content_pre_a1 import get_pre_a1_exercises
from content_a1 import get_a1_exercises
from content_a2 import get_a2_exercises
from content_b1 import get_b1_exercises
from content_b2 import get_b2_exercises
from content_c1 import get_c1_exercises
from content_c2 import get_c2_exercises

def validate_exercise(ex, lesson_meta):
    """
    Rigorously validates an individual exercise object.
    Checks:
    - Identity & Linkage
    - Cyrillic text presence and encoding
    - Answer validity & acceptable alternatives
    - Explanation & learner feedback
    - Audio synthesis metadata
    - Evaluation rules
    """
    errors = []
    
    # 1. Identity
    if not ex.get('exerciseId'):
        errors.append("Missing exerciseId")
    if not ex.get('exerciseTitle'):
        errors.append("Missing exerciseTitle")
    if not ex.get('modality'):
        errors.append("Missing modality")
    if not ex.get('interactionPattern'):
        errors.append("Missing interactionPattern")
    if not ex.get('cognitiveComplexity'):
        errors.append("Missing cognitiveComplexity")

    # 2. Prompt & Instructions
    prompt = ex.get('prompt', '')
    if not prompt or len(prompt) < 10:
        errors.append(f"Prompt is too short or empty: '{prompt}'")

    # 3. Cyrillic Presence Check
    cyrillic_pattern = re.compile(r'[\u0400-\u04FF]')
    has_cyrillic = (
        bool(cyrillic_pattern.search(prompt)) or
        bool(cyrillic_pattern.search(ex.get('stimulusTextCyrillic', ''))) or
        bool(cyrillic_pattern.search(ex.get('correctAnswer', ''))) or
        any(bool(cyrillic_pattern.search(opt.get('text', ''))) for opt in ex.get('options', [])) or
        any(bool(cyrillic_pattern.search(tok)) for tok in ex.get('wordTokens', []))
    )
    if not has_cyrillic:
        errors.append(f"Exercise {ex.get('exerciseId')} lacks Mongolian Cyrillic stimulus/answer text")

    # 4. Answer Format & Alternatives
    correct_answer = ex.get('correctAnswer')
    if not correct_answer:
        errors.append(f"Exercise {ex.get('exerciseId')} missing correctAnswer")
    alternatives = ex.get('acceptableAlternatives', [])
    if not isinstance(alternatives, list):
        errors.append(f"Exercise {ex.get('exerciseId')} acceptableAlternatives must be a list")

    # 5. Explanations & Learner Feedback
    explanation = ex.get('explanation', '')
    if not explanation or len(explanation) < 15:
        errors.append(f"Exercise {ex.get('exerciseId')} explanation is too short or missing")
    
    feedback = ex.get('learnerFeedback', {})
    if not feedback.get('onSuccess') or not feedback.get('onFailure'):
        errors.append(f"Exercise {ex.get('exerciseId')} missing onSuccess or onFailure learnerFeedback")

    # 6. Audio Requirements
    audio = ex.get('audio', {})
    if audio.get('requiresAudio'):
        if not audio.get('speechSynthesisText'):
            errors.append(f"Exercise {ex.get('exerciseId')} marked requiresAudio=True but missing speechSynthesisText")
        if not audio.get('ipaTranscription'):
            errors.append(f"Exercise {ex.get('exerciseId')} missing ipaTranscription")

    # 7. Evaluation
    eval_rules = ex.get('evaluation', {})
    if not eval_rules.get('matchType'):
        errors.append(f"Exercise {ex.get('exerciseId')} missing evaluation matchType")
    if eval_rules.get('matchType') == 'TOKEN_ORDER':
        if not ex.get('wordTokens') or not ex.get('correctTokenOrder'):
            errors.append(f"Exercise {ex.get('exerciseId')} with matchType TOKEN_ORDER missing wordTokens or correctTokenOrder")
    if eval_rules.get('matchType') == 'RUBRIC_CRITERIA':
        if not eval_rules.get('rubricCriteria') or len(eval_rules.get('rubricCriteria')) < 2:
            errors.append(f"Exercise {ex.get('exerciseId')} with matchType RUBRIC_CRITERIA missing rubricCriteria")
    if ex.get('interactionPattern') == 'PAIR_MATCHING':
        pairs = ex.get('matchingPairs')
        if not pairs or not isinstance(pairs, list) or len(pairs) < 2:
            errors.append(f"Exercise {ex.get('exerciseId')} with PAIR_MATCHING must define at least 2 matchingPairs")
        else:
            for p in pairs:
                if not p.get('left') or not p.get('right'):
                    errors.append(f"Exercise {ex.get('exerciseId')} matchingPair missing left or right: {p}")

    return errors


def main():
    print("=" * 80)
    print("PHASE 3B: EXERCISE CONTENT GENERATION PILOT BUILDER & VALIDATOR")
    print("=" * 80)

    # 1. Load frozen blueprints
    blueprint_paths = {
        'preA1': 'curriculum/lesson_blueprints/preA1.json',
        'a1': 'curriculum/lesson_blueprints/a1_complete.json',
        'a2': 'curriculum/lesson_blueprints/a2_complete.json',
        'b1': 'curriculum/lesson_blueprints/b1_complete.json',
        'b2': 'curriculum/lesson_blueprints/b2_complete.json',
        'c1': 'curriculum/lesson_blueprints/c1_complete.json',
        'c2': 'curriculum/lesson_blueprints/c2_complete.json'
    }

    blueprints = {}
    for lvl, path in blueprint_paths.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing frozen blueprint file: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            blueprints[lvl] = {l['lessonId']: l for l in json.load(f)}

    print(f"Loaded frozen blueprints across {len(blueprints)} CEFR levels.")

    # 2. Gather exercises from all level modules
    level_getters = [
        ('Pre-A1', 'preA1', get_pre_a1_exercises()),
        ('A1', 'a1', get_a1_exercises()),
        ('A2', 'a2', get_a2_exercises()),
        ('B1', 'b1', get_b1_exercises()),
        ('B2', 'b2', get_b2_exercises()),
        ('C1', 'c1', get_c1_exercises()),
        ('C2', 'c2', get_c2_exercises())
    ]

    total_lessons = 0
    total_exercises = 0
    lessons_by_level = {}
    pilot_bundles = []
    validation_failures = []

    for cefr_display, lvl_key, lesson_list in level_getters:
        lessons_by_level[cefr_display] = len(lesson_list)
        print(f"\nProcessing {cefr_display} ({len(lesson_list)} lessons)...")

        for l_data in lesson_list:
            lid = l_data['lessonId']
            if lid not in blueprints[lvl_key]:
                validation_failures.append(f"Lesson ID {lid} not found in frozen {lvl_key} blueprints!")
                continue

            bp = blueprints[lvl_key][lid]
            total_lessons += 1
            ex_list = l_data['exercises']
            total_exercises += len(ex_list)

            # Build enriched bundle
            bundle = {
                "lessonId": lid,
                "unitId": bp['unitId'],
                "cefrLevel": bp['cefrLevel'],
                "lessonTitle": bp['title'],
                "lessonType": bp['lessonType'],
                "primaryPurpose": bp['primaryPurpose'],
                "communicativeOutcome": bp['communicativeOutcome'],
                "exerciseCount": len(ex_list),
                "exercises": []
            }

            for idx, raw_ex in enumerate(ex_list, start=1):
                raw_ex['sequenceInLesson'] = idx
                raw_ex['lessonId'] = lid
                raw_ex['unitId'] = bp['unitId']
                raw_ex['cefrLevel'] = bp['cefrLevel']

                # Validate
                errs = validate_exercise(raw_ex, bp)
                if errs:
                    for e in errs:
                        validation_failures.append(f"[{lid}][{raw_ex.get('exerciseId')}] {e}")

                bundle['exercises'].append(raw_ex)

            pilot_bundles.append(bundle)
            print(f"  ✓ {lid} -> {len(ex_list)} exercises ({bp['lessonType']})")

    # 3. Overall stats check
    print("\n" + "=" * 80)
    print("PILOT CONTENT AUDIT & SUMMARY")
    print("=" * 80)
    print(f"Total Pilot Lessons: {total_lessons} (Target: 21)")
    print(f"Total Pilot Exercises: {total_exercises}")
    print(f"Level Breakdown: {lessons_by_level}")

    if total_lessons != 21:
        validation_failures.append(f"Expected exactly 21 lessons, got {total_lessons}!")

    if validation_failures:
        print("\n❌ VALIDATION FAILURES DETECTED:")
        for f in validation_failures:
            print(f"  - {f}")
        sys.exit(1)

    print("\n✓ All 21 lessons and all exercises passed quality & schema validation!")

    # 4. Write manifest and dataset
    output_dir = 'curriculum/pilot'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'exercise_content_pilot.json')

    manifest_data = {
        "manifestVersion": "1.0.0",
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "phase": "3B",
        "totalLessons": total_lessons,
        "totalExercises": total_exercises,
        "lessonsByLevel": lessons_by_level,
        "lessons": pilot_bundles
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    file_size_kb = os.path.getsize(output_file) / 1024
    print(f"\n✓ Successfully compiled and saved pilot dataset to {output_file} ({file_size_kb:.1f} KB)")
    print("=" * 80)

if __name__ == '__main__':
    main()
