"""
Builder script for gen_sec05_part2.py (Units 59 - 63: 30 lessons)
Concluding the entire A1 level!
"""

sec05_part2_code = '''"""
Section 5 Generator - Part 2 (Units 59 - 63: 30 lessons)
Prospective Future, Prohibitions, Spatial Postpositions, Weather, and A1 Capstone!
"""

import json
from typing import List, Dict, Any

def get_sec05_part2_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}
    lessons = []

    # =========================================================================
    # UNIT 59: Prospective Future Marker: Suffixes -на/-нэ/-но/-нө (pos 59)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[59]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_59_01_prospective_future_na_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Looking Ahead: The Prospective Future Marker -на/-нэ/-но/-нө",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the prospective future marker suffix -на/-нэ/-но/-нө denoting definite upcoming actions, scheduled events, and commitments, governed by four-way vowel harmony.",
            "communicativeOutcome": "State scheduled future actions, upcoming meetings, and tomorrow's plans (e.g. 'Би маргааш явна', 'Бид орой уулзана').",
            "objectivesIntroduced": ["obj_a1_59_01_form_prospective_future_na"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_58_01_form_perfective_past_san"],
            "grammarIntroduced": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarReinforced": ["gram_a1_verb_tense_past_perfective_san"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_time_calendar", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["маргааш", "нөгөөдөр", "ирэх", "явах", "уулзах"],
            "readingObjective": "Read weekly appointment calendars and scheduled program listings.",
            "listeningObjective": "Hear the four vowel harmonic allomorphs (-на/-нэ/-но/-нө) in upcoming schedule announcements.",
            "writingObjective": "Attach future suffixes to 6 action verbs respecting four-way vowel harmony.",
            "spokenProductionObjective": "Announce 3 activities you will do tomorrow using -на/-нэ aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear articulation of future intentions and temporal commitments.",
            "prerequisiteLessonIds": ["les_a1_58_06_section_05_mid_checkpoint"],
            "reviewsLessonIds": ["les_a1_58_01_perfective_past_san_allomorphs"],
            "reviewsUnitIds": ["unit_a1_58_perfective_past_participle_suffixes"],
            "reviewReason": "Contrast completed past (-сан) with prospective future (-на).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of future tense suffixes across vowel classes.",
            "successCriteria": [
                "Select -на for /a/, -нэ for /e, i/, -но for /o/, -нө for /ö/ stems.",
                "Contrast past completed action with future scheduled action."
            ],
            "masteryEvidence": [
                "Conjugates явах -> явна, ирэх -> ирнэ, уулзах -> уулзана accurately.",
                "Answers 'Та маргааш юу хийх вэ?' with a well-formed future statement."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "future_scheduling", "cued_production"]
        },
        {
            "lessonId": "les_a1_59_02_future_temporal_anchors_and_plans",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Future Anchors: Ирэх Долоо Хоногт, Дараа Сард, and Цаашид",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce future time expressions: ирэх долоо хоногт 'next week', ирэх сард 'next month', дараа жил 'next year', удахгүй 'soon', цаашид 'in the future'.",
            "communicativeOutcome": "Anchor prospective actions to specific future dates and timeframes with precision.",
            "objectivesIntroduced": ["obj_a1_59_02_anchor_future_plans"],
            "objectivesPracticed": ["obj_a1_59_01_form_prospective_future_na"],
            "objectivesReviewed": ["obj_a1_36_01_state_calendar_dates"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_time_calendar"],
            "previousVocabularyReused": ["долоо хоног", "сар", "жил", "уулзах", "явах"],
            "readingObjective": "Read forward-looking travel itineraries and conference program schedules.",
            "listeningObjective": "Comprehend colleagues stating when future milestones or exams will occur.",
            "writingObjective": "Draft a 3-point upcoming schedule outline for the next two months.",
            "spokenProductionObjective": "Explain to a peer what you will do next weekend and next month aloud.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Accurate temporal framing of commitments and upcoming plans.",
            "prerequisiteLessonIds": ["les_a1_59_01_prospective_future_na_allomorphs"],
            "reviewsLessonIds": ["les_a1_36_01_calendar_dates_and_ordinal_suffixes"],
            "reviewsUnitIds": ["unit_a1_36_calendar_dates_months_seasons"],
            "reviewReason": "Combine temporal calendar nouns with prospective future verb forms.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Brisk, forward-looking schedule planning cadence.",
            "successCriteria": [
                "Combine future time adverbs with -на verbs naturally.",
                "Distinguish between 'өнгөрсөн долоо хоног' (past) and 'ирэх долоо хоног' (future)."
            ],
            "masteryEvidence": [
                "Produces 'Бид ирэх сард Хөвсгөл рүү явна' without errors.",
                "Correctly places 3 future events onto a timeline diagram."
            ],
            "recommendedExerciseModalities": ["itinerary_matching", "timeline_sequencing", "roleplay"]
        },
        {
            "lessonId": "les_a1_59_03_weekend_commitments_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Coordinating Weekend Plans and Mutual Appointments",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate negotiating weekend plans, setting up appointments, and asking 'Та амралтын өдрүүдээр юу хийх вэ?' with coordinated responses.",
            "communicativeOutcome": "Negotiate meeting times, propose activities, and confirm upcoming social arrangements.",
            "objectivesIntroduced": ["obj_a1_59_03_coordinate_future_plans"],
            "objectivesPracticed": [
                "obj_a1_59_01_form_prospective_future_na",
                "obj_a1_59_02_anchor_future_plans"
            ],
            "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarReviewed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["хагас сайн", "бүтэн сайн", "амралт", "уулзах", "кино"],
            "readingObjective": "Read calendar invites and SMS group plans for the upcoming weekend.",
            "listeningObjective": "Comprehend friends proposing alternative meeting times and confirming commitments.",
            "writingObjective": "Write a 4-line invitation message proposing a Saturday afternoon meet-up.",
            "spokenProductionObjective": "Ask a peer about their Sunday plans and agree on a meeting time aloud.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Collaborative social scheduling and mutual consensus building.",
            "prerequisiteLessonIds": ["les_a1_59_02_future_temporal_anchors_and_plans"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Combine volitional proposal ('уулзъя') with definite future commitment ('уулзана').",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm conversational audio planning social gatherings.",
            "successCriteria": [
                "Contrast 'Уулзъя!' (Let's meet!) with 'Маргааш уулзана' (We will meet tomorrow).",
                "Negotiate mutually agreeable time without code-switching."
            ],
            "masteryEvidence": [
                "Executes a 6-turn plan coordination dialogue smoothly.",
                "Records agreed meeting time and location accurately."
            ],
            "recommendedExerciseModalities": ["calendar_negotiation", "dialogue_completion", "roleplay"]
        },
        {
            "lessonId": "les_a1_59_04_itineraries_and_schedules_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Travel Tour Itineraries and Conference Schedules",
            "lessonType": "reading_development",
            "primaryPurpose": "Read 80-word official schedules and travel itineraries detailing departure times, scheduled site visits, and meal hours across 3 days.",
            "communicativeOutcome": "Extract departure times, destination venues, and scheduled activities from written itineraries.",
            "objectivesIntroduced": ["obj_a1_59_04_read_future_itineraries"],
            "objectivesPracticed": [
                "obj_a1_59_01_form_prospective_future_na",
                "obj_a1_59_02_anchor_future_plans"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport", "lex_a1_time_calendar"],
            "previousVocabularyReused": ["өдөр", "цаг", "хөдлөх", "хооллох", "хүрэх"],
            "readingObjective": "Read a 3-day countryside tour itinerary detailing morning departures, museum visits, and evening campfires.",
            "listeningObjective": None,
            "writingObjective": "Fill in a schedule matrix detailing Day 1, Day 2, and Day 3 key events from the reading.",
            "spokenProductionObjective": None,
            "registerTarget": "Public tourism schedule standard",
            "pragmaticTarget": "Interpreting published commercial schedules and tour programs.",
            "prerequisiteLessonIds": ["les_a1_59_03_weekend_commitments_guided_drills"],
            "reviewsLessonIds": ["les_a1_59_01_prospective_future_na_allomorphs"],
            "reviewsUnitIds": ["unit_a1_59_prospective_future_marker_suffixes_"],
            "reviewReason": "Consolidate written recognition of prospective future verbs in structured schedules.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear, professional voice reading official tour schedules.",
            "successCriteria": [
                "Identify departure time and meeting point for each day.",
                "Extract meal locations and overnight accommodation sites."
            ],
            "masteryEvidence": [
                "Answers 4 itinerary comprehension questions with 100% accuracy.",
                "Populates the schedule matrix without factual errors."
            ],
            "recommendedExerciseModalities": ["itinerary_scanning", "matrix_completion", "short_answer"]
        },
        {
            "lessonId": "les_a1_59_05_schedule_announcements_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Public Schedule Changes and Future Announcements",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal announcements regarding transit schedules, opening hours changes, and upcoming event dates.",
            "communicativeOutcome": "Accurately record future dates, changed hours, and scheduled activities from spoken public broadcasts.",
            "objectivesIntroduced": ["obj_a1_59_05_parse_future_announcements_audio"],
            "objectivesPracticed": ["obj_a1_59_01_form_prospective_future_na"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport", "lex_a1_time_calendar"],
            "previousVocabularyReused": ["цаг", "эхлэх", "дуусах", "хөдлөх", "хоцрох"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 public transport and broadcast schedule announcements and record departure and arrival times.",
            "writingObjective": "Transcribe the future tense verbs and temporal phrases heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Public announcement standard",
            "pragmaticTarget": "Auditory precision parsing rapid broadcast announcements with background transit noise.",
            "prerequisiteLessonIds": ["les_a1_59_03_weekend_commitments_guided_drills"],
            "reviewsLessonIds": ["les_a1_59_02_future_temporal_anchors_and_plans"],
            "reviewsUnitIds": ["unit_a1_59_prospective_future_marker_suffixes_"],
            "reviewReason": "Zero-vocabulary auditory lab training future tense acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic public transit PA announcements with authentic acoustics.",
            "successCriteria": [
                "Extract 4 scheduled departure/event times accurately.",
                "Identify when an event has been postponed to a later date."
            ],
            "masteryEvidence": [
                "Scores 100% on the schedule announcement listening test.",
                "Transcribes all future tense forms (-на/-нэ) accurately."
            ],
            "recommendedExerciseModalities": ["audio_schedule_completion", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_59_06_future_plans_interview_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Planning Next Year and Life Goals",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Conduct an extended conversational interview discussing future plans: what you will do next weekend, where you will travel next summer, and what you will study next year.",
            "communicativeOutcome": "Conduct a fluid, forward-looking discussion articulating personal aspirations and near-future commitments.",
            "objectivesIntroduced": ["obj_a1_59_06_conduct_future_plans_interview"],
            "objectivesPracticed": [
                "obj_a1_59_01_form_prospective_future_na",
                "obj_a1_59_02_anchor_future_plans",
                "obj_a1_59_03_coordinate_future_plans"
            ],
            "objectivesReviewed": ["obj_a1_58_06_section_05_mid_mastery"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_future_prospective_na"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_verb_tense_past_perfective_san"],
            "grammarReinforced": ["gram_a1_verb_tense_past_perfective_san"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_travel_transport"],
            "previousVocabularyReused": ["маргааш", "ирэх жил", "хийх", "явах", "сургууль", "сайхан", "баярлалаа"],
            "readingObjective": "Read peer goal prompt cards.",
            "listeningObjective": "Comprehend partner sharing their future dreams and scheduled travels.",
            "writingObjective": "Draft a short 4-sentence profile summarizing your partner's top 3 future commitments.",
            "spokenProductionObjective": "Execute an 8-turn reciprocal interview contrasting past experiences with future goals.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Supportive peer dialogue discussing aspirations and realistic commitments.",
            "prerequisiteLessonIds": [
                "les_a1_59_04_itineraries_and_schedules_reading",
                "les_a1_59_05_schedule_announcements_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_59_03_weekend_commitments_guided_drills"],
            "reviewsUnitIds": ["unit_a1_59_prospective_future_marker_suffixes_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 59 future tense skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating forward-looking goal sharing.",
            "successCriteria": [
                "Use prospective future forms (-на/-нэ) in every predictive statement.",
                "Inquire about partner's plans using 'Та дараа жил юу хийх вэ?'."
            ],
            "masteryEvidence": [
                "Completes future goal interview in under 2 minutes fluently.",
                "Both partners produce matching written summaries of each other's plans."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "goal_interview", "profile_drafting"]
        }
    ])

    return lessons
'''

with open("scripts/framework_builder/gen_sec05_part2.py", "w") as f:
    f.write(sec05_part2_code)

print("gen_sec05_part2.py initialized with Unit 59!")
