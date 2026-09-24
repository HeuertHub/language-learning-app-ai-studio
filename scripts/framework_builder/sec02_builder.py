"""
Section 2 Builder: Units 24 - 33 (10 Units, 58 Lessons)
Physical Space, Quantities, and Locative Grounding
"""

import json
from typing import List, Dict, Any

def get_sec02_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}

    lessons = []

    # =========================================================================
    # UNIT 24: Existential Assertion: Байна vs Байхгүй (pos 24)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # =========================================================================
    u = u_map[24]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_24_01_existential_assertion_baina",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Affirming Presence: The Existential Predicate Байна",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the existential predicate 'байна' to express the physical presence and availability of items or persons.",
            "communicativeOutcome": "State that a person, room amenity, or household object is present at a specified location.",
            "objectivesIntroduced": ["obj_a1_24_01_affirm_existence_baina"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_20_01_deictic_identification"],
            "grammarIntroduced": ["gram_a1_existential_baina_baihgui"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_nominal_predicate_zero_copula"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
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
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Negating Existence: Contrast Between Байхгүй and Биш",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Differentiate categorical existential absence ('байхгүй') from nominal identity negation ('биш').",
            "communicativeOutcome": "State that a person or resource is unavailable or absent, without confusing entity negation with identity negation.",
            "objectivesIntroduced": ["obj_a1_24_02_negate_existence_baihgui"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_21_01_nominal_negation_bish"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_existential_baina_baihgui"],
            "grammarReviewed": ["gram_a1_nominal_negation_bish"],
            "grammarReinforced": ["gram_a1_nominal_negation_bish"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_oe_ue_contrast"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
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
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
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
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_intro"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_04_inquire_wellbeing_polar"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
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
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
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
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
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
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
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
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
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
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
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
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_formal_greeting_morning_afternoon"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
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

    # =========================================================================
    # UNIT 25: Dative-Locative Spatial Anchoring: Suffixes -д/-т (pos 25)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # =========================================================================
    u = u_map[25]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_25_01_dative_locative_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Locating Entities: Dative-Locative Suffixes -д and -т",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce the dative-locative case markers (-д after vowels and sonorant consonants; -т after voiceless stops) to express spatial location.",
            "communicativeOutcome": "State where an object or person is located using correct case suffix allomorphs.",
            "objectivesIntroduced": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": ["gram_a1_case_dative_locative_location"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["өрөө", "ширээ", "гэр", "хот"],
            "readingObjective": "Read short sentences containing nouns declined in the dative-locative case.",
            "listeningObjective": "Hear the distinction between bare nominative stems and suffixed dative forms (гэр vs гэрт, өрөө vs өрөөнд).",
            "writingObjective": "Attach correct -д/-т suffixes to 6 location nouns considering final stem consonants.",
            "spokenProductionObjective": "State aloud the physical location of 3 common objects using '...-д/т байна'.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Providing precise spatial coordinates to conversational partners.",
            "prerequisiteLessonIds": ["les_a1_24_06_household_inventory_dialogue"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine existential predication with grammatical locative anchoring.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Accurate acoustic rendering of final dental stop -т vs sonorant -д.",
            "successCriteria": [
                "Attach -т correctly after stem-final voiceless stops (б, в, г, д, ж, з, р, с, т, ц, ч, ш, х).",
                "Attach -д correctly after open vowels and sonorant finals."
            ],
            "masteryEvidence": [
                "Corrects 'гэр-д' to 'гэрт' and 'өрөө-т' to 'өрөөнд/өрөөд' across 5 test stems.",
                "Produces 'Ном ширээн дээр байна' or 'Ном өрөөнд байна'."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "sentence_reordering", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_25_02_locating_people_places",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Where are they? Locating People in Towns, Buildings, and Rooms",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Practice expressing the whereabouts of people and institutional locations using dative-locative noun phrases.",
            "communicativeOutcome": "Inform others where family members, teachers, or colleagues currently are located.",
            "objectivesIntroduced": ["obj_a1_25_02_locate_people_spatially"],
            "objectivesPracticed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "objectivesReviewed": ["obj_a1_17_01_personal_pronouns"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_pronouns_demonstrative_ene_ter"],
            "grammarReinforced": ["gram_a1_pronouns_demonstrative_ene_ter"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["Улаанбаатар", "сургууль", "эмнэлэг", "гэр"],
            "readingObjective": "Read staff directory entries indicating current work locations (e.g. 'Багш номын санд байна').",
            "listeningObjective": "Identify who is in which room from a 3-party spoken conversation.",
            "writingObjective": "Write 4 sentences describing where various individuals are currently located.",
            "spokenProductionObjective": "State aloud the locations of 3 colleagues or friends.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Accurate relay of administrative or domestic locations without ambiguity.",
            "prerequisiteLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsLessonIds": ["les_a1_17_01_singular_pronouns_subject_slots"],
            "reviewsUnitIds": ["unit_a1_17_personal_pronouns_direct_address_pr"],
            "reviewReason": "Integrate subject personal pronouns with locative spatial predicates.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Intonation phrasing linking subject noun and locative adverbial.",
            "successCriteria": [
                "Correctly link subject pronouns and proper names with dative-locative spatial destinations.",
                "Employ stable SOV phrasing: Subject + Location-д/т + байна."
            ],
            "masteryEvidence": [
                "Produces 'Тэр сургуульд байна' when prompted with a campus image.",
                "Scores 100% on a person-to-location matching comprehension activity."
            ],
            "recommendedExerciseModalities": ["cued_production", "matching", "image_description"]
        },
        {
            "lessonId": "les_a1_25_03_urban_directory_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Public Signage and Building Directories",
            "lessonType": "reading_development",
            "primaryPurpose": "Decode authentic public floor guides, office directories, and university signage using locative markers.",
            "communicativeOutcome": "Find desired departments, floors, and services inside public buildings in Mongolia.",
            "objectivesIntroduced": ["obj_a1_25_03_read_building_directories"],
            "objectivesPracticed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_iotated_vowels_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["давхар", "өрөө", "банк", "эмийн сан"],
            "readingObjective": "Read a multi-floor commercial building directory and extract floor locations for 4 services.",
            "listeningObjective": None,
            "writingObjective": "Transcribe the exact floor and room number for 3 specified offices from the directory.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Navigating municipal and commercial buildings independently.",
            "prerequisiteLessonIds": ["les_a1_25_02_locating_people_places"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_20_demonstrative_deixis_"],
            "reviewReason": "Reinforce reading comprehension of spatial nouns combined with locative case.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Authentic text read-along of floor announcements.",
            "successCriteria": [
                "Correctly identify the floor and room number for 4 out of 4 services from a directory.",
                "Recognize ordinal numbers (1-р давхарт, 2-р давхарт) with attached dative-locative marker."
            ],
            "masteryEvidence": [
                "Answers 'Эмийн сан хэддүгээр давхарт байна?' with 'Нэгдүгээр давхарт байна'.",
                "Matches service icons to directory floor text accurately."
            ],
            "recommendedExerciseModalities": ["reading_comprehension", "document_scanning", "matching"]
        },
        {
            "lessonId": "les_a1_25_04_spatial_inquiries_qa",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Asking 'Where?': Inquiries with Хаана байна?",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Formulate spatial inquiries with 'Хаана' and respond fluently with dative-locative phrases.",
            "communicativeOutcome": "Ask pedestrians, security guards, or clerks for the location of amenities and comprehend their directions.",
            "objectivesIntroduced": ["obj_a1_25_04_spatial_inquiry_exchange"],
            "objectivesPracticed": [
                "obj_a1_25_01_apply_dative_locative_suffixes",
                "obj_a1_25_02_locate_people_spatially"
            ],
            "objectivesReviewed": ["obj_a1_24_03_ask_polar_existence"],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_formal_greeting_morning_afternoon"],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["жорлон", "үүд", "угаалгын өрөө", "лифт"],
            "readingObjective": "Read dialogue transcripts of visitors asking for directions inside a hospital or library.",
            "listeningObjective": "Comprehend the location answer in a short inquiry dialogue.",
            "writingObjective": "Write 3 question-and-answer pairs inquiring about and stating locations.",
            "spokenProductionObjective": "Execute a 4-turn dialogue asking for and receiving directions inside a building.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Preceding location inquiries with polite attention-getters ('Уучлаарай, ...').",
            "prerequisiteLessonIds": ["les_a1_25_02_locating_people_places"],
            "reviewsLessonIds": ["les_a1_24_03_polar_inquiries_existence"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Consolidate conversational questioning routines.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic intonational contrast between 'Хаана байна?' and declarative '...-д байна'.",
            "successCriteria": [
                "Prefix questions with polite apology token 'Уучлаарай'.",
                "Use correct dative-locative form in the immediate response."
            ],
            "masteryEvidence": [
                "Asks 'Жорлон хаана байна?' and comprehends 'Хоёрдугаар давхарт байна'.",
                "Fluently produces 4 reciprocal turns without pausing."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "question_formation", "audio_response_matching"]
        },
        {
            "lessonId": "les_a1_25_05_acoustic_locative_listening",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Locative Suffix Discrimination in Public PA Announcements",
            "lessonType": "listening_development",
            "primaryPurpose": "Train the ear to recognize dative-locative suffixes attached to varied consonant stems in noisy public announcements.",
            "communicativeOutcome": "Identify where individuals are being paged or where events are occurring from public PA broadcasts.",
            "objectivesIntroduced": ["obj_a1_25_05_discriminate_locative_in_pa"],
            "objectivesPracticed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["сургууль", "танхим", "буудал", "номын сан"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 PA announcements and identify the destination or meeting room specified.",
            "writingObjective": "Log the location names and room numbers announced in the audio recordings.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Extracting critical administrative directives from broadcast announcements.",
            "prerequisiteLessonIds": ["les_a1_25_03_urban_directory_reading", "les_a1_25_04_spatial_inquiries_qa"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Deepen acoustic decoding of -д/-т in natural reverberant environments.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic PA system reverberation and acoustic simulation.",
            "successCriteria": [
                "Accurately extract 4 out of 4 location targets from simulated public announcements.",
                "Distinguish between stem consonants and attached case suffixes."
            ],
            "masteryEvidence": [
                "Matches broadcast recordings to corresponding campus map pins without error.",
                "Writes correct case endings for heard locations."
            ],
            "recommendedExerciseModalities": ["listening_comprehension", "map_tagging", "error_identification"]
        },
        {
            "lessonId": "les_a1_25_06_campus_orientation_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Campus and Building Orientation Guide",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Synthesize all Unit 25 dative-locative skills in a peer orientation roleplay.",
            "communicativeOutcome": "Guide a new student or international visitor around a building or town center using spatial case forms.",
            "objectivesIntroduced": ["obj_a1_25_06_guide_visitor_spatially"],
            "objectivesPracticed": [
                "obj_a1_25_01_apply_dative_locative_suffixes",
                "obj_a1_25_02_locate_people_spatially",
                "obj_a1_25_04_spatial_inquiry_exchange"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [],
            "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_12_location_simple_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_01_formal_greeting_morning_afternoon"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["давхар", "өрөө", "үүд", "номын сан", "сургууль", "эмнэлэг"],
            "readingObjective": "Read map cues detailing locations of campus facilities.",
            "listeningObjective": "Understand peer visitor questions about where specific facilities are situated.",
            "writingObjective": "Draft a 4-line mini-guide listing locations of key facilities.",
            "spokenProductionObjective": "Direct a partner to 3 locations on a campus map using dative-locative structures.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Welcoming visitors hospitably while providing precise spatial directions.",
            "prerequisiteLessonIds": ["les_a1_25_04_spatial_inquiries_qa", "les_a1_25_05_acoustic_locative_listening"],
            "reviewsLessonIds": ["les_a1_25_02_locating_people_places"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Complete synthesis of spatial predication before moving to interrogative particles.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic multi-turn orientation dialogue with natural pacing.",
            "successCriteria": [
                "Produce 3 consecutive accurate location descriptions using dative-locative suffixes without error.",
                "Demonstrate spontaneous turn-taking in responding to visitor inquiries."
            ],
            "masteryEvidence": [
                "Provides complete oral directions across 6 interactive turns.",
                "Draws accurate route on map following partner's verbal instructions."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "map_navigation", "information_gap"]
        }
    ])

    return lessons
