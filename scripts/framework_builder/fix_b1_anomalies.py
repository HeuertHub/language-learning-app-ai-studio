"""
Script to apply targeted reference fixes and normalization to B1 blueprint.
"""

import json

def main():
    # Load canonical unit definitions
    canonical_units = {}
    for p in ['preA1.json', 'a1.json', 'a2.json', 'b1.json']:
        with open('curriculum/blueprint/units/' + p) as f:
            for u in json.load(f):
                canonical_units[u['unitId']] = u['unitId']

    sections = [
        "curriculum/lesson_blueprints/b1_section_01.json",
        "curriculum/lesson_blueprints/b1_section_02.json",
        "curriculum/lesson_blueprints/b1_section_03.json",
        "curriculum/lesson_blueprints/b1_section_04.json"
    ]

    all_repaired_lessons = []

    for s_path in sections:
        with open(s_path, "r", encoding="utf-8") as f:
            lessons = json.load(f)

        for l in lessons:
            lid = l["lessonId"]

            # Fix 1: Reclassify Unit 154 Lesson 1
            if lid == "les_b1_154_01_hypothetical_wishes_morphosyntax_intro":
                l["lessonType"] = "vocabulary_introduction"

            # Fix 2: Unit 141 reinforcement of agentive participle
            if lid == "les_b1_141_03_mongolian_poetry_lyrics_reading":
                if "gram_b1_participle_agentive_gch" not in l["grammarPracticed"]:
                    l["grammarPracticed"].append("gram_b1_participle_agentive_gch")

            # Fix 3: Unit 121 Lesson 1 review references
            if lid == "les_b1_121_01_hospitality_booking_amenities_lexicon":
                l["reviewsLessonIds"] = ["les_a2_82_01_consumer_rights_service_disputes_lexicon"]
                l["reviewsUnitIds"] = ["unit_a2_82_retail_service_transaction_capstone"]

            # Fix 4: Unit 123 Lesson 1 review references
            if lid == "les_b1_123_01_reported_speech_tense_shift_intro":
                l["reviewsLessonIds"] = ["les_a2_99_01_reported_speech_gej_intro"]
                l["reviewsUnitIds"] = ["unit_a2_99_reporting_third_party_statements_ve"]

            # Fix 5: Unit 140 Lesson 1 review references
            if lid == "les_b1_140_01_agentive_participle_morphology_intro":
                l["reviewsLessonIds"] = ["les_b1_112_03_competency_lexicon_qualifications"]

            # Fix 6: Unit 155 Lesson 6 capstone review reference
            if lid == "les_b1_155_06_b1_level_culminating_mastery_capstone":
                l["reviewsLessonIds"] = [
                    "les_b1_123_06_section_01_milestone_synthesis_checkpoint" if r == "les_b1_123_05_personal_banking_portfolio_spoken" else r
                    for r in l.get("reviewsLessonIds", [])
                ]

            # Fix 7: Canonicalize reviewsUnitIds
            new_ru = []
            for ru in l.get("reviewsUnitIds", []):
                if ru in canonical_units:
                    new_ru.append(ru)
                else:
                    # Find canonical match by prefix
                    prefix = ru[:20]
                    matches = [u for u in canonical_units.values() if u.startswith(prefix)]
                    if matches:
                        new_ru.append(matches[0])
                    else:
                        print(f"Warning: unresolved unit {ru} in {lid}")
                        new_ru.append(ru)
            l["reviewsUnitIds"] = new_ru

        # Resave section file
        with open(s_path, "w", encoding="utf-8") as f:
            json.dump(lessons, f, ensure_ascii=False, indent=2)
        print(f"Updated {s_path}")
        all_repaired_lessons.extend(lessons)

    # Resave b1_complete.json
    with open("curriculum/lesson_blueprints/b1_complete.json", "w", encoding="utf-8") as f:
        json.dump(all_repaired_lessons, f, ensure_ascii=False, indent=2)
    print(f"Updated b1_complete.json with {len(all_repaired_lessons)} lessons")

if __name__ == "__main__":
    main()
