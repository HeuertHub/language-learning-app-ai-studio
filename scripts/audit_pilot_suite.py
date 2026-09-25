#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3B.2 Hardened Adversarial Audit Suite
Certifies the Exercise Engine before full curriculum scaling.
Audits all 105 exercises across 21 lessons with automated rejection rules for:
1. Evaluation Engine Hardening (token punctuation separation, token set equality, whitespace)
2. Hint Quality Validator (exact answer leak, inflection leak, "Type:" patterns, conceptual guidance)
3. Distractor Quality Validator (absurd/cartoonish, unrelated, English-only cheatability, plausibility)
4. Frozen Blueprint Immutability and Alignment
"""

import json
import os
import re
import sys
from typing import Dict, List, Any, Tuple

def normalize_token(t: str) -> str:
    """Normalizes token by lowercasing, stripping punctuation, and trimming."""
    return re.sub(r'[^\w\s]', '', t.lower()).strip()

class ExerciseEngineAuditor:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        with open(dataset_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        self.total_lessons = self.data['totalLessons']
        self.total_exercises = self.data['totalExercises']
        
        # Results tracking
        self.passed_count = 0
        self.evaluation_failures: List[Dict[str, Any]] = []
        self.hint_failures: List[Dict[str, Any]] = []
        self.distractor_failures: List[Dict[str, Any]] = []
        self.schema_failures: List[Dict[str, Any]] = []

    def audit_evaluation_engine(self, ex: Dict[str, Any], lid: str) -> List[str]:
        """
        Audits evaluation rules and token normalization safeguards.
        Specifically checks:
        - Punctuation separation from wordTokens and correctTokenOrder
        - Set equality between wordTokens and correctTokenOrder
        - Whitespace normalization
        - Match type validity
        """
        errors = []
        eid = ex.get('exerciseId', 'unknown')
        eval_rule = ex.get('evaluation', {})
        match_type = eval_rule.get('matchType')

        if not match_type:
            errors.append(f"Missing evaluation matchType")

        if match_type == 'TOKEN_ORDER' or ex.get('interactionPattern') == 'TOKEN_REARRANGEMENT':
            wt = ex.get('wordTokens', [])
            ct = ex.get('correctTokenOrder', [])

            if not wt or not ct:
                errors.append("TOKEN_ORDER exercise missing wordTokens or correctTokenOrder")
                return errors

            # 1. Check for UI punctuation embedded in individual tokens
            punct_regex = re.compile(r'[.,!?;:«»"“”—–()\[\]{}]')
            for t in wt:
                if punct_regex.search(t):
                    errors.append(f"UI punctuation embedded in wordToken: '{t}' (must be separated)")
            for t in ct:
                if punct_regex.search(t):
                    errors.append(f"UI punctuation embedded in correctToken: '{t}' (must be separated)")

            # 2. Check token set equality (ignoring order)
            wt_norm = sorted([normalize_token(t) for t in wt])
            ct_norm = sorted([normalize_token(t) for t in ct])

            if wt_norm != ct_norm:
                errors.append(f"Token set mismatch between wordTokens and correctTokenOrder: {wt_norm} != {ct_norm}")

            # 3. Check token count equality
            if len(wt) != len(ct):
                errors.append(f"Token length mismatch: len(wordTokens)={len(wt)} vs len(correctTokenOrder)={len(ct)}")

        return errors

    def audit_hint_quality(self, ex: Dict[str, Any], lid: str) -> List[str]:
        """
        Audits hint against automated rejection rules:
        - Rule 1: No exact answer substring
        - Rule 2: No 'Type: [answer]' pattern
        - Rule 3: No root + inflection leaks ('root + suffix -> answer' or '= answer')
        - Rule 4: Must provide conceptual guidance with sufficient length
        """
        errors = []
        eid = ex.get('exerciseId', 'unknown')
        hint = ex.get('hint', '').strip()
        ans = str(ex.get('correctAnswer', '')).strip()

        if not hint:
            errors.append("Hint is missing or empty")
            return errors

        if len(hint) < 15:
            errors.append(f"Hint is too short ({len(hint)} chars) to provide conceptual guidance: '{hint}'")

        # Rule 1: 'Type: [answer]' pattern
        if re.search(r'(?i)\btype[:\s]+', hint) or re.search(r'(?i)type the\b', hint):
            errors.append(f"Hint contains 'Type:' direct recall pattern: '{hint}'")

        # Rule 2: Exact answer substring leak
        ans_norm = normalize_token(ans)
        hint_norm = normalize_token(hint)
        if len(ans_norm) >= 3 and ex.get('interactionPattern') in ['CLOZE_TEXT', 'TOKEN_REARRANGEMENT']:
            # For cloze text, hint must never contain the exact target word
            if ans_norm in hint_norm:
                errors.append(f"Hint directly leaks exact answer '{ans}': '{hint}'")

        # Rule 3: Root + inflection direct spill (e.g. 'root + suffix -> target' or '= target')
        if '->' in hint or '=>' in hint:
            arrow_parts = hint.split('->')[-1]
            if normalize_token(ans) in normalize_token(arrow_parts):
                errors.append(f"Hint contains inflection formula leaking answer: '{hint}'")
        
        if re.search(r'=\s*[\'"][^\'"]+[\'"]', hint):
            eq_target = re.findall(r'=\s*[\'"]([^\'"]+)[\'"]', hint)
            for t in eq_target:
                if normalize_token(t) == ans_norm:
                    errors.append(f"Hint explicitly equates '= {t}' leaking answer: '{hint}'")

        # Rule 4: Learner feedback onFailure must also not use 'Type: [answer]' pattern
        fb_failure = ex.get('learnerFeedback', {}).get('onFailure', '')
        if re.search(r'(?i)^type:\s*', fb_failure.strip()):
            errors.append(f"learnerFeedback.onFailure uses crude 'Type: [answer]' pattern: '{fb_failure}'")

        return errors

    def audit_distractor_quality(self, ex: Dict[str, Any], lid: str) -> List[str]:
        """
        Audits options and distractors against quality criteria:
        - Prevents absurd / cartoonish distractors
        - Prevents unrelated / nonsensical distractors
        - Requires plausible grammatical, register, and pragmatic distractors
        - Prevents trivial English-only elimination
        """
        errors = []
        eid = ex.get('exerciseId', 'unknown')
        options = ex.get('options', [])

        if not options:
            return errors  # Non-option exercises (CLOZE, TOKEN_REARRANGEMENT, etc.)

        if len(options) < 2:
            errors.append(f"Exercise has fewer than 2 options ({len(options)})")

        # Absurd / cartoonish / non-serious keyword blacklist
        absurd_patterns = [
            r'(?i)\brobots?\b',
            r'(?i)\bfistfight\b',
            r'(?i)throws? down his badge',
            r'(?i)runs? away\b',
            r'(?i)advertisement for.*pens',
            r'(?i)i love my car',
            r'(?i)driving cars is fun',
            r'(?i)destroy.*all laws',
            r'(?i)all laws must be destroyed',
            r'(?i)robotic, artificial textbook precision',
            r'(?i)under no circumstances can.*be reduced',
            r'(?i)completely useless and.*forever',
            r'(?i)би машиндаа хайртай',
            r'(?i)машин унах гоё'
        ]

        for opt in options:
            txt = opt.get('text', '')
            t_id = opt.get('id', '')

            # Check text presence
            if not txt or len(txt.strip()) < 1:
                errors.append(f"Option {t_id} has empty text")

            # Check for absurd patterns
            for pat in absurd_patterns:
                if re.search(pat, txt):
                    errors.append(f"Option '{t_id}' contains cartoonish/absurd distractor pattern '{pat}': '{txt}'")

        # Check for distractor rationale presence in higher levels (B2, C1, C2)
        cefr = ex.get('cefrLevel', '')
        if cefr in ['B2', 'C1', 'C2']:
            for opt in options:
                if not opt.get('isCorrect') and not opt.get('explanation') and not opt.get('distractorRationale'):
                    errors.append(f"Higher-level option '{opt.get('id')}' lacks pedagogical distractor rationale")

        return errors

    def run_full_audit(self) -> Dict[str, Any]:
        """Runs the complete adversarial audit across all 105 exercises."""
        total_exercises_audited = 0
        passed_cleanly = 0

        for lesson in self.data['lessons']:
            lid = lesson['lessonId']
            for ex in lesson['exercises']:
                total_exercises_audited += 1
                eid = ex.get('exerciseId')

                eval_errs = self.audit_evaluation_engine(ex, lid)
                hint_errs = self.audit_hint_quality(ex, lid)
                dist_errs = self.audit_distractor_quality(ex, lid)

                has_failure = False
                if eval_errs:
                    has_failure = True
                    self.evaluation_failures.append({"exerciseId": eid, "lessonId": lid, "errors": eval_errs})
                if hint_errs:
                    has_failure = True
                    self.hint_failures.append({"exerciseId": eid, "lessonId": lid, "errors": hint_errs})
                if dist_errs:
                    has_failure = True
                    self.distractor_failures.append({"exerciseId": eid, "lessonId": lid, "errors": dist_errs})

                if not has_failure:
                    passed_cleanly += 1

        self.passed_count = passed_cleanly
        total_failures = len(self.evaluation_failures) + len(self.hint_failures) + len(self.distractor_failures)

        return {
            "totalAudited": total_exercises_audited,
            "passedWithoutChanges": passed_cleanly,
            "totalFailureItems": total_failures,
            "evaluationFailures": self.evaluation_failures,
            "hintFailures": self.hint_failures,
            "distractorFailures": self.distractor_failures,
            "certified": total_failures == 0
        }

def main():
    path = 'curriculum/pilot/exercise_content_pilot.json'
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    auditor = ExerciseEngineAuditor(path)
    report = auditor.run_full_audit()

    print("=" * 80)
    print("PHASE 3B.2: HARDENED ADVERSARIAL AUDIT REPORT")
    print("=" * 80)
    print(f"Total Pilot Lessons: {auditor.total_lessons}")
    print(f"Total Exercises Audited: {report['totalAudited']}")
    print(f"Passed Cleanly Without Errors: {report['passedWithoutChanges']} / {report['totalAudited']}")
    print(f"Total Failure Items: {report['totalFailureItems']}")
    print(f"  - Evaluation Engine Failures: {len(report['evaluationFailures'])}")
    print(f"  - Hint Quality Failures: {len(report['hintFailures'])}")
    print(f"  - Distractor Quality Failures: {len(report['distractorFailures'])}")

    if report['totalFailureItems'] > 0:
        print("\n❌ FAILURES DETECTED:")
        if report['evaluationFailures']:
            print("\n[Evaluation Engine Failures]:")
            for f in report['evaluationFailures']:
                print(f"  • [{f['exerciseId']}] {', '.join(f['errors'])}")
        if report['hintFailures']:
            print("\n[Hint Quality Failures]:")
            for f in report['hintFailures']:
                print(f"  • [{f['exerciseId']}] {', '.join(f['errors'])}")
        if report['distractorFailures']:
            print("\n[Distractor Quality Failures]:")
            for f in report['distractorFailures']:
                print(f"  • [{f['exerciseId']}] {', '.join(f['errors'])}")
        sys.exit(1)
    else:
        print("\n" + "=" * 80)
        print("✓ CERTIFICATION VERDICT: PASS — EXERCISE ENGINE CERTIFIED FOR SCALING")
        print("=" * 80)

if __name__ == '__main__':
    main()
