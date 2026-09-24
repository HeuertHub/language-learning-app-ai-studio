"""
Script to generate gen_sec04_part2.py with Units 49 - 53
"""

import json

sec04_part2_code = '''"""
Section 4 Generator - Part 2 (Units 49 - 53)
Polite Requests, Sequential Converb, Transactions, Grocery Markets, and Hospitality Protocol
"""

import json
from typing import List, Dict, Any

def get_sec04_part2_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}
    lessons = []

    # =========================================================================
    # UNIT 49: Polite Request Imperative: Suffixes -аарай/-ээрэй/-оорой/-өөрэй (pos 49)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # Lesson 6 is the MID-SECTION 4 CHECKPOINT!
    # =========================================================================
    u = u_map[49]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_49_01_polite_imperative_aarai_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Courteous Guidance: The Polite Imperative -аарай/-ээрэй/-оорой/-өөрэй",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the courteous request / polite imperative suffix -аарай/-ээрэй/-оорой/-өөрэй ('please do...', 'be sure to...') and four-way vowel harmony governing allomorph selection.",
            "communicativeOutcome": "Formulate warm, polite requests, reminders, and hospitable directives (e.g. 'Маргааш ирээрэй' - Please come tomorrow; 'Цай уугаарай' - Please drink tea).",
            "objectivesIntroduced": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["ирэх", "уух", "суух", "хүлээх", "үзэх"],
            "readingObjective": "Read courteous instructional signage and parting notes containing -аарай/-ээрэй.",
            "listeningObjective": "Hear the four vowel harmonic allomorphs (-аарай/-ээрэй/-оорой/-өөрэй) in polite domestic and service instructions.",
            "writingObjective": "Attach the polite request suffix to 6 verb stems respecting four-way vowel harmony.",
            "spokenProductionObjective": "Direct a guest to take a seat and drink tea using polite imperative suffixes aloud.",
            "registerTarget": "Courteous standard polite",
            "pragmaticTarget": "Warm, considerate communication eliminating harsh imperative undertones.",
            "prerequisiteLessonIds": ["les_a1_48_06_social_weekend_planner_synthesis"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Contrast first-person volitional intention (-я) with second-person polite imperative (-аарай).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Gentle, hospitable intonation typical of Mongolian courteous requests.",
            "successCriteria": [
                "Apply -аарай to /a/, -ээрэй to /e, i/, -оорой to /o/, -өөрэй to /ö/ stems.",
                "Distinguish bare command stems from gentle polite requests."
            ],
            "masteryEvidence": [
                "Conjugates ирэх -> ирээрэй, суух -> суугаарай, орох -> ороорой accurately.",
                "Produces 'Та тухлан суугаарай' (Please sit comfortably) fluently."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_transformation", "cued_production"]
        },
        {
            "lessonId": "les_a1_49_02_farewell_wishes_and_daily_reminders",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Parting Blessings: Сайн яваарай and Daily Courtesies",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce conventional parting formulas and daily reminders built with -аарай: 'Сайн яваарай' (Have a good journey), 'Сайн суугаарай' (Stay well), 'Дараа уулзаарай', 'Болгоомжтой яваарай' (Travel safely).",
            "communicativeOutcome": "Deliver customary parting blessings and safety reminders to departing guests, friends, and travelers.",
            "objectivesIntroduced": ["obj_a1_49_02_deliver_parting_blessings"],
            "objectivesPracticed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "objectivesReviewed": ["obj_a1_46_02_offer_and_request_beverages"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_adverbial_modifiers_time_manner"],
            "grammarReinforced": ["gram_a1_adverbial_modifiers_time_manner"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_culture_traditions", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["сайн", "явах", "суух", "болгоомжтой", "дараа"],
            "readingObjective": "Read farewell greeting cards and departing SMS messages.",
            "listeningObjective": "Comprehend hosts delivering customary departure wishes at doorways and station platforms.",
            "writingObjective": "Draft 4 farewell text messages wishing safe travels, restful sleep, and prompt return.",
            "spokenProductionObjective": "Wish a departing friend a safe journey using 'Сайн яваарай' and 'Болгоомжтой яваарай'.",
            "registerTarget": "Courteous standard cultural",
            "pragmaticTarget": "Culturally authentic departure blessings vital to Mongolian hospitality etiquette.",
            "prerequisiteLessonIds": ["les_a1_49_01_polite_imperative_aarai_allomorphs"],
            "reviewsLessonIds": ["les_a1_46_02_beverage_preferences_and_tea_service"],
            "reviewsUnitIds": ["unit_a1_46_beverages_tea_traditional_dairy_off"],
            "reviewReason": "Synthesize hospitality reception with respectful departure protocols.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm, emotional parting prosody at the conclusion of visits.",
            "successCriteria": [
                "Select 'Сайн яваарай' for departing parties and 'Сайн суугаарай' for staying hosts.",
                "Deliver 'Болгоомжтой яваарай' with natural cadence."
            ],
            "masteryEvidence": [
                "Uses correct departure blessing based on whether speaker is leaving or staying.",
                "Produces fluid parting sequences at end of roleplay."
            ],
            "recommendedExerciseModalities": ["farewell_matching", "dialogue_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_49_03_service_requests_and_instructions_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Courteous Requests in Public and Commercial Services",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate generating polite requests in stores, libraries, offices, and taxis ('Энд зогсоорой', 'Энийг хараарай', 'Түр хүлээгээрэй').",
            "communicativeOutcome": "Direct service providers, drivers, and clerks with courteous imperative forms.",
            "objectivesIntroduced": ["obj_a1_49_03_request_commercial_services"],
            "objectivesPracticed": [
                "obj_a1_49_01_form_polite_imperative_aarai",
                "obj_a1_49_02_deliver_parting_blessings"
            ],
            "objectivesReviewed": ["obj_a1_43_02_request_bus_stops"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_travel_transport"],
            "previousVocabularyReused": ["зогсох", "хүлээх", "өгөх", "харах", "түр"],
            "readingObjective": "Read public courtesy notices in transit vehicles and service offices.",
            "listeningObjective": "Comprehend taxi passengers and counter customers issuing polite instructions.",
            "writingObjective": "Write 4 polite requests for service interactions (e.g. asking to wait, stop, or show an item).",
            "spokenProductionObjective": "Ask a taxi driver to stop at the next intersection using 'Энд зогсоорой'.",
            "registerTarget": "Courteous standard public",
            "pragmaticTarget": "Assertive yet polite public navigation and commercial transactions.",
            "prerequisiteLessonIds": ["les_a1_49_02_farewell_wishes_and_daily_reminders"],
            "reviewsLessonIds": ["les_a1_43_02_requesting_stops_and_interchanges"],
            "reviewsUnitIds": ["unit_a1_43_public_transit_commuting_bus_routes"],
            "reviewReason": "Combine transit stop requests with the polite imperative suffix -аарай.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic urban ambient service audio with clear polite request directives.",
            "successCriteria": [
                "Formulate 'Энд зогсоорой' without hesitation.",
                "Politely request someone to wait a moment using 'Түр хүлээгээрэй'."
            ],
            "masteryEvidence": [
                "Completes a 4-turn taxi or counter transaction roleplay using -аарай directives.",
                "Modulates tone appropriately from urgency to calm courtesy."
            ],
            "recommendedExerciseModalities": ["service_roleplay", "instruction_matching", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_49_04_public_notice_signs_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Public Safety and Politeness Notices",
            "lessonType": "reading_development",
            "primaryPurpose": "Read public courtesy signs, safety reminders, and instructional notices in banks, transit centers, and clinics.",
            "communicativeOutcome": "Interpret official courtesy instructions, queue guidelines, and safety warnings.",
            "objectivesIntroduced": ["obj_a1_49_04_read_public_courtesy_signs"],
            "objectivesPracticed": [
                "obj_a1_49_01_form_polite_imperative_aarai",
                "obj_a1_49_02_deliver_parting_blessings"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_demonstratives_ene_tere"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["хаалга", "хаах", "цэвэрхэн", "байх", "орох"],
            "readingObjective": "Read 5 authentic public notices (e.g. 'Хаалгаа сайн хаана уу', 'Гуталдаа улавч өмсөөрэй').",
            "listeningObjective": None,
            "writingObjective": "Transcribe the imperative verb forms found across the 5 public notices.",
            "spokenProductionObjective": None,
            "registerTarget": "Public instructional formal",
            "pragmaticTarget": "Accurate civic compliance with posted guidelines and safety notices.",
            "prerequisiteLessonIds": ["les_a1_49_03_service_requests_and_instructions_drills"],
            "reviewsLessonIds": ["les_a1_49_01_polite_imperative_aarai_allomorphs"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Consolidate written recognition of polite imperative endings on public signage.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear official narration reading public instructional signage.",
            "successCriteria": [
                "Extract the core required action from each public notice.",
                "Identify which notice applies to doors, footwear, or queuing."
            ],
            "masteryEvidence": [
                "Matches 5 signs to their English summaries with 100% accuracy.",
                "Translates core polite verbs (-аарай) correctly into polite English imperatives."
            ],
            "recommendedExerciseModalities": ["sign_matching", "action_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_49_05_polite_instructions_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Discerning Polite Reminders vs Direct Commands",
            "lessonType": "listening_development",
            "primaryPurpose": "Acoustically distinguish between bare command stems (e.g. 'Суу!', 'Ир!') and polite request forms with -аарай/-ээрэй ('Суугаарай', 'Ирээрэй').",
            "communicativeOutcome": "Differentiate tone and register between curt commands and considerate polite invitations in spoken speech.",
            "objectivesIntroduced": ["obj_a1_49_05_discern_polite_imperative_audio"],
            "objectivesPracticed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_culture_traditions", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["суу", "суугаарай", "ир", "ирээрэй", "болгоомжтой"],
            "readingObjective": None,
            "listeningObjective": "Listen to 6 paired audio sentences and classify each as either a bare command or a polite reminder.",
            "writingObjective": "Transcribe the 3 polite reminder sentences heard in the audio pairs.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard comparative",
            "pragmaticTarget": "Auditory sensitivity to register nuances and social politeness markers.",
            "prerequisiteLessonIds": ["les_a1_49_03_service_requests_and_instructions_drills"],
            "reviewsLessonIds": ["les_a1_49_02_farewell_wishes_and_daily_reminders"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Zero-vocabulary auditory lab training register perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Paired voice samples demonstrating stark contrast between abrupt commands and gentle polite requests.",
            "successCriteria": [
                "Consistently distinguish bare imperative stems from polite -аарай forms in connected speech.",
                "Identify polite intonation markers accompanying courteous suffixes."
            ],
            "masteryEvidence": [
                "Scores 6/6 on the command vs polite request audio classification test.",
                "Explains the pragmatic difference between the paired sentences."
            ],
            "recommendedExerciseModalities": ["register_classification", "transcription", "audio_discrimination"]
        },
        {
            "lessonId": "les_a1_49_06_section_04_mid_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Section 4 Mid-Section Checkpoint: Dining, Social Outings, and Courtesy",
            "lessonType": "checkpoint",
            "primaryPurpose": "Comprehensive diagnostic evaluation assessing cumulative mastery of Section 4 Units 45-49: traditional cuisine ordering, dairy offerings, comitative accompaniment/possession (-тай), volitional intention (-я), and polite requests (-аарай).",
            "communicativeOutcome": "Demonstrate integrated communicative proficiency across dining, social invitations, companionship, and courteous directives.",
            "objectivesIntroduced": ["obj_a1_49_06_section_04_mid_mastery"],
            "objectivesPracticed": [
                "obj_a1_45_02_order_food_at_counter",
                "obj_a1_46_02_offer_and_request_beverages",
                "obj_a1_47_01_form_comitative_accompaniment",
                "obj_a1_47_02_express_possession_with_comitative",
                "obj_a1_48_01_form_volitional_ya",
                "obj_a1_49_01_form_polite_imperative_aarai"
            ],
            "objectivesReviewed": [
                "obj_a1_44_06_section_03_capstone_mastery",
                "obj_a1_45_01_describe_food_attributively"
            ],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_noun_phrase_attributive_adjective",
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_verb_volitional_intention_ya",
                "gram_a1_verb_imperative_polite_aarai"
            ],
            "grammarReviewed": [
                "gram_a1_case_accusative_definite_object",
                "gram_a1_verb_tense_past_witnessed_laa"
            ],
            "grammarReinforced": [
                "gram_a1_noun_phrase_attributive_adjective",
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_verb_volitional_intention_ya",
                "gram_a1_verb_imperative_polite_aarai"
            ],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_vowel_harmony_suffixes", "phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_non_initial_reduction", "phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_01_greetings_and_farewells",
                "comm_a1_03_introduce_peer_third_party",
                "comm_a1_10_identifying_objects"
            ],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_a1_food_dining", "lex_a1_culture_traditions",
                "lex_a1_friends_social_life", "lex_a1_shopping_services"
            ],
            "previousVocabularyReused": [
                "хоол", "бууз", "цай", "найз", "хамт", "явъя", "тэгье", "суугаарай", "сайн яваарай"
            ],
            "readingObjective": "Read a multi-turn social messaging thread organizing a dinner party and delegating responsibilities.",
            "listeningObjective": "Comprehend a multi-speaker conversation covering menu choices, companionship, and polite requests.",
            "writingObjective": "Compose a structured 50-word social message inviting friends to dinner, specifying who is bringing what, and closing with polite reminders.",
            "spokenProductionObjective": "Execute an unscripted multi-phase roleplay: inviting a peer to eat, ordering at a canteen, and delivering polite farewell wishes.",
            "registerTarget": "Courteous standard multi-register",
            "pragmaticTarget": "Seamless communicative integration across the first half of Section 4.",
            "prerequisiteLessonIds": [
                "les_a1_49_04_public_notice_signs_reading",
                "les_a1_49_05_polite_instructions_listening_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_45_06_canteen_lunch_dining_synthesis",
                "les_a1_46_05_tea_and_hospitality_synthesis",
                "les_a1_47_06_picnic_planning_synthesis",
                "les_a1_48_06_social_weekend_planner_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_45_traditional_cuisine_restaurant_order",
                "unit_a1_46_beverages_tea_traditional_dairy_off",
                "unit_a1_47_comitative_case_suffixes_tai_tei_toi",
                "unit_a1_48_volitional_intention_suffixes_ya_ye_"
            ],
            "reviewReason": "Mid-Section 4 diagnostic checkpoint verifying cumulative mastery of Units 45 through 49.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Integrated multi-speaker diagnostic assessment audio.",
            "successCriteria": [
                "Pass four diagnostic assessment modules (Ordering, Companionship, Volitional, Polite Imperative) with >=85% accuracy.",
                "Demonstrate zero consonant assimilation or vowel harmony errors on -тай, -я, and -аарай suffixes."
            ],
            "masteryEvidence": [
                "Executes all four diagnostic evaluation tasks successfully.",
                "Generates coherent, grammatically flawless multi-turn spoken dialogue."
            ],
            "recommendedExerciseModalities": [
                "integrated_roleplay", "cloze_diagnostic", "listening_evaluation", "writing_synthesis"
            ]
        }
    ])

    # =========================================================================
    # UNIT 50: Sequential Converb: Clause Connector -аад/-ээд/-оод/-өөд (pos 50)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[50]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_50_01_sequential_converb_aad_formation",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Chaining Actions in Time: The Sequential Converb -аад/-ээд/-оод/-өөд",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the sequential converb suffix -аад/-ээд/-оод/-өөд denoting completed anterior action ('having done X, then Y') and four-way vowel harmony rules.",
            "communicativeOutcome": "Connect two chronologically ordered actions into a single coherent clause (e.g. 'Би цай уугаад гарсан' - Having drank tea, I went out).",
            "objectivesIntroduced": ["obj_a1_50_01_form_sequential_converb_aad"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_42_01_link_clauses_with_converb_j_ch"],
            "grammarIntroduced": ["gram_a1_converb_sequential_aad"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_converb_coordinating_j_ch"],
            "grammarReinforced": ["gram_a1_converb_coordinating_j_ch"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_food_dining"],
            "previousVocabularyReused": ["идэх", "уух", "явах", "ирэх", "хийх"],
            "readingObjective": "Read sequenced daily routines and dining narratives using -аад/-ээд.",
            "listeningObjective": "Hear the four vowel harmonic allomorphs (-аад/-ээд/-оод/-өөд) linking narrative clauses.",
            "writingObjective": "Attach the sequential converb suffix to 6 verb stems following four-way vowel harmony.",
            "spokenProductionObjective": "State two sequential actions performed this morning using -аад aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear chronological clause linking without repetitive clunky coordinate structures.",
            "prerequisiteLessonIds": ["les_a1_49_06_section_04_mid_checkpoint"],
            "reviewsLessonIds": ["les_a1_42_01_coordinating_converb_j_ch_allomorphs"],
            "reviewsUnitIds": ["unit_a1_42_coordinating_converb_clause_linking"],
            "reviewReason": "Contrast simultaneous/manner coordination (-ж/-ч) with chronological succession (-аад).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural narrative rhythm connecting two sequential verbal clauses.",
            "successCriteria": [
                "Select -аад for /a/, -ээд for /e, i/, -оод for /o/, -өөд for /ö/ stems.",
                "Ensure anterior action precedes the main inflected matrix verb."
            ],
            "masteryEvidence": [
                "Conjugates идэх -> идээд, уух -> уугаад, орох -> ороод, үзэх -> үзээд accurately.",
                "Combines two simple sentences into one coherent sequential sentence."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_combining", "cued_production"]
        },
        {
            "lessonId": "les_a1_50_02_kitchen_preparation_sequences",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Kitchen Sequences: Chopping, Boiling, and Steaming with -аад",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce culinary action verbs (хэрчих 'to slice/chop', чанах 'to boil', хуурах 'to stir-fry', жигнэх 'to steam', зуурах 'to knead') in sequential procedural chains.",
            "communicativeOutcome": "Describe cooking preparation steps in order (e.g. 'Махаа хэрчээд тогоонд хуурна' - Having chopped the meat, stir-fry it in the wok).",
            "objectivesIntroduced": ["obj_a1_50_02_describe_culinary_steps_aad"],
            "objectivesPracticed": ["obj_a1_50_01_form_sequential_converb_aad"],
            "objectivesReviewed": ["obj_a1_45_01_describe_food_attributively"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": ["gram_a1_case_accusative_definite_object"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining"],
            "previousVocabularyReused": ["мах", "тогоо", "ус", "давс", "хийх"],
            "readingObjective": "Read illustrated cooking procedural steps for traditional dishes.",
            "listeningObjective": "Comprehend home cooks explaining step-by-step how to make Mongolian tea or noodle soup.",
            "writingObjective": "Draft 3 sequenced cooking instructions linking preparation steps with -аад.",
            "spokenProductionObjective": "Explain the first two steps of preparing khuushuur using sequential converbs aloud.",
            "registerTarget": "Everyday standard instructional",
            "pragmaticTarget": "Clear culinary instruction and recipe comprehension.",
            "prerequisiteLessonIds": ["les_a1_50_01_sequential_converb_aad_formation"],
            "reviewsLessonIds": ["les_a1_45_01_mongolian_menu_and_attributive_adjectives"],
            "reviewsUnitIds": ["unit_a1_45_traditional_cuisine_restaurant_order"],
            "reviewReason": "Combine culinary food nouns with sequential action verbs.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear instructional cadence describing cooking processes.",
            "successCriteria": [
                "Chain kitchen verbs accurately with -аад/-ээд.",
                "Maintain correct temporal logic in cooking sequences."
            ],
            "masteryEvidence": [
                "Orders scrambled cooking steps chronologically and writes connecting sentences.",
                "Produces 'Усаа буцалгаад цайгаа хийнэ' flawlessly."
            ],
            "recommendedExerciseModalities": ["recipe_sequencing", "sentence_construction", "visual_cue_chaining"]
        },
        {
            "lessonId": "les_a1_50_03_dining_routines_and_errands_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Chaining Daily Errands and Dining Outings",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate chaining multi-step daily outings, shopping trips, and meals ('Дэлгүүр ороод талх авна', 'Хоол идээд номын сан явъя').",
            "communicativeOutcome": "Fluently express multi-stop errand plans and activity chains combining sequential converbs with volitional verbs.",
            "objectivesIntroduced": ["obj_a1_50_03_chain_errands_and_outings"],
            "objectivesPracticed": [
                "obj_a1_50_01_form_sequential_converb_aad",
                "obj_a1_50_02_describe_culinary_steps_aad"
            ],
            "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_shopping_services"],
            "previousVocabularyReused": ["дэлгүүр", "талх", "номын сан", "явах", "авах"],
            "readingObjective": "Read weekend errand task lists arranged in geographic and chronological sequence.",
            "listeningObjective": "Comprehend friends coordinating two-step plans before meeting up.",
            "writingObjective": "Write 4 sentences describing planned sequential outings (e.g. going to bank, then eating lunch).",
            "spokenProductionObjective": "Propose a two-step afternoon plan to a classmate using -аад and -я aloud.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Efficient daily schedule planning and seamless errand coordination.",
            "prerequisiteLessonIds": ["les_a1_50_02_kitchen_preparation_sequences"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Combine sequential converb clauses with volitional matrix verbs ('... хийгээд явъя').",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio coordinating two-part errands.",
            "successCriteria": [
                "Formulate compound plans using [Verb 1]-аад [Verb 2]-я without hesitation.",
                "Ensure appropriate case marking on direct objects within converb clauses."
            ],
            "masteryEvidence": [
                "Completes a 4-turn errand coordination exchange smoothly.",
                "Produces 'Би банк ороод мөнгө аваад ирье' accurately."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "errand_chaining", "sentence_combining"]
        },
        {
            "lessonId": "les_a1_50_04_traditional_recipes_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Authentic Step-by-Step Recipes for Tsuivan and Buuz",
            "lessonType": "reading_development",
            "primaryPurpose": "Read authentic recipe texts detailing how to prepare traditional homemade tsuivan (fried noodle dish) and buuz (steamed dumplings).",
            "communicativeOutcome": "Extract ingredient lists, sequential preparation phases, and cooking times from written recipes.",
            "objectivesIntroduced": ["obj_a1_50_04_read_traditional_recipes"],
            "objectivesPracticed": [
                "obj_a1_50_01_form_sequential_converb_aad",
                "obj_a1_50_02_describe_culinary_steps_aad"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining"],
            "previousVocabularyReused": ["гурил", "мах", "сонгино", "жигнэх", "тогоо"],
            "readingObjective": "Read a 70-word authentic recipe for making traditional home tsuivan.",
            "listeningObjective": None,
            "writingObjective": "List the 4 sequential preparation stages extracted from the recipe.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard procedural",
            "pragmaticTarget": "Autonomous comprehension of culinary texts and household instructions.",
            "prerequisiteLessonIds": ["les_a1_50_03_dining_routines_and_errands_drills"],
            "reviewsLessonIds": ["les_a1_50_01_sequential_converb_aad_formation"],
            "reviewsUnitIds": ["unit_a1_50_sequential_converb_clause_connector"],
            "reviewReason": "Consolidate written recognition of sequential converb chains in instructional literature.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear procedural narration reading step-by-step recipe instructions.",
            "successCriteria": [
                "Identify which step comes first, second, and third in the recipe.",
                "Extract cooking durations and heat levels from text."
            ],
            "masteryEvidence": [
                "Answers 4 recipe comprehension questions with 100% accuracy.",
                "Accurately summarizes the dough preparation process in Mongolian."
            ],
            "recommendedExerciseModalities": ["recipe_scanning", "chronological_ordering", "short_answer"]
        },
        {
            "lessonId": "les_a1_50_05_sequential_actions_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Sequential Clauses in Connected Speech",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid spoken narratives where speakers link multiple actions using sequential converb suffixes without pauses.",
            "communicativeOutcome": "Accurately record the chronological order of events described in rapid natural speech.",
            "objectivesIntroduced": ["obj_a1_50_05_parse_sequential_clauses_audio"],
            "objectivesPracticed": ["obj_a1_50_01_form_sequential_converb_aad"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["хийгээд", "яваад", "үзээд", "ир", "өглөө"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 conversational clips and arrange the actions mentioned in each clip in exact chronological sequence.",
            "writingObjective": "Transcribe the sequential converb verb forms heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory tracking of temporal sequence in spontaneous spoken discourse.",
            "prerequisiteLessonIds": ["les_a1_50_03_dining_routines_and_errands_drills"],
            "reviewsLessonIds": ["les_a1_50_02_kitchen_preparation_sequences"],
            "reviewsUnitIds": ["unit_a1_50_sequential_converb_clause_connector"],
            "reviewReason": "Zero-vocabulary auditory lab training sequential converb acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural connected speech audio featuring fluid converb transitions.",
            "successCriteria": [
                "Arrange 4 sets of actions into correct chronological order based on audio.",
                "Distinguish -аад from coordinating -ж/-ч in rapid speech."
            ],
            "masteryEvidence": [
                "Scores 100% on the event chronological ordering listening test.",
                "Transcribes all heard -аад verbs with correct vowel harmony."
            ],
            "recommendedExerciseModalities": ["audio_event_ordering", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_50_06_cooking_and_hosting_masterclass_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Cooking Together and Serving Dinner",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate preparing dinner together with a friend: delegating kitchen tasks, narrating actions as they happen, and serving the finished meal to table.",
            "communicativeOutcome": "Conduct a collaborative kitchen cooking dialogue narrating and coordinating sequential preparation steps.",
            "objectivesIntroduced": ["obj_a1_50_06_coordinate_cooking_activity"],
            "objectivesPracticed": [
                "obj_a1_50_01_form_sequential_converb_aad",
                "obj_a1_50_02_describe_culinary_steps_aad",
                "obj_a1_50_03_chain_errands_and_outings"
            ],
            "objectivesReviewed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai", "gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["мах", "ногоо", "хэрчих", "хийх", "суугаарай", "идье"],
            "readingObjective": "Read simulated kitchen task cards delegating duties.",
            "listeningObjective": "Comprehend partner's updates on which ingredients are prepared.",
            "writingObjective": "Draft a 4-step preparation summary of the dish cooked during the simulation.",
            "spokenProductionObjective": "Execute an 8-turn collaborative cooking dialogue using sequential converbs and polite instructions.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Seamless teamwork and culinary coordination in a domestic setting.",
            "prerequisiteLessonIds": [
                "les_a1_50_04_traditional_recipes_reading",
                "les_a1_50_05_sequential_actions_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_50_03_dining_routines_and_errands_drills"],
            "reviewsUnitIds": ["unit_a1_50_sequential_converb_clause_connector"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 50 sequential converb skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating lively domestic cooking collaboration.",
            "successCriteria": [
                "Describe preparation stages using -аад fluently ('Би сонгиноо хэрчээд тогоонд хийлээ').",
                "Combine sequential converb with polite imperatives ('Махаа чанаад таваглаарай')."
            ],
            "masteryEvidence": [
                "Completes collaborative cooking roleplay smoothly within 2 minutes.",
                "Demonstrates flawless mastery of temporal clause chaining."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "kitchen_simulation", "procedural_reporting"]
        }
    ])

    # =========================================================================
    # UNIT 51: Settling the Bill & Canteen Transactions (pos 51)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[51]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_51_01_asking_for_the_check_and_receipt",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Settling the Tab: Тооцоогоо Хийе and Checking the Bill",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce essential billing vocabulary and counter payment requests: тооцоо 'bill/account', тооцооны хуудас 'receipt/invoice', тооцоо хийх 'to settle bill', нийт дүн 'total amount', and calling the waiter ('Тооцоогоо хийе').",
            "communicativeOutcome": "Ask for the check in restaurants and canteens, verify total sums, and ask for an official receipt (баримт).",
            "objectivesIntroduced": ["obj_a1_51_01_request_check_and_receipt"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": ["gram_a1_case_accusative_definite_object"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["тооцоо", "мөнгө", "өгөх", "авах", "хэд"],
            "readingObjective": "Read printed customer dining bill slips displaying itemized charges and total sums.",
            "listeningObjective": "Hear restaurant staff announcing total amounts and presenting check folders.",
            "writingObjective": "Write 3 phrases requesting the bill and asking for an electronic tax receipt (НӨАТ-ын баримт).",
            "spokenProductionObjective": "Call a restaurant server and ask for the check politely using 'Тооцоогоо хийе'.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Clear and polite settlement of commercial dining accounts.",
            "prerequisiteLessonIds": ["les_a1_50_06_cooking_and_hosting_masterclass_synthesis"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Use volitional form 'хийе' in standard payment request 'Тооцоогоо хийе'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Courteous customer callout intonation in a dining room.",
            "successCriteria": [
                "Formulate 'Тооцоогоо хийе' with authentic pronunciation.",
                "Ask for the receipt using 'Баримт авъя'."
            ],
            "masteryEvidence": [
                "Requests check and clarifies total amount in a 3-turn exchange.",
                "Identifies line items and total price on a printed bill."
            ],
            "recommendedExerciseModalities": ["bill_inspection", "roleplay_prompt", "cued_production"]
        },
        {
            "lessonId": "les_a1_51_02_payment_methods_cash_card_qpay",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Payment Channels: Бэлнээр, Картаар, and QPay QR Codes",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce payment modalities: бэлнээр 'in cash', картаар 'by card', дансаар 'by bank transfer', QPay-ээр 'via QPay QR code', and cashier inquiries ('Яаж төлөх вэ?').",
            "communicativeOutcome": "State payment method, ask to scan a QR code, and pay using cards or mobile apps.",
            "objectivesIntroduced": ["obj_a1_51_02_specify_payment_modality"],
            "objectivesPracticed": ["obj_a1_51_01_request_check_and_receipt"],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services"],
            "previousVocabularyReused": ["карт", "бэлэн", "төлөх", "яаж", "болох"],
            "readingObjective": "Read payment instruction stickers and QR code placards at retail checkouts.",
            "listeningObjective": "Comprehend cashiers asking whether payment will be in cash or by card.",
            "writingObjective": "Draft 3 short responses specifying card, cash, or mobile QR code payment.",
            "spokenProductionObjective": "Tell a cashier you will pay with QPay using 'Би QPay-ээр төлье'.",
            "registerTarget": "Everyday standard transactional",
            "pragmaticTarget": "Fast, modern transactional competence at Ulaanbaatar checkouts.",
            "prerequisiteLessonIds": ["les_a1_51_01_asking_for_the_check_and_receipt"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Ask payment questions using 'Яаж төлөх вэ?' with question particle вэ.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Crisp cashier-customer retail transaction audio.",
            "successCriteria": [
                "Respond accurately to 'Бэлнээр үү, картаар уу?'.",
                "Ask to scan QR code using 'QR кодоо харуулаарай'."
            ],
            "masteryEvidence": [
                "Completes payment transaction dialogue selecting digital payment without hesitation.",
                "Distinguishes instrumental endings -аар/-ээр across payment terms."
            ],
            "recommendedExerciseModalities": ["payment_matching", "checkout_roleplay", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_51_03_receipts_and_bill_verification_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Itemized Receipts and Mobile Payment Confirmations",
            "lessonType": "reading_development",
            "primaryPurpose": "Read itemized restaurant check slips, POS receipts with VAT lotto numbers (сугалааны дугаар), and mobile banking payment confirmation screens.",
            "communicativeOutcome": "Verify item counts, individual prices, total sums, and tax registration numbers from commercial receipts.",
            "objectivesIntroduced": ["obj_a1_51_03_read_receipts_and_pos_slips"],
            "objectivesPracticed": [
                "obj_a1_51_01_request_check_and_receipt",
                "obj_a1_51_02_specify_payment_modality"
            ],
            "objectivesReviewed": ["obj_a1_31_01_count_items_with_units"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_classifier_habits_neg_hoyor"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["төгрөг", "үнэ", "дүн", "дугаар", "огноо"],
            "readingObjective": "Read a printed dining receipt detailing 4 food items, unit prices, VAT breakdown, and final total.",
            "listeningObjective": None,
            "writingObjective": "Transcribe total amount, date, payment method, and dish item counts from the receipt.",
            "spokenProductionObjective": None,
            "registerTarget": "Transactional commercial printed",
            "pragmaticTarget": "Commercial literacy and financial verification in daily transactions.",
            "prerequisiteLessonIds": ["les_a1_51_02_payment_methods_cash_card_qpay"],
            "reviewsLessonIds": ["les_a1_31_01_measure_words_and_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_clas"],
            "reviewReason": "Read quantity and piece counts displayed on receipts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading itemized bill line items clearly.",
            "successCriteria": [
                "Locate the final payment total ('Нийт дүн') accurately.",
                "Verify whether any ordered dish was mistakenly charged twice."
            ],
            "masteryEvidence": [
                "Answers 4 receipt verification questions with 100% accuracy.",
                "Extracts payment timestamp and VAT lottery code successfully."
            ],
            "recommendedExerciseModalities": ["receipt_audit", "total_verification", "short_answer"]
        },
        {
            "lessonId": "les_a1_51_04_cashier_exchanges_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Parsing Numbers, Totals, and Change at Checkouts",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal exchanges at cash registers: totals quoted in thousands of tögrög, change given, and electronic payment prompts.",
            "communicativeOutcome": "Accurately write down spoken monetary amounts, payment confirmations, and change figures.",
            "objectivesIntroduced": ["obj_a1_51_04_parse_cashier_amounts_audio"],
            "objectivesPracticed": ["obj_a1_51_02_specify_payment_modality"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services"],
            "previousVocabularyReused": ["мянга", "төгрөг", "хариулт", "карт", "уншуулах"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 cashier announcements and record the exact price quoted and change returned for each transaction.",
            "writingObjective": "Transcribe the monetary figures heard in tögrög (e.g. 18,500₮, 42,000₮).",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard transactional",
            "pragmaticTarget": "Auditory precision parsing multi-digit prices in fast-paced retail environments.",
            "prerequisiteLessonIds": ["les_a1_51_02_payment_methods_cash_card_qpay"],
            "reviewsLessonIds": ["les_a1_51_01_asking_for_the_check_and_receipt"],
            "reviewsUnitIds": ["unit_a1_51_settling_the_bill_canteen_transacti"],
            "reviewReason": "Zero-vocabulary auditory lab training financial number comprehension.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic supermarket and cafe register ambiance with clear cashier number speech.",
            "successCriteria": [
                "Transcribe four 5-digit price figures correctly from audio.",
                "Identify change calculation phrases ('Таны хариулт хоёр мянга')."
            ],
            "masteryEvidence": [
                "Scores 100% on the checkout financial listening test.",
                "Identifies cashier card instructions ('Картаа энд уншуулаарай')."
            ],
            "recommendedExerciseModalities": ["audio_price_dictation", "change_calculation", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_51_05_canteen_settlement_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Settling the Bill at a Busy Restaurant",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate the complete end-of-meal payment process: signaling the waiter, requesting the check, splitting or paying the bill, choosing payment method, and getting the receipt.",
            "communicativeOutcome": "Conduct a fluid, confident billing settlement dialogue at a restaurant or canteen.",
            "objectivesIntroduced": ["obj_a1_51_05_execute_dining_settlement"],
            "objectivesPracticed": [
                "obj_a1_51_01_request_check_and_receipt",
                "obj_a1_51_02_specify_payment_modality",
                "obj_a1_51_03_read_receipts_and_pos_slips"
            ],
            "objectivesReviewed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["тооцоо", "дүн", "төлөх", "карт", "баярлалаа", "баримт"],
            "readingObjective": "Read simulated customer order receipts with varied menu charges.",
            "listeningObjective": "Comprehend waiter billing summaries and payment confirmation prompts.",
            "writingObjective": "Draft a short transaction confirmation log recording total amount and payment method.",
            "spokenProductionObjective": "Execute an 8-turn restaurant billing dialogue from asking for check to thanking staff.",
            "registerTarget": "Courteous standard transactional",
            "pragmaticTarget": "Seamless commercial closure of dining outings.",
            "prerequisiteLessonIds": [
                "les_a1_51_03_receipts_and_bill_verification_reading",
                "les_a1_51_04_cashier_exchanges_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_51_01_asking_for_the_check_and_receipt"],
            "reviewsUnitIds": ["unit_a1_51_settling_the_bill_canteen_transacti"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 51 billing transaction skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating polite dining bill settlement.",
            "successCriteria": [
                "Signal waiter and request check politely using 'Тооцоогоо хийе'.",
                "Select payment method, scan QR or hand card, and request receipt without confusion."
            ],
            "masteryEvidence": [
                "Completes billing roleplay within 90 seconds without hesitation.",
                "Both cashier and customer roles executed with flawless cultural courtesy."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "settlement_simulation", "receipt_verification"]
        }
    ])

    # =========================================================================
    # UNIT 52: Open Market Grocery Shopping & Bulk Quantities (pos 52)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[52]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_52_01_buying_by_weight_kilo_gram_bulk",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Weights and Quantities: Килограмм, Грамм, and Fresh Produce",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce metric weight and bulk quantity units used at open markets: килограмм / кило 'kg', грамм 'g', хагас кило 'half kg', уут 'bag/sack', and fresh produce terms (төмс, лууван, сонгино, байцаа, мах).",
            "communicativeOutcome": "Purchase meat, root vegetables, and flour specifying exact metric weights and bagged quantities.",
            "objectivesIntroduced": ["obj_a1_52_01_specify_bulk_weights_kilo"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_31_01_count_items_with_units"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_classifier_habits_neg_hoyor"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["килограмм", "төмс", "мах", "авах", "өгөх"],
            "readingObjective": "Read handwritten open-market produce price cards indicating price per kilo.",
            "listeningObjective": "Hear market vendors shouting produce weights and price per bag.",
            "writingObjective": "Write 4 grocery item requests specifying weight (e.g. 'Хоёр кило төмс авъя').",
            "spokenProductionObjective": "Ask a market stall vendor for 2 kg of potatoes and 500 grams of carrots aloud.",
            "registerTarget": "Everyday standard transactional",
            "pragmaticTarget": "Accurate procurement of staples at local food markets and grocery stores.",
            "prerequisiteLessonIds": ["les_a1_51_05_canteen_settlement_synthesis"],
            "reviewsLessonIds": ["les_a1_31_01_measure_words_and_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_clas"],
            "reviewReason": "Synthesize classifier counting habits with metric weight nouns (кило, грамм).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Bustling market vendor speech calling out produce weights and prices.",
            "successCriteria": [
                "Specify weights using 'кило' and 'грамм' accurately.",
                "Use 'хагас кило' naturally for 500 grams."
            ],
            "masteryEvidence": [
                "Orders 3 different vegetables by weight without hesitation.",
                "Combines weight specification with polite ordering formula 'авъя'."
            ],
            "recommendedExerciseModalities": ["weight_selection", "grocery_shopping_drills", "cued_production"]
        },
        {
            "lessonId": "les_a1_52_02_asking_prices_per_kilo_and_market_bargaining",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Stall Negotiations: Нэг Кило нь Хэд вэ? and Checking Freshness",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce market price inquiries: 'Нэг кило нь хэд вэ?' (How much is 1 kg?), 'Жоохон хямдруулах уу?' (Can you discount a bit?), and freshness inquiries (шинэ 'fresh', орон нутгийн 'local', Монгол төмс).",
            "communicativeOutcome": "Ask stall vendors for unit prices per kilo, verify freshness/origin, and politely negotiate minor bulk discounts.",
            "objectivesIntroduced": ["obj_a1_52_02_inquire_market_prices_and_origin"],
            "objectivesPracticed": ["obj_a1_52_01_specify_bulk_weights_kilo"],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReinforced": ["gram_a1_noun_phrase_attributive_adjective"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services"],
            "previousVocabularyReused": ["үнэ", "хямд", "шинэ", "хэд", "болох"],
            "readingObjective": "Read comparative price placards across adjacent market vendor stalls.",
            "listeningObjective": "Comprehend stall vendors quoting prices per kilogram and offering bundle deals.",
            "writingObjective": "Draft 3 questions asking price per kilo and whether the produce is domestically grown.",
            "spokenProductionObjective": "Ask a vendor the price per kilo of beef and whether it's fresh today.",
            "registerTarget": "Everyday standard open-market conversational",
            "pragmaticTarget": "Culturally appropriate market rapport, price negotiation, and quality verification.",
            "prerequisiteLessonIds": ["les_a1_52_01_buying_by_weight_kilo_gram_bulk"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine price queries with content question particle 'вэ' (Нэг кило нь хэд вэ?).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Lively open market ambiance with authentic vendor banter.",
            "successCriteria": [
                "Formulate 'Нэг кило нь хэд вэ?' fluently.",
                "Inquire about domestic origin using 'Монгол төмс мөн үү?'."
            ],
            "masteryEvidence": [
                "Completes a 4-turn market bargaining and inquiry dialogue successfully.",
                "Identifies discounted bulk pricing offers from vendor prompts."
            ],
            "recommendedExerciseModalities": ["market_negotiation", "origin_inquiry", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_52_03_market_placards_and_bulk_signs_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Bulk Placards at Bars and Naran Tuul Markets",
            "lessonType": "reading_development",
            "primaryPurpose": "Read handwritten cardboard signage, provincial origin banners (Сэлэнгийн төмс, Хөвсгөлийн мах), and sack-weight discount placards at major wholesale open markets.",
            "communicativeOutcome": "Extract commodity names, bag weights, provincial origin, and bulk discounts from open market signage.",
            "objectivesIntroduced": ["obj_a1_52_03_read_market_placards"],
            "objectivesPracticed": [
                "obj_a1_52_01_specify_bulk_weights_kilo",
                "obj_a1_52_02_inquire_market_prices_and_origin"
            ],
            "objectivesReviewed": ["obj_a1_40_01_form_ablative_origin"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_case_ablative_origin"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["төмс", "уут", "кило", "үнэ", "аймаг"],
            "readingObjective": "Read 4 authentic open market placard texts advertising bulk sack potatoes, carrots, and flour.",
            "listeningObjective": None,
            "writingObjective": "Transcribe the price comparison between single kilo purchases and 25kg sacks.",
            "spokenProductionObjective": None,
            "registerTarget": "Open market commercial handwritten",
            "pragmaticTarget": "Navigating wholesale markets to secure high-value food staples.",
            "prerequisiteLessonIds": ["les_a1_52_02_asking_prices_per_kilo_and_market_bargaining"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Read agricultural provenance markings on market produce placards.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading open market stall descriptions clearly.",
            "successCriteria": [
                "Extract commodity type and weight per sack from text.",
                "Calculate savings between per-kilo and full-sack purchases."
            ],
            "masteryEvidence": [
                "Answers 4 market reading comprehension questions with 100% accuracy.",
                "Identifies the authentic Selenge potato stall based on placard text."
            ],
            "recommendedExerciseModalities": ["placard_scanning", "bulk_calculation", "short_answer"]
        },
        {
            "lessonId": "les_a1_52_04_market_chatter_and_scales_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Parsing Weighed Produce Amounts in Open Market Ambience",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal exchanges at market weighing scales: weights announced, fractional kilos, and total prices quoted over market noise.",
            "communicativeOutcome": "Accurately capture weight amounts, item prices, and vendor confirmations from noisy market audio.",
            "objectivesIntroduced": ["obj_a1_52_04_parse_market_scale_audio"],
            "objectivesPracticed": ["obj_a1_52_01_specify_bulk_weights_kilo"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services"],
            "previousVocabularyReused": ["жин", "кило", "грам", "болох", "төгрөг"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 market stall scale recordings and write down the weighed amount and price for each item.",
            "writingObjective": "Transcribe the weighed produce names, quantities in kg/g, and total price for each customer.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard open-market colloquial",
            "pragmaticTarget": "Auditory resilience and precision in loud open-air commerce settings.",
            "prerequisiteLessonIds": ["les_a1_52_02_asking_prices_per_kilo_and_market_bargaining"],
            "reviewsLessonIds": ["les_a1_52_01_buying_by_weight_kilo_gram_bulk"],
            "reviewsUnitIds": ["unit_a1_52_open_market_grocery_shopping_bulk_q"],
            "reviewReason": "Zero-vocabulary auditory lab training market speech comprehension.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Atmospheric open-air food market audio with authentic scale weighing sounds.",
            "successCriteria": [
                "Transcribe four produce weights accurately from scale announcements.",
                "Extract total price in tögrög despite background market chatter."
            ],
            "masteryEvidence": [
                "Scores 100% on the weighed produce listening test.",
                "Catches fractional weights like 'хоёр кило зургаан зуун грамм' accurately."
            ],
            "recommendedExerciseModalities": ["audio_weight_logging", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_52_05_open_market_grocery_run_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Doing a Weekly Grocery Run at Bars Market",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a complete weekly grocery run at Bars Market: visiting vegetable and meat stalls, asking prices, purchasing multiple items by weight, checking freshness, and paying.",
            "communicativeOutcome": "Conduct a multi-stall grocery shopping simulation purchasing diverse items by weight with confidence.",
            "objectivesIntroduced": ["obj_a1_52_05_execute_market_grocery_run"],
            "objectivesPracticed": [
                "obj_a1_52_01_specify_bulk_weights_kilo",
                "obj_a1_52_02_inquire_market_prices_and_origin",
                "obj_a1_52_03_read_market_placards"
            ],
            "objectivesReviewed": ["obj_a1_51_02_specify_payment_modality"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_shopping_services", "lex_a1_food_dining"],
            "previousVocabularyReused": ["төмс", "мах", "сонгино", "кило", "үнэ", "бэлнээр", "баярлалаа"],
            "readingObjective": "Read simulated market shopping list with required weights and budget limits.",
            "listeningObjective": "Comprehend vendor weight calculations and price quotes across multiple stalls.",
            "writingObjective": "Draft a finalized grocery expense log detailing purchased items, weights, and total cost.",
            "spokenProductionObjective": "Execute an 8-turn market shopping simulation purchasing 3 staple food items by weight.",
            "registerTarget": "Courteous standard transactional",
            "pragmaticTarget": "Autonomous, budget-conscious household provisioning at open markets.",
            "prerequisiteLessonIds": [
                "les_a1_52_03_market_placards_and_bulk_signs_reading",
                "les_a1_52_04_market_chatter_and_scales_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_52_01_buying_by_weight_kilo_gram_bulk"],
            "reviewsUnitIds": ["unit_a1_52_open_market_grocery_shopping_bulk_q"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 52 open market skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating lively market bargaining and purchasing.",
            "successCriteria": [
                "Ask prices per kilo using 'Нэг кило нь хэд вэ?' at each stall.",
                "Specify weights accurately and pay within simulated budget."
            ],
            "masteryEvidence": [
                "Completes market run purchasing 3 distinct items within 2 minutes.",
                "Both buyer and seller roles executed with authentic pragmatic flair."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "shopping_simulation", "expense_logging"]
        }
    ])

    # =========================================================================
    # UNIT 53: Hospitality Protocol: Receiving Food with Both Hands (pos 53)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # Lesson 5 is the SECTION 4 CAPSTONE CHECKPOINT!
    # =========================================================================
    u = u_map[53]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_53_01_receiving_food_with_both_hands_protocol",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Sacred Hands: Receiving Food and Tea with Two Hands (Хоёр Гараараа)",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce core Mongolian hospitality etiquette vocabulary: хоёр гар 'two hands', баруун гар 'right hand', тохой 'elbow', тулах 'to support (elbow)', хүндэтгэх 'to respect', and receiving customs (хоёр гараараа авах 'to take with both hands').",
            "communicativeOutcome": "Demonstrate verbal and cultural awareness of receiving food, tea, and gifts with both hands or supported elbow.",
            "objectivesIntroduced": ["obj_a1_53_01_practice_two_handed_hospitality"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReinforced": ["gram_a1_noun_phrase_attributive_adjective"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_culture_traditions"],
            "previousVocabularyReused": ["гар", "авах", "өгөх", "цай", "баярлалаа"],
            "readingObjective": "Read illustrated cultural etiquette guides explaining Mongolian guest reception protocols.",
            "listeningObjective": "Hear elders explaining traditional rules for receiving cups and plates from hosts.",
            "writingObjective": "Write 3 sentences describing the proper posture and hand gesture when receiving tea.",
            "spokenProductionObjective": "Explain to a foreign visitor why food must be accepted with both hands in Mongolia.",
            "registerTarget": "Courteous standard cultural",
            "pragmaticTarget": "Deep cultural respect preventing unintended offenses in traditional households.",
            "prerequisiteLessonIds": ["les_a1_52_05_open_market_grocery_run_synthesis"],
            "reviewsLessonIds": ["les_a1_49_01_polite_imperative_aarai_allomorphs"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Use polite imperatives to instruct guests gently on respectful hospitality etiquette.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Dignified, respectful cultural narration describing traditional Mongolian customs.",
            "successCriteria": [
                "Name the customary gesture (хоёр гараараа авах) accurately.",
                "Explain the alternate method: taking with right hand while left hand supports the elbow."
            ],
            "masteryEvidence": [
                "Describes the hand protocol accurately in Mongolian: 'Баруун гараараа аваад, зүүн гараараа тохойгоо тулна'.",
                "Demonstrates the physical gesture during simulated food service."
            ],
            "recommendedExerciseModalities": ["cultural_etiquette_drills", "visual_matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_53_02_dining_taboos_and_ger_etiquette",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Ger Manners: Threshold Taboos, Knife Handling, and Stepping Over Food",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce traditional nomadic dining taboos (цээр): босгон дээр гишгэхгүй 'not stepping on threshold', хоол дээгүүр алхахгүй 'not stepping over food', хутганы үзүүр чиглүүлэхгүй 'not pointing knife point at people', and handling bowls by the rim.",
            "communicativeOutcome": "Recognize and state core Mongolian dining taboos and ger rules, warning peers politely when necessary.",
            "objectivesIntroduced": ["obj_a1_53_02_identify_ger_dining_taboos"],
            "objectivesPracticed": ["obj_a1_53_01_practice_two_handed_hospitality"],
            "objectivesReviewed": ["obj_a1_49_02_deliver_parting_blessings"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": ["gram_a1_adverbial_modifiers_time_manner"],
            "grammarReinforced": ["gram_a1_adverbial_modifiers_time_manner"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_culture_traditions"],
            "previousVocabularyReused": ["босго", "хутга", "хоол", "болгоомжтой", "болохгүй"],
            "readingObjective": "Read cultural taboos informational pamphlets displayed in national parks and cultural centers.",
            "listeningObjective": "Comprehend hosts and guides explaining ger layout rules and etiquette taboos.",
            "writingObjective": "Draft 3 polite reminders for visitors entering a traditional ger (e.g. 'Босгон дээр битгий гишгээрэй').",
            "spokenProductionObjective": "Warn a classmate politely not to step on the threshold or pass knife with blade facing outward.",
            "registerTarget": "Courteous standard cautionary",
            "pragmaticTarget": "Cultural sensitivity preventing sacrilege or discourtesy in rural and ger visits.",
            "prerequisiteLessonIds": ["les_a1_53_01_receiving_food_with_both_hands_protocol"],
            "reviewsLessonIds": ["les_a1_49_02_farewell_wishes_and_daily_reminders"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Formulate negative polite reminders using 'битгий ... -аарай'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Gentle, instructive guidance explaining traditional nomadic taboos.",
            "successCriteria": [
                "Identify the 3 most crucial ger taboos (threshold, knife handling, stepping over food).",
                "Formulate polite warning 'Босгон дээр битгий гишгээрэй'."
            ],
            "masteryEvidence": [
                "Matches 4 taboos to their cultural rationale with 100% accuracy.",
                "Executes a gentle reminder dialogue correcting simulated taboo behavior."
            ],
            "recommendedExerciseModalities": ["taboo_identification", "polite_warning_drills", "cultural_matching"]
        },
        {
            "lessonId": "les_a1_53_03_hospitality_guidebooks_and_elder_stories_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: The Etiquette of the Mongolian Hearth and Table",
            "lessonType": "reading_development",
            "primaryPurpose": "Read an authentic excerpt from a Mongolian cultural guide or elder's memoir recounting how guests are received with hot tea, curds, and blessed meat.",
            "communicativeOutcome": "Understand the spiritual and social significance of food offerings, hearth respect, and host-guest reciprocity in Mongolian culture.",
            "objectivesIntroduced": ["obj_a1_53_03_read_hospitality_literature"],
            "objectivesPracticed": [
                "obj_a1_53_01_practice_two_handed_hospitality",
                "obj_a1_53_02_identify_ger_dining_taboos"
            ],
            "objectivesReviewed": ["obj_a1_46_01_identify_dairy_and_tea"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_converb_sequential_aad"],
            "grammarReviewed": ["gram_a1_case_comitative_accompaniment"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_culture_traditions", "lex_a1_food_dining"],
            "previousVocabularyReused": ["зочин", "айлаар", "цай", "өрөм", "хүндэтгэл"],
            "readingObjective": "Read a 75-word narrative excerpt depicting an elder welcoming a traveler into a winter ger.",
            "listeningObjective": None,
            "writingObjective": "List 3 cultural gestures described in the text that demonstrate hospitality and respect.",
            "spokenProductionObjective": None,
            "registerTarget": "Literary and cultural narrative standard",
            "pragmaticTarget": "Appreciating the deeper philosophical values underlying Mongolian etiquette.",
            "prerequisiteLessonIds": ["les_a1_53_02_dining_taboos_and_ger_etiquette"],
            "reviewsLessonIds": ["les_a1_46_01_dairy_products_and_tea_culture"],
            "reviewsUnitIds": ["unit_a1_46_beverages_tea_traditional_dairy_off"],
            "reviewReason": "Review cultural dairy offerings in the context of hearth hospitality.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm storytelling voice evoking traditional countryside hospitality.",
            "successCriteria": [
                "Identify the hospitality sequence described in the text.",
                "Extract terms denoting respect, hospitality, and blessings."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Summarizes the host's primary obligations to travelers."
            ],
            "recommendedExerciseModalities": ["literary_scanning", "value_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_53_04_elder_blessings_and_gratitude_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Parsing Elder Blessings and Guest Gratitude Formulas",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse recorded spoken audio of elders offering food blessings (ерөөл), offering seconds, and guests expressing deep appreciation with traditional formulas.",
            "communicativeOutcome": "Accurately understand elder blessings and formulate authentic words of thanks when dining in Mongolian homes.",
            "objectivesIntroduced": ["obj_a1_53_04_parse_elder_blessings_audio"],
            "objectivesPracticed": ["obj_a1_53_01_practice_two_handed_hospitality"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_culture_traditions"],
            "previousVocabularyReused": ["буян", "ерөөл", "сайхан", "баярлалаа", "амттай"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 audio clips of elders serving food and identify the hospitality formula or blessing spoken in each.",
            "writingObjective": "Transcribe the gratitude phrases used by the guests in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Reverent cultural standard",
            "pragmaticTarget": "Auditory recognition of respectful elder discourse and traditional blessing cadences.",
            "prerequisiteLessonIds": ["les_a1_53_02_dining_taboos_and_ger_etiquette"],
            "reviewsLessonIds": ["les_a1_53_01_receiving_food_with_both_hands_protocol"],
            "reviewsUnitIds": ["unit_a1_53_hospitality_protocol_receiving_food"],
            "reviewReason": "Zero-vocabulary auditory lab training elder speech and blessing perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm resonant elder Mongolian voices speaking traditional hospitality formulas.",
            "successCriteria": [
                "Map 4 elder audio clips to their corresponding traditional blessings.",
                "Identify guest gratitude formulas ('Их амттай сайхан хоол болжээ, баярлалаа')."
            ],
            "masteryEvidence": [
                "Scores 100% on the elder blessing listening test.",
                "Transcribes all heard expressions with correct vowel harmony."
            ],
            "recommendedExerciseModalities": ["audio_blessing_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_53_05_section_04_capstone_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Section 4 Capstone Checkpoint: Traditional Dining, Commerce, and Hospitality",
            "lessonType": "checkpoint",
            "primaryPurpose": "Comprehensive summative evaluation certifying cumulative mastery of Section 4 Units 45-53: traditional cuisine, dairy offerings, comitative (-тай), volitional (-я), polite imperatives (-аарай), sequential converbs (-аад), restaurant billing, open market grocery shopping, and ger hospitality protocol.",
            "communicativeOutcome": "Demonstrate complete communicative and cultural proficiency across all Section 4 dining, market shopping, and hospitality benchmarks.",
            "objectivesIntroduced": ["obj_a1_53_05_section_04_capstone_mastery"],
            "objectivesPracticed": [
                "obj_a1_45_02_order_food_at_counter",
                "obj_a1_46_02_offer_and_request_beverages",
                "obj_a1_47_01_form_comitative_accompaniment",
                "obj_a1_48_01_form_volitional_ya",
                "obj_a1_49_01_form_polite_imperative_aarai",
                "obj_a1_50_01_form_sequential_converb_aad",
                "obj_a1_51_01_request_check_and_receipt",
                "obj_a1_52_01_specify_bulk_weights_kilo",
                "obj_a1_53_01_practice_two_handed_hospitality"
            ],
            "objectivesReviewed": [
                "obj_a1_44_06_section_03_capstone_mastery",
                "obj_a1_49_06_section_04_mid_mastery"
            ],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_noun_phrase_attributive_adjective",
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_verb_volitional_intention_ya",
                "gram_a1_verb_imperative_polite_aarai",
                "gram_a1_converb_sequential_aad"
            ],
            "grammarReviewed": [
                "gram_a1_case_dative_locative_temporal",
                "gram_a1_converb_coordinating_j_ch"
            ],
            "grammarReinforced": [
                "gram_a1_noun_phrase_attributive_adjective",
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_verb_volitional_intention_ya",
                "gram_a1_verb_imperative_polite_aarai",
                "gram_a1_converb_sequential_aad"
            ],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_vowel_harmony_suffixes", "phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_non_initial_reduction", "phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_01_greetings_and_farewells",
                "comm_a1_08_describing_daily_routines",
                "comm_a1_10_identifying_objects",
                "comm_a1_11_counting_simple_quantities"
            ],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_a1_food_dining", "lex_a1_shopping_services",
                "lex_a1_culture_traditions", "lex_a1_friends_social_life"
            ],
            "previousVocabularyReused": [
                "хоол", "бууз", "цай", "кило", "тооцоо", "явъя", "суугаарай", "идээд", "хоёр гар", "баярлалаа"
            ],
            "readingObjective": "Read a multi-genre dossier including an open market receipt, a traditional recipe, and a cultural hospitality invitation.",
            "listeningObjective": "Comprehend a multi-speaker audio recording featuring restaurant ordering, market negotiation, and ger hospitality reception.",
            "writingObjective": "Compose a comprehensive 60-word cultural summary describing a weekend visit to a nomadic family: arriving, presenting gifts with both hands, cooking tsuivan sequentially, and settling farewells.",
            "spokenProductionObjective": "Execute an unscripted 3-part capstone oral simulation: shopping at an open market, dining at a traditional eatery with bill payment, and demonstrating ger guest protocol.",
            "registerTarget": "Full Section 4 integrated register mastery",
            "pragmaticTarget": "Certified mastery of Section 4 communicative, commercial, and cultural competencies.",
            "prerequisiteLessonIds": [
                "les_a1_53_03_hospitality_guidebooks_and_elder_stories_reading",
                "les_a1_53_04_elder_blessings_and_gratitude_listening_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_49_06_section_04_mid_checkpoint",
                "les_a1_50_06_cooking_and_hosting_masterclass_synthesis",
                "les_a1_51_05_canteen_settlement_synthesis",
                "les_a1_52_05_open_market_grocery_run_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_49_polite_request_imperative_suffixes_",
                "unit_a1_50_sequential_converb_clause_connector",
                "unit_a1_51_settling_the_bill_canteen_transacti",
                "unit_a1_52_open_market_grocery_shopping_bulk_q",
                "unit_a1_53_hospitality_protocol_receiving_food"
            ],
            "reviewReason": "Comprehensive summative evaluation certifying cumulative mastery across Section 4.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Standardized benchmark assessment recordings with high-fidelity studio acoustic standards.",
            "successCriteria": [
                "Pass all five assessment sub-batteries with >=85% accuracy.",
                "Demonstrate flawless grammatical mastery of -тай, -я, -аарай, and -аад suffixes in spontaneous oral production."
            ],
            "masteryEvidence": [
                "Executes all capstone simulation tasks without instructor correction.",
                "Demonstrates authentic physical and verbal mastery of Mongolian hospitality protocol."
            ],
            "recommendedExerciseModalities": [
                "capstone_simulation", "portfolio_evaluation", "comprehensive_assessment", "oral_interview"
            ]
        }
    ])

    return lessons
'''

with open("scripts/framework_builder/gen_sec04_part2.py", "w") as f:
    f.write(sec04_part2_code)

print("gen_sec04_part2.py created successfully!")
