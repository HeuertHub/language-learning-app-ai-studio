export interface LexicalDomainSpec {
  domainId: string;
  englishName: string;
  mongolianName: string;
  targetProficiency: string;
  estimatedDomainSpecificVocabularyTarget: number;
  coreSubdomains: string[];
  sampleBenchmarkTerms: { mongolian: string; english: string; partOfSpeech: string }[];
  culturalContextNotes: string;
}

export interface FrequencyBandSpec {
  bandId: string;
  name: string;
  rankRange: [number, number];
  primaryCEFR: string[];
  pedagogicalRole: string;
  exampleLemmas: string[];
}

export interface CrossDomainGeneralVocabularyItem {
  lemma: string;
  partOfSpeech: string;
  englishGloss: string;
  frequencyBand: string;
  firstTargetLevel: string;
  crossDomainApplications: string[];
}

export interface MultiDimensionalLexicalFramework {
  classificationAxes: {
    frequencyBands: FrequencyBandSpec[];
    grammaticalFunctions: string[];
    semanticFields: string[];
    registers: string[];
    priorities: string[];
    concreteness: string[];
    mediumBiases: string[];
    scopeTypes: string[];
  };
  crossDomainCoreVerbsAndWords: CrossDomainGeneralVocabularyItem[];
  vocabularyTargetBreakdown: {
    coreSingleWordLemmasProjected: number;
    coreSingleWordLemmasRange: [number, number];
    independentlyLexicalizedDerivationsProjected: number;
    independentlyLexicalizedDerivationsRange: [number, number];
    primaryLexicalLemmasCombinedProjected: number;
    primaryLexicalLemmasCombinedRange: [number, number];
    multiwordExpressionsProjected: number;
    multiwordExpressionsRange: [number, number];
    functionWordsAndParticlesProjected: number;
    functionWordsAndParticlesRange: [number, number];
    properNounsProjected: number;
    properNounsRange: [number, number];
    inflectedSurfaceFormsCount: number;
    inflectedFormsExclusionRule: string;
  };
  thematicDomains: LexicalDomainSpec[];
}

export const lexicalDomainsData: LexicalDomainSpec[] = [
  // A1 Domains
  {
    domainId: "lex_a1_core_greetings_courtesy",
    englishName: "Greetings, Politeness, and Personal Identity",
    mongolianName: "Мэндчилгээ, хүндэтгэл ба хувийн мэдээлэл",
    targetProficiency: "A1",
    estimatedDomainSpecificVocabularyTarget: 140,
    coreSubdomains: ["Formal greetings", "Informal greetings", "Partings", "Titles of address", "Nationalities & languages"],
    sampleBenchmarkTerms: [
      { mongolian: "сайн байна уу", english: "hello / how are you", partOfSpeech: "formulaic expression" },
      { mongolian: "баярлалаа", english: "thank you", partOfSpeech: "formulaic expression" },
      { mongolian: "уучлаарай", english: "excuse me / sorry", partOfSpeech: "formulaic expression" },
      { mongolian: "багш", english: "teacher", partOfSpeech: "noun" },
      { mongolian: "оюутан", english: "student", partOfSpeech: "noun" },
      { mongolian: "нэр", english: "name", partOfSpeech: "noun" },
      { mongolian: "улс", english: "country / nation", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Essential distinction between respectful greeting to elders (Та сайн байна уу) vs peers (Сайн уу)."
  },
  {
    domainId: "lex_a1_numerals_time_calendar",
    englishName: "Numerals, Timekeeping, and Calendar",
    mongolianName: "Тоо, цаг хугацаа ба хуанли",
    targetProficiency: "A1",
    estimatedDomainSpecificVocabularyTarget: 180,
    coreSubdomains: ["Cardinal numbers 0-10,000", "Ordinal numbers", "Days of the week", "Months", "Clock intervals"],
    sampleBenchmarkTerms: [
      { mongolian: "нэг", english: "one", partOfSpeech: "numeral" },
      { mongolian: "арав", english: "ten", partOfSpeech: "numeral" },
      { mongolian: "зуу", english: "hundred", partOfSpeech: "numeral" },
      { mongolian: "мянга", english: "thousand", partOfSpeech: "numeral" },
      { mongolian: "өнөөдөр", english: "today", partOfSpeech: "noun/adverb" },
      { mongolian: "маргааш", english: "tomorrow", partOfSpeech: "noun/adverb" },
      { mongolian: "даваа гараг", english: "Monday", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Traditional days of the week use Tibetan loan designations (Даваа, Мягмар...) alongside ordinal references (нэг дэх өдөр)."
  },
  {
    domainId: "lex_a1_kinship_family",
    englishName: "Family and Kinship Relations",
    mongolianName: "Гэр бүл, төрөл садан",
    targetProficiency: "A1",
    estimatedDomainSpecificVocabularyTarget: 130,
    coreSubdomains: ["Immediate family", "Extended maternal/paternal relatives", "Age distinctions in siblings"],
    sampleBenchmarkTerms: [
      { mongolian: "аав", english: "father", partOfSpeech: "noun" },
      { mongolian: "ээж", english: "mother", partOfSpeech: "noun" },
      { mongolian: "ах", english: "older brother", partOfSpeech: "noun" },
      { mongolian: "эгч", english: "older sister", partOfSpeech: "noun" },
      { mongolian: "дүү", english: "younger sibling", partOfSpeech: "noun" },
      { mongolian: "өвөө", english: "grandfather", partOfSpeech: "noun" },
      { mongolian: "эмээ", english: "grandmother", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Strict lexical differentiation between older brother (ах) and younger sibling (дүү); age seniority is encoded in basic nouns."
  },
  {
    domainId: "lex_a1_food_dining_traditional",
    englishName: "Daily Food, Beverages, and Traditional Cuisine",
    mongolianName: "Хоол хүнс, ундаа ба уламжлалт идээ",
    targetProficiency: "A1",
    estimatedDomainSpecificVocabularyTarget: 210,
    coreSubdomains: ["Dairy products (цагаан идээ)", "Meat dishes (улаан идээ)", "Staples & vegetables", "Dining utensils"],
    sampleBenchmarkTerms: [
      { mongolian: "сүүтэй цай", english: "milk tea", partOfSpeech: "noun phrase" },
      { mongolian: "бууз", english: "steamed meat dumplings", partOfSpeech: "noun" },
      { mongolian: "хуушуур", english: "fried meat pastry", partOfSpeech: "noun" },
      { mongolian: "мах", english: "meat", partOfSpeech: "noun" },
      { mongolian: "талх", english: "bread", partOfSpeech: "noun" },
      { mongolian: "ааруул", english: "dried curd", partOfSpeech: "noun" },
      { mongolian: "ус", english: "water", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Dichotomy between white food (цагаан идээ - dairy) and red food (улаан идээ - meat) forms the core dietary conceptual framework."
  },
  {
    domainId: "lex_a1_housing_ger_household",
    englishName: "Housing, the Ger, and Household Objects",
    mongolianName: "Орон сууц, монгол гэр ба ахуйн эд хогшил",
    targetProficiency: "A1",
    estimatedDomainSpecificVocabularyTarget: 190,
    coreSubdomains: ["Ger structural elements", "Modern apartment rooms", "Furniture", "Daily tools"],
    sampleBenchmarkTerms: [
      { mongolian: "гэр", english: "ger / home", partOfSpeech: "noun" },
      { mongolian: "тооно", english: "ger roof crown", partOfSpeech: "noun" },
      { mongolian: "багана", english: "ger pillar", partOfSpeech: "noun" },
      { mongolian: "хана", english: "wall / lattice wall", partOfSpeech: "noun" },
      { mongolian: "зуух", english: "stove", partOfSpeech: "noun" },
      { mongolian: "ширээ", english: "table", partOfSpeech: "noun" },
      { mongolian: "үүд", english: "door / threshold", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Vocabulary encodes the spatial cosmology of the ger (door facing South, hoimor to the North)."
  },

  // A2 Domains
  {
    domainId: "lex_a2_urban_navigation_transit",
    englishName: "Urban Navigation, Transit, and Directions",
    mongolianName: "Хотоор зорчих, тээвэр ба зам чиглэл",
    targetProficiency: "A2",
    estimatedDomainSpecificVocabularyTarget: 220,
    coreSubdomains: ["Public buses & cards", "Taxi & ride navigation", "Landmarks & intersections", "Pedestrian routes"],
    sampleBenchmarkTerms: [
      { mongolian: "автобус", english: "bus", partOfSpeech: "noun" },
      { mongolian: "зогсоол", english: "bus stop / parking", partOfSpeech: "noun" },
      { mongolian: "түгжрэл", english: "traffic jam", partOfSpeech: "noun" },
      { mongolian: "баруун тийш", english: "towards the right / west", partOfSpeech: "adverb" },
      { mongolian: "зүүн тийш", english: "towards the left / east", partOfSpeech: "adverb" },
      { mongolian: "буудал", english: "station / hotel", partOfSpeech: "noun" },
      { mongolian: "хөлслөх", english: "to hire / rent (a taxi)", partOfSpeech: "verb" }
    ],
    culturalContextNotes: "Directions in Mongolia frequently alternate between cardinal (north/south/east/west) and relative (left/right)."
  },
  {
    domainId: "lex_a2_shopping_commerce_clothing",
    englishName: "Commerce, Markets, and Traditional/Modern Clothing",
    mongolianName: "Худалдаа, зах зээл ба хувцас хэрэглэл",
    targetProficiency: "A2",
    estimatedDomainSpecificVocabularyTarget: 260,
    coreSubdomains: ["Open-air bazaars (Нарантуул)", "Malls & supermarkets", "Traditional dress (дээл, бүс, малгай, гутал)", "Modern clothing"],
    sampleBenchmarkTerms: [
      { mongolian: "дээл", english: "traditional tunic", partOfSpeech: "noun" },
      { mongolian: "бүс", english: "sash / belt", partOfSpeech: "noun" },
      { mongolian: "гутал", english: "boots / shoes", partOfSpeech: "noun" },
      { mongolian: "үнэ", english: "price", partOfSpeech: "noun" },
      { mongolian: "хямдрал", english: "discount / sale", partOfSpeech: "noun" },
      { mongolian: "худалдагч", english: "seller / shop clerk", partOfSpeech: "noun" },
      { mongolian: "хэмжээ", english: "size", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Essential terminology for negotiating, examining garment quality, and appreciating traditional felt/silk handicrafts."
  },
  {
    domainId: "lex_a2_health_body_medicine",
    englishName: "Human Anatomy, Health, and Clinical Visits",
    mongolianName: "Хүний бие, эрүүл мэнд ба эмнэлгийн үйлчилгээ",
    targetProficiency: "A2",
    estimatedDomainSpecificVocabularyTarget: 240,
    coreSubdomains: ["External body parts", "Common ailments & symptoms", "Pharmacies & medications", "Clinic appointments"],
    sampleBenchmarkTerms: [
      { mongolian: "толгой", english: "head", partOfSpeech: "noun" },
      { mongolian: "хэвлий", english: "abdomen / belly", partOfSpeech: "noun" },
      { mongolian: "халуурах", english: "to run a fever", partOfSpeech: "verb" },
      { mongolian: "ханиад", english: "cold / flu", partOfSpeech: "noun" },
      { mongolian: "эм", english: "medicine", partOfSpeech: "noun" },
      { mongolian: "эмч", english: "doctor", partOfSpeech: "noun" },
      { mongolian: "өвдөх", english: "to ache / be in pain", partOfSpeech: "verb" }
    ],
    culturalContextNotes: "Physical symptoms often integrate with traditional diagnostic concepts (e.g. хий хурах, даарах)."
  },
  {
    domainId: "lex_a2_five_animals_herding",
    englishName: "The Five Herding Animals and Pastoral Husbandry",
    mongolianName: "Таван хошуу мал ба мал маллагаа",
    targetProficiency: "A2",
    estimatedDomainSpecificVocabularyTarget: 270,
    coreSubdomains: ["Five animals (морь, тэмээ, үхэр, хонь, ямаа)", "Age & sex terms for livestock", "Pastures & enclosures", "Seasonal herding tasks"],
    sampleBenchmarkTerms: [
      { mongolian: "унага", english: "foal", partOfSpeech: "noun" },
      { mongolian: "даага", english: "two-year-old colt", partOfSpeech: "noun" },
      { mongolian: "хурга", english: "lamb", partOfSpeech: "noun" },
      { mongolian: "бэлчээр", english: "pasture", partOfSpeech: "noun" },
      { mongolian: "саах", english: "to milk", partOfSpeech: "verb" },
      { mongolian: "хариулах", english: "to herd / graze animals", partOfSpeech: "verb" },
      { mongolian: "хот", english: "livestock pen / settlement", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Mongolian has extraordinarily specialized terminology for every year of growth and color pattern of livestock."
  },

  // B1 Domains
  {
    domainId: "lex_b1_education_career_workplace",
    englishName: "Education, Career Development, and Workplace",
    mongolianName: "Боловсрол, мэргэжил ба ажлын байр",
    targetProficiency: "B1",
    estimatedDomainSpecificVocabularyTarget: 340,
    coreSubdomains: ["University faculties & degrees", "Job applications & CVs", "Office meetings & memos", "Professional responsibilities"],
    sampleBenchmarkTerms: [
      { mongolian: "мэргэжил", english: "profession / specialization", partOfSpeech: "noun" },
      { mongolian: "төгсөх", english: "to graduate", partOfSpeech: "verb" },
      { mongolian: "гэрээ", english: "contract", partOfSpeech: "noun" },
      { mongolian: "хамт олон", english: "workplace colleagues / team", partOfSpeech: "noun phrase" },
      { mongolian: "тушаал", english: "decree / order / rank", partOfSpeech: "noun" },
      { mongolian: "цалин", english: "salary", partOfSpeech: "noun" },
      { mongolian: "өргөдөл", english: "application / petition", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Concepts of 'хамт олон' (collective work unit) hold strong social and cultural importance in Mongolian professional life."
  },
  {
    domainId: "lex_b1_national_festivals_rituals",
    englishName: "National Festivals, Ceremonies, and Holidays",
    mongolianName: "Үндэсний их баяр наадам, ёс заншил",
    targetProficiency: "B1",
    estimatedDomainSpecificVocabularyTarget: 320,
    coreSubdomains: ["Tsagaan Sar rituals", "Naadam's Three Manly Games", "State flag day & independence", "Ceremonial toasts & blessings"],
    sampleBenchmarkTerms: [
      { mongolian: "золгох", english: "to perform the formal arm-supporting greeting", partOfSpeech: "verb" },
      { mongolian: "бөхийн барилдаан", english: "wrestling match", partOfSpeech: "noun phrase" },
      { mongolian: "хурдан морь", english: "racehorse", partOfSpeech: "noun phrase" },
      { mongolian: "сур харвах", english: "to shoot arrows", partOfSpeech: "verb phrase" },
      { mongolian: "хадаг", english: "ceremonial silk scarf", partOfSpeech: "noun" },
      { mongolian: "ууц", english: "boiled sheep's back meat", partOfSpeech: "noun" },
      { mongolian: "шивээх", english: "to sprinkle milk offering", partOfSpeech: "verb" }
    ],
    culturalContextNotes: "Essential vocabulary for actively participating in family and state celebrations with correct ceremonial decorum."
  },
  {
    domainId: "lex_b1_geography_landforms_aimags",
    englishName: "Mongolian Physical Geography, Aimags, and Ecosystems",
    mongolianName: "Монгол орны газар зүй, аймаг сум ба экосистем",
    targetProficiency: "B1",
    estimatedDomainSpecificVocabularyTarget: 310,
    coreSubdomains: ["The 21 Aimags & geographical zones", "Khangai, Gobi, Steppe, Taiga", "Rivers, lakes & sacred mountains", "Administrative soums"],
    sampleBenchmarkTerms: [
      { mongolian: "аймаг", english: "province (aimag)", partOfSpeech: "noun" },
      { mongolian: "сум", english: "district / soum", partOfSpeech: "noun" },
      { mongolian: "говь", english: "gobi / semi-arid desert", partOfSpeech: "noun" },
      { mongolian: "хангай", english: "fertile mountainous zone", partOfSpeech: "noun" },
      { mongolian: "тал нутаг", english: "steppe country", partOfSpeech: "noun phrase" },
      { mongolian: "нуурын хөвөө", english: "lakeshore", partOfSpeech: "noun phrase" },
      { mongolian: "дархан цаазат газар", english: "specially protected nature reserve", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "The ecological dichotomy between Khangai (forested mountains) and Gobi (arid steppe) shapes regional dialects and identities."
  },
  {
    domainId: "lex_b1_media_digital_society",
    englishName: "Media, Internet, Communication, and Digital Society",
    mongolianName: "Хэвлэл мэдээлэл, харилцаа холбоо ба цахим ертөнц",
    targetProficiency: "B1",
    estimatedDomainSpecificVocabularyTarget: 330,
    coreSubdomains: ["News broadcasting & journalism", "Social media & digital platforms", "Mobile banking & telecommunications", "Public discourse"],
    sampleBenchmarkTerms: [
      { mongolian: "мэдээлэл", english: "information / news", partOfSpeech: "noun" },
      { mongolian: "сүлжээ", english: "network / internet", partOfSpeech: "noun" },
      { mongolian: "нийтлэл", english: "article / publication", partOfSpeech: "noun" },
      { mongolian: "ярилцлага", english: "interview", partOfSpeech: "noun" },
      { mongolian: "хэрэглэгч", english: "user / customer", partOfSpeech: "noun" },
      { mongolian: "нэвтрүүлэг", english: "broadcast / television program", partOfSpeech: "noun" },
      { mongolian: "цахим шуудан", english: "email", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Mongolia has an exceptionally high smartphone and social media usage rate per capita."
  },

  // B2 Domains
  {
    domainId: "lex_b2_ecology_climate_zud",
    englishName: "Steppe Ecology, Climate Extremes, and Zud Disasters",
    mongolianName: "Байгаль орчин, уур амьсгал ба зуд турхан",
    targetProficiency: "B2",
    estimatedDomainSpecificVocabularyTarget: 380,
    coreSubdomains: ["Zud categories (white, iron, black)", "Pasture carrying capacity & degradation", "Desertification & reforestation", "Climate change in Central Asia"],
    sampleBenchmarkTerms: [
      { mongolian: "зуд", english: "winter pastoral disaster", partOfSpeech: "noun" },
      { mongolian: "цөлжилт", english: "desertification", partOfSpeech: "noun" },
      { mongolian: "бэлчээрийн даац", english: "pasture carrying capacity", partOfSpeech: "noun phrase" },
      { mongolian: "отор хийх", english: "emergency seasonal pasture migration", partOfSpeech: "verb phrase" },
      { mongolian: "нөхөн сэргээлт", english: "environmental reclamation", partOfSpeech: "noun" },
      { mongolian: "цасан бүрхүүл", english: "snow cover layer", partOfSpeech: "noun phrase" },
      { mongolian: "дулаарал", english: "global warming", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Zud terminology is essential for understanding contemporary rural-to-urban migration and pasture tenure issues."
  },
  {
    domainId: "lex_b2_material_culture_horsemanship",
    englishName: "Nomadic Material Culture, Saddlery, and Horsemanship",
    mongolianName: "Нүүдлийн соёл, морины тоног хэрэгсэл ба эдлэл",
    targetProficiency: "B2",
    estimatedDomainSpecificVocabularyTarget: 360,
    coreSubdomains: ["Saddlery & tack (эмээл, хазаар, ташуур)", "Felt making & leather craftsmanship", "Metalwork, silver cups & snuff bottles (хөөрөг)", "Woodcarving"],
    sampleBenchmarkTerms: [
      { mongolian: "эмээл", english: "saddle", partOfSpeech: "noun" },
      { mongolian: "хазаар", english: "bridle", partOfSpeech: "noun" },
      { mongolian: "ташуур", english: "horse whip", partOfSpeech: "noun" },
      { mongolian: "хөөрөг", english: "snuff bottle", partOfSpeech: "noun" },
      { mongolian: "аргамжих", english: "to tether a horse", partOfSpeech: "verb" },
      { mongolian: "унгас", english: "raw sheep wool for felt", partOfSpeech: "noun" },
      { mongolian: "мөнгөн аяга", english: "silver-lined wooden bowl", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Snuff bottle exchange (хөөрөг зөрүүлэх) is one of the highest traditional etiquette rituals."
  },
  {
    domainId: "lex_b2_performing_arts_music_folklore",
    englishName: "Performing Arts, Folk Music, and Steppe Acoustics",
    mongolianName: "Язгуур урлаг, морин хуур ба хөгжмийн өв",
    targetProficiency: "B2",
    estimatedDomainSpecificVocabularyTarget: 350,
    coreSubdomains: ["Morin Khuur construction & playing styles", "Throat singing (хөөмий - sygyt, kargyraa)", "Long Song (уртын дуу)", "Biyelgee (traditional body dance)"],
    sampleBenchmarkTerms: [
      { mongolian: "морин хуур", english: "horsehead fiddle", partOfSpeech: "noun phrase" },
      { mongolian: "хөөмий", english: "throat overtone singing", partOfSpeech: "noun" },
      { mongolian: "уртын дуу", english: "Mongolian long song", partOfSpeech: "noun phrase" },
      { mongolian: "шууранхай", english: "falsetto long song vocal ornament", partOfSpeech: "noun" },
      { mongolian: "биелгээ", english: "traditional western body dance", partOfSpeech: "noun" },
      { mongolian: "чавхдас", english: "instrument string", partOfSpeech: "noun" },
      { mongolian: "эгшиглэх", english: "to resonate / sound melodiously", partOfSpeech: "verb" }
    ],
    culturalContextNotes: "Musical aesthetics mimic the natural acoustics of wind, water, and animal vocalizations."
  },
  {
    domainId: "lex_b2_governance_democracy_civil_society",
    englishName: "State Institutions, Democratic Governance, and Civil Society",
    mongolianName: "Төрийн тогтолцоо, ардчилал ба иргэний нийгэм",
    targetProficiency: "B2",
    estimatedDomainSpecificVocabularyTarget: 370,
    coreSubdomains: ["State Great Khural (parliament)", "Presidency & executive ministries", "Electoral processes & parties", "NGOs & civic participation"],
    sampleBenchmarkTerms: [
      { mongolian: "Улсын Их Хурал", english: "State Great Khural (Parliament)", partOfSpeech: "proper noun phrase" },
      { mongolian: "сонгууль", english: "election", partOfSpeech: "noun" },
      { mongolian: "хууль тогтоомж", english: "legislation / statutory enactments", partOfSpeech: "noun phrase" },
      { mongolian: "төрийн алба", english: "civil service", partOfSpeech: "noun phrase" },
      { mongolian: "яам", english: "ministry", partOfSpeech: "noun" },
      { mongolian: "шүүмжлэл", english: "criticism / critique", partOfSpeech: "noun" },
      { mongolian: "санал хураалт", english: "balloting / vote casting", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Vocabulary reflecting the post-1990 multi-party parliamentary democratic governance model."
  },

  // C1 Domains
  {
    domainId: "lex_c1_jurisprudence_constitutional_law",
    englishName: "Jurisprudence, Statutory Legislation, and Human Rights",
    mongolianName: "Хууль зүй, Үндсэн хуулийн эрх зүй ба хүний эрх",
    targetProficiency: "C1",
    estimatedDomainSpecificVocabularyTarget: 420,
    coreSubdomains: ["1992 Constitution & constitutional review", "Civil, criminal & administrative codes", "Court proceedings & verdicts", "Human rights conventions"],
    sampleBenchmarkTerms: [
      { mongolian: "Үндсэн хууль", english: "Constitution", partOfSpeech: "noun phrase" },
      { mongolian: "заалт", english: "clause / statutory provision", partOfSpeech: "noun" },
      { mongolian: "тогтоол", english: "resolution / decree", partOfSpeech: "noun" },
      { mongolian: "хэрэг хянан шийдвэрлэх", english: "to adjudicate / try a case", partOfSpeech: "verb phrase" },
      { mongolian: "шүүгдэгч", english: "defendant", partOfSpeech: "noun" },
      { mongolian: "эрх зүйн чадамж", english: "legal capacity", partOfSpeech: "noun phrase" },
      { mongolian: "хохирол барагдуулах", english: "to compensate for damages", partOfSpeech: "verb phrase" }
    ],
    culturalContextNotes: "The linguistic register of Mongolian statutes requires complex nominalized participial framing and formulaic legal postpositions."
  },
  {
    domainId: "lex_c1_macroeconomics_mining_infrastructure",
    englishName: "Macroeconomics, Extractive Industries, and Infrastructure",
    mongolianName: "Макро эдийн засаг, уул уурхай ба дэд бүтэц",
    targetProficiency: "C1",
    estimatedDomainSpecificVocabularyTarget: 410,
    coreSubdomains: ["Mining extraction (copper, coal, gold)", "Sovereign wealth funds & fiscal policy", "Railway & energy logistics", "Foreign direct investment"],
    sampleBenchmarkTerms: [
      { mongolian: "баяжмал", english: "mineral concentrate", partOfSpeech: "noun" },
      { mongolian: "ашигт малтмал", english: "mineral resources", partOfSpeech: "noun phrase" },
      { mongolian: "гадаадын шууд хөрөнгө оруулалт", english: "foreign direct investment", partOfSpeech: "noun phrase" },
      { mongolian: "инфляцийн түвшин", english: "inflation rate", partOfSpeech: "noun phrase" },
      { mongolian: "төсвийн алдагдал", english: "fiscal deficit", partOfSpeech: "noun phrase" },
      { mongolian: "нүүрсний экспорт", english: "coal export", partOfSpeech: "noun phrase" },
      { mongolian: "төмөр замын тээвэр", english: "rail transport", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Essential for following contemporary economic debates regarding mining revenue sharing and resource nationalism."
  },
  {
    domainId: "lex_c1_diplomacy_geopolitics_foreign_policy",
    englishName: "Diplomacy, Regional Geopolitics, and Third Neighbor Policy",
    mongolianName: "Гадаад харилцаа, геополитик ба 'Гуравдагч хөрш'-ийн бодлого",
    targetProficiency: "C1",
    estimatedDomainSpecificVocabularyTarget: 400,
    coreSubdomains: ["Relations with China & Russia", "Third Neighbor policy (US, EU, Japan, Korea)", "UN peacekeeping deployments", "International treaties & summits"],
    sampleBenchmarkTerms: [
      { mongolian: "гуравдагч хөрш", english: "Third Neighbor", partOfSpeech: "noun phrase" },
      { mongolian: "хоёр талын харилцаа", english: "bilateral relations", partOfSpeech: "noun phrase" },
      { mongolian: "энхийг сахиулах", english: "peacekeeping", partOfSpeech: "verb phrase / noun" },
      { mongolian: "тусгаар тогтнол", english: "national sovereignty / independence", partOfSpeech: "noun" },
      { mongolian: "санамж бичиг", english: "memorandum of understanding", partOfSpeech: "noun phrase" },
      { mongolian: "хэлэлцээр", english: "treaty / negotiation", partOfSpeech: "noun" },
      { mongolian: "стратегийн түншлэл", english: "strategic partnership", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Mongolia's 'Third Neighbor' doctrine is a cornerstone of national security and diplomatic rhetoric."
  },
  {
    domainId: "lex_c1_academic_philology_mongolistics",
    englishName: "Mongolian Philology, Historical Linguistics, and Mongolistics",
    mongolianName: "Монгол судлал, хэл шинжлэл ба сурвалж судлал",
    targetProficiency: "C1",
    estimatedDomainSpecificVocabularyTarget: 430,
    coreSubdomains: ["Classical Mongolian script analysis", "Dialectology (Khalkha, Buryat, Oirat, Inner Mongolian)", "Manuscript epigraphy & philological methods", "Altaic & Inner Asian comparative studies"],
    sampleBenchmarkTerms: [
      { mongolian: "сурвалж бичиг", english: "historical source document", partOfSpeech: "noun phrase" },
      { mongolian: "аялгуу", english: "dialect", partOfSpeech: "noun" },
      { mongolian: "хэл зүйн тогтолцоо", english: "grammatical system", partOfSpeech: "noun phrase" },
      { mongolian: "бичгийн дурсгал", english: "written monument / inscription", partOfSpeech: "noun phrase" },
      { mongolian: "этимологи", english: "etymology", partOfSpeech: "noun" },
      { mongolian: "харьцуулсан судалгаа", english: "comparative research", partOfSpeech: "noun phrase" },
      { mongolian: "гар бичмэл", english: "manuscript", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "Mongolistics (Монгол судлал) represents the apex academic discourse in national humanities institutions."
  },

  // C2 Domains
  {
    domainId: "lex_c2_classical_literature_secret_history",
    englishName: "Classical Literature, The Secret History, and Historical Epics",
    mongolianName: "Эртний уран зохиол, 'Монголын нууц товчоо' ба түүхэн туульс",
    targetProficiency: "C2",
    estimatedDomainSpecificVocabularyTarget: 460,
    coreSubdomains: ["1240 CE Secret History of the Mongols vocabulary", "Middle Mongol lexicon in modern transcription", "Heroic epics (Jangar, Geser)", "Chronicles of Altan Tobchi & Erdeni-yin Tobchi"],
    sampleBenchmarkTerms: [
      { mongolian: "бөртэ чоно", english: "blue-gray wolf (ancestral totem)", partOfSpeech: "noun phrase" },
      { mongolian: "анда", english: "sworn blood brother", partOfSpeech: "noun" },
      { mongolian: "хөх тэнгэр", english: "Eternal Blue Sky", partOfSpeech: "noun phrase" },
      { mongolian: "сүлд", english: "spiritual soul / state banner emblem", partOfSpeech: "noun" },
      { mongolian: "баатар", english: "hero / knight", partOfSpeech: "noun" },
      { mongolian: "хишигтэн", english: "imperial keshig royal bodyguard", partOfSpeech: "noun" },
      { mongolian: "зарлиг", english: "imperial decree / edict", partOfSpeech: "noun" }
    ],
    culturalContextNotes: "The linguistic phrasing of the Secret History permeates high-register Mongolian identity and literary prose."
  },
  {
    domainId: "lex_c2_philosophy_tengrism_buddhism",
    englishName: "Buddhism, Tengrism, and Nomadic Moral Philosophy",
    mongolianName: "Буддын гүн ухаан, Тэнгэр шүтлэг ба ёс суртахуун",
    targetProficiency: "C2",
    estimatedDomainSpecificVocabularyTarget: 440,
    coreSubdomains: ["Vajrayana Buddhist scholastic terms (Tibetan/Sanskrit roots)", "Shamanic Tengrism & nature spirits (лус савдаг)", "Karmic consequence & reincarnation (үйлийн үр)", "Nomadic bioethics"],
    sampleBenchmarkTerms: [
      { mongolian: "үйлийн үр", english: "karma / cause and effect", partOfSpeech: "noun phrase" },
      { mongolian: "гэгээрэл", english: "enlightenment / spiritual awakening", partOfSpeech: "noun" },
      { mongolian: "лус савдаг", english: "water and earth spirits", partOfSpeech: "noun phrase" },
      { mongolian: "сүсэг бишрэл", english: "religious devotion / piety", partOfSpeech: "noun phrase" },
      { mongolian: "бодь сэтгэл", english: "bodhicitta / compassionate mind", partOfSpeech: "noun phrase" },
      { mongolian: "хоосон чанар", english: "emptiness / shunyata", partOfSpeech: "noun phrase" },
      { mongolian: "буян хишиг", english: "merit and spiritual fortune", partOfSpeech: "noun phrase" }
    ],
    culturalContextNotes: "Synthesizes pre-Buddhist animist cosmology with Gelugpa Buddhist philosophical metaphysics."
  },
  {
    domainId: "lex_c2_gnomic_wisdom_proverbs_rhetoric",
    englishName: "Gnomic Metaphor, Proverbial Lore, and Supreme Oratory",
    mongolianName: "Ардын цэцэн үг, зүйр үг ба уран илтгэхүйн өв",
    targetProficiency: "C2",
    estimatedDomainSpecificVocabularyTarget: 450,
    coreSubdomains: ["Nomadic pastoral aphorisms (зүйр цэцэн үг)", "Paired metric blessings (ерөөл)", "Poetic praises of land & steed (магтаал)", "High philosophical debate rhetoric"],
    sampleBenchmarkTerms: [
      { mongolian: "дуугүй суугаа хүнийг дуугүй гэж бүү бод", english: "do not mistake silence for lack of thought", partOfSpeech: "proverb" },
      { mongolian: "дэлхий дахинд нэр алдраа дуурсгах", english: "to resonate one's fame across the world", partOfSpeech: "idiomatic phrase" },
      { mongolian: "эв санал нэгдэх", english: "to achieve seamless unanimity of purpose", partOfSpeech: "phrase" },
      { mongolian: "эрхэмсэг", english: "dignified / noble / sublime", partOfSpeech: "adjective" },
      { mongolian: "үнэн мөнийг дэнслэх", english: "to weigh truth upon the scales of justice", partOfSpeech: "idiom" },
      { mongolian: "өлзий хутаг орших болтугай", english: "may sublime auspiciousness abide", partOfSpeech: "ceremonial blessing formula" }
    ],
    culturalContextNotes: "Represents the summit of native eloquence, where metaphorical concision and alliterative balance encapsulate millennia of pastoral observation."
  }
];

export const crossDomainCoreVerbsAndWordsData: CrossDomainGeneralVocabularyItem[] = [
  { lemma: "явах", partOfSpeech: "verb", englishGloss: "to go, walk, move, travel", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["navigation", "daily routine", "workplace", "travel", "action progress"] },
  { lemma: "ирэх", partOfSpeech: "verb", englishGloss: "to come, arrive", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["greetings", "transit", "appointments", "seasons", "future time"] },
  { lemma: "авах", partOfSpeech: "verb", englishGloss: "to take, receive, buy, get", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["shopping", "dining", "workplace", "medicine", "communication"] },
  { lemma: "өгөх", partOfSpeech: "verb", englishGloss: "to give, hand over, grant", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["commerce", "family", "courtesy", "administrative", "benefactive auxiliary"] },
  { lemma: "мэдэх", partOfSpeech: "verb", englishGloss: "to know, understand, be aware of", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["education", "daily dialogue", "workplace", "navigation", "inquiry"] },
  { lemma: "бодох", partOfSpeech: "verb", englishGloss: "to think, consider, calculate", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["opinion", "commerce", "philosophy", "problem-solving", "mental state"] },
  { lemma: "хүсэх", partOfSpeech: "verb", englishGloss: "to want, desire, wish", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["dining", "career", "courtesy", "decision-making", "volition"] },
  { lemma: "хэрэгтэй", partOfSpeech: "adjective/modal", englishGloss: "needed, necessary, useful", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["all daily needs", "shopping", "health", "workplace", "planning"] },
  { lemma: "болох", partOfSpeech: "verb/auxiliary", englishGloss: "to become, happen, be possible, be allowed", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["all grammatical modals", "time passage", "cooking", "governance", "politeness"] },
  { lemma: "хэрэглэх", partOfSpeech: "verb", englishGloss: "to use, utilize, consume", frequencyBand: "Band 2", firstTargetLevel: "A2", crossDomainApplications: ["technology", "tools", "medicine", "cooking", "linguistic register"] },
  { lemma: "хэлэх", partOfSpeech: "verb", englishGloss: "to say, tell, utter", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["communication", "quotation", "instruction", "media", "negotiation"] },
  { lemma: "асуух", partOfSpeech: "verb", englishGloss: "to ask, inquire", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["directions", "classroom", "clinic", "interview", "commerce"] },
  { lemma: "харах", partOfSpeech: "verb", englishGloss: "to look at, watch, see", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["visual navigation", "arts", "observation", "daily life", "evaluation"] },
  { lemma: "үзэх", partOfSpeech: "verb", englishGloss: "to see, watch, try, experience, consider", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["entertainment", "medical exam", "trying actions (auxiliary)", "academic viewpoint"] },
  { lemma: "олох", partOfSpeech: "verb", englishGloss: "to find, acquire, earn", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["navigation", "commerce", "career", "research", "solution finding"] },
  { lemma: "ажиллах", partOfSpeech: "verb", englishGloss: "to work, operate, function", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["employment", "machinery", "civil society", "organs/health", "institutions"] },
  { lemma: "хийх", partOfSpeech: "verb", englishGloss: "to do, make, perform, create", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["all action execution", "cooking", "crafts", "administration", "hobbies"] },
  { lemma: "ойлгох", partOfSpeech: "verb", englishGloss: "to understand, comprehend", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["interpersonal dialogue", "reading", "instruction", "cultural empathy"] },
  { lemma: "байх", partOfSpeech: "verb/auxiliary", englishGloss: "to be, exist, stay, have", frequencyBand: "Band 1", firstTargetLevel: "A1", crossDomainApplications: ["existential predication", "continuous aspect", "location", "past certainty"] },
  { lemma: "чадах", partOfSpeech: "verb/auxiliary", englishGloss: "to be able to, can", frequencyBand: "Band 1", firstTargetLevel: "A2", crossDomainApplications: ["ability", "permission", "capacity", "potential", "negotiation"] }
];

export const multiDimensionalLexicalFrameworkData: MultiDimensionalLexicalFramework = {
  classificationAxes: {
    frequencyBands: [
      {
        bandId: "band_1_top_500",
        name: "Ultra-High Frequency Core Foundation",
        rankRange: [1, 500],
        primaryCEFR: ["Pre-A1", "A1"],
        pedagogicalRole: "Survival grammar, pronouns, cardinal numbers, primary auxiliary and motion verbs, core spatial postpositions.",
        exampleLemmas: ["би", "чи", "энэ", "тэр", "байх", "явах", "ирэх", "хийх", "сайн", "гэр", "ус", "хүн"]
      },
      {
        bandId: "band_2_core_communicative",
        name: "Core Communicative & Situational",
        rankRange: [501, 1500],
        primaryCEFR: ["A1", "A2"],
        pedagogicalRole: "Everyday objects, family, food, basic healthcare, transit, basic transactions, common adjectives and adverbs.",
        exampleLemmas: ["ажиллах", "сургууль", "эмнэлэг", "машин", "зам", "хямд", "хурдан", "хувцас", "хоол", "мэдэх"]
      },
      {
        bandId: "band_3_general_expanding",
        name: "General Expanding & Workplace",
        rankRange: [1501, 3500],
        primaryCEFR: ["A2", "B1"],
        pedagogicalRole: "Workplace terminology, news broadcasting, narrative past, geographical terms, social relations, emotions.",
        exampleLemmas: ["мэргэжил", "гэрээ", "мэдээлэл", "байгаль", "сонгууль", "нөхцөл", "шийдвэр", "хамгаалалт"]
      },
      {
        bandId: "band_4_advanced_general",
        name: "Advanced General, Analytical & Professional",
        rankRange: [3501, 7000],
        primaryCEFR: ["B2", "C1"],
        pedagogicalRole: "Macroeconomics, constitutional terms, ecological degradation, academic discourse markers, formal correspondence.",
        exampleLemmas: ["цөлжилт", "тогтоол", "стратеги", "инфляци", "сурвалж", "тодорхойлолт", "уялдаа", "зөрчил"]
      },
      {
        bandId: "band_5_specialized_literary",
        name: "Specialized, Literary, Philosophical & Nuance",
        rankRange: [7001, 10000],
        primaryCEFR: ["C1", "C2"],
        pedagogicalRole: "Historical epics, Secret History lexicon, Buddhist Tengrist metaphysics, archaic court terms, poetic alliteration.",
        exampleLemmas: ["хишигтэн", "лус савдаг", "шууранхай", "зарлиг", "эрхэмсэг", "өлзий", "үйлийн үр", "сүлд"]
      }
    ],
    grammaticalFunctions: [
      "Noun (Нэр үг)",
      "Verb (Үйл үг)",
      "Adjective (Тэмдэг нэр)",
      "Adverb (Дайвар үг)",
      "Pronoun (Төлөөний үг)",
      "Numeral / Quantifier (Тооны нэр / Хэмжих үг)",
      "Postposition (Холбоос үг / Дагавар үг)",
      "Particle (Сул үг)",
      "Conjunction (Холбох үг)",
      "Interjection (Аялга үг)"
    ],
    semanticFields: [
      "Kinship & Social Roles",
      "Nomadic Ecology & Pastoral Husbandry",
      "Urban Infrastructure & Commerce",
      "Spatiotemporal Deixis & Orientation",
      "Psychological & Mental States",
      "Action, Motion & Physical Impact",
      "Statecraft, Law & Public Institutions",
      "Material Culture & Technology",
      "Aesthetics, Poetics & Music",
      "Spiritual Cosmology & Philosophy"
    ],
    registers: [
      "Colloquial Spoken (Ярианы найруулга)",
      "Standard Neutral (Энгийн найруулга)",
      "Formal Administrative (Албан бичгийн найруулга)",
      "Academic & Scientific (Эрдэм шинжилгээний найруулга)",
      "Literary & Artistic (Уран зохиолын найруулга)",
      "Ceremonial & High Respectful (Хүндэтгэл, ерөөлийн найруулга)",
      "Archaic & Classical (Эртний найруулга)"
    ],
    priorities: ["Productive Core", "Receptive Comprehension"],
    concreteness: ["Concrete Physical", "Abstract Conceptual"],
    mediumBiases: ["Spoken Bias", "Written Bias", "Balanced"],
    scopeTypes: ["General-Purpose Cross-Domain", "Domain-Specific"]
  },
  crossDomainCoreVerbsAndWords: crossDomainCoreVerbsAndWordsData,
  vocabularyTargetBreakdown: {
    coreSingleWordLemmasProjected: 7200,
    coreSingleWordLemmasRange: [6500, 7500],
    independentlyLexicalizedDerivationsProjected: 1800,
    independentlyLexicalizedDerivationsRange: [1500, 2500],
    primaryLexicalLemmasCombinedProjected: 9000,
    primaryLexicalLemmasCombinedRange: [8000, 10000],
    multiwordExpressionsProjected: 2200,
    multiwordExpressionsRange: [1500, 3000],
    functionWordsAndParticlesProjected: 160,
    functionWordsAndParticlesRange: [140, 200],
    properNounsProjected: 420,
    properNounsRange: [350, 500],
    inflectedSurfaceFormsCount: 0,
    inflectedFormsExclusionRule: "Strictly excluded: Declension paradigm cases, verbal tense/aspect inflectional suffixes, and productive non-lexicalized derivatives are tracked morphologically and never counted as distinct lexical vocabulary items."
  },
  thematicDomains: lexicalDomainsData
};
