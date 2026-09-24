"""
Append Units 40 through 44 to gen_sec03_full.py
"""

code_40_to_44 = '''
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
'''

with open("scripts/framework_builder/gen_sec03_full.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_40_to_44 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec03_full.py", "w") as f:
    f.write(new_cur)

print("gen_sec03_full.py updated through Unit 44 (Section 3 Complete)!")
