#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic Exercise Schema & Contract Validator
Validates every exercise against the authoritative TypeScript contract:
- Reject unknown modality
- Reject unknown interaction pattern
- Reject unknown cognitive complexity
- Reject unknown evaluator / match type
- Reject malformed options (must have text, id, valid boolean isCorrect)
- Reject missing required evaluation payload (e.g. TOKEN_ORDER without wordTokens, RUBRIC_CRITERIA without rubricCriteria)
- Reject malformed audio metadata (requiresAudio without speechSynthesisText or ipaTranscription)
- Reject missing or insufficient learner feedback
- Reject missing Cyrillic characters

Exits 0 on success, exits 1 on any violation.
"""

import json
import os
import sys
import re

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

CYRILLIC_REGEX = re.compile(r'[\u0400-\u04FF]')

def validate_exercise(ex, lesson_id):
    eid = ex.get('exerciseId', 'UNKNOWN')
    errors = []

    # 1. Modality
    mod = ex.get('modality')
    if not mod:
        errors.append("Missing 'modality'")
    elif mod not in VALID_MODALITIES:
        errors.append(f"Unknown modality '{mod}'. Must be one of {sorted(list(VALID_MODALITIES))}")

    # 2. Interaction Pattern
    pattern = ex.get('interactionPattern')
    if not pattern:
        errors.append("Missing 'interactionPattern'")
    elif pattern not in VALID_INTERACTIONS:
        errors.append(f"Unknown interactionPattern '{pattern}'. Must be one of {sorted(list(VALID_INTERACTIONS))}")

    # 3. Cognitive Complexity
    comp = ex.get('cognitiveComplexity')
    if not comp:
        errors.append("Missing 'cognitiveComplexity'")
    elif comp not in VALID_COMPLEXITIES:
        errors.append(f"Unknown cognitiveComplexity '{comp}'. Must be one of {sorted(list(VALID_COMPLEXITIES))}")

    # 4. Evaluation Rule & Evaluator Type
    eval_rule = ex.get('evaluation')
    if not eval_rule or not isinstance(eval_rule, dict):
        errors.append("Missing or non-object 'evaluation'")
    else:
        match_type = eval_rule.get('matchType')
        if not match_type:
            errors.append("Missing 'evaluation.matchType'")
        elif match_type not in VALID_MATCH_TYPES:
            errors.append(f"Unknown evaluator matchType '{match_type}'. Must be one of {sorted(list(VALID_MATCH_TYPES))}")

        # Required payload by match type / pattern
        if match_type == 'TOKEN_ORDER' or pattern == 'TOKEN_REARRANGEMENT':
            if not ex.get('wordTokens') or not isinstance(ex.get('wordTokens'), list) or len(ex.get('wordTokens')) < 2:
                errors.append("TOKEN_ORDER exercise requires 'wordTokens' list with at least 2 tokens")
            if not ex.get('correctTokenOrder') or not isinstance(ex.get('correctTokenOrder'), list):
                errors.append("TOKEN_ORDER exercise requires 'correctTokenOrder' list")

        if match_type == 'RUBRIC_CRITERIA' or pattern in ['OPEN_RESPONSE_RUBRIC', 'FREE_RESPONSE_RUBRIC']:
            criteria = eval_rule.get('rubricCriteria')
            if not criteria or not isinstance(criteria, list) or len(criteria) < 2:
                errors.append("RUBRIC_CRITERIA exercise requires 'evaluation.rubricCriteria' list with at least 2 criteria")
            else:
                for c_idx, crit in enumerate(criteria):
                    if not crit.get('description'):
                        errors.append(f"Rubric criterion {c_idx} missing 'description'")
                    if not isinstance(crit.get('points'), (int, float)):
                        errors.append(f"Rubric criterion {c_idx} missing numerical 'points'")

        if match_type == 'SET_EQUALITY' or pattern == 'MULTI_SELECT':
            options = ex.get('options', [])
            correct_opts = [o for o in options if o.get('isCorrect') is True]
            if len(correct_opts) < 1:
                errors.append("SET_EQUALITY exercise must have at least one option marked isCorrect=True")

    # Pattern-specific payload validation
    if pattern in ['MULTIPLE_CHOICE', 'MULTI_SELECT', 'PAIR_MATCHING', 'AUDIO_COMPREHENSION']:
        options = ex.get('options')
        if not options or not isinstance(options, list) or len(options) < 2:
            errors.append(f"Pattern {pattern} requires 'options' list with at least 2 options")
        else:
            for opt_idx, opt in enumerate(options):
                if not opt.get('id'):
                    errors.append(f"Option index {opt_idx} missing 'id'")
                if not opt.get('text') or len(str(opt.get('text')).strip()) == 0:
                    errors.append(f"Option index {opt_idx} has empty 'text'")
                if not isinstance(opt.get('isCorrect'), bool):
                    errors.append(f"Option index {opt_idx} 'isCorrect' must be boolean")

    if pattern == 'SUFFIX_ATTACHMENT':
        if not ex.get('baseWord'):
            errors.append("SUFFIX_ATTACHMENT requires 'baseWord'")
        if not ex.get('suffixOptions') or len(ex.get('suffixOptions', [])) < 2:
            errors.append("SUFFIX_ATTACHMENT requires 'suffixOptions' list with at least 2 options")
        if not ex.get('correctSuffix'):
            errors.append("SUFFIX_ATTACHMENT requires 'correctSuffix'")

    # 5. Audio Metadata
    audio = ex.get('audio')
    if audio and isinstance(audio, dict):
        if audio.get('requiresAudio'):
            if not audio.get('speechSynthesisText') or len(str(audio.get('speechSynthesisText')).strip()) == 0:
                errors.append("Audio exercise has requiresAudio=True but missing 'speechSynthesisText'")
            if not audio.get('ipaTranscription') or len(str(audio.get('ipaTranscription')).strip()) == 0:
                errors.append("Audio exercise has requiresAudio=True but missing 'ipaTranscription'")
            if 'speechRate' in audio and not isinstance(audio['speechRate'], (int, float)):
                errors.append("Malformed audio 'speechRate' (must be numeric)")

    # 6. Learner Feedback
    feedback = ex.get('learnerFeedback')
    if not feedback or not isinstance(feedback, dict):
        errors.append("Missing 'learnerFeedback' object")
    else:
        if not feedback.get('onSuccess') or len(str(feedback.get('onSuccess')).strip()) == 0:
            errors.append("Missing non-empty 'learnerFeedback.onSuccess'")
        if not feedback.get('onFailure') or len(str(feedback.get('onFailure')).strip()) == 0:
            errors.append("Missing non-empty 'learnerFeedback.onFailure'")

    # 7. Prompt & Cyrillic Presence
    prompt = ex.get('prompt', '')
    if not prompt or len(prompt.strip()) < 5:
        errors.append("Prompt is empty or too short (< 5 chars)")

    has_cyrillic = (
        bool(CYRILLIC_REGEX.search(prompt)) or
        bool(CYRILLIC_REGEX.search(ex.get('stimulusTextCyrillic', ''))) or
        bool(CYRILLIC_REGEX.search(ex.get('correctAnswer', ''))) or
        bool(CYRILLIC_REGEX.search(ex.get('contextSentence', ''))) or
        any(bool(CYRILLIC_REGEX.search(opt.get('text', ''))) for opt in ex.get('options', [])) or
        any(bool(CYRILLIC_REGEX.search(tok)) for tok in ex.get('wordTokens', []))
    )
    if not has_cyrillic:
        errors.append("Exercise lacks Mongolian Cyrillic stimulus/answer text")

    return errors

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pilot_path = os.path.join(root_dir, 'curriculum', 'pilot', 'exercise_content_pilot.json')

    print("=" * 80)
    print("DETERMINISTIC EXERCISE SCHEMA & CONTRACT VALIDATOR")
    print("=" * 80)

    if not os.path.exists(pilot_path):
        print(f"❌ File not found: {pilot_path}")
        sys.exit(1)

    with open(pilot_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lessons = data.get('lessons', [])
    total_exercises = 0
    failures = []

    for lesson in lessons:
        lid = lesson.get('lessonId', 'UNKNOWN')
        for ex in lesson.get('exercises', []):
            total_exercises += 1
            errs = validate_exercise(ex, lid)
            if errs:
                failures.append({
                    'exerciseId': ex.get('exerciseId', 'UNKNOWN'),
                    'lessonId': lid,
                    'errors': errs
                })

    print(f"Audited {total_exercises} exercises across {len(lessons)} lessons.")
    if failures:
        print(f"\n❌ VALIDATION FAILED: {len(failures)} exercises violate authoritative schema:")
        for fail in failures:
            print(f"  • [{fail['exerciseId']}] ({fail['lessonId']}):")
            for e in fail['errors']:
                print(f"      - {e}")
        sys.exit(1)
    else:
        print(f"\n✓ 100% PASS: All {total_exercises} exercises conform to authoritative schema and validation gates.")
        print("=" * 80)
        sys.exit(0)

if __name__ == '__main__':
    main()
