"""
Unified Section 4 Lessons Generator (Units 45 - 53: 50 lessons)
"""

import sys
from typing import List, Dict, Any
from gen_sec04_part1 import get_sec04_part1_lessons
from gen_sec04_part2 import get_sec04_part2_lessons

def get_sec04_lessons() -> List[Dict[str, Any]]:
    return get_sec04_part1_lessons() + get_sec04_part2_lessons()

if __name__ == "__main__":
    lessons = get_sec04_lessons()
    print(f"Generated {len(lessons)} Section 4 lessons successfully.")
