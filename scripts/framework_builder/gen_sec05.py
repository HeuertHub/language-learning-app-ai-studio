"""
Section 5 Master Generator: Units 103 - 111 (42 Lessons)
"""

import json
from scripts.framework_builder.gen_sec05_part1 import get_sec05_part1_lessons
from scripts.framework_builder.gen_sec05_part2 import get_sec05_part2_lessons
from scripts.framework_builder.gen_sec05_part3 import get_sec05_part3_lessons

def get_sec05_lessons():
    with open("curriculum/blueprint/units/a2.json", "r", encoding="utf-8") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}

    lessons = []
    lessons.extend(get_sec05_part1_lessons(u_map))
    lessons.extend(get_sec05_part2_lessons(u_map))
    lessons.extend(get_sec05_part3_lessons(u_map))

    # Verify lexical budget for each unit in Section 5 (103-111)
    lessons_by_unit = {}
    for l in lessons:
        uid = l["unitId"]
        if uid not in lessons_by_unit:
            lessons_by_unit[uid] = []
        lessons_by_unit[uid].append(l)

    for seq in range(103, 112):
        u = u_map[seq]
        uid = u["unitId"]
        u_lessons = lessons_by_unit.get(uid, [])
        prod_l = sum(l["newProductiveLemmaTarget"] for l in u_lessons)
        rec_l = sum(l["newReceptiveLemmaTarget"] for l in u_lessons)
        prod_e = sum(l["newProductiveExpressionTarget"] for l in u_lessons)
        rec_e = sum(l["newReceptiveExpressionTarget"] for l in u_lessons)

        exp_prod_l = u["newProductiveCoreLemmas"]
        exp_rec_l = u["newReceptiveCoreLemmas"]
        exp_prod_e = u["newProductiveExpressions"]
        exp_rec_e = u["newReceptiveExpressions"]

        print(f"Unit {seq} ({len(u_lessons)} les): ProdL={prod_l}/{exp_prod_l}, RecL={rec_l}/{exp_rec_l}, ProdE={prod_e}/{exp_prod_e}, RecE={rec_e}/{exp_rec_e}")
        assert prod_l == exp_prod_l, f"Unit {seq} ProdL mismatch: {prod_l} != {exp_prod_l}"
        assert rec_l == exp_rec_l, f"Unit {seq} RecL mismatch: {rec_l} != {exp_rec_l}"
        assert prod_e == exp_prod_e, f"Unit {seq} ProdE mismatch: {prod_e} != {exp_prod_e}"
        assert rec_e == exp_rec_e, f"Unit {seq} RecE mismatch: {rec_e} != {exp_rec_e}"

    return lessons

if __name__ == "__main__":
    sec05 = get_sec05_lessons()
    print(f"Total Section 5 lessons: {len(sec05)}")
    with open("curriculum/lesson_blueprints/a2_section_05.json", "w", encoding="utf-8") as f:
        json.dump(sec05, f, ensure_ascii=False, indent=2)
    print("Successfully saved curriculum/lesson_blueprints/a2_section_05.json")
