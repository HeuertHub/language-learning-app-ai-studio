import { RawGrammarConcept } from './types';

export function getFullGrammarDataset(): RawGrammarConcept[] {
  const concepts: RawGrammarConcept[] = [
    // -------------------------------------------------------------------------
    // A1 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_a1_01',
      title: 'Vowel Harmony Basics (Эгшиг зохицох ёс)',
      cyrillicTitle: 'Эгшиг зохицох ёс: Эр, эм, саармаг эгшиг',
      cefr: 'A1',
      summary: 'Mongolian vowels are divided into masculine (а, о, у), feminine (э, ө, ү), and neutral (и, й). Suffixes must agree with root vowels.',
      formationRules: [
        'Masculine root (contains а, о, у) -> Takes masculine suffixes (-аар, -аас, -тай, -даг, etc.)',
        'Feminine root (contains э, ө, ү) -> Takes feminine suffixes (-ээр, -өөс, -тэй, -дэг, etc.)',
        'Neutral vowel (и) harmonizes with feminine suffixes if alone, or defers to existing masculine/feminine vowels.'
      ],
      commonMistakes: [
        'Attaching a feminine suffix like -тэй to a masculine root like аав (*аавтэй is invalid, correct is аавтай).',
        'Confusing round vowels: roots with о take -оор/-оос, roots with ө take -өөр/-өөс (labial harmony).'
      ],
      examples: [
        { cyrillic: 'аав + тай = аавтай', english: 'with father (masculine)' },
        { cyrillic: 'ээж + тэй = ээжтэй', english: 'with mother (feminine)' },
        { cyrillic: 'гэр + т = гэрт', english: 'at home / in the ger (feminine)' },
        { cyrillic: 'хот + оос = хотоос', english: 'from the city (masculine labial)' }
      ]
    },
    {
      id: 'g_a1_02',
      title: 'Nominative & Zero Copula Equative Sentences',
      cyrillicTitle: 'Нэрлэхийн тийн ялгал ба нөхцөлгүй холбоос',
      cefr: 'A1',
      summary: 'In present affirmative equative sentences ("X is Y"), no verb "to be" is required. The particle "бол" or "нь" or direct juxtaposing is used.',
      formationRules: [
        'Subject + Object / Predicate Noun (e.g. Би оюутан = I am a student)',
        'Subject + бол + Predicate Noun (emphasis / topic: Энэ бол ном = This is a book)',
        'Subject + нь + Predicate Noun (declarative focus: Тэр нь эмч = He is a doctor)'
      ],
      commonMistakes: [
        'Trying to insert a literal verb like англи "is" in basic equative sentences.',
        'Omitting negative биш in negation: "Би оюутан биш" (I am not a student).'
      ],
      examples: [
        { cyrillic: 'Би монгол хүн.', english: 'I am a Mongolian.' },
        { cyrillic: 'Энэ бол сургууль.', english: 'This is a school.' },
        { cyrillic: 'Энэ миний ном биш.', english: 'This is not my book.' }
      ]
    },
    {
      id: 'g_a1_03',
      title: 'Genitive Case (Харьяалахын тийн ялгал: -ын, -ийн, -ний, -нийх)',
      cyrillicTitle: 'Харьяалахын тийн ялгал',
      cefr: 'A1',
      summary: 'Expresses possession, origin, or association ("of / \'s"). Formed with -ын/-ийн/-ний/-ны depending on terminal phonemes.',
      formationRules: [
        'Consonant stems (masculine): + ын (e.g. адуу -> адууны, ном -> номын)',
        'Consonant stems (feminine): + ийн (e.g. гэр -> гэрийн, эгч -> эгчийн)',
        'Stems ending in long vowels or diphthongs: + н / -ны / -ний',
        'Stems ending in short vowels: usually drop final short vowel + ын/ийн'
      ],
      commonMistakes: [
        'Using -ын with feminine words (*гэрын is incorrect, use гэрийн).',
        'Confusing reflexive possessive -аа with genitive -ын.'
      ],
      examples: [
        { cyrillic: 'Монголын түүх', english: 'History of Mongolia' },
        { cyrillic: 'багшийн ном', english: 'teacher\'s book' },
        { cyrillic: 'миний аав', english: 'my father' }
      ]
    },
    {
      id: 'g_a1_04',
      title: 'Dative-Locative Case (Өгөх оршихын тийн ялгал: -д, -т)',
      cyrillicTitle: 'Өгөх оршихын тийн ялгал',
      cefr: 'A1',
      summary: 'Indicates the indirect object ("to"), static location ("in, at, on"), or time of occurrence ("at, on, in").',
      formationRules: [
        'Words ending in vowels, semi-vowels, or resonant consonants (м, н, л, б, в): + д (e.g. сургуульд, гэрт)',
        'Words ending in voiceless obstruents (г, р, с, д, т, ц, ч, х): + т (e.g. гэрт, хотод)'
      ],
      commonMistakes: [
        'Using accusative instead of dative-locative for static location (*Би хотыг байна is incorrect; use Би хотод байна).',
        'Misapplying -д after -р (*гэрд is wrong; correct is гэрт).'
      ],
      examples: [
        { cyrillic: 'Би Улаанбаатарт амьдардаг.', english: 'I live in Ulaanbaatar.' },
        { cyrillic: 'Дүүдээ ном өгөв.', english: 'Gave a book to younger sibling.' },
        { cyrillic: 'Таван цагт уулзъя.', english: 'Let\'s meet at five o\'clock.' }
      ]
    },
    {
      id: 'g_a1_05',
      title: 'Accusative Case (Заахын тийн ялгал: -ыг, -ийг, -г)',
      cyrillicTitle: 'Заахын тийн ялгал',
      cefr: 'A1',
      summary: 'Marks the definite direct object of a transitive verb. Indefinite direct objects may appear in the unmarked (zero) form.',
      formationRules: [
        'Vowel ending: + г (e.g. аав -> аавыг, ээж -> ээжийг, нохой -> нохойг)',
        'Consonant ending (masculine): + ыг (e.g. ном -> номыг, мал -> малыг)',
        'Consonant ending (feminine): + ийг (e.g. сүү -> сүүг, цэцэг -> цэцгийг)'
      ],
      commonMistakes: [
        'Adding accusative to indefinite general objects (*Би алим идмээр байна vs Би энэ алимыг идмээр байна).',
        'Vowel harmony violations (*гэрыг is wrong, correct is гэрийг).'
      ],
      examples: [
        { cyrillic: 'Би энэ номыг уншсан.', english: 'I read this specific book.' },
        { cyrillic: 'Ээжийгээ дуудав.', english: 'Called one\'s mother.' },
        { cyrillic: 'Та ус уух уу?', english: 'Will you drink water? (indefinite - zero case)' }
      ]
    },
    {
      id: 'g_a1_06',
      title: 'Ablative Case (Гарахын тийн ялгал: -аас, -ээс, -оос, -өөс)',
      cyrillicTitle: 'Гарахын тийн ялгал',
      cefr: 'A1',
      summary: 'Signifies point of departure ("from"), origin, material, cause, or the standard in comparative constructions ("than").',
      formationRules: [
        'Masculine unrounded: + аас (e.g. ааваас, сургуулиас)',
        'Feminine unrounded: + ээс (e.g. гэрээс, ээжээс)',
        'Masculine rounded (о): + оос (e.g. хотоос, олноос)',
        'Feminine rounded (ө): + өөс (e.g. өдрөөс, өвөөс)'
      ],
      commonMistakes: [
        'Ignoring labial harmony: writing *хотоос as *хотаас.',
        'Confusing comparative standard case: Mongolian uses Ablative for "than" (e.g. Ааваас өндөр = taller than father).'
      ],
      examples: [
        { cyrillic: 'Би хөдөөнөөс ирсэн.', english: 'I came from the countryside.' },
        { cyrillic: 'Модноос алим унав.', english: 'An apple fell from the tree.' },
        { cyrillic: 'Энэ ном тэр номоос сонирхолтой.', english: 'This book is more interesting than that book.' }
      ]
    },
    {
      id: 'g_a1_07',
      title: 'Instrumental Case (Үйлдэхийн тийн ялгал: -аар, -ээр, -оор, -өөр)',
      cyrillicTitle: 'Үйлдэхийн тийн ялгал',
      cefr: 'A1',
      summary: 'Indicates instrument, means, path, or mode of action ("by, through, with, in"). Four-way vowel harmony applies.',
      formationRules: [
        'Masculine non-labial: + аар (e.g. харандаагаар, номоор)',
        'Feminine non-labial: + ээр (e.g. үзэгээр, гэрээр)',
        'Masculine labial (o): + оор (e.g. олоор, хоолоор)',
        'Feminine labial (ө): + өөр (e.g. нүдээр, өдрөөр)'
      ],
      commonMistakes: [
        'Confusing Instrumental (-аар means / by way of) with Comitative (-тай accompanied by).',
        'Omitting buffer consonant -г- when stem ends in long vowel or diphthong (e.g. автобус + аар = автобусаар; but морь + оор = мориор).'
      ],
      examples: [
        { cyrillic: 'Би автобусаар явдаг.', english: 'I go by bus.' },
        { cyrillic: 'Монгол хэлээр ярьдаг.', english: 'Speaks in the Mongolian language.' },
        { cyrillic: 'Халбагаар хоол иддэг.', english: 'Eats meal with a spoon.' }
      ]
    },
    {
      id: 'g_a1_08',
      title: 'Comitative Case (Хамтрахын тийн ялгал: -тай, -тэй, -той)',
      cyrillicTitle: 'Хамтрахын тийн ялгал',
      cefr: 'A1',
      summary: 'Signifies accompaniment ("with, together with"), possession ("having X"), or age ("years old").',
      formationRules: [
        'Masculine root: + тай (e.g. аавтай, адуутай)',
        'Feminine root: + тэй (e.g. ээжтэй, эгчтэй)',
        'Masculine rounded root: + той (e.g. охинтой, морьтой)'
      ],
      commonMistakes: [
        'Using Instrumental -аар when accompanying a person (*Би ахынхаа хүчээр явав instead of ахтайгаа).',
        'Missing -тай for possessing: "Би машинтай" = "I have a car".'
      ],
      examples: [
        { cyrillic: 'Би найзтайгаа хамт сурч байна.', english: 'I am studying together with my friend.' },
        { cyrillic: 'Тэр гучин настай.', english: 'He is thirty years old.' },
        { cyrillic: 'Би машинтай, байшинтай.', english: 'I have a car and a house.' }
      ]
    },
    {
      id: 'g_a1_09',
      title: 'Present-Habitual Aspect (-даг, -дэг, -дог, -дөг)',
      cyrillicTitle: 'Үйл үгийн дадал зуршил заах цаг',
      cefr: 'A1',
      summary: 'Expresses habitual, repeated, or timeless general actions ("always does, usually does"). Subject to 4-way vowel harmony.',
      formationRules: [
        'Verb Stem + -даг (masculine non-labial: уншдаг, хардаг)',
        'Verb Stem + -дэг (feminine non-labial: үздэг, мэддэг)',
        'Verb Stem + -дог (masculine labial: ордог, боддог)',
        'Verb Stem + -дөг (feminine labial: өгдөг, өмсдөг)'
      ],
      commonMistakes: [
        'Confusing progressive -ж байна (right now) with habitual -даг (regularly).',
        'Adding personal pronoun endings directly to -даг in modern standard Khalkha.'
      ],
      examples: [
        { cyrillic: 'Би өглөө бүр сүүтэй цай уудаг.', english: 'I drink milk tea every morning.' },
        { cyrillic: 'Тэр их сургуульд багшилдаг.', english: 'She teaches at the university.' },
        { cyrillic: 'Та хаана ажилладаг вэ?', english: 'Where do you work?' }
      ]
    },
    {
      id: 'g_a1_10',
      title: 'Present Continuous Progressive (-ж / -ч байна)',
      cyrillicTitle: 'Одоо үргэлжилж буй цаг',
      cefr: 'A1',
      summary: 'Expresses an action currently unfolding at the precise moment of speech. Formed by imperfective converb -ж/-ч + auxiliary байна.',
      formationRules: [
        'Verb stem ending in vowel or voiced consonant (в, г, д, ж, з, л, м, н): + ж байна (e.g. хийж байна, уншиж байна)',
        'Verb stem ending in voiceless consonant (с, х, ц, ч, т): + ч байна (e.g. бичиж байна, сууж байна, нисч байна)'
      ],
      commonMistakes: [
        'Mixing -ж and -ч (*уншич байна is incorrect, should be уншиж байна).',
        'Using -ж байна for habitual actions (*Би өдөр бүр цай ууж байна instead of уудаг).'
      ],
      examples: [
        { cyrillic: 'Би одоо хичээлээ хийж байна.', english: 'I am doing my homework right now.' },
        { cyrillic: 'Бороо орж байна.', english: 'It is raining.' },
        { cyrillic: 'Та юу уншиж байна вэ?', english: 'What are you reading?' }
      ]
    },

    // -------------------------------------------------------------------------
    // A2 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_a2_01',
      title: 'Reflexive-Possessive Suffixes (-аа, -ээ, -оо, -өө)',
      cyrillicTitle: 'Өөртөө хамаатуулах нөхцөл',
      cefr: 'A2',
      summary: 'Replaces 3rd person and 1st/2nd person possessives when the possessor is the subject of the same clause ("one\'s own").',
      formationRules: [
        'Noun stem + Case suffix (if applicable) + -аа/-ээ/-оо/-өө (or -ндаа/-ндээ after vowel stems)',
        'Examples: Ном -> номоо (reads one\'s own book); Аав -> аавдаа (to one\'s own father)'
      ],
      commonMistakes: [
        'Using 3rd person genitive түүний when referring to the subject\'s own possession (*Тэр түүний номыг уншив instead of номоо).',
        'Violating vowel harmony across four variants (-аа, -ээ, -оо, -өө).'
      ],
      examples: [
        { cyrillic: 'Би гэр рүүгээ явж байна.', english: 'I am going towards my own home.' },
        { cyrillic: 'Тэр дүүдээ тусалсан.', english: 'He helped his own younger sibling.' },
        { cyrillic: 'Малчин малдаа явлаа.', english: 'The herder went to his own livestock.' }
      ]
    },
    {
      id: 'g_a2_02',
      title: 'Directional Case (Чиглэхийн тийн ялгал: -руу, -рүү / -луу, -лүү)',
      cyrillicTitle: 'Чиглэхийн тийн ялгал',
      cefr: 'A2',
      summary: 'Specifies movement towards a general direction or target destination ("towards, in the direction of").',
      formationRules: [
        'Words not ending in -р: + руу (masculine), + рүү (feminine)',
        'Words ending in -р: + луу (masculine), + лүү (feminine) to prevent double "r" clash (e.g. гэр -> гэр лүү)'
      ],
      commonMistakes: [
        'Writing *гэр рүү instead of dissimilated гэр лүү.',
        'Confusing with Dative-Locative -д/-т which denotes arriving AT the point, whereas -руу emphasizes motion TOWARDS.'
      ],
      examples: [
        { cyrillic: 'Би хот руу явна.', english: 'I will go towards the city.' },
        { cyrillic: 'Бид гэр лүүгээ харилаа.', english: 'We returned towards our home.' },
        { cyrillic: 'Уул өөд, гол руу алхлаа.', english: 'Walked up the mountain, towards the river.' }
      ]
    },
    {
      id: 'g_a2_03',
      title: 'Past Tense Participle (-сан, -сэн, -сон, -сөн)',
      cyrillicTitle: 'Өнгөрсөн цагийн нөхцөл (-сан)',
      cefr: 'A2',
      summary: 'Expresses completed action in the past, or acts as a past attributive participle ("having done"). 4-way harmony.',
      formationRules: [
        'Verb Stem + -сан (masculine non-labial: явсан, харсан)',
        'Verb Stem + -сэн (feminine non-labial: ирсэн, үзсэн)',
        'Verb Stem + -сон (masculine labial: орсон, бодсон)',
        'Verb Stem + -сөн (feminine labial: өгсөн, төрсөн)'
      ],
      commonMistakes: [
        'Confusing -сан (reported/neutral past) with -лаа (witnessed immediate past).',
        'Negating with биш vs үгүй: as predicate it takes үгүй (e.g. Би яваагүй).'
      ],
      examples: [
        { cyrillic: 'Би өчигдөр номын санд очсон.', english: 'I went to the library yesterday.' },
        { cyrillic: 'Тэр дөнгөж сая ирсэн.', english: 'He has just arrived.' },
        { cyrillic: 'Би энэ киног үзээгүй.', english: 'I haven\'t seen this movie.' }
      ]
    },
    {
      id: 'g_a2_04',
      title: 'Future / Deductive Participle (-х / -на, -нэ, -но, -нө)',
      cyrillicTitle: 'Ирээдүй цагийн төгсгөх ба холбох нөхцөл',
      cefr: 'A2',
      summary: 'Expresses impending action, intent, or deductive prediction in the non-past. -х forms the infinitive/participle; -на concludes.',
      formationRules: [
        'Finite indicative: Stem + -на/-нэ/-но/-нө (e.g. явна, ирнэ, орно, өгнө)',
        'Participial / Infinitive: Stem + -х (e.g. явах, ирэх, орох, өгөх)'
      ],
      commonMistakes: [
        'Using -на for habitual continuous states instead of -даг.',
        'Dropping the epenthetic vowel before -на (e.g. үз + нэ = үзнэ, but унш + на = уншина).'
      ],
      examples: [
        { cyrillic: 'Би маргааш хөдөө явна.', english: 'I will go to the countryside tomorrow.' },
        { cyrillic: 'Монгол хэл сурах амархан биш.', english: 'Learning the Mongolian language is not easy.' },
        { cyrillic: 'Цас орох байх.', english: 'It will probably snow.' }
      ]
    },
    {
      id: 'g_a2_05',
      title: 'Coordinating Imperfective Converb (-ж / -ч)',
      cyrillicTitle: 'Нийлмэл өгүүлбэрийн холбох нөхцөл (-ж / -ч)',
      cefr: 'A2',
      summary: 'Connects actions occurring sequentially in rapid succession or simultaneously by the same subject.',
      formationRules: [
        'Stem + -ж (after voiced stems: сууж, харж, ирж)',
        'Stem + -ч (after voiceless stems: очиж, бичиж, гарч)'
      ],
      commonMistakes: [
        'Using coordinating converb when subjects are different (requires conditional -вал or temporal converbs).',
        'Putting terminal punctuation immediately after a converb clause.'
      ],
      examples: [
        { cyrillic: 'Би цай ууж, талх идэв.', english: 'I drank tea and ate bread.' },
        { cyrillic: 'Тэр босож, хаалга онгойлгов.', english: 'He stood up and opened the door.' },
        { cyrillic: 'Хүүхдүүд дуулж, бүжиглэж байна.', english: 'The children are singing and dancing.' }
      ]
    },

    // -------------------------------------------------------------------------
    // B1 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_b1_01',
      title: 'Conditional Converb (-бал, -бэл, -бол, -бөл / -вал, -вэл, -вол, -вөл)',
      cyrillicTitle: 'Нөхцөлт холбох нөхцөл (-бал, -вал)',
      cefr: 'B1',
      summary: 'Expresses "if / when" conditions. Distinguishes consonant vs vowel stems with -бал/-вал.',
      formationRules: [
        'Consonant stems: + бал / бэл / бол / бөл (e.g. сурвал, үзвэл)',
        'Vowel stems and stems ending in r/l/v: + вал / вэл / вол / вөл (e.g. очвол, суувал)'
      ],
      commonMistakes: [
        'Confusing hypothetical conditional (-вал) with concessive (-вч "although").',
        'Violating 4-way harmony in the suffix vowel.'
      ],
      examples: [
        { cyrillic: 'Цаг гарвал би очно.', english: 'If time permits, I will come.' },
        { cyrillic: 'Хичээлээ сайн хийвэл шалгалтаа давна.', english: 'If you study diligently, you will pass your exam.' },
        { cyrillic: 'Бороо орвол гэртээ үлдэнэ.', english: 'If it rains, we will stay at home.' }
      ]
    },
    {
      id: 'g_b1_02',
      title: 'Concessive Converb (-вч / боловч)',
      cyrillicTitle: 'Найруулах найруулгын харшлах холбох нөхцөл',
      cefr: 'B1',
      summary: 'Signifies "although, even though, despite the fact that".',
      formationRules: [
        'Verb Stem + -вч (e.g. ядавч, суувч, үзэвч)',
        'Participle (-сан/-х) + боловч (e.g. хийсэн боловч, явах боловч)'
      ],
      commonMistakes: [
        'Using concessive where causal учир нь is required.',
        'Forgetting that the subject can change across clauses with -вч.'
      ],
      examples: [
        { cyrillic: 'Хүйтэн байвч бид гадаа ажилласан.', english: 'Although it was cold, we worked outside.' },
        { cyrillic: 'Олон удаа уншсан боловч сайн ойлгосонгүй.', english: 'Even though I read it many times, I did not understand well.' }
      ]
    },
    {
      id: 'g_b1_03',
      title: 'Causative Voice (-уул, -үүл, -лга, -лгэ, -га, -гэ)',
      cyrillicTitle: 'Үйлдэх хэв (Бусдаар үйлдүүлэх хэв)',
      cefr: 'B1',
      summary: 'Indicates that the subject causes another agent to perform the action ("make someone do, have something done").',
      formationRules: [
        'Consonant stems: + уул / үүл (e.g. унш -> уншуулах, хий -> хийлгэх)',
        'Vowel stems: + лга / лгэ / лго / лгө (e.g. суу -> суулгах, үз -> үзүүлэх)'
      ],
      commonMistakes: [
        'Marking the caused agent with wrong case: the caused agent of an intransitive verb is in the Accusative (-ыг), but of a transitive verb is in the Dative-Locative (-д).'
      ],
      examples: [
        { cyrillic: 'Багш оюутнуудаар дасгал хийлгэв.', english: 'The teacher had the students do the exercise.' },
        { cyrillic: 'Ээж хүүхдээ унтуулав.', english: 'The mother put the child to sleep.' }
      ]
    },
    {
      id: 'g_b1_04',
      title: 'Passive Voice (-гд, -д, -т)',
      cyrillicTitle: 'Үйлдэгдэх хэв',
      cefr: 'B1',
      summary: 'The grammatical subject undergoes the action. The logical agent is marked with the Dative-Locative (-д) or Ablative (-аас).',
      formationRules: [
        'Vowel and consonant stems generally take -гд- (e.g. сонс -> сонсогдох, барь -> баригдах, бич -> бичигдэх)'
      ],
      commonMistakes: [
        'Marking the agent with accusative rather than dative-locative (*Багшийг магтагдав is wrong; Багшид магтагдав).',
        'Overusing passive where Mongolian naturally prefers active voice.'
      ],
      examples: [
        { cyrillic: 'Шинэ сургууль хотод баригдав.', english: 'A new school was built in the city.' },
        { cyrillic: 'Тэр хүн олонд хүндлэгддэг.', english: 'That person is respected by the public.' }
      ]
    },

    // -------------------------------------------------------------------------
    // B2 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_b2_01',
      title: 'Complex Converb Chaining & Discourse Hierarchy',
      cyrillicTitle: 'Нийлмэл өгүүлбэр дэх нөхцөлт үйлийн дараалал',
      cefr: 'B2',
      summary: 'Mongolian constructs lengthy periodic sentences by stringing non-finite converbal clauses that terminate on a single finite main verb.',
      formationRules: [
        'Subordinate clause 1 (Converb) + Subordinate clause 2 (Converb) + Main finite clause (Verb + finite ending)',
        'Temporal sequence: -аад -> Logical condition: -вал -> Purpose: -хаар -> Main verb.'
      ],
      commonMistakes: [
        'Inserting premature finite verbs (*уншив, тэгээд явав) inside a single complex syntactic period.',
        'Losing subject tracking when chaining switches between same-subject (-ж, -аад) and different-subject (-хад, -вал) converbs.'
      ],
      examples: [
        { cyrillic: 'Өглөө босоод, цайгаа чанаж уугаад, ажилдаа гарлаа.', english: 'Having gotten up in the morning, brewed and drank tea, he departed for work.' },
        { cyrillic: 'Нар мандахад шувууд жиргэж эхлэв.', english: 'When the sun rose, the birds began to chirp.' }
      ]
    },
    {
      id: 'g_b2_02',
      title: 'Purposive Converb (-хаар, -хээр, -хоор, -хөөр)',
      cyrillicTitle: 'Зорилго заах холбох нөхцөл (-хаар)',
      cefr: 'B2',
      summary: 'Denotes the specific purpose or intent of an action ("in order to, with the purpose of").',
      formationRules: [
        'Future participle in -х + Instrumental case -аар/-ээр/-оор/-өөр',
        'e.g. сур + хаар = сурахаар (in order to learn); үз + хээр = үзэхээр (in order to see)'
      ],
      commonMistakes: [
        'Confusing with -х гэж (quotative intent) or -х тулд (formal purpose clause). -хаар is the standard spoken and written converb.'
      ],
      examples: [
        { cyrillic: 'Би ном авахаар дэлгүүр орсон.', english: 'I went to the store in order to buy a book.' },
        { cyrillic: 'Тэр монгол хэл сурахаар Улаанбаатарт иржээ.', english: 'He came to Ulaanbaatar to study Mongolian.' }
      ]
    },
    {
      id: 'g_b2_03',
      title: 'Modal Particles of Epistemic Stance (юм, байна, биз, дээ, шүү)',
      cyrillicTitle: 'Төгсгөх сул үг ба хандлага заах ай',
      cefr: 'B2',
      summary: 'Terminal modal particles calibrate certainty, evidentiary source, subjective conviction, and politeness.',
      formationRules: [
        'юм: objective factual assertion / explanatory state',
        'байна: immediate empirical observation or discovery',
        'биз / биз ээ: probable conjecture ("surely, probably")',
        'дээ: softening, resignation, or cordial affirmation',
        'шүү: emphatic reminder / gentle warning ("mind you, indeed!")'
      ],
      commonMistakes: [
        'Confusing the copular/factual particle юм with the noun юм ("thing").',
        'Overusing emphatic шүү in formal academic registers.'
      ],
      examples: [
        { cyrillic: 'Энэ бол маш чухал асуудал юм.', english: 'This is indeed a very important issue.' },
        { cyrillic: 'Маргааш цаг агаар дулаахан байх биз.', english: 'Tomorrow the weather will surely be warm.' },
        { cyrillic: 'Хичээлээ сайн давтаарай шүү!', english: 'Make sure to review your lessons, mind you!' }
      ]
    },

    // -------------------------------------------------------------------------
    // C1 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_c1_01',
      title: 'Honorific Grammatical Register (Хүндэтгэлийн найруулга)',
      cyrillicTitle: 'Эрхэмсэг ба хүндэтгэлийн найруулгын тогтолцоо',
      cefr: 'C1',
      summary: 'Mongolian features an elaborate honorific system replacing common verbs, nouns, and pronouns when referring to elders, scholars, and dignitaries.',
      formationRules: [
        'Lexical suppletion: идэх -> зооглох, явах/ирэх -> морилох, хэлэх -> айлдах, өгөх -> өргөн барих',
        'Suffixal honorific: -лаа/лээ replaced by respectful participles + байна уу, таална уу'
      ],
      commonMistakes: [
        'Using honorific verbs to describe one\'s OWN actions (*Би зооглов is a major cultural breach; only use for honored interlocutors or third persons).'
      ],
      examples: [
        { cyrillic: 'Та цай зооглоно уу?', english: 'Would you please partake of tea? (honorific)' },
        { cyrillic: 'Багш манай сургуульд морилов.', english: 'The venerable professor has arrived at our school.' },
        { cyrillic: 'Эрхэм зочин үг айлдав.', english: 'The distinguished guest delivered an address.' }
      ]
    },
    {
      id: 'g_c1_02',
      title: 'Classical Periodic Syntax & Ancient Genitive Appositions',
      cyrillicTitle: 'Сонгодог зохиолын өгүүлбэр зүй ба хуучин найруулга',
      cefr: 'C1',
      summary: 'Analysis of classical sentence architecture found in historical literature, legal documents, and official edicts.',
      formationRules: [
        'Pre-verbal nominalization with archaic accusative -ийг and genitive agents.',
        'Use of archaic converbs: -руун/-рүүн (contemporaneous narrative speech).'
      ],
      commonMistakes: [
        'Misidentifying the subject of the clause when marked in the genitive within subordinate participial embeddings.'
      ],
      examples: [
        { cyrillic: 'Тэнгэрийн тааллаар их төрийг байгуулан засагларуун...', english: 'By the will of Heaven, while establishing and governing the great state...' }
      ]
    },

    // -------------------------------------------------------------------------
    // C2 GRAMMAR CONCEPTS
    // -------------------------------------------------------------------------
    {
      id: 'g_c2_01',
      title: 'Stylistic Nuance in Epics, Oratory & Sacred Poetics',
      cyrillicTitle: 'Туульс, уран илтгэх зүй ба яруу найргийн онцлог',
      cefr: 'C2',
      summary: 'Syntactic inversions, head-alliteration (толгой холболт), parallelism, and rhythmic metrics in high Mongolian literature.',
      formationRules: [
        'Head alliteration: Every line of a quatrain begins with identical phoneme.',
        'Metrical parallelism: Paired syntagms repeating syntactic structures.'
      ],
      commonMistakes: [
        'Treating poetical inversions as ungrammatical in standard analytical prose.'
      ],
      examples: [
        { cyrillic: 'Алтан наран мандахад, ачит ээж минь сэрдэг.', english: 'When the golden sun rises, my beneficent mother awakes.' },
        { cyrillic: 'Эвт шаазгай буга барина, эвдрэлтэй арслан туулайд баригдана.', english: 'Harmonious magpies take down an elk; discordant lions are defeated by a hare.' }
      ]
    }
  ];

  return concepts;
}
