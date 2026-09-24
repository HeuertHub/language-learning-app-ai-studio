"""
Authoritative Pedagogical Specification for B1 Section 03: Part 4 (Units 143 - 144)
Units 143 (4 lessons), 144 (5 lessons - Section Capstone) -> 9 lessons
"""

from typing import List, Dict, Any

def get_sec03_part4_lessons() -> List[Dict[str, Any]]:
    lessons = []

    # =========================================================================
    # UNIT 143: Environmental Conservation & Pasture Degradation
    # Budget: (20, 14, 6, 4) across 4 lessons -> (5,4,2,1), (5,4,1,1), (6,3,2,1), (4,3,1,1)
    # =========================================================================
    uid_143 = "unit_b1_143_environmental_conservation_pasture_"
    lessons.extend([
        {
            "lessonId": "les_b1_143_01_pasture_degradation_lexicon",
            "unitId": uid_143, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Ecological Crisis Lexicon: Desertification, Overgrazing & Pasture Degradation",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Acquire technical environmental and rangeland ecology terminology (бэлчээрийн даац хэтрэх, цөлжилт, хөрсний элэгдэл, ургамлын бүрхэвч хомсдох, уур амьсгалын дулаарал, сэргээн нутагшуулах) addressing ecological threats confronting Mongolia's grasslands.",
            "communicativeOutcome": "Explain causes and consequences of rangeland degradation, overstocking, and climate drying in precise ecological Mongolian.",
            "objectivesIntroduced": ["obj_b1_143_01_pasture_degradation_lexicon"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_142_01_form_temporal_framing_clauses"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_temporal_omno_daraa_yed"],
            "grammarReviewed": ["gram_a1_verb_tense_future_prospective_na", "gram_b1_participle_agentive_gch"],
            "phonologyIntroduced": ["phono_b1_ecological_compound_articulation"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": ["comm_b1_13_discussing_environmental_issues"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_environment_geography_climate"],
            "previousVocabularyReused": ["бэлчээр", "малын тоо", "байгаль", "элс", "ургамал", "ус"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft 5 sentences analyzing the relationship between goat herd expansion (cashmere trade) and topsoil erosion.",
            "spokenProductionObjective": "Explain why rangeland carrying capacity is critical for nomadic sustainability.",
            "registerTarget": "Scientific ecology and public policy register",
            "pragmaticTarget": "Balancing economic empathy for herders with objective ecological science.",
            "prerequisiteLessonIds": ["les_b1_142_05_chronological_case_study_writing"],
            "reviewsLessonIds": ["les_b1_135_01_topography_landscapes_lexicon"],
            "reviewsUnitIds": ["unit_b1_135_geographical_landscapes_khangai_mou"],
            "reviewReason": "Deepens geographical landscape knowledge into active rangeland conservation science.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronounce complex ecological compound terminology.",
            "successCriteria": [
                "Uses rangeland ecology terms accurately (даац, цөлжилт, доройтол, сөл)",
                "Forms causal sentences linking livestock demographics to pasture carrying limits"
            ],
            "masteryEvidence": "Produces 'Бэлчээрийн даац хэтэрснээс болж хөрсний үржил шим муудаж, цөлжилт хурдасч байна' accurately.",
            "recommendedExerciseModalities": ["ecological_cause_effect_matching", "rangeland_cloze", "sentence_completion"]
        },
        {
            "lessonId": "les_b1_143_02_desertification_scientific_reading",
            "unitId": uid_143, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: Scientific Monograph on Steppe Desertification & River Drying",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic environmental research monographs published by the Mongolian Academy of Sciences on desertification rates, water table decline, and disappearance of small rivers/springs (гол горхи ширгэх).",
            "communicativeOutcome": "Comprehend scientific data, statistical environmental trends, and ecological impact assessments in academic Mongolian.",
            "objectivesIntroduced": ["obj_b1_143_02_read_desertification_research"],
            "objectivesPracticed": ["obj_b1_143_01_pasture_degradation_lexicon"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_temporal_omno_daraa_yed"],
            "grammarReviewed": ["gram_b1_voice_reciprocal_collective"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_13_discussing_environmental_issues"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_environment_geography_climate"],
            "previousVocabularyReused": ["судалгаа", "хүрээлэн", "хувь", "нэмэгдэх", "багасах"],
            "readingObjective": "Read a 300-word excerpt from an Academy of Sciences ecology report and extract 3 data points on regional desertification severity.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High academic ecological science register",
            "pragmaticTarget": "Interpreting scientific statistics and environmental risk projections.",
            "prerequisiteLessonIds": ["les_b1_143_01_pasture_degradation_lexicon"],
            "reviewsLessonIds": ["les_b1_137_03_environmental_legislation_reading"],
            "reviewsUnitIds": ["unit_b1_137_nominalization_of_participles_in_ob"],
            "reviewReason": "Pairs environmental statutory mandates with empirical scientific ecological data.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of scientific rangeland study.",
            "successCriteria": [
                "Identifies percentage statistics measuring rangeland degradation across eco-zones",
                "Extracts specific botanical indicators of overgrazing mentioned in the text"
            ],
            "masteryEvidence": "Identifies that over 70% of total national pastureland exhibits moderate to severe degradation.",
            "recommendedExerciseModalities": ["ecological_data_extraction", "graph_interpretation", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_143_03_herder_community_roundtable_listening",
            "unitId": uid_143, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Acoustic Comprehension: Herder Co-op Council on Rotational Grazing (Отор Нүүдэл)",
            "lessonType": "listening_development",
            "primaryPurpose": "Develop auditory listening comprehension for a heated pastureland management meeting where local herders, soum environmental officers, and pasture group leaders debate rotational grazing schedules and fencing off reserve pastures.",
            "communicativeOutcome": "Understand authentic rural colloquial discourse, follow multi-party deliberations on communal natural resource governance, and detect conflicting local interests.",
            "objectivesIntroduced": ["obj_b1_143_03_comprehend_pasture_council_meeting"],
            "objectivesPracticed": ["obj_b1_143_01_pasture_degradation_lexicon"],
            "objectivesReviewed": ["obj_b1_135_03_debate_pastoral_geography"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_voice_reciprocal_collective"],
            "grammarReviewed": ["gram_b1_clause_temporal_omno_daraa_yed"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_ecological_compound_articulation"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_13_discussing_environmental_issues"],
            "communicativeFunctionsReviewed": ["comm_b1_04_respectful_disagreement"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_environment_geography_climate", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["малаа бэлчээх", "нөөц бэлчээр", "маргаан", "нэгдэл", "тохиролцох"],
            "readingObjective": "",
            "listeningObjective": "Listen to a 2.5-minute audio recording of a soum herders' council and summarize the agreement reached regarding winter reserve pastures.",
            "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "Authentic rural community deliberation and herder council register",
            "pragmaticTarget": "Decoding pastoral colloquialisms and consensus-building idioms.",
            "prerequisiteLessonIds": ["les_b1_143_01_pasture_degradation_lexicon", "les_b1_143_02_desertification_scientific_reading"],
            "reviewsLessonIds": ["les_b1_135_03_pastoral_lifestyles_comparative_discussion"],
            "reviewsUnitIds": ["unit_b1_135_geographical_landscapes_khangai_mou"],
            "reviewReason": "Expands seminar discussion into authentic rural communal resource negotiations.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic meeting room audio featuring expressive rural speakers negotiating pasture boundaries.",
            "successCriteria": [
                "Identifies the core conflict between short-term family grazing needs and collective pasture resting",
                "Recognizes reciprocal and collective verb forms denoting communal collaboration (-лцах, -лцаа)"
            ],
            "masteryEvidence": "Summarizes that herders agreed to rotate herds away from northern valley reserves until late November.",
            "recommendedExerciseModalities": ["audio_consensus_mapping", "speaker_position_matching", "summary_completion"]
        },
        {
            "lessonId": "les_b1_143_04_pastoral_conservation_action_dialogue",
            "unitId": uid_143, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Interactive Dialogue: Mediating Pasture Carrying Capacity & Herder Livelihoods",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate an interactive mediation between a soum agricultural advisor and an elder herder negotiating livestock head limits, livestock quality over quantity, and participation in sustainable pasture carbon credits.",
            "communicativeOutcome": "Negotiate delicate community resource agreements, balancing traditional herding autonomy with ecological survival imperatives.",
            "objectivesIntroduced": ["obj_b1_143_04_mediate_pastoral_dispute"],
            "objectivesPracticed": [
                "obj_b1_143_01_pasture_degradation_lexicon",
                "obj_b1_143_03_comprehend_pasture_council_meeting"
            ],
            "objectivesReviewed": ["obj_b1_133_03_conduct_consulting_session"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_clause_temporal_omno_daraa_yed"],
            "grammarReviewed": ["gram_a1_verb_tense_future_prospective_na"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_ecological_compound_articulation"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_13_discussing_environmental_issues"],
            "communicativeFunctionsReviewed": ["comm_b1_16_giving_advice_recommendations"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 3, "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_environment_geography_climate", "lex_b1_opinion_argumentation_rhetoric"],
            "previousVocabularyReused": ["малын чанар", "тоо толгой", "зөвлөх", "хамтрах", "үр ашиг"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Conduct an 8-turn negotiation counseling a herder family to transition from livestock quantity to high-yield livestock quality.",
            "registerTarget": "Respectful consultative community mediation register",
            "pragmaticTarget": "Showing deep cultural reverence for elders while firmly advocating scientific rangeland recovery.",
            "prerequisiteLessonIds": ["les_b1_143_02_desertification_scientific_reading", "les_b1_143_03_herder_community_roundtable_listening"],
            "reviewsLessonIds": ["les_b1_133_03_executive_advisory_consultation_dialogue"],
            "reviewsUnitIds": ["unit_b1_133_giving_professional_advice_actionab"],
            "reviewReason": "Applies professional consulting dialogue techniques to environmental and rural community mediation.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic dialogue between an agricultural advisor and an elder herder.",
            "successCriteria": [
                "Maintains culturally deferential tone while explaining ecological carrying capacity",
                "Proposes concrete economic incentives for maintaining sustainable herd sizes"
            ],
            "masteryEvidence": "Negotiates 'Малын тооноос илүү чанарт анхаарч, бэлчээрээ сэлгэн ашиглавал урт хугацаанд таны хотонд илүү үр өгөөжтэй' persuasively.",
            "recommendedExerciseModalities": ["branching_mediation", "cultural_politeness_drill", "spoken_roleplay"]
        }
    ])

    # =========================================================================
    # UNIT 144: Expedition Itinerary Capstone: Great Western Tour (Section Capstone)
    # Budget: (25, 18, 9, 5) across 5 lessons -> (6,5,2,1), (6,4,2,1), (6,5,2,1), (7,4,3,2), (0,0,0,0)
    # =========================================================================
    uid_144 = "unit_b1_144_expedition_itinerary_capstone_great"
    lessons.extend([
        {
            "lessonId": "les_b1_144_01_expedition_logistics_lexicon",
            "unitId": uid_144, "cefrLevel": "B1", "sequenceWithinUnit": 1,
            "title": "Expedition Logistics Lexicon: Altai Mountain Passes, Navigation & Survival",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Acquire high-level expedition, wilderness survival, and cross-country overland logistics terminology (бартаат зам, даваа гүвээ, шатахууны нөөц, майхан хэрэгсэл, хөтөч замчин, осол саадалгүй аялах) preparing for the Great Western Tour capstone across Bayan-Ölgii, Khovd, and Uvs.",
            "communicativeOutcome": "Plan, equip, and organize multi-week off-grid overland expeditions through rugged alpine and desert environments.",
            "objectivesIntroduced": ["obj_b1_144_01_expedition_logistics_lexicon"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_b1_136_01_administrative_geography_lexicon"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_aspect_intensive_chih_complete"],
            "grammarReviewed": ["gram_a2_case_instrumental_transport_language", "gram_b1_postpositions_similative_shig_adil_met"],
            "phonologyIntroduced": ["phono_b1_western_toponym_phonetics"],
            "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": ["comm_b1_06_stating_purpose_long_term_goals"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 5, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_travel_transport_tourism", "lex_b1_environment_geography_climate"],
            "previousVocabularyReused": ["аялал", "зам", "хэрэгсэл", "бэлтгэл", "уул", "машин"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Draft a comprehensive gear and emergency supply checklist for a 14-day overland expedition through the Altai Mountains.",
            "spokenProductionObjective": "Explain your emergency contingency plan if an expedition vehicle breaks down in a remote mountain pass.",
            "registerTarget": "Technical wilderness expedition and overland logistics register",
            "pragmaticTarget": "Anticipating extreme environmental contingencies and wilderness safety.",
            "prerequisiteLessonIds": ["les_b1_143_04_pastoral_conservation_action_dialogue"],
            "reviewsLessonIds": ["les_b1_136_01_administrative_aimags_lexicon"],
            "reviewsUnitIds": ["unit_b1_136_administrative_geography_the_21_aim"],
            "reviewReason": "Applies administrative geographic knowledge to intensive wilderness logistics planning.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronounce Western Mongolian geographical toponyms and logistics terms.",
            "successCriteria": [
                "Categorizes expedition gear, spare parts, and communication devices correctly",
                "Integrates intensive aspect (-чих) to indicate completed preparations"
            ],
            "masteryEvidence": "Produces 'Даваа давахаас өмнө бүх тоног төхөөрөмж, нөөц дугуйгаа бэлдчихсэн байх шаардлагатай' without error.",
            "recommendedExerciseModalities": ["expedition_gear_sorting", "contingency_matrix", "sentence_completion"]
        },
        {
            "lessonId": "les_b1_144_02_altai_expedition_dispatch_reading",
            "unitId": uid_144, "cefrLevel": "B1", "sequenceWithinUnit": 2,
            "title": "Reading Analysis: Field Dispatches from the Great Western Altai Expedition",
            "lessonType": "reading_development",
            "primaryPurpose": "Deconstruct authentic travelogue chronicles and field dispatches from explorers crossing Western Mongolia (Potanin Glacier, Tavan Bogd peaks, Kazakh eagle hunters, Dayan Lake).",
            "communicativeOutcome": "Extract route coordinates, trail conditions, cultural interactions, and geographical transitions from expedition literature.",
            "objectivesIntroduced": ["obj_b1_144_02_read_expedition_field_dispatches"],
            "objectivesPracticed": ["obj_b1_144_01_expedition_logistics_lexicon"], "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_aspect_intensive_chih_complete"],
            "grammarReviewed": ["gram_b1_postpositions_similative_shig_adil_met"],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_b1_06_stating_purpose_long_term_goals"],
            "communicativeFunctionsReviewed": ["comm_b1_13_discussing_environmental_issues"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_travel_transport_tourism", "lex_b1_culture_traditions_heritage"],
            "previousVocabularyReused": ["мөсөн гол", "оргил", "бүргэдчин", "казах түмэн", "нуур"],
            "readingObjective": "Read a 350-word expedition journal entry detailing the crossing of Baga Turgen waterfall and summiting Malchin Peak, identifying 3 navigational obstacles.",
            "listeningObjective": "", "writingObjective": "", "spokenProductionObjective": "",
            "registerTarget": "High literary travel narrative and field dispatch register",
            "pragmaticTarget": "Visualizing geographic terrain and cultural encounters through descriptive travel writing.",
            "prerequisiteLessonIds": ["les_b1_144_01_expedition_logistics_lexicon"],
            "reviewsLessonIds": ["les_b1_135_02_nomadic_adaptation_reading"],
            "reviewsUnitIds": ["unit_b1_135_geographical_landscapes_khangai_mou"],
            "reviewReason": "Expands geographic reading into personal field expedition narratives.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration of mountaineering expedition field diary.",
            "successCriteria": [
                "Extracts specific topographic milestones and altitude landmarks from text",
                "Understands cultural nuances of Kazakh hospitality and nomadic mountain traditions"
            ],
            "masteryEvidence": "Identifies that the team delayed their glacial ascent due to unexpected summer blizzards on Malchin Peak.",
            "recommendedExerciseModalities": ["route_mapping_from_text", "milestone_sequencing", "multiple_choice"]
        },
        {
            "lessonId": "les_b1_144_03_western_expedition_briefing_dialogue",
            "unitId": uid_144, "cefrLevel": "B1", "sequenceWithinUnit": 3,
            "title": "Interactive Dialogue: Comprehensive Route Briefing for the Western Circuit",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Conduct an extensive, multi-turn expedition briefing between an expedition leader and a team of scientific researchers walking through daily waypoints from Khovd through Ölgii to Uvs.",
            "communicativeOutcome": "Lead comprehensive technical travel briefings, assign operational roles, and resolve navigational logistics in spoken Mongolian.",
            "objectivesIntroduced": ["obj_b1_144_03_lead_expedition_briefing"],
            "objectivesPracticed": [
                "obj_b1_144_01_expedition_logistics_lexicon",
                "obj_b1_144_02_read_expedition_field_dispatches"
            ],
            "objectivesReviewed": ["obj_b1_142_04_brief_operational_protocol"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_aspect_intensive_chih_complete"],
            "grammarReviewed": ["gram_a2_case_instrumental_transport_language"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_b1_western_toponym_phonetics"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_06_stating_purpose_long_term_goals",
                "comm_b1_13_discussing_environmental_issues"
            ],
            "communicativeFunctionsReviewed": ["comm_b1_18_delegating_tasks_causative"],
            "newProductiveLemmaTarget": 6, "newReceptiveLemmaTarget": 5, "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_b1_travel_transport_tourism", "lex_b1_environment_geography_climate"],
            "previousVocabularyReused": ["маршрут", "хөтөч", "шатахуун", "жолооч", "хоноглох"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "",
            "spokenProductionObjective": "Conduct an 8-turn expedition briefing laying out driving segments, camp locations, and water refill points for Day 4 to Day 8.",
            "registerTarget": "Authoritative expedition leader and operational briefing register",
            "pragmaticTarget": "Projecting calm authority and meticulous safety awareness.",
            "prerequisiteLessonIds": ["les_b1_144_01_expedition_logistics_lexicon", "les_b1_144_02_altai_expedition_dispatch_reading"],
            "reviewsLessonIds": ["les_b1_142_04_procedural_briefing_dialogue"],
            "reviewsUnitIds": ["unit_b1_142_temporal_framing_clauses_"],
            "reviewReason": "Synthesizes procedural briefing skills with nationwide geographical travel logistics.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic dialogue between an expedition leader and team members reviewing maps.",
            "successCriteria": [
                "Articulates complex geographic routing across multiple aimags without confusion",
                "Employs intensive aspect and temporal markers to sequence route phases clearly"
            ],
            "masteryEvidence": "Negotiates 'Өлгий хотоос гараад Толбо нуураар дайрч, Цамбагарав уулын бэлд очиж хоноглочихвол маргааш нь зам дөхөм болно' fluently.",
            "recommendedExerciseModalities": ["branching_route_briefing", "contingency_handling_drill", "spoken_roleplay"]
        },
        {
            "lessonId": "les_b1_144_04_great_western_itinerary_writing",
            "unitId": uid_144, "cefrLevel": "B1", "sequenceWithinUnit": 4,
            "title": "Writing Workshop: Authoring a 14-Day Great Western Tour Expedition Itinerary",
            "lessonType": "writing",
            "primaryPurpose": "Compose a detailed, publication-grade 200-word formal expedition itinerary document outlining a 14-day Western Mongolian traverse: daily driving kilometers, terrain descriptions, cultural milestones, ecological conservation protocols, and emergency evacuation coordinates.",
            "communicativeOutcome": "Author professional tourism and scientific expedition documentation conforming to international adventure travel standards in Mongolian.",
            "objectivesIntroduced": ["obj_b1_144_04_author_expedition_itinerary_document"],
            "objectivesPracticed": [
                "obj_b1_144_01_expedition_logistics_lexicon",
                "obj_b1_144_03_lead_expedition_briefing"
            ],
            "objectivesReviewed": ["obj_b1_133_04_write_advisory_memo"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_b1_aspect_intensive_chih_complete"],
            "grammarReviewed": [
                "gram_a2_case_instrumental_transport_language",
                "gram_b1_postpositions_similative_shig_adil_met"
            ],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_06_stating_purpose_long_term_goals",
                "comm_b1_13_discussing_environmental_issues"
            ],
            "communicativeFunctionsReviewed": ["comm_b1_10_writing_formal_email_letter"],
            "newProductiveLemmaTarget": 7, "newReceptiveLemmaTarget": 4, "newProductiveExpressionTarget": 3, "newReceptiveExpressionTarget": 2,
            "lexicalDomains": ["lex_b1_travel_transport_tourism", "lex_b1_environment_geography_climate"],
            "previousVocabularyReused": ["хөтөлбөр", "замнал", "километр", "үзвэр", "байгаль хамгаалал"],
            "readingObjective": "", "listeningObjective": "",
            "writingObjective": "Author a 200-word comprehensive expedition itinerary for a 14-day Western Tour incorporating daily targets, terrain conditions, and environmental rules.",
            "spokenProductionObjective": "",
            "registerTarget": "High professional adventure tourism and expedition publication register",
            "pragmaticTarget": "Producing meticulous, client-ready logistical and cultural travel documents.",
            "prerequisiteLessonIds": ["les_b1_144_02_altai_expedition_dispatch_reading", "les_b1_144_03_western_expedition_briefing_dialogue"],
            "reviewsLessonIds": ["les_b1_133_04_consulting_memorandum_writing"],
            "reviewsUnitIds": ["unit_b1_133_giving_professional_advice_actionab"],
            "reviewReason": "Synthesizes structured memorandum writing into comprehensive expedition itinerary authoring.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Provide audio playback of the completed expedition itinerary document.",
            "successCriteria": [
                "Structures itinerary into Overview, Daily Waypoints, Logistics & Safety, and Environmental Ethics",
                "Applies aimag names, terrain descriptors, and purposive/temporal clauses accurately"
            ],
            "masteryEvidence": "Submits an itinerary opening with 'Баруун Монголын байгаль, соёлын гайхамшгийг таниулах 14 хоногийн аяллын замнал' and sustaining professional rigor throughout.",
            "recommendedExerciseModalities": ["guided_itinerary_composition", "waypoint_bulleting", "peer_review"]
        },
        {
            "lessonId": "les_b1_144_05_section_03_milestone_synthesis_checkpoint",
            "unitId": uid_144, "cefrLevel": "B1", "sequenceWithinUnit": 5,
            "title": "Section Milestone Checkpoint: Geography, Environment & Complex Subordination",
            "lessonType": "milestone_checkpoint",
            "primaryPurpose": "Comprehensive synthesis and formal benchmark assessment across all Section 03 competencies: physical landscapes (Khangai vs Gobi), 21 aimags administration, nominalized participles in oblique cases (-сныг, -санд, -снаас, -снаар), subordinate subject genitive marking (-ын хийсэн), purposive clauses (-хын тулд, -ын төлөө), agentive derivation (-гч), similative postpositions (шиг, адил, мэт), temporal framing clauses (-хын өмнө, -сны дараа, -х үед), rangeland ecology, and expedition planning.",
            "communicativeOutcome": "Demonstrate integrated mastery of B1 geographic knowledge, ecological argumentation, and advanced complex clause subordination in a multi-skill simulated environmental summit challenge.",
            "objectivesIntroduced": ["obj_b1_144_05_section_03_synthesis_milestone"],
            "objectivesPracticed": [
                "obj_b1_135_01_geographical_landforms_lexicon",
                "obj_b1_136_01_administrative_geography_lexicon",
                "obj_b1_137_01_decline_nominalized_participles",
                "obj_b1_138_01_mark_subordinate_subject_genitive",
                "obj_b1_139_01_form_purposive_clauses",
                "obj_b1_140_01_form_agentive_participles",
                "obj_b1_141_01_form_similative_comparisons",
                "obj_b1_142_01_form_temporal_framing_clauses",
                "obj_b1_143_01_pasture_degradation_lexicon",
                "obj_b1_144_04_author_expedition_itinerary_document"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": [
                "gram_b1_nominalization_participles_cases",
                "gram_b1_subordinate_subject_marking_genitive",
                "gram_b1_clause_purposive_tuld_tuloo",
                "gram_b1_participle_agentive_gch",
                "gram_b1_postpositions_similative_shig_adil_met",
                "gram_b1_clause_temporal_omno_daraa_yed"
            ],
            "grammarReviewed": [],
            "phonologyIntroduced": [], "phonologyPracticed": [], "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": [
                "comm_b1_23_comparing_city_country_lifestyles",
                "comm_b1_06_stating_purpose_long_term_goals",
                "comm_b1_24_discussing_education_career_path",
                "comm_b1_08_speculating_visual_evidence",
                "comm_b1_02_sequencing_past_chronology",
                "comm_b1_13_discussing_environmental_issues"
            ],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0, "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": [
                "lex_b1_environment_geography_climate",
                "lex_b1_travel_transport_tourism",
                "lex_b1_education_career_workplace",
                "lex_b1_culture_traditions_heritage"
            ],
            "previousVocabularyReused": [
                "байгаль", "аймаг", "бэлчээр", "хамгаалах", "зорилго",
                "судлаач", "мэт", "өмнө", "дараа", "аялал"
            ],
            "readingObjective": "Read a 350-word regional environmental and development synthesis report on sustainable ecotourism in Western Mongolia.",
            "listeningObjective": "Comprehend a 3-minute panel discussion between aimag governors and conservation scientists debating protected area expansion.",
            "writingObjective": "Author a 150-word policy memorandum proposing an eco-corridor linking two national parks.",
            "spokenProductionObjective": "Deliver a 2.5-minute formal presentation proposing a sustainable expedition plan that protects local pastures and respects nomadic communities.",
            "registerTarget": "Full B1 environmental, geographic, and complex syntactic standard",
            "pragmaticTarget": "Seamlessly weaving complex subordinate clauses to express causes, purposes, conditions, and temporal sequences in civic discourse.",
            "prerequisiteLessonIds": [
                "les_b1_144_03_western_expedition_briefing_dialogue",
                "les_b1_144_04_great_western_itinerary_writing"
            ],
            "reviewsLessonIds": [
                "les_b1_135_04_geographic_landscape_monologue_spoken",
                "les_b1_137_05_advocating_conservation_goals_spoken",
                "les_b1_138_05_mentorship_tribute_spoken",
                "les_b1_139_04_grant_proposal_pitch_spoken",
                "les_b1_141_04_lyrical_landscape_monologue_spoken",
                "les_b1_142_05_chronological_case_study_writing",
                "les_b1_143_04_pastoral_conservation_action_dialogue"
            ],
            "reviewsUnitIds": [
                "unit_b1_135_geographical_landscapes_khangai_mou",
                "unit_b1_137_nominalization_of_participles_in_ob",
                "unit_b1_138_subordinate_subject_genitive_case_m",
                "unit_b1_139_purposive_clauses_conjunctions_and_",
                "unit_b1_141_similative_postpositions_",
                "unit_b1_142_temporal_framing_clauses_",
                "unit_b1_143_environmental_conservation_pasture_"
            ],
            "reviewReason": "Caps Section 03 with a comprehensive multi-skill benchmark synthesizing geographical knowledge, ecological debate, and complex clause syntax.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Regional environmental summit keynote listening benchmark.",
            "successCriteria": [
                "Demonstrates mastery across all Section 03 complex clause structures in reading, writing, and speaking",
                "Maintains sophisticated geographic and environmental vocabulary throughout oral and written production"
            ],
            "masteryEvidence": "Achieves 85%+ on integrated multi-skill milestone rubric covering written policy memo, oral presentation, and listening comprehension.",
            "recommendedExerciseModalities": [
                "environmental_summit_simulation",
                "multi_skill_benchmark_exam",
                "logistics_and_conservation_presentation"
            ]
        }
    ])

    return lessons
