# -*- coding: utf-8 -*-
"""Assembles and verifies Section 03 lessons (Units 247-256, 51 lessons)."""
import json
import sys
sys.path.append('scripts/c2_authoring')
import sec03_part1
import sec03_part2

def get_all_sec03_lessons():
    lessons = []
    lessons.extend(sec03_part1.get_units_247_251()) # Units 247-251 (25)
    lessons.extend(sec03_part2.get_units_252_256()) # Units 252-256 (26)
    return lessons

if __name__ == '__main__':
    all_lessons = get_all_sec03_lessons()
    print(f"Total Section 03 lessons: {len(all_lessons)}")
    
    # Load blueprint units
    blueprint_units = {u['unitId']: u for u in json.load(open('curriculum/blueprint/units/c2.json', encoding='utf-8'))}
    
    # Verify per unit
    by_unit = {}
    for l in all_lessons:
        by_unit.setdefault(l['unitId'], []).append(l)
        
    sec03_units = [u for u in blueprint_units.values() if u['sectionId'] == 'sec_c2_03_gnomic_wisdom_epics_ceremonial_tengrism']
    print(f"Section 03 Units in blueprint: {len(sec03_units)}")
    
    all_passed = True
    for u in sec03_units:
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
        
    print(f"Overall Section 03 status: {'PASS' if all_passed else 'FAIL'}")
