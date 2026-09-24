"""
Append Units 31, 32, 33 to gen_sec02.py
"""

code_31_33 = '''
    # =========================================================================
    # UNIT 31: Measure Words & Nominal Counting Classifiers (pos 31)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[31]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_31_01_container_classifiers",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Liquid and Vessel Measures: Аяга, Шил, and Данх",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce measure words for liquids and vessels (аяга 'cup', шил 'bottle', данх 'kettle', хундага 'glass') in quantified noun phrases.",
            "communicativeOutcome": "Order and quantify beverages and liquid items using appropriate container measure words (e.g. 'хоёр аяга цай').",
            "objectivesIntroduced": ["obj_a1_31_01_use_container_measure_words"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "grammarIntroduced": ["gram_a1_classifiers_measure_words"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["цай", "ус", "сүү", "нэг", "хоёр"],
            "readingObjective": "Read café drink menus specifying serving volumes in cups and bottles.",
            "listeningObjective": "Hear the acoustic sequence of [Numeral] + [Classifier] + [Noun] in beverage orders.",
            "writingObjective": "Write 4 beverage orders combining numerals, container words, and drinks.",
            "spokenProductionObjective": "Order two drinks aloud using vessel measure words at a simulated café counter.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Natural and polite phrasing when ordering beverages in hospitality settings.",
            "prerequisiteLessonIds": ["les_a1_30_06_retail_selection_synthesis"],
            "reviewsLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Insert measure words between cardinal numerals and mass nouns.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Rhythmic stress phrasing of three-word classifier noun phrases.",
            "successCriteria": [
                "Place measure word directly after the numeral and before the mass noun (e.g. 'нэг аяга цай').",
                "Leave the quantified mass noun in bare nominative form."
            ],
            "masteryEvidence": [
                "Produces 'гурван шил ус' when shown three water bottles.",
                "Explains why *уснууд is ungrammatical and requires a classifier."
            ],
            "recommendedExerciseModalities": ["phrase_building", "matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_31_02_packaging_portion_classifiers",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Packaging and Portions: Хайрцаг, Уут, and Зүсэм",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce packaging and portion classifiers (хайрцаг 'box', уут 'bag', боодол 'packet', зүсэм 'slice', хэсэг 'piece').",
            "communicativeOutcome": "Quantify packaged foodstuffs, stationery goods, and portions at grocery markets and stores.",
            "objectivesIntroduced": ["obj_a1_31_02_use_packaging_classifiers"],
            "objectivesPracticed": ["obj_a1_31_01_use_container_measure_words"],
            "objectivesReviewed": ["obj_a1_30_01_mark_accusative_definite_objects"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_classifiers_measure_words"],
            "grammarReviewed": ["gram_a1_case_accusative_definite_object"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["талх", "чихэр", "цаас", "үзэг"],
            "readingObjective": "Read grocery receipt items itemizing packaged quantities.",
            "listeningObjective": "Comprehend customer requests for bags and boxes in market speech.",
            "writingObjective": "Write a grocery shopping list containing 4 packaged items with classifiers.",
            "spokenProductionObjective": "State aloud 3 packaged items one needs to purchase at the market.",
            "registerTarget": "Everyday standard commercial",
            "pragmaticTarget": "Clear commercial requests preventing purchase quantity misunderstandings.",
            "prerequisiteLessonIds": ["les_a1_31_01_container_classifiers"],
            "reviewsLessonIds": ["les_a1_30_01_accusative_definite_marking"],
            "reviewsUnitIds": ["unit_a1_30_definite_direct_objects_the_accusat"],
            "reviewReason": "Attach accusative case suffixes to quantified classifier phrases (тэр нэг хайрцаг чихрийг).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronunciation of velar stops and affricates in packaging nouns (хайрцаг, боодол).",
            "successCriteria": [
                "Pair specific items with their culturally standard classifiers (талх -> зүсэм, цай -> хайрцаг).",
                "Construct complete quantified noun phrases without grammatical errors."
            ],
            "masteryEvidence": [
                "Produces 'Нэг уут алим авъя' during shopping drill.",
                "Sorts 8 foodstuffs to their standard containers with zero error."
            ],
            "recommendedExerciseModalities": ["categorization", "shopping_list_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_31_03_ordering_measuring_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Precision Ordering and Measurement",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining numerals, classifiers, accusative objects, and polite request verbs in transactions.",
            "communicativeOutcome": "Place complex retail and canteen orders specifying exact quantities and packaging formats.",
            "objectivesIntroduced": ["obj_a1_31_03_order_measured_goods"],
            "objectivesPracticed": [
                "obj_a1_31_01_use_container_measure_words",
                "obj_a1_31_02_use_packaging_classifiers"
            ],
            "objectivesReviewed": ["obj_a1_27_03_ask_quantity_hed_heden"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_classifiers_measure_words"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["хэдэн", "авах", "өгөх", "үнэ", "төгрөг"],
            "readingObjective": "Read canteen order chits detailing multi-item meals and drinks.",
            "listeningObjective": "Comprehend rapid clerk questions clarifying serving sizes ('Том аяга уу, жижиг аяга уу?').",
            "writingObjective": "Draft a 4-turn transaction script ordering food and drinks with classifiers.",
            "spokenProductionObjective": "Roleplay ordering breakfast at a teahouse specifying portions.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Polite responsiveness to clerk sizing inquiries.",
            "prerequisiteLessonIds": ["les_a1_31_02_packaging_portion_classifiers"],
            "reviewsLessonIds": ["les_a1_27_03_inquiries_with_hed"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Combine quantity question 'хэдэн' with classifiers (Хэдэн аяга цай вэ?).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational rhythm in fast service counters.",
            "successCriteria": [
                "Respond accurately to size inquiries (Жижиг аягаар авъя).",
                "Integrate price inquiries into the order sequence seamlessly."
            ],
            "masteryEvidence": [
                "Executes a 6-turn canteen order without hesitation.",
                "Calculates total cost based on per-unit classifier pricing."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "order_chit_completion", "audio_response_matching"]
        },
        {
            "lessonId": "les_a1_31_04_canteen_menu_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Canteen Price Boards and Recipes",
            "lessonType": "reading_development",
            "primaryPurpose": "Read university canteen menu boards, portion prices, and simple traditional recipe ingredient lists.",
            "communicativeOutcome": "Interpret canteen menus and recipe cards with itemized portion sizes and costs.",
            "objectivesIntroduced": ["obj_a1_31_04_read_menu_boards_and_recipes"],
            "objectivesPracticed": ["obj_a1_31_01_use_container_measure_words"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_classifiers_measure_words"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["хоол", "цай", "үнэ", "порц", "ширхэг"],
            "readingObjective": "Read a 55-word canteen price board with portion sizes and meal combos.",
            "listeningObjective": None,
            "writingObjective": "Extract ingredients and portion quantities for a traditional milk tea recipe.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard commercial",
            "pragmaticTarget": "Budget-conscious menu reading and portion evaluation.",
            "prerequisiteLessonIds": ["les_a1_31_03_ordering_measuring_drills"],
            "reviewsLessonIds": ["les_a1_31_01_container_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_classif"],
            "reviewReason": "Consolidate written recognition of measure words in culinary contexts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading menu items and prices clearly.",
            "successCriteria": [
                "Locate prices for single portions vs full servings accurately.",
                "Identify ingredients listed with measure words in recipe instructions."
            ],
            "masteryEvidence": [
                "Selects the most affordable combo meal meeting specified dietary constraints.",
                "Answers 4 menu comprehension questions with 100% accuracy."
            ],
            "recommendedExerciseModalities": ["menu_scanning", "recipe_matching", "table_completion"]
        },
        {
            "lessonId": "les_a1_31_05_acoustic_classifier_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Rapid Canteen Orders and Quantities",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal orders at bustling university and market food stalls.",
            "communicativeOutcome": "Accurately record multi-item food and beverage orders from rapid spoken speech.",
            "objectivesIntroduced": ["obj_a1_31_05_parse_rapid_canteen_orders"],
            "objectivesPracticed": ["obj_a1_31_01_use_container_measure_words"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_classifiers_measure_words"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["аяга", "шил", "порц", "цай", "хоол"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 customer orders in a noisy canteen and record item counts and measure words.",
            "writingObjective": "Transcribe 5 order tickets from audio input into an order fulfillment log.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Accurate auditory processing under time pressure and background noise.",
            "prerequisiteLessonIds": ["les_a1_31_03_ordering_measuring_drills"],
            "reviewsLessonIds": ["les_a1_31_02_packaging_portion_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_classif"],
            "reviewReason": "Zero-vocabulary listening lab training classifier acoustic discrimination.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic background canteen ambience with overlapping customer voices.",
            "successCriteria": [
                "Accurately transcribe all 5 customer orders without quantity or classifier errors.",
                "Identify customer order modifications from audio ('Нэг аяга биш, хоёр аяга')."
            ],
            "masteryEvidence": [
                "Produces flawless kitchen tickets matching audio recordings.",
                "Calculates bill total accurately based on heard orders."
            ],
            "recommendedExerciseModalities": ["audio_transcription", "order_logging", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_31_06_mid_section_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Milestone Checkpoint: Section 2 Mid-Section Synthesis Audit",
            "lessonType": "checkpoint",
            "primaryPurpose": "Formal formative milestone evaluation assessing cumulative mastery of Units 24-31 (existentials, dative-locative, wh-particles, numerals 1-100, phone numbers, plurals, accusative objects, classifiers).",
            "communicativeOutcome": "Demonstrate integrated communicative competence in locating entities, counting assets, and conducting retail and office transactions.",
            "objectivesIntroduced": [],
            "objectivesPracticed": [
                "obj_a1_24_01_affirm_existence_baina",
                "obj_a1_25_01_apply_dative_locative_suffixes",
                "obj_a1_26_01_select_be_ve_particles",
                "obj_a1_27_01_count_cardinals_1_to_20",
                "obj_a1_28_01_dictate_paired_phone_numbers",
                "obj_a1_29_01_form_regular_plurals_uud",
                "obj_a1_30_01_mark_accusative_definite_objects",
                "obj_a1_31_01_use_container_measure_words"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_existential_baina_baihgui",
                "gram_a1_case_dative_locative_location",
                "gram_a1_content_questions_be_ve",
                "gram_a1_numerals_cardinal_1_100",
                "gram_a1_nominal_plural_uud_nuud",
                "gram_a1_case_accusative_definite_object",
                "gram_a1_classifiers_measure_words"
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
                "comm_a1_12_location_simple_objects",
                "comm_a1_05_asking_identity_origin"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_numbers_time_calendar", "lex_a1_food_dining_beverages"],
            "previousVocabularyReused": ["байна", "байхгүй", "хаана", "хэд", "ном", "цай", "өрөө"],
            "readingObjective": "Read a multi-section civic facility report synthesizing room inventories, occupant contacts, and supply requisitions.",
            "listeningObjective": "Comprehend a 4-part facility briefing covering resource allocation, phone directories, and office locations.",
            "writingObjective": "Complete a comprehensive 6-item facility status audit report applying accurate case suffixes and numbers.",
            "spokenProductionObjective": "Deliver an integrated 60-second oral briefing detailing asset distribution in an office building.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Holistic communicative autonomy in spatial, numerical, and transaction discourse.",
            "prerequisiteLessonIds": [
                "les_a1_31_04_canteen_menu_reading",
                "les_a1_31_05_acoustic_classifier_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_24_06_household_inventory_dialogue",
                "les_a1_25_06_campus_orientation_synthesis",
                "les_a1_26_06_inquiry_dialogue_synthesis",
                "les_a1_27_06_counting_dialogue_synthesis",
                "les_a1_28_05_contact_exchange_roleplay",
                "les_a1_29_06_group_description_synthesis",
                "les_a1_30_06_retail_selection_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_24_existential_assertion_vs_",
                "unit_a1_25_dative_locative_spatial_anchoring_s",
                "unit_a1_26_content_question_particles_and_",
                "unit_a1_27_cardinal_numbers_counting_up_to_one",
                "unit_a1_28_telephone_numbers_digital_contact_e",
                "unit_a1_29_nominal_plurality_suffixes_",
                "unit_a1_30_definite_direct_objects_the_accusat",
                "unit_a1_31_measure_words_nominal_counting_classif"
            ],
            "reviewReason": "Formal milestone evaluation auditing all Section 2 grammatical competencies before proceeding to classroom directives.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Standardized benchmark listening evaluation recordings with native accent diversity.",
            "successCriteria": [
                "Demonstrate integrated mastery across all 8 tested grammatical and functional targets.",
                "Exhibit zero confusion between existential (байна), copular (мөн/биш), and locative (-д/-т) structures."
            ],
            "masteryEvidence": [
                "Successfully completes all 4 performance modalities (reading, listening, writing, oral briefing).",
                "Produces error-free case morphology on unprompted spoken sentences."
            ],
            "recommendedExerciseModalities": ["comprehensive_assessment", "oral_presentation", "dossier_audit"]
        }
    ])

    # =========================================================================
    # UNIT 32: Classroom Discourse & Spatial Instructions (pos 32)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[32]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_32_01_teacher_directives_actions",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Classroom Commands: Сонс, Бич, Унш, and Үз",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce core instructional verbs and teacher directives in bare imperative and courteous hortative forms.",
            "communicativeOutcome": "Understand and respond immediately to standard classroom teacher instructions.",
            "objectivesIntroduced": ["obj_a1_32_01_comprehend_teacher_directives"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_30_01_mark_accusative_definite_objects"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_education_classroom"],
            "previousVocabularyReused": ["дэвтэр", "ном", "самбар", "үзэг"],
            "readingObjective": "Read classroom activity prompts written on blackboard headers.",
            "listeningObjective": "Comprehend teacher directives in fast instructional speech (e.g. 'Номоо нээгээрэй', 'Самбар луу хараарай').",
            "writingObjective": "Write down 4 teacher instructions next to corresponding classroom action icons.",
            "spokenProductionObjective": "Direct a study partner to perform 3 study tasks using instructional verbs.",
            "registerTarget": "Courteous instructional",
            "pragmaticTarget": "Immediate respectful compliance with academic instructions.",
            "prerequisiteLessonIds": ["les_a1_31_06_mid_section_checkpoint"],
            "reviewsLessonIds": ["les_a1_30_01_accusative_definite_marking"],
            "reviewsUnitIds": ["unit_a1_30_definite_direct_objects_the_accusat"],
            "reviewReason": "Combine classroom directives with definite accusative objects (Номыг унш).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Clear teacher voice projection with instructional cadence.",
            "successCriteria": [
                "Respond accurately to directives without physical hesitation.",
                "Identify the target object of the verb from the accusative marker."
            ],
            "masteryEvidence": [
                "Performs the requested action (opens book, writes word, looks at board) upon hearing prompt.",
                "Explains the difference between 'унш' (read!) and 'уншаарай' (please read)."
            ],
            "recommendedExerciseModalities": ["action_response", "icon_matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_32_02_spatial_movement_directives",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Classroom Movement: Энд суу, Тэнд оч, Самбар луу хар",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce spatial directional postposition/particles (руу/рүү, дээр, доор) and movement verbs (суу, зогс, оч, ир).",
            "communicativeOutcome": "Follow and issue spatial movement directives within a classroom or meeting hall.",
            "objectivesIntroduced": ["obj_a1_32_02_follow_spatial_movement_directives"],
            "objectivesPracticed": ["obj_a1_32_01_comprehend_teacher_directives"],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_intro"],
            "phonologyReviewed": ["phono_non_initial_reduction"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom"],
            "previousVocabularyReused": ["энд", "тэнд", "сандал", "ширээ", "үүд"],
            "readingObjective": "Read room seating charts and directional signage inside a lecture hall.",
            "listeningObjective": "Comprehend rapid spatial commands during group seating activities.",
            "writingObjective": "Write 4 directional commands guiding a visitor to a specific desk or seat.",
            "spokenProductionObjective": "Direct a peer where to sit or stand using spatial directional expressions.",
            "registerTarget": "Courteous instructional",
            "pragmaticTarget": "Polite spatial guidance in shared physical learning spaces.",
            "prerequisiteLessonIds": ["les_a1_32_01_teacher_directives_actions"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Differentiate static location (-д/-т суу) from directional motion (руу/рүү хар).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Intonational clarity in spatial movement directives.",
            "successCriteria": [
                "Select 'руу' after back-vowel stems and 'рүү' after front-vowel stems correctly.",
                "Pair directional particles with appropriate movement verbs."
            ],
            "masteryEvidence": [
                "Moves correctly to designated room areas when given oral instructions.",
                "Produces 'Энд суугаарай' with natural hospitality."
            ],
            "recommendedExerciseModalities": ["map_navigation", "movement_simulation", "sentence_ordering"]
        },
        {
            "lessonId": "les_a1_32_03_classroom_rules_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Classroom Rules and Exam Protocols",
            "lessonType": "reading_development",
            "primaryPurpose": "Read and analyze classroom rules, lab protocols, and examination instructions.",
            "communicativeOutcome": "Understand student behavioral expectations, quiet zones, and exam room procedures.",
            "objectivesIntroduced": ["obj_a1_32_03_read_classroom_protocols"],
            "objectivesPracticed": [
                "obj_a1_32_01_comprehend_teacher_directives",
                "obj_a1_32_02_follow_spatial_movement_directives"
            ],
            "objectivesReviewed": ["obj_a1_24_02_negate_existence_baihgui"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_nominal_negation_bish"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_education_classroom"],
            "previousVocabularyReused": ["хичээл", "дүрэм", "утас", "хориотой", "зөвшөөрөгдсөн"],
            "readingObjective": "Read a 55-word classroom code of conduct poster.",
            "listeningObjective": None,
            "writingObjective": "List 3 permitted and 3 prohibited classroom behaviors based on the reading.",
            "spokenProductionObjective": None,
            "registerTarget": "Formal instructional",
            "pragmaticTarget": "Strict adherence to academic integrity and classroom etiquette.",
            "prerequisiteLessonIds": ["les_a1_32_02_spatial_movement_directives"],
            "reviewsLessonIds": ["les_a1_24_02_existential_negation_baihgui"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Recognize prohibited items using existential negation ('Утас хэрэглэхгүй').",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading institutional rules with solemn formal cadence.",
            "successCriteria": [
                "Extract 4 core academic rules from printed poster text.",
                "Identify restrictions regarding mobile phones and food consumption."
            ],
            "masteryEvidence": [
                "Categorizes 6 classroom behaviors into allowed vs disallowed with 100% accuracy.",
                "Answers 3 protocol comprehension questions correctly."
            ],
            "recommendedExerciseModalities": ["document_scanning", "rule_sorting", "true_false"]
        },
        {
            "lessonId": "les_a1_32_04_listening_teacher_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Processing Multi-Step Teacher Instructions",
            "lessonType": "listening_development",
            "primaryPurpose": "Process multi-step spoken instructional sequences in a live classroom setting without pausing.",
            "communicativeOutcome": "Execute complex, connected teacher instructions (e.g. 'Дэвтрээ нээгээд, 5-р дасгалыг бичээрэй').",
            "objectivesIntroduced": ["obj_a1_32_04_process_multi_step_instructions"],
            "objectivesPracticed": ["obj_a1_32_01_comprehend_teacher_directives"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom"],
            "previousVocabularyReused": ["дэвтэр", "ном", "дасгал", "хуудас", "бичих"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 multi-step teacher instructions and arrange task sequences in chronological order.",
            "writingObjective": "Transcribe the key verbs and page numbers heard in the instructions.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard instructional",
            "pragmaticTarget": "Attentive auditory processing in group instructional settings.",
            "prerequisiteLessonIds": ["les_a1_32_02_spatial_movement_directives"],
            "reviewsLessonIds": ["les_a1_32_01_teacher_directives_actions"],
            "reviewsUnitIds": ["unit_a1_32_classroom_discourse_spatial_instructio"],
            "reviewReason": "Zero-vocabulary listening lab training fast auditory processing of verbs.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural classroom teacher voice with natural background acoustic reverberation.",
            "successCriteria": [
                "Accurately sequence all 4 multi-step instructional chains.",
                "Extract page numbers and exercise numbers without error."
            ],
            "masteryEvidence": [
                "Selects the correct page and exercise combination based on audio prompt.",
                "Identifies the chronological order of 3 commanded actions."
            ],
            "recommendedExerciseModalities": ["chronological_sequencing", "audio_transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_32_05_study_session_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Peer Study Group Coordination",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Coordinate a peer study session directing classmates through exercises, page turns, and whiteboard tasks.",
            "communicativeOutcome": "Lead and participate in a study group session using polite academic directives and spatial cues.",
            "objectivesIntroduced": ["obj_a1_32_05_lead_study_group_tasks"],
            "objectivesPracticed": [
                "obj_a1_32_01_comprehend_teacher_directives",
                "obj_a1_32_02_follow_spatial_movement_directives"
            ],
            "objectivesReviewed": ["obj_a1_30_03_request_specific_items_transactionally"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom"],
            "previousVocabularyReused": ["дэвтэр", "ном", "хуудас", "дасгал", "самбар", "үзэх"],
            "readingObjective": "Read study group task assignments detailing exercise numbers.",
            "listeningObjective": "Comprehend study partner's directives regarding which problem to solve.",
            "writingObjective": "Draft a 4-point study plan using clear instructional verbs.",
            "spokenProductionObjective": "Facilitate a 6-turn collaborative study group roleplay.",
            "registerTarget": "Courteous peer educational",
            "pragmaticTarget": "Supportive peer collaboration and polite task sharing.",
            "prerequisiteLessonIds": [
                "les_a1_32_03_classroom_rules_reading",
                "les_a1_32_04_listening_teacher_lab"
            ],
            "reviewsLessonIds": ["les_a1_32_01_teacher_directives_actions"],
            "reviewsUnitIds": ["unit_a1_32_classroom_discourse_spatial_instructio"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 32 classroom language.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic peer study discussion showcasing collaborative turn-taking.",
            "successCriteria": [
                "Use polite hortatives ('-аарай/-ээрэй') when directing peers.",
                "Execute the collaborative study tasks smoothly without reverting to English."
            ],
            "masteryEvidence": [
                "Directs peer to open book to specific page and read dialogue aloud.",
                "Maintains accurate accusative and directional case forms throughout interaction."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "peer_tutoring", "task_simulation"]
        }
    ])

    # =========================================================================
    # UNIT 33: Spatial Inventory Capstone: Office & Studio Space (pos 33)
    # 6 Lessons | Targets: ProdLem=20, RecLem=8, ProdExp=6, RecExp=3
    # Budget: (6,3,2,1), (6,2,2,1), (4,2,1,1), (4,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[33]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_33_01_workplace_studio_inventory",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Workplace Assets: Office and Studio Equipment Lexicon",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce high-frequency workplace, office, and creative studio technology and furnishings.",
            "communicativeOutcome": "Identify and catalog professional equipment, workstations, and creative tools accurately.",
            "objectivesIntroduced": ["obj_a1_33_01_identify_office_studio_assets"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects", "comm_a1_12_location_simple_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["компьютер", "ширээ", "сандал", "цаас", "өрөө"],
            "readingObjective": "Read workplace asset tags and studio equipment labels.",
            "listeningObjective": "Comprehend spoken lists of studio hardware and digital gear.",
            "writingObjective": "Write an inventory list of 6 office equipment items with their condition.",
            "spokenProductionObjective": "State aloud the equipment available in an office or recording studio.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Accurate asset terminology in professional workplaces.",
            "prerequisiteLessonIds": ["les_a1_32_05_study_session_synthesis"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine newly acquired professional assets with existential assertion frames.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear pronunciation of modern technical loanwords in Mongolian speech.",
            "successCriteria": [
                "Identify 6 modern office technologies in Cyrillic script.",
                "Assert presence or absence using 'байна/байхгүй' accurately."
            ],
            "masteryEvidence": [
                "Produces 'Принтер өрөөнд байна' upon seeing an image of a printer.",
                "Sorts 10 asset terms into office vs studio categories."
            ],
            "recommendedExerciseModalities": ["image_labeling", "matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_33_02_spatial_layout_organization",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Facility Layout: Spatial Anchoring of Workplace Equipment",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce complex spatial arrangements, zone divisions, and furniture placement in open-plan offices.",
            "communicativeOutcome": "Explain the exact layout of workstations, meeting rooms, and shared amenities.",
            "objectivesIntroduced": ["obj_a1_33_02_describe_workplace_layout"],
            "objectivesPracticed": ["obj_a1_33_01_identify_office_studio_assets"],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["давхар", "өрөө", "үүд", "булан", "төв"],
            "readingObjective": "Read an architectural floor plan legend and workspace zone map.",
            "listeningObjective": "Comprehend verbal workplace orientation instructions for new employees.",
            "writingObjective": "Write a 4-sentence paragraph describing the layout of an office floor.",
            "spokenProductionObjective": "Describe the location of 3 essential workplace amenities to a new colleague.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Clear spatial orientation facilitating workplace onboarding.",
            "prerequisiteLessonIds": ["les_a1_33_01_workplace_studio_inventory"],
            "reviewsLessonIds": ["les_a1_25_02_locating_people_places"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine workplace equipment with multi-room dative-locative constructions.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Structured descriptive cadence modeling architectural orientation tours.",
            "successCriteria": [
                "Use dative-locative endings (-д/-т) accurately with architectural room zones.",
                "Describe relative positioning clearly using spatial anchor nouns."
            ],
            "masteryEvidence": [
                "Produces 'Уулзалтын өрөө гуравдугаар давхарт байна' flawlessly.",
                "Draws correct equipment placement onto a blank floor plan from verbal description."
            ],
            "recommendedExerciseModalities": ["floor_plan_labeling", "sentence_construction", "matching"]
        },
        {
            "lessonId": "les_a1_33_03_facility_audit_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Master Facility Audit and Asset Register",
            "lessonType": "reading_development",
            "primaryPurpose": "Read and cross-examine a comprehensive multi-room office facility audit, asset tags, and procurement orders.",
            "communicativeOutcome": "Extract complex asset data, detect missing equipment, and verify inventory counts across departments.",
            "objectivesIntroduced": ["obj_a1_33_03_read_facility_audit_dossiers"],
            "objectivesPracticed": [
                "obj_a1_33_01_identify_office_studio_assets",
                "obj_a1_33_02_describe_workplace_layout"
            ],
            "objectivesReviewed": ["obj_a1_27_04_read_inventory_sheets"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100", "gram_a1_nominal_plural_uud_nuud"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["бараа", "тоо", "хэрэгсэл", "нийт", "хянасан"],
            "readingObjective": "Read a 70-word comprehensive facility audit table detailing office furnishings, quantities, and locations.",
            "listeningObjective": None,
            "writingObjective": "Draft a formal asset reconciliation memorandum summarizing 4 verified inventory findings.",
            "spokenProductionObjective": None,
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Rigorous verification and professional documentation in business administration.",
            "prerequisiteLessonIds": ["les_a1_33_02_spatial_layout_organization"],
            "reviewsLessonIds": ["les_a1_27_04_inventory_sheet_reading"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Combine multi-digit numbers with complex office asset nomenclature in reading.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading professional audit reports with formal executive cadence.",
            "successCriteria": [
                "Identify missing equipment items from the comparative audit table.",
                "Calculate total asset counts across 3 separate department wings accurately."
            ],
            "masteryEvidence": [
                "Answers 5 complex factual audit questions with 100% accuracy.",
                "Drafts written memo with zero grammatical errors in case or number marking."
            ],
            "recommendedExerciseModalities": ["document_scanning", "audit_reconciliation", "memorandum_drafting"]
        },
        {
            "lessonId": "les_a1_33_04_relocation_logistics_listening",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Equipment Relocation Directives and Logistics",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal logistics directives regarding the movement, installation, and storage of workplace assets.",
            "communicativeOutcome": "Accurately decipher relocation instructions specifying which item goes to which room and floor.",
            "objectivesIntroduced": ["obj_a1_33_04_parse_relocation_directives"],
            "objectivesPracticed": ["obj_a1_33_01_identify_office_studio_assets"],
            "objectivesReviewed": ["obj_a1_30_05_detect_accusative_in_retail_speech"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["зөөх", "тавих", "өрөө", "давхар", "ширээ"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 verbal relocation directives and map each asset to its new room destination.",
            "writingObjective": "Transcribe the asset names, source rooms, and destination rooms into a moving log.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard workplace",
            "pragmaticTarget": "Executing logistical transfers accurately without physical misplacement.",
            "prerequisiteLessonIds": ["les_a1_33_02_spatial_layout_organization"],
            "reviewsLessonIds": ["les_a1_30_05_accusative_listening_lab"],
            "reviewsUnitIds": ["unit_a1_30_definite_direct_objects_the_accusat"],
            "reviewReason": "Hear definite accusative marking combined with dative-locative destinations (Энэ ширээг 302 тоотод тавь).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic busy workplace logistics audio with natural conversational urgency.",
            "successCriteria": [
                "Map 4 out of 4 moved items to their correct target rooms from audio alone.",
                "Distinguish between source location and destination location accurately."
            ],
            "masteryEvidence": [
                "Completes relocation logistics matrix with zero errors.",
                "Accurately transcribes heard case markers on audio moving directives."
            ],
            "recommendedExerciseModalities": ["audio_mapping", "logistics_table_completion", "matching"]
        },
        {
            "lessonId": "les_a1_33_05_office_planning_simulation",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Collaborative Office Layout Planning",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Collaborate with a colleague to design and furnish a new office studio from an empty blueprint.",
            "communicativeOutcome": "Negotiate furniture choices, determine room placements, and calculate asset budgets collaboratively.",
            "objectivesIntroduced": ["obj_a1_33_05_negotiate_office_layout"],
            "objectivesPracticed": [
                "obj_a1_33_01_identify_office_studio_assets",
                "obj_a1_33_02_describe_workplace_layout"
            ],
            "objectivesReviewed": ["obj_a1_27_06_conduct_stocktake_dialogue"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_accusative_definite_object"],
            "grammarReviewed": [
                "gram_a1_case_dative_locative_location",
                "gram_a1_existential_baina_baihgui",
                "gram_a1_numerals_cardinal_1_100"
            ],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects", "comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["ширээ", "сандал", "компьютер", "үнэ", "хэд", "энд", "тэнд"],
            "readingObjective": "Read space dimensions and furniture budget constraint sheets.",
            "listeningObjective": "Comprehend partner proposals regarding equipment placement.",
            "writingObjective": "Produce a finalized 5-item layout proposal listing equipment, locations, and costs.",
            "spokenProductionObjective": "Execute an 8-turn negotiation planning the optimal arrangement of an office floor.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Diplomatic suggestions and constructive compromise during collaborative planning.",
            "prerequisiteLessonIds": [
                "les_a1_33_03_facility_audit_reading",
                "les_a1_33_04_relocation_logistics_listening"
            ],
            "reviewsLessonIds": ["les_a1_33_02_spatial_layout_organization"],
            "reviewsUnitIds": ["unit_a1_33_spatial_inventory_capstone_office_stu"],
            "reviewReason": "Zero-vocabulary interactive preparation for Section 2 Capstone Evaluation.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary professional negotiation showcasing natural proposal formulas.",
            "successCriteria": [
                "Propose equipment placements using dative-locative and directional cases fluently.",
                "Reach complete agreement on the layout within the allocated budget."
            ],
            "masteryEvidence": [
                "Completes interactive roleplay maintaining professional register throughout.",
                "Produces a finalized blueprint plan reflecting both partners' negotiated inputs."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "collaborative_design", "budget_reconciliation"]
        },
        {
            "lessonId": "les_a1_33_06_section_02_capstone_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Section 2 Capstone: Comprehensive Spatial and Inventory Benchmark Evaluation",
            "lessonType": "checkpoint",
            "primaryPurpose": "Authoritative summative milestone assessment evaluating all Section 2 competencies across Units 24 through 33.",
            "communicativeOutcome": "Demonstrate complete autonomous proficiency in describing space, existential states, counting to 100, executing retail/canteen transactions, following directives, and managing workplace assets.",
            "objectivesIntroduced": [],
            "objectivesPracticed": [
                "obj_a1_24_01_affirm_existence_baina",
                "obj_a1_25_01_apply_dative_locative_suffixes",
                "obj_a1_26_01_select_be_ve_particles",
                "obj_a1_27_01_count_cardinals_1_to_20",
                "obj_a1_28_01_dictate_paired_phone_numbers",
                "obj_a1_29_01_form_regular_plurals_uud",
                "obj_a1_30_01_mark_accusative_definite_objects",
                "obj_a1_31_01_use_container_measure_words",
                "obj_a1_32_01_comprehend_teacher_directives",
                "obj_a1_33_01_identify_office_studio_assets"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_existential_baina_baihgui",
                "gram_a1_case_dative_locative_location",
                "gram_a1_content_questions_be_ve",
                "gram_a1_numerals_cardinal_1_100",
                "gram_a1_nominal_plural_uud_nuud",
                "gram_a1_case_accusative_definite_object",
                "gram_a1_classifiers_measure_words"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [],
            "phonologyPracticed": [
                "phono_vowel_harmony_suffixes",
                "phono_stress_initial_and_full_vowels",
                "phono_non_initial_reduction",
                "phono_soft_and_hard_signs"
            ],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_10_identifying_objects",
                "comm_a1_11_counting_simple_quantities",
                "comm_a1_12_location_simple_objects",
                "comm_a1_05_asking_identity_origin"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_numbers_time_calendar", "lex_a1_professions_workplace"],
            "previousVocabularyReused": ["байна", "байхгүй", "хаана", "хэд", "ном", "өрөө", "давхар"],
            "readingObjective": "Read a comprehensive 80-word workplace relocation and asset audit report.",
            "listeningObjective": "Comprehend a multi-speaker workplace orientation and inventory reconciliation briefing.",
            "writingObjective": "Compose an integrated 8-sentence facility audit certifying asset status, contact details, and locations.",
            "spokenProductionObjective": "Deliver a formal 2-minute oral presentation presenting a complete workplace layout audit.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Complete communicative self-sufficiency across all Section 2 domains.",
            "prerequisiteLessonIds": [
                "les_a1_33_03_facility_audit_reading",
                "les_a1_33_05_office_planning_simulation"
            ],
            "reviewsLessonIds": [
                "les_a1_31_06_mid_section_checkpoint",
                "les_a1_32_05_study_session_synthesis",
                "les_a1_33_02_spatial_layout_organization"
            ],
            "reviewsUnitIds": [
                "unit_a1_24_existential_assertion_vs_",
                "unit_a1_25_dative_locative_spatial_anchoring_s",
                "unit_a1_26_content_question_particles_and_",
                "unit_a1_27_cardinal_numbers_counting_up_to_one",
                "unit_a1_28_telephone_numbers_digital_contact_e",
                "unit_a1_29_nominal_plurality_suffixes_",
                "unit_a1_30_definite_direct_objects_the_accusat",
                "unit_a1_31_measure_words_nominal_counting_classif",
                "unit_a1_32_classroom_discourse_spatial_instructio",
                "unit_a1_33_spatial_inventory_capstone_office_stu"
            ],
            "reviewReason": "Formal milestone capstone evaluation certifying Section 2 mastery before advancing to Section 3 temporality.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Standardized benchmark assessment recordings with high-fidelity studio acoustic standards.",
            "successCriteria": [
                "Achieve verified mastery across all Section 2 linguistic and communicative benchmarks.",
                "Exhibit accurate case marking (dative-locative, accusative), number concordance, and question formation."
            ],
            "masteryEvidence": [
                "Completes all four multi-skill assessment sections without pedagogical deficiencies.",
                "Produces spontaneous, fluent oral responses to unscripted administrative inquiries."
            ],
            "recommendedExerciseModalities": ["comprehensive_assessment", "capstone_presentation", "portfolio_evaluation"]
        }
    ])
'''

with open("scripts/framework_builder/gen_sec02.py", "r") as f:
    current = f.read()

# Replace return lessons with appending code_31_33 and returning lessons
if "return lessons" in current:
    parts = current.rsplit("return lessons", 1)
    new_content = parts[0] + code_31_33 + "\n    return lessons\n"
    with open("scripts/framework_builder/gen_sec02.py", "w") as f:
        f.write(new_content)
    print("gen_sec02.py successfully updated with Units 31-33!")
else:
    print("Could not find 'return lessons' in gen_sec02.py")
