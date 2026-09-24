import { CEFRLevel } from '../../src/types/curriculum';

export interface SectionMeta {
  sectionId: string;
  sectionNumber: number;
  title: string;
  cyrillicTitle: string;
  cefr: CEFRLevel;
  theme: string;
  description: string;
  unitRange: [number, number]; // [startUnit, endUnit]
}

export const SECTIONS_META: SectionMeta[] = [
  {
    sectionId: 'sec_01',
    sectionNumber: 1,
    title: 'Phonology, Cyrillic Alphabet & Vowel Harmony',
    cyrillicTitle: 'Цагаан толгой, авиан зүй ба эгшиг зохицох ёс',
    cefr: 'A1',
    theme: 'Phonology & Writing',
    description: 'Master the 35 letters of Modern Mongolian Cyrillic, vowel categorization (masculine, feminine, neutral), and labial harmony.',
    unitRange: [1, 7]
  },
  {
    sectionId: 'sec_02',
    sectionNumber: 2,
    title: 'Greetings, Courtesies & Equative Sentences',
    cyrillicTitle: 'Мэндчилгээ, танилцах ёс ба энгийн өгүүлбэр',
    cefr: 'A1',
    theme: 'Greetings & Introduction',
    description: 'Polite forms of greeting, introducing oneself, asking names and origins, and zero-copula equative sentences.',
    unitRange: [8, 14]
  },
  {
    sectionId: 'sec_03',
    sectionNumber: 3,
    title: 'Family, Kinship & Dative-Locative Spatial Expressions',
    cyrillicTitle: 'Гэр бүл, төрөл садан ба өгөх оршихын тийн ялгал',
    cefr: 'A1',
    theme: 'Family & Space',
    description: 'Mongolian kinship terms, counting relatives, and indicating static location and destination with -д/-т.',
    unitRange: [15, 22]
  },
  {
    sectionId: 'sec_04',
    sectionNumber: 4,
    title: 'Food, Dairy Traditions & Accusative Direct Objects',
    cyrillicTitle: 'Хоол хүнс, цагаан идээ ба заахын тийн ялгал',
    cefr: 'A1',
    theme: 'Food & Cuisine',
    description: 'Nomadic dairy products (цагаан идээ), traditional meat dishes, ordering food, and marking definite direct objects with -ыг/-ийг/-г.',
    unitRange: [23, 30]
  },
  {
    sectionId: 'sec_05',
    sectionNumber: 5,
    title: 'Five Livestock, Pastoral Life & Ablative of Origin',
    cyrillicTitle: 'Таван хошуу мал, нүүдэлчин ахуй ба гарахын тийн ялгал',
    cefr: 'A2',
    theme: 'Pastoralism & Origin',
    description: 'The five sacred domestic animals, livestock age terminology, and origin, separation, or comparative standards with -аас/-ээс/-оос/-өөс.',
    unitRange: [31, 38]
  },
  {
    sectionId: 'sec_06',
    sectionNumber: 6,
    title: 'Steppe Geography, Nature & Instrumental Case of Means',
    cyrillicTitle: 'Байгаль, газар зүй ба үйлдэхийн тийн ялгал',
    cefr: 'A2',
    theme: 'Geography & Instruments',
    description: 'The four biomes of Mongolia (Gobi, Khangai, Steppe, Taiga), rivers, and performing actions by means of tools with -аар/-ээр/-оор/-өөр.',
    unitRange: [39, 46]
  },
  {
    sectionId: 'sec_07',
    sectionNumber: 7,
    title: 'Seasons, Weather & Reflexive-Possessive Architecture',
    cyrillicTitle: 'Улирал, цаг агаар ба өөртөө хамаатуулах нөхцөл',
    cefr: 'A2',
    theme: 'Seasons & Reflexives',
    description: 'Extreme seasonal transitions (зуд, цасан шуурга), seasonal encampments, and marking personal belongings with -аа/-ээ/-оо/-өө.',
    unitRange: [47, 54]
  },
  {
    sectionId: 'sec_08',
    sectionNumber: 8,
    title: 'Urban Life, Transport & Directional Case',
    cyrillicTitle: 'Хотжилт, тээврийн хэрэгсэл ба чиглэхийн тийн ялгал',
    cefr: 'A2',
    theme: 'City & Directions',
    description: 'Navigating Ulaanbaatar, public transit, city institutions, and expressing cardinal orientation towards targets with -руу/-рүү/-луу/-лүү.',
    unitRange: [55, 61]
  },
  {
    sectionId: 'sec_09',
    sectionNumber: 9,
    title: 'Daily Routines, Habits & Coordinating Converbs',
    cyrillicTitle: 'Өдөр тутмын хэвшил ба зэрэгцүүлэн холбох нөхцөл',
    cefr: 'B1',
    theme: 'Routines & Converbs',
    description: 'Habitual actions (-даг), progressive present (-ж байна), and chaining actions performed sequentially by the same subject with -ж/-ч and -аад.',
    unitRange: [62, 69]
  },
  {
    sectionId: 'sec_10',
    sectionNumber: 10,
    title: 'Seasonal Migrations & Conditional Clause Structures',
    cyrillicTitle: 'Нүүдэл суудал ба нөхцөлт холбох нөхцөл',
    cefr: 'B1',
    theme: 'Migration & Conditions',
    description: 'Pastoral seasonal migration (нүүдэл, отор), pasture conservation, and constructing hypothetical and temporal conditions with -вал/-вэл/-бал/-бэл.',
    unitRange: [70, 77]
  },
  {
    sectionId: 'sec_11',
    sectionNumber: 11,
    title: 'Naadam Games, Steppe Folklore & Concessive Clauses',
    cyrillicTitle: 'Эрийн гурван наадам, аман зохиол ба харшлах холбох нөхцөл',
    cefr: 'B1',
    theme: 'Naadam & Concessives',
    description: 'Wrestling, horse racing, archery, heroic epics, folk riddles, and articulating contrasts with -вч and боловч.',
    unitRange: [78, 84]
  },
  {
    sectionId: 'sec_12',
    sectionNumber: 12,
    title: 'Causative & Passive Voices in Society, History & Law',
    cyrillicTitle: 'Үйлдэх ба үйлдэгдэх хэв: Түүх, нийгэм, хууль',
    cefr: 'B2',
    theme: 'Causative, Passive & Society',
    description: 'The Mongol Empire, Chinggis Khaan, governance, and transforming syntactic agency with causative (-уул) and passive (-гд) morphemes.',
    unitRange: [85, 92]
  },
  {
    sectionId: 'sec_13',
    sectionNumber: 13,
    title: 'Complex Converb Chaining & Discourse Hierarchy',
    cyrillicTitle: 'Нийлмэл өгүүлбэр, нөхцөлт үйлийн тогтолцоо',
    cefr: 'B2',
    theme: 'Complex Syntax & Chaining',
    description: 'Forming periodic paragraphs with multiple subordinate converbs (-хаар, -магц, -тал, -саар) culminating on a single finite matrix verb.',
    unitRange: [93, 100]
  },
  {
    sectionId: 'sec_14',
    sectionNumber: 14,
    title: 'Economy, Mining, Technology & Ecology',
    cyrillicTitle: 'Эдийн засаг, уул уурхай, экологи ба технологи',
    cefr: 'B2',
    theme: 'Economy & Ecology',
    description: 'Mongolia\'s mineral wealth, renewable energy transition, desertification countermeasures, and academic discourse markers.',
    unitRange: [101, 107]
  },
  {
    sectionId: 'sec_15',
    sectionNumber: 15,
    title: 'Honorific Registers, Statehood, Philosophy & Poetry',
    cyrillicTitle: 'Хүндэтгэлийн найруулга, төрт ёс ба гүн ухаан',
    cefr: 'C1',
    theme: 'Honorifics & Steppe Philosophy',
    description: 'Ceremonial address, lexical honorifics, Buddhist-Shamanic cosmology, constitutional governance, and classical rhetorical eloquence.',
    unitRange: [108, 114]
  },
  {
    sectionId: 'sec_16',
    sectionNumber: 16,
    title: 'Master Steppe Literature, Secret History & Classical Nuances',
    cyrillicTitle: 'Монголын нууц товчоо, туульс ба дээд найруулга',
    cefr: 'C2',
    theme: 'Classical Masterworks',
    description: 'Close critical reading of the Secret History of the Mongols, heroic epics (Jangar, Geser), head-alliteration poetics, and archaic grammar registers.',
    unitRange: [115, 120]
  }
];

export interface UnitBlueprint {
  unitNumber: number;
  sectionNumber: number;
  title: string;
  cyrillicTitle: string;
  cefr: CEFRLevel;
  primaryGrammarTopic: string;
  description: string;
  lessonCount: number; // typically 5 to 6
}

// Generate the 120 Units deterministically across the 16 sections
export function generateAllUnitBlueprints(): UnitBlueprint[] {
  const units: UnitBlueprint[] = [];

  const UNIT_THEMES: { title: string; cyrillic: string; grammar: string; desc: string }[] = [
    // Units 1 - 7 (Section 1: Alphabet & Phonology)
    { title: 'The Seven Short Vowels & Lip Rounding', cyrillic: 'Долоон үндсэн эгшиг ба уруулын зохицол', grammar: 'Basic Vowels & Lip Harmony', desc: 'Identify а, э, и, о, у, ө, ү and their fundamental acoustic properties.' },
    { title: 'Masculine vs. Feminine Vowel Classification', cyrillic: 'Эр, эм эгшгийн ангилал', grammar: 'Vowel Harmony Dichotomy', desc: 'Classify words into back-harmonic masculine and front-harmonic feminine classes.' },
    { title: 'Neutral Vowel "И" and Mixed Syllabics', cyrillic: 'Саармаг эгшиг "И" ба холимог үе', grammar: 'Neutral Vowel Rules', desc: 'How neutral vowel И interacts with masculine and feminine stems.' },
    { title: 'Long Vowels & Orthographic Doubling', cyrillic: 'Урт эгшиг ба давхар үсэг', grammar: 'Vowel Length & Stress', desc: 'Long vowels formed by doubling letters (аа, ээ, оо, уу, өө, үү).' },
    { title: 'Diphthongs: Four Rising & Falling Glides', cyrillic: 'Хос эгшиг: ай, эй, ой, уй, үй', grammar: 'Mongolian Diphthongs', desc: 'Pronunciation and orthographic rules of diphthongal vowel clusters.' },
    { title: 'Voiced & Voiceless Consonants', cyrillic: 'Хонины долоо, ямааны есөн гийгүүлэгч', grammar: 'Consonant Classes', desc: 'Mnemonic groups of consonants governing suffix assimilations.' },
    { title: 'The Soft Sign (Ь) and Hard Sign (Ъ)', cyrillic: 'Зөөлний ба хатуугийн тэмдгийн дүрэм', grammar: 'Signs & Palatalization', desc: 'Palatalization with ь and separating non-palatal vowels with ъ.' },

    // Units 8 - 14 (Section 2: Greetings & Basic Syntax)
    { title: 'Formal Morning & Daily Greetings', cyrillic: 'Өглөөний ба өдрийн албан мэндчилгээ', grammar: 'Formal Greeting Formulas', desc: 'Polite greeting customs used in everyday encounters and administrative contexts.' },
    { title: 'Informal Salutations & Inquiring about Well-Being', cyrillic: 'Энгийн мэндчилгээ ба амар мэндийг асуух', grammar: 'Interrogative Particles (уу/үү)', desc: 'Asking yes-no questions with yes-no harmonic question particles.' },
    { title: 'Equative Identity Sentences with Zero Copula', cyrillic: 'Би монгол хүн: Нөхцөлгүй холбоос', grammar: 'Zero Copula Nominal Equatives', desc: 'Constructing subject-predicate noun equatives without a copular verb.' },
    { title: 'Focus Particle "бол" and Contrastive Topic', cyrillic: 'Сул үг "бол" ба сэдэв тодотгох', grammar: 'Topic Marker "бол"', desc: 'Using бол to highlight the sentence topic or introduce contrast.' },
    { title: 'Negation in Nominal Sentences: "биш"', cyrillic: 'Үгүйсгэх үг "биш"', grammar: 'Equative Negation "биш"', desc: 'Negating predicate nouns and equative statements with биш.' },
    { title: 'Demonstrative Pronouns (Энэ, Тэр, Эдгээр, Тэдгээр)', cyrillic: 'Заах төлөөний нэрс', grammar: 'Demonstrative System', desc: 'Spatial proximal (энэ) and distal (тэр) demonstrative determiners.' },
    { title: 'Section 1 & 2 Synthesis and Oral Review', cyrillic: '1 ба 2-р хэсгийн бататгал шалгалт', grammar: 'Spiral Cumulative Review', desc: 'Review of Cyrillic orthography, vowel harmony, and introductory dialogue.' },

    // Units 15 - 22 (Section 3: Family & Dative-Locative)
    { title: 'Immediate Kinship: Parents and Siblings', cyrillic: 'Гэр бүлийн ойрын гишүүд', grammar: 'Kinship Terminology', desc: 'Mongolian distinction between older/younger siblings (ах, эгч, дүү).' },
    { title: 'Grandparents and Extended Maternal/Paternal Lineages', cyrillic: 'Өвөө эмээ ба авга, нагацын төрөл', grammar: 'Bifurcate Kinship Hierarchy', desc: 'Lineage terminology distinguishing paternal (авга) and maternal (нагац) relations.' },
    { title: 'Dative-Locative of Static Location (-д / -т)', cyrillic: 'Орших байршил заах нь (-д/-т)', grammar: 'Dative-Locative: Location', desc: 'Denoting being inside a place, city, or room with -д and -т.' },
    { title: 'Dative-Locative of Recipient & Indirect Object', cyrillic: 'Үйлийн эзэнд чиглэх нь (-д/-т)', grammar: 'Dative-Locative: Indirect Object', desc: 'Expressing giving or conveying information to a person.' },
    { title: 'Temporal Dative: Hours, Days and Years', cyrillic: 'Цаг хугацаа заах нь (-д/-т)', grammar: 'Dative-Locative: Temporal Time', desc: 'Specifying when events happen on the clock and calendar.' },
    { title: 'Mongolian Cardinal Numbers 1 to 100', cyrillic: 'Тооны нэрс: 1-ээс 100 хүртэл', grammar: 'Numeral Syntax & Counting', desc: 'Forming numerals and using them as pre-nominal modifiers without plural markers.' },
    { title: 'Expressing Age with the Comitative (-тай)', cyrillic: 'Нас заах хамтрахын тийн ялгал', grammar: 'Age Predicates with -тай', desc: 'Inquiring and declaring age using -тай/-тэй/-той.' },
    { title: 'Section 3 Synthesis: Describing Families & Homes', cyrillic: 'Гэр бүл, орон гэрээ тайлбарлах нь', grammar: 'Spiral Integrative Application', desc: 'Constructing multi-sentence biographies of family households.' },

    // Units 23 - 30 (Section 4: Food & Accusative)
    { title: 'Nomadic Dairy Delicacies (Цагаан идээ)', cyrillic: 'Цагаан идээний соёл ба нэршил', grammar: 'Mass Nouns & Partitive Uses', desc: 'Traditional dairy: ааруул, өрөм, бяслаг, тараг, айраг.' },
    { title: 'Steamed & Fried Meat Fare (Бууз, Хуушуур, Цай)', cyrillic: 'Монгол махан хоол ба зоог', grammar: 'Direct Object Nouns', desc: 'Dining lexicon and customary etiquette at Mongolian meals.' },
    { title: 'Definite Direct Objects with Accusative (-ыг/-ийг/-г)', cyrillic: 'Заахын тийн ялгал: Тодорхой тусах хэрэглээ', grammar: 'Definite Accusative Marking', desc: 'Marking definite and specific objects vs unmarked indefinite direct objects.' },
    { title: 'Accusative Pronouns (Намайг, Чамайг, Түүнийг)', cyrillic: 'Төлөөний үгсийн заахын тийн ялгал', grammar: 'Irregular Pronoun Declensions', desc: 'Special accusative stems of personal pronouns.' },
    { title: 'Ordering in Restaurants & Tea Houses', cyrillic: 'Цайны газарт захиалга өгөх нь', grammar: 'Volitive / Imperative Request -я', desc: 'Polite requests using voluntative suffix -я/-е/-ё.' },
    { title: 'Adjectives of Taste, Temperature and Freshness', cyrillic: 'Хоолны амт, халуун хүйтнийг илэрхийлэх', grammar: 'Descriptive Predicate Adjectives', desc: 'Amttai, haluun, huiten, chiherleg, gashuun.' },
    { title: 'Hospitality Customs & Offering Food (Зочлох ёс)', cyrillic: 'Монгол зочломтгой ёс ба дээж өргөх', grammar: 'Honorific Food Vocabulary', desc: 'Offering the upper portion (дээж) and holding cups with both hands.' },
    { title: 'Section 4 Synthesis: Traditional Feast Simulation', cyrillic: 'Цагаан сарын идээ ундааны яриа', grammar: 'Cumulative Dialogue Integration', desc: 'Comprehensive practice ordering and describing traditional meals.' }
  ];

  // Fill out up to 120 units with systematic pedagogical topics across remaining sections
  let currentUnit = 1;
  for (const sec of SECTIONS_META) {
    const [start, end] = sec.unitRange;
    const count = end - start + 1;
    for (let u = start; u <= end; u++) {
      const existingTheme = UNIT_THEMES[u - 1];
      const title = existingTheme ? existingTheme.title : `${sec.theme}: Advanced Competency Unit ${u}`;
      const cyrillic = existingTheme ? existingTheme.cyrillic : `${sec.cyrillicTitle} - Хичээл ${u}`;
      const grammar = existingTheme ? existingTheme.grammar : `${sec.theme} Structural Principle ${u}`;
      const desc = existingTheme ? existingTheme.desc : `Comprehensive academic study of ${sec.theme.toLowerCase()} in standard Mongolian.`;
      
      // Calculate lesson count to achieve exactly 700 lessons across 120 units
      // 120 units: 100 units with 6 lessons, 20 units with 5 lessons = 600 + 100 = 700 lessons!
      const lessonCount = u <= 100 ? 6 : 5;

      units.push({
        unitNumber: u,
        sectionNumber: sec.sectionNumber,
        title,
        cyrillicTitle: cyrillic,
        cefr: sec.cefr,
        primaryGrammarTopic: grammar,
        description: desc,
        lessonCount
      });
    }
  }

  return units;
}
