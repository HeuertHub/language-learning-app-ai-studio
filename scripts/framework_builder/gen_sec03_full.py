"""
Full Section 3 Generator: Units 34 to 44 (63 lessons)
"""

import json
from typing import List, Dict, Any

def get_sec03_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}
    lessons = []

    # Import Unit 34 from build_sec03
    from build_sec03 import build_sec03
    lessons.extend(build_sec03())

    # =========================================================================
    # UNIT 35: Days of the Week & Weekly Calendars (pos 35)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[35]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_35_01_weekdays_tibetan_and_numerical",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Naming the Days: Даваа to Ням and Numerical Days",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce the seven days of the week in standard colloquial usage (даваа, мягмар, лхагва, пүрэв, баасан, бямба, ням) and numerical weekday conventions (нэг дэх өдөр ... долоо дахь өдөр).",
            "communicativeOutcome": "State and identify days of the week in both traditional and colloquial numerical counting systems.",
            "objectivesIntroduced": ["obj_a1_35_01_identify_weekdays"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_34_01_tell_hours_and_half_hours"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["өдөр", "гариг", "өнөөдөр", "маргааш"],
            "readingObjective": "Read weekly calendar columns and appointment planners displaying day abbreviations (Да, Мя, Лх, Пү, Ба, Бя, Ня).",
            "listeningObjective": "Hear spoken mentions of weekdays in school class schedules and business opening hours.",
            "writingObjective": "Write the seven days of the week in chronological order starting from Monday (Даваа).",
            "spokenProductionObjective": "State what day today, tomorrow, and yesterday are upon inquiry.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear day designation avoiding scheduling confusion between numerical and Tibetan names.",
            "prerequisiteLessonIds": ["les_a1_34_06_schedule_synchronization_synthesis"],
            "reviewsLessonIds": ["les_a1_34_01_exact_hours_and_half_hours"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Anchor clock times to specific days of the week.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear pronunciation of initial consonant clusters in weekday loanwords (лхагва, пүрэв, бямба).",
            "successCriteria": [
                "Map colloquial numerical days (нэг дэх өдөр) to standard names (даваа гариг) without hesitation.",
                "Recite all seven days in forward and reverse sequence."
            ],
            "masteryEvidence": [
                "Answers 'Өнөөдөр ямар өдөр вэ?' immediately with the correct weekday.",
                "Accurately spells Tibetan-origin day names in Cyrillic."
            ],
            "recommendedExerciseModalities": ["calendar_mapping", "cued_production", "matching"]
        },
        {
            "lessonId": "les_a1_35_02_relative_days_and_weekend_cycles",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Relative Time: Өнөөдөр, Маргааш, and Амралтын Өдөр",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce relative diurnal anchors (өчигдөр, өнөөдөр, маргааш, нөгөөдөр) and distinction between workdays (ажлын өдөр) and weekends (амралтын өдөр).",
            "communicativeOutcome": "Discuss upcoming commitments and weekly routine boundaries relative to the present day.",
            "objectivesIntroduced": ["obj_a1_35_02_use_relative_day_anchors"],
            "objectivesPracticed": ["obj_a1_35_01_identify_weekdays"],
            "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["өдөр", "ажил", "хичээл", "байхгүй"],
            "readingObjective": "Read office holiday notices announcing workdays and weekend closures.",
            "listeningObjective": "Comprehend colleagues discussing their weekend plans and upcoming day off.",
            "writingObjective": "Draft a 3-sentence weekly overview contrasting workday tasks with weekend rest.",
            "spokenProductionObjective": "State aloud one's plans for tomorrow and this coming weekend.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Casual, polite inquiries into peer availability across the week.",
            "prerequisiteLessonIds": ["les_a1_35_01_weekdays_tibetan_and_numerical"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine existential assertion with weekly events ('Маргааш хичээл байна').",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural prosody linking relative time adverbs with declarative predicates.",
            "successCriteria": [
                "Use 'өчигдөр', 'өнөөдөр', 'маргааш', 'нөгөөдөр' chronologically without confusion.",
                "Distinguish 'ажлын өдрүүд' (Mon-Fri) from 'амралтын өдрүүд' (Sat-Sun)."
            ],
            "masteryEvidence": [
                "Identifies 'нөгөөдөр' as the day after tomorrow across 3 prompt scenarios.",
                "Produces 'Бямба, Ням бол амралтын өдөр' spontaneously."
            ],
            "recommendedExerciseModalities": ["timeline_ordering", "cloze_selection", "cued_production"]
        },
        {
            "lessonId": "les_a1_35_03_weekly_schedule_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Academic and Fitness Weekly Schedules",
            "lessonType": "reading_development",
            "primaryPurpose": "Read structured weekly timetable grids for university courses, sports clubs, and library study sessions.",
            "communicativeOutcome": "Locate specific course lectures, gym classes, and instructor office hours from complex multi-day timetable grids.",
            "objectivesIntroduced": ["obj_a1_35_03_read_weekly_grids"],
            "objectivesPracticed": [
                "obj_a1_35_01_identify_weekdays",
                "obj_a1_35_02_use_relative_day_anchors"
            ],
            "objectivesReviewed": ["obj_a1_25_03_read_building_directories"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["хичээл", "багш", "өрөө", "цаг", "эхлэх"],
            "readingObjective": "Read a 60-word university semester timetable grid spanning Monday to Friday.",
            "listeningObjective": None,
            "writingObjective": "Transcribe 4 scheduled classes into an agenda listing day, time, and room number.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Efficient cross-referencing of two-dimensional schedule tables.",
            "prerequisiteLessonIds": ["les_a1_35_02_relative_days_and_weekend_cycles"],
            "reviewsLessonIds": ["les_a1_25_03_urban_directory_reading"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine weekday columns with room locative markers (Мягмар гаригт 204 тоотод).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Informational narration reading scheduled appointments with clear clarity.",
            "successCriteria": [
                "Locate Friday afternoon activities on a 5-day grid accurately.",
                "Extract course titles and classroom locations matching target days."
            ],
            "masteryEvidence": [
                "Answers 4 timetable factual queries with zero error.",
                "Identifies open time slots suitable for scheduling a new study group."
            ],
            "recommendedExerciseModalities": ["grid_scanning", "schedule_transcription", "matching"]
        },
        {
            "lessonId": "les_a1_35_04_weekly_routine_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Tracking Weekly Commitments in Conversational Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse spoken descriptions of friends and colleagues explaining their busy weekly schedules.",
            "communicativeOutcome": "Accurately record on which days of the week different speakers have classes, work shifts, and appointments.",
            "objectivesIntroduced": ["obj_a1_35_04_track_spoken_weekly_commitments"],
            "objectivesPracticed": ["obj_a1_35_01_identify_weekdays"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["даваа", "лхагва", "баасан", "ажил", "чөлөөтэй"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 speakers describing their weekly routines and note which days they are busy or free.",
            "writingObjective": "Fill in a blank 7-day schedule grid from audio descriptions.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Identifying availability markers ('Би баасанд завтай') in informal speech.",
            "prerequisiteLessonIds": ["les_a1_35_02_relative_days_and_weekend_cycles"],
            "reviewsLessonIds": ["les_a1_35_01_weekdays_tibetan_and_numerical"],
            "reviewsUnitIds": ["unit_a1_35_days_of_the_week_weekly_calendars"],
            "reviewReason": "Zero-vocabulary auditory lab sharpening weekday recognition in rapid speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio with varied speaker rates and natural day contractions.",
            "successCriteria": [
                "Correctly map 4 speakers' busy days onto calendar tracks.",
                "Distinguish between 'даваа' and 'баасан' when spoken rapidly."
            ],
            "masteryEvidence": [
                "Scores 100% on the multi-speaker weekday listening classification test.",
                "Detects which speaker has no classes on Wednesday."
            ],
            "recommendedExerciseModalities": ["audio_grid_completion", "true_false", "speaker_matching"]
        },
        {
            "lessonId": "les_a1_35_05_weekly_planner_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Harmonizing Weekly Study and Leisure Plans",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a collaborative planning session between two friends arranging a weekly routine of gym, study, and social outings.",
            "communicativeOutcome": "Negotiate and finalize a mutually agreeable weekly routine accommodating both partners' fixed commitments.",
            "objectivesIntroduced": ["obj_a1_35_05_negotiate_weekly_routine"],
            "objectivesPracticed": [
                "obj_a1_35_01_identify_weekdays",
                "obj_a1_35_02_use_relative_day_anchors"
            ],
            "objectivesReviewed": ["obj_a1_34_03_negotiate_meeting_times"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["даваа", "баасан", "бямба", "уулзах", "явах", "завтай"],
            "readingObjective": "Read personal weekly commitment agenda cards.",
            "listeningObjective": "Comprehend partner's stated availability and conflicting obligations across the 7 days.",
            "writingObjective": "Draft a finalized joint 7-day master calendar detailing shared activity days and times.",
            "spokenProductionObjective": "Execute an 8-turn scheduling conversation proposing, adjusting, and confirming activity days.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Gracious accommodation of partner's schedule limitations.",
            "prerequisiteLessonIds": [
                "les_a1_35_03_weekly_schedule_reading",
                "les_a1_35_04_weekly_routine_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_35_01_weekdays_tibetan_and_numerical"],
            "reviewsUnitIds": ["unit_a1_35_days_of_the_week_weekly_calendars"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 35 weekday skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating natural weekly coordination.",
            "successCriteria": [
                "Propose activities using dative-locative day markings ('Баасан гаригт уулзъя').",
                "Successfully establish 2 common activity slots during the week."
            ],
            "masteryEvidence": [
                "Completes roleplay without using English weekday names.",
                "Both participants produce matching weekly calendars from their discussion."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "calendar_harmonization"]
        }
    ])

    
    # =========================================================================
    # UNIT 36: Calendar Dates, Months & Seasons (pos 36)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[36]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_36_01_twelve_months_and_seasons",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Yearly Cycles: The Twelve Months and Four Seasons",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce the numerical month system (нэгдүгээр сар ... арван хоёрдугаар сар) and the four climatic seasons (хавар, зун, намар, өвөл).",
            "communicativeOutcome": "State the current month, current season, and relate months to seasonal characteristics.",
            "objectivesIntroduced": ["obj_a1_36_01_name_months_and_seasons"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_weather_nature"],
            "previousVocabularyReused": ["сар", "жил", "цаг", "нэг", "хоёр"],
            "readingObjective": "Read annual wall calendar headers showing month names and seasonal divisions.",
            "listeningObjective": "Hear spoken mentions of birth months and seasonal transitions in conversational speech.",
            "writingObjective": "Write the 12 months in numerical sequence and group them under the 4 seasons.",
            "spokenProductionObjective": "State which season and month one likes most and why in simple phrases.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear annual chronological orientation in civic and personal communication.",
            "prerequisiteLessonIds": ["les_a1_35_05_weekly_planner_synthesis"],
            "reviewsLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Attach ordinal suffixes (-дүгээр/-дугаар) to numbers 1-12 to form month names.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear vowel quality in season names (хавар, намар, өвөл).",
            "successCriteria": [
                "Map ordinal numbers 1-12 to calendar months (e.g. тавдугаар сар = May).",
                "Assign each of the 12 months to its correct climatic season."
            ],
            "masteryEvidence": [
                "Produces 'Нэгдүгээр сар бол өвлийн сар' accurately.",
                "Recites the four seasons in chronological order starting from spring."
            ],
            "recommendedExerciseModalities": ["calendar_mapping", "season_sorting", "cued_production"]
        },
        {
            "lessonId": "les_a1_36_02_calendar_dates_and_birthdays",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Exact Dates: Stating Birthdays and Historic Anniversaries",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce syntax for calendar dates: [Year] он + [Month] сар + [Day] өдөр, and asking/telling birth dates.",
            "communicativeOutcome": "State one's complete birth date and read historical and civic anniversary dates.",
            "objectivesIntroduced": ["obj_a1_36_02_state_calendar_dates_birthdays"],
            "objectivesPracticed": ["obj_a1_36_01_name_months_and_seasons"],
            "objectivesReviewed": ["obj_a1_27_02_count_decades_up_to_100"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["он", "сар", "өдөр", "төрсөн өдөр"],
            "readingObjective": "Read identity cards, passports, and official forms displaying date-of-birth fields.",
            "listeningObjective": "Comprehend administrative clerks verifying birth dates at service counters.",
            "writingObjective": "Write out 3 full calendar dates in formal Mongolian written format (Year-Month-Day).",
            "spokenProductionObjective": "State one's full birthday aloud upon official inquiry.",
            "registerTarget": "Everyday standard neutral and administrative",
            "pragmaticTarget": "Formal accuracy when stating personal identity dates on official occasions.",
            "prerequisiteLessonIds": ["les_a1_36_01_twelve_months_and_seasons"],
            "reviewsLessonIds": ["les_a1_27_02_tens_and_counting_to_100"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Combine multi-digit calendar numbers (1-31) with month and year nouns.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Descending hierarchical intonation in standard date reading (Year -> Month -> Day).",
            "successCriteria": [
                "Follow hierarchical descending date order (он -> сар -> өдөр).",
                "Answer 'Таны төрсөн өдөр хэзээ вэ?' accurately."
            ],
            "masteryEvidence": [
                "Produces 'Би 1998 оны 6 дугаар сарын 15-нд төрсөн' fluently.",
                "Extracts birth dates from simulated identity documents with 100% accuracy."
            ],
            "recommendedExerciseModalities": ["date_dictation", "form_filling", "matching"]
        },
        {
            "lessonId": "les_a1_36_03_national_holidays_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Mongolian National Holidays and Festivities",
            "lessonType": "reading_development",
            "primaryPurpose": "Read informative cultural texts describing major national holidays (Цагаан сар, Наадам, Шинэ жил, Эх үрсийн баяр).",
            "communicativeOutcome": "Identify key national holidays, their calendar dates, and corresponding cultural customs.",
            "objectivesIntroduced": ["obj_a1_36_03_read_holiday_descriptions"],
            "objectivesPracticed": [
                "obj_a1_36_01_name_months_and_seasons",
                "obj_a1_36_02_state_calendar_dates_birthdays"
            ],
            "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["баяр", "наадам", "амралт", "өдөр", "хүмүүс"],
            "readingObjective": "Read a 60-word cultural calendar text detailing the dates and significance of Naadam and Tsagaan Sar.",
            "listeningObjective": None,
            "writingObjective": "Draft a short 4-line holiday greeting card wishing happy national festivities.",
            "spokenProductionObjective": None,
            "registerTarget": "Courteous standard cultural",
            "pragmaticTarget": "Understanding public holiday scheduling and festive greetings.",
            "prerequisiteLessonIds": ["les_a1_36_02_calendar_dates_and_birthdays"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine existential assertion with annual festive events (Долоодугаар сард Наадам байна).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm festive narration reading cultural holiday descriptions.",
            "successCriteria": [
                "Match 4 major national holidays with their official calendar dates.",
                "Extract holiday closure notices from civic announcements."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions on Mongolian holidays accurately.",
                "Identifies that July 11-15 marks the National Naadam Festival."
            ],
            "recommendedExerciseModalities": ["document_scanning", "holiday_matching", "short_answer"]
        },
        {
            "lessonId": "les_a1_36_04_calendar_date_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Transcribing Spoken Dates and Event Deadlines",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse spoken administrative deadline announcements, conference dates, and birth records.",
            "communicativeOutcome": "Accurately record multi-part calendar dates from spoken speech without digit or month errors.",
            "objectivesIntroduced": ["obj_a1_36_04_parse_spoken_calendar_dates"],
            "objectivesPracticed": ["obj_a1_36_02_state_calendar_dates_birthdays"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["он", "сар", "өдөр", "хугацаа", "дуусах"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 administrative audio clips and transcribe the exact year, month, and day mentioned.",
            "writingObjective": "Transcribe 5 deadline dates into an administrative compliance tracker.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard administrative",
            "pragmaticTarget": "Auditory precision when recording contractual and institutional dates.",
            "prerequisiteLessonIds": ["les_a1_36_02_calendar_dates_and_birthdays"],
            "reviewsLessonIds": ["les_a1_36_01_twelve_months_and_seasons"],
            "reviewsUnitIds": ["unit_a1_36_calendar_dates_months_seasons"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying calendar date transcription.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic administrative broadcast audio with natural rapid date phrasing.",
            "successCriteria": [
                "Transcribe all 5 spoken dates accurately matching numerical and month forms without error.",
                "Differentiate between ordinal and cardinal numerals in date contexts."
            ],
            "masteryEvidence": [
                "Scores 100% on the spoken date transcription assessment.",
                "Catches spoken year digits (e.g. хоёр мянга хорин дөрөв)."
            ],
            "recommendedExerciseModalities": ["audio_transcription", "error_detection", "date_logging"]
        },
        {
            "lessonId": "les_a1_36_05_annual_event_planning_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Planning an Annual Academic Calendar",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate an academic committee meeting scheduling semester start dates, exam weeks, and holidays.",
            "communicativeOutcome": "Negotiate, propose, and finalize annual academic and holiday dates collaboratively.",
            "objectivesIntroduced": ["obj_a1_36_05_negotiate_annual_dates"],
            "objectivesPracticed": [
                "obj_a1_36_01_name_months_and_seasons",
                "obj_a1_36_02_state_calendar_dates_birthdays"
            ],
            "objectivesReviewed": ["obj_a1_35_05_negotiate_weekly_routine"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["сар", "өдөр", "эхлэх", "дуусах", "шалгалт", "амралт"],
            "readingObjective": "Read university administrative scheduling briefs with proposed date ranges.",
            "listeningObjective": "Comprehend partner proposals regarding exam and break scheduling.",
            "writingObjective": "Draft a finalized 4-item annual calendar summary detailing key term dates.",
            "spokenProductionObjective": "Execute an 8-turn scheduling conversation negotiating term milestone dates.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Collaborative professional calendar coordination.",
            "prerequisiteLessonIds": [
                "les_a1_36_03_national_holidays_reading",
                "les_a1_36_04_calendar_date_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_36_01_twelve_months_and_seasons"],
            "reviewsUnitIds": ["unit_a1_36_calendar_dates_months_seasons"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 36 calendar skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary professional committee dialogue negotiating annual event dates.",
            "successCriteria": [
                "State dates fluently using complete hierarchical format.",
                "Agree upon 4 academic milestones without scheduling overlaps."
            ],
            "masteryEvidence": [
                "Completes interactive roleplay maintaining professional administrative register.",
                "Both partners record identical dates on their planning dossiers."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "annual_calendar_planning"]
        }
    ])

    # =========================================================================
    # UNIT 37: Verbal Dictionary Infinitive: Suffix -х (pos 37)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[37]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_37_01_infinitive_suffix_morphology",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Verb Citation: The -х Infinitive and Dictionary Lookup",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the verbal dictionary citation form / future participle suffix -х, vowel harmony rules, and finding verbs in dictionaries.",
            "communicativeOutcome": "Identify verb roots, attach the -х suffix adhering to vowel harmony, and recognize citation forms in dictionaries.",
            "objectivesIntroduced": ["obj_a1_37_01_form_infinitive_kh"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_30_01_mark_accusative_definite_objects"],
            "grammarIntroduced": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_sov_word_order"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["унших", "бичих", "явах", "ирэх", "сурах"],
            "readingObjective": "Read printed dictionary headwords displaying verbs in their canonical -х citation forms.",
            "listeningObjective": "Hear the acoustic presence of the final unreleased /x/ in verb citation forms.",
            "writingObjective": "Attach the -х suffix to 6 verb stems following vowel harmony and vowel insertion rules.",
            "spokenProductionObjective": "Cite aloud the infinitive forms of 5 everyday actions.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear citation of action verbs during vocabulary acquisition.",
            "prerequisiteLessonIds": ["les_a1_36_05_annual_event_planning_synthesis"],
            "reviewsLessonIds": ["les_a1_30_01_accusative_definite_marking"],
            "reviewsUnitIds": ["unit_a1_30_definite_direct_objects_the_accusat"],
            "reviewReason": "Prepare verb stems to take nominal case endings and modal complements.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear phonological articulation of stem vowels preceding final -х.",
            "successCriteria": [
                "Insert connecting vowel before -х for consonant stems (яв- -> явах, сур- -> сурах).",
                "Recognize that -х is the standard dictionary entry form for all Mongolian verbs."
            ],
            "masteryEvidence": [
                "Correctly cites 6 verbs in -х form with accurate vowel harmony.",
                "Explains that 'унш' is an imperative stem while 'унших' is the citation infinitive."
            ],
            "recommendedExerciseModalities": ["infinitive_formation", "dictionary_lookup", "matching"]
        },
        {
            "lessonId": "les_a1_37_02_infinitive_complementation_duriatai",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Likes and Dislikes: Using -х дуртай and -х дургүй",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce modal adjectives 'дуртай' (likes/fond of) and 'дургүй' (dislikes) taking verbal infinitive complements (-х дуртай).",
            "communicativeOutcome": "Express personal preferences, hobbies, and disinclinations regarding everyday activities.",
            "objectivesIntroduced": ["obj_a1_37_02_express_likes_dislikes_with_infinitive"],
            "objectivesPracticed": ["obj_a1_37_01_form_infinitive_kh"],
            "objectivesReviewed": ["obj_a1_24_02_negate_existence_baihgui"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["унших", "хоол", "цай", "кино", "үзэх"],
            "readingObjective": "Read social media bios describing hobbies, favorite sports, and leisure preferences.",
            "listeningObjective": "Comprehend friends discussing what they like and dislike doing on weekends.",
            "writingObjective": "Write 4 sentences contrasting things one likes doing with things one dislikes doing.",
            "spokenProductionObjective": "State aloud 3 hobbies one enjoys and 1 activity one dislikes.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Authentic personal self-expression in social introductions.",
            "prerequisiteLessonIds": ["les_a1_37_01_infinitive_suffix_morphology"],
            "reviewsLessonIds": ["les_a1_24_02_existential_negation_baihgui"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Contrast affirmative preference (дуртай) with negative preference (дургүй).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational prosody expressing enthusiasm vs disinclination.",
            "successCriteria": [
                "Place the infinitive verb directly before 'дуртай' or 'дургүй'.",
                "Formulate questions using 'дуртай юу?' accurately."
            ],
            "masteryEvidence": [
                "Produces 'Би ном унших дуртай' smoothly upon prompt.",
                "Produces 'Би өглөө эрт босох дургүй' without grammatical hesitation."
            ],
            "recommendedExerciseModalities": ["preference_drills", "cued_production", "sentence_construction"]
        },
        {
            "lessonId": "les_a1_37_03_hobby_infinitive_practice",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Interviewing Peers About Leisure Passions",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate question and answer exchanges about hobbies, musical tastes, and recreational sports using -х complements.",
            "communicativeOutcome": "Conduct an interactive peer interview finding common recreational interests and shared hobbies.",
            "objectivesIntroduced": ["obj_a1_37_03_interview_peer_preferences"],
            "objectivesPracticed": [
                "obj_a1_37_01_form_infinitive_kh",
                "obj_a1_37_02_express_likes_dislikes_with_infinitive"
            ],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["спорт", "хөгжим", "дуулах", "бүжиглэх", "зураг"],
            "readingObjective": "Read survey cards detailing diverse student hobby clubs and recreational circles.",
            "listeningObjective": "Comprehend interview responses regarding frequency and enjoyment of activities.",
            "writingObjective": "Draft a 4-line summary of a classmate's leisure preferences from interview notes.",
            "spokenProductionObjective": "Ask a peer 4 questions exploring their leisure preferences using '... дуртай юу?'.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Supportive curiosity and finding common ground during peer networking.",
            "prerequisiteLessonIds": ["les_a1_37_02_infinitive_complementation_duriatai"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine wh-questions with infinitive preferences (Та юу хийх дуртай вэ?).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational rhythm in peer hobby interviews.",
            "successCriteria": [
                "Formulate 'Та юу хийх дуртай вэ?' fluently.",
                "Respond accurately to polar questions ('Та цанаар гулгах дуртай юу?')."
            ],
            "masteryEvidence": [
                "Completes a 6-turn peer hobby interview smoothly.",
                "Accurately transcribes partner's stated preferences into written notes."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "peer_survey"]
        },
        {
            "lessonId": "les_a1_37_04_hobby_club_posters_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: University Hobby Club Posters and Announcements",
            "lessonType": "reading_development",
            "primaryPurpose": "Read university extracurricular club posters (hiking, chess, drama, traditional music) listing activities and meeting times.",
            "communicativeOutcome": "Identify club mission statements, activities offered, membership criteria, and meeting venues from promotional posters.",
            "objectivesIntroduced": ["obj_a1_37_04_read_club_posters"],
            "objectivesPracticed": [
                "obj_a1_37_01_form_infinitive_kh",
                "obj_a1_37_02_express_likes_dislikes_with_infinitive"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["клуб", "дугуйлан", "гишүүн", "уулзалт", "цаг"],
            "readingObjective": "Read a 55-word multi-club extracurricular recruitment poster.",
            "listeningObjective": None,
            "writingObjective": "Complete a 3-field club registration slip indicating chosen activities.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Evaluating leisure options and selecting relevant campus activities.",
            "prerequisiteLessonIds": ["les_a1_37_03_hobby_infinitive_practice"],
            "reviewsLessonIds": ["les_a1_37_01_infinitive_suffix_morphology"],
            "reviewsUnitIds": ["unit_a1_37_verbal_dictionary_infinitive_suffix_"],
            "reviewReason": "Consolidate written recognition of verbal infinitives in promotional event texts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading student club mission statements clearly.",
            "successCriteria": [
                "Extract 3 core activities offered by each student club from text.",
                "Identify weekly meeting days and room numbers accurately."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Matches 4 student profiles to their optimal hobby clubs."
            ],
            "recommendedExerciseModalities": ["document_scanning", "club_matching", "form_filling"]
        },
        {
            "lessonId": "les_a1_37_05_leisure_preference_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Detecting Hobby Preferences in Casual Chat",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid colloquial conversations where speakers express strong preferences and disinclinations.",
            "communicativeOutcome": "Accurately classify multiple speakers' hobby preferences and leisure dislikes from natural audio.",
            "objectivesIntroduced": ["obj_a1_37_05_parse_leisure_preferences_auditorily"],
            "objectivesPracticed": ["obj_a1_37_02_express_likes_dislikes_with_infinitive"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["дуртай", "дургүй", "явах", "үзэх", "тоглох"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 friends discussing weekend leisure options and mark each person's likes/dislikes on a matrix.",
            "writingObjective": "Transcribe the infinitive verb phrases heard in each speaker's statement.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory detection of emotional nuance and preference markers.",
            "prerequisiteLessonIds": ["les_a1_37_03_hobby_infinitive_practice"],
            "reviewsLessonIds": ["les_a1_37_02_infinitive_complementation_duriatai"],
            "reviewsUnitIds": ["unit_a1_37_verbal_dictionary_infinitive_suffix_"],
            "reviewReason": "Zero-vocabulary listening lab training preference detection in speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational audio featuring varied emotional intonations.",
            "successCriteria": [
                "Distinguish 'дуртай' from 'дургүй' reliably in rapid discourse.",
                "Map 4 speakers to their favored hobbies on a classification grid."
            ],
            "masteryEvidence": [
                "Scores 100% on the multi-speaker preference classification test.",
                "Transcribes target infinitive verbs without orthographic errors."
            ],
            "recommendedExerciseModalities": ["audio_grid_completion", "binary_choice", "matching"]
        },
        {
            "lessonId": "les_a1_37_06_weekend_hobby_club_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Establishing a New Campus Club",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Collaborate with peers to establish a new extracurricular club, deciding on activities, meeting days, and club rules.",
            "communicativeOutcome": "Present and negotiate preferred club activities, agreeing on a weekly schedule using infinitive complements.",
            "objectivesIntroduced": ["obj_a1_37_06_collaborate_club_charter"],
            "objectivesPracticed": [
                "obj_a1_37_01_form_infinitive_kh",
                "obj_a1_37_02_express_likes_dislikes_with_infinitive",
                "obj_a1_37_03_interview_peer_preferences"
            ],
            "objectivesReviewed": ["obj_a1_35_05_negotiate_weekly_routine"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["клуб", "дуртай", "хийх", "уулзах", "өдөр", "цаг"],
            "readingObjective": "Read club charter guideline prompts.",
            "listeningObjective": "Comprehend partner proposals regarding club activities and meeting frequency.",
            "writingObjective": "Draft a finalized 5-point club charter listing activities, regular meeting day, and goals.",
            "spokenProductionObjective": "Execute an 8-turn negotiation planning a new club's seasonal program.",
            "registerTarget": "Courteous standard peer educational",
            "pragmaticTarget": "Democratic decision-making and enthusiastic shared planning.",
            "prerequisiteLessonIds": [
                "les_a1_37_04_hobby_club_posters_reading",
                "les_a1_37_05_leisure_preference_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_37_03_hobby_infinitive_practice"],
            "reviewsUnitIds": ["unit_a1_37_verbal_dictionary_infinitive_suffix_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 37 infinitive skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary student collaboration dialogue planning a shared hobby activity.",
            "successCriteria": [
                "Formulate proposals using infinitive verbs with 'дуртай' and future prospective frames.",
                "Reach complete consensus on club schedule and activities within the roleplay."
            ],
            "masteryEvidence": [
                "Completes interactive roleplay without reverts to English.",
                "Produces a finalized club charter document reflecting both partners' inputs."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "collaborative_design", "charter_drafting"]
        }
    ])

    
    # =========================================================================
    # UNIT 38: Habitual Present Participle: Aspect Suffix -даг (pos 38)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[38]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_38_01_habitual_dag_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Daily Regularity: The Habitual Aspect Suffix -даг/-дэг/-дог/-дөг",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the habitual present participle suffix -даг/-дэг/-дог/-дөг expressing recurrent, customary daily routines.",
            "communicativeOutcome": "Formulate habitual actions describing what one usually does everyday (e.g. 'Би өглөө 7 цагт босдог').",
            "objectivesIntroduced": ["obj_a1_38_01_form_habitual_dag"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_37_01_form_infinitive_kh"],
            "grammarIntroduced": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReinforced": ["gram_a1_verb_dictionary_infinitive_kh"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["босох", "цай", "уух", "явах", "хичээл"],
            "readingObjective": "Read simple daily routine descriptions written in the habitual aspect.",
            "listeningObjective": "Hear the fourfold vowel harmonic allomorphs (-даг/-дэг/-дог/-дөг) in spoken routine sentences.",
            "writingObjective": "Attach the appropriate habitual allomorph to 6 verb stems based on vowel harmony.",
            "spokenProductionObjective": "State aloud 3 habitual actions one performs every morning.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear habitual reporting of daily cycles without confusing with ongoing progressive actions.",
            "prerequisiteLessonIds": ["les_a1_37_06_weekend_hobby_club_synthesis"],
            "reviewsLessonIds": ["les_a1_37_01_infinitive_suffix_morphology"],
            "reviewsUnitIds": ["unit_a1_37_verbal_dictionary_infinitive_suffix_"],
            "reviewReason": "Derive habitual verb forms from base verb stems.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear fourfold vowel harmony modeling across all four allomorphs.",
            "successCriteria": [
                "Select -даг for back unrounded, -дэг for front unrounded, -дог for back rounded, -дөг for front rounded stems.",
                "Ensure proper vowel syncope when suffixing vowel-initial or consonant-cluster stems."
            ],
            "masteryEvidence": [
                "Conjugates босох -> босдог, ирэх -> ирдэг, унших -> уншдаг, үзэх -> үздэг with 100% accuracy.",
                "Distinguishes habitual statements from one-off imperative directives."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "vowel_harmony_sorting", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_38_02_habitual_frequency_adverbs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Frequency Markers: Үргэлж, Ихэвчлэн, and Хааяа",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce frequency adverbs (үргэлж 'always', ихэвчлэн 'usually', хааяа 'sometimes', хэзээ ч 'never') modifying habitual verbs.",
            "communicativeOutcome": "Qualify how frequently one performs specific activities in daily life.",
            "objectivesIntroduced": ["obj_a1_38_02_use_frequency_adverbs"],
            "objectivesPracticed": ["obj_a1_38_01_form_habitual_dag"],
            "objectivesReviewed": ["obj_a1_34_01_tell_hours_and_half_hours"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["өглөө", "орой", "ном", "унших", "босох"],
            "readingObjective": "Read personal health and fitness questionnaire entries detailing lifestyle habits.",
            "listeningObjective": "Comprehend speakers quantifying the frequency of their daily workouts and meals.",
            "writingObjective": "Write 4 sentences describing daily habits using diverse frequency adverbs.",
            "spokenProductionObjective": "State aloud how often one drinks coffee, exercises, or reads.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Accurate self-description in health, study, and social surveys.",
            "prerequisiteLessonIds": ["les_a1_38_01_habitual_dag_allomorphs"],
            "reviewsLessonIds": ["les_a1_34_01_exact_hours_and_half_hours"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Combine frequency adverbs with exact clock times (Би ихэвчлэн 8 цагт цайгаа уудаг).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational cadence positioning adverbs before verb phrases.",
            "successCriteria": [
                "Place frequency adverbs before the direct object or verb.",
                "Combine 'хэзээ ч' with negative predicate '... -даггүй'."
            ],
            "masteryEvidence": [
                "Produces 'Би хааяа орой гүйдэг' accurately.",
                "Produces 'Би хэзээ ч тамхи татдаггүй' with correct negative habitual agreement."
            ],
            "recommendedExerciseModalities": ["adverb_placement", "sentence_construction", "cued_production"]
        },
        {
            "lessonId": "les_a1_38_03_habitual_routine_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Contrasting My Routine with Roommates",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate third-person habitual descriptions, contrasting one's own routine with a roommate's or family member's habits.",
            "communicativeOutcome": "Describe and compare morning and evening habits of multiple people using third-person subjects and -даг.",
            "objectivesIntroduced": ["obj_a1_38_03_contrast_multiple_routines"],
            "objectivesPracticed": [
                "obj_a1_38_01_form_habitual_dag",
                "obj_a1_38_02_use_frequency_adverbs"
            ],
            "objectivesReviewed": ["obj_a1_17_01_personal_pronouns"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": ["gram_a1_pronouns_personal_direct_address"],
            "grammarReinforced": ["gram_a1_pronouns_personal_direct_address"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["тэр", "манай", "найз", "босох", "явах", "ирэх"],
            "readingObjective": "Read comparative blog entries contrasting early risers ('болжмор') with night owls ('шар шувуу').",
            "listeningObjective": "Comprehend dialogue where two roommates negotiate morning bathroom and kitchen schedules.",
            "writingObjective": "Draft a 4-sentence comparative paragraph contrasting two people's waking and eating habits.",
            "spokenProductionObjective": "Describe a family member's typical workday routine aloud in 3 sentences.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Respectful and objective description of others' personal routines.",
            "prerequisiteLessonIds": ["les_a1_38_02_habitual_frequency_adverbs"],
            "reviewsLessonIds": ["les_a1_17_01_singular_pronouns_subject_slots"],
            "reviewsUnitIds": ["unit_a1_17_personal_pronouns_direct_address_pr"],
            "reviewReason": "Ensure subject-verb semantic agreement across first, second, and third person habitual clauses.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural dialogue rhythm contrasting personal schedules.",
            "successCriteria": [
                "Maintain habitual -даг marking regardless of grammatical person (no person endings on -даг in neutral standard A1).",
                "Use contrasting conjunction 'харин' (while / but) correctly."
            ],
            "masteryEvidence": [
                "Produces 'Би 7 цагт босдог, харин манай найз 8 цагт босдог' without error.",
                "Corrects sentences where non-habitual verb endings were mistakenly applied."
            ],
            "recommendedExerciseModalities": ["comparative_writing", "cloze_selection", "audio_response_matching"]
        },
        {
            "lessonId": "les_a1_38_04_lifestyle_profile_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Daily Life of a Herder vs City Resident",
            "lessonType": "reading_development",
            "primaryPurpose": "Read comparative cultural texts illustrating the diurnal routine of a rural nomadic herder vs an urban professional in Ulaanbaatar.",
            "communicativeOutcome": "Understand and extract daily pastoral and urban routines from authentic descriptive profiles.",
            "objectivesIntroduced": ["obj_a1_38_04_read_lifestyle_profiles"],
            "objectivesPracticed": ["obj_a1_38_01_form_habitual_dag"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["хөдөө", "хот", "маргааш", "өглөө", "ажил", "мал"],
            "readingObjective": "Read a 65-word text contrasting the daily cycle of herding livestock with office commuting.",
            "listeningObjective": None,
            "writingObjective": "List 3 daily tasks unique to the herder and 3 unique to the city resident based on text.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard cultural",
            "pragmaticTarget": "Appreciating traditional nomadic cycles alongside contemporary urban living.",
            "prerequisiteLessonIds": ["les_a1_38_03_habitual_routine_guided_drills"],
            "reviewsLessonIds": ["les_a1_38_01_habitual_dag_allomorphs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Consolidate written recognition of habitual verbs across rich cultural texts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm cultural narrative tone reading lifestyle passages.",
            "successCriteria": [
                "Extract chronological milestones for both herder and city resident from text.",
                "Answer 4 factual reading comprehension questions accurately."
            ],
            "masteryEvidence": [
                "Accurately maps daily activities to morning, noon, and evening on a comparative chart.",
                "Translates 3 cultural routine sentences into English without loss of aspectual nuance."
            ],
            "recommendedExerciseModalities": ["document_scanning", "chronological_mapping", "short_answer"]
        },
        {
            "lessonId": "les_a1_38_05_routine_interviews_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Daily Routines in Fast Conversational Speech",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal descriptions of busy university students and working parents reciting their daily timetables.",
            "communicativeOutcome": "Accurately record waking times, commute methods, meal hours, and study routines from rapid audio.",
            "objectivesIntroduced": ["obj_a1_38_05_parse_spoken_routines"],
            "objectivesPracticed": ["obj_a1_38_01_form_habitual_dag"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["босох", "идэх", "уух", "явах", "хичээл"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 speakers describing their workday routines and record the times of 4 primary daily events.",
            "writingObjective": "Transcribe the habitual verbs and associated clock times heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory tracking of temporal sequences without visual aids.",
            "prerequisiteLessonIds": ["les_a1_38_03_habitual_routine_guided_drills"],
            "reviewsLessonIds": ["les_a1_38_02_habitual_frequency_adverbs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying habitual aspect perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic multi-speaker audio with varied pacing and background cafe sounds.",
            "successCriteria": [
                "Map 4 speakers' waking and sleeping hours accurately.",
                "Detect frequency adverbs (үргэлж, хааяа) from audio stream."
            ],
            "masteryEvidence": [
                "Scores 100% on the routine chronology listening test.",
                "Accurately transcribes all heard -даг/-дэг/-дог/-дөг endings."
            ],
            "recommendedExerciseModalities": ["audio_timeline_completion", "speaker_matching", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_38_06_lifestyle_interview_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Lifestyle and Healthy Habits Exchange",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a wellness consultation or lifestyle survey where partners interview each other on sleep, diet, exercise, and study habits.",
            "communicativeOutcome": "Conduct a comprehensive lifestyle interview asking and answering about daily regularity and personal habits.",
            "objectivesIntroduced": ["obj_a1_38_06_conduct_lifestyle_interview"],
            "objectivesPracticed": [
                "obj_a1_38_01_form_habitual_dag",
                "obj_a1_38_02_use_frequency_adverbs",
                "obj_a1_38_03_contrast_multiple_routines"
            ],
            "objectivesReviewed": ["obj_a1_34_03_negotiate_meeting_times"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["өглөө", "өдөр", "орой", "босох", "унтах", "идэх"],
            "readingObjective": "Read lifestyle survey questionnaire prompt cards.",
            "listeningObjective": "Comprehend partner's detailed descriptions of daily routine patterns.",
            "writingObjective": "Draft a 4-line summary report assessing partner's lifestyle balance and sleep habits.",
            "spokenProductionObjective": "Execute an 8-turn interview exchanging questions on daily routines and personal habits.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Warm, encouraging tone in personal habit discussions.",
            "prerequisiteLessonIds": [
                "les_a1_38_04_lifestyle_profile_reading",
                "les_a1_38_05_routine_interviews_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_38_03_habitual_routine_guided_drills"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 38 habitual skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating natural peer lifestyle interviewing.",
            "successCriteria": [
                "Formulate questions using '... -даг уу?' fluently.",
                "Respond using diverse frequency adverbs and clock times without grammatical errors."
            ],
            "masteryEvidence": [
                "Completes unscripted 8-turn lifestyle interview smoothly.",
                "Produces a grammatically pristine written profile of the partner's daily routine."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "lifestyle_survey", "peer_profiling"]
        }
    ])

    # =========================================================================
    # UNIT 39: Temporal Dative-Locative: Times & Deadlines (pos 39)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # Lesson 6 is Section 3 Mid-Section Checkpoint!
    # =========================================================================
    u = u_map[39]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_39_01_temporal_dative_marking",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Time Anchoring: Suffixes -д/-т on Hours, Days, and Years",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the temporal application of dative-locative case suffixes (-д/-т) to mark time points, deadlines, and temporal coordinates.",
            "communicativeOutcome": "Anchor events to exact hours, days, months, and years using correct dative-locative suffixes (e.g. 'Таван цагт', 'Даваа гаригт').",
            "objectivesIntroduced": ["obj_a1_39_01_apply_temporal_dative"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": ["gram_a1_case_dative_locative_temporal"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "өдөр", "сар", "он", "уулзах"],
            "readingObjective": "Read event posters displaying start times marked with temporal dative endings.",
            "listeningObjective": "Hear the acoustic presence of -д/-т attached to numeral time points in speech.",
            "writingObjective": "Attach -д or -т to 6 time nouns and numbers following consonant assimilation rules.",
            "spokenProductionObjective": "State aloud at what time an event starts using temporal dative marking.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Precise temporal anchoring avoiding ambiguity between duration and point-in-time.",
            "prerequisiteLessonIds": ["les_a1_38_06_lifestyle_interview_synthesis"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Transfer spatial dative-locative morphology to temporal domain.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear phonological distinction between spatial and temporal dative phrases.",
            "successCriteria": [
                "Select -т after voiceless consonant finals (цагт, минутад/минутанд) and -д after vowel/sonorant finals.",
                "Attach temporal dative directly to numbers denoting hours or dates."
            ],
            "masteryEvidence": [
                "Produces 'Би найман цагт ирнэ' with accurate case suffix.",
                "Differentiates 'хоёр цаг' (two hours duration) from 'хоёр цагт' (at two o'clock)."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_39_02_deadline_postpositions_hurtel",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Deadlines and Bounds: Хүртэл and Болтол Particles",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce temporal terminating postpositions and particles (хүртэл 'until/up to', дотор 'within', өмнө 'before') with time nouns.",
            "communicativeOutcome": "Specify submission deadlines, opening intervals, and completion targets accurately.",
            "objectivesIntroduced": ["obj_a1_39_02_use_temporal_postpositions"],
            "objectivesPracticed": ["obj_a1_39_01_apply_temporal_dative"],
            "objectivesReviewed": ["obj_a1_34_02_tell_precise_minutes_past_and_to"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "өдөр", "дуусах", "өгөх", "хүлээх"],
            "readingObjective": "Read assignment submission guidelines detailing strict deadline hours and dates.",
            "listeningObjective": "Comprehend course instructors announcing deadline cutoffs in lecture hall speech.",
            "writingObjective": "Write 4 sentences specifying assignment deadlines using 'хүртэл' and 'өмнө'.",
            "spokenProductionObjective": "State aloud when a project must be submitted.",
            "registerTarget": "Everyday standard academic and professional",
            "pragmaticTarget": "Rigorous communication of deadlines preventing late submissions.",
            "prerequisiteLessonIds": ["les_a1_39_01_temporal_dative_marking"],
            "reviewsLessonIds": ["les_a1_34_02_minutes_past_and_to_the_hour"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Combine minute precision with terminating postposition 'хүртэл'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Firm authoritative instructional intonation on deadline announcements.",
            "successCriteria": [
                "Place 'хүртэл' after the temporal noun phrase without intervening suffixes.",
                "Use 'өмнө' with ablative or dative depending on syntactic frame."
            ],
            "masteryEvidence": [
                "Produces 'Маргааш 5 цаг хүртэл өгөөрэй' fluently.",
                "Identifies whether a deadline is flexible or strict from phrasing."
            ],
            "recommendedExerciseModalities": ["deadline_matching", "cloze_selection", "cued_production"]
        },
        {
            "lessonId": "les_a1_39_03_temporal_scheduling_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Negotiating Project Timelines and Delivery Dates",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining temporal datives, duration intervals, and deadline markers in workplace task allocation.",
            "communicativeOutcome": "Negotiate task completion deadlines and milestone check-ins with team members.",
            "objectivesIntroduced": ["obj_a1_39_03_negotiate_task_deadlines"],
            "objectivesPracticed": [
                "obj_a1_39_01_apply_temporal_dative",
                "obj_a1_39_02_use_temporal_postpositions"
            ],
            "objectivesReviewed": ["obj_a1_35_01_identify_weekdays"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["ажил", "дуусах", "хэзээ", "даваа", "баасан"],
            "readingObjective": "Read workplace project task matrices listing assignees, tasks, and deadlines.",
            "listeningObjective": "Comprehend team lead delegating tasks and assigning milestone completion days.",
            "writingObjective": "Draft a 4-item project schedule detailing tasks and strict deadline days.",
            "spokenProductionObjective": "Negotiate a realistic completion date for a shared group project.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Professional negotiation of achievable timelines.",
            "prerequisiteLessonIds": ["les_a1_39_02_deadline_postpositions_hurtel"],
            "reviewsLessonIds": ["les_a1_35_01_weekdays_tibetan_and_numerical"],
            "reviewsUnitIds": ["unit_a1_35_days_of_the_week_weekly_calendars"],
            "reviewReason": "Attach temporal datives to days of the week (Баасан гаригт дуусгана).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic project meeting audio discussing milestone feasibility.",
            "successCriteria": [
                "Propose completion dates using temporal datives accurately.",
                "Request deadline extensions politely using conditional polite expressions."
            ],
            "masteryEvidence": [
                "Completes a 6-turn project negotiation roleplay smoothly.",
                "Transcribes agreed delivery dates without day or time errors."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "project_scheduling", "information_gap"]
        },
        {
            "lessonId": "les_a1_39_04_academic_calendar_deadlines_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: University Term Deadlines and Exam Notices",
            "lessonType": "reading_development",
            "primaryPurpose": "Read official university registrar notices detailing registration cutoffs, tuition deadlines, and final exam time slots.",
            "communicativeOutcome": "Extract critical academic deadline dates and avoid administrative penalties from printed university notices.",
            "objectivesIntroduced": ["obj_a1_39_04_read_academic_deadlines"],
            "objectivesPracticed": [
                "obj_a1_39_01_apply_temporal_dative",
                "obj_a1_39_02_use_temporal_postpositions"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["бүртгэл", "төлбөр", "хугацаа", "шалгалт", "хоцрох"],
            "readingObjective": "Read a 60-word university registrar notice listing 4 mandatory academic cutoffs.",
            "listeningObjective": None,
            "writingObjective": "Extract 4 deadline dates and corresponding requirements into a student compliance checklist.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard administrative",
            "pragmaticTarget": "Meticulous compliance with institutional regulations and time constraints.",
            "prerequisiteLessonIds": ["les_a1_39_03_temporal_scheduling_drills"],
            "reviewsLessonIds": ["les_a1_39_01_temporal_dative_marking"],
            "reviewsUnitIds": ["unit_a1_39_temporal_dative_locative_times_deadl"],
            "reviewReason": "Consolidate written recognition of temporal datives in official civic circulars.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading administrative university announcements with formal gravitas.",
            "successCriteria": [
                "Locate the final registration date from notice text.",
                "Identify consequences of late submission ('Хугацаа хоцорвол хүчингүй')."
            ],
            "masteryEvidence": [
                "Answers 4 comprehension questions on registrar policies with 100% accuracy.",
                "Compiles a correct chronological student checklist from text."
            ],
            "recommendedExerciseModalities": ["document_scanning", "checklist_creation", "short_answer"]
        },
        {
            "lessonId": "les_a1_39_05_deadline_announcements_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Transcribing Spoken Deadlines and Time Boundaries",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse spoken administrative and broadcast announcements warning of approaching deadlines and service cutoffs.",
            "communicativeOutcome": "Accurately record spoken deadlines and operating time boundaries without misinterpreting hour limits.",
            "objectivesIntroduced": ["obj_a1_39_05_parse_spoken_deadlines"],
            "objectivesPracticed": ["obj_a1_39_01_apply_temporal_dative"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "өдөр", "хүртэл", "дуусах", "яарах"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 radio and campus audio announcements and transcribe the exact cutoff time and date for each.",
            "writingObjective": "Transcribe 5 deadline records into a deadline management spreadsheet.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard broadcast",
            "pragmaticTarget": "Auditory vigilance regarding temporal limits under broadcast noise.",
            "prerequisiteLessonIds": ["les_a1_39_03_temporal_scheduling_drills"],
            "reviewsLessonIds": ["les_a1_39_02_deadline_postpositions_hurtel"],
            "reviewsUnitIds": ["unit_a1_39_temporal_dative_locative_times_deadl"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying temporal postposition perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic public broadcast audio with authentic deadline urgency.",
            "successCriteria": [
                "Transcribe all 5 cutoff times and dates without error.",
                "Differentiate between start times (-д) and end times (хүртэл)."
            ],
            "masteryEvidence": [
                "Scores 100% on the deadline listening comprehension test.",
                "Correctly identifies which service closes at noon vs 5 PM."
            ],
            "recommendedExerciseModalities": ["audio_transcription", "error_detection", "deadline_logging"]
        },
        {
            "lessonId": "les_a1_39_06_mid_section_03_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Milestone Checkpoint: Section 3 Mid-Section Synthesis Audit",
            "lessonType": "checkpoint",
            "primaryPurpose": "Formal formative milestone evaluation assessing cumulative mastery of Units 34-39 (clock time, weekdays, dates/seasons, infinitives, habitual aspect, temporal datives).",
            "communicativeOutcome": "Demonstrate integrated communicative competence in describing schedules, expressing habits, reading dates, and coordinating time-bound plans.",
            "objectivesIntroduced": [],
            "objectivesPracticed": [
                "obj_a1_34_01_tell_hours_and_half_hours",
                "obj_a1_35_01_identify_weekdays",
                "obj_a1_36_01_name_months_and_seasons",
                "obj_a1_37_01_form_infinitive_kh",
                "obj_a1_38_01_form_habitual_dag",
                "obj_a1_39_01_apply_temporal_dative"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_telling_time_clock_calendar",
                "gram_a1_verb_dictionary_infinitive_kh",
                "gram_a1_verb_tense_present_habitual_dag",
                "gram_a1_case_dative_locative_temporal"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [],
            "phonologyPracticed": [
                "phono_vowel_harmony_suffixes",
                "phono_stress_initial_and_full_vowels",
                "phono_non_initial_reduction"
            ],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_10_identifying_objects",
                "comm_a1_11_counting_simple_quantities",
                "comm_a1_05_asking_identity_origin"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["цаг", "өдөр", "сар", "он", "босох", "дуртай", "хүртэл"],
            "readingObjective": "Read a comprehensive multi-schedule student diary synthesizing lecture times, deadlines, and weekend routines.",
            "listeningObjective": "Comprehend a multi-part student council briefing on upcoming semester milestones and deadlines.",
            "writingObjective": "Compose an integrated 6-sentence personal schedule profile covering daily habits, favorite hobbies, and weekly deadlines.",
            "spokenProductionObjective": "Deliver an integrated 60-second oral briefing detailing one's weekly timetable and daily routine.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Holistic communicative autonomy in temporal, diurnal, and habitual discourse.",
            "prerequisiteLessonIds": [
                "les_a1_39_04_academic_calendar_deadlines_reading",
                "les_a1_39_05_deadline_announcements_listening_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_34_06_schedule_synchronization_synthesis",
                "les_a1_35_05_weekly_planner_synthesis",
                "les_a1_36_05_annual_event_planning_synthesis",
                "les_a1_37_06_weekend_hobby_club_synthesis",
                "les_a1_38_06_lifestyle_interview_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_34_telling_clock_time_tsag_minut_hagas",
                "unit_a1_35_days_of_the_week_weekly_calendars",
                "unit_a1_36_calendar_dates_months_seasons",
                "unit_a1_37_verbal_dictionary_infinitive_suffix_",
                "unit_a1_38_habitual_present_participle_aspect_s",
                "unit_a1_39_temporal_dative_locative_times_deadl"
            ],
            "reviewReason": "Formal milestone evaluation auditing all Section 3 grammatical and communicative competencies up to midpoint.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Standardized benchmark listening evaluation recordings with native accent diversity.",
            "successCriteria": [
                "Demonstrate integrated mastery across all 6 tested grammatical and temporal targets.",
                "Exhibit zero confusion between clock time (-д/-т), duration (цаг), and habitual aspect (-даг)."
            ],
            "masteryEvidence": [
                "Successfully completes all 4 performance modalities (reading, listening, writing, oral presentation).",
                "Produces spontaneous, error-free sentences describing personal schedules."
            ],
            "recommendedExerciseModalities": ["comprehensive_assessment", "oral_presentation", "dossier_audit"]
        }
    ])

    
    # =========================================================================
    # UNIT 40: Ablative of Spatial & Temporal Origin: -аас (pos 40)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[40]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_40_01_ablative_spatial_origin",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Starting Points: The Ablative Case -аас/-ээс/-оос/-өөс",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the ablative case suffix -аас/-ээс/-оос/-өөс marking point of origin, departure, and source ('from').",
            "communicativeOutcome": "State spatial origin, city of origin, and departure locations using the ablative case accurately.",
            "objectivesIntroduced": ["obj_a1_40_01_form_ablative_origin"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": ["gram_a1_case_ablative_origin"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["хот", "хөдөө", "гэр", "сургууль", "ирэх"],
            "readingObjective": "Read travel departure boards and train tickets showing origin stations marked with ablative case.",
            "listeningObjective": "Hear the fourfold vowel harmonic allomorphs (-аас/-ээс/-оос/-өөс) in spoken travel responses.",
            "writingObjective": "Attach the ablative case suffix to 6 place nouns adhering to vowel harmony and vowel insertion rules.",
            "spokenProductionObjective": "State where you are coming from aloud upon inquiry ('Би номын сангаас ирж байна').",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear articulation of departure points in travel and social greetings.",
            "prerequisiteLessonIds": ["les_a1_39_06_mid_section_03_checkpoint"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Contrast spatial goal (dative-locative -д) with spatial origin (ablative -аас).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear phonological distinction between long vowel /a:s/ ablative and short vowel dative.",
            "successCriteria": [
                "Select correct ablative allomorph according to fourfold vowel harmony.",
                "Insert epenthetic -н- for stems with hidden 'н' where required."
            ],
            "masteryEvidence": [
                "Produces 'Би Дарханаас ирсэн' and 'Улаанбаатараас явлаа' without suffix error.",
                "Answers 'Та хаанаас ирсэн бэ?' correctly using ablative."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "origin_mapping", "cued_production"]
        },
        {
            "lessonId": "les_a1_40_02_temporal_ablative_ranges",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Time Spans: The [Time]-аас [Time]-хүртэл Construction",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the temporal application of the ablative case paired with хүртэл to express time intervals ('from X until Y').",
            "communicativeOutcome": "State operating hours, working intervals, and class durations using the '...-аас ... хүртэл' frame.",
            "objectivesIntroduced": ["obj_a1_40_02_express_time_intervals"],
            "objectivesPracticed": ["obj_a1_40_01_form_ablative_origin"],
            "objectivesReviewed": ["obj_a1_39_02_use_temporal_postpositions"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "хүртэл", "эхлэх", "дуусах", "ажиллах"],
            "readingObjective": "Read shop front door placards displaying opening and closing hours.",
            "listeningObjective": "Comprehend customer service representatives stating business operating spans.",
            "writingObjective": "Write 4 sentences describing daily work or study intervals using '...-аас ... хүртэл'.",
            "spokenProductionObjective": "State aloud one's working hours from start to finish.",
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Clear definition of availability windows preventing missed appointments.",
            "prerequisiteLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsLessonIds": ["les_a1_39_02_deadline_postpositions_hurtel"],
            "reviewsUnitIds": ["unit_a1_39_temporal_dative_locative_times_deadl"],
            "reviewReason": "Combine ablative origin with terminal boundary marker хүртэл.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural prosodic curve spanning from start point to end boundary.",
            "successCriteria": [
                "Attach ablative to initial time point and place 'хүртэл' after concluding time point.",
                "Formulate questions using 'Хэдэн цагаас хэдэн цаг хүртэл вэ?' correctly."
            ],
            "masteryEvidence": [
                "Produces 'Манай дэлгүүр 9 цагаас 20 цаг хүртэл ажилладаг' fluently.",
                "Translates 'from Monday to Friday' into 'Даваагаас Баасан хүртэл' without error."
            ],
            "recommendedExerciseModalities": ["time_interval_drills", "storefront_reading", "cued_production"]
        },
        {
            "lessonId": "les_a1_40_03_travel_origin_destination_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Journey Itineraries from Origin to Destination",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining ablative origin (-аас) with dative/directive destination (-д / руу) in travel planning.",
            "communicativeOutcome": "Describe complete travel routes specifying departure city, transit stops, and final destination.",
            "objectivesIntroduced": ["obj_a1_40_03_describe_complete_routes"],
            "objectivesPracticed": [
                "obj_a1_40_01_form_ablative_origin",
                "obj_a1_40_02_express_time_intervals"
            ],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["явах", "ирэх", "хот", "галт тэрэг", "онгоц"],
            "readingObjective": "Read flight boarding passes and train tickets showing origin, transit, and destination points.",
            "listeningObjective": "Comprehend station announcements announcing train routes from source to terminus.",
            "writingObjective": "Draft a short 3-sentence travel itinerary specifying departure town, arrival town, and journey duration.",
            "spokenProductionObjective": "Explain a planned domestic journey to a travel agent or friend.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Clear travel communication ensuring correct ticketing and boarding.",
            "prerequisiteLessonIds": ["les_a1_40_02_temporal_ablative_ranges"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Synthesize origin (-аас) and destination (-д / руу) within single composite travel clauses.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic station departure announcement audio with travel cadence.",
            "successCriteria": [
                "Construct '[Origin]-аас [Destination] руу явах' structures without case confusion.",
                "Answer 'Та хаанаас хаашаа явах вэ?' fluently."
            ],
            "masteryEvidence": [
                "Produces 'Би Улаанбаатараас Эрдэнэт рүү явна' upon prompt.",
                "Extracts departure and arrival stations from simulated ticket stubs with 100% accuracy."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "itinerary_mapping", "ticket_transcription"]
        },
        {
            "lessonId": "les_a1_40_04_intercity_transport_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Intercity Bus and Train Schedules",
            "lessonType": "reading_development",
            "primaryPurpose": "Read intercity bus terminal departure timetables (Dragon Terminal / Тэнгэр плаза) and passenger route maps.",
            "communicativeOutcome": "Extract departure times, ticket prices, and destination routes from complex printed transport boards.",
            "objectivesIntroduced": ["obj_a1_40_04_read_intercity_schedules"],
            "objectivesPracticed": [
                "obj_a1_40_01_form_ablative_origin",
                "obj_a1_40_02_express_time_intervals"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["автобус", "буудал", "тасалбар", "үнэ", "хөдлөх"],
            "readingObjective": "Read a 60-word multi-province coach timetable matrix.",
            "listeningObjective": None,
            "writingObjective": "Transcribe departure station, time, and ticket cost for 3 provincial destinations.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Autonomous intercity travel navigation across Mongolia.",
            "prerequisiteLessonIds": ["les_a1_40_03_travel_origin_destination_drills"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Consolidate written recognition of ablative origin markers on route signage.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading terminal departure announcements clearly.",
            "successCriteria": [
                "Identify which bus departs earliest from Dragon Terminal to Darkhan.",
                "Extract journey duration in hours from departure and arrival columns."
            ],
            "masteryEvidence": [
                "Answers 4 timetable factual comprehension questions with zero error.",
                "Locates the correct bus gate number based on ticket details."
            ],
            "recommendedExerciseModalities": ["timetable_scanning", "ticket_matching", "short_answer"]
        },
        {
            "lessonId": "les_a1_40_05_transport_departure_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Departure Calls and Origin Clarifications",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid PA system broadcasts at intercity bus terminals and railway stations announcing boarding calls.",
            "communicativeOutcome": "Identify which vehicle is boarding, its destination, and platform number despite reverberation.",
            "objectivesIntroduced": ["obj_a1_40_05_parse_departure_broadcasts"],
            "objectivesPracticed": ["obj_a1_40_01_form_ablative_origin"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["галт тэрэг", "зам", "хөдлөх", "хоцрох", "суух"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 station boarding announcements and identify the origin, destination, and platform for each.",
            "writingObjective": "Transcribe the 5 platform and train route pairings into a transit departure board.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard broadcast",
            "pragmaticTarget": "Auditory identification of critical travel instructions amid background station bustle.",
            "prerequisiteLessonIds": ["les_a1_40_03_travel_origin_destination_drills"],
            "reviewsLessonIds": ["les_a1_40_02_temporal_ablative_ranges"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Zero-vocabulary listening lab training origin/destination acoustic parsing.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic terminal acoustic atmosphere with natural PA chime sound effects.",
            "successCriteria": [
                "Accurately map all 5 announced trains to their designated departure tracks.",
                "Recognize origin city names marked with ablative case in rapid announcements."
            ],
            "masteryEvidence": [
                "Scores 100% on the station listening comprehension test.",
                "Detects route changes or track alterations from audio stream."
            ],
            "recommendedExerciseModalities": ["audio_transcription", "track_mapping", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_40_06_travel_booking_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Booking an Intercity Coach Ticket",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate purchasing an intercity bus or train ticket at a ticket window, specifying origin, destination, departure time, and seat preference.",
            "communicativeOutcome": "Successfully conduct a transactional ticket counter dialogue purchasing a travel ticket.",
            "objectivesIntroduced": ["obj_a1_40_06_book_travel_ticket"],
            "objectivesPracticed": [
                "obj_a1_40_01_form_ablative_origin",
                "obj_a1_40_02_express_time_intervals",
                "obj_a1_40_03_describe_complete_routes"
            ],
            "objectivesReviewed": ["obj_a1_31_02_use_counting_classifiers"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["тасалбар", "үнэ", "хэзээ", "хэдэн цагт", "өгөх"],
            "readingObjective": "Read simulated passenger request prompt cards.",
            "listeningObjective": "Comprehend ticket clerk's queries regarding destination, date, and seat availability.",
            "writingObjective": "Fill out a travel booking confirmation slip detailing route, departure time, and price.",
            "spokenProductionObjective": "Execute an 8-turn ticket purchase dialogue at a simulated transit window.",
            "registerTarget": "Courteous standard transactional",
            "pragmaticTarget": "Polite, efficient civic counter transaction.",
            "prerequisiteLessonIds": [
                "les_a1_40_04_intercity_transport_reading",
                "les_a1_40_05_transport_departure_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_40_03_travel_origin_destination_drills"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 40 ablative travel skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary ticket booking dialogue between customer and booking clerk.",
            "successCriteria": [
                "Specify route using ablative origin and dative destination fluently.",
                "Inquire about departure time and ticket price using polite question particles."
            ],
            "masteryEvidence": [
                "Completes ticket purchase transaction in under 2 minutes without communication breakdown.",
                "Both clerk and customer produce matching ticket details from dialogue."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "transactional_simulation", "booking_receipt_completion"]
        }
    ])

    # =========================================================================
    # UNIT 41: Witnessed Past Verbal Tense: Suffix -лаа (pos 41)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[41]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_41_01_witnessed_past_laa_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Immediate Past: Suffixes -лаа/-лээ/-лоо/-лөө",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the witnessed / immediate past tense verbal suffix -лаа/-лээ/-лоо/-лөө expressing completed actions directly witnessed or performed recently by the speaker.",
            "communicativeOutcome": "Report recently completed actions and witnessed events (e.g. 'Би ирлээ', 'Цас орлоо').",
            "objectivesIntroduced": ["obj_a1_41_01_form_witnessed_past_laa"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_38_01_form_habitual_dag"],
            "grammarIntroduced": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReinforced": ["gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["ирэх", "явах", "унших", "дуусах", "эхлэх"],
            "readingObjective": "Read brief personal status updates reporting recently completed actions.",
            "listeningObjective": "Hear the fourfold vowel harmonic allomorphs (-лаа/-лээ/-лоо/-лөө) in spoken announcements.",
            "writingObjective": "Attach the appropriate past tense allomorph to 6 verb stems following vowel harmony.",
            "spokenProductionObjective": "Announce one's arrival or completion of a task aloud ('Би ирлээ!', 'Ажил дууслаа').",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Immediate reporting of state transitions upon entering or leaving a space.",
            "prerequisiteLessonIds": ["les_a1_40_06_travel_booking_synthesis"],
            "reviewsLessonIds": ["les_a1_38_01_habitual_dag_allomorphs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Contrast habitual actions (-даг) with witnessed completed past actions (-лаа).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear vowel length articulation in long vowel ending -лаа.",
            "successCriteria": [
                "Select correct allomorph according to fourfold vowel harmony.",
                "Use -лаа for first-person arrival announcement ('Би ирлээ') and immediate events."
            ],
            "masteryEvidence": [
                "Conjugates ирэх -> ирлээ, явах -> явлаа, дуусах -> дууслаа, өгөх -> өглөө accurately.",
                "Explains the difference between 'Би хичээлдээ явдаг' (habitual) and 'Би хичээлдээ явлаа' (immediate past/departure)."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_41_02_recent_past_reporting",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "What Just Happened: Reporting Recent Events with Сая and Түрүүн",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce immediate temporal adverbs (сая 'just now', түрүүн 'a moment ago') paired with -лаа past tense verbs.",
            "communicativeOutcome": "Explain events that just occurred moments ago in conversation or phone updates.",
            "objectivesIntroduced": ["obj_a1_41_02_report_recent_events_with_adverbs"],
            "objectivesPracticed": ["obj_a1_41_01_form_witnessed_past_laa"],
            "objectivesReviewed": ["obj_a1_39_01_apply_temporal_dative"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["сая", "түрүүн", "хүн", "ярих", "өгөх"],
            "readingObjective": "Read instant messaging chats explaining recent actions ('Сая автобус ирлээ').",
            "listeningObjective": "Comprehend phone callers explaining why they were unavailable a moment ago.",
            "writingObjective": "Write 4 sentences explaining recent events that happened moments earlier.",
            "spokenProductionObjective": "Explain to a classmate why you just arrived or what just occurred.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Immediate contextual updates in interpersonal communication.",
            "prerequisiteLessonIds": ["les_a1_41_01_witnessed_past_laa_allomorphs"],
            "reviewsLessonIds": ["les_a1_39_01_temporal_dative_marking"],
            "reviewsUnitIds": ["unit_a1_39_temporal_dative_locative_times_deadl"],
            "reviewReason": "Anchor witnessed past events to recent time points.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational prosody combining 'сая' with past verbs.",
            "successCriteria": [
                "Place 'сая' or 'түрүүн' before the predicate verb phrase.",
                "Use witnessed past tense to describe directly perceived recent happenings."
            ],
            "masteryEvidence": [
                "Produces 'Сая багш орж ирлээ' smoothly upon seeing teacher enter.",
                "Distinguishes 'сая' (seconds/minutes ago) from 'өчигдөр' (yesterday)."
            ],
            "recommendedExerciseModalities": ["event_reporting", "cloze_selection", "cued_production"]
        },
        {
            "lessonId": "les_a1_41_03_past_event_interview_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Inquiring About Completed Actions and Errands",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate question and answer exchanges about whether tasks have been completed ('Та хоолоо идсэн үү? / Идлээ').",
            "communicativeOutcome": "Confirm completion of errands, meals, and study tasks with peers and family members.",
            "objectivesIntroduced": ["obj_a1_41_03_confirm_task_completion"],
            "objectivesPracticed": [
                "obj_a1_41_01_form_witnessed_past_laa",
                "obj_a1_41_02_report_recent_events_with_adverbs"
            ],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["хийх", "дуусах", "үзэх", "унших", "ажил"],
            "readingObjective": "Read task checklist updates shared between team members.",
            "listeningObjective": "Comprehend questions checking whether daily duties were finished.",
            "writingObjective": "Draft a short 3-item status update listing finished tasks.",
            "spokenProductionObjective": "Confirm completion of 3 assigned duties upon partner inquiry.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Clear accountability and status reporting among peers.",
            "prerequisiteLessonIds": ["les_a1_41_02_recent_past_reporting"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine past actions with question particles (Та юу үзлээ?).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural dialogue rhythm confirming task completion.",
            "successCriteria": [
                "Respond to completion inquiries using -лаа affirmatively.",
                "Formulate polite inquiries regarding another's tasks."
            ],
            "masteryEvidence": [
                "Completes a 6-turn task status dialogue smoothly.",
                "Accurately answers 'Ажил дууссан уу?' with 'Дууслаа'."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "checklist_verification", "information_gap"]
        },
        {
            "lessonId": "les_a1_41_04_personal_diary_entries_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Personal Diary Notes and Incident Logs",
            "lessonType": "reading_development",
            "primaryPurpose": "Read handwritten diary notes, field trip logs, and short social journal entries recounting past events.",
            "communicativeOutcome": "Understand chronological event sequences and personal impressions from personal diary texts.",
            "objectivesIntroduced": ["obj_a1_41_04_read_diary_entries"],
            "objectivesPracticed": [
                "obj_a1_41_01_form_witnessed_past_laa",
                "obj_a1_41_02_report_recent_events_with_adverbs"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["өдөр", "уулзах", "явах", "үзэх", "сонирхолтой"],
            "readingObjective": "Read a 60-word personal journal excerpt describing a weekend excursion.",
            "listeningObjective": None,
            "writingObjective": "List 4 events from the diary in correct chronological order.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informal reflective",
            "pragmaticTarget": "Comprehending personal narrative accounts and sequence of occurrences.",
            "prerequisiteLessonIds": ["les_a1_41_03_past_event_interview_drills"],
            "reviewsLessonIds": ["les_a1_41_01_witnessed_past_laa_allomorphs"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Consolidate written recognition of witnessed past tense in narrative writing.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm introspective narration reading diary excerpts.",
            "successCriteria": [
                "Identify which activity took place first, second, and last from text.",
                "Extract emotional impressions ('маш сайхан байлаа')."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Correctly orders 5 scrambled sentences from the diary passage."
            ],
            "recommendedExerciseModalities": ["chronological_sorting", "text_scanning", "short_answer"]
        },
        {
            "lessonId": "les_a1_41_05_incident_reporting_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Eyewitness Accounts and News Flashes",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal accounts of people describing unexpected events, weather changes, or arrivals.",
            "communicativeOutcome": "Accurately record who arrived, what occurred, and when it happened from spoken eyewitness audio.",
            "objectivesIntroduced": ["obj_a1_41_05_parse_eyewitness_accounts"],
            "objectivesPracticed": ["obj_a1_41_01_form_witnessed_past_laa"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["бороо", "орох", "болох", "харагдах", "сая"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 eyewitness audio reports and record the specific event witnessed by each speaker.",
            "writingObjective": "Transcribe the witnessed past verb forms heard in each speaker's account.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory identification of rapid state changes and witnessed events.",
            "prerequisiteLessonIds": ["les_a1_41_03_past_event_interview_drills"],
            "reviewsLessonIds": ["les_a1_41_02_recent_past_reporting"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying past tense perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio featuring spontaneous emotional inflections.",
            "successCriteria": [
                "Map 4 speakers to their described recent events accurately.",
                "Differentiate witnessed past (-лаа) from habitual aspect (-даг) in rapid speech."
            ],
            "masteryEvidence": [
                "Scores 100% on the eyewitness listening assessment.",
                "Transcribes all heard past tense verbs with correct vowel harmony."
            ],
            "recommendedExerciseModalities": ["audio_event_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_41_06_weekend_debrief_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Monday Morning Weekend Debrief",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a friendly Monday morning debrief between coworkers or classmates sharing what they did over the weekend.",
            "communicativeOutcome": "Conduct a fluid conversation recounting personal weekend activities and inquiring about another's past events.",
            "objectivesIntroduced": ["obj_a1_41_06_debrief_past_activities"],
            "objectivesPracticed": [
                "obj_a1_41_01_form_witnessed_past_laa",
                "obj_a1_41_02_report_recent_events_with_adverbs",
                "obj_a1_41_03_confirm_task_completion"
            ],
            "objectivesReviewed": ["obj_a1_35_02_use_relative_day_anchors"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["амралтын өдөр", "хаана", "юу", "хийх", "уулзах"],
            "readingObjective": "Read weekend activity prompt cards.",
            "listeningObjective": "Comprehend partner's spoken narrative describing their weekend outings.",
            "writingObjective": "Draft a 4-line summary note recounting a partner's weekend highlights.",
            "spokenProductionObjective": "Execute an 8-turn conversation exchanging weekend accounts and asking follow-up questions.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Warm, engaging social small talk building rapport with peers.",
            "prerequisiteLessonIds": [
                "les_a1_41_04_personal_diary_entries_reading",
                "les_a1_41_05_incident_reporting_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_41_03_past_event_interview_drills"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 41 past tense skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating Monday morning peer small talk.",
            "successCriteria": [
                "Recount 3 past activities using witnessed past verbs accurately.",
                "Ask at least 2 relevant follow-up questions using past question frames."
            ],
            "masteryEvidence": [
                "Completes unscripted 8-turn conversation fluently.",
                "Produces grammatically accurate written debrief of the partner's weekend."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "peer_debrief", "story_retelling"]
        }
    ])

    # =========================================================================
    # UNIT 42: Coordinating Converb: Clause Linking with -ж/-ч (pos 42)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[42]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_42_01_coordinating_converb_morphology",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Action Sequences: The Coordinating Converb -ж / -ч",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the coordinating converb suffix -ж (after vowels and sonorants) and -ч (after voiceless consonants) linking actions in sequence or coordination.",
            "communicativeOutcome": "Link two or more actions into a single fluid sentence (e.g. 'Би номын санд сууж, ном уншлаа').",
            "objectivesIntroduced": ["obj_a1_42_01_form_coordinating_converb_j_ch"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_41_01_form_witnessed_past_laa"],
            "grammarIntroduced": ["gram_a1_converb_coordinating_j_ch"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReinforced": ["gram_a1_verb_tense_past_witnessed_laa"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_consonant_assimilation"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["суух", "унших", "идэх", "уух", "явах"],
            "readingObjective": "Read sequential narrative sentences containing clauses chained with -ж/-ч.",
            "listeningObjective": "Hear the phonetic alternation between voiced /dʒ/ (-ж) and voiceless /tʃ/ (-ч) in chained verbs.",
            "writingObjective": "Attach -ж or -ч to 6 verb stems following phonological voicing and assimilation rules.",
            "spokenProductionObjective": "Combine two daily actions into one spoken compound sentence.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Fluent syntactic coordination avoiding staccato chopped sentences.",
            "prerequisiteLessonIds": ["les_a1_41_06_weekend_debrief_synthesis"],
            "reviewsLessonIds": ["les_a1_41_01_witnessed_past_laa_allomorphs"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Chain converbial dependent clauses to finite past tense matrix verbs.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear phonological distinction between -ж and -ч across different stem classes.",
            "successCriteria": [
                "Select -ч after stems ending in voiceless consonants (б, в, г, д, ж, з, с, т, ш, ц, ч).",
                "Select -ж after vowels and sonorant consonants (м, н, л, р)."
            ],
            "masteryEvidence": [
                "Correctly forms явж, сурч, уншиж, босч/босож with 100% accuracy.",
                "Explains that converbs lack independent person/tense and inherit from the final finite verb."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_combining", "cued_production"]
        },
        {
            "lessonId": "les_a1_42_02_multiaction_routine_chains",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Chained Sequences: Describing 3-Step Morning Routines",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce multi-clause chaining linking 3 sequential actions in chronological order using -ж/-ч.",
            "communicativeOutcome": "Narrate chronological step-by-step sequences seamlessly (e.g. 'Би өглөө босож, нүүрээ угааж, цайгаа уудаг').",
            "objectivesIntroduced": ["obj_a1_42_02_chain_multiple_actions"],
            "objectivesPracticed": ["obj_a1_42_01_form_coordinating_converb_j_ch"],
            "objectivesReviewed": ["obj_a1_38_01_form_habitual_dag"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReinforced": ["gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["нүүр", "угаах", "хувцас", "өмсөх", "босох"],
            "readingObjective": "Read step-by-step procedural guides and morning routine profiles.",
            "listeningObjective": "Comprehend speakers narrating a chain of 3 activities performed before leaving home.",
            "writingObjective": "Write 3 complex sentences each chaining at least two converbial clauses to a finite verb.",
            "spokenProductionObjective": "Narrate aloud one's 3-step morning sequence in a single breath group.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Cohesive and fluent chronological storytelling.",
            "prerequisiteLessonIds": ["les_a1_42_01_coordinating_converb_morphology"],
            "reviewsLessonIds": ["les_a1_38_01_habitual_dag_allomorphs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Chain converbial verbs into habitual aspect final predicates.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Flowing prosody across clause boundaries without unnatural pauses.",
            "successCriteria": [
                "Maintain chronological sequence across chained converbial clauses.",
                "Ensure matrix predicate takes correct final aspect/tense marker."
            ],
            "masteryEvidence": [
                "Produces a 3-verb chained sentence fluently upon prompt.",
                "Demonstrates mastery of subject constancy across coordinated converbial clauses."
            ],
            "recommendedExerciseModalities": ["sequence_chaining", "sentence_combining", "cued_production"]
        },
        {
            "lessonId": "les_a1_42_03_recipe_and_task_instructions_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Step-by-Step Cooking and Office Instructions",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate chaining actions to give clear procedural instructions for making tea, preparing simple food, or operating office gear.",
            "communicativeOutcome": "Explain a multi-step procedure clearly and sequentially to a colleague or friend.",
            "objectivesIntroduced": ["obj_a1_42_03_explain_procedural_steps"],
            "objectivesPracticed": [
                "obj_a1_42_01_form_coordinating_converb_j_ch",
                "obj_a1_42_02_chain_multiple_actions"
            ],
            "objectivesReviewed": ["obj_a1_30_01_mark_accusative_definite_objects"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_case_accusative_definite_object"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_food_dining"],
            "previousVocabularyReused": ["ус", "буцалгах", "хийх", "хутгах", "аяга"],
            "readingObjective": "Read illustrated recipe instruction cards for traditional milk tea (сүүтэй цай).",
            "listeningObjective": "Comprehend procedural explanations of how to brew tea or make instant noodles.",
            "writingObjective": "Draft a 4-step instruction card explaining how to prepare a simple beverage.",
            "spokenProductionObjective": "Explain to a partner how to make traditional Mongolian tea step-by-step.",
            "registerTarget": "Everyday standard instructional",
            "pragmaticTarget": "Clear and orderly instructional clarity preventing culinary or procedural mistakes.",
            "prerequisiteLessonIds": ["les_a1_42_02_multiaction_routine_chains"],
            "reviewsLessonIds": ["les_a1_30_01_accusative_definite_marking"],
            "reviewsUnitIds": ["unit_a1_30_definite_direct_objects_the_accusat"],
            "reviewReason": "Mark definite direct objects within converbial procedural clauses (Усыг буцалгаж...).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Clear didactic instructional audio explaining recipe steps.",
            "successCriteria": [
                "Chain procedural steps using -ж/-ч with imperative or habitual endings.",
                "Use accurate definite direct objects throughout recipe instructions."
            ],
            "masteryEvidence": [
                "Explains the 4 steps of making milk tea without halting.",
                "Orders scrambled instructional sentences correctly into a coherent recipe."
            ],
            "recommendedExerciseModalities": ["recipe_assembly", "procedural_explanation", "dialogue_roleplay"]
        },
        {
            "lessonId": "les_a1_42_04_biographical_narratives_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Short Biographical Narratives and Life Journeys",
            "lessonType": "reading_development",
            "primaryPurpose": "Read cohesive biographical paragraphs describing someone's education, move to the city, and current occupation.",
            "communicativeOutcome": "Understand biographical milestones and sequential life events linked by converbs in reading texts.",
            "objectivesIntroduced": ["obj_a1_42_04_read_biographical_texts"],
            "objectivesPracticed": [
                "obj_a1_42_01_form_coordinating_converb_j_ch",
                "obj_a1_42_02_chain_multiple_actions"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_case_ablative_origin"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["сургууль", "төгсөх", "хот", "шилжих", "ажиллах"],
            "readingObjective": "Read a 65-word biographical profile describing an individual's migration to Ulaanbaatar and career start.",
            "listeningObjective": None,
            "writingObjective": "Extract 4 biographical milestones and their chronological order from the profile.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard narrative",
            "pragmaticTarget": "Synthesizing individual life events into a coherent narrative timeline.",
            "prerequisiteLessonIds": ["les_a1_42_03_recipe_and_task_instructions_drills"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Combine ablative origin of migration with converbial action chains.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm narrative storytelling reading personal biographies.",
            "successCriteria": [
                "Identify chronological sequence of education, relocation, and employment.",
                "Answer 4 factual reading comprehension questions accurately."
            ],
            "masteryEvidence": [
                "Builds a correct life timeline diagram from reading the text.",
                "Translates 2 converbally chained biographical sentences accurately."
            ],
            "recommendedExerciseModalities": ["timeline_construction", "text_scanning", "short_answer"]
        },
        {
            "lessonId": "les_a1_42_05_chained_instructions_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Chained Multi-Step Instructions in Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal instructions chaining 2 or 3 actions in everyday workplace and domestic requests.",
            "communicativeOutcome": "Accurately record all required steps from spoken chained instructions without omitting intermediate tasks.",
            "objectivesIntroduced": ["obj_a1_42_05_parse_spoken_chained_instructions"],
            "objectivesPracticed": ["obj_a1_42_01_form_coordinating_converb_j_ch"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["явах", "авах", "авчрах", "өгөх", "хүлээх"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 workplace audio requests and transcribe all sequential actions demanded by the speaker.",
            "writingObjective": "Transcribe 4 action chains into an executive errand task list.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory precision retaining complete multi-step task directives.",
            "prerequisiteLessonIds": ["les_a1_42_03_recipe_and_task_instructions_drills"],
            "reviewsLessonIds": ["les_a1_42_02_multiaction_routine_chains"],
            "reviewsUnitIds": ["unit_a1_42_coordinating_converb_clause_linking_"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying perception of converbial chains.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic fast-paced office and domestic instructional audio.",
            "successCriteria": [
                "Identify all 2 or 3 verbs present in each chained sentence.",
                "Distinguish between -ж and -ч in fast speech."
            ],
            "masteryEvidence": [
                "Scores 100% on the multi-step instruction retention test.",
                "Identifies which task must be executed before the second task."
            ],
            "recommendedExerciseModalities": ["audio_task_logging", "sequence_ordering", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_42_06_errand_coordination_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Coordinating Errands and Office Tasks",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a collaborative workday scenario where two colleagues coordinate who will run which errands and how tasks will be sequenced.",
            "communicativeOutcome": "Negotiate, sequence, and distribute errands using fluid coordinating converb chains.",
            "objectivesIntroduced": ["obj_a1_42_06_coordinate_errand_chains"],
            "objectivesPracticed": [
                "obj_a1_42_01_form_coordinating_converb_j_ch",
                "obj_a1_42_02_chain_multiple_actions",
                "obj_a1_42_03_explain_procedural_steps"
            ],
            "objectivesReviewed": ["obj_a1_39_03_negotiate_task_deadlines"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal", "gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["банк", "дэлгүүр", "очих", "авах", "ирж", "уулзах"],
            "readingObjective": "Read errand task cards with conflicting locations and deadlines.",
            "listeningObjective": "Comprehend partner proposals regarding route sequencing and task sharing.",
            "writingObjective": "Draft a finalized joint errand workflow detailing sequential tasks for both people.",
            "spokenProductionObjective": "Execute an 8-turn negotiation planning and sequencing shared workday errands.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Efficient collaborative problem solving and workload sharing.",
            "prerequisiteLessonIds": [
                "les_a1_42_04_biographical_narratives_reading",
                "les_a1_42_05_chained_instructions_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_42_03_recipe_and_task_instructions_drills"],
            "reviewsUnitIds": ["unit_a1_42_coordinating_converb_clause_linking_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 42 converbial skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary professional collaboration dialogue coordinating daily errands.",
            "successCriteria": [
                "Propose errand sequences using converb chains ('Би банкинд очиж мөнгө аваад...').",
                "Distribute all 4 tasks logically minimizing transit time."
            ],
            "masteryEvidence": [
                "Completes negotiation smoothly without syntactic fragmentation.",
                "Both partners produce identical agreed errand plans from the dialogue."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "task_distribution", "workflow_mapping"]
        }
    ])

    # =========================================================================
    # UNIT 43: Public Transit Commuting: Bus Routes & Stops (pos 43)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[43]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_43_01_bus_routes_and_stop_names",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "City Transit: Bus Numbers, Stop Names, and U-Money Cards",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce public bus commuting vocabulary: автобусны буудал (bus stop), чиглэл (route), картын уншигч (card reader), карт цэнэглэх (top-up card), and landmark-based stop names in Ulaanbaatar.",
            "communicativeOutcome": "Ask which bus goes to a specific destination and check bus stop names along Peace Avenue and other main thoroughfares.",
            "objectivesIntroduced": ["obj_a1_43_01_identify_bus_routes_and_stops"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_40_01_form_ablative_origin"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_case_ablative_origin"],
            "grammarReinforced": ["gram_a1_case_ablative_origin"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["автобус", "буудал", "карт", "хэд", "хаана"],
            "readingObjective": "Read electronic bus headsigns and street stop placards displaying route numbers and terminus destinations.",
            "listeningObjective": "Hear automated onboard announcements stating the next bus stop in Ulaanbaatar.",
            "writingObjective": "Write 4 sentences describing one's daily bus route number and boarding/alighting stops.",
            "spokenProductionObjective": "Ask a stranger at a bus stop which bus route goes to Sukhbaatar Square.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear street navigation and inquiries at public transit points.",
            "prerequisiteLessonIds": ["les_a1_42_06_errand_coordination_synthesis"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Combine transit routes with origin and destination case marking.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Realistic automated bus stop announcement voice chime.",
            "successCriteria": [
                "Ask 'Энэ автобус Сүхбаатарын талбай руу явах уу?' accurately.",
                "Recognize major urban bus stops (МУИС, Төв шуудан, Багшийн дээд)."
            ],
            "masteryEvidence": [
                "Identifies the correct bus number for 3 target landmarks.",
                "Inquires about transit card balance politely at a bus kiosk."
            ],
            "recommendedExerciseModalities": ["route_matching", "cued_production", "stop_identification"]
        },
        {
            "lessonId": "les_a1_43_02_boarding_and_alighting_etiquette",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Onboard Transit: Суух, Буух, and Polite Crowded Bus Expressions",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce essential phrases for navigating crowded Mongolian buses: 'Та буух уу?' (Are you getting off?), 'Урагшаа шахъя' (Let's move forward), and card tapping feedback sounds.",
            "communicativeOutcome": "Politely ask fellow passengers if they are disembarking and navigate movement through crowded bus aisles.",
            "objectivesIntroduced": ["obj_a1_43_02_navigate_crowded_bus_discourse"],
            "objectivesPracticed": ["obj_a1_43_01_identify_bus_routes_and_stops"],
            "objectivesReviewed": ["obj_a1_42_01_form_coordinating_converb_j_ch"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["буух", "суух", "урагшаа", "хүн", "өршөөгөөрэй"],
            "readingObjective": "Read passenger safety and transit etiquette posters inside city buses.",
            "listeningObjective": "Comprehend passengers exchanging quick courteous requests while moving toward exit doors.",
            "writingObjective": "Write 4 essential passenger courtesy phrases used during peak-hour commutes.",
            "spokenProductionObjective": "Ask a fellow passenger politely if they are alighting at the next stop.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Smooth physical and verbal navigation avoiding conflict in packed transit vehicles.",
            "prerequisiteLessonIds": ["les_a1_43_01_bus_routes_and_stop_names"],
            "reviewsLessonIds": ["les_a1_42_01_coordinating_converb_morphology"],
            "reviewsUnitIds": ["unit_a1_42_coordinating_converb_clause_linking_"],
            "reviewReason": "Use converbs for physical transit actions (Карт уншуулаад суух).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Authentic background bus rumble with realistic passenger exchanges.",
            "successCriteria": [
                "Ask 'Та дараагийн буудал дээр буух уу?' fluently.",
                "Pardon oneself when moving toward exit doors politely ('Өршөөгөөрэй, би бууя')."
            ],
            "masteryEvidence": [
                "Produces spontaneous polite responses during simulated crowded bus scenarios.",
                "Distinguishes front-door boarding from rear-door alighting conventions."
            ],
            "recommendedExerciseModalities": ["situational_roleplay", "cloze_selection", "audio_matching"]
        },
        {
            "lessonId": "les_a1_43_03_transit_map_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Ulaanbaatar Urban Transit Route Maps",
            "lessonType": "reading_development",
            "primaryPurpose": "Read city bus route schematics, transit navigation mobile apps (UB Smart Bus), and transfer point maps.",
            "communicativeOutcome": "Plan an urban route identifying where to board, where to transfer, and how many stops to travel.",
            "objectivesIntroduced": ["obj_a1_43_03_read_urban_transit_maps"],
            "objectivesPracticed": [
                "obj_a1_43_01_identify_bus_routes_and_stops",
                "obj_a1_43_02_navigate_crowded_bus_discourse"
            ],
            "objectivesReviewed": ["obj_a1_25_03_read_building_directories"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_case_ablative_origin"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["чиглэл", "дамжин суух", "төв", "талбай", "буудал"],
            "readingObjective": "Read a 60-word urban transit route guide detailing bus numbers Ch-1, Ch-2, and transfer points.",
            "listeningObjective": None,
            "writingObjective": "Transcribe the boarding stop, transfer stop, and alighting stop for a planned journey across the city.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Independent navigation of municipal public transit systems.",
            "prerequisiteLessonIds": ["les_a1_43_02_boarding_and_alighting_etiquette"],
            "reviewsLessonIds": ["les_a1_25_03_urban_directory_reading"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine transit stops with urban landmarks and street locative markers.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading transit app route instructions clearly.",
            "successCriteria": [
                "Locate the transfer stop ('Багшийн дээд дээр дамжин сууна') on the map.",
                "Calculate total number of stops between boarding and destination."
            ],
            "masteryEvidence": [
                "Answers 4 route-planning comprehension questions with zero error.",
                "Selects the most direct bus line between two distant city districts."
            ],
            "recommendedExerciseModalities": ["route_map_navigation", "transfer_planning", "short_answer"]
        },
        {
            "lessonId": "les_a1_43_04_onboard_announcements_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Tracking Onboard Stop Chimes and Audio PAs",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse automated onboard audio announcements and driver intercom notifications in transit.",
            "communicativeOutcome": "Recognize the current stop and upcoming stop announcements in noisy moving bus conditions.",
            "objectivesIntroduced": ["obj_a1_43_04_track_onboard_announcements"],
            "objectivesPracticed": ["obj_a1_43_01_identify_bus_routes_and_stops"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["дараагийн", "буудал", "онгойх", "хаагдах", "болгоомжтой"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 onboard bus audio chimes and identify the next stop announced in each clip.",
            "writingObjective": "Transcribe 5 stop names heard onto a linear transit line map.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard broadcast",
            "pragmaticTarget": "Auditory vigilance preventing missed alighting stops.",
            "prerequisiteLessonIds": ["les_a1_43_02_boarding_and_alighting_etiquette"],
            "reviewsLessonIds": ["les_a1_43_01_bus_routes_and_stop_names"],
            "reviewsUnitIds": ["unit_a1_43_public_transit_commuting_bus_routes_"],
            "reviewReason": "Zero-vocabulary auditory lab training bus announcement recognition.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic onboard bus audio with automated voice chime and engine noise.",
            "successCriteria": [
                "Identify all 5 announced stops accurately despite engine hum.",
                "Distinguish current stop from next stop ('Дараагийн буудал: ...')."
            ],
            "masteryEvidence": [
                "Scores 100% on the onboard audio stop recognition test.",
                "Alerts partner in roleplay when their target stop is announced."
            ],
            "recommendedExerciseModalities": ["audio_stop_matching", "map_tracking", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_43_05_transit_commute_navigation_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Navigating a City Commute with a Peer",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate taking public transit together across town: waiting at a stop, boarding, paying with card, and alighting at the right stop.",
            "communicativeOutcome": "Conduct a fluid commuting dialogue handling all phases of public bus travel with a companion.",
            "objectivesIntroduced": ["obj_a1_43_05_execute_city_transit_commute"],
            "objectivesPracticed": [
                "obj_a1_43_01_identify_bus_routes_and_stops",
                "obj_a1_43_02_navigate_crowded_bus_discourse",
                "obj_a1_43_03_read_urban_transit_maps"
            ],
            "objectivesReviewed": ["obj_a1_40_03_describe_complete_routes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_case_ablative_origin", "gram_a1_converb_coordinating_j_ch"],
            "grammarReinforced": ["gram_a1_converb_coordinating_j_ch"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_travel_transport"],
            "previousVocabularyReused": ["автобус", "буудал", "буух", "суух", "карт", "явах"],
            "readingObjective": "Read simulated transit scenario prompt cards.",
            "listeningObjective": "Comprehend companion's directions on when to prepare to alight.",
            "writingObjective": "Draft a short 3-sentence text message telling a friend which bus you just boarded.",
            "spokenProductionObjective": "Execute an 8-turn conversation navigating bus arrival, boarding, and stop alert.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Relaxed and practical coordination during shared daily transit.",
            "prerequisiteLessonIds": [
                "les_a1_43_03_transit_map_reading",
                "les_a1_43_04_onboard_announcements_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_43_01_bus_routes_and_stop_names"],
            "reviewsUnitIds": ["unit_a1_43_public_transit_commuting_bus_routes_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 43 transit skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating urban transit navigation.",
            "successCriteria": [
                "Confirm bus line number and destination before boarding.",
                "Execute the alighting dialogue ('Буудал дөхөж байна, бууя') smoothly."
            ],
            "masteryEvidence": [
                "Completes transit roleplay without communication breakdown.",
                "Demonstrates authentic cultural awareness of Ulaanbaatar bus customs."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "commute_simulation", "text_messaging"]
        }
    ])

    # =========================================================================
    # UNIT 44: Workday Schedule Synthesis: Chronological Diary (pos 44)
    # 6 Lessons | Targets: ProdLem=20, RecLem=8, ProdExp=6, RecExp=3
    # Budget: (6,3,2,1), (6,2,2,1), (4,2,1,1), (4,1,1,0), (0,0,0,0), (0,0,0,0)
    # Lesson 6 is Section 3 Capstone Checkpoint!
    # =========================================================================
    u = u_map[44]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_44_01_chronological_diary_composition",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "A Day in My Life: Chronological Time Anchors",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce transitional chronological markers (өглөө эрт 'early morning', үдийн хоолны дараа 'after lunch', оройдоо 'in the evening', эцэст нь 'finally') structuring a full day's narrative.",
            "communicativeOutcome": "Structure a coherent multi-paragraph chronological account of a full typical workday.",
            "objectivesIntroduced": ["obj_a1_44_01_structure_chronological_diary"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_42_02_chain_multiple_actions"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReinforced": ["gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["өглөө", "өдөр", "орой", "шөнө", "ажил", "эхлэх"],
            "readingObjective": "Read a model student diary entry detailing a complete 16-hour daily cycle.",
            "listeningObjective": "Hear a narrator recounting their chronological day from waking to bedtime.",
            "writingObjective": "Write a 4-paragraph chronological outline using target transitional phrases.",
            "spokenProductionObjective": "Summarize one's typical day aloud from morning to evening in 60 seconds.",
            "registerTarget": "Everyday standard reflective",
            "pragmaticTarget": "Synthesizing diverse daily experiences into a well-ordered narrative.",
            "prerequisiteLessonIds": ["les_a1_43_05_transit_commute_navigation_synthesis"],
            "reviewsLessonIds": ["les_a1_42_02_multiaction_routine_chains"],
            "reviewsUnitIds": ["unit_a1_42_coordinating_converb_clause_linking_"],
            "reviewReason": "Chain diverse daily actions into a coherent chronological text.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Smooth narrative pacing illustrating paragraph-level transitions.",
            "successCriteria": [
                "Use 3 or more chronological transitional markers correctly.",
                "Maintain consistent habitual aspect or past tense throughout the narrative."
            ],
            "masteryEvidence": [
                "Produces a structured 50-word daily diary outline.",
                "Orders 5 narrative segments into proper diurnal sequence."
            ],
            "recommendedExerciseModalities": ["chronological_composition", "paragraph_ordering", "cued_production"]
        },
        {
            "lessonId": "les_a1_44_02_work_study_balance_lexicon",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Balancing Demands: Хичээл, Ажил, and Чөлөөт Цаг",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce vocabulary for balancing commitments: чөлөөт цаг (free time), даалгавар (assignment/homework), ядрах (to get tired), амрах (to rest), төлөвлөх (to plan).",
            "communicativeOutcome": "Discuss work-life balance, study pressures, and relaxation routines in personal reflections.",
            "objectivesIntroduced": ["obj_a1_44_02_discuss_work_life_balance"],
            "objectivesPracticed": ["obj_a1_44_01_structure_chronological_diary"],
            "objectivesReviewed": ["obj_a1_38_02_use_frequency_adverbs"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["чөлөөтэй", "завгүй", "ажил", "амрах", "цаг"],
            "readingObjective": "Read university counseling articles on managing student stress and study timetables.",
            "listeningObjective": "Comprehend students sharing tips on how they balance part-time jobs with classes.",
            "writingObjective": "Draft 4 sentences evaluating one's personal weekly balance between work and rest.",
            "spokenProductionObjective": "Explain to a peer how you manage your homework assignments alongside sports.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Thoughtful personal reflection and empathetic social sharing.",
            "prerequisiteLessonIds": ["les_a1_44_01_chronological_diary_composition"],
            "reviewsLessonIds": ["les_a1_38_02_habitual_frequency_adverbs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_s"],
            "reviewReason": "Combine frequency adverbs with lifestyle balance verbs.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm conversational audio exploring lifestyle reflections.",
            "successCriteria": [
                "Express balance using 'завтай' and 'завгүй' correctly.",
                "Describe rest and study activities using habitual aspect."
            ],
            "masteryEvidence": [
                "Produces 'Би хичээлийн дараа амрах дуртай' smoothly.",
                "Identifies healthy vs unbalanced schedule patterns from reading."
            ],
            "recommendedExerciseModalities": ["lifestyle_evaluation", "sentence_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_44_03_diary_writing_workshop",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Composing an Authentic 60-Word Daily Diary",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate synthesizing clock times, transit routes, converbial chains, and habitual actions into an authentic written diary entry.",
            "communicativeOutcome": "Compose an authentic, well-structured 60-word personal journal entry detailing a full day.",
            "objectivesIntroduced": ["obj_a1_44_03_compose_full_day_diary"],
            "objectivesPracticed": [
                "obj_a1_44_01_structure_chronological_diary",
                "obj_a1_44_02_discuss_work_life_balance"
            ],
            "objectivesReviewed": ["obj_a1_39_01_apply_temporal_dative"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar", "gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["өдөр", "цаг", "сургууль", "номын сан", "уулзах"],
            "readingObjective": "Read a rubric detailing grammatical and chronological criteria for personal journal entries.",
            "listeningObjective": "Comprehend a teacher's audio feedback on student daily diary compositions.",
            "writingObjective": "Compose a full 60-word personal journal entry describing yesterday or a typical workday.",
            "spokenProductionObjective": "Read one's composed journal entry aloud with natural prosody and confidence.",
            "registerTarget": "Everyday standard reflective written",
            "pragmaticTarget": "Autonomous extended written expression in standard Mongolian.",
            "prerequisiteLessonIds": ["les_a1_44_02_work_study_balance_lexicon"],
            "reviewsLessonIds": ["les_a1_39_01_temporal_dative_marking"],
            "reviewsUnitIds": ["unit_a1_39_temporal_dative_locative_times_deadl"],
            "reviewReason": "Incorporate exact clock times marked with temporal dative into narrative writing.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm teacher guidance audio modeling expressive reading of personal journals.",
            "successCriteria": [
                "Write 6-8 cohesive sentences totaling at least 50-60 words.",
                "Incorporate at least 2 converbial chains and 3 distinct clock times."
            ],
            "masteryEvidence": [
                "Produces a grammatically correct 60-word personal diary entry.",
                "Shows zero confusion between Cyrillic case endings throughout text."
            ],
            "recommendedExerciseModalities": ["guided_journal_writing", "peer_editing", "rubric_assessment"]
        },
        {
            "lessonId": "les_a1_44_04_comparative_diaries_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: A Day in Ulaanbaatar vs A Day in the Countryside",
            "lessonType": "reading_development",
            "primaryPurpose": "Read authentic parallel diary excerpts contrasting a university student's day in Ulaanbaatar with a young herder's day in Arkhangai province.",
            "communicativeOutcome": "Compare, contrast, and extract detailed diurnal rhythms from parallel authentic Mongolian diary texts.",
            "objectivesIntroduced": ["obj_a1_44_04_read_comparative_diaries"],
            "objectivesPracticed": [
                "obj_a1_44_01_structure_chronological_diary",
                "obj_a1_44_02_discuss_work_life_balance"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReviewed": ["gram_a1_case_ablative_origin"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["хот", "хөдөө", "мал", "машин", "гэр", "байшин"],
            "readingObjective": "Read two parallel 65-word diary texts contrasting urban and rural daily routines.",
            "listeningObjective": None,
            "writingObjective": "Complete a Venn diagram identifying 3 shared daily activities and 3 unique activities for each setting.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard cultural",
            "pragmaticTarget": "Deep cultural appreciation of the dual nomadic-urban fabric of modern Mongolia.",
            "prerequisiteLessonIds": ["les_a1_44_03_diary_writing_workshop"],
            "reviewsLessonIds": ["les_a1_44_01_chronological_diary_composition"],
            "reviewsUnitIds": ["unit_a1_44_workday_schedule_synthesis_chronolog"],
            "reviewReason": "Consolidate written reading comprehension of extended multi-paragraph diary entries.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Expressive narration contrasting urban bus sounds with rural pastoral quietude.",
            "successCriteria": [
                "Identify which protagonist wakes earlier and which travels further for work.",
                "Extract cultural vocabulary specific to ger life vs apartment life."
            ],
            "masteryEvidence": [
                "Answers 5 comparative reading comprehension questions with 100% accuracy.",
                "Identifies that both protagonists value evening family tea time."
            ],
            "recommendedExerciseModalities": ["comparative_reading", "venn_diagram_sorting", "short_answer"]
        },
        {
            "lessonId": "les_a1_44_05_chronological_day_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Tracking a Full Day's Timeline from Audio Monologue",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse an extended 90-second spoken monologue where a speaker narrates their entire day from 6:30 AM to 11:00 PM.",
            "communicativeOutcome": "Accurately reconstruct a speaker's full 24-hour timeline and activity log from continuous speech.",
            "objectivesIntroduced": ["obj_a1_44_05_track_extended_diurnal_monologue"],
            "objectivesPracticed": ["obj_a1_44_01_structure_chronological_diary"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["өглөө", "цаг", "ажил", "үдэш", "унтах"],
            "readingObjective": None,
            "listeningObjective": "Listen to a continuous 90-second daily life audio narrative and plot 6 milestones on a blank 24h timeline.",
            "writingObjective": "Transcribe 6 time points and corresponding actions into an activity tracker.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard narrative",
            "pragmaticTarget": "Sustained listening stamina and real-time temporal mapping.",
            "prerequisiteLessonIds": ["les_a1_44_03_diary_writing_workshop"],
            "reviewsLessonIds": ["les_a1_44_02_work_study_balance_lexicon"],
            "reviewsUnitIds": ["unit_a1_44_workday_schedule_synthesis_chronolog"],
            "reviewReason": "Zero-vocabulary auditory lab testing extended temporal listening comprehension.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic native speaker monologue with natural narrative pacing and colloquial fillers.",
            "successCriteria": [
                "Reconstruct all 6 timeline points with correct clock times.",
                "Identify what unexpected interruption delayed the speaker in the afternoon."
            ],
            "masteryEvidence": [
                "Scores 100% on the extended diurnal timeline listening test.",
                "Accurately maps activities to morning, midday, and late evening intervals."
            ],
            "recommendedExerciseModalities": ["audio_timeline_reconstruction", "error_detection", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_44_06_section_03_capstone_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Culminating Capstone: Section 3 Diurnal Mastery Assessment",
            "lessonType": "checkpoint",
            "primaryPurpose": "Comprehensive summative evaluation certifying full communicative mastery across all Section 3 competencies (Units 34-44: telling time, weekdays, calendar dates/seasons, infinitives, habitual aspect, temporal datives, ablative origin, witnessed past, coordinating converbs, transit navigation, and daily diary synthesis).",
            "communicativeOutcome": "Demonstrate complete communicative independence in organizing, discussing, and narrating time-bound schedules, personal habits, travel routes, and chronological experiences.",
            "objectivesIntroduced": [],
            "objectivesPracticed": [
                "obj_a1_34_01_tell_hours_and_half_hours",
                "obj_a1_35_01_identify_weekdays",
                "obj_a1_36_01_name_months_and_seasons",
                "obj_a1_37_01_form_infinitive_kh",
                "obj_a1_38_01_form_habitual_dag",
                "obj_a1_39_01_apply_temporal_dative",
                "obj_a1_40_01_form_ablative_origin",
                "obj_a1_41_01_form_witnessed_past_laa",
                "obj_a1_42_01_form_coordinating_converb_j_ch",
                "obj_a1_43_01_identify_bus_routes_and_stops",
                "obj_a1_44_01_structure_chronological_diary"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_telling_time_clock_calendar",
                "gram_a1_verb_dictionary_infinitive_kh",
                "gram_a1_verb_tense_present_habitual_dag",
                "gram_a1_case_dative_locative_temporal",
                "gram_a1_case_ablative_origin",
                "gram_a1_verb_tense_past_witnessed_laa",
                "gram_a1_converb_coordinating_j_ch"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [],
            "phonologyPracticed": [
                "phono_vowel_harmony_suffixes",
                "phono_stress_initial_and_full_vowels",
                "phono_consonant_assimilation"
            ],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_10_identifying_objects",
                "comm_a1_11_counting_simple_quantities",
                "comm_a1_05_asking_identity_origin"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar", "lex_a1_daily_routines_hobbies", "lex_a1_travel_transport"],
            "previousVocabularyReused": ["цаг", "өдөр", "сар", "ажил", "сургууль", "автобус", "босох", "явах", "ирэх"],
            "readingObjective": "Read a multi-genre dossier combining university lecture schedules, transit timetables, personal diary entries, and project deadlines.",
            "listeningObjective": "Comprehend a multi-speaker radio program discussing changing seasonal habits, daily commutes, and work schedules in Ulaanbaatar.",
            "writingObjective": "Compose a comprehensive 60-word personal dossier detailing weekly routines, recent weekend highlights, and upcoming semester milestones.",
            "spokenProductionObjective": "Deliver a 90-second structured oral presentation summarizing one's daily life, favorite hobbies, and typical transit commute.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Complete communicative autonomy across temporal, habitual, and transit discourse.",
            "prerequisiteLessonIds": [
                "les_a1_44_04_comparative_diaries_reading",
                "les_a1_44_05_chronological_day_listening_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_39_06_mid_section_03_checkpoint",
                "les_a1_40_06_travel_booking_synthesis",
                "les_a1_41_06_weekend_debrief_synthesis",
                "les_a1_42_06_errand_coordination_synthesis",
                "les_a1_43_05_transit_commute_navigation_synthesis",
                "les_a1_44_03_diary_writing_workshop"
            ],
            "reviewsUnitIds": [
                "unit_a1_34_telling_clock_time_tsag_minut_hagas",
                "unit_a1_35_days_of_the_week_weekly_calendars",
                "unit_a1_36_calendar_dates_months_seasons",
                "unit_a1_37_verbal_dictionary_infinitive_suffix_",
                "unit_a1_38_habitual_present_participle_aspect_s",
                "unit_a1_39_temporal_dative_locative_times_deadl",
                "unit_a1_40_ablative_of_spatial_temporal_origin",
                "unit_a1_41_witnessed_past_verbal_tense_suffix_",
                "unit_a1_42_coordinating_converb_clause_linking_",
                "unit_a1_43_public_transit_commuting_bus_routes_",
                "unit_a1_44_workday_schedule_synthesis_chronolog"
            ],
            "reviewReason": "Summative section capstone certifying cumulative pedagogical and communicative mastery of Section 3.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Standardized benchmark assessment recordings across diverse real-world audio genres.",
            "successCriteria": [
                "Demonstrate integrated mastery across all 11 units in Section 3.",
                "Exhibit fluent and error-free usage of time markers, converb chaining, and verbal aspect."
            ],
            "masteryEvidence": [
                "Successfully passes all 4 assessment modalities (reading, listening, writing, oral presentation).",
                "Shows spontaneous command of Mongolian temporal grammar without hesitation or transfer errors."
            ],
            "recommendedExerciseModalities": ["comprehensive_assessment", "oral_presentation", "dossier_audit"]
        }
    ])

    return lessons
