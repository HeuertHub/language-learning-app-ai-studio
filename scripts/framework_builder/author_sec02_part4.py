"""
Authoritative Pedagogical Specification for B1 Section 02: Part 4 (Units 133 - 134)
Units 133 (4 lessons), 134 (6 lessons - Milestone Capstone) -> 10 lessons
"""

from typing import List, Dict, Any

def get_sec02_part4_lessons() -> List[Dict[str, Any]]:
    lessons = []

    # =========================================================================
    # UNIT 133: Giving Professional Advice & Actionable Recommendations
    # Budget: (20, 14, 6, 4) across 4 lessons -> (5,4,2,1), (5,4,1,1), (6,3,2,1), (4,3,1,1)
    # =========================================================================
    uid_133 = "unit_b1_133_giving_professional_advice_actionab"
    lessons.extend([
        {
            "lessonId": "les_b1_133_01_professional_advisory_lexicon",
            "unitId": uid_133, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Advisory Formulas: Prescribing Solutions & Strategic Recommendations",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Acquire professional advisory formulas and consulting terminology (зөвлөх, анхаарах, зөвлөмж өгөх, дээр байх, шаардлагатай гэж үзэх, санал болгох) varying from gentle suggestions to imperative professional guidelines.",
            "communicativeOutcome": "Provide tailored professional advice and strategic recommendations to clients, colleagues, and subordinates.",
            "objectivesIntroduced": ["obj_b1_133_01_professional_advisory_formulas"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_132_01_differentiate_epistemic_modals"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_epistemic_probability_bololtoi_magadgui"],
            "grammarReviewed": ["gram_a1_case_dative_locative_recipient", "gram_b1_converb_limiting_ngaa"],
            "phonologyIntroduced": ["phono_b1_consultative_gentle_cadence"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": ["comm_b1_16_giving_advice_recommendations"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_education_career_workplace"],
            "previousVocabularyReused": ["зөвлөгөө", "санал", "туслах", "хийх", "чухал", "үр дүнтэй"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft 5 professional recommendations for optimizing an organization's workflow using varied advisory formulas.",
            "spokenProductionObjective": "Advise a client on how to protect their assets during currency devaluation.",
            "registerTarget": "Professional consulting and advisory register",
            "pragmaticTarget": "Framing advice constructively (гээд үзвэл ямар вэ, зүгээр болов уу) to invite client collaboration.",
            "prerequisiteLessonIds": ["les_b1_132_05_investigative_forensic_report_writing"],
            "reviewsLessonIds": ["les_b1_132_01_epistemic_particles_morphosyntax_intro"],
            "reviewsUnitIds": ["unit_b1_132_epistemic_probability_particles_vs_"],
            "reviewReason": "Transforms probabilistic deductions into actionable consulting advice.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Model warm, authoritative, non-condescending consultative speech cadence.",
            "successCriteria": [
                "Selects appropriate advisory degree based on urgency and relationship",
                "Applies dative case correctly for the advice recipient (Танд зөвлөхөд...)"
            ],
            "masteryEvidence": "Produces 'Танд энэ гэрээнд гарын үсэг зурахаасаа өмнө хуульчтай зөвлөлдөхийг зөвлөж байна' accurately.",
            "recommendedExerciseModalities": ["advice_calibration_matching", "scenario_response_drill", "cloze_completion"]
        },
        {
            "lessonId": "les_b1_133_02_management_consulting_audit_reading",
            "unitId": uid_133, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: Management Consulting Audits & Strategic Roadmaps",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic executive consulting reports, organizational audits, and operational roadmaps published by Mongolian business advisors.",
            "communicativeOutcome": "Extract priority recommendations, resource allocations, and risk mitigations from management consulting texts.",
            "objectivesIntroduced": ["obj_b1_133_02_read_consulting_roadmaps"],
            "objectivesPracticed": ["obj_b1_133_01_professional_advisory_formulas"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_epistemic_probability_bololtoi_magadgui"],
            "grammarReviewed": ["gram_a1_case_dative_locative_recipient"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_16_giving_advice_recommendations"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_education_career_workplace"],
            "previousVocabularyReused": ["аудит", "стратеги", "зөвлөмж", "шийдвэрлэх", "байгууллага"],
            "readingObjective": "Read a 300-word consulting executive summary and categorize recommendations into short-term and long-term priority tiers.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High executive corporate consulting register",
            "pragmaticTarget": "Synthesizing complex systemic findings into executive-level action items.",
            "prerequisiteLessonIds": ["les_b1_133_01_professional_advisory_lexicon"],
            "reviewsLessonIds": ["les_b1_126_03_socio_economic_causality_reading"],
            "reviewsUnitIds": ["unit_b1_126_causal_conjunctions_connectors_"],
            "reviewReason": "Connects diagnostic reading comprehension with solution-oriented recommendation roadmaps.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of consulting report summary.",
            "successCriteria": [
                "Identifies conditional and modal structures used to formulate recommendations",
                "Distinguishes mandatory regulatory advice from discretionary strategic options"
            ],
            "masteryEvidence": "Identifies that digitizing the inventory ledger was categorized as an immediate mandatory step.",
            "recommendedExerciseModalities": ["recommendation_sorting", "priority_matrix", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_133_03_executive_advisory_consultation_dialogue",
            "unitId": uid_133, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Interactive Dialogue: One-on-One Strategic Consultation with a Client",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Conduct an interactive consulting session diagnosing a business owner's operational bottlenecks, responding to their anxieties, and proposing tailored interventions.",
            "communicativeOutcome": "Deliver persuasive, empathetic professional counsel while handling client hesitations and cost concerns.",
            "objectivesIntroduced": ["obj_b1_133_03_conduct_consulting_session"],
            "objectivesPracticed": [
                "obj_b1_133_01_professional_advisory_formulas",
                "obj_b1_133_02_read_consulting_roadmaps"
            ],
            "objectivesReviewed": ["obj_b1_125_01_polite_disagreement_formulas"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_epistemic_probability_bololtoi_magadgui"],
            "grammarReviewed": ["gram_b1_converb_limiting_ngaa"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_consultative_gentle_cadence"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_16_giving_advice_recommendations"],
            "communicativeFunctionsReviewed": ["comm_b1_04_respectful_disagreement"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_education_career_workplace"],
            "previousVocabularyReused": ["харилцагч", "төсөв", "шийдэл", "зөвлөх", "итгэл"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Enact an 8-turn consultation with a hesitant business owner advising them to restructure staff shifts.",
            "registerTarget": "Warm, confident professional consulting register",
            "pragmaticTarget": "Acknowledging client cost concerns with empathy before demonstrating long-term ROI.",
            "prerequisiteLessonIds": ["les_b1_133_01_professional_advisory_lexicon", "les_b1_133_02_management_consulting_audit_reading"],
            "reviewsLessonIds": ["les_b1_123_04_wire_transfer_teller_dialogue"],
            "reviewsUnitIds": ["unit_b1_123_complex_banking_electronic_funds_tr"],
            "reviewReason": "Revisits high-level professional dialogue with an advisory, problem-solving focus.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic dialogue between an expert consultant and an anxious Mongolian entrepreneur.",
            "successCriteria": [
                "Maintains empathetic rapport while offering concrete, actionable solutions",
                "Uses consultative modal expressions (-вал дээр, -х хэрэгтэй, зөвлөж байна) effectively"
            ],
            "masteryEvidence": "Negotiates 'Эхний ээлжинд маркетингийн зардлаа бага зэрэг танаж, бүтээгдэхүүнийхээ чанарт анхаарвал үр дүнтэй болов уу' fluently.",
            "recommendedExerciseModalities": ["branching_consultation", "client_objection_handling", "advisory_roleplay"]
        },
        {
            "lessonId": "les_b1_133_04_consulting_memorandum_writing",
            "unitId": uid_133, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Writing Workshop: Authoring an Actionable Advisory Memo",
            "lessonType": "writing",
            "primaryPurpose": "Compose a structured 150-word formal advisory memorandum for a corporate department head recommending 3 operational enhancements.",
            "communicativeOutcome": "Produce a well-organized professional advisory memo with background analysis, concrete recommendations, and implementation timeline.",
            "objectivesIntroduced": ["obj_b1_133_04_write_advisory_memo"],
            "objectivesPracticed": [
                "obj_b1_133_01_professional_advisory_formulas",
                "obj_b1_133_03_conduct_consulting_session"
            ],
            "objectivesReviewed": ["obj_b1_125_04_write_rebuttal_letter"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_epistemic_probability_bololtoi_magadgui"],
            "grammarReviewed": ["gram_a1_case_dative_locative_recipient"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_16_giving_advice_recommendations"],
            "communicativeFunctionsReviewed": ["comm_b1_10_writing_formal_email_letter"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_opinion_argumentation_rhetoric", "lex_b1_education_career_workplace"],
            "previousVocabularyReused": ["санамж бичиг", "хэрэгжүүлэх", "хугацаа", "үр ашиг", "сайжруулах"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Author a 150-word advisory memo with 3 numbered recommendations for software adoption, risk mitigation, and staff upskilling.",
            "spokenProductionObjective": "",
            "registerTarget": "Formal corporate administrative advisory register",
            "pragmaticTarget": "Presenting recommendations with crisp numbered clarity and realistic resource milestones.",
            "prerequisiteLessonIds": ["les_b1_133_02_management_consulting_audit_reading", "les_b1_133_03_executive_advisory_consultation_dialogue"],
            "reviewsLessonIds": ["les_b1_125_04_formal_rebuttal_letter_writing"],
            "reviewsUnitIds": ["unit_b1_125_respectful_disagreement_constructiv"],
            "reviewReason": "Synthesizes formal written advocacy into actionable management recommendations.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Provide audio playback of the completed advisory memo.",
            "successCriteria": [
                "Structures memo with Context, Findings, Recommendations, and Timeline sections",
                "Applies professional advisory lexicon and conditional syntax accurately"
            ],
            "masteryEvidence": "Submits a memo opening with 'Байгууллагын үр ашгийг дээшлүүлэх зорилгоор дараах 3 зөвлөмжийг дэвшүүлж байна' and sustaining clear structure throughout.",
            "recommendedExerciseModalities": ["guided_memo_writing", "action_item_bulleting", "peer_review"]
        }
    ])

    # =========================================================================
    # UNIT 134: Film & Literary Criticism: Evaluating Works of Art (Milestone Capstone)
    # Budget: (20, 14, 6, 4) across 6 lessons -> (4,3,1,1), (4,3,1,1), (4,3,1,1), (4,3,1,1), (4,2,2,0), (0,0,0,0)
    # =========================================================================
    uid_134 = "unit_b1_134_film_literary_criticism_evaluating_"
    lessons.extend([
        {
            "lessonId": "les_b1_134_01_critical_appraisal_lexicon",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Aesthetic Criticism Lexicon: Plot, Character Arc, Cinematography & Theme",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Acquire critical aesthetic and analytical vocabulary for reviewing literature, films, and theater (зохиолын өрнөл, дүр бүтээлт, зураглал, найруулга, далд утга, шүүмжлэх, сайшаах).",
            "communicativeOutcome": "Evaluate cultural works of art using specialized aesthetic and critical terminology.",
            "objectivesIntroduced": ["obj_b1_134_01_aesthetic_criticism_lexicon"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_129_02_manner_posture_lexicon"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag", "gram_b1_converb_abnutative_lgui"],
            "phonologyIntroduced": ["phono_b1_critical_evaluative_stress"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": ["comm_b1_22_discussing_books_films_reviews"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["кино", "ном", "жүжигчин", "найруулагч", "үзэгч", "үнэлэх"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft 4 critical evaluation sentences analyzing the cinematography and musical score of a Mongolian film.",
            "spokenProductionObjective": "Explain why a particular character in a novel resonated with you using aesthetic terms.",
            "registerTarget": "High cultural criticism and arts commentary register",
            "pragmaticTarget": "Balancing appreciation of artistic craft with objective identification of flaws.",
            "prerequisiteLessonIds": ["les_b1_133_04_consulting_memorandum_writing"],
            "reviewsLessonIds": ["les_b1_129_02_manner_and_posture_lexicon"],
            "reviewsUnitIds": ["unit_b1_129_modal_converb_of_manner_suffix_"],
            "reviewReason": "Applies literary and behavioral descriptive terms to formal arts criticism.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronunciation of cinematic and literary analytical terminology.",
            "successCriteria": [
                "Uses critical arts vocabulary accurately (найруулагчийн шийдэл, дүр хөгжүүлэлт, далд санаа)",
                "Forms cohesive evaluation clauses substantiating aesthetic impressions"
            ],
            "masteryEvidence": "Produces 'Киноны зураглал гайхалтай болсон ч зохиолын өрнөл хэт удаан, учир дутагдалтай байв' without error.",
            "recommendedExerciseModalities": ["arts_vocabulary_matching", "evaluative_collocation", "sentence_expansion"]
        },
        {
            "lessonId": "les_b1_134_02_film_reviews_reading",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: Published Reviews of Mongolian Cinema & International Festivals",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic film critiques of contemporary Mongolian cinema (e.g., works by modern directors exploring urban youth or nomadic heritage) published in cultural journals.",
            "communicativeOutcome": "Decipher cultural symbolism, directorial choices, and critical evaluations in published artistic reviews.",
            "objectivesIntroduced": ["obj_b1_134_02_read_film_reviews"],
            "objectivesPracticed": ["obj_b1_134_01_aesthetic_criticism_lexicon"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "grammarReviewed": ["gram_a2_verb_past_narrative_v"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_22_discussing_books_films_reviews"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_media_digital_society"],
            "previousVocabularyReused": ["шүүмж", "нийтлэл", "дэлгэц", "фестиваль", "шагнал"],
            "readingObjective": "Read a 300-word film review of an award-winning Mongolian indie film and identify 2 strengths and 1 critique raised by the reviewer.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "Sophisticated journalistic arts criticism register",
            "pragmaticTarget": "Understanding nuanced cultural metaphors and subtextual socio-political commentary in arts reviews.",
            "prerequisiteLessonIds": ["les_b1_134_01_critical_appraisal_lexicon"],
            "reviewsLessonIds": ["les_b1_129_03_literary_short_stories_reading"],
            "reviewsUnitIds": ["unit_b1_129_modal_converb_of_manner_suffix_"],
            "reviewReason": "Extends literary reading from narrative storytelling to meta-critical evaluation of artistic works.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of published film review text.",
            "successCriteria": [
                "Identifies the reviewer's overall verdict (praise vs mixed reception)",
                "Extracts specific critiques regarding pacing, casting, and thematic execution"
            ],
            "masteryEvidence": "Identifies that the reviewer praised the authentic portrayal of steppe life but criticized the dialogue sound mixing.",
            "recommendedExerciseModalities": ["review_deconstruction", "critique_sorting", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_134_03_film_podcast_cultural_listening",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Acoustic Comprehension: Cinema Podcast on Nomadic Motifs in Modern Art",
            "lessonType": "listening_development",
            "primaryPurpose": "Develop listening comprehension for an unscripted cultural podcast where two Mongolian critics debate the representation of nomadic tradition versus modern globalization in cinema.",
            "communicativeOutcome": "Follow dynamic cultural discourse, comprehend rapid turn-taking, and identify conflicting interpretations of artistic motifs.",
            "objectivesIntroduced": ["obj_b1_134_03_comprehend_cultural_podcast"],
            "objectivesPracticed": ["obj_b1_134_01_aesthetic_criticism_lexicon"],
            "objectivesReviewed": ["obj_b1_125_02_comprehend_symposium_debate"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_converb_abnutative_lgui"],
            "grammarReviewed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_critical_evaluative_stress"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_22_discussing_books_films_reviews"],
            "communicativeFunctionsReviewed": ["comm_b1_03_expressing_opinions_agreements"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_media_digital_society"],
            "previousVocabularyReused": ["подкаст", "яриа", "сэдэв", "уламжлал", "орчин үе"],
            "readingObjective": "",
            "listeningObjective": "Listen to a 2.5-minute cultural podcast excerpt and transcribe the divergent opinions of the two critics regarding the film's climax.",
            "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "Intellectual conversational cultural podcast register",
            "pragmaticTarget": "Tracking colloquial cultural metaphors and unscripted interjections in spoken Mongolian commentary.",
            "prerequisiteLessonIds": ["les_b1_134_01_critical_appraisal_lexicon", "les_b1_134_02_film_reviews_reading"],
            "reviewsLessonIds": ["les_b1_125_02_academic_symposium_rebuttal_listening"],
            "reviewsUnitIds": ["unit_b1_125_respectful_disagreement_constructiv"],
            "reviewReason": "Expands listening from academic symposiums to contemporary digital arts media.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic studio podcast audio with two engaging conversational speakers.",
            "successCriteria": [
                "Distinguishes the differing perspectives of Host A and Host B regarding cinematic symbolism",
                "Recognizes fast-paced cultural loanwords and evaluative idioms in natural speech"
            ],
            "masteryEvidence": "Summarizes accurately that Host A viewed the horse-race climax as triumphant while Host B interpreted it as tragic.",
            "recommendedExerciseModalities": ["audio_comprehension", "speaker_attribution", "summary_completion"]
        },
        {
            "lessonId": "les_b1_134_04_book_club_cultural_discussion",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Discussion: Book Club Round Table on Modern Mongolian Literature",
            "lessonType": "discussion",
            "primaryPurpose": "Participate in an intellectual book club roundtable evaluating a novel's philosophical themes, character transformations, and reflection of post-nomadic society.",
            "communicativeOutcome": "Debate literary interpretations with peers, defend personal readings with textual citations, and challenge superficial evaluations.",
            "objectivesIntroduced": ["obj_b1_134_04_debate_literary_themes"],
            "objectivesPracticed": [
                "obj_b1_134_01_aesthetic_criticism_lexicon",
                "obj_b1_134_03_comprehend_cultural_podcast"
            ],
            "objectivesReviewed": ["obj_b1_125_03_participate_formal_debate"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "grammarReviewed": ["gram_a1_verb_tense_present_habitual_dag"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_critical_evaluative_stress"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_22_discussing_books_films_reviews"],
            "communicativeFunctionsReviewed": ["comm_b1_04_respectful_disagreement"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["уншигч", "үзэл санаа", "дүгнэлт", "сэтгэгдэл", "сонирхолтой"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Contribute 4 substantive speaking turns in a book club debate exploring why the protagonist's moral choices matter.",
            "registerTarget": "Intellectual cultural dialogue and literary salon register",
            "pragmaticTarget": "Validating fellow readers' interpretations while introducing deeper symbolic subtext.",
            "prerequisiteLessonIds": ["les_b1_134_02_film_reviews_reading", "les_b1_134_03_film_podcast_cultural_listening"],
            "reviewsLessonIds": ["les_b1_125_03_structured_oxford_debate_simulation"],
            "reviewsUnitIds": ["unit_b1_125_respectful_disagreement_constructiv"],
            "reviewReason": "Transfers structured debate skills into cultured literary and philosophical book discussion.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Provide discussion prompts and provocative literary interpretations by native panelists.",
            "successCriteria": [
                "Contributes 4 analytical speaking turns evaluating themes and character motivations",
                "Employs causal and evaluative structures fluently in conversational turn-taking"
            ],
            "masteryEvidence": "Articulates 'Энэ зохиолын гол санаа нь хүний мөн чанар, байгальтайгаа зохицон амьдрах уламжлалын үнэ цэнийг харуулсан гэж бодож байна' persuasively.",
            "recommendedExerciseModalities": ["roundtable_discussion", "thematic_interpretation", "peer_critique"]
        },
        {
            "lessonId": "les_b1_134_05_critical_arts_essay_writing",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 5,
            "title": "Writing Workshop: Authoring a Published Arts Critique (Шүүмж)",
            "lessonType": "writing",
            "primaryPurpose": "Compose a polished 150-word cultural critique of a book, film, or theatrical production suitable for publication in a cultural journal or lifestyle blog.",
            "communicativeOutcome": "Author a balanced, engaging cultural review featuring synopsis, aesthetic critique, technical appraisal, and overall recommendation.",
            "objectivesIntroduced": ["obj_b1_134_05_author_published_review"],
            "objectivesPracticed": [
                "obj_b1_134_01_aesthetic_criticism_lexicon",
                "obj_b1_134_04_debate_literary_themes"
            ],
            "objectivesReviewed": ["obj_b1_124_04_write_opinion_editorial"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_causal_uchir_uchraas_tul"],
            "grammarReviewed": ["gram_b1_converb_abnutative_lgui"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_22_discussing_books_films_reviews"],
            "communicativeFunctionsReviewed": ["comm_b1_03_expressing_opinions_agreements"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 2, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_b1_culture_traditions_heritage", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["үнэлгээ", "зөвлөмж", "үзэх", "унших", "сэтгэгдэл"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Author a 150-word film or book review containing a succinct hook, plot summary without spoilers, craft critique, and star rating.",
            "spokenProductionObjective": "",
            "registerTarget": "High literary and cultural journalism review register",
            "pragmaticTarget": "Balancing critical rigor with engaging prose that sparks reader interest in the work.",
            "prerequisiteLessonIds": ["les_b1_134_02_film_reviews_reading", "les_b1_134_04_book_club_cultural_discussion"],
            "reviewsLessonIds": ["les_b1_124_04_opinion_editorial_writing"],
            "reviewsUnitIds": ["unit_b1_124_formulating_nuanced_personal_stance"],
            "reviewReason": "Synthesizes opinion essay writing into specialized cultural arts criticism.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Provide audio playback of the student's authored cultural critique.",
            "successCriteria": [
                "Structures review into Catchy Title, Context/Synopsis, Analysis of Form & Content, and Final Verdict",
                "Integrates target aesthetic lexicon and causal structures seamlessly"
            ],
            "masteryEvidence": "Submits a review concluding 'Энэхүү бүтээл нь орчин үеийн залууст соёлын өвөө эргэн харах боломжийг олгосон шилдэг кино болжээ' without error.",
            "recommendedExerciseModalities": ["guided_review_composition", "spoilers_avoidance_drill", "peer_editing"]
        },
        {
            "lessonId": "les_b1_134_06_section_02_milestone_synthesis_checkpoint",
            "unitId": uid_134, "cefrLevel": "B1", "sequenceWithinUnit": 6,
            "title": "Section Milestone Checkpoint: Discourse, Argumentation & Converb Mastery",
            "lessonType": "milestone_checkpoint",
            "primaryPurpose": "Comprehensive synthesis and formal benchmark assessment across all Section 02 competencies: nuanced stances, respectful disagreement, causal conjunctions (учраас/тул/учир нь), contemporaneous (-магц), durative (-саар), manner (-н), limiting (-нгаа), abnutative (-лгүй) converbs, epistemic probability (бололтой/магадгүй), consulting advice, and cultural criticism.",
            "communicativeOutcome": "Demonstrate integrated threshold B1 discursive, rhetorical, and converbial mastery in a multi-skill simulated public symposium challenge.",
            "objectivesIntroduced": ["obj_b1_134_06_section_02_synthesis_milestone"],
            "objectivesPracticed": [
                "obj_b1_124_01_express_nuanced_stance",
                "obj_b1_125_01_polite_disagreement_formulas",
                "obj_b1_126_01_form_causal_clauses",
                "obj_b1_127_01_form_contemporaneous_converb",
                "obj_b1_128_01_form_durative_converb",
                "obj_b1_129_01_form_modal_converb_n",
                "obj_b1_130_01_form_limiting_converb",
                "obj_b1_131_01_form_abnutative_converb",
                "obj_b1_132_01_differentiate_epistemic_modals",
                "obj_b1_133_01_professional_advisory_formulas",
                "obj_b1_134_05_author_published_review"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_b1_clause_causal_uchir_uchraas_tul",
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
                "comm_b1_03_expressing_opinions_agreements",
                "comm_b1_04_respectful_disagreement",
                "comm_b1_05_making_causal_arguments",
                "comm_b1_02_sequencing_past_chronology",
                "comm_b1_01_narrating_personal_anecdotes",
                "comm_b1_08_speculating_visual_evidence",
                "comm_b1_16_giving_advice_recommendations",
                "comm_b1_22_discussing_books_films_reviews"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0, "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_b1_opinion_argumentation_rhetoric",
                "lex_b1_education_career_workplace",
                "lex_b1_culture_traditions_heritage"
            ],
            "previousVocabularyReused": [
                "байр суурь", "нотолгоо", "шалтгаан", "үр дүн", "өөрчлөгдөх",
                "соёл", "зөвлөмж", "магадлал", "шинжилгээ", "шүүмж"
            ],
            "readingObjective": "Read and deconstruct a 350-word cultural symposium keynote addressing the future of Mongolian nomadic identity.",
            "listeningObjective": "Comprehend a 3-minute panel discussion where three intellectual speakers debate language preservation.",
            "writingObjective": "Author a 150-word synthesis essay synthesizing the opposing arguments and proposing a balanced resolution.",
            "spokenProductionObjective": "Deliver a 2.5-minute formal symposium address synthesizing your viewpoint, refuting counter-claims, and proposing actionable recommendations.",
            "registerTarget": "Full B1 academic, discursive, and intellectual public standard",
            "pragmaticTarget": "Seamlessly navigating between polite concession, sharp causal reasoning, and persuasive rhetorical advocacy.",
            "prerequisiteLessonIds": [
                "les_b1_134_04_book_club_cultural_discussion",
                "les_b1_134_05_critical_arts_essay_writing"
            ],
            "reviewsLessonIds": [
                "les_b1_124_04_opinion_editorial_writing",
                "les_b1_125_03_structured_oxford_debate_simulation",
                "les_b1_126_05_explaining_systemic_causes_spoken",
                "les_b1_128_04_personal_transformation_anecdote_spoken",
                "les_b1_132_04_forensic_case_deduction_dialogue",
                "les_b1_133_04_consulting_memorandum_writing"
            ],
            "reviewsUnitIds": [
                "unit_b1_124_formulating_nuanced_personal_stance",
                "unit_b1_125_respectful_disagreement_constructiv",
                "unit_b1_126_causal_conjunctions_connectors_",
                "unit_b1_128_durative_converb_suffixes_",
                "unit_b1_132_epistemic_probability_particles_vs_",
                "unit_b1_133_giving_professional_advice_actionab"
            ],
            "reviewReason": "Caps Section 02 with a comprehensive benchmark synthesizing discourse, converb morphology, argumentation, and cultural evaluation.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Symposium keynote listening benchmark featuring high-register public intellectual oratory.",
            "successCriteria": [
                "Demonstrates mastery across all 7 Section 02 target converbs and grammatical structures in reading, writing, and speaking",
                "Maintains sophisticated cohesive discourse across a 150-word written essay and a 2.5-minute spoken address"
            ],
            "masteryEvidence": "Achieves 85%+ on integrated multi-skill milestone rubric covering written essay, oral presentation, and listening comprehension.",
            "recommendedExerciseModalities": [
                "symposium_simulation",
                "multi_skill_benchmark_exam",
                "rhetorical_advocacy_evaluation"
            ]
        }
    ])

    return lessons
