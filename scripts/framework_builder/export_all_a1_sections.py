"""
Export all generated A1 Section blueprints into curriculum/lesson_blueprints/
"""

import json
import os
import sys

sys.path.append("scripts/framework_builder")
import gen_sec02
import gen_sec03_full
import gen_sec04_full
import gen_sec05_full

os.makedirs("curriculum/lesson_blueprints", exist_ok=True)

sec02_lessons = gen_sec02.build_sec02()
sec03_lessons = gen_sec03_full.get_sec03_lessons()
sec04_lessons = gen_sec04_full.get_sec04_lessons()
sec05_lessons = gen_sec05_full.get_sec05_lessons()

print(f"Section 2: {len(sec02_lessons)} lessons")
print(f"Section 3: {len(sec03_lessons)} lessons")
print(f"Section 4: {len(sec04_lessons)} lessons")
print(f"Section 5: {len(sec05_lessons)} lessons")

with open("curriculum/lesson_blueprints/a1_section_02.json", "w", encoding="utf-8") as f:
    json.dump(sec02_lessons, f, ensure_ascii=False, indent=2)

with open("curriculum/lesson_blueprints/a1_section_03.json", "w", encoding="utf-8") as f:
    json.dump(sec03_lessons, f, ensure_ascii=False, indent=2)

with open("curriculum/lesson_blueprints/a1_section_04.json", "w", encoding="utf-8") as f:
    json.dump(sec04_lessons, f, ensure_ascii=False, indent=2)

with open("curriculum/lesson_blueprints/a1_section_05.json", "w", encoding="utf-8") as f:
    json.dump(sec05_lessons, f, ensure_ascii=False, indent=2)

# Load frozen Section 1
with open("curriculum/lesson_blueprints/a1_section_01.json", "r", encoding="utf-8") as f:
    sec01_lessons = json.load(f)

print(f"Section 1 (frozen): {len(sec01_lessons)} lessons")

all_a1_lessons = sec01_lessons + sec02_lessons + sec03_lessons + sec04_lessons + sec05_lessons
print(f"TOTAL A1 LESSONS: {len(all_a1_lessons)}")

with open("curriculum/lesson_blueprints/a1_complete.json", "w", encoding="utf-8") as f:
    json.dump(all_a1_lessons, f, ensure_ascii=False, indent=2)

print("Export completed successfully!")
