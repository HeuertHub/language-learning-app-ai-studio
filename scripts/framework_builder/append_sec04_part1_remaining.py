"""
Append Units 46, 47, 48 to gen_sec04_part1.py
"""

code_46_to_48 = '''
    # =========================================================================
    # UNIT 46: Beverages, Tea & Traditional Dairy Offerings (pos 46)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[46]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_46_01_dairy_products_and_tea_culture",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "White Foods: Сүүтэй Цай, Ааруул, and Тараг",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce traditional dairy offerings (цагаан идээ): ааруул (curds), өрөм (clotted cream), тараг (yogurt), аарц (sour curd), and Mongolian salted milk tea (сүүтэй цай).",
            "communicativeOutcome": "Identify, name, and describe staple Mongolian dairy foods and tea varieties.",
            "objectivesIntroduced": ["obj_a1_46_01_identify_dairy_and_tea"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_45_01_describe_food_attributively"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_sov_word_order"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_food_dining", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["цай", "сүү", "чихэр", "амттай", "уух"],
            "readingObjective": "Read illustrated culinary guides introducing Mongolian white foods (цагаан идээ).",
            "listeningObjective": "Hear hosts offering diverse varieties of tea and dried curds to visitors.",
            "writingObjective": "Write 4 sentences describing different dairy foods and their tastes (исгэлэн, чихэрлэг, зөөлөн).",
            "spokenProductionObjective": "Describe what aaruul and orom taste like to a foreign guest.",
            "registerTarget": "Everyday standard cultural",
            "pragmaticTarget": "Appreciating and explaining traditional nomadic hospitality foodways.",
            "prerequisiteLessonIds": ["les_a1_45_06_canteen_lunch_dining_synthesis"],
            "reviewsLessonIds": ["les_a1_45_01_mongolian_menu_and_attributive_adjectives"],
            "reviewsUnitIds": ["unit_a1_45_traditional_cuisine_restaurant_order"],
            "reviewReason": "Use attributive adjectives to modify traditional dairy nouns.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm cultural tone reading descriptions of nomadic dairy foods.",
            "successCriteria": [
                "Name 4 core varieties of Mongolian dairy products accurately.",
                "Describe tastes using appropriate sensory adjectives."
            ],
            "masteryEvidence": [
                "Matches 5 dairy product terms to their descriptions without error.",
                "Produces 'Сүүтэй цай бол Монголын уламжлалт ундаа' smoothly."
            ],
            "recommendedExerciseModalities": ["visual_matching", "sensory_classification", "cued_production"]
        },
        {
            "lessonId": "les_a1_46_02_beverage_preferences_and_tea_service",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Beverage Options: Цай, Кофе, and Hospitality Offers",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce modern beverage vocabulary (хар цай 'black tea', ногоон цай 'green tea', кофе, жүүс, хийжүүлсэн ундаа) and polite tea offering phrases ('Та цай уух уу?').",
            "communicativeOutcome": "Offer beverages to guests, ask for preferred drinks, and accept or decline politely.",
            "objectivesIntroduced": ["obj_a1_46_02_offer_and_request_beverages"],
            "objectivesPracticed": ["obj_a1_46_01_identify_dairy_and_tea"],
            "objectivesReviewed": ["obj_a1_37_02_express_likes_dislikes_with_infinitive"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_dictionary_infinitive_kh"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining"],
            "previousVocabularyReused": ["цай", "уух", "дуртай", "халуун", "хүйтэн"],
            "readingObjective": "Read beverage menu cards in modern Ulaanbaatar coffee houses and tea rooms.",
            "listeningObjective": "Comprehend hosts asking guests how they take their tea or coffee.",
            "writingObjective": "Draft a short 3-sentence note expressing drink preferences (e.g. 'Би элсэн чихэргүй хар кофе уудаг').",
            "spokenProductionObjective": "Offer tea to a guest and respond politely to an offer.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Gracious host and guest etiquette during tea service.",
            "prerequisiteLessonIds": ["les_a1_46_01_dairy_products_and_tea_culture"],
            "reviewsLessonIds": ["les_a1_37_02_infinitive_complementation_duriatai"],
            "reviewsUnitIds": ["unit_a1_37_verbal_dictionary_infinitive_suffix_"],
            "reviewReason": "Express beverage preferences using -х дуртай.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm welcoming host intonation when offering refreshments.",
            "successCriteria": [
                "Ask 'Та ямар цай уух вэ?' with polite intonation.",
                "Accept refreshments with 'Баярлалаа' and decline politely if necessary."
            ],
            "masteryEvidence": [
                "Executes a fluid 4-turn beverage offering dialogue.",
                "Specifies sugar or milk additions accurately in Mongolian."
            ],
            "recommendedExerciseModalities": ["beverage_selection", "dialogue_roleplay", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_46_03_dairy_market_stall_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Dairy Stalls at Naran Tuul and Bars Market",
            "lessonType": "reading_development",
            "primaryPurpose": "Read market signage and price placards at open-air food markets advertising artisanal countryside dairy products (Архангайн ааруул, Булганы айраг).",
            "communicativeOutcome": "Identify provincial origin, freshness markers, and prices per kilogram from market dairy signs.",
            "objectivesIntroduced": ["obj_a1_46_03_read_dairy_market_signs"],
            "objectivesPracticed": [
                "obj_a1_46_01_identify_dairy_and_tea",
                "obj_a1_46_02_offer_and_request_beverages"
            ],
            "objectivesReviewed": ["obj_a1_40_01_form_ablative_origin"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_ablative_origin"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_food_dining", "lex_a1_shopping_services"],
            "previousVocabularyReused": ["ааруул", "айраг", "үнэ", "килограмм", "аймаг"],
            "readingObjective": "Read a 60-word price and origin board at a traditional dairy market pavilion.",
            "listeningObjective": None,
            "writingObjective": "Transcribe product name, provincial origin, and price per kg for 3 dairy offerings.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard transactional",
            "pragmaticTarget": "Recognizing authentic artisanal provenance in food procurement.",
            "prerequisiteLessonIds": ["les_a1_46_02_beverage_preferences_and_tea_service"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Read provincial origin markings with genitive/ablative on food placards.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading market stall product listings clearly.",
            "successCriteria": [
                "Identify which province each dairy product originates from.",
                "Extract price per kilogram accurately from text."
            ],
            "masteryEvidence": [
                "Answers 4 market reading comprehension questions with 100% accuracy.",
                "Selects the authentic Arkhangai aaruul based on placard description."
            ],
            "recommendedExerciseModalities": ["market_placard_reading", "price_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_46_04_tea_table_hospitality_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Parsing Hospitality Offers in a Ger Setting",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse natural spoken audio recorded in a ger or home setting where hosts invite guests to drink tea and sample curds.",
            "communicativeOutcome": "Accurately understand hospitable invitations, tea refills, and food offerings from conversational audio.",
            "objectivesIntroduced": ["obj_a1_46_04_parse_hospitality_offers"],
            "objectivesPracticed": ["obj_a1_46_01_identify_dairy_and_tea"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["цай", "уу", "ид", "сайхан", "баярлалаа"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 hospitality audio clips and identify what beverage or food item is being offered in each.",
            "writingObjective": "Transcribe the polite offering phrases heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard hospitable",
            "pragmaticTarget": "Auditory recognition of warm traditional hospitality formulas.",
            "prerequisiteLessonIds": ["les_a1_46_02_beverage_preferences_and_tea_service"],
            "reviewsLessonIds": ["les_a1_46_01_dairy_products_and_tea_culture"],
            "reviewsUnitIds": ["unit_a1_46_beverages_tea_traditional_dairy_off"],
            "reviewReason": "Zero-vocabulary auditory lab training hospitality speech perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic domestic audio with pouring tea sounds and warm hospitable prosody.",
            "successCriteria": [
                "Map 4 audio offerings to their corresponding food/drink items accurately.",
                "Identify when a host offers a refill ('Дахиад цай авах уу?')."
            ],
            "masteryEvidence": [
                "Scores 100% on the tea table hospitality listening test.",
                "Identifies polite acceptance phrases used by guests in the clips."
            ],
            "recommendedExerciseModalities": ["audio_offering_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_46_05_tea_and_hospitality_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Welcoming a Guest with Tea and White Foods",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate welcoming a guest into a home or ger: greeting, serving hot milk tea, presenting a plate of aaruul and orom, and engaging in polite small talk.",
            "communicativeOutcome": "Conduct a fluid, culturally authentic hospitality dialogue demonstrating traditional guest etiquette.",
            "objectivesIntroduced": ["obj_a1_46_05_host_guest_tea_service"],
            "objectivesPracticed": [
                "obj_a1_46_01_identify_dairy_and_tea",
                "obj_a1_46_02_offer_and_request_beverages"
            ],
            "objectivesReviewed": ["obj_a1_45_06_execute_canteen_dining"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_food_dining", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["тавтай морил", "цай", "ааруул", "амсах", "баярлалаа"],
            "readingObjective": "Read cultural etiquette prompt cards for host and guest roles.",
            "listeningObjective": "Comprehend partner's polite inquiries and compliments on the tea.",
            "writingObjective": "Draft a short 3-line thank-you note praising a host's hospitality and delicious tea.",
            "spokenProductionObjective": "Execute an 8-turn hospitality dialogue welcoming a guest and serving refreshments.",
            "registerTarget": "Courteous standard cultural",
            "pragmaticTarget": "Authentic demonstration of Mongolian hospitality values and manners.",
            "prerequisiteLessonIds": [
                "les_a1_46_03_dairy_market_stall_reading",
                "les_a1_46_04_tea_table_hospitality_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_46_01_dairy_products_and_tea_culture"],
            "reviewsUnitIds": ["unit_a1_46_beverages_tea_traditional_dairy_off"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 46 hospitality skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary cultural dialogue illustrating genuine Mongolian hospitality etiquette.",
            "successCriteria": [
                "Offer tea using respectful honorific/courteous phrasing ('Цайгаа ууна уу').",
                "Receive food and tea using both hands or right hand supported at elbow."
            ],
            "masteryEvidence": [
                "Completes roleplay smoothly with authentic cultural gestures.",
                "Both partners demonstrate flawless guest-host interactive etiquette."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "cultural_simulation", "etiquette_audit"]
        }
    ])

    # =========================================================================
    # UNIT 47: Comitative Case: Suffixes -тай/-тэй/-той (pos 47)
    # 6 Lessons | Targets: ProdLem=19, RecLem=7, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,2,1,1), (4,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[47]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_47_01_comitative_accompaniment",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Doing Things Together: The Comitative Case -тай/-тэй/-той",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the comitative case suffix -тай/-тэй/-той denoting accompaniment ('with someone') and vowel harmony rules governing allomorph selection.",
            "communicativeOutcome": "State whom one goes with, studies with, or lives with using the comitative case (e.g. 'Би найзтайгаа хамт явлаа').",
            "objectivesIntroduced": ["obj_a1_47_01_form_comitative_accompaniment"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_41_01_form_witnessed_past_laa"],
            "grammarIntroduced": ["gram_a1_case_comitative_accompaniment"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReinforced": ["gram_a1_verb_tense_past_witnessed_laa"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_03_introduce_peer_third_party"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["найз", "хамт", "явах", "уулзах", "багш"],
            "readingObjective": "Read social plans describing group outings and shared activities.",
            "listeningObjective": "Hear the three vowel harmonic allomorphs (-тай/-тэй/-той) in spoken social sentences.",
            "writingObjective": "Attach the comitative case suffix to 6 kinship and peer nouns following vowel harmony.",
            "spokenProductionObjective": "State aloud whom you are going to the cinema or library with.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear communication of companionship and social partnership.",
            "prerequisiteLessonIds": ["les_a1_46_05_tea_and_hospitality_synthesis"],
            "reviewsLessonIds": ["les_a1_41_01_witnessed_past_laa_allomorphs"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Combine comitative companions with witnessed past action verbs.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear vowel diphthong /ai/, /ei/, /oi/ articulation in comitative suffixes.",
            "successCriteria": [
                "Select -тай for back unrounded stems, -тэй for front stems, -той for back rounded stems.",
                "Pair comitative nouns naturally with adverb 'хамт' (together)."
            ],
            "masteryEvidence": [
                "Conjugates найз -> найзтай, дүү -> дүүтэй, ах -> ахтай accurately.",
                "Answers 'Та хэнтэй хамт явсан бэ?' fluently using comitative."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_construction", "cued_production"]
        },
        {
            "lessonId": "les_a1_47_02_comitative_predicative_possession",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Having and Possessing: Predicates with -тай байна",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the predicative possessive construction: [Noun]-тай байна (to have / possess something) and its negative [Noun]-гүй байна (not to have / lack).",
            "communicativeOutcome": "Express possession of tangible objects, family members, pets, and attributes (e.g. 'Би машинтал байна', 'Би ахтай').",
            "objectivesIntroduced": ["obj_a1_47_02_express_possession_with_comitative"],
            "objectivesPracticed": ["obj_a1_47_01_form_comitative_accompaniment"],
            "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": ["gram_a1_case_comitative_possession_predicates"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life", "lex_a1_personal_possessions"],
            "previousVocabularyReused": ["машин", "ном", "мөнгө", "байх", "байхгүй"],
            "readingObjective": "Read personal profiles listing possessions, family relations, and skills.",
            "listeningObjective": "Comprehend speakers stating whether they have specific items or family members.",
            "writingObjective": "Write 4 sentences contrasting things one possesses (-тай) with things one lacks (-гүй).",
            "spokenProductionObjective": "State aloud 3 things you have in your bag and 1 thing you do not have.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear inventory and attribute reporting in personal introductions.",
            "prerequisiteLessonIds": ["les_a1_47_01_comitative_accompaniment"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Synthesize existential copula 'байна' with comitative noun forms to express 'to have'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural prosody linking comitative nouns with existential verbs.",
            "successCriteria": [
                "Formulate 'Би [X]-тай' to state possession of family or permanent traits.",
                "Formulate 'Би [X]-тай байна' to state possession of temporary or portable items."
            ],
            "masteryEvidence": [
                "Produces 'Би нэг эгчтэй, хоёр дүүтэй' smoothly.",
                "Differentiates possession (-тай байна) from location (-д байна)."
            ],
            "recommendedExerciseModalities": ["possession_drills", "bag_inventory", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_47_03_comitative_food_ingredients_and_flavors",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Food Ingredients with -тай and -гүй",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate using -тай (with) and -гүй (without) to specify food ingredients, toppings, and dietary preferences (махтай хуушуур, ногоотой шөл, сонгиногүй).",
            "communicativeOutcome": "Specify exact dish preparations, ingredient inclusions, and dietary omissions when ordering food.",
            "objectivesIntroduced": ["obj_a1_47_03_specify_food_ingredients_comitative"],
            "objectivesPracticed": [
                "obj_a1_47_01_form_comitative_accompaniment",
                "obj_a1_47_02_express_possession_with_comitative"
            ],
            "objectivesReviewed": ["obj_a1_45_02_order_food_at_counter"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates"
            ],
            "grammarReviewed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReinforced": ["gram_a1_noun_phrase_attributive_adjective"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_food_dining"],
            "previousVocabularyReused": ["мах", "ногоо", "давс", "сонгино", "элсэн чихэр"],
            "readingObjective": "Read custom order forms and dietary menu labels.",
            "listeningObjective": "Comprehend diners requesting food adjustments and ingredient exclusions.",
            "writingObjective": "Write 4 custom dish orders specifying desired ingredients (-тай) and excluded items (-гүй).",
            "spokenProductionObjective": "Order a milk tea with low salt and khuushuur without onions.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Precise dietary self-advocacy preventing food allergies or unwelcome ingredients.",
            "prerequisiteLessonIds": ["les_a1_47_02_comitative_predicative_possession"],
            "reviewsLessonIds": ["les_a1_45_02_ordering_at_the_counter_avya"],
            "reviewsUnitIds": ["unit_a1_45_traditional_cuisine_restaurant_order"],
            "reviewReason": "Combine counter ordering formulas with comitative ingredient descriptors.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural diner-waiter dialogue clarifying ingredient modifications.",
            "successCriteria": [
                "Use -тай for inclusions (сүүтэй, чихэртэй, махтай) and -гүй for exclusions (давсгүй, сонгиногүй).",
                "Formulate questions using '... -тай юу?' to check ingredients."
            ],
            "masteryEvidence": [
                "Orders 'Сонгиногүй, ногоотой хуушуур авъя' upon prompt.",
                "Identifies vegetarian dishes on a menu from comitative descriptors."
            ],
            "recommendedExerciseModalities": ["menu_customization", "dietary_roleplay", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_47_04_social_outing_profiles_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Social Outing Profiles and Travel Companions",
            "lessonType": "reading_development",
            "primaryPurpose": "Read social media travel blurbs, photo captions, and weekend trip blogs describing outings with friends, family, and colleagues.",
            "communicativeOutcome": "Extract companionship networks, travel destinations, and shared equipment from social travel texts.",
            "objectivesIntroduced": ["obj_a1_47_04_read_social_outing_texts"],
            "objectivesPracticed": [
                "obj_a1_47_01_form_comitative_accompaniment",
                "obj_a1_47_02_express_possession_with_comitative"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates"
            ],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life", "lex_a1_travel_transport"],
            "previousVocabularyReused": ["найз", "хамт", "уул", "майхан", "аялал"],
            "readingObjective": "Read a 60-word social blog entry recounting a weekend camping trip to Terelj National Park.",
            "listeningObjective": None,
            "writingObjective": "List 3 companions and 4 items of gear mentioned in the camping narrative.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard friendly informal",
            "pragmaticTarget": "Comprehending group social dynamics and travel narratives in reading.",
            "prerequisiteLessonIds": ["les_a1_47_03_comitative_food_ingredients_and_flavors"],
            "reviewsLessonIds": ["les_a1_47_01_comitative_accompaniment"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Consolidate written recognition of comitative accompaniment in narrative text.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Lively friendly narration reading social travel blogs.",
            "successCriteria": [
                "Identify who traveled with whom from comitative suffix markings.",
                "Extract equipment possessed by the camping group."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Maps out the social network of the traveling party correctly."
            ],
            "recommendedExerciseModalities": ["text_scanning", "companion_mapping", "short_answer"]
        },
        {
            "lessonId": "les_a1_47_05_companion_inquiries_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Companionship and Possession in Casual Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal discussions where speakers discuss whom they went with and what gear or resources they brought.",
            "communicativeOutcome": "Accurately record companion names and possessed items from fast spoken dialogue.",
            "objectivesIntroduced": ["obj_a1_47_05_parse_spoken_companionship"],
            "objectivesPracticed": ["obj_a1_47_01_form_comitative_accompaniment"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["хэнтэй", "хамт", "юутай", "явах", "уулзах"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 conversational audio clips and record the companion and key possessed item for each speaker.",
            "writingObjective": "Transcribe the comitative noun forms heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory precision detecting comitative suffixes in rapid connected speech.",
            "prerequisiteLessonIds": ["les_a1_47_03_comitative_food_ingredients_and_flavors"],
            "reviewsLessonIds": ["les_a1_47_02_comitative_predicative_possession"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Zero-vocabulary auditory lab solidifying comitative acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio featuring varied colloquial pacing.",
            "successCriteria": [
                "Map 4 speakers to their stated companions accurately.",
                "Differentiate between -тай (with) and -д (at/in) in acoustic stream."
            ],
            "masteryEvidence": [
                "Scores 100% on the companionship listening test.",
                "Transcribes all heard comitative nouns with correct vowel harmony."
            ],
            "recommendedExerciseModalities": ["audio_companion_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_47_06_picnic_planning_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Planning a Group Picnic and Supplies",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate planning a group weekend picnic with friends: deciding who to invite, who will bring which food/supplies, and checking dietary restrictions.",
            "communicativeOutcome": "Conduct a collaborative social planning dialogue negotiating companions, shared possessions, and food ingredients.",
            "objectivesIntroduced": ["obj_a1_47_06_plan_group_social_event"],
            "objectivesPracticed": [
                "obj_a1_47_01_form_comitative_accompaniment",
                "obj_a1_47_02_express_possession_with_comitative",
                "obj_a1_47_03_specify_food_ingredients_comitative"
            ],
            "objectivesReviewed": ["obj_a1_41_06_weekend_debrief_synthesis"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_comitative_accompaniment",
                "gram_a1_case_comitative_possession_predicates"
            ],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life", "lex_a1_food_dining"],
            "previousVocabularyReused": ["найз", "хамт", "хоол", "унд", "авах", "явах"],
            "readingObjective": "Read simulated friend availability cards and gear inventories.",
            "listeningObjective": "Comprehend partner proposals regarding who to invite and who has a car.",
            "writingObjective": "Draft a finalized picnic checklist detailing who is coming, who has which gear, and what food to buy.",
            "spokenProductionObjective": "Execute an 8-turn conversation organizing a weekend group picnic.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Enthusiastic and well-coordinated social event planning.",
            "prerequisiteLessonIds": [
                "les_a1_47_04_social_outing_profiles_reading",
                "les_a1_47_05_companion_inquiries_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_47_03_comitative_food_ingredients_and_flavors"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 47 comitative skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating enthusiastic peer picnic planning.",
            "successCriteria": [
                "Propose companions using comitative accompaniment fluently ('Доржтой хамт явъя').",
                "Confirm gear possession using 'Чамд майхан байна уу?'."
            ],
            "masteryEvidence": [
                "Completes picnic planning dialogue without grammatical errors.",
                "Produces a comprehensive written picnic plan listing all required items and people."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "event_coordination", "checklist_creation"]
        }
    ])

    # =========================================================================
    # UNIT 48: Volitional Intention: Suffixes -я/-е/-ё (pos 48)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[48]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_48_01_volitional_ya_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Let's Do It: The Volitional Mood -я/-е/-ё/-ье",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the first-person volitional / cohortative suffix -я/-е/-ё/-ье expressing intention ('I will / let me') and collective suggestion ('let's...').",
            "communicativeOutcome": "Express immediate intention and propose shared collective actions (e.g. 'Явъя!' - Let's go!, 'Хоол идье' - Let's eat).",
            "objectivesIntroduced": ["obj_a1_48_01_form_volitional_ya"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_47_01_form_comitative_accompaniment"],
            "grammarIntroduced": ["gram_a1_verb_volitional_intention_ya"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_comitative_accompaniment"],
            "grammarReinforced": ["gram_a1_case_comitative_accompaniment"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["явах", "идэх", "уух", "уулзах", "үзэх"],
            "readingObjective": "Read text messages proposing spontaneous outings and shared meals.",
            "listeningObjective": "Hear the four vowel harmonic allomorphs (-я/-е/-ё/-ье) in spoken invitations and departure calls.",
            "writingObjective": "Attach the volitional suffix to 6 verb stems following Cyrillic hard/soft sign rules.",
            "spokenProductionObjective": "Propose an immediate action to a partner aloud ('Кино үзье!', 'Цай ууя').",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Enthusiastic and socially inviting initiative in peer interactions.",
            "prerequisiteLessonIds": ["les_a1_47_06_picnic_planning_synthesis"],
            "reviewsLessonIds": ["les_a1_47_01_comitative_accompaniment"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Combine volitional proposals with comitative companionship ('Хоёулаа хамт явъя').",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Upbeat enthusiastic intonation characteristic of peer suggestions.",
            "successCriteria": [
                "Select -я for back unrounded stems, -е for front stems, -ё for back rounded stems.",
                "Insert hard sign (ъ) before -я/-ё and soft sign (ь) before -е after consonant finals."
            ],
            "masteryEvidence": [
                "Conjugates явах -> явъя, идэх -> идье, уулзах -> уулзъя, үзэх -> үзье with 100% orthographic accuracy.",
                "Responds affirmatively to an invitation using 'Тэгье!' (Let's do that!)."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "invitation_matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_48_02_social_invitations_and_tegye",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Accepting and Declining: Тэгье, За, and Polite Alternatives",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce conventional responses to volitional proposals: 'Тэгье тэгье' (Sure! Let's do that), 'Тэгье л дээ', 'За тэгье', and polite expressions for postponing ('Өөр өдөр тэгэх үү?').",
            "communicativeOutcome": "Enthusiastically accept social invitations or propose polite alternatives without causing offense.",
            "objectivesIntroduced": ["obj_a1_48_02_respond_to_social_proposals"],
            "objectivesPracticed": ["obj_a1_48_01_form_volitional_ya"],
            "objectivesReviewed": ["obj_a1_35_01_identify_weekdays"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar"],
            "grammarReinforced": ["gram_a1_telling_time_clock_calendar"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["за", "өдөр", "маргааш", "завтай", "уулзах"],
            "readingObjective": "Read instant message exchanges arranging coffee dates and cinema outings.",
            "listeningObjective": "Comprehend friends proposing activities and negotiating alternative days.",
            "writingObjective": "Draft 3 invitation acceptance messages and 1 polite postponement message.",
            "spokenProductionObjective": "Accept an invitation enthusiastically and suggest an exact meeting time.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Social graciousness and agile conversational negotiation.",
            "prerequisiteLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsLessonIds": ["les_a1_35_01_weekdays_tibetan_and_numerical"],
            "reviewsUnitIds": ["unit_a1_35_days_of_the_week_weekly_calendars"],
            "reviewReason": "Anchor volitional proposals to specific days of the week.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm conversational tone illustrating cheerful social agreement.",
            "successCriteria": [
                "Respond to volitional proposals using 'Тэгье!' naturally.",
                "Offer alternative time slots politely when unavailable."
            ],
            "masteryEvidence": [
                "Executes a 4-turn invitation and agreement exchange smoothly.",
                "Demonstrates authentic prosodic enthusiasm in 'Тэгье, сайхан санаа байна!'."
            ],
            "recommendedExerciseModalities": ["invitation_response", "dialogue_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_48_03_weekend_outing_proposals_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Proposing Spontaneous Social Outings",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate generating spontaneous suggestions for leisure, dining, study, and sports using volitional verbs.",
            "communicativeOutcome": "Spontaneously propose social activities, reaching mutual agreement on activity, time, and location.",
            "objectivesIntroduced": ["obj_a1_48_03_propose_spontaneous_activities"],
            "objectivesPracticed": [
                "obj_a1_48_01_form_volitional_ya",
                "obj_a1_48_02_respond_to_social_proposals"
            ],
            "objectivesReviewed": ["obj_a1_34_03_negotiate_meeting_times"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["кино", "хоол", "газар", "хэзээ", "хаана"],
            "readingObjective": "Read activity event listings proposing concert and museum visits.",
            "listeningObjective": "Comprehend telephone invitations to join a study session or sporting match.",
            "writingObjective": "Draft an invitation text proposing a specific activity, venue, and time to a friend.",
            "spokenProductionObjective": "Propose 3 different activities to a classmate during a conversation drill.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Proactive peer socialization and friendly initiative.",
            "prerequisiteLessonIds": ["les_a1_48_02_social_invitations_and_tegye"],
            "reviewsLessonIds": ["les_a1_34_03_time_drills_and_appointment_setting"],
            "reviewsUnitIds": ["unit_a1_34_telling_clock_time_tsag_minut_hagas"],
            "reviewReason": "Combine volitional suggestions with precise meeting hours.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic peer phone call proposing an afternoon coffee meetup.",
            "successCriteria": [
                "Formulate proposals using volitional verbs with smooth pronunciation.",
                "Agree upon meetup details within 4 conversational turns."
            ],
            "masteryEvidence": [
                "Completes a 6-turn peer outing proposal dialogue fluently.",
                "Uses 'Хоёулаа ... явъя' (Let the two of us go...) naturally."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "phone_call_simulation", "information_gap"]
        },
        {
            "lessonId": "les_a1_48_04_campus_event_invitations_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Student Union Activity Flyers and Social Calls",
            "lessonType": "reading_development",
            "primaryPurpose": "Read student union bulletin board flyers, social invitations, and event posters calling peers to join campus activities.",
            "communicativeOutcome": "Understand event calls, meeting points, entry conditions, and activity agendas from student flyers.",
            "objectivesIntroduced": ["obj_a1_48_04_read_event_calls"],
            "objectivesPracticed": [
                "obj_a1_48_01_form_volitional_ya",
                "obj_a1_48_02_respond_to_social_proposals"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["оюутан", "уралдаан", "баяр", "оролцох", "уулзах"],
            "readingObjective": "Read a 60-word university campus event flyer calling students to a sports tournament and evening celebration.",
            "listeningObjective": None,
            "writingObjective": "Transcribe event name, date, meeting venue, and call-to-action slogan from the flyer.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard student motivational",
            "pragmaticTarget": "Interpreting persuasive public and campus social invitations.",
            "prerequisiteLessonIds": ["les_a1_48_03_weekend_outing_proposals_drills"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Consolidate written recognition of volitional slogans in promotional texts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Enthusiastic student announcer voice reading campus social notices.",
            "successCriteria": [
                "Extract the volitional slogan ('Хамтдаа хөгжилдөцгөөе!') from text.",
                "Identify start time, ticket conditions, and event location accurately."
            ],
            "masteryEvidence": [
                "Answers 4 flyer reading comprehension questions with 100% accuracy.",
                "Invites a peer to the featured event based on flyer details."
            ],
            "recommendedExerciseModalities": ["flyer_scanning", "slogan_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_48_05_invitations_and_plans_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Casual Invitations and Spontaneous Proposals",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal invitations, peer negotiations, and spontaneous meetup plans in recorded conversational audio.",
            "communicativeOutcome": "Accurately record proposed activity, time, and agreed response from spoken social exchanges.",
            "objectivesIntroduced": ["obj_a1_48_05_parse_spoken_invitations"],
            "objectivesPracticed": ["obj_a1_48_01_form_volitional_ya"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["явъя", "уулзъя", "тэгье", "за", "маргааш"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 conversational clips and determine whether the invitation was accepted, declined, or rescheduled.",
            "writingObjective": "Transcribe the volitional proposal phrases and response formulas heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory detection of social agreement and nuance in spoken Mongolian.",
            "prerequisiteLessonIds": ["les_a1_48_03_weekend_outing_proposals_drills"],
            "reviewsLessonIds": ["les_a1_48_02_social_invitations_and_tegye"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Zero-vocabulary auditory lab training invitation perception in rapid speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio featuring varied emotional intonations.",
            "successCriteria": [
                "Identify whether each proposal was accepted ('Тэгье') or declined.",
                "Extract the proposed meetup time from the dialogue."
            ],
            "masteryEvidence": [
                "Scores 100% on the invitation outcome listening test.",
                "Transcribes all heard volitional verb forms without spelling errors."
            ],
            "recommendedExerciseModalities": ["audio_outcome_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_48_06_social_weekend_planner_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Planning an Entire Saturday Outing",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate planning a complete Saturday excursion with a friend: deciding on morning hike, lunch spot, afternoon movie, and evening cafe.",
            "communicativeOutcome": "Conduct a fluid, unscripted planning conversation using volitional proposals for all phases of a full day out.",
            "objectivesIntroduced": ["obj_a1_48_06_plan_full_day_social_outing"],
            "objectivesPracticed": [
                "obj_a1_48_01_form_volitional_ya",
                "obj_a1_48_02_respond_to_social_proposals",
                "obj_a1_48_03_propose_spontaneous_activities"
            ],
            "objectivesReviewed": ["obj_a1_47_06_plan_group_social_event"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReviewed": ["gram_a1_telling_time_clock_calendar", "gram_a1_case_comitative_accompaniment"],
            "grammarReinforced": ["gram_a1_case_comitative_accompaniment"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_01_greetings_and_farewells"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life", "lex_a1_food_dining"],
            "previousVocabularyReused": ["бямба", "өглөө", "өдөр", "орой", "хоол", "кино"],
            "readingObjective": "Read leisure option prompt cards.",
            "listeningObjective": "Comprehend partner proposals regarding activity sequence and times.",
            "writingObjective": "Draft a finalized Saturday excursion itinerary detailing 4 activities, locations, and hours.",
            "spokenProductionObjective": "Execute an 8-turn conversation organizing a full Saturday schedule using volitional forms.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Enthusiastic and harmonious social collaboration.",
            "prerequisiteLessonIds": [
                "les_a1_48_04_campus_event_invitations_reading",
                "les_a1_48_05_invitations_and_plans_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_48_03_weekend_outing_proposals_drills"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 48 volitional skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating peer planning for a fun weekend.",
            "successCriteria": [
                "Propose activities using volitional -я/-е/-ё at each step of the itinerary.",
                "Agree upon 4 distinct activities without communication breakdown."
            ],
            "masteryEvidence": [
                "Completes unscripted 8-turn conversation fluently in under 2 minutes.",
                "Both partners produce identical written Saturday timelines from their discussion."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "itinerary_design", "social_simulation"]
        }
    ])
'''

with open("scripts/framework_builder/gen_sec04_part1.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_46_to_48 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec04_part1.py", "w") as f:
    f.write(new_cur)

print("gen_sec04_part1.py updated through Unit 48!")
