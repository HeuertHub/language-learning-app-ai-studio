#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C1 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_c1_198_01_administrative_chancellery_syntax_intro (Grammar Introduction)
2. les_c1_198_02_constitutional_articles_parsing_reading (Reading)
3. les_c1_198_03_sovereign_rights_commentary_writing (Writing)
"""

def get_c1_exercises():
    return [
        # LESSON 16: les_c1_198_01_administrative_chancellery_syntax_intro
        {
            "lessonId": "les_c1_198_01_administrative_chancellery_syntax_intro",
            "exercises": [
                {
                    "exerciseId": "ex_c1_198_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Deconstructing Multi-Tiered Chancellery Participial Embedding",
                    "modality": "CHANCELLERY_SYNTACTIC_PARSING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["chancellery_parsing", "complex_nominal_embedding"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["үндэслэн", "тогтоосугай", "заасныг"],
                    "prompt": "Analyze the opening statutory clause of a Government Resolution (Засгийн газрын тогтоол):\n\n'Монгол Улсын Засгийн газрын тухай хуулийн 30 дугаар зүйлийн 1 дэх хэсэгт заасныг үндэслэн, Төрийн албаны тухай хуулийн хэрэгжилтийг хангах зорилгоор Монгол Улсын Засгийн газраас ТОГТООХ нь:'\n\nWhat is the syntactic function of the participial chain 'заасныг үндэслэн'?",
                    "stimulusTextCyrillic": "хуулийн ... заасныг үндэслэн",
                    "hint": "'Заасныг' is an accusative past participial nominal head ('that which was stipulated'), and 'үндэслэн' is a modal converb meaning 'basing upon'.",
                    "options": [
                        {"id": "parse_legal_basis", "text": "It establishes the statutory legal basis and enabling authority upon which the executive branch derives its decree power.", "cyrillic": "Хууль зүйн үндэслэлийг заах бүтээц", "isCorrect": True, "explanation": "Correct! '[Statute]-д заасныг үндэслэн' is the mandatory constitutional chancellery formula anchoring executive legality."},
                        {"id": "parse_historical", "text": "It serves as an informal historical anecdote with no binding legal effect.", "cyrillic": "Түүхэн жишээ", "isCorrect": False, "explanation": "Incorrect. It is the operative jurisdictional authority."},
                        {"id": "parse_interrogative", "text": "It expresses a question asking parliament for clarification.", "cyrillic": "Асуулт", "isCorrect": False, "explanation": "Incorrect. It is a formal decree enactment."}
                    ],
                    "correctAnswer": "It establishes the statutory legal basis and enabling authority upon which the executive branch derives its decree power.",
                    "acceptableAlternatives": ["It establishes statutory legal basis", "Хууль зүйн үндэслэлийг заах"],
                    "explanation": "Chancellery syntax embeds statutory authority using: [Statute]-д 'заасныг' (accusative nominalized participle) + 'үндэслэн' (modal converb = based upon).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Accurate deconstruction of formal chancellery enabling clauses.",
                        "onFailure": "'заасныг үндэслэн' establishes the statutory legal authority of the decree."
                    },
                    "detailedGrammarNote": "Modern Mongolian administrative drafting strictly adheres to the 'Preamble -> Legal Basis -> Enactment Formula (ТОГТООХ нь:)' tri-partite statutory structure.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Монгол Улсын Засгийн газрын тухай хуулийн гучдугаар зүйлийн нэг дэх хэсэгт заасныг үндэслэн, тогтоох нь.",
                        "slowSpeechSynthesisText": "заасныг үндэслэн, тогтоох нь.",
                        "ipaTranscription": "/mɔŋɢəɮ ʊɮsiːŋ tsasɡiːŋ ɢatsriːŋ tʰʊxæː xʊːɮʲiːŋ ɢʊtsʰtʊɢaːr tsʊiɮiːŋ nʲeɡ tʰex xisəɡtʰ tsaːsniːɡ untəsɮəŋ, tʰɔxtʰɔːx nʲ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Interpreting Archaic Precative Enactment: 'ТОГТООСУГАЙ'",
                    "modality": "CHANCELLERY_SYNTACTIC_PARSING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["archaic_chancellery_morphology", "legal_performatives"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["тогтоосугай", "батламжилсугай"],
                    "prompt": "In traditional chancellery and formal governmental decrees, operational paragraphs conclude with archaic verb endings like 'тогтоосугай' or 'батламжилсугай'. What is the grammatical and pragmatic function of the suffix '-сугай/-сүгэй'?",
                    "stimulusTextCyrillic": "Батлан хамгаалах бодлогыг шинэчлэн БАТАЛСУГАЙ.",
                    "hint": "'-сугай' is the historical classical precative/imperative suffix expressing sovereign enactment ('Be it resolved / It is hereby decreed').",
                    "options": [
                        {"id": "arch_performative", "text": "Classical 1st/3rd-person solemn precative suffix expressing binding sovereign fiat ('Be it enacted / Let it be resolved').", "cyrillic": "Төрийн зарлиг, тогтоолын заах төлөвийн эртний нөхцөл", "isCorrect": True, "explanation": "Correct! '-сугай/-сүгэй' is the solemn chancellery performative establishing binding legal decree."},
                        {"id": "arch_past", "text": "Ordinary conversational past tense indicating an action that happened yesterday.", "cyrillic": "Өнгөрсөн цаг", "isCorrect": False, "explanation": "Incorrect. It is not past tense; it enacts present legal authority."},
                        {"id": "arch_doubt", "text": "Subjunctive mood expressing deep doubt and uncertainty.", "cyrillic": "Эргэлзэх төлөв", "isCorrect": False, "explanation": "Incorrect. Decrees are definitive commands, not doubts."}
                    ],
                    "correctAnswer": "Classical 1st/3rd-person solemn precative suffix expressing binding sovereign fiat ('Be it enacted / Let it be resolved').",
                    "acceptableAlternatives": ["Classical precative suffix", "Төрийн зарлиг тогтоолын эртний нөхцөл"],
                    "explanation": "'-сугай/-сүгэй' is inherited from Middle Mongolian and Classical Mongolian chancellery tradition, reserved exclusively for the President, Government, and Supreme Court enactments.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Profound philological and legal comprehension of '-сугай'.",
                        "onFailure": "'-сугай' expresses binding sovereign enactment: 'Let it be enacted'."
                    },
                    "detailedGrammarNote": "Although obsolete in colloquial speech, -сугай⁴ remains actively productive in sovereign jurisprudence, distinguishing constitutional decrees from regular administrative memos.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Төрийн албаны шинэчлэлийн хөтөлбөрийг үүгээр баталсугай.",
                        "slowSpeechSynthesisText": "үүгээр баталсугай.",
                        "ipaTranscription": "/tʰɵriːŋ aɮpəniː ʃinətʃʰɮeɮiːŋ xɵtʰɵɮpɵriːɡ uːɡeːr pʰatʰəɮsʊɢæː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Canonical Decree Article Architecture",
                    "modality": "CHANCELLERY_SYNTACTIC_PARSING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["decree_clause_ordering", "chancellery_hierarchy"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["хяналт тавьж", "үүрэг болгосугай"],
                    "prompt": "Reconstruct the mandatory concluding accountability clause of a Cabinet decree: 'Charge the Minister of Justice with supervising the implementation of this resolution':",
                    "wordTokens": ["үүрэг", "Энэхүү", "сайдад", "хяналт", "тогтоолын", "Хууль", "хэрэгжилтэд", "тавьж", "болгосугай", "ажиллахыг", "зүйн"],
                    "correctTokenOrder": ["Энэхүү", "тогтоолын", "хэрэгжилтэд", "хяналт", "тавьж", "ажиллахыг", "Хууль", "зүйн", "сайдад", "үүрэг", "болгосугай"],
                    "correctAnswer": "Энэхүү тогтоолын хэрэгжилтэд хяналт тавьж ажиллахыг Хууль зүйн сайдад үүрэг болгосугай",
                    "acceptableAlternatives": ["Энэхүү тогтоолын хэрэгжилтэд хяналт тавьж ажиллахыг Хууль зүйн сайдад үүрэг болгосугай."],
                    "hint": "Scope (Энэхүү тогтоолын хэрэгжилтэд) -> Action nominal (хяналт тавьж ажиллахыг) -> Target official (Хууль зүйн сайдад) -> Decree verb (үүрэг болгосугай).",
                    "explanation": "Standard administrative closing: 'Энэхүү тогтоолын хэрэгжилтэд хяналт тавьж ажиллахыг [Title]-д үүрэг болгосугай' (Charge [Title] with exercising oversight over the implementation of this resolution).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Impeccable mastery of Mongolian chancellery article syntax.",
                        "onFailure": "Follow the sequence: Энэхүү тогтоолын хэрэгжилтэд -> хяналт тавьж ажиллахыг -> Хууль зүйн сайдад -> үүрэг болгосугай."
                    },
                    "detailedGrammarNote": "The assigned obligation appears as an accusative verbal noun ('ажиллахыг'), the designated official takes the dative ('сайдад'), and the sovereign verb 'үүрэг болгосугай' anchors the decree.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэхүү тогтоолын хэрэгжилтэд хяналт тавьж ажиллахыг Хууль зүйн сайдад үүрэг болгосугай.",
                        "slowSpeechSynthesisText": "хяналт тавьж ажиллахыг сайдад үүрэг болгосугай.",
                        "ipaTranscription": "/enəxuː tʰɔxtʰɔːɮiːŋ xirəkʰtʃʰiɮtʰət xʲanaɮtʰ tʰæwʲtʃʰ atʃʰiɮɮəxiːɡ xʊːɮʲ tsʊiŋ sæːtʰət ʊːrəkʰ pɔɮɢɔsʊɢæː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Insertion: Chancellery Impersonal Agency Particle",
                    "modality": "CHANCELLERY_SYNTACTIC_PARSING",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["chancellery_enactment_formula", "cloze_accuracy"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["нь", "тогтоох нь"],
                    "prompt": "Fill in the standard administrative topicalizing particle in the enactment heading:\n\n'Монгол Улсын Засгийн газраас ТОГТООХ ______:'",
                    "contextSentence": "Засгийн газраас ТОГТООХ нь: (The Government hereby resolves:)",
                    "stimulusTextCyrillic": "ТОГТООХ ______:",
                    "hint": "Recall the ubiquitous third-person nominalizing/topicalizing enclitic that turns the future verbal noun into a formal chancellery colon introducer.",
                    "correctAnswer": "нь",
                    "acceptableAlternatives": ["нь", "НЬ"],
                    "explanation": "'ТОГТООХ нь:' (The resolving of the Government is as follows:) is the universal statutory heading separating the preamble from the numbered articles.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'ТОГТООХ нь:' correctly formed.",
                        "onFailure": "Remember that 'ТОГТООХ нь:' is the canonical administrative enactment heading."
                    },
                    "detailedGrammarNote": "Verbal noun in -х + 'нь' functions as a formal performative colon-introducer in Mongolian administrative legislation ('ТОГТООХ нь:', 'ЗАХИРАМЖЛАХ нь:').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Монгол Улсын Засгийн газраас тогтоох нь.",
                        "slowSpeechSynthesisText": "тогтоох нь.",
                        "ipaTranscription": "/mɔŋɢəɮ ʊɮsiːŋ tsasɡiːŋ ɢatsraːs tʰɔxtʰɔːx nʲ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Ambiguity Resolution in Administrative Compound Modifiers",
                    "modality": "CHANCELLERY_SYNTACTIC_PARSING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["statutory_ambiguity_resolution", "legal_interpretation"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["хуульд өөрөөр заагаагүй бол", "эрх бүхий байгууллага"],
                    "prompt": "Interpret the statutory proviso: 'Хуульд өөрөөр заагаагүй бол, тусгай зөвшөөрлийг эрх бүхий төрийн захиргааны төв байгууллага олгоно.' (Unless otherwise provided by law, the competent central state administrative body shall issue special licenses.)\n\nWhat happens if another specific statute explicitly designates a different agency to issue a license?",
                    "stimulusTextCyrillic": "Хуульд өөрөөр заагаагүй бол...",
                    "hint": "'Хуульд өөрөөр заагаагүй бол' is a default fallback clause that yields to lex specialis (specific statutes).",
                    "options": [
                        {"id": "amb_yield", "text": "The specific statute takes precedence (lex specialis derogat legi generali); this general clause only applies when no specific statutory provision exists.", "cyrillic": "Тусгайлан заасан хуулийн заалт давамгайлна", "isCorrect": True, "explanation": "Correct! 'Хуульд өөрөөр заагаагүй бол' is the universal Mongolian chancellery phrase establishing a default rule subject to specific statutory overrides."},
                        {"id": "amb_ignore", "text": "The specific statute is invalidated and this general clause always overrules everything.", "cyrillic": "Бусад хуулийг хүчингүй болгоно", "isCorrect": False, "explanation": "Incorrect. 'Өөрөөр заагаагүй бол' explicitly defers to specific legislation."},
                        {"id": "amb_void", "text": "No entity is allowed to issue licenses at all.", "cyrillic": "Олгохгүй", "isCorrect": False, "explanation": "Incorrect. The clause provides a clear regulatory path."}
                    ],
                    "correctAnswer": "The specific statute takes precedence (lex specialis derogat legi generali); this general clause only applies when no specific statutory provision exists.",
                    "acceptableAlternatives": ["The specific statute takes precedence", "Тусгайлан заасан хуулийн заалт давамгайлна"],
                    "explanation": "'Хуульд өөрөөр заагаагүй бол' (Unless otherwise stipulated in law) establishes default administrative jurisdiction while preserving higher statutory specificity.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Rigorous jurisprudential understanding of chancellery provisos.",
                        "onFailure": "'Хуульд өөрөөр заагаагүй бол' yields whenever a specific law provides otherwise."
                    },
                    "detailedGrammarNote": "Dative 'хуульд' + manner adverb 'өөрөөр' + negative past participle 'заагаагүй' + conditional 'бол' constitutes the most ubiquitous jurisdictional qualifier in statutory Mongolian.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хуульд өөрөөр заагаагүй бол тусгай зөвшөөрлийг эрх бүхий байгууллага олгоно.",
                        "slowSpeechSynthesisText": "Хуульд өөрөөр заагаагүй бол.",
                        "ipaTranscription": "/xʊːɮʲtʰ ɵːrɵːr tsaːɢaːɢuː pɔɮ tʰʊst͡sæː tsɵwʃɵːrɮiːɡ erx puxiː pæːɢʊːɮɮəɢ ɔɮɢɔn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 17: les_c1_198_02_constitutional_articles_parsing_reading
        {
            "lessonId": "les_c1_198_02_constitutional_articles_parsing_reading",
            "exercises": [
                {
                    "exerciseId": "ex_c1_198_02_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Constitutional Statutory Parsing: Article 16 Fundamental Rights",
                    "modality": "CONSTITUTIONAL_STATUTORY_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["constitutional_interpretation", "statutory_parsing"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["амьд явах эрх", "халдашгүй чөлөөтэй байх эрх", "үндсэн эрх"],
                    "prompt": "Read the authentic excerpt from Article 16, Clause 1 of the 1992 Democratic Constitution of Mongolia:\n\n'Монгол Улсын иргэн дараах үндсэн эрх, эрх чөлөөг баталгаатай эдэлнэ:\n1/ Амьд явах эрхтэй. Монгол Улсын Эрүүгийн хуульд заасан онц хүнд гэмт хэрэг үйлдсэний учир шүүхийн хүчин төгөлдөр тогтоолоор ялын дээд хэмжээ оногдуулснаас бусад тохиолдолд хүний амь нас бусниулахыг хатуу хориглоно.'\n\nWhat is the strict constitutional threshold established for limiting the fundamental right to life?",
                    "stimulusTextCyrillic": "шүүхийн хүчин төгөлдөр тогтоолоор ... бусад тохиолдолд хүний амь нас бусниулахыг хатуу хориглоно",
                    "hint": "Note the strict procedural requirement: only upon a valid court judgment for extraordinarily grave crimes defined specifically in the Criminal Code.",
                    "options": [
                        {"id": "thresh_court", "text": "It can strictly only occur upon a legally in-force final court judgment for exceptionally grave crimes explicitly prescribed in the Criminal Code; in all other instances, deprivation of life is strictly prohibited.", "cyrillic": "Шүүхийн хүчин төгөлдөр тогтоолоос бусад тохиолдолд хатуу хориглох", "isCorrect": True, "explanation": "Correct! The constitutional text permits limitation only under in-force judicial sentence for statutorily defined grave crimes."},
                        {"id": "thresh_executive", "text": "The Prime Minister or police can suspend the right to life during economic downturns.", "cyrillic": "Захиргааны шийдвэрээр", "isCorrect": False, "explanation": "Incorrect. The executive branch has zero power to alter this right."},
                        {"id": "thresh_absolute_no_court", "text": "The text states the right to life cannot be regulated by any court under any circumstance.", "cyrillic": "Шүүх хамаарахгүй", "isCorrect": False, "explanation": "Incorrect. The text contains the historical proviso regarding judicial sentencing."}
                    ],
                    "correctAnswer": "It can strictly only occur upon a legally in-force final court judgment for exceptionally grave crimes explicitly prescribed in the Criminal Code; in all other instances, deprivation of life is strictly prohibited.",
                    "acceptableAlternatives": ["Only upon an in-force court judgment", "Шүүхийн хүчин төгөлдөр тогтоолоор"],
                    "explanation": "Article 16.1 enshrines the right to life ('Амьд явах эрхтэй') with absolute procedural safeguards ('хүчин төгөлдөр тогтоолоор... бусад тохиолдолд хатуу хориглоно').",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Precise statutory deconstruction of constitutional protections.",
                        "onFailure": "The text requires a final in-force court verdict: 'шүүхийн хүчин төгөлдөр тогтоол'."
                    },
                    "detailedGrammarNote": "'Хүчин төгөлдөр' (legally valid / in-force) + 'тогтоол' (judicial decision) is the cornerstone phrase of procedural due process in Mongolian jurisprudence.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Шүүхийн хүчин төгөлдөр тогтоолоор ялын дээд хэмжээ оногдуулснаас бусад тохиолдолд хүний амь нас бусниулахыг хатуу хориглоно.",
                        "slowSpeechSynthesisText": "хүний амь нас бусниулахыг хатуу хориглоно.",
                        "ipaTranscription": "/ʃuːxiːŋ xutʃʰiŋ tʰɵɡɵɮtɵr tʰɔxtʰɔːɮɔːr jaɮiːŋ tʰeːtʰ ximtʃʰeː ɔnɔɡtʰʊːɮsnaːs pʊsətʰ tʰɔxʲɔɮtʰɔɮtʰ xuniː amʲ nas pʊsʲnʲʊːɮəxiːɡ xatʰʊː xɔrʲiɡɮɔn/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_02_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Distinguishing Legal Terms of Art: Due Process & Inviolability",
                    "modality": "CONSTITUTIONAL_STATUTORY_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["jurisprudential_lexicon", "term_differentiation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["халдашгүй чөлөөтэй байх эрх", "тэгш эрх"],
                    "prompt": "Article 16, Clause 13 guarantees: 'Халдашгүй, чөлөөтэй байх эрхтэй. Хуульд заасан үндэслэл, журмаас гадуур хэнийг ч нэгжих, баривчлах, хорих, мөрдөн мөшгих, эрх чөлөөг нь хязгаарлахыг хориглоно.'\n\nWhat legal concept corresponds to 'Хуульд заасан үндэслэл, журмаас гадуур хэнийг ч баривчлахыг хориглоно'?",
                    "stimulusTextCyrillic": "Хуульд заасан үндэслэл, журмаас гадуур хэнийг ч баривчлахыг хориглоно",
                    "hint": "Think of the constitutional principle ensuring protection against arbitrary arrest: Due Process / Habeas Corpus.",
                    "options": [
                        {"id": "term_habeas", "text": "Procedural Due Process and Freedom from Arbitrary Detention (Habeas Corpus principle).", "cyrillic": "Хууль ёсны дагуу баривчлах, дур мэдэн хорихыг хориглох зарчим", "isCorrect": True, "explanation": "Correct! Forbidding arrest 'outside grounds and procedures established by law' embodies procedural due process."},
                        {"id": "term_property", "text": "Eminent domain compensation for real estate seizure.", "cyrillic": "Өмчлөх эрх", "isCorrect": False, "explanation": "Incorrect. This clause protects personal bodily liberty, not property."},
                        {"id": "term_speech", "text": "Freedom of the press and publication.", "cyrillic": "Хэвлэн нийтлэх эрх", "isCorrect": False, "explanation": "Incorrect. Clause 13 protects bodily security and liberty."}
                    ],
                    "correctAnswer": "Procedural Due Process and Freedom from Arbitrary Detention (Habeas Corpus principle).",
                    "acceptableAlternatives": ["Procedural Due Process", "Хууль ёсны дагуу баривчлах зарчим"],
                    "explanation": "'Халдашгүй, чөлөөтэй байх эрх' guarantees personal inviolability; prohibiting arrest outside statutory procedure ('үндэслэл, журмаас гадуур') enshrines due process.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Accurate constitutional jurisprudence recognition.",
                        "onFailure": "This guarantees due process and protection against arbitrary detention."
                    },
                    "detailedGrammarNote": "'Халдашгүй' derives from verb 'халдах' (to violate/trespass) with the passive potential modal suffix -шгүй ('that which cannot be violated / inviolable').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хуульд заасан үндэслэл, журмаас гадуур хэнийг ч баривчлах, хорихыг хориглоно.",
                        "slowSpeechSynthesisText": "үндэслэл, журмаас гадуур баривчлахыг хориглоно.",
                        "ipaTranscription": "/xʊːɮʲtʰ tsaːsəŋ untəsɮəɮ, tʃʰʊrmraːs ɢatʊːr xiniːɡ tʃʰ pʰarʲiwtʃʰɮəx, xɔrʲixiːɡ xɔrʲiɡɮɔn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_02_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Judicial Torture Prohibition Mandate",
                    "modality": "CONSTITUTIONAL_STATUTORY_READING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["statutory_syntax", "prohibition_formulation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["эрүү шүүлт", "хүнлэг бус", "хориглоно"],
                    "prompt": "Reconstruct this non-derogable constitutional mandate from Article 16.13: 'No one shall be subjected to torture, or to cruel, inhuman or degrading treatment':",
                    "wordTokens": ["хэнийг", "харьцахад", "ч", "бус", "шүүлт", "хориглоно", "хүнлэг", "эрүү", "тулгах"],
                    "correctTokenOrder": ["хэнийг", "ч", "эрүү", "шүүлт", "тулгах", "хүнлэг", "бус", "харьцахад", "хориглоно"],
                    "correctAnswer": "хэнийг ч эрүү шүүлт тулгах, хүнлэг бус харьцахад хориглоно",
                    "acceptableAlternatives": [
                        "хэнийг ч эрүү шүүлт тулгах хүнлэг бус харьцахад хориглоно",
                        "Хэнийг ч эрүү шүүлт тулгах, хүнлэг бус харьцахад хориглоно.",
                        "Хэнийг ч эрүү шүүлт тулгахыг хориглоно",
                        "хэнийг ч эрүү шүүлт тулгахыг хүнлэг бус харьцахад хориглоно"
                    ],
                    "hint": "Structure the negative polarity pronoun and particle first ('хэнийг ч'), followed by the compound crime ('эрүү шүүлт') and its verbal modifier, before concluding with the prohibition.",
                    "explanation": "Constitutional formulation: 'Хэнийг ч эрүү шүүлт тулгах... хатуу хориглоно'. 'Эрүү шүүлт' is the statutory term for torture.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Exact constitutional syntax reassembled.",
                        "onFailure": "Sequence: хэнийг -> ч -> эрүү -> шүүлт -> тулгах -> хүнлэг -> бус -> харьцахад -> хориглоно."
                    },
                    "detailedGrammarNote": "'Эрүү шүүлт' (torture) is a compound noun originating in classical legal terminology, codified in contemporary Mongolian criminal jurisprudence.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хэнийг ч эрүү шүүлт тулгах, хүнлэг бус харьцахад хориглоно.",
                        "slowSpeechSynthesisText": "хэнийг ч эрүү шүүлт тулгахыг хориглоно.",
                        "ipaTranscription": "/xiniːɡ tʃʰ eruː ʃuːɮtʰ tʰʊɮɢəx, xunɮəɡ pʊs xarʲtsʰəxət xɔrʲiɡɮɔn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_02_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Insertion: Judicial Inviolability and Independence",
                    "modality": "CONSTITUTIONAL_STATUTORY_READING",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["constitutional_doctrine_cloze", "judicial_independence"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хараат бус", "шүүгч"],
                    "prompt": "Complete the bedrock constitutional doctrine on the separation of judicial powers from Article 49:\n\n'Шүүгч хараат бус байж, гагцхүү _______ захирагдана.' (Judges shall be independent and subject only to the law.)",
                    "stimulusTextCyrillic": "гагцхүү _______ захирагдана",
                    "hint": "Inflect the nominal root for 'law' into the dative-locative case (-д/-т) following a soft sign (ь).",
                    "correctAnswer": "хуульд",
                    "acceptableAlternatives": ["хуульд", "Хуульд"],
                    "explanation": "'Гагцхүү хуульд захирагдана' (shall be subject only to the law) is the fundamental constitutional formula establishing the independence of the judiciary.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'гагцхүү хуульд захирагдана' is the classic constitutional declaration.",
                        "onFailure": "Remember that 'хууль' takes the dative suffix -д to denote legal subordination ('хуульд захирагдана')."
                    },
                    "detailedGrammarNote": "'Гагцхүү' (only, solely) is an elevated restrictive particle governing the dative passive verb 'захирагдана' (is subjugated to / bound by).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Шүүгч хараат бус байж, гагцхүү хуульд захирагдана.",
                        "slowSpeechSynthesisText": "гагцхүү хуульд захирагдана.",
                        "ipaTranscription": "/ʃuːɡtʃʰ xaraːtʰ pʊs pæːtʃʰ, ɢaɢtsʰxuː xʊːɮʲtʰ tsaxʲirəɢtən/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_02_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Constitutional Court (Цэц) Petition Interpretation",
                    "modality": "CONSTITUTIONAL_STATUTORY_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["constitutional_court_discourse", "jurisprudential_conflict"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Үндсэн хуулийн цэц", "зөрчсөн тухай", "дүгнэлт"],
                    "prompt": "Read the summary of a petition submitted to the Constitutional Court of Mongolia (Үндсэн хуулийн цэц):\n\n'Иргэн Д-гээс гаргасан мэдээлэлд: \"Эрүүгийн хэрэг хянан шийдвэрлэх тухай хуулийн холбогдох заалт нь хүний халдашгүй чөлөөтэй байх эрхийг шүүхийн зөвшөөрөлгүйгээр 48 цагаас илүү хугацаагаар хязгаарлах боломж олгож байгаа нь Монгол Улсын Үндсэн хуулийн 16 дугаар зүйлийн 13 дахь заалтыг зөрчсөн\" гэжээ.'\n\nWhat is the substantive constitutional dispute raised by the petitioner?",
                    "stimulusTextCyrillic": "шүүхийн зөвшөөрөлгүйгээр 48 цагаас илүү хугацаагаар хязгаарлах нь Үндсэн хууль зөрчсөн",
                    "hint": "The petitioner claims allowing detention beyond 48 hours without judicial warrant directly breaches the constitutional guarantee of personal inviolability.",
                    "options": [
                        {"id": "tsets_detention", "text": "Statutory detention of a citizen beyond 48 hours without judicial warrant infringes the constitutional protection of personal liberty and inviolability.", "cyrillic": "Шүүхийн шийдвэргүйгээр 48 цагаас илүү хорих нь Үндсэн хууль зөрчинө", "isCorrect": True, "explanation": "Correct! The petition challenges the procedural duration of warrantless detention under the Criminal Procedure Code."},
                        {"id": "tsets_fee", "text": "The citizen is protesting against paying court filing administrative fees.", "cyrillic": "Төлбөр", "isCorrect": False, "explanation": "Incorrect. No fee dispute is present."},
                        {"id": "tsets_electoral", "text": "The petition challenges the election results of parliamentary representatives.", "cyrillic": "Сонгуулийн маргаан", "isCorrect": False, "explanation": "Incorrect. This is a fundamental human rights petition regarding liberty."}
                    ],
                    "correctAnswer": "Statutory detention of a citizen beyond 48 hours without judicial warrant infringes the constitutional protection of personal liberty and inviolability.",
                    "acceptableAlternatives": ["Statutory detention beyond 48 hours without judicial warrant infringes the Constitution", "48 цагаас илүү баривчлах нь Үндсэн хууль зөрчинө"],
                    "explanation": "Constitutional jurisprudence in Mongolia strictly limits warrantless detention to 48 hours; any statutory expansion triggers immediate Constitutional Court challenge.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Advanced legal reasoning and constitutional petition analysis.",
                        "onFailure": "The challenge focuses on warrantless detention exceeding 48 hours."
                    },
                    "detailedGrammarNote": "'Үндсэн хуулийн цэц' (Constitutional Court) exercises exclusive judicial review over statutory compliance with the 1992 Constitution.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Шүүхийн зөвшөөрөлгүйгээр хүнийг баривчлах хугацааг хуулиар хязгаарласан байдаг.",
                        "slowSpeechSynthesisText": "шүүхийн зөвшөөрөлгүйгээр баривчлах хугацаа.",
                        "ipaTranscription": "/ʃuːxiːŋ tsɵwʃɵːrɵɮɡuːɡeːr xuniːɡ pʰarʲiwtʃʰɮəx xʊɢatsʰaːɡ xʊːɮʲaːr xʲatsɢaːrɮəsəŋ pæːtəɡ/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 18: les_c1_198_03_sovereign_rights_commentary_writing
        {
            "lessonId": "les_c1_198_03_sovereign_rights_commentary_writing",
            "exercises": [
                {
                    "exerciseId": "ex_c1_198_03_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Structuring a Jurisprudential Commentary (Эрх зүйн нийтлэл)",
                    "modality": "JURISPRUDENTIAL_LEGAL_COMMENTARY",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["legal_commentary_structure", "macro_argumentation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хууль зүйн үндэслэл", "дүгнэлт", "маргаантай асуудал"],
                    "prompt": "Arrange the core sections of a formal jurisprudential commentary into canonical scholarly legal sequence:",
                    "wordTokens": ["Дүгнэлт ба зөвлөмж", "Хууль зүйн үндэслэл ба нотолгоо", "Асуудлын тодорхойлолт", "Хууль тогтоомжийн харьцуулсан шинжилгээ"],
                    "correctTokenOrder": ["Асуудлын тодорхойлолт", "Хууль тогтоомжийн харьцуулсан шинжилгээ", "Хууль зүйн үндэслэл ба нотолгоо", "Дүгнэлт ба зөвлөмж"],
                    "correctAnswer": "Асуудлын тодорхойлолт, Хууль тогтоомжийн харьцуулсан шинжилгээ, Хууль зүйн үндэслэл ба нотолгоо, Дүгнэлт ба зөвлөмж",
                    "acceptableAlternatives": ["Асуудлын тодорхойлолт Хууль тогтоомжийн харьцуулсан шинжилгээ Хууль зүйн үндэслэл ба нотолгоо Дүгнэлт ба зөвлөмж"],
                    "hint": "1. Issue Definition -> 2. Statutory Analysis -> 3. Evidentiary Justification -> 4. Conclusion & Recommendations.",
                    "explanation": "Scholarly Mongolian legal writing follows strict progression: 1. Асуудлын тодорхойлолт (Statement of Issue) -> 2. Хууль тогтоомжийн харьцуулсан шинжилгээ (Comparative Statutory Analysis) -> 3. Хууль зүйн үндэслэл (Jurisprudential Arguments) -> 4. Дүгнэлт ба зөвлөмж (Conclusion & Recommendations).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Authoritative structural sequencing of legal analysis.",
                        "onFailure": "Sequence: Асуудлын тодорхойлолт -> Харьцуулсан шинжилгээ -> Үндэслэл -> Дүгнэлт."
                    },
                    "detailedGrammarNote": "Legal commentaries ('Эрх зүйн нийтлэл / Эрдэм шинжилгээний өгүүлэл') require rigorous formal architecture to establish academic and judicial credibility.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Эрх зүйн нийтлэл нь асуудлын тодорхойлолт, хууль зүйн дүн шинжилгээ, дүгнэлтээс бүрдэнэ.",
                        "slowSpeechSynthesisText": "асуудлын тодорхойлолт, хууль зүйн үндэслэл, дүгнэлт.",
                        "ipaTranscription": "/erx tsʊiŋ nʲiːtʰɮəɮ nʲ asʊːtɮiːŋ tʰɔtʰɔrxɔeɮɔɮtʰ, xʊːɮʲ tsʊiŋ tʰuŋ ʃintʃʰiɮɡeː, tʰuɡnəɮtʰeːs pʊrtən/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_03_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "High-Register Concessive and Conditional Legal Qualifications",
                    "modality": "JURISPRUDENTIAL_LEGAL_COMMENTARY",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["legal_qualification", "concessive_syntax"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["үл харгалзан", "хэдий тийм боловч", "хязгаарласнаас бусад тохиолдолд"],
                    "prompt": "Which sentence demonstrates the appropriate high-register concessive legal qualification for reconciling public health emergencies with constitutional civil liberties?",
                    "hint": "Combine the modal converb for 'notwithstanding' with the statutory limitation proviso ('except where specifically restricted by statute').",
                    "options": [
                        {"id": "qual_scholarly", "text": "Онцгой дэглэм тогтоосон нөхцөл байдлыг үл харгалзан, Үндсэн хуульд тусгайлан заасан язгуур эрхийг хуулиар хязгаарласнаас бусад тохиолдолд дур мэдэн хязгаарлах нь эрх зүйт төрийн зарчимд үл нийцнэ. (Notwithstanding the circumstances of an emergency regime, arbitrarily curtailing fundamental rights explicitly guaranteed by the Constitution—except where specifically restricted by statute—contravenes the principle of the rule of law.)", "cyrillic": "Нөхцөл байдлыг үл харгалзан ... дур мэдэн хязгаарлах нь үл нийцнэ", "isCorrect": True, "explanation": "Correct! High-register chancellery phrasing incorporating modal converb 'үл харгалзан' and formal negation 'үл нийцнэ'."},
                        {"id": "qual_weak", "text": "Өвчин гарсан ч гэсэн хүмүүсийг хорьж болохгүй гэж бодож байна. (Even if sickness came, I think we shouldn't lock folks up.)", "cyrillic": "болохгүй гэж бодож байна", "isCorrect": False, "explanation": "Incorrect. Conversational, colloquial, and devoid of legal authority."},
                        {"id": "qual_unilateral", "text": "Гүйцэтгэх засаглалын тэргүүн онцгой дэглэмийн үед хүний эрхийг дур мэдэн хязгаарлах бүрэн эрхтэй гэж үзэх нь зүйтэй. (It is appropriate to deem that the head of the executive branch holds full authority to arbitrarily restrict human rights during an emergency regime.)", "cyrillic": "дур мэдэн хязгаарлах бүрэн эрхтэй", "isCorrect": False, "explanation": "Incorrect. Contravenes the constitutional supremacy and non-derogable rights doctrine."}
                    ],
                    "correctAnswer": "Онцгой дэглэм тогтоосон нөхцөл байдлыг үл харгалзан, Үндсэн хуульд тусгайлан заасан язгуур эрхийг хуулиар хязгаарласнаас бусад тохиолдолд дур мэдэн хязгаарлах нь эрх зүйт төрийн зарчимд үл нийцнэ. (Notwithstanding the circumstances of an emergency regime, arbitrarily curtailing fundamental rights explicitly guaranteed by the Constitution—except where specifically restricted by statute—contravenes the principle of the rule of law.)",
                    "acceptableAlternatives": ["Онцгой дэглэм тогтоосон нөхцөл байдлыг үл харгалзан"],
                    "explanation": "Advanced legal commentary employs compound concessives ('үл харгалзан' = notwithstanding) and absolute negative verb prefixes ('үл нийцнэ' = does not conform to).",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Flawless jurisprudential balance and scholarly qualification.",
                        "onFailure": "Use 'үл харгалзан' and formal chancellery syntax."
                    },
                    "detailedGrammarNote": "The negative particle 'үл' prefixed directly to present-future finite verbs ('үл нийцнэ', 'үл болно') is a hallmark of formal Mongolian juridical style.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Язгуур эрхийг хууль бусаар хязгаарлах нь эрх зүйт төрийн зарчимд үл нийцнэ.",
                        "slowSpeechSynthesisText": "эрх зүйт төрийн зарчимд үл нийцнэ.",
                        "ipaTranscription": "/jazɢʊːr erxiːɡ xʊːɮʲ pʊsaːr xʲatsɢaːrɮəx nʲ erx tsʊitʰ tʰɵriːŋ tsartʃʰimtʰ uɮ nʲiːtsʰnə/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_03_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Drafting an Amicus Curiae Legal Argument on Proportionality",
                    "modality": "JURISPRUDENTIAL_LEGAL_COMMENTARY",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["proportionality_principle_writing", "legal_argumentation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["зохистой харьцааны зарчим", "үндэслэлтэй байх"],
                    "prompt": "How is the international legal doctrine of 'proportionality' (the measure must be suitable, necessary, and proportionate to the legitimate aim) formulated in authoritative Mongolian legal jurisprudence?",
                    "hint": "Recall the bedrock administrative and constitutional law test requiring that state interventions be suitable, strictly necessary, and inflict the least possible intrusion on rights.",
                    "options": [
                        {"id": "prop_formal", "text": "Зохистой харьцааны зарчим: Төрийн байгууллагаас иргэний эрхийг хязгаарлахдаа тавьсан зорилгодоо нийцсэн, хамгийн бага хохирол учруулах хувилбарыг сонгосон байх шаардлага. (The principle of proportionality: The requirement that when limiting citizen rights, state organs must choose the measure that is suited to the stated objective and inflicts the least harm.)", "cyrillic": "Зохистой харьцааны зарчим", "isCorrect": True, "explanation": "Correct! 'Зохистой харьцааны зарчим' is the authoritative Mongolian legal term for proportionality in constitutional and administrative law."},
                        {"id": "prop_legitimacy", "text": "Хууль ёсны итгэлийг хамгаалах зарчим: Төрийн байгууллагын хууль ёсны шийдвэрт итгэсэн иргэний эрх ашгийг хамгаалах шаардлага. (Principle of legitimate expectations: The requirement to protect the rights of citizens who relied on official state decisions.)", "cyrillic": "Хууль ёсны итгэлийг хамгаалах зарчим", "isCorrect": False, "explanation": "Incorrect. This defines legitimate expectation (Vertrauensschutz), not proportionality."},
                        {"id": "prop_equity", "text": "Шударга ёсыг тэгш хангах зарчим: Бүх оролцогчдод процессын хувьд адил тэгш боломж олгох шаардлага. (Principle of procedural equity: The requirement to grant identical procedural opportunities to all participants.)", "cyrillic": "Шударга ёсыг тэгш хангах зарчим", "isCorrect": False, "explanation": "Incorrect. This refers to procedural due process and equality before the law."}
                    ],
                    "correctAnswer": "Зохистой харьцааны зарчим: Төрийн байгууллагаас иргэний эрхийг хязгаарлахдаа тавьсан зорилгодоо нийцсэн, хамгийн бага хохирол учруулах хувилбарыг сонгосон байх шаардлага. (The principle of proportionality: The requirement that when limiting citizen rights, state organs must choose the measure that is suited to the stated objective and inflicts the least harm.)",
                    "acceptableAlternatives": ["Зохистой харьцааны зарчим", "Principle of proportionality"],
                    "explanation": "'Зохистой харьцааны зарчим' governs all legitimate state limitations on constitutional rights in Modern Mongolian jurisprudence.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'Зохистой харьцааны зарчим' is the exact legal doctrine.",
                        "onFailure": "Proportionality in Mongolian jurisprudence is 'Зохистой харьцааны зарчим'."
                    },
                    "detailedGrammarNote": "Adopted into the General Administrative Law of Mongolia (Захиргааны ерөнхий хууль), this doctrine binds administrative agencies under Article 4.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Төрийн үйл ажиллагаанд зохистой харьцааны зарчмыг чанд баримтлах үүрэгтэй.",
                        "slowSpeechSynthesisText": "зохистой харьцааны зарчим.",
                        "ipaTranscription": "/tʰɵriːŋ uæɮ atʃʰiɮɮaɢaːntʰ tsɔxʲistʰɔe xartʃʰaːniː tsartʃʰmiːɡ tʃʰaŋtʰ pʰarʲimtʰɮəx ʊːrəkʰtʰeː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_03_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Insertion: Judicial Precedent and Case Grounding",
                    "modality": "JURISPRUDENTIAL_LEGAL_COMMENTARY",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["case_citation_cloze", "legal_commentary"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Улсын Дээд шүүх", "тайлбар"],
                    "prompt": "Fill in the blank with the legal term for official judicial interpretation issued by the Supreme Court of Mongolia:\n\n'Энэхүү маргааныг шийдвэрлэхдээ Улсын Дээд шүүхийн албан ёсны _________ иш татах шаардлагатай.' (In resolving this dispute, it is necessary to cite the official interpretation of the Supreme Court.)",
                    "contextSentence": "Дээд шүүхийн албан ёсны тайлбар. (Supreme Court official interpretation.)",
                    "stimulusTextCyrillic": "албан ёсны _________ иш татах",
                    "hint": "Recall the legal term denoting an authoritative judicial interpretation or doctrinal commentary, declined here into the accusative case (-ыг) as the direct object of 'иш татах'.",
                    "correctAnswer": "тайлбарыг",
                    "acceptableAlternatives": ["тайлбар", "тайлбарыг", "Тайлбарыг"],
                    "explanation": "'Улсын Дээд шүүхийн албан ёсны тайлбар' (Official Interpretation of the Supreme Court) provides authoritative guidance on statutory application.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'тайлбар' (in accusative: 'тайлбарыг') correctly cited.",
                        "onFailure": "Remember that 'тайлбарыг иш татах' denotes citing an official Supreme Court judicial interpretation."
                    },
                    "detailedGrammarNote": "Under Article 50 of the Constitution, the Supreme Court issues binding interpretations ('албан ёсны тайлбар') to ensure uniform national law enforcement.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Улсын Дээд шүүхийн албан ёсны тайлбарыг иш татах шаардлагатай.",
                        "slowSpeechSynthesisText": "албан ёсны тайлбарыг иш татах.",
                        "ipaTranscription": "/ʊɮsiːŋ tʰeːtʰ ʃuːxiːŋ aɮpəŋ jɵsniː tʰæːɮpriːɡ iʃ tʰatʰəx ʃaːrtɮəɢtʰaː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_c1_198_03_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "C1 Holistic Legal Commentary Rubric Evaluation",
                    "modality": "JURISPRUDENTIAL_LEGAL_COMMENTARY",
                    "interactionPattern": "OPEN_RESPONSE_RUBRIC",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["legal_argument_evaluation", "rubric_assessment"],
                    "grammarTargets": ["gram_c1_administrative_chancellery_syntax"],
                    "vocabularyTargets": ["хуулийн хэрэгжилт", "эрх зүйн шинжилгээ", "үндсэн хуулийн хяналт"],
                    "prompt": "Evaluate this submitted legal commentary paragraph written by an advanced scholar:\n\n'Төрийн нууцын тухай хуулиар мэдээлэл хайх, хүлээн авах иргэний үндсэн эрхийг хязгаарлах нь зөвхөн үндэсний аюулгүй байдлыг хамгаалах зайлшгүй шаардлагад үндэслэсэн байх ёстой. Хэдийгээр төр өөрийн бүрэн эрхийн хүрээнд нууцын зэрэглэл тогтоох эрхтэй боловч, уг хязгаарлалт нь зохистой харьцааны зарчмыг хангаагүй тохиолдолд Үндсэн хуулийн 16 дугаар зүйлийн 17 дахь хэсгийг зөрчсөн гэж үзэх хууль зүйн бүрэн үндэслэлтэй юм.'\n\nEvaluate the paragraph against: 1. Constitutional statutory citation precision, 2. Concessive and balance syntax (хэдийгээр... боловч), 3. Application of the proportionality doctrine.",
                    "stimulusTextCyrillic": "Төрийн нууцын тухай хуулиар ... зохистой харьцааны зарчмыг хангаагүй тохиолдолд Үндсэн хуулийн ... зөрчсөн гэж үзэх бүрэн үндэслэлтэй.",
                    "correctAnswer": "Exemplary C1 jurisprudential commentary exhibiting precise constitutional grounding (Art 16.17), sophisticated concessive syntax (хэдийгээр... боловч), and rigorous operationalization of the proportionality doctrine (зохистой харьцааны зарчим).",
                    "acceptableAlternatives": ["Exemplary C1 jurisprudential commentary", "Шалгуурыг бүрэн хангасан", "Meets all criteria"],
                    "hint": "Analyze whether the paragraph reconciles state secrets with citizen information rights using the proportionality principle and balanced complex conjunctions.",
                    "explanation": "This text exemplifies authentic C1 legal scholarship: accurate citation (Art. 16.17 - right to seek and receive information), sophisticated antithetical conjunctions ('хэдийгээр... боловч'), and sound doctrine ('зохистой харьцааны зарчим').",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! High-level jurisprudential critical evaluation executed flawlessly.",
                        "onFailure": "Check statutory citations, concessive conjunctions, and proportionality doctrine."
                    },
                    "detailedGrammarNote": "Pairing 'хэдийгээр... боловч' (although... nevertheless) with conditional 'тохиолдолд' (in the event that) is standard rhetorical architecture in Mongolian Supreme Court briefs.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэхүү эрх зүйн тайлбар нь дүн шинжилгээний өндөр түвшинд боловсруулагдсан байна.",
                        "slowSpeechSynthesisText": "эрх зүйн дүн шинжилгээний үнэлгээ.",
                        "ipaTranscription": "/enəxuː erx tsʊiŋ tʰæːɮpər nʲ tʰuŋ ʃintʃʰiɮɡeːniː ɵntɵr tʰuwʃintʰ pɔɮɔwsrʊːɮəɢtsʰəŋ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "RUBRIC_CRITERIA",
                        "rubricCriteria": [
                            {"criterion": "Statutory Grounding & Citation", "points": 35, "description": "Accurately references constitutional rights (Art. 16.17) and State Secrets Act."},
                            {"criterion": "Syntactic Complexity & Concessive Balance", "points": 35, "description": "Deploys 'хэдийгээр... боловч' and conditional participial chaining seamlessly."},
                            {"criterion": "Doctrinal Application (Proportionality)", "points": 30, "description": "Integrates 'зохистой харьцааны зарчим' as the test of constitutionality."}
                        ]
                    }
                }
            ]
        }
    ]
