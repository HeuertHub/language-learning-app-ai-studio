export interface ProficiencyLevelSpec {
  level: string;
  name: string;
  mongolianName: string;
  summary: string;
  receptiveVocabularyEstimate: number;
  productiveVocabularyEstimate: number;
  listening: {
    speechSpeed: string;
    utteranceLength: string;
    vocabularyFamiliarity: string;
    grammaticalComplexity: string;
    registersAndGenres: string[];
    canUnderstand: string[];
    limitations: string[];
  };
  reading: {
    wordRecognition: string;
    sentenceComplexity: string;
    textLength: string;
    genres: string[];
    unfamiliarVocabTolerance: string;
    inferredMeaning: string;
    canRead: string[];
    limitations: string[];
  };
  spokenProduction: {
    fluencyAndPacing: string;
    interactionScope: string;
    discourseTypes: string[];
    canProduce: string[];
    limitations: string[];
  };
  writtenProduction: {
    scriptAndTyping: string;
    textComplexity: string;
    genres: string[];
    canWrite: string[];
    limitations: string[];
  };
  grammarControl: {
    activeControl: string[];
    receptiveControl: string[];
    emergingStructures: string[];
  };
  pronunciationPhonology: {
    phonemicContrasts: string[];
    vowelHarmonyControl: string;
    palatalizationControl: string;
    prosodyAndIntonation: string;
    commonLearnerStruggles: string[];
  };
  pragmaticsAndRegister: {
    politenessMarkers: string[];
    kinshipAndAgeRespect: string;
    registersHandled: string[];
    culturalEtiquette: string[];
  };
}

export const proficiencyLevelsData: ProficiencyLevelSpec[] = [
  {
    level: "Pre-A1",
    name: "Absolute Beginner / Cyrillic Foundation",
    mongolianName: "Цагаан толгойн анхан шат",
    summary: "Establish complete orthographic decoding, basic phonemic discrimination, standard Cyrillic keyboard input, and essential formulaic courtesies.",
    receptiveVocabularyEstimate: 250,
    productiveVocabularyEstimate: 120,
    listening: {
      speechSpeed: "Very slow, deliberately articulated with extended pauses between words (approx. 50-70 words per minute).",
      utteranceLength: "Isolated phonemes, single words, and short formulaic 2-3 word greetings.",
      vocabularyFamiliarity: "Strictly limited to the 35 Cyrillic letters, basic numerals, and common greetings.",
      grammaticalComplexity: "No clause parsing expected; acoustic discrimination of vowel length (а vs аа) and vowel timbre (у vs ү, о vs ө).",
      registersAndGenres: ["Clear synthetic citation audio", "Laboratory phonology pairs", "Standard everyday formulaic greetings"],
      canUnderstand: [
        "Letter names and their primary sounds in citation form.",
        "Minimal phonemic pairs (e.g. шар vs шаар, хүн vs хөн).",
        "Elementary greetings: Сайн байна уу, Баяртай, Тийм, Үгүй, Баярлалаа."
      ],
      limitations: ["Cannot parse continuous colloquial speech or multi-clause utterances."]
    },
    reading: {
      wordRecognition: "Letter-by-letter decoding transitioning to automatic sight-recognition of high-frequency monosyllabic and disyllabic stems.",
      sentenceComplexity: "Single words, labeled images, and elementary 2-word formulas.",
      textLength: "1 to 5 words at a time.",
      genres: ["Alphabet charts", "Flashcard entries", "Signage labels", "Basic nameplates"],
      unfamiliarVocabTolerance: "Very low; every unlearned word requires manual phonetic decoding.",
      inferredMeaning: "None; purely literal sound-letter matching.",
      canRead: [
        "All 35 Mongolian Cyrillic letters in uppercase and lowercase print.",
        "Recognize distinct Mongolian letters Ө ө and Ү ү without confusing with О or У.",
        "Identify soft sign Ь and hard sign Ъ in written words."
      ],
      limitations: ["Cannot comprehend connected prose, newspaper titles, or cursive handwriting."]
    },
    spokenProduction: {
      fluencyAndPacing: "Halting, requiring deliberate mental preparation before producing single words.",
      interactionScope: "Restricted to formulaic greetings and reciting alphabet sounds and numbers 1-10.",
      discourseTypes: ["Repetition drills", "Citation pronunciation", "Fixed ritual responses"],
      canProduce: [
        "Pronounce cardinal vowels [a, e, i, ɔ, ʊ, o, u] with recognizable clarity.",
        "State one's own name using basic equative formulas.",
        "Count from 1 to 10."
      ],
      limitations: ["Cannot form spontaneous creative sentences or answer open-ended questions."]
    },
    writtenProduction: {
      scriptAndTyping: "Keyboard typing in standard Mongolian Cyrillic layout (Windows/Mac/iOS standard); letter stroke matching.",
      textComplexity: "Transcribing isolated words and short formulaic phrases.",
      genres: ["Alphabet exercises", "Spelling dictations", "Name and identity labels"],
      canWrite: [
        "Type all 35 Mongolian Cyrillic characters on a digital keyboard.",
        "Spell phonetically regular 1- and 2-syllable Mongolian words.",
        "Write basic courtesies (Сайн байна уу, Баярлалаа)."
      ],
      limitations: ["Cannot compose original sentences without an exact structural model."]
    },
    grammarControl: {
      activeControl: ["Citation forms of nouns and pronouns", "Equative frame [Subject + байна]"],
      receptiveControl: ["Interrogative particle уу/үү in greetings", "Negative particle биш"],
      emergingStructures: ["Back vs front vowel identification"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Short vs long vowel phonemic length (унших vs уншаач, шар vs шаар)",
        "Rounded back [ɔ, ʊ] (О, У) vs rounded front [o, u] (Ө, Ү)",
        "Diphthongs [ai, ui, ɔi, ʊi]"
      ],
      vowelHarmonyControl: "Receptive awareness that back vowels (А, О, У) and front vowels (Э, Ө, Ү) do not mix in native words.",
      palatalizationControl: "Identifying soft sign (ь) and iotated vowels (я, е, ё, ю) indicating palatalized consonants.",
      prosodyAndIntonation: "Initial syllable stress prominence in Mongolian roots.",
      commonLearnerStruggles: [
        "Confusing Cyrillic В [w/v], Н [n/ŋ], Р [r trill], Х [x velar fricative].",
        "Equating Mongolian Cyrillic with Russian phonetic values.",
        "Failing to distinguish Ө from О, and Ү from У."
      ]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Greeting elder vs contemporary with appropriate formula"],
      kinshipAndAgeRespect: "Initial awareness that greeting elders requires respectful intonation.",
      registersHandled: ["Standard polite textbook register"],
      culturalEtiquette: ["Basic handshake/greeting posture in Mongolian cultural context"]
    }
  },
  {
    level: "A1",
    name: "Beginner / Breakthrough",
    mongolianName: "Анхан шат",
    summary: "Interact in simple everyday situations, introduce oneself and family, order food, describe surroundings, and utilize fundamental nominal cases and present/past verbal predicates.",
    receptiveVocabularyEstimate: 850,
    productiveVocabularyEstimate: 450,
    listening: {
      speechSpeed: "Slow, clear, standard Khalkha with gentle pacing (80-100 words per minute).",
      utteranceLength: "Short single clauses (4-8 words), simple dialogues with clear pauses.",
      vocabularyFamiliarity: "High-frequency core words: self, family, food, numbers, time, basic locations, common verbs.",
      grammaticalComplexity: "Simple SOV sentences, equatives, existential constructions, basic case-marked noun phrases.",
      registersAndGenres: ["Slow instructional dialogues", "Simple street directions", "Store checkout exchanges", "Classroom instructions"],
      canUnderstand: [
        "Questions about personal details (name, nationality, origin, profession, family).",
        "Prices, dates, hours of the day, and telephone numbers.",
        "Simple spatial directions (энд, тэнд, дээр, доор, дотор, гадаа)."
      ],
      limitations: ["Struggles when native speakers use fast colloquial vowel reduction or multiple chained converbs."]
    },
    reading: {
      wordRecognition: "Instant sight recognition of top 500 core lemmas and frequent case suffixes.",
      sentenceComplexity: "Single-clause SOV sentences and coordinate clauses joined with тэгээд or ба.",
      textLength: "Short paragraphs of 30-70 words (e.g. personal profiles, menus, receipts, timetables).",
      genres: ["Personal introduction blurbs", "Restaurant menus", "Public transit signs", "Simple SMS text messages"],
      unfamiliarVocabTolerance: "Moderate if context is supported by images or high-frequency scaffolding.",
      inferredMeaning: "Direct factual comprehension of stated details.",
      canRead: [
        "Personal introduction texts describing hometown, occupation, and family members.",
        "Everyday signage in Ulaanbaatar (дэлгүүр, эмийн сан, зоогийн газар, буудал).",
        "Simple notices and schedules."
      ],
      limitations: ["Cannot decipher complex literary texts, newspaper articles, or official government forms."]
    },
    spokenProduction: {
      fluencyAndPacing: "Deliberate speech with pauses to search for vocabulary and select harmonizing suffixes.",
      interactionScope: "Structured question-and-answer exchanges with supportive interlocutors.",
      discourseTypes: ["Self-introductions", "Ordering food and drinks", "Shopping transactions", "Asking for directions"],
      canProduce: [
        "Introduce oneself: Намайг ... гэдэг. Би Монгол хэл сурч байна.",
        "Express origin: Би Америк/Герман/Япон улсаас ирсэн.",
        "State possession: Надад ном бий / Надад машин байхгүй.",
        "Order meals: Би хуушуур, сүүтэй цай авъя."
      ],
      limitations: ["Cannot sustain long narratives or defend abstract viewpoints."]
    },
    writtenProduction: {
      scriptAndTyping: "Fluent Cyrillic typing of known vocabulary; correct harmonic suffix attachment.",
      textComplexity: "Simple declarative, interrogative, and imperative sentences (4-10 words).",
      genres: ["Short postcards", "Personal notes", "Shopping lists", "Brief informational forms"],
      canWrite: [
        "Fill out standard hotel/library forms (name, nationality, address, date of birth).",
        "Compose a 5-8 sentence paragraph about one's daily routine, family, or room.",
        "Send simple greetings for birthdays or Tsagaan Sar."
      ],
      limitations: ["Cannot write coherent multi-paragraph essays or formal correspondence."]
    },
    grammarControl: {
      activeControl: [
        "Nominal predicate with zero copula and negative биш",
        "Existential construction: байна / байхгүй / бий",
        "Vowel harmony in fourfold suffixes (-аа/-ээ/-оо/-өө, -даг/-дэг/-дог/-дөг)",
        "Genitive case (-ын/-ийн/-ы/-ий/-н) for possession and modification",
        "Accusative case (-ыг/-ийг/-г) for definite direct objects",
        "Dative-Locative case (-д/-т) for static location and recipient",
        "Ablative case (-аас/-ээс/-оос/-өөс) for origin and departure",
        "Comitative case (-тай/-тэй/-той) for accompaniment and possession",
        "Present-habitual verbal suffix -даг/-дэг/-дог/-дөг",
        "Present continuous construction -ж байна / -ч байна",
        "Simple past in -сан/-сэн/-сон/-сөн and -лаа/-лээ/-лоо/-лөө",
        "Prospective/future in -на/-нэ/-но/-нө",
        "Volitional -я/-е/-ё and polite request -аарай/-ээрэй"
      ],
      receptiveControl: [
        "Instrumental case -аар/-ээр/-оор/-өөр",
        "Directional case -руу/-рүү/-луу/-лүү",
        "Coordinating converb -ж/-ч and -аад/-ээд"
      ],
      emergingStructures: ["Reflexive-possessive suffix -аа/-ээ/-оо/-өө"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Short vs long vowel minimal pairs in open and closed syllables",
        "Velar [x] vs uvular [χ] vs velar nasal [ŋ]",
        "Affricates [t͡s] (ц) vs [t͡ʃ] (ч) and [d͡z] (з) vs [d͡ʒ] (ж)"
      ],
      vowelHarmonyControl: "Consistent selection of masculine vs feminine harmonic variants in high-frequency suffixes.",
      palatalizationControl: "Accurate pronunciation of palatalized consonants before soft sign and iotated letters.",
      prosodyAndIntonation: "Falling intonation for content questions (хэн бэ, юу вэ); rising-then-falling intonation for polar questions (уу/үү).",
      commonLearnerStruggles: [
        "Dropping unstable short vowels in non-initial syllables (fleeting vowel rule).",
        "Over-pronouncing reduced final vowels.",
        "Confusing accusative (-ыг) and genitive (-ын) endings in rapid speech."
      ]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Using Та instead of чи with elders and strangers", "Adding -аарай/-ээрэй for polite requests"],
      kinshipAndAgeRespect: "Addressing older acquaintances with ах (older brother) or эгч (older sister).",
      registersHandled: ["Standard informal with peers", "Polite everyday formal with strangers"],
      culturalEtiquette: [
        "Offering and receiving items with the right hand supported by the left arm.",
        "Not stepping on the yurt threshold (босго)."
      ]
    }
  },
  {
    level: "A2",
    name: "Elementary / Waystage",
    mongolianName: "Суурь шат",
    summary: "Handle routine daily tasks, express past experiences, future intentions, pastoral and urban realities, navigate transport, and employ all seven nominal cases, reflexive-possession, and foundational converbs.",
    receptiveVocabularyEstimate: 1800,
    productiveVocabularyEstimate: 950,
    listening: {
      speechSpeed: "Normal everyday speed with standard pauses (100-120 words per minute).",
      utteranceLength: "Compound sentences (8-15 words) connected with sequential converbs.",
      vocabularyFamiliarity: "Everyday life, weather, seasonal migration basics, five livestock, transport, health symptoms, domestic chores.",
      grammaticalComplexity: "Multi-clause sentences with -аад, -ж, -вал, and basic participial clauses.",
      registersAndGenres: ["Public announcements at train/bus stations", "Weather forecasts", "Doctor-patient consultations", "Neighbourly conversations"],
      canUnderstand: [
        "Detailed descriptions of weather and seasonal changes across Mongolia.",
        "Public transport instructions, stops, and schedule announcements.",
        "Explanations of common ailments and medication instructions."
      ],
      limitations: ["Struggles with rapid colloquial ellipsis, specialized technical jargon, or fast television broadcasts."]
    },
    reading: {
      wordRecognition: "Rapid recognition of all inflected case and verbal forms of top 1,500 words.",
      sentenceComplexity: "Compound and complex sentences with participial relative clauses and basic converb linkages.",
      textLength: "Passages of 100-200 words (short blog posts, weather summaries, news briefs, personal letters).",
      genres: ["Weather bulletins", "Travel itineraries", "Social media posts", "Instruction manuals for appliances"],
      unfamiliarVocabTolerance: "Able to infer meaning from context and transparent derivational affixes (-чин, -лаг, -гүй).",
      inferredMeaning: "Can deduce sequence of events and cause-effect in simple narrative prose.",
      canRead: [
        "A description of nomadic pastoral life, ger structure, and livestock management.",
        "A travel blog recounting a journey through the Gobi or Khövsgöl.",
        "Clear instructional leaflets from a clinic or pharmacy."
      ],
      limitations: ["Cannot comfortably read classical poetry, legal codes, or philosophical treatises."]
    },
    spokenProduction: {
      fluencyAndPacing: "Can sustain short conversational turns; occasional self-correction for case harmony and verb endings.",
      interactionScope: "Can exchange practical information, arrange appointments, describe past vacations, and negotiate small purchases.",
      discourseTypes: ["Narrating a weekend trip", "Explaining why one is late", "Describing symptoms to a pharmacist", "Comparing two items"],
      canProduce: [
        "Narrate past events: Би өчигдөр найзуудтайгаа уулзаад, хамт кино үзсэн.",
        "Express conditions: Хэрэв маргааш цас орвол, би гэртээ үлдэнэ.",
        "Compare objects: Энэ дээл тэр дээлээс илүү дулаахан байна.",
        "Express preference and purpose: Би монгол хэл сурахаар энд ирсэн."
      ],
      limitations: ["Struggles to articulate complex hypothetical scenarios or abstract ideological debates."]
    },
    writtenProduction: {
      scriptAndTyping: "Accurate typing with correct orthography for fleeting vowels and suffix assimilation.",
      textComplexity: "Cohesive multi-sentence paragraphs (50-100 words) using logical connectives (тийм учраас, гэвч, дараа нь).",
      genres: ["Personal emails", "Narrative diary entries", "Short reviews of restaurants/events", "Formal notes of absence"],
      canWrite: [
        "A 100-word email describing vacation plans or a visit to the countryside.",
        "A coherent description of a cultural holiday (Tsagaan Sar celebration at home).",
        "A structured message explaining an absence from work or class with reasons."
      ],
      limitations: ["Cannot compose analytical essays or administrative official memos."]
    },
    grammarControl: {
      activeControl: [
        "All 7 standard nominal cases: Nominative, Genitive, Accusative, Dative-Locative, Ablative, Instrumental, Comitative",
        "Directional case in -руу/-рүү/-луу/-лүү",
        "Reflexive-possessive suffix -аа/-ээ/-оо/-өө and combinations (-аараа, -тайгаа, -даа)",
        "Participial relative clauses: past (-сан), present/habitual (-даг), prospective (-х)",
        "Coordinating converb -ж/-ч (sequential and manner)",
        "Sequential prior converb -аад/-ээд/-оод/-өөд",
        "Conditional converb -вал/-вэл/-бал/-бэл",
        "Purposive converb -хаар/-хээр/-хоор/-хөөр",
        "Comparative structures using ablative (-аас илүү / дутуу)",
        "Modal constructions of obligation: -х хэрэгтэй, -х ёстой",
        "Modal constructions of permission and possibility: -ж болно / -ж болохгүй"
      ],
      receptiveControl: [
        "Concessive converb -вч and construction боловч",
        "Terminative converb -тал/-тэл",
        "Causative voice in -уул/-үүл and passive in -гд"
      ],
      emergingStructures: ["Subject marking in subordinate clauses (Genitive subject in participial clauses)"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Differentiating lateral fricative /ɮ/ (л) from alveolar trill /r/ (р) and glide /w/ (в)",
        "Consonant assimilation at morpheme boundaries (e.g. н + б -> [м], т + д -> [дд])",
        "Preserving long vowels in non-initial syllables against vowel reduction tendencies"
      ],
      vowelHarmonyControl: "Mastery of fourfold harmonic alternations across all high-frequency nominal and verbal suffixes.",
      palatalizationControl: "Accurate articulatory posture for palatalized dentals and labials (дь, ть, нь, ль).",
      prosodyAndIntonation: "Natural clause boundary pausing and correct intonational rise before conditional converbs (-вал).",
      commonLearnerStruggles: [
        "Inserting erroneous epenthetic vowels into standard consonant clusters.",
        "Overgeneralizing masculine suffix vowels to words with front rounded vowels (Ө, Ү).",
        "Distinguishing reflexive -аа from dative -д."
      ]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Proper use of modal particles (даа/дээ, шүү, л)", "Honorific address in retail and hospitality"],
      kinshipAndAgeRespect: "Appropriate honorific titles for family seniors (өвөө, эмээ, авга, нагац).",
      registersHandled: ["Colloquial conversational", "Standard polite administrative/commercial"],
      culturalEtiquette: [
        "Greeting rituals with snuff bottle (хөөрөг зөрүүлэх).",
        "Proper behavior during ger visits (entering left, sitting on designated side, never pointing feet at fire)."
      ]
    }
  },
  {
    level: "B1",
    name: "Intermediate / Threshold",
    mongolianName: "Дунд шат",
    summary: "Participate independently in most communicative situations across Mongolia, understand main points of radio/TV, narrate experiences and ambitions, express causes and consequences, and command converb chaining, causatives, and passives.",
    receptiveVocabularyEstimate: 3400,
    productiveVocabularyEstimate: 1800,
    listening: {
      speechSpeed: "Natural native conversational speed (120-140 words per minute) with standard reductions.",
      utteranceLength: "Extended complex sentences with multiple subordinate converb clauses.",
      vocabularyFamiliarity: "Broad everyday, cultural, economic, social, geographical, and narrative vocabulary.",
      grammaticalComplexity: "Embedded relative clauses, reported speech, causative/passive alternations, evidential particles.",
      registersAndGenres: ["Radio and podcast interviews", "Documentaries on Mongolian history and wildlife", "Naadam commentary", "Workplace staff meetings"],
      canUnderstand: [
        "Main arguments and concrete details in informational radio broadcasts and podcasts.",
        "Personal narratives recounting life stories, educational backgrounds, and career choices.",
        "Discussions comparing urban development in Ulaanbaatar with rural aimag realities."
      ],
      limitations: ["Occasional difficulty with archaic epic idioms, specialized legal statutes, or rapid slang."]
    },
    reading: {
      wordRecognition: "Effortless recognition of general vocabulary and complex affixed stems.",
      sentenceComplexity: "Periodically constructed sentences with left-branching subordinate clauses and converb chains.",
      textLength: "Articles of 300-600 words (newspaper feature stories, popular science articles, biographies, short stories).",
      genres: ["News reporting (News.mn, Montsame)", "Contemporary short stories", "Museum exhibitions and historical plaques", "Workplace emails and proposals"],
      unfamiliarVocabTolerance: "High; able to decipher low-frequency derived words via productive derivational affixes.",
      inferredMeaning: "Can understand irony, implicit stance, and underlying rhetorical intent in contemporary prose.",
      canRead: [
        "Newspaper reports on environmental issues (mining rehabilitation, air pollution, desertification).",
        "Biographical accounts of prominent historical figures (Chinggis Khaan, Sükhbaatar, Zanabazar).",
        "Short literary stories by modern Mongolian authors."
      ],
      limitations: ["Cannot decipher Old Mongolian script transcriptions or deeply philosophical pre-modern sutras."]
    },
    spokenProduction: {
      fluencyAndPacing: "Continuous discourse with natural rhythm; pauses occur primarily for idea formulation rather than grammatical search.",
      interactionScope: "Can initiate, maintain, and conclude conversations on familiar and abstract topics.",
      discourseTypes: ["Sustained storytelling", "Job interview responses", "Debating environmental solutions", "Giving detailed presentations"],
      canProduce: [
        "Express cause and consequence: Уул уурхайн салбар хөгжсөнөөр олон ажлын байр бий болсон боловч байгаль орчинд сөрөг нөлөө үзүүлж байна.",
        "Report speech: Тэр намайг маргааш хүрээд ир гэж хэлсэн.",
        "Use causative: Би машиныхаа тосыг солиулсан.",
        "Formulate nuanced hypotheses: Хэрэв засгийн газар дэд бүтцийг сайжруулахгүй бол хотын түгжрэл буурахгүй."
      ],
      limitations: ["Lacks full control of subtle stylistic honorific registers used in official diplomatic or poetic contexts."]
    },
    writtenProduction: {
      scriptAndTyping: "Rapid, accurate typing; full command of all orthographic rules, including foreign loanwords and double vowels.",
      textComplexity: "Structured essays, reports, and detailed narratives (200-350 words) with clear thematic progression.",
      genres: ["Opinion essays", "Detailed trip reports", "Formal complaints/inquiries", "Book and film reviews"],
      canWrite: [
        "A 300-word argumentative essay on the advantages and challenges of living in Ulaanbaatar.",
        "A formal letter to an educational institution requesting program information.",
        "A detailed synopsis of a Mongolian film or literary work with personal commentary."
      ],
      limitations: ["Does not yet command the full bureaucratic lexicon of official government decrees."]
    },
    grammarControl: {
      activeControl: [
        "Converb chaining: coordinating (-ж), sequential (-аад), conditional (-вал), concessive (-вч / боловч)",
        "Purposive converb (-хаар), Contemporaneous converb (-магц), Terminative converb (-тал)",
        "Durative converb (-саар) and Manner converb (-н)",
        "Causative voice suffixes (-уул/-үүл, -лга/-лгэ, -аа/-ээ, -га/-гэ)",
        "Passive voice suffixes (-гд/-эгд, -д)",
        "Reciprocal voice (-лц/-элц) and Collective voice (-цгаа/-цгээ)",
        "Complex participial nominalization with case markers (-сныг, -санд, -снаас, -снаар)",
        "Reported speech with гэж хэлэх, гэж үзэх, гэж бодох",
        "Direct vs indirect question structures",
        "Evidential / hearsay particles: гэнэ, сурагтай, биз",
        "Discourse connectors: гэтэл, тэгснээ, үүний зэрэгцээ, тиймээс"
      ],
      receptiveControl: [
        "Abnutative converb -лгүй / -лгүйгээр",
        "Limiting converb -нгаа/-нгээ",
        "Honorific verbal suffixes (-хүйц, -гтун)"
      ],
      emergingStructures: ["Complex clause subordination with multiple subjects and reference tracking"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Accurate control of non-initial short vowel phonological reduction in natural rapid speech",
        "Distinguishing syllable-final nasal variations: [n] vs velar [ŋ]",
        "Natural execution of consonant cluster phonotactics without artificial vowel insertion"
      ],
      vowelHarmonyControl: "Flawless spontaneous execution of vowel harmony even on loanwords with assimilated stems.",
      palatalizationControl: "Natural distinction between palatalized and non-palatalized consonants across all environments.",
      prosodyAndIntonation: "Native-like sentence intonation contours for compound converb clauses, marking subordinate boundaries with rising tones.",
      commonLearnerStruggles: [
        "Maintaining correct vowel harmony in complex multi-suffix derivations.",
        "Distinguishing the nuances of evidential particles in natural dialogue."
      ]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Subtle modal particles (болов уу, байлгүй дээ, шив)", "Indirect requests to soften directives"],
      kinshipAndAgeRespect: "Strict adherence to age-based honorific forms in multi-generational gatherings.",
      registersHandled: ["Colloquial informal", "General standard public", "Introductory professional/workplace"],
      culturalEtiquette: [
        "Etiquette surrounding Tsagaan Sar greetings (золгох ritual based on relative age).",
        "Understanding pastoral taboos regarding water, fire, and livestock herds."
      ]
    }
  },
  {
    level: "B2",
    name: "Upper Intermediate / Vantage",
    mongolianName: "Ахисан дунд шат",
    summary: "Communicate fluently and spontaneously with native speakers, comprehend complex academic and journalistic texts, follow extended lectures, write detailed argumentative essays, and command sophisticated discourse chaining and stylistic variants.",
    receptiveVocabularyEstimate: 5200,
    productiveVocabularyEstimate: 2800,
    listening: {
      speechSpeed: "Full natural native speed (140-170 words per minute) including regional accents, dialectal coloring, and colloquial elisions.",
      utteranceLength: "Full paragraph-length compound discourse units with dense subordinate embedding.",
      vocabularyFamiliarity: "Broad political, economic, sociological, scientific, environmental, and cultural lexicon.",
      grammaticalComplexity: "Periodic sentence structures, complex converb subordination, passive-causative stacks, varied epistemic stances.",
      registersAndGenres: ["Live television debate panels (MNB, Eagle News)", "University academic lectures", "Parliamentary hearings", "Literary audiobooks and dramatic performances"],
      canUnderstand: [
        "In-depth discussions on national economic policy, foreign investment, and mining legislation.",
        "Academic lectures on Central Asian history, linguistics, or pastoral ecology.",
        "Subtle emotional shifts, sarcasm, and rhetorical questioning in native dialogues."
      ],
      limitations: ["May need clarification with highly specialized archaisms or esoteric regional sub-dialects."]
    },
    reading: {
      wordRecognition: "Automatic across standard, literary, and technical vocabulary.",
      sentenceComplexity: "Dense academic and journalistic periodic structures spanning several lines before reaching the matrix verb.",
      textLength: "Extended texts of 800-1,500 words (investigative journalism, academic journal articles, historical essays).",
      genres: ["Academic publications (MUIs, Academy of Sciences)", "Editorials and investigative journalism", "Contemporary novels and poetry", "Legal contracts and administrative statutes"],
      unfamiliarVocabTolerance: "Very high; readily parses root-derivation etymologies and Sino-Mongolian or Tibeto-Mongolian calques.",
      inferredMeaning: "Comprehends complex figurative language, allegories, historical allusions, and ideological subtexts.",
      canRead: [
        "Analytical essays on geopolitical relations between Mongolia, China, Russia, and third neighbours.",
        "Chapters of contemporary Mongolian fiction analyzing post-socialist societal transformation.",
        "Statutory articles and legal codes regarding business, labor, and property rights."
      ],
      limitations: ["Struggles with archaic 13th-century Secret History vocabulary without glosses."]
    },
    spokenProduction: {
      fluencyAndPacing: "High fluency and spontaneity; minimal hesitation for formulation; natural native-like rhythmic cadence.",
      interactionScope: "Participates effectively in formal debates, negotiations, professional meetings, and academic seminars.",
      discourseTypes: ["Formal debate presentations", "Critical evaluations of policy", "Impromptu responses to complex inquiries", "Detailed technical instruction"],
      canProduce: [
        "Structure multi-stage arguments with sophisticated transitions (нэг талаас ... нөгөө талаас, үүний үр дүнд, цаашилбал).",
        "Defend a controversial position with evidence and nuanced rebuttal.",
        "Switch smoothly between casual colloquial register and polite professional register.",
        "Employ idiomatic collocations and customary proverbs (зүйр цэцэн үг) naturally."
      ],
      limitations: ["Does not yet possess the supreme oratorical eloquence of classical Mongolian literature."]
    },
    writtenProduction: {
      scriptAndTyping: "Flawless orthography, punctuation, and typographical style.",
      textComplexity: "Well-structured academic papers, formal reports, and analytical essays (400-800 words) with sophisticated syntactic variety.",
      genres: ["Policy briefs", "Academic seminar papers", "Professional project proposals", "Critical literary essays"],
      canWrite: [
        "A 600-word analytical essay evaluating Mongolia's renewable energy potential against coal dependency.",
        "A formal project proposal outlining timelines, budgets, and stakeholder impact in standard administrative style.",
        "A detailed critique of a contemporary sociological study or documentary."
      ],
      limitations: ["Cannot produce archaic high-prestige Buddhist or royal chancery prose."]
    },
    grammarControl: {
      activeControl: [
        "Full repertoire of complex subordinate converbs (-нгаа, -саар, -магц, -тал, -хаар, -лгүйгээр)",
        "Complex participial chaining with multiple nested genitive subjects",
        "Stacking of voice suffixes (e.g. Causative + Passive: хийлгэгдэх)",
        "Nuanced epistemic and evidential modalities (бололтой, магадгүй, байх учиртай, шинжтэй)",
        "Rhetorical inversion and topic-comment foregrounding",
        "Adverbial derivation (-аар/-ээр, -хан/-хэн, -таа/-тээ)",
        "Comprehensive discourse particles (атал, хэдий ч, гэсэн хэдий ч, харин, тухайлбал)",
        "Formulation of counterfactual conditionals (-сан бол ... -х байсан)"
      ],
      receptiveControl: [
        "Classical/archaic converb endings found in formal speeches (-ваас/-вээс, -хуйц/-хүйц)",
        "High honorific verbal stems and periphrastic expressions"
      ],
      emergingStructures: ["Integration of classical rhetorical parallelism in formal speech"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Flawless articulation of all phonemic distinctions in rapid and formal speech styles",
        "Precise phonotactic treatment of complex medial and final consonant clusters",
        "Natural native-level phonetic reduction of weak syllables without sacrificing intelligibility"
      ],
      vowelHarmonyControl: "Spontaneous, intuitive application of vowel harmony across all morphological environments.",
      palatalizationControl: "Native-like precision across all palatalized consonants in all environments.",
      prosodyAndIntonation: "Sophisticated intonational control for irony, rhetorical questions, suspense, and formal emphasis.",
      commonLearnerStruggles: ["Mastering the exact cadence of high-speed Mongolian conversational turn-taking."]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Mastery of honorific verbal prefixes and suffixes in formal and ceremonial settings"],
      kinshipAndAgeRespect: "Seamless adaptation to the strict hierarchical expectations of formal Mongolian family gatherings.",
      registersHandled: [
        "Intimate casual",
        "Everyday colloquial",
        "Standard public media",
        "Professional and corporate",
        "Official administrative (Албан бичиг)"
      ],
      culturalEtiquette: [
        "Full fluency in traditional toast rituals, poetic blessings (ерөөл), and banquet protocols.",
        "Deep understanding of Mongolian pastoral philosophy, connection to nature, and historical pride."
      ]
    }
  },
  {
    level: "C1",
    name: "Advanced / Effective Operational",
    mongolianName: "Гүнзгий шат",
    summary: "Understand a wide range of demanding, longer texts and recognize implicit meaning; express ideas fluently and spontaneously without searching for expressions; use language flexibly for social, academic, and professional purposes; command honorific registers, classical literary allusions, and official state administrative style.",
    receptiveVocabularyEstimate: 7800,
    productiveVocabularyEstimate: 4500,
    listening: {
      speechSpeed: "Native rapid speech, including colloquial idioms, fast radio commentary, and formal ceremonial addresses.",
      utteranceLength: "Unrestricted length, including multi-paragraph extemporaneous speeches and dense academic papers.",
      vocabularyFamiliarity: "Extensive mastery of abstract, philosophical, administrative, historical, and literary registers.",
      grammaticalComplexity: "Mastery of complex syntactic hierarchies, classical converbial retentions, and poetic sentence structures.",
      registersAndGenres: ["Live parliamentary debates and legal arguments", "Scholarly symposiums", "High-literature theatrical recitations", "Unscripted rural dialectal interviews"],
      canUnderstand: [
        "Nuanced philosophical and political discourse with implicit ideological commitments.",
        "Complex legal argumentation and constitutional interpretations.",
        "Traditional poetic recitations (тууль, магтаал, ерөөл) and classical folk wisdom."
      ],
      limitations: ["Minor unfamiliarity with highly localized regional sub-dialects or pre-14th-century philological fragments."]
    },
    reading: {
      wordRecognition: "Effortless across contemporary and 20th-century literary and scientific corpora.",
      sentenceComplexity: "Highly complex periodic paragraphs with extensive subordination and non-finite clause embedding.",
      textLength: "Full-length books, comprehensive research monographs, legal treatises, and literary collections.",
      genres: ["Academic dissertations", "Constitutional and legal statutes", "Historical chronicles (modern editions)", "Classical 20th-century literature (D. Natsagdorj, B. Rinchen, Ch. Lodoidamba)"],
      unfamiliarVocabTolerance: "Superior; accurately deduces obsolete, archaic, or newly coined terminology through morphological analysis.",
      inferredMeaning: "Perceives subtle subtext, irony, socio-political allusions, and classical intertextual echoes.",
      canRead: [
        "Modern editions of historical epics (Jangar, Geser) and the Secret History of the Mongols.",
        "Advanced literary works such as 'Тунгалаг Тамир' (Clear Tamir) by Ch. Lodoidamba.",
        "Official government resolutions, supreme court rulings, and legislative treaties."
      ],
      limitations: ["Requires specialized philological training for pre-classical Middle Mongol manuscripts in Uighur script."]
    },
    spokenProduction: {
      fluencyAndPacing: "Near-native fluency, rhythm, and spontaneity; articulates complex thoughts with precision and rhetorical power.",
      interactionScope: "Leads academic seminars, delivers keynote addresses, participates in high-stakes negotiations and media broadcasts.",
      discourseTypes: ["Keynote addresses", "Formal diplomatic negotiation", "Philosophical and ideological debate", "Literary and poetic recitation"],
      canProduce: [
        "Deliver a 15-minute structured speech on socio-economic development using formal administrative register.",
        "Participate in high-level debates on constitutional reform, skillfully handling counter-arguments and rhetorical strategies.",
        "Employ honorific register (хүндэтгэлийн хэл) flawlessly when addressing dignitaries or spiritual leaders.",
        "Incorporate classical proverbs, idioms, and metrical parallelism into spontaneous speech."
      ],
      limitations: ["Cannot pass as a lifelong native speaker in highly localized generational youth slang."]
    },
    writtenProduction: {
      scriptAndTyping: "Mastery of modern Mongolian orthographic standards, official state correspondence templates, and academic publishing conventions.",
      textComplexity: "Comprehensive research articles, policy documents, and stylistically sophisticated essays (800-2,000 words).",
      genres: ["Scholarly journal papers", "State administrative documents (тогтоол, албан бичиг)", "Literary essays and cultural criticism", "Legal contracts and briefs"],
      canWrite: [
        "A 1,500-word peer-reviewed journal article on Mongolian linguistic history or pastoral economy.",
        "An official diplomatic or corporate communique adhering strictly to state chancellery guidelines.",
        "A compelling cultural critique analyzing contemporary Mongolian cinema or literature."
      ],
      limitations: ["Does not produce genuine classical Mongolian calligraphy without dedicated graphic training."]
    },
    grammarControl: {
      activeControl: [
        "Flawless command of all literary and conversational converbial systems",
        "Full mastery of lexical and grammatical honorific systems (айлдах, морилох, таалагдах, зооглох)",
        "Official chancellery formulaic grammar (тогтоох нь, үүрэг болгосугай, дурдсанчлан)",
        "Classical conditional (-ваас) and purposive-honorific (-хуйц) forms",
        "Rhetorical parallelism and head-alliteration syntactic balance",
        "Discourse cohesion across multi-page texts with sophisticated reference tracking",
        "Exquisite modulation of epistemic stance and evidential responsibility"
      ],
      receptiveControl: [
        "Archaic case markers and participial endings found in 17th-19th century chronicles",
        "Dialectal morphological variations across Oirat, Buryat, and Inner Mongolian dialects"
      ],
      emergingStructures: ["Creative personal literary style and rhetorical mastery"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Indistinguishable from educated native speakers in standard Khalkha phonology",
        "Flawless execution of poetic meter, alliterative phrasing, and oratorical resonance"
      ],
      vowelHarmonyControl: "Intuitive and absolute across all lexemes.",
      palatalizationControl: "Flawless in both formal and rapid colloquial speech.",
      prosodyAndIntonation: "Command of varied oratorical intonations (ceremonial, academic, conversational, poetic).",
      commonLearnerStruggles: ["Subtle emotional nuances in traditional poetic recitation (ерөөлийн аялга)."]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Mastery of the entire honorific matrix: respectful vocabulary, humble self-reference, indirect requests"],
      kinshipAndAgeRespect: "Flawless execution of all cultural etiquette rules across generations, ranks, and social settings.",
      registersHandled: [
        "All registers from intimate vernacular to supreme ceremonial state register",
        "Official chancellery (Төрийн албан бичиг)",
        "Academic and scientific (Шинжлэх ухааны найруулга)",
        "Journalistic (Нийтлэлийн найруулга)",
        "Literary and poetic (Уран зохиолын найруулга)"
      ],
      culturalEtiquette: [
        "Deep intuitive grasp of Mongolian cosmological concepts: Тэнгэр, газар дэлхий, лус савдаг, төрийн сүлд.",
        "Active participation in traditional formal oratory and ceremonial banqueting."
      ]
    }
  },
  {
    level: "C2",
    name: "Mastery of Modern Eloquence & Cultural Heritage",
    mongolianName: "Дээд шат: Төгс эзэмшил ба соёлын өв",
    summary: "Effortlessly understand virtually everything heard or read in modern Mongolian society; navigate rapid unscripted colloquial exchanges, regional dialectal speech, subtle irony, humor, and understatement; produce highly articulate, persuasive modern editorial, academic, and professional discourse; and engage with classical literature, epic poetry, and ceremonial oratory as an advanced cultural enrichment dimension.",
    receptiveVocabularyEstimate: 10000,
    productiveVocabularyEstimate: 6500,
    listening: {
      speechSpeed: "Any native speech speed, including rapid unscripted colloquial speech, phonetically reduced natural talk, radio/podcast banter, heated parliamentary debates, and regional dialectal variations.",
      utteranceLength: "Unrestricted; multi-hour lectures, investigative broadcasts, panel discussions, courtroom arguments, and traditional storytelling.",
      vocabularyFamiliarity: "Comprehensive mastery of modern standard Mongolian, high-frequency slang, professional and academic terminology, journalistic idioms, complemented by classical and pastoral terms.",
      grammaticalComplexity: "Universal mastery of all modern syntactic constructions, complex converb clause chaining, nuanced epistemic particles, and classical stylistic forms.",
      registersAndGenres: ["Live unscripted street interviews and television talk shows", "Investigative podcasts and round-table discussions", "Supreme court judicial deliberations and legal arguments", "Scholarly debates on contemporary sociolinguistics", "Traditional epics and ceremonial oratory (cultural enrichment)"],
      canUnderstand: [
        "Rapid natural conversational Khalkha with extreme unstressed vowel reduction and particle coalescence.",
        "Subtle regional dialectal variations across western (Oirat), eastern (Buryat, Dariganga), and southern Mongolian speech.",
        "Deeply nuanced humorous, sarcastic, ironical, and philosophically veiled modern speech.",
        "Traditional heroic epics (Жангар, Гэсэр) and oral blessings as cultural heritage."
      ],
      limitations: ["Virtually none within Modern Standard Mongolian and its living spoken varieties."]
    },
    reading: {
      wordRecognition: "Immediate and effortless across modern publications, academic papers, literary works, and administrative documents.",
      sentenceComplexity: "Universal mastery of modern syntactic architecture, complex participial subordination, and stylized prose.",
      textLength: "Unrestricted.",
      genres: ["Contemporary investigative journalism and editorial essays", "Monographs in sociology, economics, law, and history", "Award-winning modern Mongolian novels, short stories, and essays", "Statutory legislation, contracts, and bilateral treaties", "The Secret History of the Mongols (modern Cyrillic edition) and historical chronicles (enrichment)"],
      unfamiliarVocabTolerance: "Complete philological capability; easily deduces meaning through morphology, context, and Mongolic root analysis.",
      inferredMeaning: "Perceives the finest shades of emotional stance, irony, cultural metaphor, and sociopolitical subtext.",
      canRead: [
        "Complex editorial polemics, satire, and cultural commentary with complete appreciation of nuance.",
        "Modern legislation, administrative regulations, and commercial arbitration filings.",
        "Contemporary Mongolian literature, poetry, and reflective memoirs.",
        "The Secret History of the Mongols in modern Cyrillic adaptation with historical and syntactic comprehension."
      ],
      limitations: ["None in modern Mongolian Cyrillic."]
    },
    spokenProduction: {
      fluencyAndPacing: "Native-equivalent fluency, articulation, rhythmic mastery, and communicative precision.",
      interactionScope: "Unrestricted; can speak authoritatively on complex topics in any setting, public or private, professional or informal.",
      discourseTypes: ["Spontaneous debate and negotiation", "Public political and civic oratory", "Academic doctoral defenses and peer critiques", "Contemporary broadcast media commentary", "Traditional ceremonial blessing (ерөөл тавих) for special rites"],
      canProduce: [
        "Participate in heated live discussions and debates with rapid rhetorical adaptation, humor, and persuasive tact.",
        "Lead high-stakes professional negotiations and diplomatic discussions with register-appropriate finesse.",
        "Express subtle philosophical, social, and emotional distinctions using rich modern vocabulary.",
        "Switch effortlessly between colloquial banter, formal administrative, and elevated ceremonial registers as social decorum demands."
      ],
      limitations: ["None."]
    },
    writtenProduction: {
      scriptAndTyping: "Flawless orthographic and stylistic mastery across all modern genres of writing.",
      textComplexity: "Publishable literary, scholarly, journalistic, or legal works of unrestricted length and complexity.",
      genres: ["Journalistic opinion pieces and investigative features", "Scholarly research papers and monographs", "Professional legal briefs and policy white papers", "Creative literary prose and contemporary essays", "Traditional alliterative verse and ceremonial blessings (enrichment)"],
      canWrite: [
        "Persuasive, elegant opinion columns and cultural commentaries for leading media outlets.",
        "A full-length scholarly paper or policy analysis meeting rigorous academic standards.",
        "Statutory drafts, legal contracts, or official administrative directives in precise legal Mongolian.",
        "Creative prose, contemporary essays, and traditional metric alliteration when culturally appropriate."
      ],
      limitations: ["None."]
    },
    grammarControl: {
      activeControl: [
        "Universal mastery of the entire grammatical and syntactic inventory of Modern Mongolian",
        "Nuanced deployment of epistemic stance particles and indirect speech framing",
        "Flawless orchestration of complex multi-clause sentence architectures",
        "Effortless control of all passive, causative, and reciprocal voice configurations",
        "Supreme mastery of textual cohesion, discourse pragmatics, and rhetorical transitions"
      ],
      receptiveControl: [
        "Comprehension of classical and archaic syntactic patterns, legal formulations, and dialectal variations"
      ],
      emergingStructures: ["Personal authorial voice, stylistic versatility, and rhetorical eloquence"]
    },
    pronunciationPhonology: {
      phonemicContrasts: [
        "Indistinguishable from an educated native speaker across all speech styles, speeds, and registers",
        "Mastery of natural connected speech processes (coalescence, reduction, assimilation) as well as formal oratorical cadence"
      ],
      vowelHarmonyControl: "Universal, natural, and intuitive.",
      palatalizationControl: "Universal and native-level in both rapid colloquial and formal speech.",
      prosodyAndIntonation: "Complete mastery of all communicative, emotional, and pragmatic prosodic patterns.",
      commonLearnerStruggles: ["None."]
    },
    pragmaticsAndRegister: {
      politenessMarkers: ["Effortless mastery of all shades of social distance, honorific elevation, and contemporary peer politeness"],
      kinshipAndAgeRespect: "Flawless adherence to traditional kinship protocol, seating arrangements, and ritual gestures.",
      registersHandled: [
        "All modern registers: urban colloquial, youth slang, standard neutral, administrative, academic, journalistic, literary, and ceremonial"
      ],
      culturalEtiquette: [
        "Living understanding of Mongolian cultural memory, nomadic heritage, historical transitions, and modern democratic resilience.",
        "Complete cultural and linguistic fluency as an articulate user of modern Mongolian."
      ]
    }
  }
];
