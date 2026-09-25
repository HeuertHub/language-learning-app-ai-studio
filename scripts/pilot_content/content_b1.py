#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_b1_112_01_abstract_noun_derivation_intro (Grammar Introduction)
2. les_b1_112_03_competency_lexicon_qualifications (Vocabulary Introduction)
3. les_b1_112_04_authoring_professional_cv_writing (Writing)
"""

def get_b1_exercises():
    return [
        # LESSON 10: les_b1_112_01_abstract_noun_derivation_intro
        {
            "lessonId": "les_b1_112_01_abstract_noun_derivation_intro",
            "exercises": [
                {
                    "exerciseId": "ex_b1_112_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Deriving Abstract Noun from Verb Stem: -лга⁴",
                    "modality": "NOMINALIZER_DERIVATION",
                    "interactionPattern": "SUFFIX_ATTACHMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["abstract_nominalization", "morphological_derivation"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["хариуцах", "хариуцлага"],
                    "prompt": "Derive the corporate abstract noun meaning 'responsibility / accountability' from the verb stem 'хариуц-' (to be in charge of / answer for) using the nominalizer suffix -лга⁴:",
                    "baseWord": "хариуц-",
                    "suffixOptions": ["-лага", "-лэг", "-лого", "-лөгө"],
                    "correctSuffix": "-лага",
                    "correctAnswer": "хариуцлага",
                    "acceptableAlternatives": ["хариуцлага", "-лага"],
                    "hint": "The stem 'хариуц-' has back vowel 'у' in the root, so it attaches the back unrounded nominalizer suffix '-лага'.",
                    "explanation": "Verb stem 'хариуц-' + nominalizer '-лага' yields the standard professional noun 'хариуцлага' (responsibility, accountability).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'хариуцлага' is the fundamental corporate concept of responsibility.",
                        "onFailure": "'хариуц-' + '-лага' = 'хариуцлага'."
                    },
                    "detailedGrammarNote": "The productive deverbal nominalizer suffix -лга⁴ (-лага, -лэг, -лого, -лөгөө) transforms action verbs into institutional abstract concepts, processes, and corporate obligations.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Ажлын хариуцлага өндөр байх ёстой.",
                        "slowSpeechSynthesisText": "хариуцлага",
                        "ipaTranscription": "/xarʲʊtsʰɮəɢ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Nominalizer -дал⁴ Application to Intransitive Stems",
                    "modality": "NOMINALIZER_DERIVATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["allomorph_selection", "stative_nominalization"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["байдал", "нөхцөл байдал"],
                    "prompt": "Which abstract noun is formed by attaching -дал⁴ to the copular verb stem 'бай-' (to be/exist)?",
                    "stimulusTextCyrillic": "бай- + -дал⁴",
                    "hint": "Think of the common word for 'situation / state / condition'.",
                    "options": [
                        {"id": "nom_baidal", "text": "байдал (situation / state / condition)", "cyrillic": "байдал", "isCorrect": True, "explanation": "Correct! 'бай-' + '-дал' -> 'байдал'."},
                        {"id": "nom_bailga", "text": "байлга (act of maintaining / causing to be)", "cyrillic": "байлга", "isCorrect": False, "explanation": "Incorrect. '-лга' yields action/causative noun, not stative condition."},
                        {"id": "nom_baishil", "text": "байшил", "cyrillic": "байшил", "isCorrect": False, "explanation": "Incorrect. Non-existent derivation."}
                    ],
                    "correctAnswer": "байдал (situation / state / condition)",
                    "acceptableAlternatives": ["байдал"],
                    "explanation": "'Бай-' (to be) combines with nominalizer '-дал' to form 'байдал' (situation, condition, state of affairs).",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! 'байдал' describes conditions and states.",
                        "onFailure": "бай- + -дал = байдал."
                    },
                    "detailedGrammarNote": "Suffix -дал⁴ often attaches to stative and intransitive verbs to denote states of being or phenomena ('байдал' = condition, 'явдал' = conduct/affair, 'суудал' = seat/settlement).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Эдийн засгийн байдал тогтвортой байна.",
                        "slowSpeechSynthesisText": "байдал",
                        "ipaTranscription": "/pæːtəɮ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Syntactic Substitution: Converting Verb Clauses to Nominal Heads",
                    "modality": "NOMINALIZER_DERIVATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["syntactic_nominalization", "register_elevation"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["төлөвлөх", "төлөвлөгөө"],
                    "prompt": "Convert the verbal sentence 'Бид ирэх жил шинэ салбар нээхээр төлөвлөж байна' (We are planning to open a new branch next year) into a formal administrative noun phrase using 'төлөвлөгөө' (plan):",
                    "hint": "'Бидний төлөвлөгөө' (Our plan) replaces the verb.",
                    "options": [
                        {"id": "sub_correct", "text": "Ирэх жил шинэ салбар нээх нь бидний төлөвлөгөөнд тусгагдсан. (Opening a new branch next year is reflected in our plan.)", "cyrillic": "бидний төлөвлөгөөнд тусгагдсан", "isCorrect": True, "explanation": "Correct! Elegant conversion from verbal clause to formal institutional nominal structure."},
                        {"id": "sub_wrong1", "text": "*Бид нар төлөвлөдөг юм уу.", "cyrillic": "*Бид нар төлөвлөдөг юм уу.", "isCorrect": False, "explanation": "Incorrect. Casual colloquial question."},
                        {"id": "sub_wrong2", "text": "*Төлөвлөж байгаа бид.", "cyrillic": "*Төлөвлөж байгаа бид.", "isCorrect": False, "explanation": "Incorrect. Ungrammatical word order."}
                    ],
                    "correctAnswer": "Ирэх жил шинэ салбар нээх нь бидний төлөвлөгөөнд тусгагдсан. (Opening a new branch next year is reflected in our plan.)",
                    "acceptableAlternatives": ["бидний төлөвлөгөөнд тусгагдсан", "Ирэх жил шинэ салбар нээх нь бидний төлөвлөгөөнд тусгагдсан."],
                    "explanation": "Professional Mongolian chancellery style elevates clauses by replacing verbs with derived nominals ('төлөвлөх' -> 'төлөвлөгөөнд тусгагдах').",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Masterful transformation into formal institutional register.",
                        "onFailure": "Nominalize 'төлөвлөх' to 'төлөвлөгөө'."
                    },
                    "detailedGrammarNote": "Deverbal abstract nouns readily take possessive and locative markers ('төлөвлөгөө-нд') to anchor passive and impersonal predicates in organizational reporting.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Ирэх жил шинэ салбар нээх нь бидний төлөвлөгөөнд тусгагдсан.",
                        "slowSpeechSynthesisText": "бидний төлөвлөгөөнд тусгагдсан.",
                        "ipaTranscription": "/irəx tʃʰiɮ ʃinə saɮpər neːx nʲ pitniː tʰɵɮɵwɮɵɡɵːntʰ tʰʊsɢəɡtsʰəŋ/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Semantic Discrimination: Action Verb vs Abstract Derivative",
                    "modality": "NOMINALIZER_DERIVATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["verb_noun_semantic_contrast", "contextual_insertion"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["ажиллах", "ажиллагаа"],
                    "prompt": "Choose the correct word to complete: 'Энэ төхөөрөмжийн хэвийн _________ хангаж ажиллах хэрэгтэй' (We must ensure the normal operation/functioning of this equipment):",
                    "stimulusTextCyrillic": "хэвийн _________ хангаж ажиллах",
                    "hint": "The adjective 'хэвийн' (normal) requires a nominal head meaning 'operation / functioning'.",
                    "options": [
                        {"id": "sem_ajillagaa", "text": "ажиллагааг (operation / functioning - accusative noun)", "cyrillic": "ажиллагааг", "isCorrect": True, "explanation": "Correct! 'Хэвийн ажиллагааг хангах' is the standard technical collocation for ensuring normal operation."},
                        {"id": "sem_ajillah", "text": "ажиллахыг (infinitive action)", "cyrillic": "ажиллахыг", "isCorrect": False, "explanation": "Incorrect. Unnatural technical phrasing."},
                        {"id": "sem_ajilchin", "text": "ажилчныг (worker)", "cyrillic": "ажилчныг", "isCorrect": False, "explanation": "Incorrect. 'Worker' does not fit with 'хэвийн'."}
                    ],
                    "correctAnswer": "ажиллагааг (operation / functioning - accusative noun)",
                    "acceptableAlternatives": ["ажиллагааг", "ажиллагаа"],
                    "explanation": "'Ажиллах' (to work) derives 'ажиллагаа' (operation, process, action). In the accusative case with 'хангах' (to ensure/provide), it forms the idiomatic compound 'хэвийн ажиллагааг хангах'.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'хэвийн ажиллагаа' is the standard operational term.",
                        "onFailure": "Use derived noun: 'ажиллагааг'."
                    },
                    "detailedGrammarNote": "Compound deverbal nouns in -лгаа⁴ ('үйл ажиллагаа' = operations, 'ажиллагаа' = function/operation) dominate workplace technical instructions.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэ төхөөрөмжийн хэвийн ажиллагааг хангаж ажиллах хэрэгтэй.",
                        "slowSpeechSynthesisText": "хэвийн ажиллагааг хангах.",
                        "ipaTranscription": "/en tʰɵxɵːrɵmtʃʰiːŋ xewiːŋ atʃʰiɮɮaɢaːɡ xaŋɢətʃʰ atʃʰiɮɮəx xirəkʰtʰeː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Token Assembly: Workplace Policy Statement with Multiple Derived Nominals",
                    "modality": "NOMINALIZER_DERIVATION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["multi_nominal_clause_assembly", "institutional_syntax"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["хамтын", "ажиллагаа", "амжилт", "үндэс"],
                    "prompt": "Reconstruct this organizational motto: 'Cooperation is the foundation of success':",
                    "wordTokens": ["үндэс", "хамтын", "ажиллагаа", "амжилтын", "мөн"],
                    "correctTokenOrder": ["хамтын", "ажиллагаа", "амжилтын", "үндэс", "мөн"],
                    "correctAnswer": "хамтын ажиллагаа амжилтын үндэс мөн",
                    "acceptableAlternatives": ["Хамтын ажиллагаа амжилтын үндэс мөн.", "хамтын ажиллагаа амжилтын үндэс"],
                    "hint": "Cooperation (хамтын ажиллагаа) -> of success (амжилтын) -> foundation (үндэс) -> is (мөн).",
                    "explanation": "'Хамтын ажиллагаа' (cooperation) + 'амжилтын үндэс мөн' (is indeed the foundation of success). Both 'ажиллагаа' and 'амжилт' are derived abstract nouns.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Exemplary professional motto assembled.",
                        "onFailure": "Order: хамтын -> ажиллагаа -> амжилтын -> үндэс -> мөн."
                    },
                    "detailedGrammarNote": "'Мөн' at the end of nominal equative clauses acts as an emphatic copula in formal administrative and philosophical statements.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хамтын ажиллагаа амжилтын үндэс мөн.",
                        "slowSpeechSynthesisText": "Хамтын ажиллагаа амжилтын үндэс мөн.",
                        "ipaTranscription": "/xamtʰiːŋ atʃʰiɮɮaɢaː amtʃʰiɮtʰiːŋ untəs mɵŋ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                }
            ]
        },

        # LESSON 11: les_b1_112_03_competency_lexicon_qualifications
        {
            "lessonId": "les_b1_112_03_competency_lexicon_qualifications",
            "exercises": [
                {
                    "exerciseId": "ex_b1_112_03_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Distinguishing 'Мэргэжил' (Profession) vs 'Мэргэшил' (Specialization)",
                    "modality": "COMPETENCY_LEXICON_SELECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["lexical_precision", "hr_terminology_differentiation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["мэргэжил", "мэргэшил"],
                    "prompt": "In formal Mongolian human resources terminology, what is the crucial distinction between 'мэргэжил' and 'мэргэшил'?",
                    "hint": "'Мэргэжил' is your broad baseline profession; 'мэргэшил' is specialized postgraduate or practical qualification.",
                    "options": [
                        {"id": "diff_correct", "text": "'Мэргэжил' denotes basic occupation/profession (e.g. эмч - physician); 'мэргэшил' denotes sub-specialization or advanced credential (e.g. зүрхний эмч - cardiologist).", "cyrillic": "мэргэжил бол мэргэжлийн үндэс, мэргэшил бол нарийн мэргэшлийн зэрэг", "isCorrect": True, "explanation": "Correct! 'Мэргэжил' is occupation/trade, while 'мэргэшил' is professional specialization/qualification."},
                        {"id": "diff_wrong1", "text": "They are completely interchangeable synonyms with no legal or HR difference.", "cyrillic": "Ижил утгатай", "isCorrect": False, "explanation": "Incorrect. Mongolian Civil Service and labor codes strictly differentiate them."},
                        {"id": "diff_wrong2", "text": "'Мэргэшил' means hobby or extracurricular interest.", "cyrillic": "Сонирхол", "isCorrect": False, "explanation": "Incorrect. 'Мэргэшил' is an official credential."}
                    ],
                    "correctAnswer": "'Мэргэжил' denotes basic occupation/profession (e.g. эмч - physician); 'мэргэшил' denotes sub-specialization or advanced credential (e.g. зүрхний эмч - cardiologist).",
                    "acceptableAlternatives": ["мэргэжил - profession, мэргэшил - specialization"],
                    "explanation": "'Мэргэжил' = profession/occupation obtained via initial diploma. 'Мэргэшил' = specialization, continuous professional advancement, or specific qualification accreditation.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Essential distinction for HR and CV writing.",
                        "onFailure": "Мэргэжил = profession; Мэргэшил = specialization/qualification."
                    },
                    "detailedGrammarNote": "Deverbal noun 'мэргэшил' derives from the verb 'мэргэших' (to become specialized/expert in a field).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Миний үндсэн мэргэжил инженер, нарийн мэргэшил нь мэдээллийн аюулгүй байдал.",
                        "slowSpeechSynthesisText": "мэргэжил ба мэргэшил.",
                        "ipaTranscription": "/mʲinʲiː untsəŋ merɡətʃʰiɮ intʃʰineːr, nareːŋ merɡətʃʰiɮ nʲ metiːɮɮiːŋ ajʊːɮɡuː pæːtəɮ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_03_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "HR Collocation Pairing: Verbs to Competency Nouns",
                    "modality": "COMPETENCY_LEXICON_SELECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["collocational_competence", "workplace_phrasing"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["туршлага хуримтлуулах", "ур чадвар эзэмших"],
                    "prompt": "Which verb naturally pairs with 'туршлага' (experience) to mean 'to accumulate / gain professional experience'?",
                    "stimulusTextCyrillic": "ажлын туршлага _________",
                    "hint": "Look for the verb derived from 'хуримтлал' (accumulation).",
                    "options": [
                        {"id": "col_hurimtlulax", "text": "хуримтлуулах (to accumulate / build up)", "cyrillic": "хуримтлуулах", "isCorrect": True, "explanation": "Correct! 'Туршлага хуримтлуулах' is the standard, elegant corporate collocation."},
                        {"id": "col_hudaldan", "text": "худалдан авах (to purchase)", "cyrillic": "худалдан авах", "isCorrect": False, "explanation": "Incorrect. Experience cannot be bought with 'худалдан авах'."},
                        {"id": "col_гээх", "text": "гээх (to lose/drop)", "cyrillic": "гээх", "isCorrect": False, "explanation": "Incorrect. Means to lose."}
                    ],
                    "correctAnswer": "хуримтлуулах (to accumulate / build up)",
                    "acceptableAlternatives": ["хуримтлуулах", "туршлага хуримтлуулах"],
                    "explanation": "'Ажлын туршлага хуримтлуулах' (to accumulate work experience) is the authoritative collocation across resume descriptions.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'туршлага хуримтлуулах' is the authentic professional collocation.",
                        "onFailure": "Pair 'туршлага' with 'хуримтлуулах'."
                    },
                    "detailedGrammarNote": "'Хуримтлуулах' is a causative verb from 'хуримтлах' (to accumulate, amass), widely used in educational and corporate discourse.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Тэрээр санхүүгийн салбарт арван жилийн туршлага хуримтлуулсан.",
                        "slowSpeechSynthesisText": "туршлага хуримтлуулах.",
                        "ipaTranscription": "/tʰereːr saŋxuːɡiːŋ saɮpərtʰ arwəŋ tʃʰiɮiːŋ tʰʊrʃɮəɢ xʊrʲimtʰɮʊːɮsəŋ/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_03_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Deciphering Job Vacancy Minimum Criteria",
                    "modality": "COMPETENCY_LEXICON_SELECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["job_posting_analysis", "qualification_audit"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["тавигдах шаардлага", "бакалавр", "дээш"],
                    "prompt": "Read the following extract from an Ulaanbaatar corporate job posting:\n\n'ТАВИГДАХ ШААРДЛАГА:\n- Бизнесийн удирдлага, эдийн засгийн чиглэлээр бакалавр болон түүнээс дээш зэрэгтэй байх\n- Мэргэжлээрээ 3-аас доошгүй жил ажилласан туршлагатай байх\n- Англи хэлний ахисан түвшний мэдлэгтэй байх'\n\nWhat is the minimum work experience required in the candidate's field?",
                    "stimulusTextCyrillic": "Мэргэжлээрээ 3-аас доошгүй жил ажилласан туршлагатай байх",
                    "hint": "'3-аас доошгүй' means 'not less than 3 / at least 3'.",
                    "options": [
                        {"id": "req_3years", "text": "At least 3 years of work experience in the profession (3-аас доошгүй жил)", "cyrillic": "3-аас доошгүй жил", "isCorrect": True, "explanation": "Correct! '3-аас доошгүй' = minimum of 3 years."},
                        {"id": "req_max3", "text": "Maximum 3 years of experience", "cyrillic": "3-аас ихгүй", "isCorrect": False, "explanation": "Incorrect. 'Доошгүй' means not less than."},
                        {"id": "req_none", "text": "No previous experience required", "cyrillic": "Туршлага шаардахгүй", "isCorrect": False, "explanation": "Incorrect. Experience is mandatory."}
                    ],
                    "correctAnswer": "At least 3 years of work experience in the profession (3-аас доошгүй жил)",
                    "acceptableAlternatives": ["At least 3 years", "3-аас доошгүй жил", "3 years minimum"],
                    "explanation": "'3-аас доошгүй' combines ablative case '-аас' with postposition 'доош' and negative caritive '-гүй' to denote 'not lower than 3 / minimum 3'.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Accurate decoding of legal HR criteria.",
                        "onFailure": "'3-аас доошгүй' = at least 3 years."
                    },
                    "detailedGrammarNote": "Standard administrative threshold criteria utilize the formula '[Num]-аас доошгүй' (minimum) and '[Num]-аас дээшгүй' (maximum).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Мэргэжлээрээ гурваас доошгүй жил ажилласан туршлагатай байх шаардлагатай.",
                        "slowSpeechSynthesisText": "гурваас доошгүй жил ажилласан туршлага.",
                        "ipaTranscription": "/merɡətʃʰɮeːreː ɢʊrwaːs tʰɔːʃɢuː tʃʰiɮ atʃʰiɮɮəsəŋ tʰʊrʃɮəɢtʰæː pæːx ʃaːrtɮəɢtʰaː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_03_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "High-Register Teamwork Descriptor Selection",
                    "modality": "COMPETENCY_LEXICON_SELECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["register_elevation", "soft_skills_lexicon"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["багаар ажиллах", "харилцааны ур чадвар"],
                    "prompt": "Which phrase is the standard, elevated professional expression for 'demonstrates strong teamwork and interpersonal communication skills'?",
                    "hint": "'Багаар ажиллах' (working in a team) + 'харилцааны ур чадвар сайтай' (having good communication skills).",
                    "options": [
                        {"id": "sk_formal", "text": "Багаар ажиллах болон харилцааны өндөр ур чадвартай (Possessing high teamwork and communication competencies)", "cyrillic": "Багаар ажиллах болон харилцааны өндөр ур чадвартай", "isCorrect": True, "explanation": "Correct! Elegant, standard resume wording."},
                        {"id": "sk_colloquial", "text": "Хүмүүстэй сайн ярьж, найзалдаг (Talks well and makes friends with folks)", "cyrillic": "Хүмүүстэй сайн ярьдаг", "isCorrect": False, "explanation": "Incorrect. Overly colloquial and unsuited for a professional profile."},
                        {"id": "sk_passive", "text": "Хүн дуудахаар очдог (Goes when someone calls)", "cyrillic": "Хүн дуудахаар очдог", "isCorrect": False, "explanation": "Incorrect. Not a professional competency."}
                    ],
                    "correctAnswer": "Багаар ажиллах болон харилцааны өндөр ур чадвартай (Possessing high teamwork and communication competencies)",
                    "acceptableAlternatives": ["Багаар ажиллах болон харилцааны өндөр ур чадвартай"],
                    "explanation": "Professional CVs utilize compound nominals with comitative/possessive adjectival suffixes: 'багаар ажиллах болон харилцааны өндөр ур чадвартай'.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! High-register professional soft skill description.",
                        "onFailure": "Use: 'Багаар ажиллах болон харилцааны өндөр ур чадвартай'."
                    },
                    "detailedGrammarNote": "The adjectival suffix '-тай/-тэй⁴' acts productively to create predicate descriptors ('ур чадвартай' = competent, skilled).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Тэрээр багаар ажиллах болон харилцааны өндөр ур чадвартай мэргэжилтэн юм.",
                        "slowSpeechSynthesisText": "багаар ажиллах болон харилцааны өндөр ур чадвар.",
                        "ipaTranscription": "/tʰereːr pʰaɢaːr atʃʰiɮɮəx pɔɮəŋ xarʲiɮtsʰaːniː ɵntɵr ʊr tʃʰatwərtʰæː merɡətʃʰiɮtʰəŋ jʊm/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_03_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Insertion: Professional Analytical Capability",
                    "modality": "COMPETENCY_LEXICON_SELECTION",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["cloze_precision", "analytical_competency_lexicon"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["дүн шинжилгээ хийх"],
                    "prompt": "Fill in the blank with the institutional term meaning 'analysis / evaluation' in the phrase 'асуудалд ______ хийх чадвартай' (capable of conducting analysis on issues):",
                    "contextSentence": "Асуудалд дүн шинжилгээ хийх чадвартай. (Capable of conducting analysis on issues.)",
                    "stimulusTextCyrillic": "асуудалд ______ хийх чадвартай",
                    "hint": "Recall the standard professional compound noun combining the word for evaluation/result with the word for research/analysis.",
                    "correctAnswer": "дүн шинжилгээ",
                    "acceptableAlternatives": ["дүн шинжилгээ", "Дүн шинжилгээ"],
                    "explanation": "'Дүн шинжилгээ хийх' (to perform analytical assessment / data analysis) is the formal phrase for analytical competence.",
                    "learnerFeedback": {
                        "onSuccess": "Гайхалтай! 'дүн шинжилгээ' is the authoritative term for analysis.",
                        "onFailure": "Remember that 'дүн шинжилгээ хийх' expresses professional analytical capability."
                    },
                    "detailedGrammarNote": "'Дүн шинжилгээ' combines 'дүн' (summary, result, grade) with deverbal noun 'шинжилгээ' (investigation, research, analysis from 'шинжлэх').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Асуудалд бодит дүн шинжилгээ хийх чадвартай.",
                        "slowSpeechSynthesisText": "дүн шинжилгээ хийх чадвар.",
                        "ipaTranscription": "/asʊːtəɮtʰ pɔtʲitʰ tʰuŋ ʃintʃʰiɮɡeː xiːx tʃʰatwər/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 12: les_b1_112_04_authoring_professional_cv_writing
        {
            "lessonId": "les_b1_112_04_authoring_professional_cv_writing",
            "exercises": [
                {
                    "exerciseId": "ex_b1_112_04_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Sequencing Standard Mongolian CV Sections",
                    "modality": "PROFESSIONAL_CV_WRITING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["resume_macrostructure", "document_formatting"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Хувийн мэдээлэл", "Боловсрол", "Ажлын туршлага", "Ур чадвар"],
                    "prompt": "Arrange the standard Mongolian resume sections into canonical order from top to bottom:",
                    "wordTokens": ["Ур чадвар", "Хувийн мэдээлэл", "Ажлын туршлага", "Боловсрол"],
                    "correctTokenOrder": ["Хувийн мэдээлэл", "Боловсрол", "Ажлын туршлага", "Ур чадвар"],
                    "correctAnswer": "Хувийн мэдээлэл, Боловсрол, Ажлын туршлага, Ур чадвар",
                    "acceptableAlternatives": ["Хувийн мэдээлэл Боловсрол Ажлын туршлага Ур чадвар"],
                    "hint": "Personal info comes first, followed by education, work history, and competencies.",
                    "explanation": "Standard Mongolian professional resume (товч намтар) architecture progresses logically: 1. Хувийн мэдээлэл (Personal Info) -> 2. Боловсрол (Education) -> 3. Ажлын туршлага (Experience) -> 4. Ур чадвар (Skills).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Standard Mongolian CV layout mastered.",
                        "onFailure": "Order: Хувийн мэдээлэл -> Боловсрол -> Ажлын туршлага -> Ур чадвар."
                    },
                    "detailedGrammarNote": "The traditional term 'намтар' (biography) has evolved in modern corporate practice into 'Анкет' or 'Товч намтар / CV'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Товч намтар нь хувийн мэдээлэл, боловсрол, ажлын туршлага болон ур чадвараас бүрдэнэ.",
                        "slowSpeechSynthesisText": "Хувийн мэдээлэл, боловсрол, ажлын туршлага, ур чадвар.",
                        "ipaTranscription": "/tʰɔwtʃʰ namtʰər nʲ xʊwiːŋ metiːɮəɮ, pɔɮɔwsrɔɮ, atʃʰiɮiːŋ tʰʊrʃɮəɢ pɔɮɔŋ ʊr tʃʰatwəraːs pʊrtən/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_04_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Register Elevation in Action Bullet Points",
                    "modality": "PROFESSIONAL_CV_WRITING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["resume_bullet_crafting", "register_transformation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["удирдан зохион байгуулах", "төсөл хэрэгжүүлэх"],
                    "prompt": "A candidate drafted this conversational draft for their resume: 'Би 5 хүнийг хариуцаж ажилласан' (I worked taking care of 5 people). Which option elevates this into a formal, high-impact bullet point?",
                    "hint": "Use formal participial phrasing: 'удирдан зохион байгуулсан' (managed and organized).",
                    "options": [
                        {"id": "elev_correct", "text": "5 хүний бүрэлдэхүүнтэй төслийн багийг удирдан зохион байгуулж, төлөвлөгөөт ажлыг амжилттай хэрэгжүүлсэн. (Organized and led a 5-person project team, successfully implementing planned targets.)", "cyrillic": "багийг удирдан зохион байгуулсан", "isCorrect": True, "explanation": "Correct! Replaces conversational 'хариуцаж ажилласан' with professional compound verbs 'удирдан зохион байгуулж... хэрэгжүүлсэн'."},
                        {"id": "elev_weak", "text": "Би дарга байсан, 5 хүн миний дор ажилласан. (I was boss, 5 people worked under me.)", "cyrillic": "Би дарга байсан", "isCorrect": False, "explanation": "Incorrect. Egocentric and colloquial."},
                        {"id": "elev_passive", "text": "5 хүн ажиллаж байхыг харсан. (Watched 5 people working.)", "cyrillic": "харсан", "isCorrect": False, "explanation": "Incorrect. Passive observation, not achievement."}
                    ],
                    "correctAnswer": "5 хүний бүрэлдэхүүнтэй төслийн багийг удирдан зохион байгуулж, төлөвлөгөөт ажлыг амжилттай хэрэгжүүлсэн. (Organized and led a 5-person project team, successfully implementing planned targets.)",
                    "acceptableAlternatives": ["5 хүний бүрэлдэхүүнтэй төслийн багийг удирдан зохион байгуулсан"],
                    "explanation": "Professional Mongolian CV bullet points utilize compound modal converbs with perfective past participles: 'удирдан зохион байгуулж... амжилттай хэрэгжүүлсэн'.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! High-impact corporate leadership articulation.",
                        "onFailure": "Elevate with: '5 хүний бүрэлдэхүүнтэй төслийн багийг удирдан зохион байгуулж... хэрэгжүүлсэн.'."
                    },
                    "detailedGrammarNote": "The modal converb in -н ('удирдан') joins seamlessly with secondary transitive verbs ('зохион байгуулах') to form elegant elevated verb chains.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Таван хүний бүрэлдэхүүнтэй төслийн багийг удирдан зохион байгуулж, амжилттай хэрэгжүүлсэн.",
                        "slowSpeechSynthesisText": "төслийн багийг удирдан зохион байгуулсан.",
                        "ipaTranscription": "/tʰawəŋ xuniː pʊreɮtəxuːntʰeː tʰɵsɮiːŋ pʰaɡiːɡ ʊtirtəŋ tsɔxʲɔŋ pæːɢʊːɮtʃʰ, amtʃʰiɮtʰtʰæː xirəkʰtʃuːɮsəŋ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_04_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Composing Career Objective Statement (Зорилго)",
                    "modality": "PROFESSIONAL_CV_WRITING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["career_objective_composition", "rhetorical_framing"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хувь нэмэр оруулах", "мэргэжлийн өсөлт"],
                    "prompt": "Which career objective statement (Зорилго) best demonstrates mutual value creation for an applicant seeking a financial analyst position?",
                    "hint": "Balance personal growth with institutional contribution ('байгууллагын хөгжилд хувь нэмэр оруулах').",
                    "options": [
                        {"id": "obj_mutual", "text": "Өөрийн мэдлэг, ур чадвараа дайчлан санхүүгийн шинжилгээний чиглэлээр тасралтгүй хөгжиж, байгууллагын үйл ажиллагаанд бодитой хувь нэмэр оруулах. (To deploy my knowledge and competencies to continuously develop in financial analysis, making a tangible contribution to organizational operations.)", "cyrillic": "байгууллагын үйл ажиллагаанд бодитой хувь нэмэр оруулах", "isCorrect": True, "explanation": "Correct! Exemplary career objective balancing dedication ('дайчлан'), growth ('хөгжиж'), and institutional impact ('хувь нэмэр оруулах')."},
                        {"id": "obj_selfish", "text": "Өндөр цалинтай ажилд орж, туршлага олж авах. (To get a high-paying job and get experience.)", "cyrillic": "Өндөр цалин авах", "isCorrect": False, "explanation": "Incorrect. Blunt, mercenary, and unacceptable in formal profiles."},
                        {"id": "obj_vague", "text": "Ямар нэгэн ажил олж хийхийг хүсэж байна. (Wanting to find some work to do.)", "cyrillic": "Ямар нэг ажил хийх", "isCorrect": False, "explanation": "Incorrect. Vague and passive."}
                    ],
                    "correctAnswer": "Өөрийн мэдлэг, ур чадвараа дайчлан санхүүгийн шинжилгээний чиглэлээр тасралтгүй хөгжиж, байгууллагын үйл ажиллагаанд бодитой хувь нэмэр оруулах. (To deploy my knowledge and competencies to continuously develop in financial analysis, making a tangible contribution to organizational operations.)",
                    "acceptableAlternatives": ["байгууллагын үйл ажиллагаанд бодитой хувь нэмэр оруулах"],
                    "explanation": "A professional Mongolian career summary highlights: 1. Deploying capability ('дайчлан') + 2. Organizational contribution ('байгууллагын хөгжилд хувь нэмэр оруулах').",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Balanced and persuasive career objective.",
                        "onFailure": "Focus on institutional contribution: 'хувь нэмэр оруулах'."
                    },
                    "detailedGrammarNote": "'Хувь нэмэр оруулах' (literally 'to introduce a share and addition') is the universal idiomatic expression for 'to contribute to a collective goal'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Өөрийн ур чадвараа дайчлан, байгууллагын хөгжилд бодитой хувь нэмэр оруулах.",
                        "slowSpeechSynthesisText": "байгууллагын хөгжилд хувь нэмэр оруулах.",
                        "ipaTranscription": "/ɵːriːŋ ʊr tʃʰatwəraː tæːtʃʰɮəŋ, pæːɢʊːɮɮəɢiːŋ xɵɡtʃʰiɮtʰ pɔtʲitʰeː xʊwʲ nʲimər ɔrʊːɮəx/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_04_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Completion: Educational Degree Qualification Phrase",
                    "modality": "PROFESSIONAL_CV_WRITING",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["diploma_entry_precision", "academic_credential_cloze"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["төгссөн", "мэргэжлээр", "диплом"],
                    "prompt": "Fill in the blank with the appropriate past participle of 'төгсөх' (to graduate) in your education entry:\n\n'2020 онд Монгол Улсын Их Сургуулийг программ хангамжийн инженер мэргэжлээр _______.'",
                    "contextSentence": "2020 онд МУИС-ийг төгссөн. (Graduated NUM in 2020.)",
                    "stimulusTextCyrillic": "инженер мэргэжлээр _______.",
                    "hint": "Apply the rounded front-vowel past participle suffix (-сөн) to the verbal stem for completing/graduating.",
                    "correctAnswer": "төгссөн",
                    "acceptableAlternatives": ["төгссөн", "Төгссөн"],
                    "explanation": "'Төгссөн' (graduated) is the standard terminal participle for educational history entries in Mongolian CVs.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'төгссөн' is the exact credential verb.",
                        "onFailure": "Use the past participle form of 'төгсөх' (-сөн) to mark educational completion."
                    },
                    "detailedGrammarNote": "In Mongolian CV syntax, the university name takes the accusative case ('Их Сургуулийг'), the major takes the instrumental ('мэргэжлээр'), and the entry concludes with past participle 'төгссөн'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хоёр мянга хорин онд Монгол Улсын Их Сургуулийг программ хангамжийн инженер мэргэжлээр төгссөн.",
                        "slowSpeechSynthesisText": "инженер мэргэжлээр төгссөн.",
                        "ipaTranscription": "/xɔjər mʲaŋɢə xɔrʲəŋ ɔŋtʰ mɔŋɢəɮ ʊɮsiːŋ ix sʊrɢʊːɮiːɡ pʰrɔɡram xaŋɢəmtʃʰiːŋ intʃʰineːr merɡətʃʰɮeːr tʰɵɡssɵŋ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_b1_112_04_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "CV Section Rubric Evaluation",
                    "modality": "PROFESSIONAL_CV_WRITING",
                    "interactionPattern": "OPEN_RESPONSE_RUBRIC",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["cv_self_evaluation", "holistic_rubric_grading"],
                    "grammarTargets": ["gram_b1_noun_derivation_abstract_dal_laga"],
                    "vocabularyTargets": ["ажлын туршлага", "гүйцэтгэсэн үүрэг", "үр дүн"],
                    "prompt": "Evaluate this draft CV work experience excerpt against institutional standards:\n\n'2021-2023 он: \"Номин Холдинг\" ХХК-д Маркетингийн менежер.\n- Компанийн шинэ бүтээгдэхүүний зах зээлийн судалгааг удирдан хийсэн.\n- Борлуулалтын хэмжээг 15 хувиар өсгөсөн.\n- Багийн 4 гишүүнийг өдөр тутмын үйл ажиллагаагаар чиглүүлсэн.'\n\nExplain whether this excerpt meets professional standards for: 1. Action verbs, 2. Quantified results, 3. Grammatical accuracy.",
                    "stimulusTextCyrillic": "2021-2023 он: Маркетингийн менежер ... Борлуулалтын хэмжээг 15 хувиар өсгөсөн.",
                    "correctAnswer": "Meets professional standards with clear elevated action verbs (удирдан хийсэн, өсгөсөн, чиглүүлсэн), measurable outcome (15 хувиар өсгөсөн), and correct casing.",
                    "acceptableAlternatives": ["Meets professional standards", "Зөв боловсруулсан", "Standard compliant"],
                    "hint": "Notice whether verbs are elevated and whether measurable outcomes (15%) are included.",
                    "explanation": "The excerpt successfully satisfies professional CV criteria: elevated deverbal participles, quantified commercial achievement (15% growth), and accurate casing (ХХК-д, судалгааг).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! You evaluated the CV entry with critical professional acuity.",
                        "onFailure": "Check if the entry contains elevated action verbs and quantified impact."
                    },
                    "detailedGrammarNote": "Modern Mongolian business CVs emphasize concrete results ('үр дүн') expressed via quantified instrumental percentages ('15 хувиар').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэхүү товч намтрын хэсэг нь мэргэжлийн шаардлагад бүрэн нийцсэн байна.",
                        "slowSpeechSynthesisText": "мэргэжлийн шаардлагад бүрэн нийцсэн.",
                        "ipaTranscription": "/enəxuː tʰɔwtʃʰ namtʰriːŋ xisəɡ nʲ merɡətʃʰɮiːŋ ʃaːrtɮəɢtʰ pʰurəŋ nʲiːtsʰsəŋ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "RUBRIC_CRITERIA",
                        "rubricCriteria": [
                            {"criterion": "Identifies elevated action verbs", "points": 40, "description": "Notes 'удирдан хийсэн', 'өсгөсөн', 'чиглүүлсэн'."},
                            {"criterion": "Recognizes quantified metrics", "points": 30, "description": "Points out '15 хувиар өсгөсөн'."},
                            {"criterion": "Verifies grammatical suffix accuracy", "points": 30, "description": "Confirms correct case usage like accusative 'судалгааг'."}
                        ]
                    }
                }
            ]
        }
    ]
