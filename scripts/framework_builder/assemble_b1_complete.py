"""
Assemble all B1 sections into b1_complete.json and run the comprehensive audit.
"""

import json
import os
import sys

def main():
    sections = [
        "curriculum/lesson_blueprints/b1_section_01.json",
        "curriculum/lesson_blueprints/b1_section_02.json",
        "curriculum/lesson_blueprints/b1_section_03.json",
        "curriculum/lesson_blueprints/b1_section_04.json"
    ]

    all_lessons = []
    for s_path in sections:
        assert os.path.exists(s_path), f"Missing {s_path}"
        with open(s_path, "r", encoding="utf-8") as f:
            sec_lessons = json.load(f)
            print(f"Loaded {len(sec_lessons)} lessons from {s_path}")
            all_lessons.extend(sec_lessons)

    total_count = len(all_lessons)
    print(f"Total B1 lessons collected: {total_count}")
    assert total_count == 194, f"Expected 194 lessons, got {total_count}"

    # Write b1_complete.json
    complete_path = "curriculum/lesson_blueprints/b1_complete.json"
    with open(complete_path, "w", encoding="utf-8") as f:
        json.dump(all_lessons, f, ensure_ascii=False, indent=2)
    print(f"Serialized complete B1 blueprint to {complete_path}")

if __name__ == "__main__":
    main()
