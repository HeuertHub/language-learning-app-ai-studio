"""
Append Units 60, 61, 62, 63 to gen_sec05_part2.py
"""

code_60_to_63 = '''
    # =========================================================================
    # UNIT 60: Prohibitive Imperative: The Particle Битгий (pos 60)
    # 6 Lessons | Targets: ProdLem=21, RecLem=8, ProdExp=4, RecExp=2
    # Budget: (6,2,1,1), (5,2,1,0), (5,2,1,1), (5,2,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[60]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_60_01_prohibitive_particle_bitgii",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Don't Do That: The Prohibitive Particle Битгий and -аарай",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the prohibitive particle 'битгий' placed before bare imperatives or polite imperative suffixes (-аарай/-ээрэй/-оорой/-өөрэй) to express polite warnings and negative commands ('Битгий хоцроорой', 'Битгий санаа зов').",
            "communicativeOutcome": "Issue polite prohibitions, safety warnings, and comforting reassurances against negative actions.",
            "objectivesIntroduced": ["obj_a1_60_01_form_prohibitive_bitgii"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_49_01_form_polite_imperative_aarai"],
            "grammarIntroduced": ["gram_a1_verb_prohibitive_bitgii"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_health_safety_rules", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["битгий", "хоцрох", "мартах", "санаа", "орох"],
            "readingObjective": "Read public warning signs and instructional prohibitions ('Битгий хүр', 'Битгий тамхи тат').",
            "listeningObjective": "Hear the prohibitive particle 'битгий' combined with various imperative forms in spoken warnings.",
            "writingObjective": "Formulate 4 polite warning notices using 'битгий' and '-аарай/-ээрэй'.",
            "spokenProductionObjective": "Tell a friend not to worry and not to be late aloud in Mongolian.",
            "registerTarget": "Everyday standard friendly/cautious",
            "pragmaticTarget": "Courteous admonition and comforting reassurance without sounding harsh or aggressive.",
            "prerequisiteLessonIds": ["les_a1_59_06_future_plans_interview_synthesis"],
            "reviewsLessonIds": ["les_a1_49_01_polite_imperative_aarai_allomorphs"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Combine polite imperative suffix (-аарай) with prohibitive pre-verbal particle (битгий).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Gentle, caring prosody conveying reassurance ('Битгий санаа зовоорой').",
            "successCriteria": [
                "Place 'битгий' directly before the verb stem or inflected imperative.",
                "Differentiate between standard negative copula (биш) and prohibitive particle (битгий)."
            ],
            "masteryEvidence": [
                "Produces 'Битгий хоцроорой, цагтаа ирээрэй' fluently.",
                "Constructs 3 warning signs without word-order errors."
            ],
            "recommendedExerciseModalities": ["warning_matching", "sign_formulation", "cued_production"]
        },
        {
            "lessonId": "les_a1_60_02_urging_optative_aach_and_jussive_g",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Urgent Requests and Third-Person Wishes: -аач/-ээч and -г",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce the urging optative suffix -аач/-ээч/-ооч/-өөч ('please do!', urgent entreaty) and third-person jussive/permissive suffix -г ('let him/them do!').",
            "communicativeOutcome": "Make heartfelt urgent requests to peers and express third-person permissions or blessings.",
            "objectivesIntroduced": [
                "obj_a1_60_02_form_urging_optative_aach",
                "obj_a1_60_03_form_third_person_jussive_g"
            ],
            "objectivesPracticed": ["obj_a1_60_01_form_prohibitive_bitgii"],
            "objectivesReviewed": ["obj_a1_48_01_form_volitional_ya"],
            "grammarIntroduced": [
                "gram_a1_verb_urging_optative_aach",
                "gram_a1_verb_jussive_third_person_g"
            ],
            "grammarPracticed": ["gram_a1_verb_prohibitive_bitgii"],
            "grammarReviewed": ["gram_a1_verb_volitional_intention_ya"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_daily_routines_hobbies", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["харах", "өгөх", "хэлэх", "орох", "болох"],
            "readingObjective": "Read dialogue lines in plays and storybooks featuring urgent pleas and blessings.",
            "listeningObjective": "Comprehend speakers making pleading requests ('Надад туслаач!') and third-person permissions.",
            "writingObjective": "Draft 3 urgent requests using -аач and 2 third-person blessings using -г.",
            "spokenProductionObjective": "Ask a friend earnestly to show you a book using 'Надад харуулаач' aloud.",
            "registerTarget": "Emotional friendly standard / traditional optative",
            "pragmaticTarget": "Navigating degrees of urgency and emotional entreaty appropriately.",
            "prerequisiteLessonIds": ["les_a1_60_01_prohibitive_particle_bitgii"],
            "reviewsLessonIds": ["les_a1_48_01_volitional_ya_allomorphs"],
            "reviewsUnitIds": ["unit_a1_48_volitional_intention_suffixes_ya_ye_"],
            "reviewReason": "Contrast first-person volitional (-я) with second-person urging (-аач) and third-person jussive (-г).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Expressive intonation conveying earnest entreaty and goodwill.",
            "successCriteria": [
                "Select -аач/-ээч/-ооч/-өөч respecting four-way vowel harmony.",
                "Attach -г to third-person subject clauses ('Тэр ороод ирэг' - Let him come in)."
            ],
            "masteryEvidence": [
                "Produces 'Надад туслаач, гуйж байна' naturally.",
                "Accurately distinguishes between -аарай (polite advice) and -аач (urgent plea)."
            ],
            "recommendedExerciseModalities": ["request_intensity_sorting", "dialogue_completion", "roleplay"]
        },
        {
            "lessonId": "les_a1_60_03_safety_rules_and_reminders_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Safety Instructions, Lab Etiquette, and Classroom Rules",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate generating and responding to safety instructions, prohibitions, and classroom guidelines using 'Битгий [Verb]-аарай' and affirmative directives.",
            "communicativeOutcome": "Explain school and workplace safety rules, caution colleagues, and follow safety protocols.",
            "objectivesIntroduced": ["obj_a1_60_04_deliver_safety_instructions"],
            "objectivesPracticed": [
                "obj_a1_60_01_form_prohibitive_bitgii",
                "obj_a1_60_02_form_urging_optative_aach"
            ],
            "objectivesReviewed": ["obj_a1_49_02_give_classroom_instructions"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_verb_prohibitive_bitgii",
                "gram_a1_verb_urging_optative_aach"
            ],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_health_safety_rules", "lex_a1_education_classroom"],
            "previousVocabularyReused": ["битгий", "хүрэх", "гүйлгэх", "дуугүй", "анхаарах"],
            "readingObjective": "Read safety posters in laboratories, museums, and transport facilities.",
            "listeningObjective": "Comprehend tour guides and instructors briefing groups on what not to do during an excursion.",
            "writingObjective": "Write a 5-rule safety guide for a science lab or computer room.",
            "spokenProductionObjective": "Deliver a 30-second safety briefing cautioning peers against touching equipment.",
            "registerTarget": "Institutional safety standard",
            "pragmaticTarget": "Clear, authoritative yet polite transmission of precautionary rules.",
            "prerequisiteLessonIds": ["les_a1_60_02_urging_optative_aach_and_jussive_g"],
            "reviewsLessonIds": ["les_a1_49_02_classroom_imperatives_and_exercises"],
            "reviewsUnitIds": ["unit_a1_49_polite_request_imperative_suffixes_"],
            "reviewReason": "Combine affirmative classroom instructions with prohibitive safety rules.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Clear, instructional briefing voice delivering safety protocols.",
            "successCriteria": [
                "Generate both affirmative instructions (-аарай) and prohibitions (битгий ... -аарай) accurately.",
                "Maintain polite register when giving cautions."
            ],
            "masteryEvidence": [
                "Delivers complete safety briefing from prompt card without errors.",
                "Categorizes 6 actions into 'Allowed' vs 'Prohibited'."
            ],
            "recommendedExerciseModalities": ["safety_briefing_simulation", "rule_drafting", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_60_04_museum_and_library_notices_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Museum Regulations and Public Notice Boards",
            "lessonType": "reading_development",
            "primaryPurpose": "Read official public notices, museum behavior guidelines, and library silence regulations featuring prohibitive and imperative constructions.",
            "communicativeOutcome": "Understand public regulations, photography bans, quiet zones, and security instructions in public buildings.",
            "objectivesIntroduced": ["obj_a1_60_05_read_public_regulations"],
            "objectivesPracticed": [
                "obj_a1_60_01_form_prohibitive_bitgii",
                "obj_a1_60_04_deliver_safety_instructions"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_verb_prohibitive_bitgii"],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_health_safety_rules", "lex_a1_public_services_amenities"],
            "previousVocabularyReused": ["музей", "зураг", "авах", "хориотой", "битгий"],
            "readingObjective": "Read a 70-word National History Museum visitor notice detailing photography rules, bag drop policies, and silence zones.",
            "listeningObjective": None,
            "writingObjective": "List 3 prohibited behaviors and 2 mandatory requirements based on the museum notice.",
            "spokenProductionObjective": None,
            "registerTarget": "Formal administrative regulation standard",
            "pragmaticTarget": "Autonomous comprehension of official public signage and institutional notices.",
            "prerequisiteLessonIds": ["les_a1_60_03_safety_rules_and_reminders_guided_drills"],
            "reviewsLessonIds": ["les_a1_60_01_prohibitive_particle_bitgii"],
            "reviewsUnitIds": ["unit_a1_60_prohibitive_imperative_the_particle"],
            "reviewReason": "Consolidate written recognition of prohibitive particle constructions in public texts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Formal administrative voice reading museum guidelines.",
            "successCriteria": [
                "Identify where photography is permitted and where flash is prohibited.",
                "Extract cloakroom requirements accurately."
            ],
            "masteryEvidence": [
                "Answers 4 regulation reading comprehension questions with 100% accuracy.",
                "Accurately summarizes the rules in a bulleted checklist."
            ],
            "recommendedExerciseModalities": ["notice_scanning", "rule_categorization", "short_answer"]
        },
        {
            "lessonId": "les_a1_60_05_urgent_warnings_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Sudden Warnings and Cautionary Shouts in Spoken Audio",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal cautions, urgent entreaties, and warnings shouted in noisy public environments (traffic, construction, icy sidewalks).",
            "communicativeOutcome": "Instantly react to spoken cautions ('Болгоомжтой!', 'Битгий гишгээрэй!') and extract the hazard described.",
            "objectivesIntroduced": ["obj_a1_60_06_parse_warning_audio"],
            "objectivesPracticed": ["obj_a1_60_01_form_prohibitive_bitgii"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_verb_prohibitive_bitgii",
                "gram_a1_verb_urging_optative_aach"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_health_safety_rules"],
            "previousVocabularyReused": ["болгоомжтой", "битгий", "хүрэх", "унаарай", "хараарай"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 sudden audio alerts and identify the physical hazard and prohibited action in each clip.",
            "writingObjective": "Transcribe the imperative and prohibitive phrases heard in each warning.",
            "spokenProductionObjective": None,
            "registerTarget": "Urgent colloquial alert standard",
            "pragmaticTarget": "Immediate auditory hazard recognition and compliance response.",
            "prerequisiteLessonIds": ["les_a1_60_03_safety_rules_and_reminders_guided_drills"],
            "reviewsLessonIds": ["les_a1_60_02_urging_optative_aach_and_jussive_g"],
            "reviewsUnitIds": ["unit_a1_60_prohibitive_imperative_the_particle"],
            "reviewReason": "Zero-vocabulary auditory lab training acoustic recognition of rapid warnings.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic urgent audio with environmental sound effects (slipping, traffic horn).",
            "successCriteria": [
                "Identify 4 specific hazards from rapid spoken cautions.",
                "Transcribe 'битгий' constructions with correct spelling."
            ],
            "masteryEvidence": [
                "Scores 100% on the acoustic hazard identification test.",
                "Distinguishes between general advice and immediate physical danger."
            ],
            "recommendedExerciseModalities": ["hazard_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_60_06_laboratory_tour_briefing_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Conducting a Site Tour and Enforcing Guidelines",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate guiding a new visitor through a sensitive workplace or museum: showing exhibits, giving affirmative guidance, warning about restricted areas, and asking earnest cooperation.",
            "communicativeOutcome": "Conduct a fluid, authoritative yet courteous tour dialogue balancing permissions with prohibitions.",
            "objectivesIntroduced": ["obj_a1_60_07_conduct_tour_briefing"],
            "objectivesPracticed": [
                "obj_a1_60_01_form_prohibitive_bitgii",
                "obj_a1_60_02_form_urging_optative_aach",
                "obj_a1_60_04_deliver_safety_instructions"
            ],
            "objectivesReviewed": ["obj_a1_59_06_conduct_future_plans_interview"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_verb_prohibitive_bitgii",
                "gram_a1_verb_urging_optative_aach",
                "gram_a1_verb_jussive_third_person_g"
            ],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_22_polite_requests_instructions"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_health_safety_rules", "lex_a1_public_services_amenities"],
            "previousVocabularyReused": ["битгий", "ороорой", "үзээрэй", "дуугүй", "баярлалаа", "за"],
            "readingObjective": "Read simulated site map with restricted zones.",
            "listeningObjective": "Comprehend visitor questions regarding what they may photograph or touch.",
            "writingObjective": "Draft a 4-bullet site protocol card summarizing the rules given during the tour.",
            "spokenProductionObjective": "Execute an 8-turn guide-visitor interaction enforcing rules and answering questions courteously.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Firm yet respectful interpersonal diplomacy enforcing rules smoothly.",
            "prerequisiteLessonIds": [
                "les_a1_60_04_museum_and_library_notices_reading",
                "les_a1_60_05_urgent_warnings_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_60_03_safety_rules_and_reminders_guided_drills"],
            "reviewsUnitIds": ["unit_a1_60_prohibitive_imperative_the_particle"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 60 prohibitive skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating professional site tour etiquette.",
            "successCriteria": [
                "Issue at least 2 polite prohibitions ('Битгий ... -аарай') and 2 affirmative permissions.",
                "Respond to visitor queries politely without hesitation."
            ],
            "masteryEvidence": [
                "Completes site tour dialogue in under 2 minutes with flawless etiquette.",
                "Both partners demonstrate command of prohibitive and imperative distinctions."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "site_tour_simulation", "protocol_logging"]
        }
    ])

    # =========================================================================
    # UNIT 61: Spatial Postpositions: Дээр, Доор, Дотор, Гадаа (pos 61)
    # 6 Lessons | Targets: ProdLem=19, RecLem=7, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,2,1,1), (4,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[61]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_61_01_spatial_postpositions_deer_door_dotor_gadaa",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "On, Under, Inside, and Outside: Дээр, Доор, Дотор, and Гадаа",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce primary spatial postpositions taking base or genitive noun complements: дээр 'on/above', доор 'under/below', дотор 'inside', гадаа 'outside', and contrast them with simple case suffixes.",
            "communicativeOutcome": "Locate household items, furniture, and persons relative to surfaces and enclosures (e.g. 'Ширээн дээр ном байна', 'Гэрийн гадаа морь байна').",
            "objectivesIntroduced": ["obj_a1_61_01_form_spatial_postpositions"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_54_02_form_genitive_possession"],
            "grammarIntroduced": ["gram_a1_spatial_postpositions_deeree_door"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_genitive_possession"],
            "grammarReinforced": ["gram_a1_case_genitive_possession"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_physical_objects_locations"],
            "previousVocabularyReused": ["дээр", "доор", "дотор", "гадаа", "ширээ", "гэр"],
            "readingObjective": "Read room diagrams and furniture placement inventories.",
            "listeningObjective": "Hear spatial postpositions pinpointing exact locations of misplaced personal objects.",
            "writingObjective": "Write 4 sentences describing where objects are located relative to a desk, chair, box, and ger.",
            "spokenProductionObjective": "State aloud where your notebook and pen are located using postpositions.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Precise spatial navigation and physical object localization.",
            "prerequisiteLessonIds": ["les_a1_60_06_laboratory_tour_briefing_synthesis"],
            "reviewsLessonIds": ["les_a1_54_01_nuclear_kinship_and_genitive_possession"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Combine genitive noun modifiers with spatial postpositions (гэрийн гадаа, ширээний доор).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of postposition long vowels (дээр, доор).",
            "successCriteria": [
                "Select 'дээр' for surface contact and 'дотор' for three-dimensional containment.",
                "Use 'гадаа' for exterior location without adding redundant locative suffixes."
            ],
            "masteryEvidence": [
                "Produces 'Түлхүүр ширээн дээр байна' without hesitation.",
                "Draws correct item positions from 4 verbal prompts."
            ],
            "recommendedExerciseModalities": ["spatial_matching", "diagram_drawing", "cued_production"]
        },
        {
            "lessonId": "les_a1_61_02_oblique_personal_pronoun_stems_nadad_chamd",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "To Me, To You: Oblique Pronoun Stems Надад, Чамд, Түүнд, and Бидэнд",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce the suppletive oblique personal pronoun stems and their case forms: надад/надаас/намайг (from би), чамд/чамаас/чамайг (from чи), түүнд/түүнээс/түүнийг (from тэр), бидэнд (from бид).",
            "communicativeOutcome": "Address actions toward personal pronouns as indirect objects, recipients, and sources (e.g. 'Надад өгөөч', 'Чамд баярлалаа').",
            "objectivesIntroduced": ["obj_a1_61_02_form_oblique_pronoun_stems"],
            "objectivesPracticed": ["obj_a1_61_01_form_spatial_postpositions"],
            "objectivesReviewed": ["obj_a1_55_01_form_possessive_pronouns"],
            "grammarIntroduced": ["gram_a1_pronouns_personal_oblique_stems"],
            "grammarPracticed": ["gram_a1_spatial_postpositions_deeree_door"],
            "grammarReviewed": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "grammarReinforced": ["gram_a1_possessive_pronouns_minii_chiniih"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_ownership_possession"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_friends_social_life"],
            "previousVocabularyReused": ["надад", "чамд", "түүнд", "өгөх", "хэлэх"],
            "readingObjective": "Read personal messages and notes expressing gratitude and giving instructions.",
            "listeningObjective": "Comprehend speakers addressing requests to specific individuals using oblique pronouns.",
            "writingObjective": "Draft 4 sentences using 'надад', 'чамд', and 'түүнд' as recipients.",
            "spokenProductionObjective": "Ask a friend politely to hand something to you ('Надад өгөөч') aloud.",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Accurate pronominal targeting in reciprocal interpersonal exchanges.",
            "prerequisiteLessonIds": ["les_a1_61_01_spatial_postpositions_deer_door_dotor_gadaa"],
            "reviewsLessonIds": ["les_a1_55_01_personal_vs_collective_possessive_pronouns"],
            "reviewsUnitIds": ["unit_a1_55_possessive_pronouns_"],
            "reviewReason": "Contrast nominative/genitive pronouns (би/миний) with oblique dative forms (надад).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational cadence directing objects between speakers.",
            "successCriteria": [
                "Select 'надад' (not 'бид') for 'to me' and 'чамд' (not 'чид') for 'to you'.",
                "Combine oblique pronouns with request imperatives fluently."
            ],
            "masteryEvidence": [
                "Produces 'Энэ номыг надад өгөөч' with authentic prosody.",
                "Selects correct pronoun form in a 6-item case declension quiz."
            ],
            "recommendedExerciseModalities": ["pronoun_declension_matrix", "request_completion", "roleplay"]
        },
        {
            "lessonId": "les_a1_61_03_ger_layout_and_household_orientation_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Ger Layout, Khoimor, and Traditional Spatial Orientation",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate spatial descriptions within traditional and modern living quarters: хоймор 'honorific rear/north', баруун тал 'west/right side', зүүн тал 'east/left side', үүд 'entrance/south', and placement of household items.",
            "communicativeOutcome": "Explain room layouts, describe traditional ger seating etiquette, and direct visitors to specific spaces.",
            "objectivesIntroduced": ["obj_a1_61_03_describe_ger_spatial_layout"],
            "objectivesPracticed": [
                "obj_a1_61_01_form_spatial_postpositions",
                "obj_a1_61_02_form_oblique_pronoun_stems"
            ],
            "objectivesReviewed": ["obj_a1_53_01_receive_traditional_hospitality"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_spatial_postpositions_deeree_door",
                "gram_a1_pronouns_personal_oblique_stems"
            ],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_04_thanking_and_apologizing"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_culture_traditions"],
            "previousVocabularyReused": ["гэр", "хоймор", "баруун", "зүүн", "үүд", "суух"],
            "readingObjective": "Read cultural diagrams explaining seating zones and sacred spaces inside a traditional Mongolian ger.",
            "listeningObjective": "Comprehend hosts inviting guests to sit in the honorific rear area (хоймор).",
            "writingObjective": "Write 4 sentences describing the location of furniture inside a ger or apartment room.",
            "spokenProductionObjective": "Direct a guest where to sit and place their coat using spatial terms aloud.",
            "registerTarget": "Courteous traditional respectful",
            "pragmaticTarget": "Adherence to spatial decorum and traditional host-guest positioning.",
            "prerequisiteLessonIds": ["les_a1_61_02_oblique_personal_pronoun_stems_nadad_chamd"],
            "reviewsLessonIds": ["les_a1_53_01_hospitality_arrival_and_greeting_protocol"],
            "reviewsUnitIds": ["unit_a1_53_hospitality_protocol_receiving_food"],
            "reviewReason": "Combine hospitality greetings with traditional ger spatial orientation.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm host voice directing guests with respectful spatial terminology.",
            "successCriteria": [
                "Identify хоймор as the north/rear place of honor.",
                "Locate items using 'баруун талд' (on the right) and 'зүүн талд' (on the left)."
            ],
            "masteryEvidence": [
                "Executes a guest seating roleplay smoothly and respectfully.",
                "Draws a ger interior labeling all 4 cardinal zones correctly."
            ],
            "recommendedExerciseModalities": ["ger_diagram_labeling", "guest_seating_simulation", "cued_production"]
        },
        {
            "lessonId": "les_a1_61_04_interior_design_and_apartment_tours_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Apartment Floor Plans and Rental Listings",
            "lessonType": "reading_development",
            "primaryPurpose": "Read 80-word apartment rental descriptions and furniture floor plans detailing room dimensions, balcony positions, and kitchen appliances.",
            "communicativeOutcome": "Extract room counts, furniture placements, window orientations, and rental amenities from property listings.",
            "objectivesIntroduced": ["obj_a1_61_04_read_apartment_listings"],
            "objectivesPracticed": [
                "obj_a1_61_01_form_spatial_postpositions",
                "obj_a1_61_03_describe_ger_spatial_layout"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_spatial_postpositions_deeree_door"],
            "grammarReviewed": ["gram_a1_case_comitative_possession_predicates"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["байр", "өрөө", "тагт", "гал тогоо", "цэвэрхэн"],
            "readingObjective": "Read a 2-room apartment rental advertisement describing balcony view, furniture included, and floor location.",
            "listeningObjective": None,
            "writingObjective": "List 4 key features and furniture items included in the listed apartment.",
            "spokenProductionObjective": None,
            "registerTarget": "Real estate commercial listing standard",
            "pragmaticTarget": "Evaluating housing options and spatial accommodations from written texts.",
            "prerequisiteLessonIds": ["les_a1_61_03_ger_layout_and_household_orientation_drills"],
            "reviewsLessonIds": ["les_a1_61_01_spatial_postpositions_deer_door_dotor_gadaa"],
            "reviewsUnitIds": ["unit_a1_61_spatial_postpositions_"],
            "reviewReason": "Consolidate written recognition of spatial postpositions in housing descriptions.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Professional real estate agent voice reading property listings.",
            "successCriteria": [
                "Identify how many rooms and what furniture is included.",
                "Extract spatial postpositional relationships (e.g. 'цонхны доор')."
            ],
            "masteryEvidence": [
                "Answers 4 property listing comprehension questions with 100% accuracy.",
                "Fills out an apartment comparison checklist without error."
            ],
            "recommendedExerciseModalities": ["listing_scanning", "furniture_inventory", "short_answer"]
        },
        {
            "lessonId": "les_a1_61_05_locating_lost_items_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Rapid Search Directions for Misplaced Items",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid verbal instructions directing someone where to find keys, glasses, or documents inside a cluttered room or office.",
            "communicativeOutcome": "Accurately pinpoint object locations based on fast spatial audio descriptions.",
            "objectivesIntroduced": ["obj_a1_61_05_parse_spatial_directions_audio"],
            "objectivesPracticed": ["obj_a1_61_01_form_spatial_postpositions"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_spatial_postpositions_deeree_door",
                "gram_a1_pronouns_personal_oblique_stems"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_physical_objects_locations"],
            "previousVocabularyReused": ["дээр", "доор", "дотор", "ард", "урд", "хаана"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 phone audio clips where a roommate directs the listener to find 4 misplaced items.",
            "writingObjective": "Write down the exact location of each item based on the audio.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard hurried conversational",
            "pragmaticTarget": "Auditory precision parsing rapid spatial prepositions and oblique pronouns under time pressure.",
            "prerequisiteLessonIds": ["les_a1_61_03_ger_layout_and_household_orientation_drills"],
            "reviewsLessonIds": ["les_a1_61_02_oblique_personal_pronoun_stems_nadad_chamd"],
            "reviewsUnitIds": ["unit_a1_61_spatial_postpositions_"],
            "reviewReason": "Zero-vocabulary auditory lab training spatial postposition perception in fast speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic hurried phone audio looking for misplaced keys and tickets.",
            "successCriteria": [
                "Identify exact locations of all 4 misplaced objects.",
                "Distinguish between 'дээр' (on top of) and 'доор' (underneath) in rapid audio."
            ],
            "masteryEvidence": [
                "Scores 100% on the item localization listening test.",
                "Locates all items on a room graphic without error."
            ],
            "recommendedExerciseModalities": ["audio_map_search", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_61_06_arranging_the_room_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Rearranging Furniture and Organizing the Home",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate moving into a new apartment or rearranging a ger: discussing where the desk, bed, bookshelf, and stove should go, giving mutual directions, and finalizing the layout.",
            "communicativeOutcome": "Conduct a fluid, collaborative domestic planning dialogue organizing physical space effectively.",
            "objectivesIntroduced": ["obj_a1_61_06_coordinate_room_arrangement"],
            "objectivesPracticed": [
                "obj_a1_61_01_form_spatial_postpositions",
                "obj_a1_61_02_form_oblique_pronoun_stems",
                "obj_a1_61_03_describe_ger_spatial_layout"
            ],
            "objectivesReviewed": ["obj_a1_60_06_laboratory_tour_briefing_synthesis"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_spatial_postpositions_deeree_door",
                "gram_a1_pronouns_personal_oblique_stems"
            ],
            "grammarReviewed": ["gram_a1_verb_volitional_intention_ya", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_verb_volitional_intention_ya"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_greetings_and_farewells"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_physical_objects_locations"],
            "previousVocabularyReused": ["ширээ", "ор", "цонх", "дээр", "доор", "баруун", "зүүн", "тавих"],
            "readingObjective": "Read empty floor plan layout cards.",
            "listeningObjective": "Comprehend partner proposals for where to place heavy furniture items.",
            "writingObjective": "Draft a finalized room inventory checklist indicating where each piece of furniture was placed.",
            "spokenProductionObjective": "Execute an 8-turn room arranging conversation reaching consensus on furniture positions.",
            "registerTarget": "Courteous standard friendly collaborative",
            "pragmaticTarget": "Seamless peer collaboration in organizing domestic physical environments.",
            "prerequisiteLessonIds": [
                "les_a1_61_04_interior_design_and_apartment_tours_reading",
                "les_a1_61_05_locating_lost_items_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_61_03_ger_layout_and_household_orientation_drills"],
            "reviewsUnitIds": ["unit_a1_61_spatial_postpositions_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 61 spatial skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating collaborative room organization.",
            "successCriteria": [
                "Use spatial postpositions in every turn describing placement.",
                "Propose positions using volitional and polite imperative forms smoothly."
            ],
            "masteryEvidence": [
                "Completes room arrangement dialogue in under 2 minutes fluently.",
                "Both partners produce identical floor plan sketches from the conversation."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "furniture_placement_simulation", "floorplan_sketching"]
        }
    ])

    # =========================================================================
    # UNIT 62: Weather, Temperatures & Seasonal Sensations (pos 62)
    # 6 Lessons | Targets: ProdLem=21, RecLem=8, ProdExp=4, RecExp=2
    # Budget: (6,2,1,1), (5,2,1,0), (5,2,1,1), (5,2,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[62]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_62_01_weather_phenomena_and_temperatures",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Sun, Rain, Snow, and Degrees: Нар, Бороо, Цас, and Градус",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce core meteorological vocabulary (нар 'sun', бороо 'rain', цас 'snow', салхи 'wind', хүйтэн 'cold', халуун 'hot', дулаан 'warm', сэрүүн 'cool') and temperature reports using 'градус' with positive/negative numbers.",
            "communicativeOutcome": "Describe daily weather conditions, read thermometers, and state temperatures (e.g. 'Өнөөдөр цас орж байна, хасах арван таван градус').",
            "objectivesIntroduced": ["obj_a1_62_01_describe_weather_conditions", "obj_a1_62_02_report_temperatures"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_57_01_form_progressive_aspect_j_baina"],
            "grammarIntroduced": ["gram_a1_case_ablative_comparative"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_verb_aspect_progressive_j_baina"],
            "grammarReinforced": ["gram_a1_verb_aspect_progressive_j_baina"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_nature_weather_environment"],
            "previousVocabularyReused": ["цаг агаар", "хүйтэн", "халуун", "өнөөдөр", "байна"],
            "readingObjective": "Read weather forecast icons and temperature displays on mobile apps.",
            "listeningObjective": "Hear daily weather forecasts detailing precipitation and temperature highs/lows.",
            "writingObjective": "Write 4 sentences describing today's weather and temperature in Ulaanbaatar and provincial centers.",
            "spokenProductionObjective": "State what the weather is like today outside your window aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Accurate meteorological observation and dressing appropriately for climate conditions.",
            "prerequisiteLessonIds": ["les_a1_61_06_arranging_the_room_synthesis"],
            "reviewsLessonIds": ["les_a1_57_01_progressive_aspect_j_baina_formation"],
            "reviewsUnitIds": ["unit_a1_57_ongoing_progressive_aspect_verbal_s"],
            "reviewReason": "Combine meteorological nouns with progressive precipitation verbs (бороо орж байна, цас орж байна).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear meteorological broadcast delivery style.",
            "successCriteria": [
                "Use 'нэмэх' (plus) and 'хасах' (minus) accurately with temperature figures.",
                "Pair 'орж байна' with precipitation nouns (бороо, цас)."
            ],
            "masteryEvidence": [
                "Produces 'Өнөөдөр нартай, дулаахан байна' fluently.",
                "Extracts high/low temperatures correctly from a forecast graphic."
            ],
            "recommendedExerciseModalities": ["weather_matching", "forecast_reading", "cued_production"]
        },
        {
            "lessonId": "les_a1_62_02_comparative_weather_with_ablative_aasaa",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Colder Than Yesterday: Comparative Weather with Ablative -аас/-ээс",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce the comparative construction using the ablative case -аас/-ээс/-оос/-өөс ('[Noun]-аас илүү хүйтэн' / '[Noun]-аас дулаан' - colder/warmer than X) and demonstrative pronoun case declensions (үүнээс, түүнээс).",
            "communicativeOutcome": "Compare weather across days, cities, and seasons (e.g. 'Өнөөдөр өчигдрөөс хүйтэн байна', 'Улаанбаатар Дарханаас хүйтэн').",
            "objectivesIntroduced": ["obj_a1_62_03_form_comparative_ablative"],
            "objectivesPracticed": ["obj_a1_62_01_describe_weather_conditions"],
            "objectivesReviewed": ["obj_a1_40_01_form_ablative_origin"],
            "grammarIntroduced": [
                "gram_a1_pronouns_demonstrative_case_declension",
                "gram_a1_interrogatives_case_declension"
            ],
            "grammarPracticed": ["gram_a1_case_ablative_comparative"],
            "grammarReviewed": ["gram_a1_case_ablative_source_origin"],
            "grammarReinforced": ["gram_a1_case_ablative_source_origin"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_nature_weather_environment"],
            "previousVocabularyReused": ["өчигдөр", "өнөөдөр", "илүү", "хот", "хүйтэн"],
            "readingObjective": "Read comparative weather charts ranking the coldest and warmest aimags.",
            "listeningObjective": "Comprehend weather reporters comparing this winter's temperatures to last year's averages.",
            "writingObjective": "Draft 3 comparative sentences contrasting temperatures between two cities.",
            "spokenProductionObjective": "Explain to a peer that today is much colder than yesterday aloud.",
            "registerTarget": "Everyday standard conversational",
            "pragmaticTarget": "Clear analytical comparison of environmental conditions.",
            "prerequisiteLessonIds": ["les_a1_62_01_weather_phenomena_and_temperatures"],
            "reviewsLessonIds": ["les_a1_40_01_ablative_spatial_origin"],
            "reviewsUnitIds": ["unit_a1_40_ablative_of_spatial_temporal_origin"],
            "reviewReason": "Extend spatial ablative case (-аас) to comparative degrees of adjectives.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural conversational comparison prosody highlighting differences.",
            "successCriteria": [
                "Attach correct ablative allomorph to comparison standard noun.",
                "Structure '[Item A] [Item B]-аас [Adjective]' without word-order distortion."
            ],
            "masteryEvidence": [
                "Produces 'Энэ өвөл өнгөрсөн жилээс хүйтэн байна' accurately.",
                "Compares 4 regional climates correctly on a worksheet."
            ],
            "recommendedExerciseModalities": ["comparative_drills", "climate_comparison_matrix", "roleplay"]
        },
        {
            "lessonId": "les_a1_62_03_four_seasons_and_clothing_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Four Seasons, Seasonal Clothing, and Daily Sensation",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate discussions of the four seasons (хавар 'spring', зун 'summer', намар 'autumn', өвөл 'winter'), seasonal sensations (даарах 'to feel cold', халууцах 'to feel hot'), and dressing appropriately (дулаан хувцаслаарай).",
            "communicativeOutcome": "Describe seasons, express bodily sensations of heat/cold, and advise others on suitable attire.",
            "objectivesIntroduced": ["obj_a1_62_04_discuss_seasons_and_clothing"],
            "objectivesPracticed": [
                "obj_a1_62_01_describe_weather_conditions",
                "obj_a1_62_03_form_comparative_ablative"
            ],
            "objectivesReviewed": ["obj_a1_60_01_form_prohibitive_bitgii"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_ablative_comparative"],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsReviewed": ["comm_a1_22_polite_requests_instructions"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_nature_weather_environment", "lex_a1_shopping_clothing"],
            "previousVocabularyReused": ["өвөл", "зун", "хавар", "намар", "хувцас", "өмсөх"],
            "readingObjective": "Read seasonal advice columns recommending winter gear and summer sun protection.",
            "listeningObjective": "Comprehend elders warning youth to bundle up warmly because the wind is biting.",
            "writingObjective": "Write 4 recommendations for what to wear during each of the four seasons in Mongolia.",
            "spokenProductionObjective": "Advise a partner to dress warmly because it is minus 25 degrees outside.",
            "registerTarget": "Courteous caring standard",
            "pragmaticTarget": "Showing interpersonal care and practical survival advice in extreme weather.",
            "prerequisiteLessonIds": ["les_a1_62_02_comparative_weather_with_ablative_aasaa"],
            "reviewsLessonIds": ["les_a1_60_01_prohibitive_particle_bitgii"],
            "reviewsUnitIds": ["unit_a1_60_prohibitive_imperative_the_particle"],
            "reviewReason": "Combine polite imperatives and prohibitions with seasonal health advice ('Битгий нимгэн яв, дулаан хувцаслаарай').",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm, caring parental voice offering practical weather advice.",
            "successCriteria": [
                "Name all four seasons accurately.",
                "Express personal physical sensation ('Би даарч байна', 'Би халууцаж байна')."
            ],
            "masteryEvidence": [
                "Produces 'Гадаа маш хүйтэн байна, дулаан малгай өмсөөрэй' fluently.",
                "Matches seasons to appropriate clothing sets correctly."
            ],
            "recommendedExerciseModalities": ["seasonal_matching", "advice_formulation", "roleplay"]
        },
        {
            "lessonId": "les_a1_62_04_meteorological_reports_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: National Weather Bulletins and Seasonal Forecasts",
            "lessonType": "reading_development",
            "primaryPurpose": "Read 80-word official National Meteorological Agency weather bulletins detailing regional storm alerts, wind speeds, and temperature drops across the country.",
            "communicativeOutcome": "Understand official storm warnings, road condition alerts, and regional weather forecasts in print and online media.",
            "objectivesIntroduced": ["obj_a1_62_05_read_weather_bulletins"],
            "objectivesPracticed": [
                "obj_a1_62_01_describe_weather_conditions",
                "obj_a1_62_02_report_temperatures"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_ablative_comparative"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_nature_weather_environment"],
            "previousVocabularyReused": ["цаг агаар", "мэдээ", "салхи", "шуурга", "зам"],
            "readingObjective": "Read a national weather bulletin reporting an incoming blizzard in eastern aimags.",
            "listeningObjective": None,
            "writingObjective": "List the affected aimags, expected temperature drops, and cautionary advice from the bulletin.",
            "spokenProductionObjective": None,
            "registerTarget": "Official meteorological broadcast standard",
            "pragmaticTarget": "Interpreting critical public safety meteorological alerts.",
            "prerequisiteLessonIds": ["les_a1_62_03_four_seasons_and_clothing_guided_drills"],
            "reviewsLessonIds": ["les_a1_62_01_weather_phenomena_and_temperatures"],
            "reviewsUnitIds": ["unit_a1_62_weather_temperatures_seasonal_sensa"],
            "reviewReason": "Consolidate written recognition of weather terminology in official reports.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Professional broadcast announcer reading national weather bulletin.",
            "successCriteria": [
                "Extract wind velocity and snowfall predictions accurately.",
                "Identify which road routes are cautioned against travel."
            ],
            "masteryEvidence": [
                "Answers 4 bulletin reading comprehension questions with 100% accuracy.",
                "Fills out a regional forecast summary table correctly."
            ],
            "recommendedExerciseModalities": ["bulletin_scanning", "hazard_extraction", "short_answer"]
        },
        {
            "lessonId": "les_a1_62_05_radio_forecast_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Rapid Radio and TV Weather Broadcasts",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse fast professional weather broadcasts on radio and television featuring rapid numerical listings of temperatures and weather conditions across all Mongolian regions.",
            "communicativeOutcome": "Accurately record temperatures and weather phenomena across different aimags from spoken media.",
            "objectivesIntroduced": ["obj_a1_62_06_parse_weather_broadcasts_audio"],
            "objectivesPracticed": ["obj_a1_62_01_describe_weather_conditions"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_ablative_comparative"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_nature_weather_environment"],
            "previousVocabularyReused": ["градус", "хүйтэн", "цас", "бороо", "шөнөдөө", "өдөртөө"],
            "readingObjective": None,
            "listeningObjective": "Listen to a 1-minute national radio weather report and record daytime and nighttime temperatures for 4 aimag capitals.",
            "writingObjective": "Transcribe the weather adjectives and degree figures heard in each region.",
            "spokenProductionObjective": None,
            "registerTarget": "Media broadcast journalistic standard",
            "pragmaticTarget": "Auditory tracking of rapid numeric meteorological data in connected media speech.",
            "prerequisiteLessonIds": ["les_a1_62_03_four_seasons_and_clothing_guided_drills"],
            "reviewsLessonIds": ["les_a1_62_02_comparative_weather_with_ablative_aasaa"],
            "reviewsUnitIds": ["unit_a1_62_weather_temperatures_seasonal_sensa"],
            "reviewReason": "Zero-vocabulary auditory lab training weather broadcast acoustic perception.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic fast-paced radio weather report with signature jingle.",
            "successCriteria": [
                "Accurately record all daytime and nighttime temperatures without confusing positive and negative degree readings.",
                "Identify regions experiencing snow vs clear skies correctly."
            ],
            "masteryEvidence": [
                "Scores 100% on the weather forecast listening test.",
                "Transcribes all numeric temperatures and conditions without error."
            ],
            "recommendedExerciseModalities": ["audio_map_population", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_62_06_travel_packing_and_weather_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Weather Debrief and Travel Packing Consultation",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate consulting a friend before an upcoming trip to the countryside: checking the regional forecast, comparing it with the capital, and agreeing on what warm clothes and gear to pack.",
            "communicativeOutcome": "Conduct a fluid, practical weather consultation dialogue ensuring proper travel preparation.",
            "objectivesIntroduced": ["obj_a1_62_07_consult_travel_weather_packing"],
            "objectivesPracticed": [
                "obj_a1_62_01_describe_weather_conditions",
                "obj_a1_62_02_report_temperatures",
                "obj_a1_62_03_form_comparative_ablative",
                "obj_a1_62_04_discuss_seasons_and_clothing"
            ],
            "objectivesReviewed": ["obj_a1_61_06_coordinate_room_arrangement"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_ablative_comparative",
                "gram_a1_pronouns_demonstrative_case_declension"
            ],
            "grammarReviewed": ["gram_a1_verb_imperative_polite_aarai", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_verb_imperative_polite_aarai"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_31_weather_seasons_basic"],
            "communicativeFunctionsReviewed": ["comm_a1_22_polite_requests_instructions"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_nature_weather_environment", "lex_a1_shopping_clothing"],
            "previousVocabularyReused": ["цаг агаар", "градус", "хүйтэн", "дулаан", "хувцас", "авах", "баярлалаа"],
            "readingObjective": "Read countryside regional forecast prompt cards.",
            "listeningObjective": "Comprehend partner inquiries regarding what the weather is forecasted to be like in the destination province.",
            "writingObjective": "Draft a finalized 5-item weather-appropriate packing list based on the dialogue.",
            "spokenProductionObjective": "Execute an 8-turn travel weather consultation comparing temperatures and agreeing on packing items.",
            "registerTarget": "Courteous standard friendly collaborative",
            "pragmaticTarget": "Practical mutual consultation ensuring personal safety and preparedness in cold weather.",
            "prerequisiteLessonIds": [
                "les_a1_62_04_meteorological_reports_reading",
                "les_a1_62_05_radio_forecast_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_62_03_four_seasons_and_clothing_guided_drills"],
            "reviewsUnitIds": ["unit_a1_62_weather_temperatures_seasonal_sensa"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 62 weather skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating travel weather consultation.",
            "successCriteria": [
                "Compare temperatures between two locations using comparative ablative (-аас).",
                "Recommend specific clothing items using polite imperatives."
            ],
            "masteryEvidence": [
                "Completes travel packing dialogue in under 2 minutes without grammatical hesitation.",
                "Both partners draft identical packing lists suited to the simulated destination climate."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "weather_consultation", "packing_list_creation"]
        }
    ])

    # =========================================================================
    # UNIT 63: A1 Capstone: Family Story & Living Environment (pos 63)
    # 6 Lessons | Targets: ProdLem=20, RecLem=8, ProdExp=6, RecExp=3
    # Budget: (5,2,2,1), (5,2,2,1), (5,2,1,1), (5,2,1,0), (0,0,0,0), (0,0,0,0)
    # Lesson 6 is the A1 STAGE FINAL CERTIFICATION CAPSTONE CHECKPOINT!
    # =========================================================================
    u = u_map[63]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_63_01_my_hometown_and_origins_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "A1 Capstone 1: My Hometown, Ancestral Roots, and Landscape",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Synthesize descriptive vocabulary for hometowns, natural landscapes (уул, гол, тал, нуур), and ancestral origins ('Манай аавын нутаг Завханд байдаг') combining genitive, ablative, and spatial markers.",
            "communicativeOutcome": "Deliver an expressive, structured oral and written description of one's hometown and ancestral origin.",
            "objectivesIntroduced": ["obj_a1_63_01_synthesize_hometown_origins"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_62_01_describe_weather_conditions"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_genitive_possession",
                "gram_a1_case_ablative_source_origin",
                "gram_a1_spatial_postpositions_deeree_door"
            ],
            "grammarReviewed": ["gram_a1_case_comitative_possession_predicates"],
            "grammarReinforced": ["gram_a1_case_comitative_possession_predicates"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_nature_weather_environment", "lex_a1_kinship_family"],
            "previousVocabularyReused": ["нутаг", "уул", "гол", "тал", "сайхан", "амьдрах"],
            "readingObjective": "Read illustrated cultural essays about Mongolian aimags and homeland pride.",
            "listeningObjective": "Comprehend speakers describing their birthplace and natural surroundings with warmth.",
            "writingObjective": "Write a 5-sentence descriptive paragraph about your hometown and its landscape.",
            "spokenProductionObjective": "Present your hometown, its geographical features, and climate aloud.",
            "registerTarget": "Expressive standard neutral",
            "pragmaticTarget": "Communicating cultural affinity with land, lineage, and geographic origins.",
            "prerequisiteLessonIds": ["les_a1_62_06_travel_packing_and_weather_synthesis"],
            "reviewsLessonIds": ["les_a1_62_01_weather_phenomena_and_temperatures"],
            "reviewsUnitIds": ["unit_a1_62_weather_temperatures_seasonal_sensa"],
            "reviewReason": "Integrate weather and environmental descriptors with ancestral hometown narratives.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm, poetic voice describing the open beauty of the Mongolian countryside.",
            "successCriteria": [
                "Combine geographical landscape nouns with spatial postpositions effortlessly.",
                "Express ancestral connection using '[Relative]-ын нутаг' accurately."
            ],
            "masteryEvidence": [
                "Delivers a 1-minute hometown presentation without pause.",
                "Produces well-formed sentences linking physical geography with family history."
            ],
            "recommendedExerciseModalities": ["hometown_profile", "photo_narration", "cued_production"]
        },
        {
            "lessonId": "les_a1_63_02_three_generations_family_narrative",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "A1 Capstone 2: Three Generations - Grandparents, Parents, and Children",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Synthesize three-generation family narratives (өвөө, эмээ, аав, ээж, хүүхдүүд, ач, зээ) integrating past accomplishments (-сан), ongoing occupations (-ж байна), and ages.",
            "communicativeOutcome": "Narrate an extensive family history spanning three generations with chronological and relational clarity.",
            "objectivesIntroduced": ["obj_a1_63_02_synthesize_multigenerational_family"],
            "objectivesPracticed": ["obj_a1_63_01_synthesize_hometown_origins"],
            "objectivesReviewed": ["obj_a1_58_01_form_perfective_past_san"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_case_genitive_possession",
                "gram_a1_verb_tense_past_perfective_san",
                "gram_a1_verb_aspect_progressive_j_baina"
            ],
            "grammarReviewed": ["gram_a1_case_dative_locative_recipient"],
            "grammarReinforced": ["gram_a1_case_dative_locative_recipient"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": ["comm_a1_16_family_size_marital_status"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_professions_occupations"],
            "previousVocabularyReused": ["өвөө", "эмээ", "аав", "ээж", "нас", "ажилласан", "хийж байна"],
            "readingObjective": "Read a multi-generational family portrait biography spanning 1950 to the present.",
            "listeningObjective": "Comprehend an elder recounting the life paths and professions of their children and grandchildren.",
            "writingObjective": "Draft a structured 6-sentence three-generation genealogy profile.",
            "spokenProductionObjective": "Explain a three-generation family tree aloud in Mongolian smoothly.",
            "registerTarget": "Courteous standard familial",
            "pragmaticTarget": "Deep cultural respect for generational hierarchy and ancestral legacy.",
            "prerequisiteLessonIds": ["les_a1_63_01_my_hometown_and_origins_synthesis"],
            "reviewsLessonIds": ["les_a1_58_01_perfective_past_san_allomorphs"],
            "reviewsUnitIds": ["unit_a1_58_perfective_past_participle_suffixes"],
            "reviewReason": "Combine multigenerational kinship with past perfective life achievements.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm, multigenerational family narrative voice.",
            "successCriteria": [
                "Accurately differentiate agnatic grandchildren (ач) from cognatic grandchildren (зээ).",
                "Weave past accomplishments (-сан) with present activities (-ж байна) cohesively."
            ],
            "masteryEvidence": [
                "Narrates a complete 3-generation family tree without relational confusion.",
                "Produces accurate timeline linking birth years to professions."
            ],
            "recommendedExerciseModalities": ["genealogy_narration", "family_tree_mapping", "roleplay"]
        },
        {
            "lessonId": "les_a1_63_03_daily_life_and_living_space_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "A1 Capstone 3: Daily Life, Household Routines, and Domestic Living Space",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Synthesize descriptions of living spaces (ger/apartment), daily domestic routines (-даг), ongoing household tasks (-ж байна), and spatial arrangements (дээр, доор, дотор, гадаа).",
            "communicativeOutcome": "Deliver a comprehensive overview of home life, describing physical living spaces and daily household patterns.",
            "objectivesIntroduced": ["obj_a1_63_03_synthesize_living_space_routines"],
            "objectivesPracticed": [
                "obj_a1_63_01_synthesize_hometown_origins",
                "obj_a1_63_02_synthesize_multigenerational_family"
            ],
            "objectivesReviewed": ["obj_a1_61_01_form_spatial_postpositions"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_spatial_postpositions_deeree_door",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_present_habitual_dag"
            ],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": ["гэр", "өрөө", "өглөө", "орой", "хийх", "цэвэрлэх", "байх"],
            "readingObjective": "Read an essay by a student describing their daily life in a countryside ger camp.",
            "listeningObjective": "Comprehend a resident giving a virtual tour of their living quarters and domestic routine.",
            "writingObjective": "Write a 6-sentence essay detailing your living space layout and typical day.",
            "spokenProductionObjective": "Give a 1-minute guided oral tour of your home describing rooms and daily activities.",
            "registerTarget": "Everyday standard friendly narrative",
            "pragmaticTarget": "Seamless integration of spatial description with dynamic daily activity narration.",
            "prerequisiteLessonIds": ["les_a1_63_02_three_generations_family_narrative"],
            "reviewsLessonIds": ["les_a1_61_01_spatial_postpositions_deer_door_dotor_gadaa"],
            "reviewsUnitIds": ["unit_a1_61_spatial_postpositions_"],
            "reviewReason": "Combine domestic spatial postpositions with habitual and progressive action verbs.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm, inviting host giving a virtual home tour.",
            "successCriteria": [
                "Describe at least 4 rooms or furniture positions using spatial postpositions.",
                "Contrast habitual morning routines (-даг) with current activities (-ж байна)."
            ],
            "masteryEvidence": [
                "Presents fluent, coherent virtual home tour from memory.",
                "Produces zero errors in verb aspect or spatial postposition selection."
            ],
            "recommendedExerciseModalities": ["home_tour_presentation", "routine_spatial_mapping", "cued_production"]
        },
        {
            "lessonId": "les_a1_63_04_grand_story_integration_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "A1 Capstone 4: Reading the Grand Mongolian Life Story",
            "lessonType": "reading_development",
            "primaryPurpose": "Read an authentic 120-word multi-paragraph life chronicle integrating all core A1 domains: origin, schooling, marriage, children, home environment, weather, and future dreams.",
            "communicativeOutcome": "Demonstrate autonomous reading comprehension of full-length A1 narrative prose.",
            "objectivesIntroduced": ["obj_a1_63_04_read_grand_a1_chronicle"],
            "objectivesPracticed": [
                "obj_a1_63_01_synthesize_hometown_origins",
                "obj_a1_63_02_synthesize_multigenerational_family",
                "obj_a1_63_03_synthesize_living_space_routines"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_verb_tense_past_perfective_san",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_future_prospective_na",
                "gram_a1_case_genitive_possession"
            ],
            "grammarReviewed": ["gram_a1_case_ablative_comparative"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_nature_weather_environment"],
            "previousVocabularyReused": ["төрсөн", "сурсан", "гэрлэсэн", "хүүхэд", "маргааш", "өвөл", "сайхан"],
            "readingObjective": "Read a comprehensive 120-word biographical chronicle of a nomad family living in Arkhangai.",
            "listeningObjective": None,
            "writingObjective": "Complete a 6-question comprehensive reading analysis extracting timeline, family relations, and future plans.",
            "spokenProductionObjective": None,
            "registerTarget": "Full A1 authentic biographical narrative standard",
            "pragmaticTarget": "End-of-stage reading fluency across interconnected narrative paragraphs.",
            "prerequisiteLessonIds": ["les_a1_63_03_daily_life_and_living_space_synthesis"],
            "reviewsLessonIds": ["les_a1_63_01_my_hometown_and_origins_synthesis"],
            "reviewsUnitIds": ["unit_a1_63_a1_capstone_family_story_living_env"],
            "reviewReason": "Consolidate cumulative reading comprehension across the entire A1 grammatical spectrum.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Rich, resonant literary narrative voice reading the capstone life story.",
            "successCriteria": [
                "Extract biographical milestones, seasonal activities, and future goals accurately.",
                "Demonstrate total comprehension without relying on bilingual dictionaries."
            ],
            "masteryEvidence": [
                "Answers all 6 multi-sentence reading comprehension questions with 100% accuracy.",
                "Reconstructs the full family timeline without error."
            ],
            "recommendedExerciseModalities": ["chronicle_scanning", "timeline_synthesis", "short_answer"]
        },
        {
            "lessonId": "les_a1_63_05_capstone_dress_rehearsal_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "A1 Capstone 5: Comprehensive Dress Rehearsal and Acoustic Evaluation",
            "lessonType": "listening_development",
            "primaryPurpose": "Execute an intensive zero-vocabulary capstone dress rehearsal: multi-speaker acoustic evaluations, speed parsing of connected discourse, and self-diagnostic error checks prior to certification.",
            "communicativeOutcome": "Validate auditory comprehension across diverse speakers and rehearse full spoken delivery seamlessly.",
            "objectivesIntroduced": ["obj_a1_63_05_execute_capstone_dress_rehearsal"],
            "objectivesPracticed": [
                "obj_a1_63_01_synthesize_hometown_origins",
                "obj_a1_63_02_synthesize_multigenerational_family",
                "obj_a1_63_03_synthesize_living_space_routines"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_verb_tense_past_perfective_san",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_future_prospective_na",
                "gram_a1_spatial_postpositions_deeree_door"
            ],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_08_describing_daily_routines"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_daily_routines_hobbies"],
            "previousVocabularyReused": [
                "аав", "ээж", "гэр", "ажил", "сургууль", "өчигдөр", "одоо", "маргааш", "хүйтэн"
            ],
            "readingObjective": None,
            "listeningObjective": "Listen to a 2-minute continuous spoken life story and take structured notes on 8 core factual dimensions.",
            "writingObjective": "Transcribe key morphosyntactic pivot phrases linking past, present, and future statements.",
            "spokenProductionObjective": None,
            "registerTarget": "Full A1 multi-speaker connected discourse standard",
            "pragmaticTarget": "Auditory mastery and high-speed processing of natural connected Mongolian speech.",
            "prerequisiteLessonIds": ["les_a1_63_04_grand_story_integration_reading"],
            "reviewsLessonIds": ["les_a1_63_02_three_generations_family_narrative"],
            "reviewsUnitIds": ["unit_a1_63_a1_capstone_family_story_living_env"],
            "reviewReason": "Zero-vocabulary auditory dress rehearsal preparing learner for final stage certification.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Comprehensive multi-speaker audio suite covering the entire A1 communicative repertoire.",
            "successCriteria": [
                "Accurately extract all 8 core factual dimensions from continuous audio without omissions.",
                "Demonstrate immediate comprehension of rapid temporal shifts (өчигдөр -> одоо -> маргааш)."
            ],
            "masteryEvidence": [
                "Scores 100% on the capstone acoustic dress rehearsal test.",
                "Identifies and self-corrects subtle case and tense nuances."
            ],
            "recommendedExerciseModalities": ["audio_fact_extraction", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_63_06_a1_stage_final_certification_checkpoint",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "A1 Stage Final Certification Checkpoint: The Mongolian Life Chronicle",
            "lessonType": "checkpoint",
            "primaryPurpose": "The definitive, authoritative summative certification checkpoint for the entire CEFR A1 Stage (Sections 1-5, Units 14-63). Evaluates comprehensive linguistic, pragmatic, communicative, and cultural competence across: (1) Identity, introductions, courtesy, and nominal clauses; (2) Physical space, quantities, commerce, and locative structures; (3) Daily routines, motion, transport, and temporality; (4) Food, dining, transactions, and hospitality protocol; and (5) Family kinship, possession, living environment, progressive aspect, past achievements, future commitments, and weather.",
            "communicativeOutcome": "Achieve full official CEFR A1 certification in Mongolian: engage in spontaneous survival transactions, present an extended family and life story, navigate physical space, and comprehend authentic everyday spoken and written texts.",
            "objectivesIntroduced": ["obj_a1_63_06_a1_stage_final_certification_mastery"],
            "objectivesPracticed": [
                "obj_a1_63_01_synthesize_hometown_origins",
                "obj_a1_63_02_synthesize_multigenerational_family",
                "obj_a1_63_03_synthesize_living_space_routines",
                "obj_a1_58_06_section_05_mid_mastery",
                "obj_a1_53_05_section_04_capstone_mastery"
            ],
            "objectivesReviewed": [
                "obj_a1_14_01_introduce_self",
                "obj_a1_24_01_ask_price_settle_payment",
                "obj_a1_34_01_tell_time_hours_minutes",
                "obj_a1_45_01_order_traditional_food"
            ],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_a1_nominal_predicate_zero_copula",
                "gram_a1_existential_baina_baihgui",
                "gram_a1_case_accusative_definite",
                "gram_a1_case_dative_locative_location",
                "gram_a1_case_ablative_comparative",
                "gram_a1_case_comitative_possession_predicates",
                "gram_a1_case_genitive_possession",
                "gram_a1_verb_tense_present_habitual_dag",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_past_perfective_san",
                "gram_a1_verb_tense_future_prospective_na",
                "gram_a1_spatial_postpositions_deeree_door"
            ],
            "grammarReviewed": [
                "gram_a1_verb_imperative_polite_aarai",
                "gram_a1_verb_volitional_intention_ya",
                "gram_a1_verb_prohibitive_bitgii",
                "gram_a1_content_questions_be_ve",
                "gram_a1_polar_questions_uu_uu"
            ],
            "grammarReinforced": [
                "gram_a1_case_genitive_possession",
                "gram_a1_verb_tense_past_perfective_san",
                "gram_a1_verb_aspect_progressive_j_baina",
                "gram_a1_verb_tense_future_prospective_na",
                "gram_a1_spatial_postpositions_deeree_door"
            ],
            "phonologyIntroduced": [],
            "phonologyPracticed": [
                "phono_vowel_harmony_suffixes",
                "phono_stress_initial_and_full_vowels",
                "phono_non_initial_reduction",
                "phono_vowel_length_contrast"
            ],
            "phonologyReviewed": [
                "phono_oe_ue_contrast",
                "phono_consonant_voicing_and_nasals"
            ],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_a1_01_greetings_and_farewells",
                "comm_a1_03_introduce_peer_third_party",
                "comm_a1_05_asking_identity_origin",
                "comm_a1_08_describing_daily_routines",
                "comm_a1_10_identifying_objects",
                "comm_a1_11_ownership_possession",
                "comm_a1_15_family_nuclear_members",
                "comm_a1_16_family_size_marital_status",
                "comm_a1_22_polite_requests_instructions",
                "comm_a1_25_restaurant_ordering",
                "comm_a1_31_weather_seasons_basic"
            ],
            "communicativeFunctionsReviewed": [
                "comm_a1_04_thanking_and_apologizing",
                "comm_a1_26_paying_bill_counter",
                "comm_a1_27_open_market_produce_buying"
            ],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_a1_core_social_courtesy",
                "lex_a1_kinship_family",
                "lex_a1_personal_possessions",
                "lex_a1_housing_ger_household",
                "lex_a1_food_beverages",
                "lex_a1_daily_routines_hobbies",
                "lex_a1_nature_weather_environment",
                "lex_a1_travel_transport"
            ],
            "previousVocabularyReused": [
                "сайн байна уу", "баярлалаа", "аав", "ээж", "гэр", "сургууль",
                "хоол", "цай", "өчигдөр", "одоо", "маргааш", "зун", "өвөл", "хүйтэн"
            ],
            "readingObjective": "Read a multi-genre A1 certification portfolio consisting of a personal letter, a weather bulletin, a receipt, and an apartment notice.",
            "listeningObjective": "Comprehend a 3-part authentic audio evaluation: a formal interview, a fast market transaction, and a family narrative.",
            "writingObjective": "Compose a finalized 100-word 'Mongolian Life Chronicle' portfolio essay detailing: (1) self-introduction and origins, (2) family tree and kinship relations, (3) daily routine and home space, (4) completed education and past travels, and (5) upcoming plans and future aspirations.",
            "spokenProductionObjective": "Execute an unscripted 10-minute multi-station oral certification exam: (Station 1) Personal & Family Identity; (Station 2) Market & Dining Transaction; (Station 3) Daily Routines & Living Space; and (Station 4) Life Accomplishments & Future Aspirations.",
            "registerTarget": "Exemplary CEFR A1 comprehensive multi-register competence",
            "pragmaticTarget": "Autonomous, dignified, culturally authentic communicative survival across all standard A1 Mongolian social domains.",
            "prerequisiteLessonIds": [
                "les_a1_63_04_grand_story_integration_reading",
                "les_a1_63_05_capstone_dress_rehearsal_lab"
            ],
            "reviewsLessonIds": [
                "les_a1_58_06_section_05_mid_checkpoint",
                "les_a1_53_05_section_04_capstone_checkpoint",
                "les_a1_63_01_my_hometown_and_origins_synthesis",
                "les_a1_63_02_three_generations_family_narrative",
                "les_a1_63_03_daily_life_and_living_space_synthesis"
            ],
            "reviewsUnitIds": [
                "unit_a1_58_perfective_past_participle_suffixes",
                "unit_a1_53_hospitality_protocol_receiving_food",
                "unit_a1_63_a1_capstone_family_story_living_env"
            ],
            "reviewReason": "The authoritative final certification checkpoint validating complete mastery of the entire CEFR A1 curriculum.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary formal certification audio testing all A1 listening modalities.",
            "successCriteria": [
                "Pass all 4 oral certification stations with cumulative score >=85%.",
                "Demonstrate flawless command of vowel harmony, noun cases, verb tenses, and kinship terms.",
                "Display natural pragmatic etiquette, eye contact, and respectful cultural posture."
            ],
            "masteryEvidence": [
                "Learner produces the 100-word written chronicle without systemic grammatical errors.",
                "Conducts all transactional, social, and narrative oral tasks with fluid autonomous confidence.",
                "Certified as having attained full CEFR A1 Stage Competence in Mongolian."
            ],
            "recommendedExerciseModalities": [
                "certification_oral_exam",
                "portfolio_essay_evaluation",
                "diagnostic_transcription_battery",
                "transactional_simulation_station"
            ]
        }
    ])
'''

with open("scripts/framework_builder/gen_sec05_part2.py", "r") as f:
    cur = f.read()

parts = cur.rsplit("return lessons", 1)
new_cur = parts[0] + code_60_to_63 + "\n    return lessons\n"
with open("scripts/framework_builder/gen_sec05_part2.py", "w") as f:
    f.write(new_cur)

print("gen_sec05_part2.py updated through Unit 63 (A1 FINAL CAPSTONE CHECKPOINT)!")
