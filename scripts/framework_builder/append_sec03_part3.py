"""
Append Units 38 through 44 to gen_sec03_full.py
"""

code_38_to_44 = '''
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
'''

with open("scripts/framework_builder/gen_sec03_full.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_38_to_44 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec03_full.py", "w") as f:
    f.write(new_cur)

print("gen_sec03_full.py updated through Unit 39!")
