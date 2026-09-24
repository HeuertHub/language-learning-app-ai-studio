"""
Assemble and validate B1 Section 03 lesson blueprint.
"""

import json
import sys
from author_sec03_part1 import get_sec03_part1_lessons
from author_sec03_part2 import get_sec03_part2_lessons
from author_sec03_part3 import get_sec03_part3_lessons
from author_sec03_part4 import get_sec03_part4_lessons

def main():
    lessons = []
    lessons.extend(get_sec03_part1_lessons())
    lessons.extend(get_sec03_part2_lessons())
    lessons.extend(get_sec03_part3_lessons())
    lessons.extend(get_sec03_part4_lessons())

    print(f"Total Section 03 lessons assembled: {len(lessons)}")
    assert len(lessons) == 44, f"Expected 44 lessons, got {len(lessons)}"

    # Load b1.json unit definitions
    with open("curriculum/blueprint/units/b1.json", "r") as f:
        b1_units = json.load(f)

    unit_by_seq = {u["sequencePosition"]: u for u in b1_units}

    # Normalize unitId based on unit sequence
    for l in lessons:
        seq_num = int(l["lessonId"].split("_")[2])
        if seq_num in unit_by_seq:
            canonical_uid = unit_by_seq[seq_num]["unitId"]
            l["unitId"] = canonical_uid

    # Group lessons by unit
    lessons_by_unit = {}
    lesson_ids = set()
    for l in lessons:
        lid = l["lessonId"]
        assert lid not in lesson_ids, f"Duplicate lesson ID: {lid}"
        lesson_ids.add(lid)
        uid = l["unitId"]
        lessons_by_unit.setdefault(uid, []).append(l)

    # Check budget reconciliation for units 135 to 144
    for u in b1_units[23:33]:
        uid = u["unitId"]
        u_lessons = lessons_by_unit.get(uid, [])
        assert len(u_lessons) > 0, f"No lessons for unit {uid}"
        
        pl = sum(l["newProductiveLemmaTarget"] for l in u_lessons)
        rl = sum(l["newReceptiveLemmaTarget"] for l in u_lessons)
        pe = sum(l["newProductiveExpressionTarget"] for l in u_lessons)
        re = sum(l["newReceptiveExpressionTarget"] for l in u_lessons)

        t_pl = u["newProductiveCoreLemmas"]
        t_rl = u["newReceptiveCoreLemmas"]
        t_pe = u["newProductiveExpressions"]
        t_re = u["newReceptiveExpressions"]

        print(f"Unit {u['sequencePosition']} ({uid[-25:]}): count={len(u_lessons)} "
              f"PL={pl}/{t_pl} RL={rl}/{t_rl} PE={pe}/{t_pe} RE={re}/{t_re}")

        assert pl == t_pl, f"Mismatch PL in {uid}: {pl} != {t_pl}"
        assert rl == t_rl, f"Mismatch RL in {uid}: {rl} != {t_rl}"
        assert pe == t_pe, f"Mismatch PE in {uid}: {pe} != {t_pe}"
        assert re == t_re, f"Mismatch RE in {uid}: {re} != {t_re}"

    # Write out b1_section_03.json
    out_path = "curriculum/lesson_blueprints/b1_section_03.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print(f"Successfully validated and serialized {len(lessons)} lessons to {out_path}")

if __name__ == "__main__":
    main()
