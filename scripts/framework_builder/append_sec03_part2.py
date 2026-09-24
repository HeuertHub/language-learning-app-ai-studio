"""
Append Units 36 through 44 to gen_sec03_full.py
"""

code_36_to_44 = '''
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
'''

with open("scripts/framework_builder/gen_sec03_full.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_36_to_44 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec03_full.py", "w") as f:
    f.write(new_cur)

print("gen_sec03_full.py updated through Unit 37!")
