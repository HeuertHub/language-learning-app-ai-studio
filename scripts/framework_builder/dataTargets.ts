export interface VocabularyArchitecturePlan {
  primaryLexicalLemmaRange: [number, number];
  coreSingleWordLemmasRange: [number, number];
  independentlyLexicalizedDerivationsRange: [number, number];
  multiwordExpressionsRange: [number, number];
  functionWordsAndParticlesRange: [number, number];
  properNounsRange: [number, number];
  inflectedSurfaceFormsExclusion: string;
}

export interface LessonPlanningBands {
  microLessonPhoneticReview: [number, number];
  standardInstructional: [number, number];
  grammarIntegratedSkills: [number, number];
  majorReviewWorkshopCheckpoint: [number, number];
}

export interface LevelScaleTarget {
  level: string;
  name: string;
  mongolianName: string;
  projectedSectionsRange: [number, number];
  projectedUnitsRange: [number, number];
  projectedLessonsRange: [number, number];
  targetCoreLemmasRange: [number, number];
  targetMultiwordExpressionsRange: [number, number];
  grammarConceptRange: [number, number];
  primaryPedagogicalFocus: string;
}

export interface ExerciseModalitySpec {
  modalityId: string;
  name: string;
  mongolianName: string;
  primaryCognitiveSkill: "receptive" | "productive" | "analytical" | "interactive";
  description: string;
  targetLinguisticLayers: string[];
  bestSuitedLevels: string[];
}

export interface CurriculumScaleBlueprint {
  sectionsPlanningRange: [number, number];
  unitsPlanningRange: [number, number];
  lessonsPlanningRange: [number, number];
  exercisePlanningNote: string;
  vocabularyPlan: VocabularyArchitecturePlan;
  lessonPlanningBands: LessonPlanningBands;
  levelTargets: LevelScaleTarget[];
  exerciseModalities: ExerciseModalitySpec[];
  architecturalPrinciples: string[];
}

export const curriculumScaleBlueprintData: CurriculumScaleBlueprint = {
  sectionsPlanningRange: [20, 30],
  unitsPlanningRange: [200, 300],
  lessonsPlanningRange: [1300, 1700],
  exercisePlanningNote: "Exercise quantity will be calculated only after individual lesson blueprints exist.",
  vocabularyPlan: {
    primaryLexicalLemmaRange: [8000, 10000],
    coreSingleWordLemmasRange: [6500, 7500],
    independentlyLexicalizedDerivationsRange: [1500, 2500],
    multiwordExpressionsRange: [1500, 3000],
    functionWordsAndParticlesRange: [140, 200],
    properNounsRange: [350, 500],
    inflectedSurfaceFormsExclusion: "Strictly 0. Inflected surface forms and synthetic paradigm variants must never count toward lexical targets."
  },
  lessonPlanningBands: {
    microLessonPhoneticReview: [4, 8],
    standardInstructional: [8, 15],
    grammarIntegratedSkills: [12, 25],
    majorReviewWorkshopCheckpoint: [20, 45]
  },
  architecturalPrinciples: [
    "No rigid multiplier formulas: Lesson counts and exercise counts emerge from pedagogical objectives, not artificial arithmetic multiples.",
    "Decoupled exercise sizing: Exercise volumes will be determined during individual lesson blueprinting according to cognitive depth and lesson type.",
    "Categorical vocabulary separation: Primary lexical lemmas, derived words, multiword expressions, function words, and proper nouns are measured in distinct inventories.",
    "Variable structural density: Unit and lesson counts vary naturally across sections depending on thematic and linguistic complexity."
  ],
  levelTargets: [
    {
      level: "Pre-A1",
      name: "Orthographic & Phonetic Foundations",
      mongolianName: "Цагаан толгой ба авиа зүй",
      projectedSectionsRange: [2, 3],
      projectedUnitsRange: [14, 20],
      projectedLessonsRange: [80, 110],
      targetCoreLemmasRange: [120, 200],
      targetMultiwordExpressionsRange: [20, 50],
      grammarConceptRange: [0, 2],
      primaryPedagogicalFocus: "Cyrillic decoding, vowel length discrimination, soft vs hard consonants, basic handwriting and syllabification"
    },
    {
      level: "A1",
      name: "Beginner Survival & Everyday Basics",
      mongolianName: "Анхан шат: Өдөр тутмын хэрэглээ",
      projectedSectionsRange: [4, 6],
      projectedUnitsRange: [36, 50],
      projectedLessonsRange: [230, 290],
      targetCoreLemmasRange: [800, 1100],
      targetMultiwordExpressionsRange: [150, 300],
      grammarConceptRange: [38, 45],
      primaryPedagogicalFocus: "Canonical SOV word order, fourfold vowel harmony, seven primary cases, personal pronouns, basic copulas and numbers"
    },
    {
      level: "A2",
      name: "Elementary Situational Autonomy",
      mongolianName: "Анхан дунд шат: Ахуйн хүрээний харилцаа",
      projectedSectionsRange: [4, 6],
      projectedUnitsRange: [40, 52],
      projectedLessonsRange: [260, 310],
      targetCoreLemmasRange: [1200, 1600],
      targetMultiwordExpressionsRange: [250, 450],
      grammarConceptRange: [24, 30],
      primaryPedagogicalFocus: "Reflexive-possessive, instrumental/directional cases, relative participial clauses, sequential converbs, modals"
    },
    {
      level: "B1",
      name: "Intermediate Independent User",
      mongolianName: "Дунд шат: Бие даасан харилцагч",
      projectedSectionsRange: [4, 6],
      projectedUnitsRange: [45, 55],
      projectedLessonsRange: [300, 350],
      targetCoreLemmasRange: [1600, 2100],
      targetMultiwordExpressionsRange: [350, 650],
      grammarConceptRange: [22, 28],
      primaryPedagogicalFocus: "Voice inflections (causative/passive), participial nominalization, converb chaining, evidentials, indirect speech with гэж"
    },
    {
      level: "B2",
      name: "Upper-Intermediate Analytical & Professional",
      mongolianName: "Ахисан дунд шат: Мэргэжлийн харилцаа",
      projectedSectionsRange: [3, 5],
      projectedUnitsRange: [35, 48],
      projectedLessonsRange: [240, 290],
      targetCoreLemmasRange: [1800, 2400],
      targetMultiwordExpressionsRange: [400, 750],
      grammarConceptRange: [20, 28],
      primaryPedagogicalFocus: "Multi-clause converb chaining, counterfactual past, switch-reference tracking, discourse cohesion, stylistic particles, epistemic stance"
    },
    {
      level: "C1",
      name: "Advanced Effective Operational Proficiency",
      mongolianName: "Гүнзгий шат: Эрдэм шинжилгээ, албан харилцаа",
      projectedSectionsRange: [3, 5],
      projectedUnitsRange: [28, 38],
      projectedLessonsRange: [170, 220],
      targetCoreLemmasRange: [1400, 1900],
      targetMultiwordExpressionsRange: [300, 550],
      grammarConceptRange: [18, 25],
      primaryPedagogicalFocus: "Subject/object honorific tiers, state chancellery syntax, classical converbs, academic nominalized frames, statutory analysis"
    },
    {
      level: "C2",
      name: "Mastery of Modern Eloquence & Cultural Heritage",
      mongolianName: "Дээд шат: Өв соёл, сонгодог найруулга",
      projectedSectionsRange: [2, 4],
      projectedUnitsRange: [18, 30],
      projectedLessonsRange: [100, 160],
      targetCoreLemmasRange: [1000, 1400],
      targetMultiwordExpressionsRange: [250, 450],
      grammarConceptRange: [14, 20],
      primaryPedagogicalFocus: "Rapid unscripted colloquial mastery, pragmatic nuance, satire/irony, modern nonfiction/fiction, metric alliteration, traditional gnomic proverbs and ceremonial oratory"
    }
  ],
  exerciseModalities: [
    {
      modalityId: "mod_phonetic_minimal_pair_discrim",
      name: "Acoustic Minimal Pair Discrimination",
      mongolianName: "Авиа ялгах дасгал",
      primaryCognitiveSkill: "receptive",
      description: "Learner listens to two acoustically similar native recordings (e.g. хол vs хоол, үхэр vs үсэр) and identifies target phoneme or vowel length.",
      targetLinguisticLayers: ["Phonetics", "Vowel length", "Consonant palatalization"],
      bestSuitedLevels: ["Pre-A1", "A1"]
    },
    {
      modalityId: "mod_vowel_harmony_suffix_selector",
      name: "Vowel Harmony Allomorph Selector",
      mongolianName: "Эгшиг зохицох нөхцөл сонгох",
      primaryCognitiveSkill: "analytical",
      description: "Given a noun or verb stem, learner selects the correct harmonizing allomorph out of four variants (-аар, -ээр, -оор, -өөр).",
      targetLinguisticLayers: ["Orthography", "Fourfold harmony", "Stem phonotactics"],
      bestSuitedLevels: ["A1", "A2"]
    },
    {
      modalityId: "mod_case_inflection_fill_blank",
      name: "Case Inflection Contextual Cloze",
      mongolianName: "Тийн ялгалын нөхцөл нөхөх",
      primaryCognitiveSkill: "productive",
      description: "Learner applies the appropriate case ending to a bracketed base noun to complete an authentic sentence with correct meaning.",
      targetLinguisticLayers: ["Case morphology", "Syntax", "Government"],
      bestSuitedLevels: ["A1", "A2", "B1"]
    },
    {
      modalityId: "mod_sov_word_order_scramble",
      name: "Syntactic Scramble & Reordering",
      mongolianName: "Өгүүлбэрийн гишүүдийг зөв байрлуулах",
      primaryCognitiveSkill: "analytical",
      description: "Learner rearranges disordered syntactic constituents into canonical Mongolian SOV clause structure.",
      targetLinguisticLayers: ["Syntax", "SOV constraints", "Postpositional phrases"],
      bestSuitedLevels: ["A1", "A2"]
    },
    {
      modalityId: "mod_converb_clause_combiner",
      name: "Converb Subordination Clause Combiner",
      mongolianName: "Холбох нөхцөлөөр өгүүлбэр холбох",
      primaryCognitiveSkill: "productive",
      description: "Learner transforms two independent propositions into a single subordinated sentence using the targeted converb (-аад, -ж, -вал, -магц).",
      targetLinguisticLayers: ["Converbs", "Complex sentences", "Temporal aspect"],
      bestSuitedLevels: ["A2", "B1", "B2"]
    },
    {
      modalityId: "mod_reflexive_vs_possessive_contrast",
      name: "Reflexive (-аа4) vs Non-Reflexive (-нь) Contrast",
      mongolianName: "Өөртөө ба заах хамаатуулах ялгах",
      primaryCognitiveSkill: "analytical",
      description: "Learner chooses between reflexive possessive and third-person possessive depending on whether possessor is the clause subject.",
      targetLinguisticLayers: ["Reflexive possession", "Anaphora", "Subject tracking"],
      bestSuitedLevels: ["A2", "B1"]
    },
    {
      modalityId: "mod_voice_transformation_causative_passive",
      name: "Voice Transduction (Active to Causative/Passive)",
      mongolianName: "Хэвийн хувиргалт хийх",
      primaryCognitiveSkill: "productive",
      description: "Learner reformulates an active clause into passive or causative voice, updating argument cases (nominative to dative agent).",
      targetLinguisticLayers: ["Voice", "Valency", "Argument structure"],
      bestSuitedLevels: ["B1", "B2"]
    },
    {
      modalityId: "mod_reading_authentic_passage_comprehension",
      name: "Authentic Text Comprehension & Inference",
      mongolianName: "Эх уншиж ойлгох шалгалт",
      primaryCognitiveSkill: "receptive",
      description: "Learner reads an authentic excerpt (news article, diary, literature) and answers factual, inferential, and vocabulary questions.",
      targetLinguisticLayers: ["Reading comprehension", "Discourse", "Inference"],
      bestSuitedLevels: ["A2", "B1", "B2", "C1", "C2"]
    },
    {
      modalityId: "mod_audio_dialogue_inference",
      name: "Spoken Dialogue Listening & Speaker Stance",
      mongolianName: "Харилцан яриа сонсож дүгнэх",
      primaryCognitiveSkill: "receptive",
      description: "Learner listens to an unscripted or semi-scripted audio dialogue and identifies speakers' social relationship, emotional tone, and decisions.",
      targetLinguisticLayers: ["Listening", "Prosody", "Pragmatics"],
      bestSuitedLevels: ["A1", "A2", "B1", "B2"]
    },
    {
      modalityId: "mod_dictation_orthography_check",
      name: "Full-Sentence Acoustic Dictation",
      mongolianName: "Сонсоод зөв бичих дасгал",
      primaryCognitiveSkill: "productive",
      description: "Learner listens to a sentence spoken at natural speed and types the exact Cyrillic orthography, testing silent vowel deletion and consonant rules.",
      targetLinguisticLayers: ["Orthography", "Phoneme-to-grapheme", "Spelling"],
      bestSuitedLevels: ["A1", "A2", "B1"]
    },
    {
      modalityId: "mod_honorific_register_shift",
      name: "Sociolinguistic Register & Honorific Shift",
      mongolianName: "Хүндэтгэлийн найруулгад шилжүүлэх",
      primaryCognitiveSkill: "productive",
      description: "Learner rewrites colloquial or standard statements into appropriate respectful forms suitable for addressing an elder or dignitary.",
      targetLinguisticLayers: ["Sociolinguistics", "Honorific vocabulary", "Politeness"],
      bestSuitedLevels: ["B2", "C1"]
    },
    {
      modalityId: "mod_discourse_marker_insertion",
      name: "Rhetorical Discourse Connector Insertion",
      mongolianName: "Найруулгын холбоос зөв сонгох",
      primaryCognitiveSkill: "analytical",
      description: "Learner selects the optimal rhetorical transition (үүний үр дүнд, цаашилбал, гэтэл) to logically bind consecutive paragraphs.",
      targetLinguisticLayers: ["Discourse grammar", "Cohesion", "Rhetoric"],
      bestSuitedLevels: ["B2", "C1"]
    },
    {
      modalityId: "mod_proverb_metaphor_interpretation",
      name: "Proverbial Metaphor & Cultural Wisdom Analysis",
      mongolianName: "Зүйр цэцэн үгийн цаад утгыг тайлах",
      primaryCognitiveSkill: "analytical",
      description: "Learner interprets the figurative meaning and real-world application of a traditional nomadic proverb or aphorism.",
      targetLinguisticLayers: ["Proverbs", "Metaphor", "Cultural semantics"],
      bestSuitedLevels: ["B2", "C1", "C2"]
    },
    {
      modalityId: "mod_error_detection_and_correction",
      name: "Linguistic Error Spotting & Correction",
      mongolianName: "Найруулга, дүрмийн алдаа засах",
      primaryCognitiveSkill: "analytical",
      description: "Learner detects intentional grammatical, orthographic, or case errors in a paragraph and provides the corrected form.",
      targetLinguisticLayers: ["Error analysis", "Prescriptive grammar", "Proofreading"],
      bestSuitedLevels: ["B1", "B2", "C1"]
    },
    {
      modalityId: "mod_contextual_vocabulary_collocation_cloze",
      name: "Contextual Collocation & Lexical Cloze",
      mongolianName: "Хам үгийн тохироог сонгох",
      primaryCognitiveSkill: "receptive",
      description: "Learner fills missing lexical items within idiomatic collocations and institutional compounds (e.g. нөхөн сэргээлт, гэрээ байгуулах).",
      targetLinguisticLayers: ["Collocations", "Semantic precision", "Vocabulary"],
      bestSuitedLevels: ["B1", "B2", "C1"]
    },
    {
      modalityId: "mod_dialogue_roleplay_completion",
      name: "Interactive Communicative Dialogue Turn-Taking",
      mongolianName: "Харилцан ярианд тохирох хариулт өгөх",
      primaryCognitiveSkill: "interactive",
      description: "Given a realistic situational prompt (e.g. in a clinic, negotiating rent), learner supplies the culturally appropriate next conversational turn.",
      targetLinguisticLayers: ["Pragmatics", "Turn-taking", "Fluency"],
      bestSuitedLevels: ["A1", "A2", "B1", "B2"]
    },
    {
      modalityId: "mod_table_declension_matrix_fill",
      name: "Morphological Paradigm Matrix Completion",
      mongolianName: "Тийн ялгалын хүснэгт нөхөх",
      primaryCognitiveSkill: "analytical",
      description: "Learner systematically fills in irregular pronoun oblique stems or noun paradigm cases across singular and plural.",
      targetLinguisticLayers: ["Morphology", "Paradigms", "Suppletion"],
      bestSuitedLevels: ["A1", "A2"]
    },
    {
      modalityId: "mod_chancellery_administrative_drafting",
      name: "Administrative Decree & Official Formulation",
      mongolianName: "Албан бичиг, тогтоол найруулах",
      primaryCognitiveSkill: "productive",
      description: "Learner composes formulaic legal clauses, statutory references, and prescriptive directives following official state chancellery format.",
      targetLinguisticLayers: ["Administrative register", "Legal syntax", "Nominalization"],
      bestSuitedLevels: ["C1"]
    },
    {
      modalityId: "mod_head_alliteration_verse_composition",
      name: "Metric Head-Alliteration Verse Composition",
      mongolianName: "Толгой холбож шүлэг зохиох",
      primaryCognitiveSkill: "productive",
      description: "Learner drafts paired poetic lines matching initial consonants or vowels and maintaining syntactic balance according to traditional rules.",
      targetLinguisticLayers: ["Poetics", "Alliteration", "Metric balance"],
      bestSuitedLevels: ["C2"]
    },
    {
      modalityId: "mod_ceremonial_blessing_oratory",
      name: "Ceremonial Blessing (Ерөөл) Delivery & Transcription",
      mongolianName: "Ерөөл магтаалын айлдвар бүтээх",
      primaryCognitiveSkill: "productive",
      description: "Learner structures an extemporaneous ceremonial blessing for a national holiday, wedding, or child's rite of passage.",
      targetLinguisticLayers: ["Ceremonial register", "High eloquence", "Oral folklore"],
      bestSuitedLevels: ["C2"]
    }
  ]
};
