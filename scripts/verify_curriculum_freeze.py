#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic Curriculum Freeze Verifier
Validates all 43 entries in curriculum/CURRICULUM_FREEZE_MANIFEST.json:
- Ensures all 43 files exist
- Computes SHA-256 for each file and checks against the frozen manifest
- Reads the complete lesson blueprint files and verifies exactly 1,257 authoritative lessons
- Exits 0 on success, exits 1 on any failure
"""

import os
import sys
import json
import hashlib

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    manifest_path = os.path.join(root_dir, 'curriculum', 'CURRICULUM_FREEZE_MANIFEST.json')

    print("=" * 80)
    print("FROZEN CURRICULUM INTEGRITY & HASH VERIFICATION")
    print("=" * 80)

    if not os.path.exists(manifest_path):
        print(f"❌ FATAL: Manifest not found at {manifest_path}")
        sys.exit(1)

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    files = manifest.get('files', {})
    expected_count = 43
    if len(files) != expected_count:
        print(f"❌ FATAL: Expected {expected_count} manifest entries, found {len(files)}")
        sys.exit(1)

    print(f"Manifest Status: {manifest.get('status')}")
    print(f"Freeze Timestamp: {manifest.get('freeze_timestamp')}")
    print(f"Verifying {len(files)} frozen files across blueprints and lessons...\n")

    missing = []
    mismatches = []
    verified_count = 0

    for rel_path, meta in files.items():
        full_path = os.path.join(root_dir, rel_path)
        if not os.path.exists(full_path):
            missing.append(rel_path)
            print(f"  ❌ MISSING: {rel_path}")
            continue

        with open(full_path, 'rb') as f:
            content = f.read()

        computed_sha = hashlib.sha256(content).hexdigest()
        expected_sha = meta['sha256']
        expected_size = meta['size_bytes']
        actual_size = len(content)

        if computed_sha != expected_sha:
            mismatches.append((rel_path, expected_sha, computed_sha))
            print(f"  ❌ HASH MISMATCH: {rel_path}")
            print(f"     Expected: {expected_sha}")
            print(f"     Computed: {computed_sha}")
        elif actual_size != expected_size:
            mismatches.append((rel_path, f"size {expected_size}", f"size {actual_size}"))
            print(f"  ❌ SIZE MISMATCH: {rel_path} (Expected {expected_size}, got {actual_size})")
        else:
            verified_count += 1

    print(f"\nVerification Results:")
    print(f"  • Verified Clean: {verified_count} / {len(files)}")
    print(f"  • Missing Files:  {len(missing)}")
    print(f"  • Hash Failures:  {len(mismatches)}")

    if missing or mismatches:
        print("\n❌ VERIFICATION FAILED: Frozen curriculum files have been altered or are missing.")
        sys.exit(1)

    # Verify lesson counts across complete level blueprint files
    complete_blueprints = [
        ('Pre-A1', 'curriculum/lesson_blueprints/preA1.json'),
        ('A1', 'curriculum/lesson_blueprints/a1_complete.json'),
        ('A2', 'curriculum/lesson_blueprints/a2_complete.json'),
        ('B1', 'curriculum/lesson_blueprints/b1_complete.json'),
        ('B2', 'curriculum/lesson_blueprints/b2_complete.json'),
        ('C1', 'curriculum/lesson_blueprints/c1_complete.json'),
        ('C2', 'curriculum/lesson_blueprints/c2_complete.json'),
    ]

    total_lessons = 0
    lesson_breakdown = {}
    for level_name, rel_path in complete_blueprints:
        full_path = os.path.join(root_dir, rel_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        count = len(data)
        lesson_breakdown[level_name] = count
        total_lessons += count

    print("\nAuthoritative Lesson Count Breakdown:")
    for lvl, cnt in lesson_breakdown.items():
        print(f"  • {lvl:6s}: {cnt:4d} lessons")
    print(f"  • Total : {total_lessons:4d} lessons (Target: {manifest.get('total_authoritative_lessons', 1257)})")

    expected_total_lessons = manifest.get('total_authoritative_lessons', 1257)
    if total_lessons != expected_total_lessons:
        print(f"\n❌ LESSON COUNT MISMATCH: Expected {expected_total_lessons}, got {total_lessons}")
        sys.exit(1)

    print("\n" + "=" * 80)
    print("✓ CURRICULUM FREEZE VERIFICATION PASSED: All 43 files intact, 1,257 lessons verified.")
    print("=" * 80)
    sys.exit(0)

if __name__ == '__main__':
    main()
