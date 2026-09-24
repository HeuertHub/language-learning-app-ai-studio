"""
Section 2 Generator: Full 58 Lesson Blueprints (Units 24 - 33)
"""

import json
from typing import List, Dict, Any

def generate_section_02():
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}

    # Load previously written U24 and U25 from sec02_builder
    from sec02_builder import get_sec02_lessons
    lessons = get_sec02_lessons()

    # =========================================================================
    # UNIT 26: Content Question Particles: Бэ and Вэ (pos 26)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # =========================================================================
    u = u_map[26]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_26_01_content_particles_distribution",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Interrogative Markers: Phonological Selection of Бэ vs Вэ",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the complementary phonological distribution of content question particles 'бэ' (after sonorants and nasals) and 'вэ' (after vowels and other consonants).",
            "communicativeOutcome": "Formulate wh-questions asking 'Who?', 'What?', and 'Where?' using the phonologically correct question particle.",
            "objectivesIntroduced": ["obj_a1_26_01_select_be_ve_particles"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_19_01_polar_question_particles"],
            "grammarIntroduced": ["gram_a1_content_questions_be_ve"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["хэн", "юу", "хаана", "хэзээ"],
            "readingObjective": "Read question-and-answer pairs matching question stems with either бэ or вэ.",
            "listeningObjective": "Hear the acoustic shift between 'Хэн бэ?' (nasal final) and 'Юу вэ?' (vowel final).",
            "writingObjective": "Complete 6 interrogative sentences by selecting the correct particle бэ or вэ based on the preceding terminal sound.",
            "spokenProductionObjective": "Accurately pronounce 4 content questions with appropriate terminal particle and pitch.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Natural questioning tone without abrupt or aggressive intonation.",
            "prerequisiteLessonIds": ["les_a1_25_06_campus_orientation_synthesis"],
            "reviewsLessonIds": ["les_a1_19_01_polar_particle_harmony"],
            "reviewsUnitIds": ["unit_a1_19_polar_inquiries_polar_question_part"],
            "reviewReason": "Contrast polar question particles (уу/үү) with content question particles (бэ/вэ).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear acoustic differentiation between bilabial plosive /b/ and fricative/approximant /w/.",
            "successCriteria": [
                "Select 'бэ' after m, n, ng, l stems and 'вэ' after vowels and non-nasal consonants.",
                "Apply terminal falling question intonation characteristic of Mongolian content questions."
            ],
            "masteryEvidence": [
                "Correctly selects particle for 'Хэн ...' (бэ) vs 'Энэ юу ...' (вэ) with 100% accuracy.",
                "Explains the phonological rule governing particle choice."
            ],
            "recommendedExerciseModalities": ["cloze_selection", "phonetic_sorting", "question_formation"]
        },
        {
            "lessonId": "les_a1_26_02_interrogative_pronoun_inventory",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Question Words: Хэн, Юу, Хаана, and Аль",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce and drill key interrogative pronouns and their syntactic placement in SOV question clauses.",
            "communicativeOutcome": "Ask targeted questions regarding identity, object category, spatial location, and selection among options.",
            "objectivesIntroduced": ["obj_a1_26_02_use_interrogative_pronouns"],
            "objectivesPracticed": ["obj_a1_26_01_select_be_ve_particles"],
            "objectivesReviewed": ["obj_a1_20_01_deictic_identification"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_10_identifying_objects"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["хүн", "бараа", "хот", "өрөө"],
            "readingObjective": "Read a dialogue transcript containing varied wh-questions and answers.",
            "listeningObjective": "Identify which question word was used in fast spoken prompts.",
            "writingObjective": "Write 4 distinct content questions using хэн, юу, хаана, and аль.",
            "spokenProductionObjective": "Ask a peer 3 wh-questions about unfamiliar objects and persons in a photo.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Directing inquiries precisely to elicit targeted factual information.",
            "prerequisiteLessonIds": ["les_a1_26_01_content_particles_distribution"],
            "reviewsLessonIds": ["les_a1_20_01_spatial_demonstratives_core_deixis"],
            "reviewsUnitIds": ["unit_a1_20_demonstrative_deixis_"],
            "reviewReason": "Link interrogative pronouns to demonstrative answers (Аль нь? - Энэ нь).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural sentence-level intonation on content question frames.",
            "successCriteria": [
                "Position the interrogative pronoun directly before the verb or predicate noun.",
                "Pair 'аль' with selective partitive markers when choosing from a set."
            ],
            "masteryEvidence": [
                "Produces 'Та хэн бэ?' and 'Энэ юу вэ?' without hesitation.",
                "Transforms affirmative statements into corresponding wh-questions."
            ],
            "recommendedExerciseModalities": ["sentence_transformation", "cued_production", "matching"]
        },
        {
            "lessonId": "les_a1_26_03_inquiry_clarification_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Seeking Factual Clarification",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate the formulation and comprehension of rapid content questions in everyday informational encounters.",
            "communicativeOutcome": "Clarify ambiguous identities, misplaced items, and unknown vocabulary by asking clarifying questions.",
            "objectivesIntroduced": ["obj_a1_26_03_conduct_clarification_drills"],
            "objectivesPracticed": [
                "obj_a1_26_01_select_be_ve_particles",
                "obj_a1_26_02_use_interrogative_pronouns"
            ],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["овог", "нэр", "ажил", "мэргэжил"],
            "readingObjective": "Read administrative registration interview prompts.",
            "listeningObjective": "Comprehend spoken requests for personal details (Нэр тань хэн бэ?).",
            "writingObjective": "Draft 5 registration inquiry questions for a student enrollment intake.",
            "spokenProductionObjective": "Roleplay an administrative intake clerk asking 4 clarification questions.",
            "registerTarget": "Courteous standard official",
            "pragmaticTarget": "Maintaining polite respect while gathering essential administrative data.",
            "prerequisiteLessonIds": ["les_a1_26_02_interrogative_pronoun_inventory"],
            "reviewsLessonIds": ["les_a1_25_04_spatial_inquiries_qa"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine locative inquiries ('Хаана байна?') with personal identity questions.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic courteous administrative question intonation.",
            "successCriteria": [
                "Incorporate honorific second-person markers (Таны нэр хэн бэ?) seamlessly.",
                "Ensure correct particle alignment across varied noun endings."
            ],
            "masteryEvidence": [
                "Conducts a smooth 1-minute simulated registration intake interview.",
                "Corrects deliberately flawed question particles in peer speech."
            ],
            "recommendedExerciseModalities": ["cloze_selection", "audio_response_matching", "interactive_drill"]
        },
        {
            "lessonId": "les_a1_26_04_interview_transcript_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Short Interview Profiles and FAQs",
            "lessonType": "reading_development",
            "primaryPurpose": "Read and analyze authentic Q&A profiles, interview transcripts, and civic questionnaire excerpts.",
            "communicativeOutcome": "Extract biographical and factual details from structured question-and-answer texts.",
            "objectivesIntroduced": ["obj_a1_26_04_read_interview_profiles"],
            "objectivesPracticed": ["obj_a1_26_02_use_interrogative_pronouns"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["оюутан", "эмч", "хот", "сургууль"],
            "readingObjective": "Read a 50-word interview profile of an incoming university student.",
            "listeningObjective": None,
            "writingObjective": "Write a 3-question profile inquiry for an interview with a classmate.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Extracting targeted answers to factual questions in written texts.",
            "prerequisiteLessonIds": ["les_a1_26_03_inquiry_clarification_drills"],
            "reviewsLessonIds": ["les_a1_26_01_content_particles_distribution"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Consolidate recognition of wh-particle structures in authentic reading texts.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Read-along narration modeling rhythm of printed interviews.",
            "successCriteria": [
                "Locate answers to who, what, where, and which questions in the profile.",
                "Match question headings to their corresponding response paragraphs."
            ],
            "masteryEvidence": [
                "Completes a profile summary chart with zero comprehension errors.",
                "Identifies the grammatical role of бэ and вэ in 5 textual questions."
            ],
            "recommendedExerciseModalities": ["reading_comprehension", "profile_mapping", "true_false"]
        },
        {
            "lessonId": "les_a1_26_05_interrogative_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Rapid Question Parsing in Conversational Speech",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse rapid content questions in multi-speaker audio clips to identify inquiry goals instantly.",
            "communicativeOutcome": "Immediately determine what information is being requested in rapid natural conversations.",
            "objectivesIntroduced": ["obj_a1_26_05_parse_rapid_questions_auditorily"],
            "objectivesPracticed": ["obj_a1_26_01_select_be_ve_particles"],
            "objectivesReviewed": ["obj_a1_24_03_ask_polar_existence"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu"],
            "grammarReinforced": ["gram_a1_polar_questions_uu_uu"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["хэн", "юу", "хаана", "хэзээ", "аль"],
            "readingObjective": None,
            "listeningObjective": "Listen to 6 rapid conversational questions and categorize each by information target.",
            "writingObjective": "Write down the question particle (бэ/вэ/уу/үү) heard in each audio clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial and courteous",
            "pragmaticTarget": "Fast auditory comprehension without requiring repetition.",
            "prerequisiteLessonIds": ["les_a1_26_03_inquiry_clarification_drills"],
            "reviewsLessonIds": ["les_a1_24_05_reception_inquiry_listening"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Contrast polar question intonation with wh-question intonation in natural audio.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational tempo with natural reductions and elisions.",
            "successCriteria": [
                "Classify 6 out of 6 spoken questions into polar vs content categories correctly.",
                "Identify the specific question word uttered in noisy listening conditions."
            ],
            "masteryEvidence": [
                "Selects the appropriate factual response to each question from 3 options.",
                "Accurately transcribes heard question particles."
            ],
            "recommendedExerciseModalities": ["listening_comprehension", "audio_categorization", "dictation"]
        },
        {
            "lessonId": "les_a1_26_06_inquiry_dialogue_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Civic and Campus Fact-Finding Mission",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Integrate content questions, answers, and spatial grounding in a cooperative information-gap task.",
            "communicativeOutcome": "Gather complete factual dossiers on unfamiliar people, objects, and locations through reciprocal questioning.",
            "objectivesIntroduced": ["obj_a1_26_06_conduct_fact_finding_dialogue"],
            "objectivesPracticed": [
                "obj_a1_26_01_select_be_ve_particles",
                "obj_a1_26_02_use_interrogative_pronouns",
                "obj_a1_26_03_conduct_clarification_drills"
            ],
            "objectivesReviewed": ["obj_a1_25_02_locate_people_spatially"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_05_asking_identity_origin"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_personal_identity_civics"],
            "previousVocabularyReused": ["хэн", "юу", "хаана", "сургууль", "багш", "ном", "өрөө"],
            "readingObjective": "Read information-gap dossier cards detailing incomplete facts.",
            "listeningObjective": "Comprehend partner's questions and verbal answers in an information exchange.",
            "writingObjective": "Record 4 facts elicited from partner into an information table.",
            "spokenProductionObjective": "Execute an 8-turn unscripted information-gap dialogue.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Reciprocal conversational cooperation and clear articulation of inquiries.",
            "prerequisiteLessonIds": [
                "les_a1_26_04_interview_transcript_reading",
                "les_a1_26_05_interrogative_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_26_02_interrogative_pronoun_inventory"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Full mastery checkpoint of Unit 26 without added lexical load.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange showcasing reciprocal question-answer pacing.",
            "successCriteria": [
                "Formulate 4 grammatically correct wh-questions using appropriate бэ/вэ particles.",
                "Successfully extract all missing information to complete the dossier table."
            ],
            "masteryEvidence": [
                "Conducts full interactive exchange without reverting to English or using incorrect particles.",
                "Scores 100% on the factual details recorded in the final dossier."
            ],
            "recommendedExerciseModalities": ["information_gap", "dialogue_roleplay", "dossier_completion"]
        }
    ])

    return lessons
