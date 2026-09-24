"""
Section 3 Generator (Units 34 - 44): 63 Lessons
Temporality, Diurnal Cycles, and Routines
"""

import json
from typing import List, Dict, Any

def build_sec03() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}
    lessons = []

    # =========================================================================
    # UNIT 34: Telling Clock Time: Цаг, Минут, Хагас (pos 34)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[34]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_34_01_exact_hours_and_half_hours",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "On the Hour: Цаг and Хагас Time Expressions",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce conventions for telling exact hours and half-hours using 'цаг' (o'clock/hour) and 'хагас' (half past).",
            "communicativeOutcome": "Ask for and tell the current time on the hour and half-hour accurately in everyday speech.",
            "objectivesIntroduced": ["obj_a1_34_01_tell_hours_and_half_hours"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "grammarIntroduced": ["gram_a1_telling_time_clock_calendar"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["хэд", "нэг", "хоёр", "арван хоёр"],
            "readingObjective": "Read analog and digital clock faces displaying whole and half hours.",
            "listeningObjective": "Hear spoken time inquiries and responses ('Одоо цаг хэд болж байна вэ?' - 'Таван цаг болж байна').",
            "writingObjective": "Write down 4 clock times in words based on visual clock diagrams.",
            "spokenProductionObjective": "State aloud the current time upon hearing an inquiry.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Prompt and clear time reporting in interpersonal encounters.",
            "prerequisiteLessonIds": ["les_a1_33_06_section_02_capstone_checkpoint"],
            "reviewsLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Repurpose cardinal numbers 1-12 as hour markers with 'цаг'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural prosodic contour of 'Цаг хэд болж байна вэ?'.",
            "successCriteria": [
                "Formulate 'хэдэн цаг' questions correctly with question particle 'вэ'.",
                "Express half past an hour using 'хагас' (e.g. 'хоёр цаг хагас')."
            ],
            "masteryEvidence": [
                "Produces 'Одоо гурван цаг хагас болж байна' from a 3:30 clock prompt.",
                "Differentiates 'хэдэн цаг' (what time) from 'хэзээ' (when)."
            ],
            "recommendedExerciseModalities": ["clock_reading", "cued_production", "matching"]
        },
        {
            "lessonId": "les_a1_34_02_minutes_past_and_to_the_hour",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Precision Minutes: Минут, Өнгөрч, and Дутуу",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce minute designations with 'өнгөрч байна' (past) and 'дутуу байна' (to/until the next hour).",
            "communicativeOutcome": "State precise minutes past and to the hour for train departures, appointments, and meeting schedules.",
            "objectivesIntroduced": ["obj_a1_34_02_tell_precise_minutes_past_and_to"],
            "objectivesPracticed": ["obj_a1_34_01_tell_hours_and_half_hours"],
            "objectivesReviewed": ["obj_a1_27_02_count_decades_up_to_100"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "хорин", "гучин", "дөчин"],
            "readingObjective": "Read flight and train timetables displaying 24-hour and 12-hour minute notations.",
            "listeningObjective": "Comprehend public transit broadcast announcements specifying departure minutes.",
            "writingObjective": "Write 4 time expressions using 'өнгөрч байна' and 'дутуу байна'.",
            "spokenProductionObjective": "State exact time to a partner down to 5-minute precision intervals.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Punctual clarity preventing missed travel or appointment departures.",
            "prerequisiteLessonIds": ["les_a1_34_01_exact_hours_and_half_hours"],
            "reviewsLessonIds": ["les_a1_27_02_tens_and_counting_to_100"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Recycle numbers 1-59 into precise minute descriptions.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear distinction between 'өнгөрч' and 'дутуу' in rapid speech.",
            "successCriteria": [
                "Use 'өнгөрч байна' for minutes 1-29 past the hour.",
                "Use 'дутуу байна' for minutes approaching the next hour (e.g. 'Арван цагт арван минут дутуу')."
            ],
            "masteryEvidence": [
                "Produces 'Таван цаг арван минут өнгөрч байна' for 5:10.",
                "Produces 'Зургаан цагт таван минут дутуу' for 5:55."
            ],
            "recommendedExerciseModalities": ["time_conversion", "cloze_selection", "audio_matching"]
        },
        {
            "lessonId": "les_a1_34_03_time_drills_and_appointment_setting",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Setting Meeting and Class Times",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining time expressions with postpositional particles, temporal adverbs, and polite scheduling proposals.",
            "communicativeOutcome": "Negotiate and agree upon exact meeting times for study sessions and doctor appointments.",
            "objectivesIntroduced": ["obj_a1_34_03_negotiate_meeting_times"],
            "objectivesPracticed": [
                "obj_a1_34_01_tell_hours_and_half_hours",
                "obj_a1_34_02_tell_precise_minutes_past_and_to"
            ],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["уулзах", "ярилцах", "хэзээ", "хаана"],
            "readingObjective": "Read calendar appointment invites with suggested meeting times.",
            "listeningObjective": "Comprehend spoken appointment proposals and time counter-offers.",
            "writingObjective": "Draft a short 3-sentence message suggesting a meeting time and location.",
            "spokenProductionObjective": "Negotiate a time slot with a classmate in a short oral exchange.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Flexibility in proposing alternative times when initial slots conflict.",
            "prerequisiteLessonIds": ["les_a1_34_02_minutes_past_and_to_the_hour"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine time inquiries with 'Хэдэн цагт вэ?'.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational rhythm in appointment setting dialogues.",
            "successCriteria": [
                "Propose a time using '... цагт уулзъя' smoothly.",
                "Accept or decline suggested meeting hours with appropriate politeness."
            ],
            "masteryEvidence": [
                "Completes a 4-turn appointment negotiation roleplay without communicative breakdown.",
                "Converts 24h schedule entries into natural 12h colloquial spoken speech."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "calendar_scheduling"]
        },
        {
            "lessonId": "les_a1_34_04_schedule_board_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Public Timetables and Station Displays",
            "lessonType": "reading_development",
            "primaryPurpose": "Read bus, intercity coach, and train departure boards, doctor consultation schedules, and shop opening hours.",
            "communicativeOutcome": "Extract departure times, operating hours, and break intervals from published schedules.",
            "objectivesIntroduced": ["obj_a1_34_04_read_station_timetables"],
            "objectivesPracticed": ["obj_a1_34_01_tell_hours_and_half_hours"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цагийн хуваарь", "нээх", "хаах", "завсарлага"],
            "readingObjective": "Read a 55-word multi-route station schedule board.",
            "listeningObjective": None,
            "writingObjective": "Transcribe 4 departure times and route numbers into a trip planner matrix.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard informational",
            "pragmaticTarget": "Independent navigation of civic transport and public facility hours.",
            "prerequisiteLessonIds": ["les_a1_34_03_time_drills_and_appointment_setting"],
            "reviewsLessonIds": ["les_a1_34_01_exact_hours_and_half_hours"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Consolidate written recognition of time formats in institutional timetables.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration modeling station informational announcements.",
            "successCriteria": [
                "Identify lunch break hours ('Цайны завсарлага 13:00-14:00') accurately.",
                "Extract arrival and departure times for 3 target routes."
            ],
            "masteryEvidence": [
                "Answers 4 schedule comprehension questions with 100% accuracy.",
                "Identifies which department closes earliest based on published hours."
            ],
            "recommendedExerciseModalities": ["timetable_scanning", "matching", "short_answer"]
        },
        {
            "lessonId": "les_a1_34_05_time_announcements_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Public Transit and Broadcast Time Pings",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid radio time checks, airport boarding announcements, and station departure pings.",
            "communicativeOutcome": "Accurately record announced departure times and schedule changes amidst background echo.",
            "objectivesIntroduced": ["obj_a1_34_05_parse_transit_time_announcements"],
            "objectivesPracticed": ["obj_a1_34_01_tell_hours_and_half_hours"],
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
            "previousVocabularyReused": ["цаг", "минут", "эхлэх", "дуусах", "хүлээх"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 public transit audio announcements and record the exact departure times heard.",
            "writingObjective": "Transcribe 5 departure times and platform numbers into a transit log.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard broadcast",
            "pragmaticTarget": "Auditory precision under public acoustic reverberation and chime interruptions.",
            "prerequisiteLessonIds": ["les_a1_34_03_time_drills_and_appointment_setting"],
            "reviewsLessonIds": ["les_a1_34_02_minutes_past_and_to_the_hour"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying time perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic public station chime and PA system audio quality.",
            "successCriteria": [
                "Transcribe all 5 departure times without minute or hour errors.",
                "Recognize delay announcements ('15 минутаар хойшиллоо')."
            ],
            "masteryEvidence": [
                "Correctly maps audio announcements to 5 departure gates on a visual map.",
                "Catches last-minute schedule modifications accurately."
            ],
            "recommendedExerciseModalities": ["audio_transcription", "gate_mapping", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_34_06_schedule_synchronization_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Synchronizing Daily Itineraries",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Coordinate a shared travel or study itinerary with a partner, resolving scheduling conflicts and agreeing on pickup times.",
            "communicativeOutcome": "Conduct a fluid dialogue coordinating multiple time-bound activities throughout a day.",
            "objectivesIntroduced": ["obj_a1_34_06_coordinate_daily_itinerary"],
            "objectivesPracticed": [
                "obj_a1_34_01_tell_hours_and_half_hours",
                "obj_a1_34_02_tell_precise_minutes_past_and_to",
                "obj_a1_34_03_negotiate_meeting_times"
            ],
            "objectivesReviewed": ["obj_a1_28_05_execute_contact_exchange"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["цаг", "өглөө", "өдөр", "орой", "уулзах", "явах"],
            "readingObjective": "Read conflicting daily schedule cards during an information-gap task.",
            "listeningObjective": "Comprehend partner's stated availability and time constraints.",
            "writingObjective": "Produce a synchronized joint schedule detailing 4 shared daily activities and times.",
            "spokenProductionObjective": "Execute an 8-turn scheduling conversation finding mutually open time windows.",
            "registerTarget": "Courteous standard neutral",
            "pragmaticTarget": "Constructive compromise in schedule alignment.",
            "prerequisiteLessonIds": [
                "les_a1_34_04_schedule_board_reading",
                "les_a1_34_05_time_announcements_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_34_03_time_drills_and_appointment_setting"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 34 time-telling skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational scheduling exchange between two busy students.",
            "successCriteria": [
                "Negotiate pickup and meeting times using correct temporal particles without hesitation.",
                "Agree upon 3 common activity times meeting both partners' schedule limits."
            ],
            "masteryEvidence": [
                "Successfully builds an agreed joint schedule within 2 minutes.",
                "Both partners produce identical written timelines from their conversation."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "itinerary_matching"]
        }
    ])

    return lessons
