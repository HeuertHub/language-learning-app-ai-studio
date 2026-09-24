"""
Section 2 Full Builder: Units 24 through 33 (10 Units, 58 Lessons)
Physical Space, Quantities, and Locative Grounding
"""

import json
from typing import List, Dict, Any

def get_sec02_full_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}

    # Import U24, U25, U26 from generate_full_sec02
    from generate_full_sec02 import generate_section_02
    lessons = generate_section_02()

    # =========================================================================
    # UNIT 27: Cardinal Numbers & Counting up to One Hundred (pos 27)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[27]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_27_01_cardinal_numerals_1_to_20",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Counting Foundations: Cardinal Numerals 1 to 20",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce cardinal numbers from 1 to 20, focusing on the lack of plural marking on nouns modified by numerals in Mongolian.",
            "communicativeOutcome": "State quantities of objects and persons from 1 to 20 accurately without applying ungrammatical plural suffixes.",
            "objectivesIntroduced": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": ["gram_a1_numerals_cardinal_1_100"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["хүн", "ном", "үзэг", "ширээ"],
            "readingObjective": "Read numeral digits matched with Cyrillic number words up to 20.",
            "listeningObjective": "Hear and distinguish numbers with similar sound profiles (долоо vs найм, арван нэг vs арван хоёр).",
            "writingObjective": "Write numeral words for given visual quantities of classroom objects.",
            "spokenProductionObjective": "Count aloud from 1 to 20 with clear vowel length distinction.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Direct, clear quantification in transactions and inquiries.",
            "prerequisiteLessonIds": ["les_a1_26_06_inquiry_dialogue_synthesis"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine numeral quantification directly with existential assertions.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear phonological rendering of vowel lengths in 'нэг', 'хоёр', 'гурав', 'дөрөв', 'тав'.",
            "successCriteria": [
                "Pronounce numerals 1-20 with correct vowel qualities.",
                "Leave following noun in bare singular form (e.g. 'хоёр ном', not 'хоёр номууд')."
            ],
            "masteryEvidence": [
                "Correctly counts 12 objects in a picture without adding plural suffixes.",
                "Scores 100% on a number-to-spelling matching exercise."
            ],
            "recommendedExerciseModalities": ["counting_drill", "matching", "cued_production"]
        },
        {
            "lessonId": "les_a1_27_02_tens_and_counting_to_100",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Decades and Hundreds: Numbers 20 to 100",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce decade multiples (хорь, гуч, дөч, тавь, жар, дал, ная, ер, зуу) and compound two-digit number construction.",
            "communicativeOutcome": "Formulate and understand any cardinal number between 21 and 100 in financial, inventory, and metric contexts.",
            "objectivesIntroduced": ["obj_a1_27_02_count_decades_up_to_100"],
            "objectivesPracticed": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_sov_word_order"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["төгрөг", "оюутан", "өрөө"],
            "readingObjective": "Read two-digit prices and room numbers written out in Mongolian text.",
            "listeningObjective": "Discriminate between teens and decades (арван гурав vs гуч).",
            "writingObjective": "Write 5 compound two-digit numbers in Cyrillic script.",
            "spokenProductionObjective": "State aloud the prices of 4 everyday consumer items up to 100 tugriks.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Accurate numerical reporting to avoid transactional errors.",
            "prerequisiteLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Build compound two-digit numbers upon mastered single-digit bases.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Rhythmic stress cadence in compound number phrases (e.g. 'хорин тав', 'гучин долоо').",
            "successCriteria": [
                "Construct compound numbers with decade stem preceding unit digit.",
                "Recognize the combining stem forms (хорь -> хорин, гуч -> гучин)."
            ],
            "masteryEvidence": [
                "Transcribes spoken two-digit numbers into digits with 100% accuracy.",
                "Produces 'тавин найм' upon seeing numeral 58."
            ],
            "recommendedExerciseModalities": ["dictation", "multiple_choice", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_27_03_inquiries_with_hed",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "How Many? Quantity Questions with Хэд and Хэдэн",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Differentiate and use the interrogative quantifiers 'хэд' (asking for bare number) and 'хэдэн' (modifying a noun: 'how many Xs?').",
            "communicativeOutcome": "Ask and answer questions about the quantity of people, inventory items, and prices.",
            "objectivesIntroduced": ["obj_a1_27_03_ask_quantity_hed_heden"],
            "objectivesPracticed": [
                "obj_a1_27_01_count_cardinals_1_to_20",
                "obj_a1_27_02_count_decades_up_to_100"
            ],
            "objectivesReviewed": ["obj_a1_26_01_select_be_ve_particles"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_intro"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["сандал", "хүүхэд", "ном", "өрөө"],
            "readingObjective": "Read inventory survey questions inquiring about asset counts.",
            "listeningObjective": "Comprehend questions like 'Энд хэдэн сандал байна вэ?' in fast speech.",
            "writingObjective": "Write 3 questions asking about quantities of items in an office.",
            "spokenProductionObjective": "Ask a peer how many siblings or books they have.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Direct, polite quantification inquiries in civic and domestic situations.",
            "prerequisiteLessonIds": ["les_a1_27_02_tens_and_counting_to_100"],
            "reviewsLessonIds": ["les_a1_26_01_content_particles_distribution"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Attach content question particles (бэ/вэ) to numerical interrogatives (Хэд вэ?).",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural falling intonation on 'Хэдэн ... байна вэ?'.",
            "successCriteria": [
                "Select 'хэдэн' before a noun and 'хэд' in predicate position (Үнэ нь хэд вэ?).",
                "Pair 'хэд вэ' with particle 'вэ' (vowel final)."
            ],
            "masteryEvidence": [
                "Distinguishes 'Хэд вэ?' from 'Хэдэн ном бэ?' without error.",
                "Produces full answer: 'Таван ном байна'."
            ],
            "recommendedExerciseModalities": ["question_formation", "cloze_selection", "audio_response_matching"]
        },
        {
            "lessonId": "les_a1_27_04_inventory_sheet_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Asset Logs and Store Stock Inventories",
            "lessonType": "reading_development",
            "primaryPurpose": "Scan and interpret commercial stock sheets, store receipt totals, and warehouse lists.",
            "communicativeOutcome": "Verify inventory lists against stock count records and identify numerical discrepancies.",
            "objectivesIntroduced": ["obj_a1_27_04_read_inventory_sheets"],
            "objectivesPracticed": ["obj_a1_27_02_count_decades_up_to_100"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["бараа", "тоо", "нийт", "хэрэгсэл"],
            "readingObjective": "Read a 50-word office supply inventory sheet with itemized quantities.",
            "listeningObjective": None,
            "writingObjective": "Fill out a stock summary table detailing item names and numerical counts.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard administrative",
            "pragmaticTarget": "Meticulous verification of quantities in commercial records.",
            "prerequisiteLessonIds": ["les_a1_27_03_inquiries_with_hed"],
            "reviewsLessonIds": ["les_a1_27_02_tens_and_counting_to_100"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Reinforce written recognition of compound number words in real documents.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading stock numbers cleanly and rhythmically.",
            "successCriteria": [
                "Locate total quantities for 5 distinct inventory categories.",
                "Identify any mismatch between requested numbers and on-hand counts."
            ],
            "masteryEvidence": [
                "Calculates total count from 3 line items correctly.",
                "Extracts specific quantities with zero reading comprehension errors."
            ],
            "recommendedExerciseModalities": ["document_scanning", "table_completion", "matching"]
        },
        {
            "lessonId": "les_a1_27_05_auditory_number_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Rapid Number Recognition in Market Bidding",
            "lessonType": "listening_development",
            "primaryPurpose": "Train the ear to decipher rapid numbers spoken in lively market auctions, checkout counters, and announcements.",
            "communicativeOutcome": "Accurately record numerical values from rapid native spoken input without hesitation.",
            "objectivesIntroduced": ["obj_a1_27_05_decipher_rapid_spoken_numbers"],
            "objectivesPracticed": ["obj_a1_27_01_count_cardinals_1_to_20", "obj_a1_27_02_count_decades_up_to_100"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["тоо", "үнэ", "төгрөг", "нийт"],
            "readingObjective": None,
            "listeningObjective": "Listen to 8 rapid numerical values spoken with natural rhythm and record them in digits.",
            "writingObjective": "Transcribe 6 heard numbers from audio into Arabic numerals.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard commercial",
            "pragmaticTarget": "Fast numerical comprehension in bustling commercial exchanges.",
            "prerequisiteLessonIds": ["les_a1_27_03_inquiries_with_hed"],
            "reviewsLessonIds": ["les_a1_27_01_cardinal_numerals_1_to_20"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Consolidate auditory comprehension of numbers up to 100.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Rapid authentic native speech with natural acoustic reductions of non-initial vowels.",
            "successCriteria": [
                "Accurately write down 8 out of 8 spoken numbers on first or second listen.",
                "Differentiate between 14 (арван дөрөв) and 40 (дөч) reliably."
            ],
            "masteryEvidence": [
                "Scores 100% on a rapid-fire number transcription test.",
                "Selects correct price tag from audio prompts without hesitation."
            ],
            "recommendedExerciseModalities": ["number_dictation", "audio_matching", "rapid_sorting"]
        },
        {
            "lessonId": "les_a1_27_06_counting_dialogue_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Classroom and Office Stocktake",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Execute a full collaborative inventory stocktake using numbers, existential predicates, and locative cases.",
            "communicativeOutcome": "Conduct a comprehensive room audit with a partner, checking and agreeing upon item quantities.",
            "objectivesIntroduced": ["obj_a1_27_06_conduct_stocktake_dialogue"],
            "objectivesPracticed": [
                "obj_a1_27_01_count_cardinals_1_to_20",
                "obj_a1_27_02_count_decades_up_to_100",
                "obj_a1_27_03_ask_quantity_hed_heden"
            ],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["ширээ", "сандал", "компьютер", "ном", "үзэг", "өрөө"],
            "readingObjective": "Read stocktake assignment prompt specifying items to verify.",
            "listeningObjective": "Understand partner's count affirmations and corrections.",
            "writingObjective": "Produce a finalized 5-item stocktake certificate with accurate numerals.",
            "spokenProductionObjective": "Participate in an 8-turn cooperative inventory verification dialogue.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Professional collaborative precision in institutional audits.",
            "prerequisiteLessonIds": [
                "les_a1_27_04_inventory_sheet_reading",
                "les_a1_27_05_auditory_number_lab"
            ],
            "reviewsLessonIds": ["les_a1_27_03_inquiries_with_hed"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Zero-vocabulary synthesis consolidating all counting competencies.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary collaborative interaction demonstrating count verification.",
            "successCriteria": [
                "Accurately query and state quantities for 5 distinct objects.",
                "Maintain error-free lack of plural suffixes on all quantified nouns."
            ],
            "masteryEvidence": [
                "Produces 'Манай өрөөнд арван хоёр сандал байна' during dialogue.",
                "Completes shared stocktake sheet with zero numerical discrepancies."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "audit_reconciliation"]
        }
    ])

    return lessons
