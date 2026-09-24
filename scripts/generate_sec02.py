import json

with open("curriculum/blueprint/units/b2.json") as f:
    b2_units = {u["unitId"]: u for u in json.load(f)}

# Let's import the full list of lessons for Section 02
from build_sec02_full import sec02_lessons

print(f"Total Section 02 lessons authored: {len(sec02_lessons)}")

# Verify unit allocations
unit_sums = {}
for l in sec02_lessons:
    uid = l["unitId"]
    if uid not in unit_sums:
        unit_sums[uid] = {"PL": 0, "RL": 0, "PE": 0, "RE": 0, "count": 0}
    unit_sums[uid]["PL"] += l["newProductiveLemmaTarget"]
    unit_sums[uid]["RL"] += l["newReceptiveLemmaTarget"]
    unit_sums[uid]["PE"] += l["newProductiveExpressionTarget"]
    unit_sums[uid]["RE"] += l["newReceptiveExpressionTarget"]
    unit_sums[uid]["count"] += 1

mismatches = 0
for uid, sums in sorted(unit_sums.items()):
    u = b2_units[uid]
    exp = (u["newProductiveCoreLemmas"], u["newReceptiveCoreLemmas"], u["newProductiveExpressions"], u["newReceptiveExpressions"])
    act = (sums["PL"], sums["RL"], sums["PE"], sums["RE"])
    if exp != act:
        print(f"MISMATCH in {uid}: Expected {exp}, got {act}")
        mismatches += 1
    else:
        print(f"OK {u['sequencePosition']}: {uid} ({sums['count']} lessons) -> {act}")

if mismatches == 0:
    print("All 10 Section 02 Units reconciled perfectly!")
    with open("curriculum/lesson_blueprints/b2_section_02.json", "w", encoding="utf-8") as f:
        json.dump(sec02_lessons, f, indent=2, ensure_ascii=False)
    print("Saved curriculum/lesson_blueprints/b2_section_02.json")
else:
    print(f"Found {mismatches} mismatches. Fix before saving.")
