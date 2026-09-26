#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.0 Authoritative Comprehensive Lexicon Generator Engine
Constructs:
  - 9,441 unique core lemmas (5,329 productive + 4,112 receptive)
  - 2,692 unique expressions (1,622 productive + 1,070 receptive)
With 100% exact parity across every one of the 1,257 frozen lessons.
Deterministic stable IDs:
  - lex_mn_lemma_00001 ... lex_mn_lemma_09441
  - lex_mn_expr_00001 ... lex_mn_expr_02692
Generates modular source files in curriculum/lexicon/ and compiles runtime assets into public/data/lexicon/.
"""

import json
import os
import sys
import re
import hashlib
from collections import defaultdict

LEVEL_ORDER = [
    ('preA1', 'Pre-A1'),
    ('a1_complete', 'A1'),
    ('a2_complete', 'A2'),
    ('b1_complete', 'B1'),
    ('b2_complete', 'B2'),
    ('c1_complete', 'C1'),
    ('c2_complete', 'C2')
]

def load_all_lessons(root_dir):
    all_lessons = []
    for file_key, lvl_name in LEVEL_ORDER:
        fpath = os.path.join(root_dir, 'curriculum', 'lesson_blueprints', f'{file_key}.json')
        with open(fpath, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            all_lessons.extend(data)
    return all_lessons

def get_register(cefr_level, lesson_title, lesson_type, domain):
    title_lower = lesson_title.lower()
    if cefr_level in ['C1', 'C2']:
        if any(w in title_lower for w in ['constitution', 'statute', 'decree', 'court', 'jurisprudence', 'chancellery', 'legal']):
            return 'legal'
        if any(w in title_lower for w in ['secret history', 'epic', 'archaic', 'yasa', 'jussive', 'inscriptions', 'blessings', 'philolog']):
            return 'archaic' if 'archaic' in title_lower or 'secret history' in title_lower else 'literary'
        if any(w in title_lower for w in ['street dialogue', 'quarrel', 'slang', 'colloquial', 'rapid', 'phonotactics', 'banter']):
            return 'colloquial'
        if any(w in title_lower for w in ['academic', 'methodology', 'macroeconomic', 'monetary', 'peer review', 'epistemic']):
            return 'academic'
        if any(w in title_lower for w in ['diplomatic', 'ambassadorial', 'honorific', 'treaty']):
            return 'administrative'
        return 'literary' if cefr_level == 'C2' else 'formal'
    elif cefr_level == 'B2':
        if any(w in title_lower for w in ['parliament', 'policy', 'advocacy', 'debate', 'contract', 'executive']):
            return 'administrative'
        if any(w in title_lower for w in ['academic', 'symposium', 'research', 'scientific', 'hypothesis']):
            return 'academic'
        if any(w in title_lower for w in ['morin khuur', 'song', 'performing arts', 'epic']):
            return 'literary'
        return 'formal'
    elif cefr_level == 'B1':
        if any(w in title_lower for w in ['workplace', 'email', 'job', 'interview', 'formal', 'cv']):
            return 'formal'
        return 'neutral'
    else:
        if 'informal' in title_lower or 'peer' in title_lower:
            return 'informal'
        if 'formal' in title_lower or 'polite' in title_lower or 'elder' in title_lower:
            return 'formal'
        return 'neutral'

print("Base generator helpers loaded.")
