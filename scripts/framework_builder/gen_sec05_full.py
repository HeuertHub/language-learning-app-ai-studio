"""
Unified Section 5 Lessons Generator (Units 54 - 63: 60 lessons)
"""

import sys
from typing import List, Dict, Any
from gen_sec05_part1 import get_sec05_part1_lessons
from gen_sec05_part2 import get_sec05_part2_lessons

def get_sec05_lessons() -> List[Dict[str, Any]]:
    return get_sec05_part1_lessons() + get_sec05_part2_lessons()

if __name__ == "__main__":
    lessons = get_sec05_lessons()
    print(f"Generated {len(lessons)} Section 5 lessons successfully.")
