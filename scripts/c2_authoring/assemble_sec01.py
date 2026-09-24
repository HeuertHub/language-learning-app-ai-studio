# -*- coding: utf-8 -*-
"""Assembles and verifies Section 01 lessons (Units 229-237, 46 lessons)."""
import json
import sys
sys.path.append('scripts/c2_authoring')
import sec01
import sec01_part2
import sec01_part3

def get_all_sec01_lessons():
    lessons = []
    lessons.extend(sec01.get_section_01_lessons()) # Units 229-230 (10)
    lessons.extend(sec01_part2.get_units_231_234()) # Units 231-234 (20)
    lessons.extend(sec01_part3.get_units_235_237()) # Units 235-237 (16)
    return lessons

if __name__ == '__main__':
    all_lessons = get_all_sec01_lessons()
    print(f"Total Section 01 lessons: {len(all_lessons)}")
    
    # Load blueprint units
    blueprint_units = {u['unitId']: u for u in json.load(open('curriculum/blueprint/units/c2.json', encoding='utf-8'))}
    
    # Verify per unit
    by_unit = {}
    for l in all_lessons:
        by_unit.setdefault(l['unitId'], []).append(l)
        
    sec01_units = [u for u in blueprint_units.values() if u['sectionId'] == 'sec_c2_01_contemporary_literature_satire_stylistics']
    print(f"Section 01 Units in blueprint: {len(sec01_units)}")
    
    all_passed = True
    for u in sec01_units:
        uid = u['unitId']
        u_lessons = by_unit.get(uid, [])
        pl = sum(l['newProductiveLemmaTarget'] for l in u_lessons)
        rl = sum(l['newReceptiveLemmaTarget'] for l in u_lessons)
        pe = sum(l['newProductiveExpressionTarget'] for l in u_lessons)
        re = sum(l['newReceptiveExpressionTarget'] for l in u_lessons)
        
        tpl = u['newProductiveCoreLemmas']
        trl = u['newReceptiveCoreLemmas']
        tpe = u['newProductiveExpressions']
        tre = u['newReceptiveExpressions']
        
        matches = (pl == tpl and rl == trl and pe == tpe and re == tre)
        status = "OK" if matches else f"MISMATCH! Got ({pl},{rl},{pe},{re}) expected ({tpl},{trl},{tpe},{tre})"
        if not matches:
            all_passed = False
        print(f"[{status}] {uid}: {len(u_lessons)} lessons")
        
    print(f"Overall Section 01 status: {'PASS' if all_passed else 'FAIL'}")
