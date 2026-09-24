# -*- coding: utf-8 -*-
"""Pedagogical sampling and C2 authenticity audit across Sections 01, 02, and 03."""
import json

def pedagogical_audit():
    with open('curriculum/lesson_blueprints/c2_complete.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)
        
    sec01 = [l for l in lessons if 229 <= int(l['unitId'].split('_')[2]) <= 237]
    sec02 = [l for l in lessons if 238 <= int(l['unitId'].split('_')[2]) <= 246]
    sec03 = [l for l in lessons if 247 <= int(l['unitId'].split('_')[2]) <= 256]
    
    print(f"Sec 01 count: {len(sec01)}, Sec 02 count: {len(sec02)}, Sec 03 count: {len(sec03)}")
    
    # Sample 20 from each
    import random
    random.seed(42) # deterministic sampling
    sample_sec01 = sorted(random.sample(sec01, 20), key=lambda x: x['lessonId'])
    sample_sec02 = sorted(random.sample(sec02, 20), key=lambda x: x['lessonId'])
    sample_sec03 = sorted(random.sample(sec03, 20), key=lambda x: x['lessonId'])
    
    for sec_num, sample in [(1, sample_sec01), (2, sample_sec02), (3, sample_sec03)]:
        print(f"\n--- SECTION {sec_num} SAMPLE (20 LESSONS) ---")
        for i, l in enumerate(sample, 1):
            print(f"{i:02d}. [{l['lessonId']}] ({l['lessonType']}) - {l['title']}")
            print(f"    Register: {l['registerTarget']}")
            print(f"    Pragmatic: {l['pragmaticTarget']}")
            print(f"    Outcome: {l['communicativeOutcome'][:100]}...")

if __name__ == '__main__':
    pedagogical_audit()
