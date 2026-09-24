# -*- coding: utf-8 -*-
"""Assembles and verifies Section 02 lessons (Units 238-246, 46 lessons)."""
import json
import sys
sys.path.append('scripts/c2_authoring')
import sec02_part1
import sec02_part2

def get_all_sec02_lessons():
    lessons = []
    lessons.extend(sec02_part1.get_units_238_242()) # Units 238-242 (25)
    lessons.extend(sec02_part2.get_units_243_246()) # Units 243-246 (21)
    return lessons

if __name__ == '__main__':
    all_lessons = get_all_sec02_lessons()
    print(f"Total Section 02 lessons: {len(all_lessons)}")
    
    # Load blueprint units
    blueprint_units = {u['unitId']: u for u in json.load(open('curriculum/blueprint/units/c2.json', encoding='utf-8'))}
    
    # Verify per unit
    by_unit = {}
    for l in all_lessons:
        by_unit.setdefault(l['unitId'], []).append(l)
        
    sec02_units = [u for u in blueprint_units.values() if u['sectionId'] == 'sec_c2_02_secret_history_classical_mongolian_philology']
    print(f"Section 02 Units in blueprint: {len(sec02_units)}")
    
    all_passed = True
    for u in sec02_units:
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
        
    print(f"Overall Section 02 status: {'PASS' if all_passed else 'FAIL'}")
