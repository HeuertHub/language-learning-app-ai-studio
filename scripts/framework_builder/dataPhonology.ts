export interface PhonologyConcept {
  conceptId: string;
  title: string;
  mongolianTerminology: string;
  category: "Alphabet & Orthography" | "Vowel System" | "Vowel Harmony" | "Consonants & Palatalization" | "Prosody & Intonation";
  firstTargetLevel: string;
  prerequisites: string[];
  unlocks: string[];
  verificationStatus: "VERIFIED" | "NEEDS REVISION" | "UNCERTAIN / SOURCE REVIEW REQUIRED";
  pedagogicalLabel: string;
  linguisticAnalysis: string;
  learnerExplanation: string;
  technicalNotes: string;
  orthographicRules: string[];
  phoneticNotation: string;
}

export const phonologyInventoryData: PhonologyConcept[] = [
  {
    conceptId: "phono_cyr_35_alphabet",
    title: "Mongolian Cyrillic Alphabet Inventory (35 Letters)",
    mongolianTerminology: "Монгол кирилл цагаан толгой",
    category: "Alphabet & Orthography",
    firstTargetLevel: "Pre-A1",
    prerequisites: [],
    unlocks: ["phono_vowel_short_seven", "phono_consonant_basic_inventory", "phono_mongolian_specific_letters"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The 35-Letter Alphabet (Цагаан толгой)",
    linguisticAnalysis: "Graphemic system adapted from Russian Cyrillic in 1941 by Ts. Damdinsüren, comprising 35 glyphs representing 29 native phonemes plus 4 loan consonants (К, П, Ф, Щ) and 2 orthographic signs (Ъ, Ь).",
    learnerExplanation: "Mongolian uses the Cyrillic alphabet with 35 letters. While many look like Russian, two letters (Ө and Ү) are unique to Mongolian, and several letters make distinct sounds.",
    technicalNotes: "Standard alphabetical order: А Б В Г Д Е Ё Ж З И Й К Л М Н О Ө П Р С Т У Ү Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я. Cyrillic false friends with Latin must be drilled immediately (e.g. В = [w/v], Н = [n/ŋ], Р = [r], Х = [x]).",
    orthographicRules: [
      "Standard alphabetical collation sequence must be strictly maintained for dictionary navigation.",
      "Distinguish uppercase and lowercase glyphs, paying particular attention to handwritten vs printed forms."
    ],
    phoneticNotation: "35 graphemic units mapping to native Khalkha vowel and consonant phonemes."
  },
  {
    conceptId: "phono_mongolian_specific_letters",
    title: "Mongolian-Specific Letters: Ө ө and Ү ү",
    mongolianTerminology: "Монгол хэлний өвөрмөц үсэг Ө, Ү",
    category: "Alphabet & Orthography",
    firstTargetLevel: "Pre-A1",
    prerequisites: ["phono_cyr_35_alphabet"],
    unlocks: ["phono_vowel_front_back_distinction"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Special Mongolian Letters: Ө and Ү",
    linguisticAnalysis: "Ө ө represents the open-mid front/central rounded vowel [o/ɵ] ([+ATR]); Ү ү represents the close front/central rounded vowel [u/ʉ] ([+ATR]). They contrast systematically with back/retracted О [ɔ] ([-ATR]) and У [ʊ] ([-ATR]).",
    learnerExplanation: "Ө looks like an O with a horizontal bar inside; Ү looks like a Y or straight-stemmed V. They represent 'front' rounded vowels that sound softer and higher than regular О and У.",
    technicalNotes: "These two letters were specifically added to the standard Cyrillic character set for Mongolian. A frequent orthographic error among digital learners is substituting Russian letter equivalents or failing to observe the barred glyph.",
    orthographicRules: [
      "Ө ө is written with a horizontal crossbar centered in the oval, distinguishing it from unbarred О о.",
      "Ү ү has a straight central descending stem topped by a symmetrical V-shape, distinguishing it from slanted-stem У у."
    ],
    phoneticNotation: "Ө = [o] / [ɵ]; Ү = [u] / [ʉ]. Contrast pairs: О = [ɔ]; У = [ʊ]."
  },
  {
    conceptId: "phono_vowel_short_seven",
    title: "The Seven Basic Short Vowels",
    mongolianTerminology: "Үндсэн долоон богино эгшиг",
    category: "Vowel System",
    firstTargetLevel: "Pre-A1",
    prerequisites: ["phono_cyr_35_alphabet"],
    unlocks: ["phono_vowel_long_pairs", "phono_vowel_front_back_distinction"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "7 Short Vowels: А, Э, И, О, У, Ө, Ү",
    linguisticAnalysis: "The primary vocalic inventory of Khalkha Mongolian consists of seven phonemic short vowels partitioned along tongue root retraction (ATR) and labial rounding dimensions: /a, e, i, ɔ, ʊ, o, u/.",
    learnerExplanation: "Mongolian has 7 basic vowels. Pronouncing them accurately is vital because changing a vowel changes the meaning of the word completely.",
    technicalNotes: "Phonetically, in non-initial syllables, short vowels undergo centralization and reduction to [ə], but orthography preserves the etymological harmonic vowel grapheme.",
    orthographicRules: [
      "Every native syllable must contain at least one vocalic nucleus.",
      "In non-initial syllables, short vowels are written with the harmonic letter even when acoustically reduced to [ə]."
    ],
    phoneticNotation: "А [a], Э [e], И [i], О [ɔ], У [ʊ], Ө [o], Ү [u]."
  },
  {
    conceptId: "phono_vowel_long_pairs",
    title: "Long Vowels and Phonemic Vowel Length",
    mongolianTerminology: "Урт эгшиг ба авианы урт богинын ялгаа",
    category: "Vowel System",
    firstTargetLevel: "Pre-A1",
    prerequisites: ["phono_vowel_short_seven"],
    unlocks: ["phono_vowel_diphthongs", "phono_vowel_harmony_masc_fem"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Long Vowels (Double Letters: АА, ЭЭ, ОО, УУ, ӨӨ, ҮҮ, ИЙ)",
    linguisticAnalysis: "Vowel length is strictly phonemic in Mongolian, contrasting in duration by a ratio of approximately 2:1. Long vowels carry full phonetic quality and do not reduce in non-initial syllables.",
    learnerExplanation: "When you see two vowel letters together, hold the sound for twice as long. Holding a vowel longer changes the word: 'шар' means yellow, but 'шаар' means balloon; 'хол' means far, but 'хоол' means food.",
    technicalNotes: "Long vowels are written as geminate double letters (аа, ээ, оо, уу, өө, үү). The long counterpart of И in final syllables or stems is written as ИЙ.",
    orthographicRules: [
      "Long vowels are written with doubled identical graphemes: аа, ээ, оо, уу, өө, үү.",
      "The long high unrounded vowel in word-final or stem-final positions is written with ИЙ (e.g. дэлхий, бичиг->бичгийн)."
    ],
    phoneticNotation: "[aː, eː, ɔː, ʊː, oː, uː, iː]. Phonemic duration contrast ~2:1."
  },
  {
    conceptId: "phono_vowel_diphthongs",
    title: "Diphthongs and Glide Combinations",
    mongolianTerminology: "Хос эгшиг (ай, эй, ой, уй, үй)",
    category: "Vowel System",
    firstTargetLevel: "Pre-A1",
    prerequisites: ["phono_vowel_long_pairs"],
    unlocks: ["phono_vowel_harmony_masc_fem"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Diphthongs (Vowel + Й)",
    linguisticAnalysis: "The native diphthongs are falling diphthongs ending in a palatal offglide [i̯]: ай [ai̯], ой [ɔi̯], уй [ʊi̯], үй [ui̯]. The combination эй [ei̯] occurs predominantly in foreign loanwords, interjections, or expressive roots.",
    learnerExplanation: "Diphthongs are two vowel sounds blended into one syllable ending with a 'y' sound: ай (like 'eye'), ой (like 'oy'), уй (like 'oo-y'), үй (like 'front-u + y').",
    technicalNotes: "In phonotactic weight calculations, diphthongs count as bimoraic heavy syllables equivalent to long vowels. They determine suffix harmony based on the initial vowel nucleus.",
    orthographicRules: [
      "Diphthongs are written with the short vowel grapheme followed by short I (Й): а+й, э+й, о+й, у+й, ү+й.",
      "In suffixation, stems ending in diphthongs select suffix allomorphs based on the harmonic class of the primary vowel."
    ],
    phoneticNotation: "[ai̯, ei̯, ɔi̯, ʊi̯, ui̯]."
  },
  {
    conceptId: "phono_vowel_front_back_distinction",
    title: "Vowel Harmonic Classification: Masculine, Feminine, and Neutral",
    mongolianTerminology: "Эгшгийн ангилал: Эр, эм, саармаг эгшиг",
    category: "Vowel Harmony",
    firstTargetLevel: "A1",
    prerequisites: ["phono_mongolian_specific_letters", "phono_vowel_short_seven"],
    unlocks: ["phono_vowel_harmony_masc_fem"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Vowel Classes: Masculine (Эр), Feminine (Эм), Neutral (Саармаг)",
    linguisticAnalysis: "Traditional Mongolian pedagogy labels retracted tongue root ([-ATR]) vowels as 'masculine' (эр эгшиг: А, О, У) and advanced tongue root ([+ATR]) vowels as 'feminine' (эм эгшиг: Э, Ө, Ү). The vowel И is phonologically neutral / transparent.",
    learnerExplanation: "Mongolian divides vowels into two contrasting families: 'Hard/Deep' (Masculine: А, О, У) and 'Soft/Light' (Feminine: Э, Ө, Ү). The letter И is neutral and can sit in either family.",
    technicalNotes: "Linguistic reality vs terminology: While traditional grammar calls them back (эр) and front (эм), modern acoustic and phonological analysis demonstrates that the core articulatory contrast is Advanced Tongue Root (ATR) / pharyngeal expansion.",
    orthographicRules: [
      "Masculine vowels: А, О, У (including their long forms аа, оо, уу and diphthongs ай, ой, уй).",
      "Feminine vowels: Э, Ө, Ү (including long forms ээ, өө, үү and diphthongs эй, үй).",
      "Neutral vowel: И (and ий)."
    ],
    phoneticNotation: "[-ATR] / Retracted: {a, ɔ, ʊ}; [+ATR] / Advanced: {e, o, u}; Neutral: {i}."
  },
  {
    conceptId: "phono_vowel_harmony_masc_fem",
    title: "Stem Vowel Harmony: The Golden Constraint",
    mongolianTerminology: "Үгийн үндсийн эгшиг зохицох ёс",
    category: "Vowel Harmony",
    firstTargetLevel: "A1",
    prerequisites: ["phono_vowel_front_back_distinction"],
    unlocks: ["phono_suffix_vowel_selection_fourfold", "phono_rounding_harmony_labial"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Vowel Harmony: Masculine vs Feminine Words",
    linguisticAnalysis: "Root harmony constraint: In native Mongolian lexical roots, [-ATR] (masculine) vowels and [+ATR] (feminine) vowels cannot co-occur. A word must belong entirely to the masculine harmonic set or feminine set.",
    learnerExplanation: "Words in Mongolian never mix masculine vowels (А, О, У) with feminine vowels (Э, Ө, Ү). Once a word starts masculine, every suffix added to it must also be masculine.",
    technicalNotes: "Compound words (e.g. хөдөө аж ахуй) and recent foreign loans (e.g. кино, ресторан) violate root harmony across morphemes. In such cases, the suffix harmonizes with the final syllable.",
    orthographicRules: [
      "A root containing А, О, or У is a masculine word (эр үг) and requires masculine suffixes.",
      "A root containing Э, Ө, or Ү is a feminine word (эм үг) and requires feminine suffixes.",
      "Compound words take suffixes agreeing with the final stem element."
    ],
    phoneticNotation: "Harmonic domain spans the prosodic word: *[+ATR]...[-ATR] is ungrammatical in native roots."
  },
  {
    conceptId: "phono_neutral_vowel_behavior",
    title: "The Neutral Vowel И in Harmony and Suffixation",
    mongolianTerminology: "Саармаг эгшиг И-ийн онцлог үүрэг",
    category: "Vowel Harmony",
    firstTargetLevel: "A1",
    prerequisites: ["phono_vowel_harmony_masc_fem"],
    unlocks: ["phono_suffix_vowel_selection_fourfold"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The Behavior of Neutral 'И'",
    linguisticAnalysis: "The high unrounded vowel /i/ behaves neutrally in root phonotactics. When an initial syllable contains a masculine vowel, subsequent /i/ does not disrupt masculine harmony. If a root contains only /i/, it selects feminine suffixes by default.",
    learnerExplanation: "If a word has both a masculine vowel and И (like 'багш' or 'ажил'), the masculine vowel wins: you use masculine endings (багшаар). But if a word contains ONLY the letter И (like 'бичиг' or 'гэрчилгээ'), it takes feminine endings (бичгээр).",
    technicalNotes: "Historically, Classical Mongolian had two distinct vowels: *i (front) and *ï (back). They merged phonetically into [i] in modern Khalkha, leaving behind the 'neutral' harmonic behavior.",
    orthographicRules: [
      "Pure-И stems (containing no vowels other than И/ИЙ) govern feminine suffix agreement (e.g. бичиг -> бичгээр).",
      "Mixed stems (Masculine + И) govern masculine suffix agreement (e.g. багш -> багшаар, ажил -> ажлаар)."
    ],
    phoneticNotation: "[i] transparent to progressive ATR harmony from preceding syllables."
  },
  {
    conceptId: "phono_rounding_harmony_labial",
    title: "Labial / Rounding Harmony (О and Ө Harmony)",
    mongolianTerminology: "Уруул зохицох ёс (О, Ө-ийн зохицол)",
    category: "Vowel Harmony",
    firstTargetLevel: "A1",
    prerequisites: ["phono_vowel_harmony_masc_fem"],
    unlocks: ["phono_suffix_vowel_selection_fourfold"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Rounding Harmony: The 'О' and 'Ө' Rules",
    linguisticAnalysis: "Progressive labial harmony constraint: Stem-initial non-high rounded vowels /ɔ/ (О) and /o/ (Ө) trigger obligatory rounding of non-high suffix vowels to [ɔ] (-оор, -сон) and [o] (-өөр, -сөн). Crucially, high rounded vowels /ʊ/ (У) and /u/ (Ү) DO NOT trigger rounding on non-high vowels.",
    learnerExplanation: "If a word's main vowel is О, endings with 'a' change to 'o' (хотод, хотоос). If it is Ө, endings change to 'ө' (өдөрт, өдрөөс). But if the vowel is high У or Ү, endings stay 'a' or 'e' (уулаар, not *уулоор; хүүгээр, not *хүүгөөр).",
    technicalNotes: "This is a classic phonological distinction: rounding harmony operates strictly within identical vowel height ([+low] / [-high]). High rounded vowels do not spread [+round] to non-high suffix targets.",
    orthographicRules: [
      "After stem О: suffix variant with О is selected for non-high vowels (e.g. -оор, -сон, -дог).",
      "After stem Ө: suffix variant with Ө is selected for non-high vowels (e.g. -өөр, -сөн, -дөг).",
      "Stems with У or Ү select unrounded suffixes: -аар (not *-оор) and -ээр (not *-өөр)."
    ],
    phoneticNotation: "[+round, -high] spreads progressively to following [-high] vocalic nuclei."
  },
  {
    conceptId: "phono_suffix_vowel_selection_fourfold",
    title: "Suffix Vowel Selection: Fourfold and Twofold Alternations",
    mongolianTerminology: "Дагавар, нөхцөлийн эгшиг сонгох дүрэм (дөрвөн ба хоёр хувилбарт нөхцөл)",
    category: "Vowel Harmony",
    firstTargetLevel: "A1",
    prerequisites: ["phono_neutral_vowel_behavior", "phono_rounding_harmony_labial"],
    unlocks: ["phono_iotated_vowels_behavior", "phono_soft_and_hard_signs"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Suffix Harmony: 4-Variant and 2-Variant Endings",
    linguisticAnalysis: "Morphophonemic alternation algorithms: Non-high suffixes possess four allomorphs {-а, -э, -о, -ө}; high suffixes possess two allomorphs {-у, -ү}; invariant/irregular suffixes maintain fixed vocalism (e.g. -тай/-тэй/-той, -ын/-ийн).",
    learnerExplanation: "Most suffixes come in 4 versions: -аар, -ээр, -оор, -өөр. Choose the version that matches your word's vowel: А/У word -> -аар; Э/Ү word -> -ээр; О word -> -оор; Ө word -> -өөр.",
    technicalNotes: "Fourfold suffix selection table: Stems with А/У/АЙ/УЙ take -а; Stems with Э/Ү/ЭЙ/ҮЙ take -э; Stems with О/ОЙ take -о; Stems with Ө take -ө. Twofold suffixes (e.g. -ууд/-үүд) select -у for masculine and -ү for feminine.",
    orthographicRules: [
      "Rule of 4 variants: Stem in А/У -> -а; Stem in Э/Ү -> -э; Stem in О -> -о; Stem in Ө -> -ө.",
      "Rule of 2 variants: Masculine stem -> -у; Feminine stem -> -ү.",
      "Invariant suffixes: Comitative has 3 variants (-тай, -тэй, -той); Genitive uses phonetic coda rules."
    ],
    phoneticNotation: "Archiphonemic realization: /A4/ -> [a, e, ɔ, o]; /U2/ -> [ʊ, u]."
  },
  {
    conceptId: "phono_iotated_vowels_behavior",
    title: "Iotated Vowels: Я, Е, Ё, Ю and Palatalization Marking",
    mongolianTerminology: "Еэ үсэг (Я, Е, Ё, Ю) ба зөөлрүүлэх үүрэг",
    category: "Alphabet & Orthography",
    firstTargetLevel: "A1",
    prerequisites: ["phono_suffix_vowel_selection_fourfold"],
    unlocks: ["phono_soft_and_hard_signs", "phono_consonant_palatalization"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Iotated Vowels: Я, Е, Ё, Ю",
    linguisticAnalysis: "The four iotated Cyrillic graphemes encode either an onset glide /j/ + vowel in word-initial position, or a palatalized consonant /Cʲ/ + vowel in post-consonantal position. Я = [ja/ʲa] (masculine); Е = [je/ʲe] (feminine); Ё = [jɔ/ʲɔ] (strictly masculine); Ю = [jʊ/ʲʊ] (masculine) or [ju/ʲu] (feminine).",
    learnerExplanation: "These letters make a 'y' sound before a vowel (like ya, ye, yo, yu). When they come after a consonant, they soften that consonant. Remember: Ё is always masculine in native Mongolian words.",
    technicalNotes: "Critical linguistic fact: In Russian, Ё is a front-soft vowel, but in Mongolian Cyrillic, Ё represents [jɔ] and is strictly a masculine vowel that takes masculine suffixes (e.g. ёс -> ёсоор, NOT *ёсоор).",
    orthographicRules: [
      "Я and Ё are masculine iotated vowels; Е is feminine; Ю represents masculine [jʊ] or feminine [ju].",
      "Post-consonantally, they indicate palatalization of the preceding consonant without requiring a soft sign (Ь)."
    ],
    phoneticNotation: "Word-initial: [ja, je, jɔ, jʊ, ju]. Post-consonantal: [Cʲa, Cʲe, Cʲɔ, Cʲʊ, Cʲu]."
  },
  {
    conceptId: "phono_soft_and_hard_signs",
    title: "Orthographic Signs: Soft Sign (Ь) and Hard Sign (Ъ)",
    mongolianTerminology: "Хатуу ба зөөлний тэмдэг (Ъ, Ь)-ийн дүрэм",
    category: "Alphabet & Orthography",
    firstTargetLevel: "A1",
    prerequisites: ["phono_iotated_vowels_behavior"],
    unlocks: ["phono_consonant_palatalization", "phono_fleeting_vowels_deletion"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The Signs: Soft Sign (Ь) and Hard Sign (Ъ)",
    linguisticAnalysis: "Orthographic diacritics: Soft sign (Ь) denotes coda consonant palatalization [Cʲ]. Before vocalic suffixes, Ь alternates with the full neutral vowel И. Hard sign (Ъ) functions exclusively as a hiatus/separation marker preventing palatalization before iotated vowels in masculine stems.",
    learnerExplanation: "Ь softens the consonant before it (like in 'морь' horse). When you add an ending, Ь turns into an И (морь -> мориор). Ъ is used in masculine words to separate a consonant from a 'y' sound without softening it (явъя).",
    technicalNotes: "Ь -> И alternation rule: When a suffix beginning with a vowel is added to a stem ending in Ь, the Ь changes to И (e.g. барь + аад = бариад; морь + ын = морины). Ъ only occurs before Я, Ё, Ю in masculine words.",
    orthographicRules: [
      "Soft sign (Ь): marks consonant palatalization at word or syllable end (e.g. тань, хонь, сурь).",
      "Before vocalic suffixes, Ь regularly transforms into И (барь -> бариарай).",
      "Hard sign (Ъ): separates non-palatalized consonants from iotated vowels in masculine words (явъя, олгъё)."
    ],
    phoneticNotation: "Ь = [ʲ] coda palatalization / morphophonemic /i/ alternant; Ъ = [C.jV] boundary."
  },
  {
    conceptId: "phono_consonant_basic_inventory",
    title: "Consonant Inventory and Articulation Points",
    mongolianTerminology: "Монгол хэлний гийгүүлэгч авианы тогтолцоо",
    category: "Consonants & Palatalization",
    firstTargetLevel: "Pre-A1",
    prerequisites: ["phono_cyr_35_alphabet"],
    unlocks: ["phono_consonant_palatalization", "phono_consonant_clusters_syllables"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The Consonant Sounds of Mongolian",
    linguisticAnalysis: "Modern Khalkha consonant system comprises stops /p, pʰ, t, tʰ, k, kʰ/, affricates /t͡s, t͡sʰ, t͡ʃ, t͡ʃʰ/, fricatives /s, ʃ, x, w, j/, nasals /m, n, ŋ/, and liquids /l, ɮ, r/. The stop series contrasts in aspiration rather than European-style true voicing.",
    learnerExplanation: "Mongolian consonants differ in aspiration (puff of air). Letter Л is pronounced with air hissing past the sides of the tongue [ɮ]. Letter В between vowels sounds like a soft 'w' or 'v'.",
    technicalNotes: "Cyrillic Б, Д, Г represent unaspirated, lenis voiceless stops [p, t, k/ɡ], while П, Т, К represent aspirated, fortis stops [pʰ, tʰ, kʰ]. Letter Л in Khalkha is a voiced lateral fricative [ɮ].",
    orthographicRules: [
      "К, П, Ф, Щ occur only in foreign loanwords in standard Cyrillic orthography.",
      "The velar nasal [ŋ] is written as Н in coda position (e.g. байшин [pai̯ʃiŋ], монгол [mɔŋɡɔɮ])."
    ],
    phoneticNotation: "Stops/Affricates: /p, pʰ, t, tʰ, t͡s, t͡sʰ, t͡ʃ, t͡ʃʰ, k, kʰ/; Fricatives: /s, ʃ, x, ɮ/; Nasals: /m, n, ŋ/; Liquids: /r/."
  },
  {
    conceptId: "phono_consonant_palatalization",
    title: "Consonant Palatalization Contrast (Зөөлөрсөн гийгүүлэгч)",
    mongolianTerminology: "Зөөлөрсөн гийгүүлэгчийн дуудлага ба бичлэг",
    category: "Consonants & Palatalization",
    firstTargetLevel: "A1",
    prerequisites: ["phono_consonant_basic_inventory", "phono_soft_and_hard_signs", "phono_iotated_vowels_behavior"],
    unlocks: ["phono_consonant_alternations_assimilation"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Soft (Palatalized) Consonants",
    linguisticAnalysis: "Phonemic palatalization contrast: Plain consonants /t, d, n, l, m, s, x/ systematically contrast with their palatalized counterparts /tʲ, dʲ, nʲ, lʲ, mʲ, sʲ, xʲ/. Palatalization involves raising the tongue dorsum toward the hard palate.",
    learnerExplanation: "Palatalized consonants sound like they have a subtle 'y' blended into them. It changes word meanings: 'тана' means mother-of-pearl, but 'тань' means know/recognize; 'хоно' means stay overnight, but 'хоньо' means sheep.",
    technicalNotes: "Minimal pairs: тана [tana] vs тань [tanʲ]; сар [sar] 'moon' vs сарь [sarʲ] 'membrane'; хор [xɔr] 'poison' vs хорь [xɔrʲ] 'twenty'.",
    orthographicRules: [
      "Word-final palatalization is indicated by the soft sign Ь (e.g. хонь, морь, тань).",
      "Intervocalic palatalization is represented by iotated vowels or the letter И (e.g. барья, моринд)."
    ],
    phoneticNotation: "/C/ vs /Cʲ/ phonemic secondary articulation contrast."
  },
  {
    conceptId: "phono_consonant_clusters_syllables",
    title: "Syllable Structure and Consonant Clusters",
    mongolianTerminology: "Үеийн бүтэц ба гийгүүлэгчийн бөөгнөрөл",
    category: "Consonants & Palatalization",
    firstTargetLevel: "A2",
    prerequisites: ["phono_consonant_basic_inventory"],
    unlocks: ["phono_epenthesis_consonant_contact"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Syllable Structure and End-of-Word Clusters",
    linguisticAnalysis: "Khalkha syllable template allows complex consonant codas: (C)V(V)(C)(C)(C). Word-initial consonant clusters are strictly prohibited in native vocabulary, but complex clusters occur freely in syllable codas (e.g. эрсдэл [erstəl]).",
    learnerExplanation: "Native Mongolian words never start with two consonants together. But at the end of words, Mongolian easily stacks 2 or 3 consonants (like 'эрсдэл' or 'ажиллагсдад').",
    technicalNotes: "When foreign loanwords with initial clusters enter Mongolian (e.g. спорт, трамвай, стакан), native speakers traditionally insert a prothetic or epenthetic vowel in speech ([is.pɔrt], [is.ta.kan]).",
    orthographicRules: [
      "Native Mongolian words cannot begin with a consonant cluster.",
      "Complex clusters in coda positions are permitted without intervening vowels provided sonority constraints are respected."
    ],
    phoneticNotation: "Maximal syllable template: (C₁)V(V)(C₂)(C₃)(C₄)."
  },
  {
    conceptId: "phono_epenthesis_consonant_contact",
    title: "Syllable Contact, Epenthesis, and Consonant Classes",
    mongolianTerminology: "Эгшиг жийрэглэх ёс: Эгшигт долоо ба заримдаг ес",
    category: "Consonants & Palatalization",
    firstTargetLevel: "A2",
    prerequisites: ["phono_consonant_clusters_syllables"],
    unlocks: ["phono_fleeting_vowels_deletion"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The Epenthetic Vowel Rule (Эгшиг жийрэглэх дүрэм)",
    linguisticAnalysis: "Linguistic fact-check and correction of the 'ДОЛЖОО' confusion: The authoritative orthographic rule classifies native consonants into 7 Sonorants (эгшигт 7: М, Н, Г, Л, Б, В, Р) and 9 Obstruents (заримдаг 9: Д, Ж, З, С, Т, Х, Ц, Ч, Ш). Syllable contact constraint: An obstruent (заримдаг) cannot immediately follow another obstruent without an intervening epenthetic short vowel (e.g. бод + с = бодос; compare sonorant ав + т = авт).",
    learnerExplanation: "When attaching suffixes, two 'hard' consonants (Д, Ж, З, С, Т, Х, Ц, Ч, Ш) cannot collide directly: you must insert a linking vowel between them. But a 'soft/flowing' consonant (М, Н, Г, Л, Б, В, Р) can touch another consonant directly.",
    technicalNotes: "Popular pedagogical mnemonics sometimes garble this into names like 'Должоо', but the actual linguistic distinction is strictly between Sonorant consonants (capable of voicing/sonority maintenance in clusters) and Obstruent consonants (which require epenthesis to prevent illegal stop-fricative clusters).",
    orthographicRules: [
      "7 Sonorant consonants (Эгшигт 7): М, Н, Г, Л, Б, В, Р.",
      "9 Obstruent consonants (Заримдаг 9): Д, Ж, З, С, Т, Х, Ц, Ч, Ш.",
      "Rule: If an obstruent suffix follows an obstruent stem coda, an epenthetic vowel must be inserted (e.g. бод + х = бодох)."
    ],
    phoneticNotation: "C[-son] + C[-son] -> C[-son] + [ə] + C[-son] morphophonemic epenthesis."
  },
  {
    conceptId: "phono_fleeting_vowels_deletion",
    title: "Fleeting Vowels and Syncope (Балархай эгшиг гээгдэх хууль)",
    mongolianTerminology: "Балархай эгшиг гээгдэх хууль",
    category: "Alphabet & Orthography",
    firstTargetLevel: "A2",
    prerequisites: ["phono_epenthesis_consonant_contact", "phono_suffix_vowel_selection_fourfold"],
    unlocks: ["phono_consonant_alternations_assimilation"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Dropped Vowels (Балархай эгшиг гээгдэх)",
    linguisticAnalysis: "Unstressed vowel syncope in open non-initial syllables: In a disyllabic or multisyllabic root with a short vowel in the second syllable, that vowel drops in spelling and pronunciation when a vowel-initial suffix is added, provided the deletion does not create an illegal consonant cluster (e.g. ажил + ыг = ажлыг; нөхөр + ийн = нөхрийн; өдөр + өөр = өдрөөр).",
    learnerExplanation: "In two-syllable words with a short vowel in the second syllable, adding an ending that starts with a vowel makes that middle vowel disappear: ажил -> ажлыг; өдөр -> өдрөөр.",
    technicalNotes: "Blocked deletion conditions: The vowel is retained if dropping it would cause two obstruents to cluster illegally, or if the preceding syllable contains a geminate or cluster that would result in a forbidden CCC cluster (e.g. хоног + т = хоногт).",
    orthographicRules: [
      "The short vowel of the second syllable drops before vowel-initial suffixes: CVCVC + VC -> CVCC-VC.",
      "The vowel does not drop if its loss would produce an unpronounceable or illegal cluster."
    ],
    phoneticNotation: "Syncope rule: V[-stress, -long] -> Ø / VC __ C + V."
  },
  {
    conceptId: "phono_consonant_alternations_assimilation",
    title: "Consonant Assimilation and Morpheme Boundaries",
    mongolianTerminology: "Гийгүүлэгч авиа нийлэх, хувирах ёс",
    category: "Consonants & Palatalization",
    firstTargetLevel: "A2",
    prerequisites: ["phono_fleeting_vowels_deletion", "phono_consonant_palatalization"],
    unlocks: ["phono_secret_n_consonant_alternation"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Consonant Blending and Sound Shifts",
    linguisticAnalysis: "Phonetic assimilation at morpheme junctions: Regressive place assimilation (alveolar /n/ before bilabial /p, b/ surfaces as [m], e.g. минж [mind͡ʒ]); dental stop voicing/devoicing assimilation (/d/ + /t/ -> [tt]); and intervocalic spirantization of /b/ to [w] or [β].",
    learnerExplanation: "When certain consonants touch in speech, they blend: 'н' before 'б' sounds like 'm'; two 'д' and 'т' sounds merge into a crisp double 't'. Orthography usually keeps the base spelling.",
    technicalNotes: "Mongolian Cyrillic spelling is largely etymological and morphophonemic rather than purely phonetic; students must learn where spoken phonetics diverge from written letters.",
    orthographicRules: [
      "Etymological spelling is maintained despite phonetic regressive assimilation (e.g. бидэнтэй is pronounced [pitəntteː]).",
      "Stems ending in Г before certain suffixes may exhibit alternation or epenthesis."
    ],
    phoneticNotation: "/n/ -> [m] / __ [p, b]; /d/ + /t/ -> [tː]; /b/ -> [w] / V __ V."
  },
  {
    conceptId: "phono_secret_n_consonant_alternation",
    title: "The Unstable / Secret 'N' (Нууц 'Н'-ийн дүрэм)",
    mongolianTerminology: "Нууц Н үсгийн хувирал, дүрэм",
    category: "Alphabet & Orthography",
    firstTargetLevel: "A2",
    prerequisites: ["phono_consonant_alternations_assimilation"],
    unlocks: [],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "The Hidden / Secret 'N' (Нууц Н)",
    linguisticAnalysis: "Historical stem-final nasal alternation: Stems historically ending in *-n lose the nasal in the citation nominative form, but re-activate the underlying /n/ when taking certain case suffixes (Genitive -ны/-ний, Dative -нд/-нт, and various derivational affixes).",
    learnerExplanation: "Some words have a 'hidden N' that hides in the plain word but pops out when you add endings: 'мод' (tree) becomes 'модны' (of the tree) and 'модонд' (in the tree); 'нар' (sun) becomes 'нарны'.",
    technicalNotes: "Nouns possessing unstable 'N' include: мод (модны), нар (нарны), сар (сарны), төмөр (төмрийн/төмөрний), үнэг (үнэгний). Learners must memorize these as lexical stem properties.",
    orthographicRules: [
      "Citation nominative is written without -н (мод, нар, төмөр).",
      "Takes genitive -ны/-ний instead of standard -ын/-ийн.",
      "Takes dative -нд/-нт instead of standard -д/-т."
    ],
    phoneticNotation: "Underlying morphophoneme /...n/ surfacing in non-nominative environments."
  },
  {
    conceptId: "phono_prosody_stress_prominence",
    title: "Word Stress and Acoustic Prominence in Khalkha",
    mongolianTerminology: "Үгийн өргөлт, хэмнэлийн онцлог",
    category: "Prosody & Intonation",
    firstTargetLevel: "A1",
    prerequisites: ["phono_vowel_long_pairs"],
    unlocks: ["phono_prosody_sentence_intonation"],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Where Stress and Beat Fall in Words",
    linguisticAnalysis: "Prosodic prominence in Khalkha: Default dynamic stress falls on the initial root syllable. However, if the word contains a non-initial long vowel or diphthong (bimoraic heavy syllable), acoustic pitch and duration peak shifts to the first heavy syllable.",
    learnerExplanation: "In Mongolian, regular short words are stressed on the first syllable. But if a word has a long vowel (double letter) later in the word, that long vowel naturally gets the emphasis and duration.",
    technicalNotes: "Stress in Mongolian does not trigger dramatic vowel reduction of the English or Russian type; short vowels in unstressed non-initial syllables are reduced to [ə], but long vowels NEVER reduce, maintaining full duration regardless of position.",
    orthographicRules: [
      "Stress is not marked with diacritics in standard Mongolian Cyrillic orthography.",
      "Never reduce the duration of double-vowel letters even if an initial syllable has dynamic stress."
    ],
    phoneticNotation: "Default: [ˈσ...]. Weight-sensitive shift: [σ...ˈσː...]."
  },
  {
    conceptId: "phono_prosody_sentence_intonation",
    title: "Sentence Intonation Patterns: Statements, Questions, and Converbs",
    mongolianTerminology: "Өгүүлбэрийн аялга, дуудлагын хэмнэл",
    category: "Prosody & Intonation",
    firstTargetLevel: "A2",
    prerequisites: ["phono_prosody_stress_prominence"],
    unlocks: [],
    verificationStatus: "VERIFIED",
    pedagogicalLabel: "Sentence Intonation and Melody",
    linguisticAnalysis: "Intonational contours: Neutral declarative sentences exhibit terminal falling pitch (L%). Yes/no polar questions with interrogative particle уу/үү display a rising-falling contour peaking on the particle. Content questions with interrogative pronouns exhibit high initial pitch with falling terminal contour. Converb clauses feature a non-terminal continuation rise (H-).",
    learnerExplanation: "Statements drop in pitch at the end. Yes/no questions ending in 'уу/үү' rise and then gently drop on the question word. When speaking a long sentence connected with converbs, your voice stays slightly raised until the final verb.",
    technicalNotes: "Distinguish polar questions (уу/үү: terminal particle pitch peak) from content wh-questions (юу, хэн, хаана: pitch peak on the question word itself, with particle бэ/вэ carrying low falling pitch).",
    orthographicRules: [
      "Interrogative sentences terminate with question marks (?).",
      "Complex converb clauses in written prose are separated by commas when structurally extensive."
    ],
    phoneticNotation: "Declarative: L%; Polar Question (уу/үү): H-L%; Wh-Question: M-L%; Dependent Converb: H-."
  }
];
