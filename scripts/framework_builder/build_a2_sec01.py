"""
Section 1 Generator (Units 64 - 72): 46 Lessons
Urban Transit, Wayfinding & Public Space Encounters
"""

import json
from typing import List, Dict, Any

def build_a2_sec01() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a2.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}

    lessons: List[Dict[str, Any]] = []

    # =========================================================================
    # UNIT 64: Navigating Ulaanbaatar Bus Routes & Digital Smart Cards (pos 64)
    # 6 Lessons | Targets: ProdLem=21, RecLem=10, ProdExp=5, RecExp=3
    # Budget: (4,2,1,1), (6,3,1,1), (0,0,0,0), (5,3,1,0), (4,2,2,1), (2,0,0,0) = (21, 10, 5, 3)
    # =========================================================================
    u = u_map[64]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a2_64_01_instrumental_transport_allomorphs",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 1,
            "title": "Taking the Bus: The Instrumental Suffix (-аар/-ээр/-оор/-өөр)",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the instrumental case suffix to express vehicles, transport modes, and physical instruments of transit.",
            "communicativeOutcome": "Explain which mode of transport you use to commute across the city (e.g. 'Би автобусаар явна', 'Би машинаар ирлээ').",
            "objectivesIntroduced": ["obj_a2_64_01_express_transport_instrumental"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_38_01_habitual_routines"],
            "grammarIntroduced": ["gram_a2_case_instrumental_transport_language"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_sov_word_order", "gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": ["phono_a2_instrumental_suffix_vowel_harmony"],
            "phonologyPracticed": ["phono_a1_long_vowels"], "phonologyReviewed": ["phono_a1_masculine_feminine_harmony"],
            "communicativeFunctionsIntroduced": ["comm_a2_18_buying_bus_train_tickets"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": ["comm_a1_17_describing_daily_routines"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 2, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_domain_transportation_travel", "lex_domain_city_urban_life"],
            "previousVocabularyReused": ["автобус", "машин", "гэр", "сургууль", "ажил", "явах", "ирэх"],
            "readingObjective": "Read short commuters' forum sentences contrasting travel modes (bus vs walking vs car).",
            "listeningObjective": "Recognize the instrumental suffix when speakers state how they arrived at school or work.",
            "writingObjective": "Write 3 simple sentences declaring daily commute methods using instrumental case marking.",
            "spokenProductionObjective": "Answer prompts regarding how you travel to work or university using instrumental nouns.",
            "registerTarget": "Standard polite everyday transit register",
            "pragmaticTarget": "Stating transit choices plainly and neutrally without unnecessary hesitation.",
            "prerequisiteLessonIds": ["les_a1_63_06_elementary_stage_synthesis_capstone"],
            "reviewsLessonIds": ["les_a1_43_01_bus_routes_stops_intro"],
            "reviewsUnitIds": ["unit_a1_43_public_transit_commuting_bus_routes"],
            "reviewReason": "Builds directly upon A1 public transit vocabulary by introducing the formal instrumental case.",
            "audioSuitability": "standard_speech_synthesis_acceptable", "audioPurpose": "Model vowel harmony allomorphs of the instrumental case on stems ending in consonants and vowels.",
            "successCriteria": [
                "Selects correct instrumental allomorph (-аар, -ээр, -оор, -өөр) based on root vowel harmony",
                "Constructs well-formed SOV sentences specifying transit mode as instrumental adjunct"
            ],
            "masteryEvidence": "Produces 'Би өдөр бүр арван хоёр дугаар автобусаар явдаг' accurately matching vowel harmony.",
            "recommendedExerciseModalities": ["suffix_selection", "sentence_construction", "case_marking"]
        },
        {
            "lessonId": "les_a2_64_02_bus_routes_u_money_cards",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 2,
            "title": "Smart Card Tap & Bus Stops: U-Money in Practice",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce practical vocabulary for digital transit smart cards (U-Money), balance checks, and boarding etiquette.",
            "communicativeOutcome": "Purchase, tap, and reload a municipal bus card, and ask where to check card balance.",
            "objectivesIntroduced": ["obj_a2_64_02_u_money_card_lexicon"],
            "objectivesPracticed": ["obj_a2_64_01_express_transport_instrumental"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a2_case_instrumental_transport_language"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_a1_consonant_clusters"], "phonologyReviewed": ["phono_a1_vowel_reduction_non_initial"],
            "communicativeFunctionsIntroduced": ["comm_a2_18_buying_bus_train_tickets"],
            "communicativeFunctionsPracticed": ["comm_a1_22_making_purchases"], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_domain_transportation_travel", "lex_domain_commerce_transactions"],
            "previousVocabularyReused": ["мөнгө", "карт", "хэд", "өгөх", "авах"],
            "readingObjective": "Read kiosk stickers instructing passengers where and how to reload U-Money cards.",
            "listeningObjective": "Understand convenience store cashier explaining minimum card reload amounts.",
            "writingObjective": "Note down card balance and bus line numbers in a pocket memo.",
            "spokenProductionObjective": "Ask a kiosk vendor to top up a transit card with a specified amount of tugriks.",
            "registerTarget": "Everyday transactional customer-to-vendor register",
            "pragmaticTarget": "Handing over card and cash with respectful two-handed or right-hand elbow support gesture.",
            "prerequisiteLessonIds": ["les_a2_64_01_instrumental_transport_allomorphs"],
            "reviewsLessonIds": ["les_a1_51_01_canteen_bill_settlement"],
            "reviewsUnitIds": ["unit_a1_51_settling_the_bill_canteen_transacti"],
            "reviewReason": "Connects money transactions from A1 canteen encounters to digital smart transit reloading.",
            "audioSuitability": "mongolian_voice_required", "audioPurpose": "Demonstrate authentic fast speech customer requests at small street convenience kiosks.",
            "successCriteria": [
                "Accurately names smart card components: цэнэглэх (top up), үлдэгдэл (balance), уншуулах (tap card)",
                "Conducts a smooth kiosk transaction requesting a 5,000 or 10,000 MNT card recharge"
            ],
            "masteryEvidence": "Requests 'U-Money карт таван мянган төгрөгөөр цэнэглэж өгөөч' fluently at a sales counter.",
            "recommendedExerciseModalities": ["contextual_cloze", "dialogue_completion", "categorization"]
        },
        {
            "lessonId": "les_a2_64_03_transit_announcements_decoding",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 3,
            "title": "Onboard Chimes & Next Stop PA Announcements",
            "lessonType": "listening_development",
            "primaryPurpose": "Develop acoustic decoding skills for automated public bus announcements, next-stop chimes, and door warnings.",
            "communicativeOutcome": "Identify target stop names, upcoming transfer points, and door alerts from authentic bus audio.",
            "objectivesIntroduced": ["obj_a2_64_03_decode_automated_bus_announcements"],
            "objectivesPracticed": ["obj_a2_64_02_u_money_card_lexicon"], "objectivesReviewed": ["obj_a1_43_01_identify_bus_stops"],
            "grammarIntroduced": [],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_a1_diphthongs", "phono_a1_nasal_vowels"], "phonologyReviewed": ["phono_a1_vowel_length_distinction"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a2_18_buying_bus_train_tickets"],
            "communicativeFunctionsReviewed": ["comm_a1_19_inquiring_location"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0, "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_domain_transportation_travel"],
            "previousVocabularyReused": ["зогсоол", "дараагийн", "хаалга", "хаагдах", "буух", "суух"],
            "readingObjective": "",
            "listeningObjective": "Identify next stop name ('Дараагийн зогсоол...'), transfer alerts, and door closing warnings from onboard automated PA clips.",
            "writingObjective": "",
            "spokenProductionObjective": "Confirm with fellow passenger if the bus stops at your target destination.",
            "registerTarget": "Public automated civic announcement register",
            "pragmaticTarget": "Attuning ear to automated voice inflection and noisy bus engine acoustics.",
            "prerequisiteLessonIds": ["les_a2_64_02_bus_routes_u_money_cards"],
            "reviewsLessonIds": ["les_a1_43_03_bus_stop_listening"],
            "reviewsUnitIds": ["unit_a1_43_public_transit_commuting_bus_routes"],
            "reviewReason": "Progresses from simple A1 stop name recognition to parsing compound automated PA sentences.",
            "audioSuitability": "mongolian_voice_required", "audioPurpose": "Provide high-fidelity onboard recordings with authentic bus background ambient rumble and chime.",
            "successCriteria": [
                "Identifies stop name following 'Дараагийн зогсоол' under simulated cabin engine noise",
                "Extracts door safety warning 'Хаалга хаагдлаа, болгоомжтой байгаарай' without visual text"
            ],
            "masteryEvidence": "Correctly matches 4 recorded bus announcements to their corresponding route map stop sequences.",
            "recommendedExerciseModalities": ["listening_comprehension", "sequencing", "phonetic_discrimination"]
        },
        {
            "lessonId": "les_a2_64_04_route_maps_schedules_reading",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 4,
            "title": "Deciphering Bus Shelter Route Diagrams & Operating Hours",
            "lessonType": "reading_development",
            "primaryPurpose": "Build reading skills for authentic municipal bus stop route placards, direction arrows, and first/last bus schedules.",
            "communicativeOutcome": "Read a bus shelter schedule to determine operating hours, route paths, and whether a bus runs on weekends.",
            "objectivesIntroduced": ["obj_a2_64_04_read_bus_route_placards"],
            "objectivesPracticed": ["obj_a2_64_01_express_transport_instrumental"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a2_case_instrumental_transport_language"],
            "grammarReviewed": ["gram_a1_case_ablative_origin", "gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_a1_vowel_reduction_non_initial"], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a2_17_giving_multistep_directions"],
            "communicativeFunctionsReviewed": ["comm_a1_18_scheduling_appointments"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_domain_transportation_travel", "lex_domain_time_calendar"],
            "previousVocabularyReused": ["өглөө", "орой", "цаг", "эхлэх", "дуусах", "чиглэл"],
            "readingObjective": "Locate departure interval (зай/хүлээх хугацаа), terminal stop, and evening cutoff time on a bus route diagram.",
            "listeningObjective": "",
            "writingObjective": "Transcribe bus schedule operating window into a personal calendar entry.",
            "spokenProductionObjective": "Explain to a peer how often the bus runs and when the final bus departs.",
            "registerTarget": "Public administrative transit signage",
            "pragmaticTarget": "Extracting vital transit facts quickly from complex graphic layouts.",
            "prerequisiteLessonIds": ["les_a2_64_02_bus_routes_u_money_cards"],
            "reviewsLessonIds": ["les_a1_35_01_days_of_the_week_intro"],
            "reviewsUnitIds": ["unit_a1_35_days_of_the_week_weekly_calendars"],
            "reviewReason": "Integrates time/calendar terms from A1 with public transit schedule reading.",
            "audioSuitability": "standard_speech_synthesis_acceptable", "audioPurpose": "Provide spoken pronunciation of route numbers and schedule captions.",
            "successCriteria": [
                "Locates operating hours (e.g. 06:40 - 22:30) on a Cyrillic route graphic",
                "Determines whether bus route runs straight along Peace Avenue or turns north towards Sansar"
            ],
            "masteryEvidence": "Identifies departure frequency and final evening run from an authentic Ulaanbaatar route diagram.",
            "recommendedExerciseModalities": ["reading_comprehension", "contextual_cloze", "categorization"]
        },
        {
            "lessonId": "les_a2_64_05_bus_stop_inquiries_dialogue",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 5,
            "title": "Which Bus Goes to the Central Post Office? Stop Inquiries",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Develop interactive spoken ability to ask bystanders at a crowded stop which bus reaches a specific destination.",
            "communicativeOutcome": "Ask pedestrians for bus route advice, confirm if a bus goes through Sukhbaatar Square, and signal intent to alight.",
            "objectivesIntroduced": ["obj_a2_64_05_inquire_bus_destinations"],
            "objectivesPracticed": ["obj_a2_64_01_express_transport_instrumental", "obj_a2_64_03_decode_automated_bus_announcements"],
            "objectivesReviewed": ["obj_a1_16_01_greet_time_of_day"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a2_case_instrumental_transport_language"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu", "gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_a1_intonation_questions"], "phonologyReviewed": ["phono_a1_polite_phrasing"],
            "communicativeFunctionsIntroduced": ["comm_a2_17_giving_multistep_directions"],
            "communicativeFunctionsPracticed": ["comm_a2_18_buying_bus_train_tickets"],
            "communicativeFunctionsReviewed": ["comm_a1_19_inquiring_location"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 2, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_domain_transportation_travel", "lex_domain_city_urban_life"],
            "previousVocabularyReused": ["уучлаарай", "энэ", "тийшээ", "хүрэх", "зогсох", "буух"],
            "readingObjective": "",
            "listeningObjective": "Follow a fellow passenger's spoken reply explaining which bus number to take and where to transfer.",
            "writingObjective": "",
            "spokenProductionObjective": "Ask a fellow commuter: 'Уучлаарай, энэ автобус Төв шуудангаар дайрах уу?' and respond appropriately.",
            "registerTarget": "Spontaneous polite public bystander register",
            "pragmaticTarget": "Using polite attention getters ('Уучлаарай, танаас нэг зүйл асууж болох уу?') without being intrusive.",
            "prerequisiteLessonIds": ["les_a2_64_03_transit_announcements_decoding", "les_a2_64_04_route_maps_schedules_reading"],
            "reviewsLessonIds": ["les_a1_19_01_polar_questions_intro"],
            "reviewsUnitIds": ["unit_a1_19_polar_inquiries_polar_question_part"],
            "reviewReason": "Spirals polar question syntax (уу/үү) into real-time transit route inquiries.",
            "audioSuitability": "mongolian_voice_required", "audioPurpose": "Simulate natural conversational pace between two commuters at an outdoor winter bus stop.",
            "successCriteria": [
                "Asks whether a specific bus line passes a landmark using polite particle and instrumental case",
                "Understands bystander's recommendation to wait for another line or transfer at the next stop"
            ],
            "masteryEvidence": "Participates in an unscripted roleplay asking how to reach the Central Post Office from 120 Myangat.",
            "recommendedExerciseModalities": ["dialogue_completion", "role-play response", "listening_comprehension"]
        },
        {
            "lessonId": "les_a2_64_06_transit_card_sms_writing",
            "unitId": uid, "cefrLevel": "A2", "sequenceWithinUnit": 6,
            "title": "Transit SMS: Coordinating Bus Commute Times with a Friend",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Synthesize instrumental case, bus route numbers, and arrival predictions in short personal messaging.",
            "communicativeOutcome": "Compose a brief message informing a friend which bus you boarded and at which stop to meet.",
            "objectivesIntroduced": ["obj_a2_64_06_draft_transit_sms"],
            "objectivesPracticed": ["obj_a2_64_01_express_transport_instrumental", "obj_a2_64_05_inquire_bus_destinations"],
            "objectivesReviewed": ["obj_a1_34_01_tell_clock_time"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a2_case_instrumental_transport_language"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal", "gram_a1_verb_aspect_progressive_j_baina"],
            "phonologyIntroduced": [],
            "phonologyPracticed": [], "phonologyReviewed": ["phono_a1_cyrillic_spelling_rules"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a2_18_buying_bus_train_tickets", "comm_a1_18_scheduling_appointments"],
            "communicativeFunctionsReviewed": ["comm_a1_17_describing_daily_routines"],
            "newProductiveLemmaTarget": 2, "newReceptiveLemmaTarget": 0, "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_domain_transportation_travel", "lex_domain_communication_media"],
            "previousVocabularyReused": ["найз", "уулзах", "зогсоол", "хүлээх", "ирж байна", "минут"],
            "readingObjective": "Read a friend's incoming SMS inquiring about your current bus stop location.",
            "listeningObjective": "",
            "writingObjective": "Write a 3-sentence SMS stating which bus you are on, your current stop, and estimated arrival.",
            "spokenProductionObjective": "",
            "registerTarget": "Casual digital peer messaging",
            "pragmaticTarget": "Using concise digital text conventions while maintaining accurate grammatical case endings.",
            "prerequisiteLessonIds": ["les_a2_64_05_bus_stop_inquiries_dialogue"],
            "reviewsLessonIds": ["les_a1_57_01_progressive_aspect_intro"],
            "reviewsUnitIds": ["unit_a1_57_ongoing_progressive_aspect_verbal_s"],
            "reviewReason": "Combines ongoing progressive aspect (-ж байна) with instrumental transit markings.",
            "audioSuitability": "standard_speech_synthesis_acceptable", "audioPurpose": "Read back written messages for ear training.",
            "successCriteria": [
                "Drafts a coherent text message indicating bus number in instrumental case",
                "Coordinates arrival time with meeting place using locative case correctly"
            ],
            "masteryEvidence": "Writes 'Би 2-р автобусаар явж байна. Их дэлгүүрийн зогсоол дээр 10 минутын дараа уулзъя' without grammatical error.",
            "recommendedExerciseModalities": ["short-answer writing", "sentence construction", "error correction"]
        }
    ])

    return lessons
