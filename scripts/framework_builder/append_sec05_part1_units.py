"""
Append Units 55, 56, 57, 58 to gen_sec05_part1.py
"""

code_55_to_58 = '''
    # =========================================================================
    # UNIT 55: Possessive Pronouns: Миний, Чиний, Түүний, Манай (pos 55)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[55]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_55_01_personal_vs_collective_possessive_pronouns",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Mine, Yours, and Ours: Миний, Чиний, Түүний, and Манай",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce singular possessive pronouns (миний 'my', чиний 'your', түүний 'his/her') and distinguish personal ownership from collective family/communal belonging using 'манай' ('our/my family/my house').",
            "communicativeOutcome": "Express personal ownership and distinguish individual belongings from family possessions (e.g. 'Энэ миний ном', 'Манай гэр Ховдод байдаг').",
            "objectivesIntroduced": ["obj_a1_55_01_form_possessive_pronouns", "obj_a1_55_02_contrast_minii_and_manai"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_54_02_form_genitive_possession"],
            "grammarIntroduced": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_genitive_possession"],
            "grammarReinforced": ["gram_a1_case_genitive_possession"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_personal_possessions", "lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["миний", "чиний", "ном", "гэр", "цүнх"],
            "readingObjective": "Read labels on personal items and household property rosters.",
            "listeningObjective": "Hear the pragmatic contrast between 'миний' (individual) and 'манай' (collective family) in spoken sentences.",
            "writingObjective": "Write 4 sentences contrasting personal items (миний харандаа) with family items (манай машин).",
            "spokenProductionObjective": "State aloud 3 items that are yours and 2 things that belong to your family.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Culturally sensitive differentiation between egocentric ownership and collective family belonging.",
            "prerequisiteLessonIds": ["les_a1_54_06_family_album_presentation_synthesis"],
            "reviewsLessonIds": ["les_a1_54_01_nuclear_kinship_and_genitive_possession"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Synthesize noun genitive forms with personal pronominal possessives.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear prosodic emphasis contrasting 'миний' and 'манай'.",
            "successCriteria": [
                "Use 'манай' when referring to home, family, country, or shared workplace.",
                "Use 'миний' for personal portable possessions and private attributes."
            ],
            "masteryEvidence": [
                "Produces 'Энэ миний утас, энэ манай гэр' without hesitation.",
                "Distinguishes 'танай' (your family/household) from 'таны' (your formal personal)."
            ],
            "recommendedExerciseModalities": ["pronoun_matching", "sentence_transformation", "cued_production"]
        },
        {
            "lessonId": "les_a1_55_02_formal_and_plural_possessives_tanii_tednii",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Respect and Groups: Таны, Танай, Бидний, and Тэдний",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce polite formal possessives (таны 'your formal', танай 'your household/family') and plural possessive pronouns (бидний 'our', тэдний 'their').",
            "communicativeOutcome": "Politely ask about others' possessions and refer to third-party group belongings with respectful address.",
            "objectivesIntroduced": ["obj_a1_55_03_form_formal_and_plural_possessives"],
            "objectivesPracticed": ["obj_a1_55_01_form_possessive_pronouns"],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_possessions", "lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["та", "таны", "гэр", "сургууль", "хэн"],
            "readingObjective": "Read visitor badges, property title tags, and school ownership lists.",
            "listeningObjective": "Comprehend polite inquiries regarding whether an object belongs to the listener or their office.",
            "writingObjective": "Draft 3 polite questions asking if an item belongs to a teacher or host.",
            "spokenProductionObjective": "Ask a teacher politely if an umbrella is theirs using 'Энэ таны шүхэр үү?'.",
            "registerTarget": "Courteous standard polite",
            "pragmaticTarget": "Respectful interpersonal address honoring seniority and institutional etiquette.",
            "prerequisiteLessonIds": ["les_a1_55_01_personal_vs_collective_possessive_pronouns"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine polite possessive queries with question particle 'үү/үү'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Courteous honorific inquiry prosody.",
            "successCriteria": [
                "Select 'таны' for formal individual and 'танай' for household.",
                "Inquire ownership accurately using 'Энэ хэнийх вэ?'."
            ],
            "masteryEvidence": [
                "Executes a 4-turn lost-and-found inquiry dialogue flawlessly.",
                "Differentiates 'бидний' from 'манай' accurately in written exercises."
            ],
            "recommendedExerciseModalities": ["ownership_inquiry", "dialogue_completion", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_55_03_substantive_possessive_heniyh_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Substantive Possessives -ийнх and Whose Is It? (Хэнийх вэ?)",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate substantive possessive pronouns and nouns ending in -х/-ийнх (минийх 'mine', чинийх 'yours', манайх 'ours/our family', багшийнх 'the teacher's') and questions with 'Хэнийх вэ?'.",
            "communicativeOutcome": "Clarify ownership of unattached objects and claim items using substantive possessives.",
            "objectivesIntroduced": ["obj_a1_55_04_form_substantive_possessives"],
            "objectivesPracticed": [
                "obj_a1_55_01_form_possessive_pronouns",
                "obj_a1_55_03_form_formal_and_plural_possessives"
            ],
            "objectivesReviewed": ["obj_a1_16_01_identify_classroom_objects"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": ["gram_a1_nominal_predicate_zero_copula"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_personal_possessions"],
            "previousVocabularyReused": ["минийх", "чинийх", "хэнийх", "цүнх", "түлхүүр"],
            "readingObjective": "Read lost-and-found notice boards at school and office lobbies.",
            "listeningObjective": "Comprehend speakers claiming items or denying ownership in lost-property disputes.",
            "writingObjective": "Write 4 sentences identifying the owners of misplaced items using substantive possessives.",
            "spokenProductionObjective": "Claim a misplaced bag aloud using 'Энэ минийх, баярлалаа!'.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear resolution of ownership queries in common spaces.",
            "prerequisiteLessonIds": ["les_a1_55_02_formal_and_plural_possessives_tanii_tednii"],
            "reviewsLessonIds": ["les_a1_16_01_classroom_items_and_identities"],
            "reviewsUnitIds": ["unit_a1_16_classroom_core_objects_nominal_p"],
            "reviewReason": "Combine classroom stationery nouns with substantive possessives.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic lost-and-found classroom interaction.",
            "successCriteria": [
                "Formulate 'Энэ хэнийх вэ?' with natural intonation.",
                "Respond accurately with 'Энэ минийх биш, Доржийнх' when appropriate."
            ],
            "masteryEvidence": [
                "Completes a 6-item lost-and-found matching drill with 100% accuracy.",
                "Explains ownership without repeating modified head nouns."
            ],
            "recommendedExerciseModalities": ["lost_and_found_simulation", "substantive_transformation", "roleplay"]
        },
        {
            "lessonId": "les_a1_55_04_roommates_and_shared_spaces_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Dormitory Rules and Roommate Possession Agreements",
            "lessonType": "reading_development",
            "primaryPurpose": "Read student dormitory roommate agreements and household guidelines distinguishing personal belongings from communal resources.",
            "communicativeOutcome": "Understand roommate chore rosters and possession boundaries in shared living quarters.",
            "objectivesIntroduced": ["obj_a1_55_05_read_dormitory_agreements"],
            "objectivesPracticed": [
                "obj_a1_55_01_form_possessive_pronouns",
                "obj_a1_55_04_form_substantive_possessives"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["өрөө", "оюутан", "хамт", "хөргөгч", "хэрэглэх"],
            "readingObjective": "Read a 70-word dormitory shared-room agreement detailing personal shelves and shared appliances.",
            "listeningObjective": None,
            "writingObjective": "List 3 items designated as personal and 3 items designated as shared from the text.",
            "spokenProductionObjective": None,
            "registerTarget": "Institutional living standard",
            "pragmaticTarget": "Understanding communal rights and property etiquette in shared housing.",
            "prerequisiteLessonIds": ["les_a1_55_03_substantive_possessive_heniyh_drills"],
            "reviewsLessonIds": ["les_a1_55_01_personal_vs_collective_possessive_pronouns"],
            "reviewsUnitIds": ["unit_a1_55_possessive_pronouns_"],
            "reviewReason": "Consolidate written recognition of possessive pronouns in domestic guidelines.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear narration reading student accommodation regulations.",
            "successCriteria": [
                "Distinguish which refrigerator shelves belong to which student.",
                "Extract communal chore responsibilities accurately."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Identifies property conflicts correctly in simulated case studies."
            ],
            "recommendedExerciseModalities": ["agreement_scanning", "property_sorting", "short_answer"]
        },
        {
            "lessonId": "les_a1_55_05_possessions_and_claims_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Ownership Disputes and Inquiries in Fast Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid spoken dialogue where people claim items, inquire about lost objects, and sort out belongings after group trips.",
            "communicativeOutcome": "Accurately record who owns which item from fast conversational exchanges.",
            "objectivesIntroduced": ["obj_a1_55_06_parse_ownership_dialogue"],
            "objectivesPracticed": ["obj_a1_55_04_form_substantive_possessives"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_possessions"],
            "previousVocabularyReused": ["минийх", "чинийх", "түүнийх", "манайх", "юу"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 conversational clips sorting gear after a hike and match 5 items to their rightful owners.",
            "writingObjective": "Transcribe the substantive possessive forms heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory precision detecting subtle possessive suffixes in spontaneous speech.",
            "prerequisiteLessonIds": ["les_a1_55_03_substantive_possessive_heniyh_drills"],
            "reviewsLessonIds": ["les_a1_55_02_formal_and_plural_possessives_tanii_tednii"],
            "reviewsUnitIds": ["unit_a1_55_possessive_pronouns_"],
            "reviewReason": "Zero-vocabulary auditory lab training possessive discrimination.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic multi-speaker audio with background packing noises.",
            "successCriteria": [
                "Map all 5 items to their correct owners based on audio clues.",
                "Identify when an owner denies possession ('Үгүй ээ, энэ минийх биш')."
            ],
            "masteryEvidence": [
                "Scores 100% on the belongings sorting listening test.",
                "Transcribes substantive forms (-ийнх) without orthographic errors."
            ],
            "recommendedExerciseModalities": ["audio_property_sorting", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_55_06_sorting_belongings_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Packing Up and Sorting Communal Supplies",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate packing up after a weekend camping trip or study session: sorting mixed-up gear, returning books, identifying jackets, and organizing bags.",
            "communicativeOutcome": "Conduct a fluid, unscripted sorting dialogue establishing ownership for a dozen items smoothly.",
            "objectivesIntroduced": ["obj_a1_55_07_coordinate_belongings_sorting"],
            "objectivesPracticed": [
                "obj_a1_55_01_form_possessive_pronouns",
                "obj_a1_55_03_form_formal_and_plural_possessives",
                "obj_a1_55_04_form_substantive_possessives"
            ],
            "objectivesReviewed": ["obj_a1_54_06_family_album_presentation_synthesis"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_case_genitive_possession"],
            "grammarReinforced": ["gram_a1_case_genitive_possession"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_ownership_possession"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_possessions", "lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["цүнх", "ном", "хувцас", "хэнийх", "минийх", "манайх", "баярлалаа"],
            "readingObjective": "Read simulated gear packing checklist cards.",
            "listeningObjective": "Comprehend partner inquiries regarding whose water bottle or jacket is on the chair.",
            "writingObjective": "Draft a finalized gear inventory log noting which items belong to each person.",
            "spokenProductionObjective": "Execute an 8-turn belongings sorting conversation returning items to rightful owners.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Seamless peer collaboration and respectful property stewardship.",
            "prerequisiteLessonIds": [
                "les_a1_55_04_roommates_and_shared_spaces_reading",
                "les_a1_55_05_possessions_and_claims_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_55_03_substantive_possessive_heniyh_drills"],
            "reviewsUnitIds": ["unit_a1_55_possessive_pronouns_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 55 possessive skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating cooperative property sorting.",
            "successCriteria": [
                "Identify ownership using substantive possessives naturally ('Энэ минийх, тэр чинийх').",
                "Inquire about unknown items using 'Энэ хэнийх вэ?'."
            ],
            "masteryEvidence": [
                "Completes sorting dialogue in under 2 minutes with zero grammatical mistakes.",
                "Both partners produce matching written inventories of returned belongings."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "gear_sorting", "inventory_logging"]
        }
    ])

    # =========================================================================
    # UNIT 56: Family Milestones, Ages & Marital Status (pos 56)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[56]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_56_01_stating_ages_nas_and_dative_recipient",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Ages and Milestones: Хэдэн Настай вэ? and Dative Recipients",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce age inquiries ('Та хэдэн настай вэ?'), age assertions ('Би хорин таван настай'), and dative-locative case marking on milestone recipients (хүүдээ бэлэг өгөх 'giving a gift to one's son').",
            "communicativeOutcome": "Ask and state ages of oneself and family members, and designate milestone recipients with dative case.",
            "objectivesIntroduced": ["obj_a1_56_01_ask_and_state_ages", "obj_a1_56_02_form_dative_recipient"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_31_01_count_items_with_units"],
            "grammarIntroduced": ["gram_a1_case_dative_locative_recipient"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_time_calendar"],
            "previousVocabularyReused": ["нас", "хэд", "аав", "ээж", "өгөх"],
            "readingObjective": "Read demographic survey summaries and birthday invitation notices.",
            "listeningObjective": "Hear speakers stating their age and the ages of their siblings and children.",
            "writingObjective": "Write 4 sentences stating the exact ages of family members (e.g. 'Манай ах гучин настай').",
            "spokenProductionObjective": "State your age and ask a partner their age politely aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Accurate age reporting across bureaucratic and personal social domains.",
            "prerequisiteLessonIds": ["les_a1_55_06_sorting_belongings_synthesis"],
            "reviewsLessonIds": ["les_a1_31_01_measure_words_and_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_clas"],
            "reviewReason": "Combine cardinal numbers (20, 30, 45) with the age noun 'нас' and comitative suffix 'настай'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of multi-digit numbers and age phrasing.",
            "successCriteria": [
                "Formulate 'Би [X] настай' without grammatical hesitation.",
                "Mark milestone gift recipient with dative case (-д/-т)."
            ],
            "masteryEvidence": [
                "Answers 'Танай дүү хэдэн настай вэ?' fluently.",
                "Distinguishes cardinal count from age specification."
            ],
            "recommendedExerciseModalities": ["age_drills", "recipient_marking", "cued_production"]
        },
        {
            "lessonId": "les_a1_56_02_marital_status_and_family_composition",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Marital Status and Households: Гэрлэсэн, Суусан, and Хүүхэдтэй",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce relationship and marital status vocabulary: гэрлэсэн 'married', хүнтэй суусан 'married/settled', ганц бие 'single', хүүхэдтэй 'with children', сандарсан/салсан 'separated/divorced'.",
            "communicativeOutcome": "Describe marital status, spouse, and family composition accurately and courteously.",
            "objectivesIntroduced": ["obj_a1_56_03_describe_marital_status"],
            "objectivesPracticed": ["obj_a1_56_01_ask_and_state_ages"],
            "objectivesReviewed": ["obj_a1_47_02_express_possession_with_comitative"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReviewed": ["gram_a1_case_comitative_possession_predicates"],
            "grammarReinforced": ["gram_a1_case_comitative_possession_predicates"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsReviewed": ["comm_a1_15_family_nuclear_members"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["хүн", "гэр", "хүүхэд", "байх", "нөхөр", "эхнэр"],
            "readingObjective": "Read civil registration census forms and personal introductory bios.",
            "listeningObjective": "Comprehend speakers discussing their marital status, spouse's profession, and children.",
            "writingObjective": "Draft a short 3-sentence profile stating marital status, spouse, and child status.",
            "spokenProductionObjective": "Explain your marital status or a fictional character's family status aloud.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Discreet, polite communication regarding personal and marital circumstances.",
            "prerequisiteLessonIds": ["les_a1_56_01_stating_ages_nas_and_dative_recipient"],
            "reviewsLessonIds": ["les_a1_47_02_comitative_predicative_possession"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Combine comitative possession (-тай) with child terms (хоёр хүүхэдтэй).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Courteous, neutral tone discussing demographic and civil status.",
            "successCriteria": [
                "Differentiate between 'ганц бие' (single) and 'гэрлэсэн' (married).",
                "Refer to husband (нөхөр) and wife (эхнэр) respectfully."
            ],
            "masteryEvidence": [
                "Produces 'Би гэрлэсэн, хоёр хүүхэдтэй' with natural cadence.",
                "Fills out civil registration demographic questions correctly."
            ],
            "recommendedExerciseModalities": ["status_classification", "demographic_form_filling", "roleplay"]
        },
        {
            "lessonId": "les_a1_56_03_birth_years_and_zodiac_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Birth Years, Anniversaries, and Lunar Zodiac Animals",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining four-digit birth years ('Би 1998 онд төрсөн') with traditional 12-year lunar zodiac signs (жил: морь, хонь, бич, нохой гэх мэт) and anniversary milestones.",
            "communicativeOutcome": "State birth years, identify lunar birth animals, and celebrate family anniversaries fluently.",
            "objectivesIntroduced": ["obj_a1_56_04_state_birth_year_and_zodiac"],
            "objectivesPracticed": [
                "obj_a1_56_01_ask_and_state_ages",
                "obj_a1_56_03_describe_marital_status"
            ],
            "objectivesReviewed": ["obj_a1_36_01_state_calendar_dates"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_time_calendar", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["он", "төрсөн", "жил", "баяр", "өдөр"],
            "readingObjective": "Read astrological lunar calendar charts and biographical summaries.",
            "listeningObjective": "Comprehend elders asking young relatives which animal year they were born in ('Ямар жилтэй вэ?').",
            "writingObjective": "Write 3 sentences detailing birth year, lunar animal sign, and birth month for family members.",
            "spokenProductionObjective": "State your birth year and animal sign aloud in Mongolian.",
            "registerTarget": "Courteous standard cultural",
            "pragmaticTarget": "Cultural engagement with traditional Mongolian chronological reckoning.",
            "prerequisiteLessonIds": ["les_a1_56_02_marital_status_and_family_composition"],
            "reviewsLessonIds": ["les_a1_36_01_calendar_dates_and_ordinal_suffixes"],
            "reviewsUnitIds": ["unit_a1_36_calendar_dates_months_seasons"],
            "reviewReason": "Combine historical years with temporal dative marking (-д онд).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm conversational audio discussing traditional birth year reckoning.",
            "successCriteria": [
                "Formulate 'Би [Year] онд төрсөн' accurately.",
                "State lunar animal sign using '[Animal] жилтэй'."
            ],
            "masteryEvidence": [
                "Answers 'Та ямар жилтэй вэ?' fluently.",
                "Converts western birth years to corresponding Mongolian lunar zodiac signs."
            ],
            "recommendedExerciseModalities": ["zodiac_matching", "birth_year_drills", "interview_simulation"]
        },
        {
            "lessonId": "les_a1_56_04_biographical_anniversaries_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Golden Wedding Anniversaries and Milestone Tributes",
            "lessonType": "reading_development",
            "primaryPurpose": "Read anniversary tribute cards, newspaper notices, and social greetings honoring parents' silver/golden wedding milestones and retirement celebrations.",
            "communicativeOutcome": "Understand familial milestones, celebration dates, honorees' ages, and commemorative wishes.",
            "objectivesIntroduced": ["obj_a1_56_05_read_milestone_tributes"],
            "objectivesPracticed": [
                "obj_a1_56_01_ask_and_state_ages",
                "obj_a1_56_03_describe_marital_status"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReviewed": ["gram_a1_noun_phrase_attributive_adjective"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["баяр", "гэр бүл", "жил", "амьдрал", "сайхан"],
            "readingObjective": "Read a 70-word anniversary announcement celebrating 50 years of marriage and a growing extended family.",
            "listeningObjective": None,
            "writingObjective": "List the milestone date, ages of celebrants, and number of grandchildren mentioned in the tribute.",
            "spokenProductionObjective": None,
            "registerTarget": "Formal celebratory standard",
            "pragmaticTarget": "Interpreting congratulatory and commemorative social documents.",
            "prerequisiteLessonIds": ["les_a1_56_03_birth_years_and_zodiac_guided_drills"],
            "reviewsLessonIds": ["les_a1_56_01_stating_ages_nas_and_dative_recipient"],
            "reviewsUnitIds": ["unit_a1_56_family_milestones_ages_marital_stat"],
            "reviewReason": "Consolidate written recognition of milestone terminology and ages.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm, formal commemorative voice reading celebratory announcements.",
            "successCriteria": [
                "Identify the honorees and their milestone achievement.",
                "Extract participant numbers (children, grandchildren) from the text."
            ],
            "masteryEvidence": [
                "Answers 4 milestone reading comprehension questions with 100% accuracy.",
                "Drafts a 2-line congratulatory wish suitable for an anniversary card."
            ],
            "recommendedExerciseModalities": ["tribute_scanning", "chronological_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_56_05_milestone_interviews_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Ages, Marriage Years, and Generations in Spoken Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal interviews where individuals state their age, marriage date, children's ages, and generational milestones.",
            "communicativeOutcome": "Accurately record multi-digit dates, ages, and marital statuses from natural spoken interviews.",
            "objectivesIntroduced": ["obj_a1_56_06_parse_demographic_audio"],
            "objectivesPracticed": ["obj_a1_56_01_ask_and_state_ages"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["нас", "хүүхэд", "он", "гэрлэсэн", "хэд"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 biographical audio snippets and complete demographic record cards for each speaker.",
            "writingObjective": "Transcribe the age numbers and marital descriptors heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard journalistic/conversational",
            "pragmaticTarget": "Auditory precision parsing rapid numeric dates and demographic facts.",
            "prerequisiteLessonIds": ["les_a1_56_03_birth_years_and_zodiac_guided_drills"],
            "reviewsLessonIds": ["les_a1_56_02_marital_status_and_family_composition"],
            "reviewsUnitIds": ["unit_a1_56_family_milestones_ages_marital_stat"],
            "reviewReason": "Zero-vocabulary auditory lab training demographic audio perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational interview audio with varied regional speakers.",
            "successCriteria": [
                "Record 4 ages and 4 birth years correctly from spoken audio.",
                "Determine marital status without misinterpreting colloquial phrasing."
            ],
            "masteryEvidence": [
                "Scores 100% on the demographic listening test.",
                "Correctly writes down both western years and lunar animal years heard."
            ],
            "recommendedExerciseModalities": ["audio_form_completion", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_56_06_life_history_interview_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Conducting a Life History and Milestone Interview",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a friendly biographical interview with a partner: asking about their age, birth year, zodiac sign, marital status, children, and family milestones.",
            "communicativeOutcome": "Conduct a comprehensive personal demographic interview with courteous tone and reciprocal sharing.",
            "objectivesIntroduced": ["obj_a1_56_07_conduct_life_history_interview"],
            "objectivesPracticed": [
                "obj_a1_56_01_ask_and_state_ages",
                "obj_a1_56_03_describe_marital_status",
                "obj_a1_56_04_state_birth_year_and_zodiac"
            ],
            "objectivesReviewed": ["obj_a1_55_06_sorting_belongings_synthesis"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": ["gram_a1_case_dative_locative_temporal"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_16_family_size_marital_status"],
            "communicativeFunctionsReviewed": ["comm_a1_15_family_nuclear_members"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_time_calendar"],
            "previousVocabularyReused": ["нас", "он", "төрсөн", "гэрлэсэн", "хүүхэд", "сонин", "сайхан"],
            "readingObjective": "Read biographical roleplay persona cards.",
            "listeningObjective": "Comprehend partner responses regarding milestone dates and family facts.",
            "writingObjective": "Draft a structured 5-point demographic summary profile of the interviewed partner.",
            "spokenProductionObjective": "Execute an 8-turn reciprocal biographical interview covering all milestone domains.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Empathetic, polite conversational inquiry into life milestones.",
            "prerequisiteLessonIds": [
                "les_a1_56_04_biographical_anniversaries_reading",
                "les_a1_56_05_milestone_interviews_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_56_03_birth_years_and_zodiac_guided_drills"],
            "reviewsUnitIds": ["unit_a1_56_family_milestones_ages_marital_stat"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 56 milestone skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating warm biographical interview.",
            "successCriteria": [
                "Inquire about age, birth year, and family status with polite question forms.",
                "Record all biographical details accurately on the interview form."
            ],
            "masteryEvidence": [
                "Completes unscripted life milestone interview in under 2 minutes.",
                "Both partners produce identical written biographical summaries of each other."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "biographical_interview", "profile_creation"]
        }
    ])

    # =========================================================================
    # UNIT 57: Ongoing Progressive Aspect: Verbal Suffix -ж байна (pos 57)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[57]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_57_01_progressive_aspect_j_baina_formation",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Happening Right Now: The Progressive Aspect -ж байна / -ч байна",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the present progressive aspect construction [Verb]-ж/-ч байна denoting actions ongoing right at the moment of speech ('is doing X right now') and phonological rules for selecting -ж vs -ч.",
            "communicativeOutcome": "State what one is doing right now and describe real-time ongoing actions of others (e.g. 'Би ном уншиж байна', 'Тэр цай ууж байна').",
            "objectivesIntroduced": ["obj_a1_57_01_form_progressive_aspect_j_baina"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_38_01_form_habitual_aspect_dag"],
            "grammarIntroduced": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag"],
            "grammarReinforced": ["gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_consonant_voicing_and_nasals"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["унших", "бичих", "хийх", "идэх", "уух", "одоо"],
            "readingObjective": "Read instant message status updates and live activity captions.",
            "listeningObjective": "Hear the phonetic alternation between -ж байна and -ч байна in spoken ongoing statements.",
            "writingObjective": "Attach -ж/-ч байна to 6 high-frequency action verbs respecting stem consonant constraints.",
            "spokenProductionObjective": "State aloud 3 things happening around you right now using -ж байна.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Immediate real-time reporting of active events.",
            "prerequisiteLessonIds": ["les_a1_56_06_life_history_interview_synthesis"],
            "reviewsLessonIds": ["les_a1_38_01_habitual_aspect_dag_allomorphs"],
            "reviewsUnitIds": ["unit_a1_38_habitual_present_participle_aspect_"],
            "reviewReason": "Contrast habitual actions (-даг 'usually does') with ongoing current actions (-ж байна 'is doing now').",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of progressive converb endings and auxiliary 'байна'.",
            "successCriteria": [
                "Select -ч after voiceless obstruents (в, г, д, ж, з, с, т) and -ж elsewhere.",
                "Contrast 'Би ажилладаг' (I work) with 'Би ажиллаж байна' (I am working right now)."
            ],
            "masteryEvidence": [
                "Conjugates унших -> уншиж байна, бичих -> бичиж байна, идэх -> идэж байна without error.",
                "Answers 'Та одоо юу хийж байна вэ?' fluently."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "aspect_contrast_drills", "cued_production"]
        },
        {
            "lessonId": "les_a1_57_02_household_activities_and_chores_in_progress",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Around the House: Хоол Хийж Байна, Гэрээ Цэвэрлэж Байна",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce domestic household action verbs (цэвэрлэх 'to clean', угаах 'to wash', засах 'to fix/tidy', хоол хийх 'to cook', индүүдэх 'to iron') in progressive ongoing frames.",
            "communicativeOutcome": "Describe household chores currently underway and explain what each family member is doing at home.",
            "objectivesIntroduced": ["obj_a1_57_02_describe_household_chores_progressive"],
            "objectivesPracticed": ["obj_a1_57_01_form_progressive_aspect_j_baina"],
            "objectivesReviewed": ["obj_a1_54_01_identify_nuclear_kinship"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarReviewed": ["gram_a1_case_accusative_definite_object"],
            "grammarReinforced": ["gram_a1_case_accusative_definite_object"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_15_family_nuclear_members"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["гэр", "хоол", "хувцас", "цэвэрлэх", "угаах"],
            "readingObjective": "Read family group chat updates detailing chore progress at home.",
            "listeningObjective": "Comprehend phone callers explaining why they cannot talk because they are currently busy with chores.",
            "writingObjective": "Draft 3 sentences explaining what family members are doing right now around the house.",
            "spokenProductionObjective": "Explain that you are cooking dinner and your brother is washing dishes aloud.",
            "registerTarget": "Everyday standard domestic friendly",
            "pragmaticTarget": "Seamless domestic coordination and polite real-time availability updates.",
            "prerequisiteLessonIds": ["les_a1_57_01_progressive_aspect_j_baina_formation"],
            "reviewsLessonIds": ["les_a1_54_01_nuclear_kinship_and_genitive_possession"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Combine family kinship subjects with progressive predicate verbs.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural phone conversation cadence discussing ongoing household tasks.",
            "successCriteria": [
                "Formulate domestic progressive sentences without dropping the auxiliary 'байна'.",
                "State chore progress fluently upon prompt."
            ],
            "masteryEvidence": [
                "Produces 'Ээж хоол хийж байна, аав гэрээ цэвэрлэж байна' accurately.",
                "Executes a phone availability roleplay smoothly."
            ],
            "recommendedExerciseModalities": ["chore_matching", "phone_call_simulation", "sentence_construction"]
        },
        {
            "lessonId": "les_a1_57_03_phone_availability_and_interruptions_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Phone Calls, Busy Signals, and Одоо Завгүй Байна",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate answering phone calls, stating ongoing activities, and explaining temporary unavailability ('Би одоо хичээл хийж байна, дараа залгая').",
            "communicativeOutcome": "Politely manage phone calls while busy, explaining current activities and proposing later follow-up.",
            "objectivesIntroduced": ["obj_a1_57_03_manage_phone_calls_progressive"],
            "objectivesPracticed": [
                "obj_a1_57_01_form_progressive_aspect_j_baina",
                "obj_a1_57_02_describe_household_chores_progressive"
            ],
            "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_aspect_progressive_j_baina"],
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
            "previousVocabularyReused": ["залгах", "ярих", "одоо", "дараа", "завгүй"],
            "readingObjective": "Read quick text messages declining calls with pre-set auto-replies.",
            "listeningObjective": "Comprehend callers explaining they are currently in class, driving, or having a meeting.",
            "writingObjective": "Write 3 text message auto-replies explaining current ongoing tasks and promising to call back.",
            "spokenProductionObjective": "Answer a simulated phone call, explain you are studying, and promise to call in 10 minutes.",
            "registerTarget": "Courteous standard conversational",
            "pragmaticTarget": "Polite call screening and respectful communication of availability.",
            "prerequisiteLessonIds": ["les_a1_57_02_household_activities_and_chores_in_progress"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Combine progressive ongoing state with volitional future promise ('... хийж байна, дараа залгая').",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic mobile phone ringtones and brisk conversational speech.",
            "successCriteria": [
                "Formulate 'Би одоо [Verb]-ж байна, дараа ярья' without pause.",
                "Inquire about caller's situation using 'Та одоо юу хийж байна вэ?'."
            ],
            "masteryEvidence": [
                "Completes a 4-turn telephone triage roleplay fluently.",
                "Modulates tone appropriately from busy haste to polite courtesy."
            ],
            "recommendedExerciseModalities": ["phone_triage_simulation", "auto_reply_composition", "roleplay"]
        },
        {
            "lessonId": "les_a1_57_04_live_action_and_event_reports_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Live Social Feeds and Real-Time Event Reports",
            "lessonType": "reading_development",
            "primaryPurpose": "Read live text feeds, sports commentary updates, and event status streams describing what is happening on the field or festival grounds right now.",
            "communicativeOutcome": "Extract ongoing actions, participant positions, and event dynamics from real-time text updates.",
            "objectivesIntroduced": ["obj_a1_57_04_read_live_event_updates"],
            "objectivesPracticed": [
                "obj_a1_57_01_form_progressive_aspect_j_baina",
                "obj_a1_57_02_describe_household_chores_progressive"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["наадам", "морь", "уралдах", "хүмүүс", "үзэх"],
            "readingObjective": "Read a 70-word live social feed reporting the start of a Naadam horse race in real time.",
            "listeningObjective": None,
            "writingObjective": "List 4 simultaneous ongoing actions described in the live update stream.",
            "spokenProductionObjective": None,
            "registerTarget": "Journalistic live report standard",
            "pragmaticTarget": "Comprehending fast-paced real-time informational streams.",
            "prerequisiteLessonIds": ["les_a1_57_03_phone_availability_and_interruptions_drills"],
            "reviewsLessonIds": ["les_a1_57_01_progressive_aspect_j_baina_formation"],
            "reviewsUnitIds": ["unit_a1_57_ongoing_progressive_aspect_verbal_s"],
            "reviewReason": "Consolidate written recognition of progressive aspect in dynamic narrative contexts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Energetic commentator voice reading live status feeds.",
            "successCriteria": [
                "Identify which action is currently happening on the course.",
                "Extract participant locations and actions from the progressive clauses."
            ],
            "masteryEvidence": [
                "Answers 4 live feed reading comprehension questions with 100% accuracy.",
                "Identifies the current leader in the simulated race report."
            ],
            "recommendedExerciseModalities": ["feed_scanning", "action_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_57_05_busy_household_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Ambient Activity and Multi-Tasking in Spoken Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse complex spoken audio featuring multiple background domestic noises (cooking, vacuuming, television) where speakers narrate ongoing activities.",
            "communicativeOutcome": "Accurately correlate background soundscapes with stated ongoing progressive actions.",
            "objectivesIntroduced": ["obj_a1_57_05_parse_ongoing_actions_audio"],
            "objectivesPracticed": ["obj_a1_57_01_form_progressive_aspect_j_baina"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["хийж байна", "цэвэрлэж байна", "уншиж байна", "үзэж байна"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 audio scenes and identify what each person in the room is doing based on dialogue and sound cues.",
            "writingObjective": "Transcribe the progressive verb phrases heard in each scene.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard domestic colloquial",
            "pragmaticTarget": "Auditory scene analysis mapping speech to real-time physical environments.",
            "prerequisiteLessonIds": ["les_a1_57_03_phone_availability_and_interruptions_drills"],
            "reviewsLessonIds": ["les_a1_57_02_household_activities_and_chores_in_progress"],
            "reviewsUnitIds": ["unit_a1_57_ongoing_progressive_aspect_verbal_s"],
            "reviewReason": "Zero-vocabulary auditory lab training progressive aspect acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Rich ambient acoustic scenes with authentic domestic background sounds.",
            "successCriteria": [
                "Map all 4 speakers to their respective ongoing domestic tasks based on dialogue and sound cues.",
                "Distinguish progressive -ж байна from habitual -даг in rapid stream."
            ],
            "masteryEvidence": [
                "Scores 100% on the multi-tasking household listening test.",
                "Correctly spells all progressive converb endings in transcription."
            ],
            "recommendedExerciseModalities": ["audio_scene_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_57_06_live_broadcast_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Live Video Call and Activity Commentary",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a live video call between two friends in different locations: showing one's surroundings, asking what the other is doing right now, and commenting on activities in progress.",
            "communicativeOutcome": "Conduct a fluid, spontaneous video call exchange narrating real-time surroundings and ongoing actions.",
            "objectivesIntroduced": ["obj_a1_57_06_conduct_video_call_commentary"],
            "objectivesPracticed": [
                "obj_a1_57_01_form_progressive_aspect_j_baina",
                "obj_a1_57_02_describe_household_chores_progressive",
                "obj_a1_57_03_manage_phone_calls_progressive"
            ],
            "objectivesReviewed": ["obj_a1_56_06_life_history_interview_synthesis"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_friends_social_life"],
            "previousVocabularyReused": ["одоо", "хийх", "харах", "байна", "зураг", "ярих", "баяртай"],
            "readingObjective": "Read simulated video call scene prompt cards.",
            "listeningObjective": "Comprehend partner descriptions of what is happening around them on camera.",
            "writingObjective": "Draft a short 4-line chat recap summarizing what both friends were doing during the call.",
            "spokenProductionObjective": "Execute an 8-turn video call dialogue describing ongoing real-time activities using -ж байна.",
            "registerTarget": "Courteous standard friendly informal",
            "pragmaticTarget": "Engaging, spontaneous peer communication during live video interactions.",
            "prerequisiteLessonIds": [
                "les_a1_57_04_live_action_and_event_reports_reading",
                "les_a1_57_05_busy_household_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_57_03_phone_availability_and_interruptions_drills"],
            "reviewsUnitIds": ["unit_a1_57_ongoing_progressive_aspect_verbal_s"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 57 progressive skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating lively video call commentary.",
            "successCriteria": [
                "Use progressive -ж байна in every turn describing current actions.",
                "Inquire about partner's surroundings using 'Чи одоо юу хийж байна?'."
            ],
            "masteryEvidence": [
                "Completes video call roleplay without pausing or grammatical errors.",
                "Both partners describe at least 3 distinct ongoing actions naturally."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "video_call_simulation", "activity_commentary"]
        }
    ])

    # =========================================================================
    # UNIT 58: Perfective Past Participle: Suffixes -сан/-сэн/-сон/-сөн (pos 58)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # Lesson 6 is the MID-SECTION 5 CHECKPOINT!
    # =========================================================================
    u = u_map[58]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_58_01_perfective_past_san_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Completed Achievements: The Perfective Past Participle -сан/-сэн/-сон/-сөн",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the perfective past participle suffix -сан/-сэн/-сон/-сөн denoting completed past actions, facts, and life achievements, governed by four-way vowel harmony.",
            "communicativeOutcome": "State completed past actions, historical facts, and educational/career milestones (e.g. 'Би их сургууль төгссөн' - I graduated from university).",
            "objectivesIntroduced": ["obj_a1_58_01_form_perfective_past_san"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_41_01_form_witnessed_past_laa"],
            "grammarIntroduced": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_tense_past_witnessed_laa"],
            "grammarReinforced": ["gram_a1_verb_tense_past_witnessed_laa"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_education_classroom", "lex_a1_professions_occupations"],
            "previousVocabularyReused": ["сургууль", "төгсөх", "ажиллах", "ирэх", "үзэх"],
            "readingObjective": "Read curriculum vitae summaries and biographical profiles featuring completed degrees.",
            "listeningObjective": "Hear the four vowel harmonic allomorphs (-сан/-сэн/-сон/-сөн) across biographical statements.",
            "writingObjective": "Attach the perfective past suffix to 6 verb stems respecting four-way vowel harmony.",
            "spokenProductionObjective": "State where you went to school and what you studied using -сан aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear articulation of historical background and completed qualifications.",
            "prerequisiteLessonIds": ["les_a1_57_06_live_broadcast_synthesis"],
            "reviewsLessonIds": ["les_a1_41_01_witnessed_past_laa_allomorphs"],
            "reviewsUnitIds": ["unit_a1_41_witnessed_past_verbal_tense_suffix_"],
            "reviewReason": "Contrast immediate witnessed past (-лаа) with factual perfective past (-сан).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of perfective past allomorphs across vowel classes.",
            "successCriteria": [
                "Apply -сан to /a/, -сэн to /e, i/, -сон to /o/, -сөн to /ö/ stems.",
                "Use -сан for permanent life achievements and historical statements."
            ],
            "masteryEvidence": [
                "Conjugates сурах -> сурсан, ирэх -> ирсэн, орох -> орсон, үзэх -> үзсэн accurately.",
                "Produces 'Би Монголд гурван жил амьдарсан' fluently."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "biography_completion", "cued_production"]
        },
        {
            "lessonId": "les_a1_58_02_past_interrogatives_and_negatives_san_uu_gui",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Questions and Negation: -сан уу? and -аагүй / -сангүй",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce perfective past questions with '... -сан уу?' (Did you...?) and past negation using '... -аагүй' (haven't yet / didn't) and '... -сангүй' (did not).",
            "communicativeOutcome": "Ask whether someone completed an action and answer affirmatively or negatively.",
            "objectivesIntroduced": ["obj_a1_58_02_ask_and_negate_perfective_past"],
            "objectivesPracticed": ["obj_a1_58_01_form_perfective_past_san"],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu"],
            "grammarReinforced": ["gram_a1_polar_questions_uu_uu"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["хийх", "үзэх", "идэх", "тийм", "үгүй"],
            "readingObjective": "Read checklist status queries and email confirmations of completed tasks.",
            "listeningObjective": "Comprehend speakers asking whether an errand or assignment was finished.",
            "writingObjective": "Draft 3 past questions and provide negative answers using -аагүй.",
            "spokenProductionObjective": "Ask a classmate if they watched a movie and answer if you haven't seen it yet.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Clear progress verification and honest status reporting.",
            "prerequisiteLessonIds": ["les_a1_58_01_perfective_past_san_allomorphs"],
            "reviewsLessonIds": ["les_a1_26_01_content_question_particles_be_ve"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Combine past participle verbs with polar question particles (уу/үү).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational inquiry cadence with rising question intonation.",
            "successCriteria": [
                "Formulate 'Та хоол идсэн үү?' accurately.",
                "Respond negatively using 'Би хараахан идээгүй' (I haven't eaten yet)."
            ],
            "masteryEvidence": [
                "Executes a 4-turn task completion inquiry exchange flawlessly.",
                "Differentiates between past negation (-аагүй) and present negation (биш/байхгүй)."
            ],
            "recommendedExerciseModalities": ["question_response", "task_checklist_verification", "dialogue_roleplay"]
        },
        {
            "lessonId": "les_a1_58_03_travel_and_life_experience_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Places Visited and Experiences Had",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate sharing life experiences, places visited, and books read using the perfective past ('Би Хөвсгөл нуур явсан', 'Тэр энэ номыг уншсан').",
            "communicativeOutcome": "Describe past travels, literary experiences, and cultural encounters in structured conversation.",
            "objectivesIntroduced": ["obj_a1_58_03_describe_past_experiences"],
            "objectivesPracticed": [
                "obj_a1_58_01_form_perfective_past_san",
                "obj_a1_58_02_ask_and_negate_perfective_past"
            ],
            "objectivesReviewed": ["obj_a1_40_01_form_ablative_origin"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_travel_transport", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["явах", "үзэх", "нуур", "хот", "хэзээ"],
            "readingObjective": "Read travel blog snippets recounting visits to Mongolian aimags.",
            "listeningObjective": "Comprehend travelers describing what tourist sights they visited last summer.",
            "writingObjective": "Write 4 sentences listing provinces or cities you have visited in the past.",
            "spokenProductionObjective": "Ask a partner what tourist destination they visited and share your own trip aloud.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Sharing personal life history and cultural experiences with peers.",
            "prerequisiteLessonIds": ["les_a1_58_02_past_interrogatives_and_negatives_san_uu_gui"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Combine directional destination nouns with past perfective verbs.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm conversational audio sharing memorable vacation memories.",
            "successCriteria": [
                "Formulate travel past sentences using [Destination]-д/руу очсон/явсан.",
                "Inquire about past experiences using 'Та тэнд очсон уу?'."
            ],
            "masteryEvidence": [
                "Completes a 6-turn travel debrief dialogue fluently.",
                "Correctly lists 3 tourist sites visited with appropriate postposition or case."
            ],
            "recommendedExerciseModalities": ["travel_exchange", "experience_matrix", "cued_production"]
        },
        {
            "lessonId": "les_a1_58_04_autobiographical_essays_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Short Autobiographical Essays and Profiles",
            "lessonType": "reading_development",
            "primaryPurpose": "Read 80-word personal autobiographies describing birth, schooling, career moves, and current life.",
            "communicativeOutcome": "Extract chronological milestones, schools attended, and career achievements from written autobiographies.",
            "objectivesIntroduced": ["obj_a1_58_04_read_autobiographies"],
            "objectivesPracticed": [
                "obj_a1_58_01_form_perfective_past_san",
                "obj_a1_58_03_describe_past_experiences"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarReviewed": ["gram_a1_case_dative_locative_temporal"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom", "lex_a1_professions_occupations"],
            "previousVocabularyReused": ["төрсөн", "сурсан", "төгссөн", "ажилласан", "жил"],
            "readingObjective": "Read an authentic 80-word autobiography of an engineer from Darkhan.",
            "listeningObjective": None,
            "writingObjective": "Create a timeline placing 4 major life events from the essay into chronological order.",
            "spokenProductionObjective": None,
            "registerTarget": "Autobiographical narrative standard",
            "pragmaticTarget": "Autonomous reading of biographical texts and CV summaries.",
            "prerequisiteLessonIds": ["les_a1_58_03_travel_and_life_experience_guided_drills"],
            "reviewsLessonIds": ["les_a1_58_01_perfective_past_san_allomorphs"],
            "reviewsUnitIds": ["unit_a1_58_perfective_past_participle_suffixes"],
            "reviewReason": "Consolidate written recognition of perfective past chains in narrative prose.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear, dignified narration reading autobiographical reflections.",
            "successCriteria": [
                "Extract graduation year and university name from text.",
                "Identify career transitions and relocation dates accurately."
            ],
            "masteryEvidence": [
                "Answers 4 autobiography reading comprehension questions with 100% accuracy.",
                "Reconstructs the subject's career path on a timeline without error."
            ],
            "recommendedExerciseModalities": ["timeline_construction", "cv_scanning", "short_answer"]
        },
        {
            "lessonId": "les_a1_58_05_life_stories_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Past Narratives and Accomplishments in Fast Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal narratives where speakers summarize their life accomplishments, career shifts, and past experiences.",
            "communicativeOutcome": "Accurately record past accomplishments, dates, and qualifications from spoken personal accounts.",
            "objectivesIntroduced": ["obj_a1_58_05_parse_past_narratives_audio"],
            "objectivesPracticed": ["obj_a1_58_01_form_perfective_past_san"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_verb_tense_past_perfective_san"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_education_classroom", "lex_a1_professions_occupations"],
            "previousVocabularyReused": ["сурсан", "ажилласан", "очсон", "хийгээгүй", "он"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 life story audio clips and record the highest qualification and key past job for each speaker.",
            "writingObjective": "Transcribe the perfective past verb forms heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard narrative",
            "pragmaticTarget": "Auditory tracking of past achievements and historical facts in spoken discourse.",
            "prerequisiteLessonIds": ["les_a1_58_03_travel_and_life_experience_guided_drills"],
            "reviewsLessonIds": ["les_a1_58_02_past_interrogatives_and_negatives_san_uu_gui"],
            "reviewsUnitIds": ["unit_a1_58_perfective_past_participle_suffixes"],
            "reviewReason": "Zero-vocabulary auditory lab training past perfective acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic narrative recordings featuring diverse speaker accents and pacing.",
            "successCriteria": [
                "Extract 4 key past achievements correctly from audio.",
                "Distinguish -сан (completed) from -даг (habitual) in rapid speech."
            ],
            "masteryEvidence": [
                "Scores 100% on the life narrative listening test.",
                "Correctly spells all heard perfective past verbs."
            ],
            "recommendedExerciseModalities": ["audio_cv_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_58_06_section_05_mid_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Section 5 Mid-Section Checkpoint: Kinship, Possession, and Life History",
            "lessonType": "checkpoint",
            "primaryPurpose": "Comprehensive diagnostic evaluation assessing cumulative mastery across Section 5 Units 54-58: nuclear kinship, genitive possession (-ын/-ийн), possessive pronouns (миний, манай, хэнийх), family milestones and ages, progressive aspect (-ж байна), and perfective past achievements (-сан).",
            "communicativeOutcome": "Demonstrate integrated communicative proficiency describing family relations, asserting possession, discussing life milestones, reporting real-time activities, and narrating past accomplishments.",
            "objectivesIntroduced": ["obj_a1_58_06_section_05_mid_mastery"],
            "objectivesPracticed": [
                "obj_a1_54_01_identify_nuclear_kinship",
                "obj_a1_54_02_form_genitive_possession",
                "obj_a1_55_01_form_possessive_pronouns",
                "obj_a1_56_01_ask_and_state_ages",
                "obj_a1_57_01_form_progressive_aspect_j_baina",
                "obj_a1_58_01_form_perfective_past_san"
            ],
            "objectivesReviewed": [
                "obj_a1_53_05_section_04_capstone_mastery",
                "obj_a1_54_04_introduce_family_and_professions"
            ],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_genitive_possession",
                "gram_a1_possessive_pronouns_minii_chiniih",
                "gram_a1_case_dative_locative_recipient",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_past_perfective_san"
            ],
            "grammarReviewed": [
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_verb_tense_past_witnessed_laa"
            ],
            "grammarReinforced": [
                "gram_a1_case_genitive_possession",
                "gram_a1_possessive_pronouns_minii_chiniih",
                "gram_a1_case_dative_locative_recipient",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_past_perfective_san"
            ],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_vowel_harmony_suffixes", "phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_non_initial_reduction", "phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_11_ownership_possession",
                "comm_a1_15_family_nuclear_members",
                "comm_a1_16_family_size_marital_status",
                "comm_a1_08_describing_daily_routines"
            ],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_a1_kinship_family", "lex_a1_personal_possessions",
                "lex_a1_education_classroom", "lex_a1_housing_ger_household"
            ],
            "previousVocabularyReused": [
                "аав", "ээж", "миний", "манай", "нас", "хүүхэд", "хийж байна", "сурсан", "төгссөн", "баярлалаа"
            ],
            "readingObjective": "Read a multi-paragraph personal profile incorporating family background, current ongoing studies, and past achievements.",
            "listeningObjective": "Comprehend a multi-speaker audio conversation covering family relations, possession claims, and life history.",
            "writingObjective": "Compose a structured 60-word personal essay detailing: (1) family tree and parents' jobs, (2) current activities (-ж байна), and (3) past completed schooling (-сан).",
            "spokenProductionObjective": "Execute an unscripted 3-part oral interview: introducing family members, stating what you are doing right now, and narrating your past education.",
            "registerTarget": "Courteous standard multi-register",
            "pragmaticTarget": "Seamless communicative integration across the first half of Section 5.",
            "prerequisiteLessonIds": [
                "les_a1_58_04_autobiographical_essays_reading",
                "les_a1_58_05_life_stories_listening_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_54_06_family_album_presentation_synthesis",
                "les_a1_55_06_sorting_belongings_synthesis",
                "les_a1_56_06_life_history_interview_synthesis",
                "les_a1_57_06_live_broadcast_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_54_nuclear_kinship_parents_siblings_ch",
                "unit_a1_55_possessive_pronouns_",
                "unit_a1_56_family_milestones_ages_marital_stat",
                "unit_a1_57_ongoing_progressive_aspect_verbal_s"
            ],
            "reviewReason": "Mid-Section 5 diagnostic checkpoint verifying cumulative mastery of Units 54 through 58.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Integrated multi-speaker diagnostic assessment audio.",
            "successCriteria": [
                "Pass all four diagnostic modules (Kinship, Possession, Progressive, Past Perfective) with >=85% accuracy.",
                "Demonstrate zero confusion between progressive (-ж байна) and past perfective (-сан)."
            ],
            "masteryEvidence": [
                "Executes all diagnostic oral and written tasks successfully.",
                "Produces fluent, coherent autobiographical monologue without structural flaws."
            ],
            "recommendedExerciseModalities": [
                "integrated_interview", "diagnostic_cloze", "writing_portfolio", "listening_evaluation"
            ]
        }
    ])
'''

with open("scripts/framework_builder/gen_sec05_part1.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_55_to_58 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec05_part1.py", "w") as f:
    f.write(new_cur)

print("gen_sec05_part1.py updated through Unit 58 (Checkpoint)!")
