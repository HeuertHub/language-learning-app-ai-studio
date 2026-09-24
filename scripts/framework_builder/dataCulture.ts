export interface CulturalModuleSpec {
  moduleId: string;
  theme: string;
  mongolianTheme: string;
  targetLevel: string;
  scope: "National normative" | "Pastoral nomadic specific" | "Urban Ulaanbaatar specific" | "Regional / Aimag specific" | "Institutional / Formal";
  region: string;
  traditionalVsContemporary: "Traditional ideal" | "Contemporary living practice" | "Historical evolution" | "Hybrid traditional-modern";
  degreeOfUniversality: "Widespread consensus" | "Variable across families/aimags" | "Generational / declining among youth" | "Situational etiquette";
  pedagogicalCaveat: string;
  pedagogicalRole: string;
  coreConcepts: string[];
  taboosAndEtiquette: string[];
  historicalAndCosmologicalRoots: string;
  linguisticIntegration: {
    targetVocabularyFields: string[];
    grammaticalCorrelates: string[];
    communicativeTasks: string[];
  };
}

export const culturalContentArchitectureData: CulturalModuleSpec[] = [
  {
    moduleId: "cult_a1_ger_etiquette_hospitality",
    theme: "The Ger as Sacred Space, Spatial Orientation & Hospitality Customs",
    mongolianTheme: "Монгол гэр, зочлох ёсон ба цээрлэх зан үйл",
    targetLevel: "A1",
    scope: "Pastoral nomadic specific",
    region: "Rural pastoral regions and traditional ger settings nationwide",
    traditionalVsContemporary: "Contemporary living practice",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "While strictly observed in rural gers and countryside homestays, urban apartment life follows modern cosmopolitan domestic customs, though greeting respect and right-hand hospitality gestures persist even in apartments.",
    pedagogicalRole: "Foundational cultural orientation preventing severe social blunders during homestays or countryside visits.",
    coreConcepts: [
      "Spatial orientation of the Ger: door faces South; North (Хоймор) is the place of honor for elders, sacred altars, and honored guests.",
      "West side (Баруун тал) is the male domain: saddlery, herding gear, airag bag.",
      "East side (Зүүн тал) is the female domain: kitchen utensils, pantry, cradle.",
      "Central hearth (Зуух/Тулга): symbolizes the ancestral spirit and household flame (гал голомт)."
    ],
    taboosAndEtiquette: [
      "Never step on the threshold (босго дээр гишгэж болохгүй); stepping on the threshold is treated as stepping on the host's neck.",
      "Never pass anything between the two central pillars (багана хоорондоо юм дамжуулахгүй).",
      "Do not lean against the ger pillars or walls.",
      "Always receive bowls of tea or food with the right hand, with the left hand supporting the right elbow (баруун гараараа тосож авах, зүүн гараар тохойг тулах)."
    ],
    historicalAndCosmologicalRoots: "The ger functions as an astronomical clock (тооно captures sunlight marking the 12 zodiac hours) and a microcosm of nomadic cosmology.",
    linguisticIntegration: {
      targetVocabularyFields: ["гэр", "үүд", "тооно", "багана", "хоймор", "зуух", "сүүтэй цай", "идээ"],
      grammaticalCorrelates: ["Dative-locative case (-д/-т)", "Spatial postpositions (өмнө, хойно, баруун, зүүн)", "Reflexive-possessive (-аа4)"],
      communicativeTasks: ["Enter a ger properly and greet the host", "Accept tea with correct body language", "Inquire where to sit"]
    }
  },
  {
    moduleId: "cult_a1_tavan_khoshuu_mal",
    theme: "The Five Herding Animals (Таван хошуу мал) and Steppe Subsistence",
    mongolianTheme: "Таван хошуу мал ба нүүдлийн ахуй амьдрал",
    targetLevel: "A1",
    scope: "National normative",
    region: "Nationwide (rural livelihood, urban cultural identity)",
    traditionalVsContemporary: "Contemporary living practice",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "Urban Mongolians revere the five animals as symbols of national identity and consume their dairy and meat daily, but specific livestock handling and herding techniques are practical realities primarily for rural herding families.",
    pedagogicalRole: "Teaches the economic and spiritual foundation of nomadic civilization through its core animal vocabulary.",
    coreConcepts: [
      "The Five Snouts: Horse (морь), Camel (тэмээ), Cattle/Yak (үхэр/сарлаг), Sheep (хонь), Goat (ямаа).",
      "Warm-muzzled animals (халуун хошуутай мал: horse, sheep) bringing good fortune.",
      "Cold-muzzled animals (хүйтэн хошуутай мал: cattle, camel, goat) resilient in harsh weather.",
      "Pastoral products: White food (цагаан идээ - dairy) in summer, Red food (улаан идээ - meat) in winter."
    ],
    taboosAndEtiquette: [
      "Never whistle in the ger or near herds (attracts severe storms or wolves).",
      "Never call an animal by bad names.",
      "Show profound reverence to horses; a horse's head and mane are sacred."
    ],
    historicalAndCosmologicalRoots: "Centuries of empirical selective breeding in extreme continental climates, establishing a sustainable nomadic ecosystem without destroying native grasslands.",
    linguisticIntegration: {
      targetVocabularyFields: ["морь", "тэмээ", "үхэр", "хонь", "ямаа", "бэлчээр", "сүү", "мах", "айраг"],
      grammaticalCorrelates: ["Plural suffixes (-д, -с, -ууд)", "Numeral counters (толгой, ширхэг)", "Habitual present (-даг)"],
      communicativeTasks: ["Identify and count different herd animals", "Describe what herders eat across seasons", "Explain why milk tea is salted"]
    }
  },
  {
    moduleId: "cult_a2_urban_ub_life",
    theme: "Modern Ulaanbaatar: Street Life, Ger Districts, and Youth Culture",
    mongolianTheme: "Орчин үеийн Улаанбаатар: Хотын амьдрал, гэр хороолол ба залуус",
    targetLevel: "A2",
    scope: "Urban Ulaanbaatar specific",
    region: "Ulaanbaatar capital metropolitan region",
    traditionalVsContemporary: "Contemporary living practice",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "Ulaanbaatar is a hyper-modern metropolis contrasting sharply with provincial aimag centers; learners should recognize that urban youth vernacular differs from traditional countryside speech.",
    pedagogicalRole: "Bridges the gap between traditional stereotypes and the vibrant, bustling reality of a modern democratic metropolis.",
    coreConcepts: [
      "Ulaanbaatar as home to nearly half of Mongolia's total population.",
      "Contrasts between downtown skyscrapers (Сүхбаатарын талбай, Peace Avenue) and the sprawling Ger Districts (Гэр хороолол).",
      "Youth population dynamism: cafe culture, tech startups, universities, hip-hop and indie rock scenes.",
      "Urban winter challenges: coal smoke (утаа), traffic congestion (түгжрэл), and sub-zero temperatures reaching -35°C."
    ],
    taboosAndEtiquette: [
      "Pedestrian etiquette and navigating city bus card system (U-Money).",
      "Showing respect to elderly riders on public transit by giving up one's seat immediately (суудал тавьж өгөх)."
    ],
    historicalAndCosmologicalRoots: "Evolved from a mobile monastic settlement (Өргөө / Их Хүрээ) established in 1639 into the world's coldest national capital.",
    linguisticIntegration: {
      targetVocabularyFields: ["хот", "талбай", "түгжрэл", "утаа", "дэлгүүр", "автобус", "гэр хороолол", "байшин"],
      grammaticalCorrelates: ["Directional case (-руу/-рүү)", "Modal obligation (-х хэрэгтэй, -х ёстой)", "Comparative forms (-аас илүү)"],
      communicativeTasks: ["Ask for bus routes and card refills", "Discuss city traffic with a taxi driver", "Compare living in a flat vs ger district"]
    }
  },
  {
    moduleId: "cult_b1_tsagaan_sar_celebration",
    theme: "Tsagaan Sar (White Moon): Lunar New Year Rituals, Hierarchy & Renewal",
    mongolianTheme: "Цагаан сар: Сар шинийн баяр, золгох ёс ба ахмад настнаа хүндэтгэхүй",
    targetLevel: "B1",
    scope: "National normative",
    region: "Nationwide and diaspora communities",
    traditionalVsContemporary: "Hybrid traditional-modern",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "While celebrated universally by virtually all Mongolian families, specific practices (such as number of ul boov pastry layers, or gift-giving scale) vary by household budget, aimag traditions, and generational outlook.",
    pedagogicalRole: "Illuminates the highest social and familial ritual in Mongolian culture, reinforcing age-graded respect.",
    coreConcepts: [
      "The Eve of the New Year (Битүүн): cleaning house, settling all debts, family feast of whole boiled sheep back (ууц) and dumplings (бууз).",
      "The First Day of the New Year (Шинийн нэгэн): greeting the first dawn (мөрөө гаргах), visiting ancestral elders.",
      "The Zolgolt ritual (Золгох): younger person places hands underneath elder's elbows to provide support, exchanging traditional greetings.",
      "Ceremonial foods: towering tiered pastries (ул боов), white foods for spiritual purity."
    ],
    taboosAndEtiquette: [
      "Husbands and wives must never do zolgolt with each other (believed to bring divorce or discord).",
      "Two people born in the same year or pregnant women should not perform zolgolt directly.",
      "Never cry, quarrel, or utter harsh words during Tsagaan Sar."
    ],
    historicalAndCosmologicalRoots: "Originated as a seasonal dairy thanksgiving feast, formalized by Chinggis Khaan in 1206 as a national springtime celebration of renewal and clan harmony.",
    linguisticIntegration: {
      targetVocabularyFields: ["битүүн", "шинийн нэгэн", "золгох", "ул боов", "ууц", "цагаалга", "мөр гаргах", "хадаг"],
      grammaticalCorrelates: ["Honorific expressions (амар мэнд үү, та сайн шинэлж байна уу)", "Causative verbs (-уул/-үүл)", "Volitional future (-я/-е)"],
      communicativeTasks: ["Perform proper Zolgolt with elders", "Wish blessings for the New Year", "Explain the meaning of Bitüün to a foreigner"]
    }
  },
  {
    moduleId: "cult_b1_naadam_three_manly_games",
    theme: "Naadam Festival: The Three Manly Games (Эрийн гурван наадам)",
    mongolianTheme: "Үндэсний их баяр наадам: Эрийн гурван наадам ба тусгаар тогтнол",
    targetLevel: "B1",
    scope: "National normative",
    region: "Nationwide (State Naadam in Ulaanbaatar and local Aimag/Soum Naadams)",
    traditionalVsContemporary: "Contemporary living practice",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "The Central Stadium Naadam in Ulaanbaatar is a major televised state spectacle, whereas local Soum Naadams feature more grassroots community participation and spontaneous steppe hospitality.",
    pedagogicalRole: "Explores the celebration of martial prowess, cultural pride, and national independence every July 11–13.",
    coreConcepts: [
      "Mongolian Wrestling (Бөхийн барилдаан): 512 or 1024 wrestlers, no weight classes, single elimination; traditional eagle dance (дэвээ, шаваа); titles (Начин, Заан, Арслан, Аварга).",
      "Horse Racing (Хурдан морины уралдаан): 6 age categories racing 15–30 km across open steppe, ridden by child jockeys aged 7–12; the sweet praise of the last horse (Баян ходоод).",
      "Archery (Сур харвах): shooting blunt arrows at cylinders of woven leather (хана, хасаа сур); calls of encouragement (уухай).",
      "Anklebone Shooting (Шагайн харваа): flicking polished sheep astragalus bones."
    ],
    taboosAndEtiquette: [
      "Never walk between wrestlers during a bout.",
      "Never step over a wrestler's costume (зодог шуудаг) or an archer's bow.",
      "Touch the sweat of winning racehorses for good fortune, but never startle them."
    ],
    historicalAndCosmologicalRoots: "Ancient military mobilization tournaments testing readiness, agility, and stamina of the nomadic cavalry, held under the Nine White Banners (Есөн хөлт цагаан туг).",
    linguisticIntegration: {
      targetVocabularyFields: ["наадам", "бөх", "барилдах", "зодог", "шуудаг", "хурдан морь", "унаач", "сур харвах", "уухай", "баян ходоод"],
      grammaticalCorrelates: ["Passive voice (-гд/-эгд)", "Converb chains (-аад, -магц)", "Similative postpositions (бүргэд шиг, сум шиг)"],
      communicativeTasks: ["Explain the rules of Mongolian wrestling", "Describe a child jockey's race across the steppe", "Narrate a visit to the central stadium"]
    }
  },
  {
    moduleId: "cult_b2_ecology_climate_zud",
    theme: "Steppe Ecology, Climatic Extremes, and the Threat of Zud",
    mongolianTheme: "Байгаль экологи, цаг уурын эрс тэс байдал ба зуд турхан",
    targetLevel: "B2",
    scope: "Pastoral nomadic specific",
    region: "Steppe and Gobi pastoral zones, affecting national economy",
    traditionalVsContemporary: "Contemporary living practice",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "While herders bear the immediate physical brunt of Zud disasters, the resulting rural-urban migration directly affects Ulaanbaatar's demographic and economic infrastructure.",
    pedagogicalRole: "Connects traditional pastoral knowledge with the acute contemporary realities of global climate change.",
    coreConcepts: [
      "The concept of Zud (Зуд): winter natural disaster where freezing temperatures, impenetrable ice cover, or heavy snow prevent livestock from grazing, causing mass starvation.",
      "Varieties of Zud: White Zud (цагаан зуд - deep snow), Iron/Clear Zud (төмөр/мөсөн зуд - frozen ice crust), Black Zud (хар зуд - bitter freezing without snow, lacking water).",
      "Otor migration (Отор хийх): emergency long-distance seasonal pasture movement to save herds.",
      "Pasture degradation: overgrazing driven by cashmere goat herd expansion, soil erosion, desertification moving northward."
    ],
    taboosAndEtiquette: [
      "Never litter or throw dirty water into natural rivers or springs (ус бохирдуулж болохгүй).",
      "Do not dig the ground unnecessarily (earth spirits become disturbed).",
      "Treat all living pastures with custodial stewardship rather than private exploitation."
    ],
    historicalAndCosmologicalRoots: "Centuries of traditional customary environmental law (e.g. Chinggis Khaan's prohibition against washing clothes in flowing water during summer).",
    linguisticIntegration: {
      targetVocabularyFields: ["зуд", "цасан бүрхүүл", "бэлчээрийн даац", "отор", "цөлжилт", "уур амьсгал", "нөхөн сэргээлт"],
      grammaticalCorrelates: ["Causal connectives (учраас, тул, үүний улмаас)", "Counterfactual conditionals (-сан бол ... -х байсан)", "Agentless passives"],
      communicativeTasks: ["Analyze the socio-economic impacts of a recent Zud winter", "Propose measures for pasture preservation", "Participate in an environmental debate"]
    }
  },
  {
    moduleId: "cult_c1_history_empire_democratic_transition",
    theme: "Historical Continuity: The Mongol Empire, Tibetan Buddhism, and the 1990 Revolution",
    mongolianTheme: "Түүхийн уламжлал: Их Монгол Улс, Буддын шашин ба 1990 оны Ардчилсан хувьсгал",
    targetLevel: "C1",
    scope: "National normative",
    region: "Nationwide and historical territory",
    traditionalVsContemporary: "Historical evolution",
    degreeOfUniversality: "Widespread consensus",
    pedagogicalCaveat: "Historiographical interpretations of the Soviet era and socialist modernization are nuanced and debated among generations, with older generations often remembering social welfare while younger generations emphasize democratic freedom and human rights.",
    pedagogicalRole: "Provides deep historical grounding in the statehood and intellectual heritage of the Mongolian nation.",
    coreConcepts: [
      "1206 CE founding of the Great Mongol State (Их Монгол Улс) under Chinggis Khaan, unification of pastoral tribes, implementation of the Great Yasa (Их Засаг) legal code.",
      "The Pax Mongolica: religious tolerance, transcontinental postal relay system (Өртөө), paper currency, international diplomacy.",
      "The adoption of Tibetan Vajrayāna Buddhism, Undur Gegeen Zanabazar's artistic renaissance, creation of Soyombo and Square scripts.",
      "20th-century geopolitical upheaval: 1911 independence declaration, 1921 revolution, Soviet era modernization and repressions.",
      "1990 Peaceful Democratic Revolution: hunger strikes on Sükhbaatar Square leading to a multi-party democratic republic and free-market economy."
    ],
    taboosAndEtiquette: [
      "Disparaging Chinggis Khaan is deeply offensive to modern national identity.",
      "Respecting religious imagery, stupas (суварга), and circling prayer wheels strictly clockwise (нар зөв эргэх)."
    ],
    historicalAndCosmologicalRoots: "A collective historical memory spanning over two millennia from the Xiongnu Empire (Хүннү гүрэн) to the contemporary democratic state.",
    linguisticIntegration: {
      targetVocabularyFields: ["эзэнт гүрэн", "засаг хууль", "өртөө", "тусгаар тогтнол", "ардчилал", "хэлмэгдүүлэлт", "сүсэг бишрэл"],
      grammaticalCorrelates: ["Historical past tense (-жээ/-чээ)", "Official administrative register", "Complex participial clauses"],
      communicativeTasks: ["Deliver an analytical presentation on the legal legacy of the Great Yasa", "Explain the socio-political significance of the 1990 democratic revolution", "Discuss how Buddhism shapes modern ethics"]
    }
  },
  {
    moduleId: "cult_c2_intangible_heritage_epic_wisdom",
    theme: "Masterpieces of Intangible Heritage: Epic Recitation, Morin Khuur, and Proverbial Wisdom",
    mongolianTheme: "Хүн төрөлхтний соёлын биет бус өв: Туульс, морин хуур ба ардын мэргэн ухаан",
    targetLevel: "C2",
    scope: "Regional / Aimag specific",
    region: "Western Mongolian epic traditions (Altai Uriankhai, Bayad, Dörvöd) and national classical heritage",
    traditionalVsContemporary: "Traditional ideal",
    degreeOfUniversality: "Generational / declining among youth",
    pedagogicalCaveat: "Authentic multi-night epic chanting (тууль хайлах) is a specialized ritual preserved predominantly in Western Mongolia and among master rhapsodists, rather than an everyday occurrence across all households.",
    pedagogicalRole: "Elevates the student to native-level cultural appreciation and philosophical understanding of Mongolian oral lore.",
    coreConcepts: [
      "The Morin Khuur: legend of Khökhöö Namjil and the winged steed; acoustic mimicry of horse neighs, galloping, and wind.",
      "Khöömii (overtone throat singing): harmonic resonance producing two distinct vocal frequencies simultaneously, echoing the sounds of mountains, rivers, and breezes.",
      "Urtyn Duu (Long Song): ornamentation with intricate glissandos, falsetto flourishes, and prolonged breathing, evoking vast steppe horizons.",
      "Oral Epics (Тууль): multi-night performances by bards chanting thousands of alliterative poetic lines reciting the deeds of heroic warriors battling demonic forces (Мангас).",
      "Proverbial and Aphoristic Wisdom: embodying nomadic moral philosophy, environmental reciprocity, and kinship solidarity."
    ],
    taboosAndEtiquette: [
      "A Morin Khuur must never be left neglected, unplayed, or face down; it is regarded as the soul of the home.",
      "Oral epics must be recited only during cold seasons and with reverent ritual preparation (never lightly or during daytime)."
    ],
    historicalAndCosmologicalRoots: "The animistic belief that vocal music and acoustic vibrations commune directly with nature spirits (савдаг, лус) and cosmic forces.",
    linguisticIntegration: {
      targetVocabularyFields: ["морин хуур", "хөөмий", "уртын дуу", "шууранхай", "туульч", "зүйр цэцэн үг", "лус савдаг", "эрхэмсэг"],
      grammaticalCorrelates: ["Head-alliteration metrics (толгой холболт)", "Archaic optative and jussive endings (-сугай, -тугай)", "Metaphorical compression"],
      communicativeTasks: ["Interpret complex proverbs and their underlying nomadic life lessons", "Analyze the metric composition of an excerpt from the Jangar epic", "Deliver an elevated speech praising cultural heritage"]
    }
  }
];
