"""
Authoritative Pedagogical Specification for B1 Section 04: Part 4 (Units 154 - 155)
Units 154 (4 lessons), 155 (6 lessons - Grand B1 Milestone Capstone) -> 10 lessons
"""

from typing import List, Dict, Any

def get_sec04_part4_lessons() -> List[Dict[str, Any]]:
    lessons = []

    # =========================================================================
    # UNIT 154: Hypothetical Wishes & Conditional Yearnings
    # Budget: (20, 14, 6, 4) across 4 lessons -> (5,4,2,1), (5,4,1,1), (6,3,2,1), (4,3,1,1)
    # =========================================================================
    uid_154 = "unit_b1_154_hypothetical_wishes_conditional_yea"
    lessons.extend([
        {
            "lessonId": "les_b1_154_01_hypothetical_wishes_morphosyntax_intro",
            "unitId": uid_154, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Morphosyntax of Yearning: Unreal Wishes & Hypothetical Conditions (-вал сан)",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the B1 counterfactual and hypothetical yearning system: conditional converb -вал/-вэл + past auxiliary сан/байсан (-вал сан/бол оо 'if only, I wish that...'), past participle + сан бол ('if it had been...'), and regretful counterfactuals (тэгдэг байж, явах минь яав даа).",
            "communicativeOutcome": "Formulate poignant hypothetical wishes, unreal present aspirations, and counterfactual yearnings in elegant Mongolian.",
            "objectivesIntroduced": ["obj_b1_154_01_form_hypothetical_wishes"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_153_01_festive_affect_lexicon"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_modal_manner_n"],
            "grammarReviewed": ["gram_a2_converb_conditional_val"],
            "phonologyIntroduced": ["phono_b1_wistful_yearning_cadence"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": ["comm_b1_25_hypothetical_present_wishes"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["хүсэх", "хэрэв", "бол", "сан", "харамсах", "мөрөөдөл"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft 6 sentences expressing unrealized personal aspirations and counterfactual wishes using -вал сан and -сан бол.",
            "spokenProductionObjective": "Explain a hypothetical path in life you sometimes wonder about if you had chosen differently.",
            "registerTarget": "Introspective, poetic, and philosophically reflective register",
            "pragmaticTarget": "Conveying wistful longing (хүсэл мөрөөдөл) without sounding defeatist or bitter.",
            "prerequisiteLessonIds": ["les_b1_153_04_deep_festive_reflection_spoken"],
            "reviewsLessonIds": ["les_b1_153_01_festive_affect_exclamations_lexicon"],
            "reviewsUnitIds": ["unit_b1_153_expressing_deep_emotional_reactions"],
            "reviewReason": "Channels deep emotional reactions into philosophical hypothetical aspirations.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Model gentle, wistful, trailing intonation on -вал сан.",
            "successCriteria": [
                "Combines conditional converb (-вал/-вэл) with past copula сан to express unreal present wishes",
                "Uses past participle -сан with бол to express unfulfilled past counterfactuals"
            ],
            "masteryEvidence": "Produces 'Хэрэв би шувуу шиг нисдэг сэн бол эх орныхоо үзэсгэлэнт уулсыг дээрээс нь тольдон харах сан' eloquently.",
            "recommendedExerciseModalities": ["hypothetical_transformation", "wishing_cloze", "sentence_completion"]
        },
        {
            "lessonId": "les_b1_154_02_philosophical_allegories_reading",
            "unitId": uid_154, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: Philosophical Parables & Existential Reflections on Destiny (Хувь Заяа)",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic philosophical parables and literary essays (e.g., works exploring destiny, nomadic stoicism, and what-if musings on historical crossroads).",
            "communicativeOutcome": "Comprehend elevated philosophical essays on human fate, choices, and counterfactual existential reflections.",
            "objectivesIntroduced": ["obj_b1_154_02_read_philosophical_parables"],
            "objectivesPracticed": ["obj_b1_154_01_form_hypothetical_wishes"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_modal_manner_n"],
            "grammarReviewed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_25_hypothetical_present_wishes"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_culture_traditions_heritage"],
            "previousVocabularyReused": ["хувь заяа", "сонголт", "амьдрал", "гүн ухаан", "өгүүллэг"],
            "readingObjective": "Read a 300-word philosophical parable about a wanderer at a mountain crossroads and trace the hypothetical consequences of each path.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High literary philosophical essay and allegorical register",
            "pragmaticTarget": "Appreciating nomadic fatalism balanced with ethical personal agency.",
            "prerequisiteLessonIds": ["les_b1_154_01_hypothetical_wishes_morphosyntax_intro"],
            "reviewsLessonIds": ["les_b1_141_03_mongolian_poetry_lyrics_reading"],
            "reviewsUnitIds": ["unit_b1_141_similative_postpositions_"],
            "reviewReason": "Expands literary reading from verse poetry to existential allegorical prose.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of philosophical parable.",
            "successCriteria": [
                "Identifies hypothetical conditional structures throughout the text",
                "Extracts the parable's moral resolution regarding accepting one's chosen journey"
            ],
            "masteryEvidence": "Identifies that the wanderer realized true contentment lies in embracing the walked path rather than lamenting untrodden trails.",
            "recommendedExerciseModalities": ["allegory_deconstruction", "counterfactual_clause_mapping", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_154_03_existential_aspirations_listening",
            "unitId": uid_154, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Acoustic Comprehension: Intellectual Radio Dialogue on What-If Historical Scenarios",
            "lessonType": "listening_development",
            "primaryPurpose": "Develop auditory listening comprehension for an intellectual radio salon where a historian and philosopher debate alternate history (Хэрэв түүх өөрөөр эргэсэн бол...): what if railway lines had been laid decades earlier, or what if urban planning in the 1950s had integrated traditional gers?",
            "communicativeOutcome": "Follow high-level abstract hypothetical discourse, track nested counterfactual clauses, and comprehend speculative historical reasoning in speech.",
            "objectivesIntroduced": ["obj_b1_154_03_comprehend_counterfactual_debate"],
            "objectivesPracticed": ["obj_b1_154_01_form_hypothetical_wishes"],
            "objectivesReviewed": ["obj_b1_134_03_comprehend_cultural_podcast"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_modal_manner_n"],
            "grammarReviewed": ["gram_b1_evidentiality_hearsay_gene_suragtai"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_wistful_yearning_cadence"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_25_hypothetical_present_wishes"],
            "communicativeFunctionsReviewed": ["comm_b1_04_respectful_disagreement"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_culture_traditions_heritage"],
            "previousVocabularyReused": ["түүх", "хэрэв", "өөрчлөгдөх", "нөхцөл байдал", "эрдэмтэн"],
            "readingObjective": "",
            "listeningObjective": "Listen to a 2.5-minute radio discussion and summarize the two scholars' contrasting hypotheses regarding alternate urban development.",
            "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High intellectual radio salon and historical debate register",
            "pragmaticTarget": "Tracking complex multi-clause hypothetical conditions in rapid oral exchange.",
            "prerequisiteLessonIds": ["les_b1_154_01_hypothetical_wishes_morphosyntax_intro", "les_b1_154_02_philosophical_allegories_reading"],
            "reviewsLessonIds": ["les_b1_134_03_film_podcast_cultural_listening"],
            "reviewsUnitIds": ["unit_b1_134_film_literary_criticism_evaluating_"],
            "reviewReason": "Advances radio listening from arts criticism to speculative historiographical theory.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic intellectual studio dialogue with two articulate Mongolian thinkers debating historical contingencies.",
            "successCriteria": [
                "Identifies conditional counterfactual markers in spontaneous intellectual speech",
                "Transcribes the alternative outcomes proposed by the speakers accurately"
            ],
            "masteryEvidence": "Summarizes that Scholar A argued industrialization would have proceeded faster had mining infrastructure begun in the early 20th century.",
            "recommendedExerciseModalities": ["audio_hypothesis_mapping", "speaker_scenario_matching", "summary_completion"]
        },
        {
            "lessonId": "les_b1_154_04_personal_yearnings_dialogue_spoken",
            "unitId": uid_154, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Interactive Dialogue: Sharing Unfulfilled Hopes, Dreams & Idealized Realities",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Engage in an intimate, thoughtful dialogue between two close friends sharing idealistic hopes for society, personal creative dreams, and 'what-if' scenarios using -вал сан and counterfactual structures.",
            "communicativeOutcome": "Express tender, vulnerable aspirations and empathetic responses in deep interpersonal conversations.",
            "objectivesIntroduced": ["obj_b1_154_04_share_idealistic_dreams"],
            "objectivesPracticed": [
                "obj_b1_154_01_form_hypothetical_wishes",
                "obj_b1_154_03_comprehend_counterfactual_debate"
            ],
            "objectivesReviewed": ["obj_b1_150_04_enact_complete_zolgokh"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_modal_manner_n"],
            "grammarReviewed": ["gram_b1_converb_durative_saar"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_wistful_yearning_cadence"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_25_hypothetical_present_wishes"],
            "communicativeFunctionsReviewed": ["comm_b1_03_expressing_opinions_agreements"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["мөрөөдөх", "итгэх", "өөдрөг", "найз", "хуваалцах"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Conduct an 8-turn dialogue with a friend discussing how you would improve education or public health if you had unlimited resources.",
            "registerTarget": "Warm, intimate, reflective interpersonal dialogue register",
            "pragmaticTarget": "Validating a friend's idealistic yearnings with warmth before adding one's own hopes.",
            "prerequisiteLessonIds": ["les_b1_154_02_philosophical_allegories_reading", "les_b1_154_03_existential_aspirations_listening"],
            "reviewsLessonIds": ["les_b1_150_04_zolgokh_etiquette_roleplay_spoken"],
            "reviewsUnitIds": ["unit_b1_150_zolgokh_greeting_ritual_supporting_"],
            "reviewReason": "Shifts conversational dialogue from formal holiday rituals to intimate, authentic personal dreaming.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic dialogue between two friends having a deep conversation over evening tea.",
            "successCriteria": [
                "Employs -вал сан and counterfactual constructions fluently in responsive turns",
                "Demonstrates empathetic active listening when receiving another's personal dreams"
            ],
            "masteryEvidence": "Negotiates 'Бүх хүүхдэд дэлхийн жишигт нийцсэн боловсрол олгох боломж бүрдвэл хичнээн сайхан бэ' with genuine warmth.",
            "recommendedExerciseModalities": ["branching_idealism_dialogue", "empathy_response_drill", "spoken_roleplay"]
        }
    ])

    # =========================================================================
    # UNIT 155: Threshold Independence Capstone: Cultural Documentary (Grand Capstone!)
    # Budget: (25, 18, 9, 5) across 6 lessons -> (5,4,2,1), (5,4,2,1), (5,4,2,1), (5,3,1,1), (5,3,2,1), (0,0,0,0)
    # =========================================================================
    uid_155 = "unit_b1_155_threshold_independence_capstone_cul"
    lessons.extend([
        {
            "lessonId": "les_b1_155_01_documentary_production_lexicon",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Documentary Filmmaking Lexicon: Cultural Heritage Storytelling & Voice-Over",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Acquire high-level cultural documentary filmmaking and narration terminology (баримтат кино, өв уламжлал, дүрс бичлэг, дуу оруулах, гэрчлэх, өвлөн үлдээх, биет бус соёлын өв, тайлбарлагчийн яриа) preparing for the grand B1 capstone portfolio.",
            "communicativeOutcome": "Script, narrate, and critique cultural ethnographic documentary projects in sophisticated Mongolian.",
            "objectivesIntroduced": ["obj_b1_155_01_documentary_filmmaking_lexicon"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_154_01_form_hypothetical_wishes"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_limiting_ngaa"],
            "grammarReviewed": ["gram_a2_reflexive_possessive_base", "gram_b1_evidentiality_hearsay_gene_suragtai"],
            "phonologyIntroduced": ["phono_b1_documentary_narration_cadence"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b1_15_naadam_festival_three_games",
                "comm_b2_22_discussing_historical_events"
            ],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_media_digital_society"],
            "previousVocabularyReused": ["кино", "баримт", "соёл", "өв", "тайлбарлах", "үзэгч"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft 5 sentences scripting the voice-over narration for the opening sequence of a documentary on nomadic resilience.",
            "spokenProductionObjective": "Explain your creative vision and theme for a 5-minute cultural documentary about Mongolia.",
            "registerTarget": "High documentary filmmaking, cultural stewardship, and multimedia narrative register",
            "pragmaticTarget": "Synthesizing deep cultural knowledge with professional multimedia storytelling.",
            "prerequisiteLessonIds": ["les_b1_154_04_personal_yearnings_dialogue_spoken"],
            "reviewsLessonIds": ["les_b1_134_01_critical_appraisal_lexicon"],
            "reviewsUnitIds": ["unit_b1_134_film_literary_criticism_evaluating_"],
            "reviewReason": "Connects film criticism with active documentary screenwriting and narration.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronounce media production and documentary narration terms.",
            "successCriteria": [
                "Uses documentary production terminology accurately",
                "Crafts evocative voice-over sentences integrating limiting converbs (-нгаа)"
            ],
            "masteryEvidence": "Produces 'Энэхүү баримтат кино нь нүүдэлчдийн олон мянган жилийн соёлын өвийг хойч үедээ өвлүүлэн үлдээх зорилготой' with professional polish.",
            "recommendedExerciseModalities": ["media_collocation_matching", "voiceover_scripting_cloze", "sentence_composition"]
        },
        {
            "lessonId": "les_b1_155_02_unesco_heritage_dossier_reading",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: UNESCO Intangible Cultural Heritage Inscription Dossiers",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic UNESCO cultural dossier documents submitted by the Mongolian government for the inscription of the Morin Khuur, Naadam, Falconry, and Khoomei throat singing as Intangible Cultural Heritage of Humanity.",
            "communicativeOutcome": "Comprehend dense, formal cultural diplomacy documentation, heritage safeguarding measures, and ethnological justifications.",
            "objectivesIntroduced": ["obj_b1_155_02_read_unesco_heritage_dossiers"],
            "objectivesPracticed": ["obj_b1_155_01_documentary_filmmaking_lexicon"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_limiting_ngaa"],
            "grammarReviewed": ["gram_a2_reflexive_possessive_base"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b1_15_naadam_festival_three_games"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["ЮНЕСКО", "өв", "бүртгэх", "хамгаалах", "хүн төрөлхтөн"],
            "readingObjective": "Read a 350-word excerpt from an official UNESCO nomination dossier and summarize 3 concrete safeguarding actions pledged by the state.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High international cultural diplomacy and heritage policy register",
            "pragmaticTarget": "Interpreting cultural heritage protection as a universal human imperative.",
            "prerequisiteLessonIds": ["les_b1_155_01_documentary_production_lexicon"],
            "reviewsLessonIds": ["les_b1_145_02_naadam_historical_origins_reading"],
            "reviewsUnitIds": ["unit_b1_145_national_pride_the_three_manly_game"],
            "reviewReason": "Deepens festival history into international treaty and cultural diplomacy documentation.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of UNESCO nomination dossier excerpt.",
            "successCriteria": [
                "Extracts specific criteria justifying intangible cultural heritage inscription",
                "Identifies transmission strategies preserving crafts and oral traditions for youth"
            ],
            "masteryEvidence": "Identifies that establishing regional master-apprentice workshops was central to safeguarding morin khuur crafting.",
            "recommendedExerciseModalities": ["dossier_analysis", "safeguarding_matrix", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_155_03_cultural_master_interview_listening",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Acoustic Comprehension: In-Depth Documentary Interview with a Heritage Living Treasure",
            "lessonType": "listening_development",
            "primaryPurpose": "Develop auditory listening comprehension for a master documentary interview where an 80-year-old Living Cultural Treasure (Өвлөн уламжлагч) reflects on six decades of preserving rare nomadic epics, craftsmanship, and philosophical wisdom.",
            "communicativeOutcome": "Understand extended, unhurried, deeply profound spoken Mongolian rich in dialectal richness, elder cadence, and philosophical metaphors.",
            "objectivesIntroduced": ["obj_b1_155_03_comprehend_master_interview"],
            "objectivesPracticed": ["obj_b1_155_01_documentary_filmmaking_lexicon"],
            "objectivesReviewed": ["obj_b1_151_03_comprehend_chanted_blessing_odes"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_evidentiality_hearsay_gene_suragtai"],
            "grammarReviewed": ["gram_b1_converb_limiting_ngaa"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_documentary_narration_cadence"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b2_22_discussing_historical_events"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage"],
            "previousVocabularyReused": ["өв залгамжлагч", "мастер", "ухаан", "залуу үе", "захиас"],
            "readingObjective": "",
            "listeningObjective": "Listen to a 3-minute master interview excerpt and transcribe the elder's final message to 21st-century youth regarding language preservation.",
            "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High documentary interview and elder oral testament register",
            "pragmaticTarget": "Internalizing ancestral oral memory and cultural stewardship.",
            "prerequisiteLessonIds": ["les_b1_155_01_documentary_production_lexicon", "les_b1_155_02_unesco_heritage_dossier_reading"],
            "reviewsLessonIds": ["les_b1_151_03_morin_khuur_blessing_listening"],
            "reviewsUnitIds": ["unit_b1_151_traditional_blessing_poetry_recitin"],
            "reviewReason": "Expands listening to authentic life-history interviews with national living cultural treasures.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic studio documentary audio featuring a revered elder living treasure speaking with warmth and dignified authority.",
            "successCriteria": [
                "Follows unhurried elder speech without loss of comprehension across a 3-minute passage",
                "Transcribes philosophical advice and idiomatic cultural reflections accurately"
            ],
            "masteryEvidence": "Transcribes elder's testament: 'Эх хэл, өв соёл хоёр бол тусгаар тогтнолын маань дархлаа мөн' with 100% accuracy.",
            "recommendedExerciseModalities": ["audio_oral_history_transcription", "thematic_synthesis", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_155_04_documentary_panel_roundtable",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Discussion: Filmmakers' Round Table on Modernizing Traditional Heritage",
            "lessonType": "discussion",
            "primaryPurpose": "Participate in a dynamic filmmakers' roundtable debating how modern cinema, digital media, and video games can revitalize ancient nomadic mythology and folklore without distorting cultural authenticity.",
            "communicativeOutcome": "Defend creative interpretations, balance tradition against creative modernization, and engage in high-level aesthetic debate.",
            "objectivesIntroduced": ["obj_b1_155_04_debate_heritage_modernization"],
            "objectivesPracticed": [
                "obj_b1_155_01_documentary_filmmaking_lexicon",
                "obj_b1_155_03_comprehend_master_interview"
            ],
            "objectivesReviewed": ["obj_b1_134_04_debate_literary_themes"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_limiting_ngaa"],
            "grammarReviewed": ["gram_a2_reflexive_possessive_base"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_documentary_narration_cadence"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b1_15_naadam_festival_three_games",
                "comm_b2_22_discussing_historical_events"
            ],
            "communicativeFunctionsReviewed": ["comm_b1_04_respectful_disagreement"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_media_digital_society"],
            "previousVocabularyReused": ["орчин үе", "уламжлал", "шинэчлэл", "залуучууд", "хэлбэр"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Contribute 4 analytical turns debating whether contemporary folk-rock and digital arts honor or dilute traditional nomadic folklore.",
            "registerTarget": "High intellectual cultural arts and filmmaking seminar register",
            "pragmaticTarget": "Synthesizing respect for ancient canon with appreciation for dynamic contemporary adaptation.",
            "prerequisiteLessonIds": ["les_b1_155_02_unesco_heritage_dossier_reading", "les_b1_155_03_cultural_master_interview_listening"],
            "reviewsLessonIds": ["les_b1_134_04_book_club_cultural_discussion"],
            "reviewsUnitIds": ["unit_b1_134_film_literary_criticism_evaluating_"],
            "reviewReason": "Synthesizes arts criticism discussion with media production and cultural preservation debate.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Provide discussion prompts and contrasting viewpoints by film directors.",
            "successCriteria": [
                "Contributes 4 substantive turns integrating documentary lexicon and aesthetic critique",
                "Maintains polite conversational turn-taking and balanced rhetorical argumentation"
            ],
            "masteryEvidence": "Articulates 'Өв соёлыг зөвхөн музейд хадгалах бус, орчин үеийн дижитал урлагаар дамжуулан амьд байлгах нь бидний үүрэг' persuasively.",
            "recommendedExerciseModalities": ["filmmakers_roundtable", "cultural_dilemma_evaluation", "peer_critique"]
        },
        {
            "lessonId": "les_b1_155_05_documentary_voiceover_script_writing",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 5,
            "title": "Writing Workshop: Authoring a 200-Word Cultural Documentary Voice-Over Script",
            "lessonType": "writing",
            "primaryPurpose": "Compose a polished, publication-grade 200-word voice-over script for an internationally distributed cultural documentary showcasing the enduring soul of Mongolian nomadic heritage, pastoral resilience, and festival celebrations.",
            "communicativeOutcome": "Author an evocative, poetic, and factually rigorous multimedia voice-over script in threshold B1 Mongolian.",
            "objectivesIntroduced": ["obj_b1_155_05_author_documentary_script"],
            "objectivesPracticed": [
                "obj_b1_155_01_documentary_filmmaking_lexicon",
                "obj_b1_155_04_debate_heritage_modernization"
            ],
            "objectivesReviewed": ["obj_b1_144_04_author_expedition_itinerary_document"],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_b1_converb_limiting_ngaa",
                "gram_b1_evidentiality_hearsay_gene_suragtai"
            ],
            "grammarReviewed": ["gram_a2_reflexive_possessive_base"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b1_15_naadam_festival_three_games",
                "comm_b2_22_discussing_historical_events"
            ],
            "communicativeFunctionsReviewed": ["comm_b1_10_writing_formal_email_letter"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_media_digital_society"],
            "previousVocabularyReused": ["дэлгэц", "үзэгч", "дуу хоолой", "баялаг түүх", "бахархал"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Author a 200-word evocative voice-over narration script structured with Hook, Pastoral Reality, Festival Climax, and Final Philosophical Reflection.",
            "spokenProductionObjective": "",
            "registerTarget": "Poetic, cinematic, and culturally resonant voice-over register",
            "pragmaticTarget": "Crafting prose tailored for spoken delivery with natural breathing pauses and cinematic rhythm.",
            "prerequisiteLessonIds": ["les_b1_155_03_cultural_master_interview_listening", "les_b1_155_04_documentary_panel_roundtable"],
            "reviewsLessonIds": ["les_b1_144_04_great_western_itinerary_writing"],
            "reviewsUnitIds": ["unit_b1_144_expedition_itinerary_capstone_great"],
            "reviewReason": "Synthesizes structured itinerary writing into cinematic voice-over documentary screenwriting.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Provide audio playback of the completed documentary script.",
            "successCriteria": [
                "Produces a 200-word cohesive cinematic script with scene directions and narration text",
                "Weaves advanced B1 subordination, converbs, and cultural lexicon seamlessly"
            ],
            "masteryEvidence": "Submits a script opening with 'Цагийн эрхээр өөрчлөгдөх дэлхийн урсгалд нүүдэлчдийн сэтгэл зүрх, өв соёл он цагийг туулан гэрэлтсээр байна' without error.",
            "recommendedExerciseModalities": ["guided_scriptwriting", "voiceover_timing_drill", "peer_script_review"]
        },
        {
            "lessonId": "les_b1_155_06_b1_level_culminating_mastery_capstone",
            "unitId": uid_155, "cefrLevel": "B1", "sequenceWithinUnit": 6,
            "title": "B1 Level Culminating Mastery Checkpoint: Cultural Documentary Presentation",
            "lessonType": "milestone_checkpoint",
            "primaryPurpose": "Grand culminating B1 Threshold Independence benchmark. Comprehensive synthesis across all 44 B1 units: workplace discourse, negotiations, debate, causal/temporal/manner converbs, participial oblique nominalization, subordinate subject genitive marking, purposive postpositions, agentives, similatives, evidential hearsay, emotional affect, and festival pageantry. The learner performs a multi-skill capstone portfolio: reading an archival source, listening to a panel debate, authoring a documentary essay, and delivering a 3-minute oral documentary presentation.",
            "communicativeOutcome": "Demonstrate complete Threshold B1 communicative independence across reading, listening, writing, and oral production in Mongolian.",
            "objectivesIntroduced": ["obj_b1_155_06_b1_culminating_mastery_capstone"],
            "objectivesPracticed": [
                "obj_b1_112_01_professional_qualifications_lexicon",
                "obj_b1_124_01_express_nuanced_stance",
                "obj_b1_125_01_polite_disagreement_formulas",
                "obj_b1_126_01_form_causal_clauses",
                "obj_b1_133_01_professional_advisory_formulas",
                "obj_b1_134_05_author_published_review",
                "obj_b1_137_01_decline_nominalized_participles",
                "obj_b1_138_01_mark_subordinate_subject_genitive",
                "obj_b1_139_01_form_purposive_clauses",
                "obj_b1_140_01_form_agentive_participles",
                "obj_b1_141_01_form_similative_comparisons",
                "obj_b1_142_01_form_temporal_framing_clauses",
                "obj_b1_145_01_naadam_pageantry_lexicon",
                "obj_b1_150_01_zolgokh_greeting_formulas_lexicon",
                "obj_b1_152_01_use_hearsay_particles",
                "obj_b1_153_01_festive_affect_lexicon",
                "obj_b1_154_01_form_hypothetical_wishes",
                "obj_b1_155_05_author_documentary_script"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_b1_nominalization_participles_cases",
                "gram_b1_subordinate_subject_marking_genitive",
                "gram_b1_clause_purposive_tuld_tuloo",
                "gram_b1_participle_agentive_gch",
                "gram_b1_postpositions_similative_shig_adil_met",
                "gram_b1_clause_temporal_omno_daraa_yed",
                "gram_b1_evidentiality_hearsay_gene_suragtai",
                "gram_b1_converb_contemporaneous_magts",
                "gram_b1_converb_durative_saar",
                "gram_b1_converb_modal_manner_n",
                "gram_b1_converb_limiting_ngaa",
                "gram_b1_converb_abnutative_lgui",
                "gram_b1_epistemic_probability_bololtoi_magadgui"
            ],
            "grammarReviewed": [],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_01_narrating_personal_anecdotes",
                "comm_b1_02_sequencing_past_chronology",
                "comm_b1_03_expressing_opinions_agreements",
                "comm_b1_04_respectful_disagreement",
                "comm_b1_05_making_causal_arguments",
                "comm_b1_06_stating_purpose_long_term_goals",
                "comm_b1_07_relaying_hearsay_news",
                "comm_b1_08_speculating_visual_evidence",
                "comm_b1_13_discussing_environmental_issues",
                "comm_b1_14_traditional_celebrations_tsagaan_sar",
                "comm_b1_15_naadam_festival_three_games",
                "comm_b1_16_giving_advice_recommendations",
                "comm_b1_17_expressing_emotional_reactions",
                "comm_b1_22_discussing_books_films_reviews",
                "comm_b1_23_comparing_city_country_lifestyles",
                "comm_b1_24_discussing_education_career_path",
                "comm_b1_25_hypothetical_present_wishes",
                "comm_b2_22_discussing_historical_events"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0, "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_b1_culture_traditions_heritage",
                "lex_b1_environment_geography_climate",
                "lex_b1_education_career_workplace",
                "lex_b1_opinion_argumentation_rhetoric",
                "lex_b1_media_digital_society",
                "lex_b1_travel_transport_tourism"
            ],
            "previousVocabularyReused": [
                "өв соёл", "тусгаар тогтнол", "байгаль", "бэлчээр", "хөгжил",
                "наадам", "Цагаан сар", "золгох", "ерөөл", "ирээдүй"
            ],
            "readingObjective": "Read and deconstruct a 400-word multi-disciplinary cultural treatise analyzing the endurance of nomadic values in a globalized digital society.",
            "listeningObjective": "Comprehend a 3.5-minute cultural documentary soundtrack featuring elder narration, folk music, and intellectual debate.",
            "writingObjective": "Author a 200-word comprehensive capstone essay articulating how traditional cultural values and modern civic development can harmoniously coexist in Mongolia.",
            "spokenProductionObjective": "Deliver a 3-minute oral documentary presentation narrating a chosen aspect of Mongolian cultural heritage with poise, accurate subordination, and affective eloquence.",
            "registerTarget": "Complete B1 Threshold level communicative mastery across all registers",
            "pragmaticTarget": "Full communicative independence in the target language community: navigating daily, professional, and cultural interactions with autonomy.",
            "prerequisiteLessonIds": [
                "les_b1_155_04_documentary_panel_roundtable",
                "les_b1_155_05_documentary_voiceover_script_writing"
            ],
            "reviewsLessonIds": [
                "les_b1_123_05_personal_banking_portfolio_spoken",
                "les_b1_134_06_section_02_milestone_synthesis_checkpoint",
                "les_b1_144_05_section_03_milestone_synthesis_checkpoint",
                "les_b1_150_04_zolgokh_etiquette_roleplay_spoken",
                "les_b1_151_04_toast_blessing_recitation_spoken",
                "les_b1_152_05_investigative_debrief_spoken",
                "les_b1_153_04_deep_festive_reflection_spoken",
                "les_b1_154_04_personal_yearnings_dialogue_spoken"
            ],
            "reviewsUnitIds": [
                "unit_b1_123_complex_banking_electronic_funds_tr",
                "unit_b1_134_film_literary_criticism_evaluating_",
                "unit_b1_144_expedition_itinerary_capstone_great",
                "unit_b1_150_zolgokh_greeting_ritual_supporting_",
                "unit_b1_151_traditional_blessing_poetry_recitin",
                "unit_b1_152_hearsay_evidentiality_particles_and",
                "unit_b1_153_expressing_deep_emotional_reactions",
                "unit_b1_154_hypothetical_wishes_conditional_yea"
            ],
            "reviewReason": "Ultimate B1 Grand Capstone integrating all linguistic, communicative, and cultural competencies acquired across the entire 44-unit level.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Culminating cultural documentary audio benchmark featuring full orchestral morin khuur score and master orator delivery.",
            "successCriteria": [
                "Achieves 85%+ on the comprehensive CEFR B1 multi-skill benchmark rubric",
                "Demonstrates effortless syntactic subordination, converbial chaining, and cultural register calibration across writing and speaking"
            ],
            "masteryEvidence": "Submits a flawless 200-word capstone essay and delivers a 3-minute oral presentation demonstrating complete B1 threshold independence.",
            "recommendedExerciseModalities": [
                "b1_grand_capstone_portfolio",
                "multimedia_documentary_presentation",
                "cefr_b1_oral_proficiency_exam"
            ]
        }
    ])

    return lessons
