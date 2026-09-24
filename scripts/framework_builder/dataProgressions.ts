export interface SkillProgressionStage {
  stageId: string;
  level: string;
  stageName: string;
  mongolianStageName: string;
  readingMilestone: {
    textTypes: string[];
    wordCountRange: [number, number];
    lexicalDensity: string;
    syntacticComplexity: string;
    sampleTasks: string[];
  };
  listeningMilestone: {
    audioFormats: string[];
    speechRateWpm: [number, number]; // words per minute
    acousticContext: string;
    comprehensionFocus: string;
    sampleTasks: string[];
  };
  writingMilestone: {
    outputGenres: string[];
    wordCountRange: [number, number];
    orthographicExpectation: string;
    syntacticStructure: string;
    samplePrompts: string[];
  };
}

export const skillProgressionsData: SkillProgressionStage[] = [
  {
    stageId: "prog_pre_a1_alphabet",
    level: "Pre-A1",
    stageName: "Orthographic & Phonetic Emergence",
    mongolianStageName: "Үсэг зүй ба авиа дуудлагын анхан үе",
    readingMilestone: {
      textTypes: ["Cyrillic single letters", "Syllable charts", "Street signs", "Store logos", "Price tags"],
      wordCountRange: [1, 15],
      lexicalDensity: "High frequency isolated words",
      syntacticComplexity: "Zero syntactic complexity; phonetic decoding",
      sampleTasks: ["Match Cyrillic uppercase and lowercase forms", "Read store signs in Ulaanbaatar (Хүнс, Эмийн сан, Банк)", "Pronounce short vowel vs long vowel word pairs"]
    },
    listeningMilestone: {
      audioFormats: ["Isolated phonemes", "Minimal word pairs", "Individual letter names", "Basic numbers"],
      speechRateWpm: [40, 60],
      acousticContext: "Studio recorded, pristine acoustic clarity, native speaker pronunciation",
      comprehensionFocus: "Phonetic discrimination between short, long, and diphthong vowels, and soft vs hard consonants",
      sampleTasks: ["Distinguish between хол (far) and хоол (food)", "Identify which syllable carries main vowel", "Write down dictated numbers 1 to 20"]
    },
    writingMilestone: {
      outputGenres: ["Individual Cyrillic letters", "CVC and CV syllables", "Personal name in Cyrillic", "Numbers in words"],
      wordCountRange: [1, 10],
      orthographicExpectation: "Letter formation accuracy, distinguishing Cyrillic cursive from print, correct soft/hard sign placement",
      syntacticStructure: "Isolated words and labels",
      samplePrompts: ["Transcribe your full name into modern Mongolian Cyrillic", "Write the Cyrillic alphabet in alphabetical order", "Write the names of 5 classroom objects"]
    }
  },
  {
    stageId: "prog_a1_foundational",
    level: "A1",
    stageName: "Elementary Interaction & Functional Literacy",
    mongolianStageName: "Анхан шатны харилцаа ба бичиг хэргийн суурь",
    readingMilestone: {
      textTypes: ["Canteen menus", "Short text messages (SMS)", "Basic business cards", "Simple personal profiles", "Class schedules"],
      wordCountRange: [20, 60],
      lexicalDensity: "Concrete everyday nouns and high-frequency basic verbs",
      syntacticComplexity: "Single-clause SOV sentences, copular clauses, basic case suffixes",
      sampleTasks: ["Read a menu at a cafeteria and identify dishes with mutton vs beef", "Extract meeting time and sender name from a short SMS", "Read an introductory student bio and identify their major"]
    },
    listeningMilestone: {
      audioFormats: ["Slow, clear spoken dialogues", "Classroom directions", "Simple greetings and introductions", "Telephone numbers and prices"],
      speechRateWpm: [70, 95],
      acousticContext: "Clear speech with minimal background noise and generous pauses between phrases",
      comprehensionFocus: "Extracting specific factual details (prices, times, names, places)",
      sampleTasks: ["Listen to a phone number dictation and write down the digits", "Identify what food item a speaker requests in a canteen dialogue", "Understand basic teacher commands (Номоо нээнэ үү, Сонсоорой)"]
    },
    writingMilestone: {
      outputGenres: ["Personal introduction bios", "Brief greetings and thank-you notes", "Simple lists and schedules", "Single-sentence answers to questions"],
      wordCountRange: [20, 50],
      orthographicExpectation: "Correct application of fourfold vowel harmony in case suffixes (-д/-т, -ын/-ийн, -ыг/-ийг)",
      syntacticStructure: "SOV word order with correct subject-predicate agreement and simple noun phrase modifiers",
      samplePrompts: ["Write a 5-sentence personal introduction stating your name, nationality, profession, and family members", "Write an SMS to a friend confirming tomorrow's meeting time at the library", "Describe what is on your desk using 4 locational sentences"]
    }
  },
  {
    stageId: "prog_a2_situational",
    level: "A2",
    stageName: "Situational Autonomy & Connected Narrative",
    mongolianStageName: "Нөхцөл байдалд дасан зохицох ба холбоост хүүрнэл",
    readingMilestone: {
      textTypes: ["Short personal emails", "Travel brochures and itineraries", "Weather forecasts", "Public notices and signs", "Short adapted folktales"],
      wordCountRange: [60, 150],
      lexicalDensity: "Expanded vocabulary covering travel, health, weather, shopping, and everyday tasks",
      syntacticComplexity: "Compound sentences joined by sequential converb (-аад), coordinating converb (-ж), and simple relative clauses (-сан, -даг)",
      sampleTasks: ["Read a 3-day travel itinerary to Terelj National Park and identify planned activities", "Read a weather report for Ulaanbaatar and provincial centers and summarize weekend forecast", "Read a short email from a friend recounting their weekend in the countryside"]
    },
    listeningMilestone: {
      audioFormats: ["Public transport announcements (bus, train, airport)", "Everyday conversational exchanges", "Doctor-patient consultations", "Short weather broadcasts"],
      speechRateWpm: [100, 125],
      acousticContext: "Authentic tempo with standard clear Ulaanbaatar dialect and typical urban ambient sound",
      comprehensionFocus: "Grasping the main idea and following sequential chronological narratives",
      sampleTasks: ["Listen to an intercity bus announcement and determine boarding gate and departure time", "Follow a 2-minute dialogue between a customer and pharmacist to identify prescribed dosage", "Understand directions given by a passerby on Sukhbaatar Square"]
    },
    writingMilestone: {
      outputGenres: ["Short personal narratives (weekend recap, holiday trip)", "Formal inquiries and email requests", "Recipe steps or sequential directions", "Postcards and social media updates"],
      wordCountRange: [60, 120],
      orthographicExpectation: "Consistent spelling of reflexive-possessive suffixes (-аа4) and vowel deletion before case endings",
      syntacticStructure: "Use of converbial subordination (-аад, -ж, -вал) and relative participial clauses",
      samplePrompts: ["Write a paragraph of 8-10 sentences describing a memorable trip you took recently", "Write an email to an apartment landlord asking about rent, utilities, and location", "Write instructions for brewing traditional Mongolian milk tea (сүүтэй цай)"]
    }
  },
  {
    stageId: "prog_b1_independent",
    level: "B1",
    stageName: "Independent Communication & Contextual Discourse",
    mongolianStageName: "Бие даасан харилцаа ба хам сэдвийн өгүүлэмж",
    readingMilestone: {
      textTypes: ["News reports on current events", "Informative magazine articles", "Standard workplace correspondence and memos", "Biographies of notable Mongolians", "Clear instructions and regulations"],
      wordCountRange: [150, 350],
      lexicalDensity: "Broader abstract vocabulary covering education, economy, ecological topics, and societal trends",
      syntacticComplexity: "Participial nominalizations with case markers (-сныг, -санд, -снаас), causal and purposive clauses (учраас, тулд)",
      sampleTasks: ["Read an article on pasture conditions in Arkhangai and extract primary environmental factors", "Analyze a job announcement and determine required qualifications and applicant responsibilities", "Summarize the biographical milestones of Damdin Sükhbaatar or modern cultural figures"]
    },
    listeningMilestone: {
      audioFormats: ["Radio and podcast interviews", "TV news segments with field reporters", "Workplace team meetings", "University orientation lectures"],
      speechRateWpm: [130, 160],
      acousticContext: "Native conversational speed, overlapping dialogue, occasional background music or field noise",
      comprehensionFocus: "Tracking arguments, recognizing speaker stance and evidentiality (гэнэ, биз, бололтой)",
      sampleTasks: ["Listen to an 8-minute interview with a nomadic herder and note seasonal migration challenges", "Extract key policy decisions from an evening news report on Ulaanbaatar traffic regulations", "Follow a workplace discussion regarding project deadline extensions"]
    },
    writingMilestone: {
      outputGenres: ["Structured expository essays", "Formal letters of application or petition (өргөдөл)", "Summaries of articles or lectures", "Opinion blogs on cultural or social questions"],
      wordCountRange: [150, 280],
      orthographicExpectation: "Mastery of seven consonant rules (ДОЛЖОО), non-phonemic silent vowels, and derivational suffixes (-лага, -лт)",
      syntacticStructure: "Multi-layered causal, temporal, and conditional subordinate structures with switch-reference",
      samplePrompts: ["Write an essay of 3 paragraphs discussing the advantages and challenges of nomadic vs urban lifestyles", "Write a formal petition (өргөдөл) to a university dean requesting a semester leave of absence", "Summarize an article about renewable solar and wind energy potential in the South Gobi"]
    }
  },
  {
    stageId: "prog_b2_professional",
    level: "B2",
    stageName: "Professional Fluency & Analytical Synthesis",
    mongolianStageName: "Мэргэжлийн түвшний чөлөөт хэрэглээ ба дүн шинжилгээ",
    readingMilestone: {
      textTypes: ["Editorials and op-eds from major newspapers (Өнөөдөр, Зууны мэдээ)", "Academic book chapters", "Technical and business reports", "Legal contracts and leases", "Modern short stories (e.g. by S. Erdene, D. Maam)"],
      wordCountRange: [350, 800],
      lexicalDensity: "Dense specialized terminology, idioms, metaphors, and socio-political discourse",
      syntacticComplexity: "Complex converb chaining, counterfactual conditionals, passive-causative stacking, topic-comment marking (бол, харин)",
      sampleTasks: ["Identify author's underlying thesis and rhetorical strategies in an editorial on mining policy", "Compare two differing analytical perspectives on pasture degradation in scientific journals", "Interpret literary symbolism and emotional nuance in an unabridged modern Mongolian short story"]
    },
    listeningMilestone: {
      audioFormats: ["Roundtable debate panels (Монгол тулгатны 100 эрхэм)", "Documentary films with authentic narration", "University academic lectures", "Live parliamentary debates (УИХ-ын чуулган)"],
      speechRateWpm: [150, 190],
      acousticContext: "Fast native delivery, regional phonetic variants (Khalkha, Buriad, Oirat accents), rhetorical pauses",
      comprehensionFocus: "Recognizing implicit assumptions, subtle sarcasm, rhetorical emphasis, and evidential hedging",
      sampleTasks: ["Analyze arguments presented by two economists on inflation during a 20-minute television panel", "Transcribe and evaluate conclusions from a documentary on Gobi bear (мазаалай) conservation", "Synthesize recommendations made during a public municipal hearing on smog reduction"]
    },
    writingMilestone: {
      outputGenres: ["Argumentative thesis-driven essays", "Executive project reports and policy evaluations", "Critical reviews of literature or cinema", "Formal business partnership proposals"],
      wordCountRange: [280, 500],
      orthographicExpectation: "Flawless orthography of specialized loanwords, derivational compounds, and elevated connective particles",
      syntacticStructure: "Rhetorical discourse markers (үүний үр дүнд, цаашилбал, нөгөөтэйгүүр) with flawless cohesive ties",
      samplePrompts: ["Compose an analytical essay defending an actionable strategy to balance coal export revenues with carbon reduction targets", "Draft a comprehensive formal business proposal establishing an eco-tourism project in the Altai mountains", "Write a critical review of a contemporary Mongolian novel analyzing its portrayal of rural-to-urban migration"]
    }
  },
  {
    stageId: "prog_c1_authoritative",
    level: "C1",
    stageName: "Authoritative & Academic Precision",
    mongolianStageName: "Эрдэм шинжилгээ, мэргэжлийн найруулгын дээд түвшин",
    readingMilestone: {
      textTypes: ["Supreme Court rulings and statutes", "Peer-reviewed research monographs (Шинжлэх Ухааны Академи)", "Diplomatic treaties and state communiqués", "Philosophical treatises", "Classical 20th-century historical novels (e.g. Тунгалаг Тамир)"],
      wordCountRange: [800, 2000],
      lexicalDensity: "High-level administrative, juridical, philological, and philosophical terminology",
      syntacticComplexity: "Archaic and literary converbs (-ваас, -хуйц), highly embedded nominalization chains, passive state attributions",
      sampleTasks: ["Extract precise statutory obligations from a Parliamentary act on Foreign Investment", "Deconstruct philosophical and ethical arguments in a treatise on Zanabazar's artistic canon", "Evaluate historical veracity and philological choices in a critique of 17th-century chronicles"]
    },
    listeningMilestone: {
      audioFormats: ["Diplomatic addresses and keynote speeches", "Academic defense ceremonies (Doctoral dissertations)", "High-level legal courtroom arguments", "Complex theatrical and poetic performances"],
      speechRateWpm: [160, 210],
      acousticContext: "Formal oratorical delivery, elevated register, archaic cadence, complex rhetorical questions",
      comprehensionFocus: "Full comprehension of nuanced sociolinguistic register, subtle cultural innuendo, and diplomatic subtext",
      sampleTasks: ["Follow a 45-minute doctoral thesis defense in linguistics and critique methodology questions raised by committee", "Analyze the rhetorical and diplomatic subtext of a Presidential State of the Nation address", "Identify stylistic archaisms and metric nuances in an epic theatrical performance at the State Drama Theatre"]
    },
    writingMilestone: {
      outputGenres: ["Scholarly journal articles", "Statutory decrees and administrative standards", "Diplomatic notes and bilateral communiqués", "Comprehensive judicial briefs"],
      wordCountRange: [500, 1200],
      orthographicExpectation: "Rigorous adherence to academic publishing norms and official state chancellery orthography",
      syntacticStructure: "Dense left-branching nominalizations, passive attributions, and classical connective constructions",
      samplePrompts: ["Write a scholarly critique analyzing the morphological evolution of converbial systems from Middle Mongol to Modern Cyrillic", "Draft an official administrative decree (тогтоол) establishing regulatory oversight for autonomous mining operations", "Compose a formal diplomatic démarche conveying state position on transboundary water resource management"]
    }
  },
  {
    stageId: "prog_c2_mastery",
    level: "C2",
    stageName: "Mastery of Heritage, Epic Literature & Spontaneous Eloquence",
    mongolianStageName: "Өв соёл, туульс ба цэцэн мэргэн найруулгын дээд чадвар",
    readingMilestone: {
      textTypes: ["The Secret History of the Mongols in modern philological Cyrillic edition", "Heroic oral epics (Жангар, Гэсэр)", "Orkhon-Yenisey runic translations", "Ancient Buddhist canonical commentaries (Данжур)", "Intricate metric poetry and allegorical literature"],
      wordCountRange: [1500, 4000],
      lexicalDensity: "Archaic lexicon, dialectal idioms, rare metric rhymes, Buddhist loanwords, epic formulae",
      syntacticComplexity: "Head-alliteration parallelism, gnomic aphorisms, metric couplets, Middle Mongol syntactic remnants",
      sampleTasks: ["Analyze the structural and metrical parallelisms in the 1240 CE coronation oath in the Secret History", "Compare editorial recensions of the Jangar epic across Xinjiang, Kalmyk, and Khalkha traditions", "Deconstruct multi-layered Buddhist allegory in 19th-century didactic poetry (Равжаа хутагтын зохиол)"]
    },
    listeningMilestone: {
      audioFormats: ["Live traditional epic recitation (тууль хайлах) with morin khuur or tovshuur", "Unabridged ceremonial orations (ерөөл, магтаал)", "Debates among senior philologists and cultural elders", "Unscripted regional dialect speech from remote aimags"],
      speechRateWpm: [140, 240], // can range from slow solemn recitation to rapid-fire poetic verse
      acousticContext: "Oral storytelling acoustics, throat singing accompaniment, dialectal phonetics (Bayan-Ölgii, Dornod, Uvs)",
      comprehensionFocus: "Deciphering archaic oral formulae, spontaneous alliterative rhymes, and cosmological metaphors",
      sampleTasks: ["Transcribe and annotate an 18-minute oral epic performance recorded in Western Mongolia", "Analyze spontaneous metric adaptations made by a master bard during a Naadam horse-race blessing (морины цол)", "Identify dialectal phonological shifts in unscripted speech of an elderly nomad from the Darkhad valley"]
    },
    writingMilestone: {
      outputGenres: ["Original metric alliterative poetry (толгой холбосон шүлэг)", "Ceremonial blessings (ерөөл)", "Philological treatises on Mongolian historical monuments", "Masterful literary essays and philosophical dialogues"],
      wordCountRange: [800, 2500],
      orthographicExpectation: "Complete mastery of Classical Mongolian etymological principles reflected in Cyrillic standard, as well as awareness of traditional script correspondences",
      syntacticStructure: "Exemplary balanced rhetorical symmetry, rhythmic cadences, and poetic compression",
      samplePrompts: ["Compose an original 4-stanza poem adhering strictly to traditional head-alliteration (толгой холбох) commemorating the steppe winds", "Deliver an authoritative philological monograph analyzing the semantic shifts of pastoral terminology over 800 years", "Write a complete traditional ceremonial blessing (ерөөл) suitable for the dedication of a new ancestral home"]
    }
  }
];
