"""
Builder script for gen_sec05_part1.py (Units 54 - 58: 30 lessons)
"""

sec05_part1_code = '''"""
Section 5 Generator - Part 1 (Units 54 - 58: 30 lessons)
Kinship, Possession, Milestones, Progressive Aspect, and Past Perfective
"""

import json
from typing import List, Dict, Any

def get_sec05_part1_lessons() -> List[Dict[str, Any]]:
    with open("curriculum/blueprint/units/a1.json") as f:
        units = json.load(f)
    u_map = {u["sequencePosition"]: u for u in units}
    lessons = []

    # =========================================================================
    # UNIT 54: Nuclear Kinship: Parents, Siblings & Children (pos 54)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[54]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_54_01_nuclear_kinship_and_genitive_possession",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Immediate Family: Parents, Siblings, and Genitive Possession -ын/-ийн",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce nuclear kinship terms (аав, ээж, ах, эгч, дүү, хүү, охин) and the genitive case of possession (-ын/-ийн/-ны/-ний) linking family members.",
            "communicativeOutcome": "Name nuclear family members and describe relational possession (e.g. 'Доржийн ах', 'Багшийн охин').",
            "objectivesIntroduced": ["obj_a1_54_01_identify_nuclear_kinship", "obj_a1_54_02_form_genitive_possession"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_47_01_form_comitative_accompaniment"],
            "grammarIntroduced": ["gram_a1_case_genitive_possession"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_case_comitative_accompaniment"],
            "grammarReinforced": ["gram_a1_case_comitative_accompaniment"],
            "phonologyIntroduced": ["phono_hidden_n_genitive"],
            "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": ["comm_a1_15_family_nuclear_members", "comm_a1_11_ownership_possession"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["хүн", "нэр", "ах", "эгч", "дүү"],
            "readingObjective": "Read simple family tree labels and captions identifying relatives.",
            "listeningObjective": "Hear kinship terms and genitive markers (-ын/-ийн) in spoken introductions.",
            "writingObjective": "Attach genitive suffixes to 6 personal and kinship nouns respecting vowel harmony.",
            "spokenProductionObjective": "Introduce your parents and siblings using genitive and kinship terms aloud.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Accurate familial identification and respectful generational terminology.",
            "prerequisiteLessonIds": ["les_a1_53_05_section_04_capstone_checkpoint"],
            "reviewsLessonIds": ["les_a1_47_01_comitative_accompaniment"],
            "reviewsUnitIds": ["unit_a1_47_comitative_case_suffixes_tai_tei_toi"],
            "reviewReason": "Combine comitative companionship with kinship nouns (e.g. аавтайгаа хамт).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clear articulation of genitive allomorphs and kinship vowel lengths.",
            "successCriteria": [
                "Select correct genitive allomorph (-ын, -ийн, -ны, -ний) based on stem coda and vowel harmony.",
                "Distinguish older brother (ах), older sister (эгч), and younger sibling (дүү)."
            ],
            "masteryEvidence": [
                "Produces 'Энэ бол манай аавын ном' without grammatical errors.",
                "Names all 6 nuclear kinship terms with correct pronunciation."
            ],
            "recommendedExerciseModalities": ["family_tree_labeling", "suffix_attachment", "cued_production"]
        },
        {
            "lessonId": "les_a1_54_02_older_and_younger_siblings_distinctions",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Siblings and Children: Ах, Эгч, Дүү, Хүү, and Охин",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Deepen distinction between older and younger siblings (эр дүү 'younger brother', эмэгтэй дүү 'younger sister') and sons/daughters (хүү, охин), practicing age rankings.",
            "communicativeOutcome": "State sibling birth order and identify children within a family structure.",
            "objectivesIntroduced": ["obj_a1_54_03_describe_sibling_hierarchy"],
            "objectivesPracticed": ["obj_a1_54_01_identify_nuclear_kinship", "obj_a1_54_02_form_genitive_possession"],
            "objectivesReviewed": ["obj_a1_31_01_count_items_with_units"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_genitive_possession"],
            "grammarReviewed": ["gram_a1_classifier_habits_neg_hoyor"],
            "grammarReinforced": ["gram_a1_classifier_habits_neg_hoyor"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["хүү", "охин", "том", "бага", "хоёр"],
            "readingObjective": "Read family diagram descriptions highlighting sibling numbers and birth order.",
            "listeningObjective": "Comprehend speakers detailing how many brothers and sisters they have.",
            "writingObjective": "Draft 3 sentences specifying your own siblings or a fictional family's children.",
            "spokenProductionObjective": "Explain your sibling order aloud ('Би нэг ах, хоёр дүүтэй').",
            "registerTarget": "Everyday standard friendly",
            "pragmaticTarget": "Clear sibling accounting aligned with Mongolian kinship concepts.",
            "prerequisiteLessonIds": ["les_a1_54_01_nuclear_kinship_and_genitive_possession"],
            "reviewsLessonIds": ["les_a1_31_01_measure_words_and_classifiers"],
            "reviewsUnitIds": ["unit_a1_31_measure_words_nominal_counting_clas"],
            "reviewReason": "Use counting classifiers with kinship nouns (хоёр дүү, нэг охин).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm conversational tone discussing family members.",
            "successCriteria": [
                "Distinguish gender among younger siblings using 'эрэгтэй дүү' and 'эмэгтэй дүү'.",
                "Combine count words with kinship nouns without redundant plural suffixes."
            ],
            "masteryEvidence": [
                "Produces 'Би нэг эрэгтэй дүүтэй, хоёр эмэгтэй дүүтэй' smoothly.",
                "Correctly maps out sibling relations on a diagram."
            ],
            "recommendedExerciseModalities": ["sibling_ranking", "diagram_completion", "dialogue_roleplay"]
        },
        {
            "lessonId": "les_a1_54_03_family_introductions_guided_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Introducing Family Members and Occupations",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining kinship terms, genitive possession, and occupations ('Манай аавын нэр Дорж, тэр эмч хийдэг').",
            "communicativeOutcome": "Present family members, stating their names, professions, and relationships fluently.",
            "objectivesIntroduced": ["obj_a1_54_04_introduce_family_and_professions"],
            "objectivesPracticed": [
                "obj_a1_54_01_identify_nuclear_kinship",
                "obj_a1_54_02_form_genitive_possession"
            ],
            "objectivesReviewed": ["obj_a1_14_01_introduce_self"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_genitive_possession"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": ["gram_a1_nominal_predicate_zero_copula"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_kinship_family", "lex_a1_professions_occupations"],
            "previousVocabularyReused": ["багш", "эмч", "жолооч", "ажиллах", "нэр"],
            "readingObjective": "Read short introductory family profiles on personal blogs or social profiles.",
            "listeningObjective": "Comprehend friends introducing their parents and older siblings in social contexts.",
            "writingObjective": "Write a 4-sentence introductory paragraph describing parents' names and jobs.",
            "spokenProductionObjective": "Present a family photograph describing who each person is and what they do.",
            "registerTarget": "Courteous standard neutral",
            "pragmaticTarget": "Respectful presentation of family members to friends and colleagues.",
            "prerequisiteLessonIds": ["les_a1_54_02_older_and_younger_siblings_distinctions"],
            "reviewsLessonIds": ["les_a1_14_01_self_introduction"],
            "reviewsUnitIds": ["unit_a1_14_self_introductions_core_courtesy_f"],
            "reviewReason": "Synthesize self-introduction patterns with extended family introductions.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Warm, natural personal introductions showing family pride.",
            "successCriteria": [
                "Link kinship nouns with genitive possessive constructions effortlessly.",
                "State professions accurately using nominal predicates."
            ],
            "masteryEvidence": [
                "Delivers a 1-minute family presentation from prompt cards.",
                "Answers 'Танай ээж ямар ажил хийдэг вэ?' accurately."
            ],
            "recommendedExerciseModalities": ["photo_presentation", "guided_substitution", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_54_04_family_letters_and_profiles_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Letters Home and Family Portrait Captions",
            "lessonType": "reading_development",
            "primaryPurpose": "Read written letters and social profiles where a writer describes their parents, siblings, and rural hometown roots.",
            "communicativeOutcome": "Extract family composition, ages, locations, and professions from written family letters.",
            "objectivesIntroduced": ["obj_a1_54_05_read_family_letters"],
            "objectivesPracticed": [
                "obj_a1_54_01_identify_nuclear_kinship",
                "obj_a1_54_02_form_genitive_possession"
            ],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_genitive_possession"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["захидал", "гэр бүл", "нутгийн", "амьдрах", "сайн"],
            "readingObjective": "Read a 70-word authentic personal letter describing family members living in the countryside.",
            "listeningObjective": None,
            "writingObjective": "Complete a structured family relationship chart based on the letter's text.",
            "spokenProductionObjective": None,
            "registerTarget": "Personal informal narrative",
            "pragmaticTarget": "Reading comprehension of authentic familial correspondence.",
            "prerequisiteLessonIds": ["les_a1_54_03_family_introductions_guided_drills"],
            "reviewsLessonIds": ["les_a1_54_01_nuclear_kinship_and_genitive_possession"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Consolidate written recognition of genitive possession on kinship terms.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Warm epistolary voice reading personal letters from home.",
            "successCriteria": [
                "Identify every relative mentioned in the letter and their relation to the writer.",
                "Extract professions and hometown locations accurately."
            ],
            "masteryEvidence": [
                "Answers 4 reading comprehension questions with 100% accuracy.",
                "Fills out the accompanying family pedigree chart without error."
            ],
            "recommendedExerciseModalities": ["letter_scanning", "chart_completion", "short_answer"]
        },
        {
            "lessonId": "les_a1_54_05_family_narratives_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Parsing Rapid Spoken Kinship Descriptions",
            "lessonType": "listening_development",
            "primaryPurpose": "Parse natural spoken audio where speakers quickly describe family sizes, sibling orders, and parents' backgrounds.",
            "communicativeOutcome": "Accurately record family members, names, and sibling counts from fast conversational speech.",
            "objectivesIntroduced": ["obj_a1_54_06_parse_spoken_family_narratives"],
            "objectivesPracticed": ["obj_a1_54_01_identify_nuclear_kinship"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_genitive_possession"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["аав", "ээж", "ах", "эгч", "дүү", "байна"],
            "readingObjective": None,
            "listeningObjective": "Listen to 4 personal audio introductions and note down the number of children and siblings for each speaker.",
            "writingObjective": "Transcribe the kinship terms and genitive case markings heard in each clip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Auditory tracking of family trees and relationships in casual conversations.",
            "prerequisiteLessonIds": ["les_a1_54_03_family_introductions_guided_drills"],
            "reviewsLessonIds": ["les_a1_54_02_older_and_younger_siblings_distinctions"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Zero-vocabulary auditory lab training kinship perception in connected speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational audio featuring varied speaker ages and speech rates.",
            "successCriteria": [
                "Map 4 speakers to their respective family size profiles accurately.",
                "Distinguish between -ын (genitive) and -тай (comitative) in spoken audio."
            ],
            "masteryEvidence": [
                "Scores 100% on the family structure listening test.",
                "Accurately transcribes all heard kinship nouns."
            ],
            "recommendedExerciseModalities": ["audio_tree_matching", "transcription", "multiple_choice"]
        },
        {
            "lessonId": "les_a1_54_06_family_album_presentation_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Sharing the Family Photo Album",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate looking through a family photo album with a peer: pointing out relatives, explaining generational relationships, and asking reciprocal questions.",
            "communicativeOutcome": "Conduct a fluid, engaging dialogue presenting one's family and inquiring about a peer's relatives.",
            "objectivesIntroduced": ["obj_a1_54_07_present_family_album"],
            "objectivesPracticed": [
                "obj_a1_54_01_identify_nuclear_kinship",
                "obj_a1_54_02_form_genitive_possession",
                "obj_a1_54_03_describe_sibling_hierarchy"
            ],
            "objectivesReviewed": ["obj_a1_47_02_express_possession_with_comitative"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_genitive_possession"],
            "grammarReviewed": ["gram_a1_case_comitative_possession_predicates", "gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_case_comitative_possession_predicates"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_15_family_nuclear_members"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_kinship_family"],
            "previousVocabularyReused": ["зураг", "аав", "ээж", "эгч", "дүү", "хэн", "байна"],
            "readingObjective": "Read simulated photo caption cards describing various relatives.",
            "listeningObjective": "Comprehend partner inquiries regarding family members' names and locations.",
            "writingObjective": "Draft a 4-line caption for a family portrait summarizing who is in the photo.",
            "spokenProductionObjective": "Execute an 8-turn conversation presenting a family album and answering peer questions.",
            "registerTarget": "Courteous standard friendly",
            "pragmaticTarget": "Warm, authentic personal sharing building interpersonal rapport.",
            "prerequisiteLessonIds": [
                "les_a1_54_04_family_letters_and_profiles_reading",
                "les_a1_54_05_family_narratives_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_54_03_family_introductions_guided_drills"],
            "reviewsUnitIds": ["unit_a1_54_nuclear_kinship_parents_siblings_ch"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 54 kinship skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating personal family album sharing.",
            "successCriteria": [
                "Identify and introduce 4 family members using genitive constructions fluently.",
                "Inquire about partner's family using 'Энэ хэн бэ?' and 'Танай аавын нэр хэн бэ?'."
            ],
            "masteryEvidence": [
                "Completes unscripted album sharing dialogue in under 2 minutes.",
                "Both partners demonstrate flawless mastery of kinship vocabulary and genitive forms."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "photo_simulation", "peer_interview"]
        }
    ])

    return lessons
'''

with open("scripts/framework_builder/gen_sec05_part1.py", "w") as f:
    f.write(sec05_part1_code)

print("gen_sec05_part1.py initialized with Unit 54!")
