# -*- coding: utf-8 -*-
"""Assembles all C2 lesson blueprints into curriculum/lesson_blueprints/c2_complete.json."""
import json
import os
import sys
sys.path.append('scripts/c2_authoring')

import assemble_sec01
import assemble_sec02
import assemble_sec03

def build_c2_complete():
    lessons = []
    lessons.extend(assemble_sec01.get_all_sec01_lessons()) # 46 lessons
    lessons.extend(assemble_sec02.get_all_sec02_lessons()) # 46 lessons
    lessons.extend(assemble_sec03.get_all_sec03_lessons()) # 51 lessons
    
    print(f"Total compiled C2 lessons: {len(lessons)}")
    
    out_dir = 'curriculum/lesson_blueprints'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'c2_complete.json')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully wrote {len(lessons)} lessons to {out_path}")

if __name__ == '__main__':
    build_c2_complete()
