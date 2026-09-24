"""
Section 2 Lesson Blueprint Builder: Units 24 - 33
Physical Space, Quantities, and Locative Grounding
10 Units, 58 Lessons
"""

import json

def build_section_02():
    with open("curriculum/blueprint/units/a1.json") as f:
        units_raw = json.load(f)
    unit_map = {u["sequencePosition"]: u for u in units_raw}

    lessons = []

    # =========================================================================
    # UNIT 24: Existential Assertion: Байна vs Байхгүй (pos 24)
    # Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2 | Lessons: 6
    # =========================================================================
    u24 = unit_map[24]
    lessons.extend([
        {
            "lessonId": "les_a1_24_01_existential_assertion_baina",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 1,
            "title": "Affirming Presence: The Existential Predicate Байна",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the existential predicate 'байна' to express the physical presence and availability of items or persons.",
            "communicativeOutcome": "State that a person, room amenity, or household object is present at a specified location.",
            "objectivesIntroduced": ["obj_a1_24_01_affirm_existence_baina"],
            "objectivesPracticed": [],
            "objectivesReviewed": ["obj_a1_20_01_deictic_identification"],
            "grammarIntroduced": ["gram_a1_existential_baina_baihgui"],
            "grammarPracticed": [],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_nominal_predicate_zero_copula"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5,
            "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1,
            "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ном", "ширээ", "багш"],
            "readingObjective": "Read short affirmative room descriptions identifying which furnishings are present.",
            "listeningObjective": "Distinguish between copular identification ('Энэ ширээ') and existential affirmation ('Ширээ байна').",
            "writingObjective": "Construct 3 existential sentences asserting the presence of items in a living space.",
            "spokenProductionObjective": "State aloud three items currently present in the immediate room.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Clear matter-of-fact confirmation of available resources without over-elaboration.",
            "prerequisiteLessonIds": ["les_a1_23_05_interactive_social_reception_simulation"],
            "reviewsLessonIds": ["les_a1_20_02_spatial_demonstratives_here_there"],
            "reviewsUnitIds": ["unit_a1_20_demonstrative_deixis_"],
            "reviewReason": "Anchor spatial deictics to existential predication.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Acoustic discrimination between short non-initial vowel in 'байна' and lengthened lexical vowels.",
            "successCriteria": [
                "Select 'байна' appropriately in existential sentence frames rather than zero-copula identity structures.",
                "Accurately pronounce 'байна' with neutral non-initial vowel reduction."
            ],
            "masteryEvidence": [
                "Produces 'Цай байна' when prompted with tea imagery.",
                "Corrects faulty SVO word order into canonical 'Noun + байна'."
            ],
            "recommendedExerciseModalities": ["cloze_selection", "cued_production", "matching"]
        },
        {
            "lessonId": "les_a1_24_02_existential_negation_baihgui",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 2,
            "title": "Negating Existence: Contrast Between Байхгүй and Биш",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Differentiate categorical existential absence ('байхгүй') from nominal identity negation ('биш').",
            "communicativeOutcome": "State that a person or resource is unavailable or absent, without confusing entity negation with identity negation.",
            "objectivesIntroduced": ["obj_a1_24_02_negate_existence_baihgui"],
            "objectivesPracticed": [],
            "objectivesReviewed": ["obj_a1_21_01_nominal_negation_bish"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_nominal_negation_bish"],
            "grammarReinforced": ["gram_a1_nominal_negation_bish"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_oe_ue_contrast"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5,
            "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1,
            "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ус", "цаас", "үзэг", "эмч"],
            "readingObjective": "Read signage and status notices indicating lack of inventory or absence of staff.",
            "listeningObjective": "Detect negative existential particle 'байхгүй' in spoken announcements.",
            "writingObjective": "Write pairs of sentences contrasting identity ('Энэ ус биш') and absence ('Ус байхгүй').",
            "spokenProductionObjective": "State aloud the absence of two specific office or household items upon prompt.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Polite indication of non-availability to prevent guest disappointment.",
            "prerequisiteLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsLessonIds": ["les_a1_21_02_copular_negation_usage_drills"],
            "reviewsUnitIds": ["unit_a1_21_negative_nominal_assertion_the_copu"],
            "reviewReason": "Systematically resolve the common learner confusion between 'биш' and 'байхгүй'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear pitch modulation on negative particle 'байхгүй'.",
            "successCriteria": [
                "Select 'байхгүй' when denying existence and 'биш' when denying identity.",
                "Accurately articulate the long diphthong in 'байхгүй'."
            ],
            "masteryEvidence": [
                "Sorts 8 visual prompts into '... биш' vs '... байхгүй' without errors.",
                "Produces 'Сүү байхгүй' when milk carton is empty."
            ],
            "recommendedExerciseModalities": ["binary_choice", "sentence_transformation", "listening_comprehension"]
        },
        {
            "lessonId": "les_a1_24_03_polar_inquiries_existence",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 3,
            "title": "Inquiring About Availability: Байна уу? / Байгаа юу?",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Form polar questions inquiring whether items or services are present using question particles.",
            "communicativeOutcome": "Ask hotel receptionists, hosts, or clerks if specific items or facilities are available.",
            "objectivesIntroduced": ["obj_a1_24_03_ask_polar_existence"],
            "objectivesPracticed": ["obj_a1_24_01_affirm_existence_baina", "obj_a1_24_02_negate_existence_baihgui"],
            "objectivesReviewed": ["obj_a1_19_01_polar_question_particles"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu"],
            "grammarReinforced": ["gram_a1_polar_questions_uu_uu"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_vowel_harmony_intro"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_04_inquire_wellbeing_polar"],
            "newProductiveLemmaTarget": 4,
            "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1,
            "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["өрөө", "түлхүүр", "интернет"],
            "readingObjective": "Read customer inquiry FAQs regarding available guest amenities.",
            "listeningObjective": "Identify whether an inquiry is asking about presence ('Байна уу?') or identity ('Мөн үү?').",
            "writingObjective": "Formulate 4 inquiry questions regarding household or hotel facilities.",
            "spokenProductionObjective": "Ask a partner whether 3 essential daily items are available.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Framing requests as availability inquiries to maintain conversational deference.",
            "prerequisiteLessonIds": ["les_a1_24_02_existential_negation_baihgui"],
            "reviewsLessonIds": ["les_a1_19_02_polar_inquiry_drill_answering"],
            "reviewsUnitIds": ["unit_a1_19_polar_inquiries_polar_question_part"],
            "reviewReason": "Harmonize polar question particles with the back vowel stem of 'байна'.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic final rising-falling pitch contour on 'Байна уу?'.",
            "successCriteria": [
                "Select back-vowel question particle 'уу' matching 'байна'.",
                "Produce appropriate short affirmative ('Байна') or negative ('Байхгүй' / 'Алга') replies."
            ],
            "masteryEvidence": [
                "Conducts a 4-turn mini-inquiry verifying key amenities.",
                "Recognizes informal 'алга' as semantic equivalent to 'байхгүй' in receptive audio."
            ],
            "recommendedExerciseModalities": ["question_formation", "audio_response_matching", "interactive_drill"]
        },
        {
            "lessonId": "les_a1_24_04_ger_interior_inventory_reading",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 4,
            "title": "Reading Exploration: Traditional Ger Furnishings and Layout",
            "lessonType": "reading_development",
            "primaryPurpose": "Read descriptive paragraphs describing traditional items found inside a Mongolian yurt (ger).",
            "communicativeOutcome": "Extract key factual information about traditional household items and their customary presence.",
            "objectivesIntroduced": ["obj_a1_24_04_read_ger_inventory"],
            "objectivesPracticed": ["obj_a1_24_01_affirm_existence_baina", "obj_a1_24_02_negate_existence_baihgui"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": [],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3,
            "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1,
            "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ор", "зуух", "авдар", "тооно"],
            "readingObjective": "Read a 45-word illustrated text about the interior furnishings of a nomadic dwelling.",
            "listeningObjective": None,
            "writingObjective": "Extract a checklist of 5 items confirmed as present in the reading text.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Respectful familiarity with sacred and domestic spaces within the traditional ger.",
            "prerequisiteLessonIds": ["les_a1_24_03_polar_inquiries_existence"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_20_demonstrative_deixis_"],
            "reviewReason": "Ground reading comprehension in demonstrated domestic spatial vocabulary.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Authentic text read-along with correct phrasal rhythm.",
            "successCriteria": [
                "Answer 4 factual true/false questions based on the text without error.",
                "Identify the 3 cultural centerpieces mentioned in the passage (тооно, багана, зуух)."
            ],
            "masteryEvidence": [
                "Selects correct items present in the text from an illustrated grid.",
                "Accurately translates 3 existential sentences into English equivalents."
            ],
            "recommendedExerciseModalities": ["reading_comprehension", "item_matching", "true_false"]
        },
        {
            "lessonId": "les_a1_24_05_reception_inquiry_listening",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Tracking Availability at Customer Service",
            "lessonType": "listening_development",
            "primaryPurpose": "Consolidate auditory comprehension of existential queries and responses in rapid service interactions.",
            "communicativeOutcome": "Accurately decipher whether requested items or staff members are available from fast spoken Mongolian.",
            "objectivesIntroduced": ["obj_a1_24_05_auditory_availability_tracking"],
            "objectivesPracticed": ["obj_a1_24_03_ask_polar_existence"],
            "objectivesReviewed": ["obj_a1_24_02_negate_existence_baihgui"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu"],
            "grammarReinforced": ["gram_a1_nominal_negation_bish"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0,
            "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0,
            "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["түлхүүр", "өрөө", "интернет", "ус", "цаас"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 short dialogic exchanges at a hotel desk and determine presence/absence status.",
            "writingObjective": "Fill out a status chart marking items as [+] present, [-] absent, or [?] inquiring.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Recognizing indirect polite hedges in customer reception discourse.",
            "prerequisiteLessonIds": ["les_a1_24_03_polar_inquiries_existence"],
            "reviewsLessonIds": ["les_a1_24_02_existential_negation_baihgui"],
            "reviewsUnitIds": ["unit_a1_21_negative_nominal_assertion_the_copu"],
            "reviewReason": "Reinforce acoustic discrimination of negation types in spoken dialogue.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic conversational speech with natural background ambient sounds and conversational tempo.",
            "successCriteria": [
                "Correctly categorize 4 out of 4 audio dialogue outcomes as available vs unavailable.",
                "Identify the exact item queried in each dialogue from audio alone."
            ],
            "masteryEvidence": [
                "Accurately maps spoken items to an availability status matrix.",
                "Transcribes the key response word ('байхгүй' or 'байна') with accurate spelling."
            ],
            "recommendedExerciseModalities": ["listening_comprehension", "status_table_completion", "audio_discrimination"]
        },
        {
            "lessonId": "les_a1_24_06_household_inventory_dialogue",
            "unitId": u24["unitId"],
            "cefrLevel": "A1",
            "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Household and Office Asset Check",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Synthesize existential assertions, inquiries, and negations in an unscripted cooperative task.",
            "communicativeOutcome": "Cooperate with a conversation partner to determine what equipment is in the room and what needs to be procured.",
            "objectivesIntroduced": ["obj_a1_24_06_execute_inventory_dialogue"],
            "objectivesPracticed": [
                "obj_a1_24_01_affirm_existence_baina",
                "obj_a1_24_02_negate_existence_baihgui",
                "obj_a1_24_03_ask_polar_existence"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_polar_questions_uu_uu", "gram_a1_nominal_negation_bish"],
            "grammarReinforced": ["gram_a1_nominal_negation_bish"],
            "phonologyIntroduced": [],
            "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_formal_greeting_morning_afternoon"],
            "newProductiveLemmaTarget": 0,
            "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0,
            "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ширээ", "сандал", "компьютер", "цаас", "үзэг", "ном"],
            "readingObjective": "Read situational role cards specifying missing and available items.",
            "listeningObjective": "Comprehend partner inquiries regarding available workplace tools.",
            "writingObjective": "Draft a 4-bullet inventory summary of verified and missing equipment.",
            "spokenProductionObjective": "Participate in a 6-turn roleplay checking room readiness.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Constructive collaboration and polite clarification during joint practical tasks.",
            "prerequisiteLessonIds": [
                "les_a1_24_04_ger_interior_inventory_reading",
                "les_a1_24_05_reception_inquiry_listening"
            ],
            "reviewsLessonIds": ["les_a1_24_02_existential_negation_baihgui"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Consolidate Unit 24 existential competence without adding cognitive vocabulary burden.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary interactive exchange demonstrating realistic pauses and intonation turns.",
            "successCriteria": [
                "Complete all 6 turns of the dialogue maintaining accurate existential predicate usage.",
                "Never confuse 'биш' and 'байхгүй' throughout the oral performance."
            ],
            "masteryEvidence": [
                "Spontaneously clarifies missing items when asked 'Түлхүүр байна уу?'.",
                "Pronounces all consonant clusters cleanly without inserting illegal epenthetic vowels."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "error_spotting"]
        }
    ])

    # Let's verify sum of U24:
    # ProdLem: 5+5+4+3+0+0 = 17 (exact)
    # RecLem: 2+2+1+1+0+0 = 6 (exact)
    # ProdExp: 1+1+1+1+0+0 = 4 (exact)
    # RecExp: 1+0+1+0+0+0 = 2 (exact)

    # Continue with Unit 25..33 in the builder
    return lessons
