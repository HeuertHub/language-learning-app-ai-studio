#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B2 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_b2_156_01_parliamentary_interpellation_listening (Listening)
2. les_b2_156_02_topic_vs_contrastive_topic_syntax (Grammar Introduction)
3. les_b2_166_06_b2_sec01_culminating_mastery_capstone (Synthesis/Capstone)
"""

def get_b2_exercises():
    return [
        # LESSON 13: les_b2_156_01_parliamentary_interpellation_listening
        {
            "lessonId": "les_b2_156_01_parliamentary_interpellation_listening",
            "exercises": [
                {
                    "exerciseId": "ex_b2_156_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Acoustic Dissection: Identifying Interpellation Thrust",
                    "modality": "PARLIAMENTARY_ACOUSTIC_DISSECTION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["parliamentary_discourse_analysis", "political_stance_identification"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["УИХ-ын асуулга", "төсвийн зарцуулалт", "хариуцлага тооцох"],
                    "prompt": "Listen to the Member of Parliament addressing the Minister of Finance during question time:\n\n'Улсын төсвийн тодотголд тусгагдсан нийтийн тээврийн парк шинэчлэлийн хөрөнгө оруулалт бодит байдал дээр ямар үр дүнд хүрсэн бэ? Энэ талаар холбогдох сайд тодорхой тайлбар өгнө үү.'\n\nWhat is the primary thrust of the MP's interpellation?",
                    "stimulusTextCyrillic": "Улсын төсвийн тодотголд тусгагдсан нийтийн тээврийн парк шинэчлэлийн хөрөнгө оруулалт бодит байдал дээр ямар үр дүнд хүрсэн бэ?",
                    "hint": "Focus on 'төсвийн тодотгол' (budget amendment) and 'бодит үр дүн' (actual tangible results).",
                    "options": [
                        {"id": "thrust_budget", "text": "Demanding accountability and concrete evidence on how budget funds for public transit fleet modernization were spent.", "cyrillic": "Нийтийн тээврийн төсвийн бодит үр дүнг шаардах", "isCorrect": True, "explanation": "Correct! The MP questions the tangible return on investment from public transit budget allocations."},
                        {"id": "thrust_praise", "text": "Formally congratulating the minister on completing the transit modernization ahead of schedule.", "cyrillic": "Баяр хүргэх", "isCorrect": False, "explanation": "Incorrect. The tone is interrogative and skeptical."},
                        {"id": "thrust_delay", "text": "Proposing that transit funding be canceled altogether.", "cyrillic": "Цуцлах", "isCorrect": False, "explanation": "Incorrect. The MP is pressing for implementation results, not cancellation."}
                    ],
                    "correctAnswer": "Demanding accountability and concrete evidence on how budget funds for public transit fleet modernization were spent.",
                    "acceptableAlternatives": ["Demanding accountability on transit budget spending", "төсвийн зарцуулалтын үр дүнг шаардах"],
                    "explanation": "Parliamentary interpellation (асуулга) uses polite chancellery syntax ('тодорхой тайлбар өгнө үү') to demand rigorous executive accountability regarding public expenditures.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Sharp political acoustic decoding.",
                        "onFailure": "The MP is pressing the minister on the real results of the transit budget."
                    },
                    "detailedGrammarNote": "Interpellation syntax in the State Great Khural (УИХ) relies on relative participial heads ('төсвийн тодотголд тусгагдсан хөрөнгө оруулалт') followed by an open interrogative ('ямар үр дүнд хүрсэн бэ').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Улсын төсвийн тодотголд тусгагдсан нийтийн тээврийн парк шинэчлэлийн хөрөнгө оруулалт бодит байдал дээр ямар үр дүнд хүрсэн бэ? Энэ талаар холбогдох сайд тодорхой тайлбар өгнө үү.",
                        "slowSpeechSynthesisText": "нийтийн тээврийн хөрөнгө оруулалт ямар үр дүнд хүрсэн бэ?",
                        "ipaTranscription": "/ʊɮsiːŋ tʰɵswiːŋ tʰɔtʰɔtʰɢɔɮtʰ tʰʊsɢəɡtsʰəŋ nʲiːtʰiːŋ tʰeːwriːŋ pʰarx ʃinətʃʰɮeɮiːŋ xɵrɵŋɡɵ ɔrʊːɮəɮtʰ pɔtʲitʰ pæːtəɮ tʰeːr jəmər ʊr tʰuntʰ xursəŋ pe/",
                        "speakerRole": "male_native",
                        "speechRate": 0.9,
                        "acousticEnvironment": "parliament_chamber"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Diplomatic Courtesy vs Underlying Acoustic Tension",
                    "modality": "PARLIAMENTARY_ACOUSTIC_DISSECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["diplomatic_irony_detection", "subtext_comprehension"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["эрхэм сайд", "үл ойлгогдох", "эргэлзээ"],
                    "prompt": "Listen to the committee chair's remark to a testifying official:\n\n'Эрхэм сайдын илтгэлийг сонслоо. Гэвч энэ удаагийн танилцуулсан тоо баримт нь өмнөх сарын Аудитын тайлантай илтэд зөрчилдөж байгааг юу гэж ойлгох вэ?'\n\nBehind the formal honorific 'Эрхэм сайд' (Honorable Minister), what subtext is the speaker conveying?",
                    "stimulusTextCyrillic": "Гэвч энэ удаагийн танилцуулсан тоо баримт нь өмнөх сарын Аудитын тайлантай илтэд зөрчилдөж байгааг юу гэж ойлгох вэ?",
                    "hint": "'Илтэд зөрчилдөх' means 'to blatantly contradict'.",
                    "options": [
                        {"id": "sub_distrust", "text": "Direct skepticism: The minister's reported numbers directly contradict the independent Audit Report, implying potential dishonesty or gross mismanagement.", "cyrillic": "Тоо баримт аудитын тайлантай зөрчилдөж буйг шүүмжлэх", "isCorrect": True, "explanation": "Correct! Blatant contradiction ('илтэд зөрчилдөх') between ministry figures and official audit reports signals severe parliamentary distrust."},
                        {"id": "sub_agreement", "text": "Unreserved agreement and endorsement of the ministry's financial management.", "cyrillic": "Дэмжих", "isCorrect": False, "explanation": "Incorrect. The speaker explicitly flags severe discrepancies."},
                        {"id": "sub_pardon", "text": "Granting the minister an exemption from submitting further accounting documentation.", "cyrillic": "Чөлөөлөх", "isCorrect": False, "explanation": "Incorrect. The speaker is holding the minister to account."}
                    ],
                    "correctAnswer": "Direct skepticism: The minister's reported numbers directly contradict the independent Audit Report, implying potential dishonesty or gross mismanagement.",
                    "acceptableAlternatives": ["Direct skepticism", "тоо баримт зөрчилдөж буйг илчлэх"],
                    "explanation": "High-register Mongolian parliamentary discourse wraps sharp evidentiary contradictions in strictly polite chancellery phrasing ('сонслоо... гэвч... юу гэж ойлгох вэ').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! You detected the underlying legislative confrontation beneath the diplomatic polish.",
                        "onFailure": "Notice the phrase 'илтэд зөрчилдөж байгааг' (blatantly contradicting)."
                    },
                    "detailedGrammarNote": "The rhetorical interrogative 'юу гэж ойлгох вэ?' (how are we to understand this?) serves as a conventionalized vehicle for aggressive institutional challenge in Khural debates.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Эрхэм сайдын илтгэлийг сонслоо. Гэвч энэ удаагийн танилцуулсан тоо баримт нь өмнөх сарын Аудитын тайлантай илтэд зөрчилдөж байгааг юу гэж ойлгох вэ?",
                        "slowSpeechSynthesisText": "тоо баримт Аудитын тайлантай илтэд зөрчилдөж байгааг юу гэж ойлгох вэ?",
                        "ipaTranscription": "/erxəm sæːtʰiːŋ iɮtʰɡəɮiːɡ sɔŋsɮɔː. kewtʃʰ en ʊtʰaːɡiːŋ tʰanʲiɮtsʰʊːɮsəŋ tʰɔː pʰarʲimtʰ nʲ ɵmnɵx sariːŋ aʊtʲitʰiːŋ tʰæːɮəŋtʰæː iɮtʰət tsɵrtʃʰiɮtətʃʰ pæːɢaːɡ jʊː ɡetʃʰ ɔeɮɢɔx we/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85,
                        "acousticEnvironment": "parliament_chamber"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Rhetorical Discourse Markers in High-Speed Legislative Debate",
                    "modality": "PARLIAMENTARY_ACOUSTIC_DISSECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["discourse_connectives", "transition_recognition"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Үүнтэй холбогдуулан", "Бодит байдал дээр", "Нэгдүгээрт"],
                    "prompt": "Listen to the MP transition between macro-policy and immediate fiscal repercussions:\n\n'Хуулийн үзэл баримтлал нь зөв боловч, бодит байдал дээр иргэдийн амьжиргаанд хүндээр тусаж байна. Үүнтэй холбогдуулан бид гурван асуудлыг нэн даруй шийдвэрлэх шаардлагатай.'\n\nWhat discourse function does the phrase 'Үүнтэй холбогдуулан' perform?",
                    "stimulusTextCyrillic": "Үүнтэй холбогдуулан бид гурван асуудлыг нэн даруй шийдвэрлэх шаардлагатай.",
                    "hint": "'Үүнтэй холбогдуулан' means 'In connection with this / Accordingly'.",
                    "options": [
                        {"id": "dm_transition", "text": "Logical transition: Connecting the stated practical problem to immediate concrete policy proposals.", "cyrillic": "Шалтгаант холбоос", "isCorrect": True, "explanation": "Correct! It links the preceding critique to an actionable agenda."},
                        {"id": "dm_contradiction", "text": "Rejecting the previous sentence as false and irrelevant.", "cyrillic": "Үгүйсгэх", "isCorrect": False, "explanation": "Incorrect. It builds upon, rather than refutes, the prior clause."},
                        {"id": "dm_closing", "text": "Signaling the conclusion of the speech and bidding farewell.", "cyrillic": "Төгсгөл", "isCorrect": False, "explanation": "Incorrect. It introduces three upcoming substantive proposals."}
                    ],
                    "correctAnswer": "Logical transition: Connecting the stated practical problem to immediate concrete policy proposals.",
                    "acceptableAlternatives": ["Logical transition", "холбох шилжилт"],
                    "explanation": "'Үүнтэй холбогдуулан' (literally: 'having connected with this') is the preeminent formal connective phrase bridging diagnosis to programmatic intervention.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'Үүнтэй холбогдуулан' guides parliamentary rhetoric flawlessly.",
                        "onFailure": "'Үүнтэй холбогдуулан' connects the issue to the proposed solution."
                    },
                    "detailedGrammarNote": "Dative-converb construction 'холбогдуулан' (causative of холбогдох) functions as a complex phrasal preposition governing preceding comitative demonstratives ('үүнтэй').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Үүнтэй холбогдуулан бид гурван асуудлыг нэн даруй шийдвэрлэх шаардлагатай байна.",
                        "slowSpeechSynthesisText": "Үүнтэй холбогдуулан гурван асуудал.",
                        "ipaTranscription": "/uːntʰeː xɔɮpɔɢtʰʊːɮəŋ pʰitʰ ɢʊrwəŋ asʊːtɮiːɡ neŋ tʰarʊːe ʃiːtwərɮəx ʃaːrtɮəɢtʰaː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Token Assembly: Standing Committee Legislative Motion",
                    "modality": "PARLIAMENTARY_ACOUSTIC_DISSECTION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["parliamentary_motion_assembly", "institutional_syntax"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["байнгын хороо", "тогтоолын төсөл", "санал хураалт"],
                    "prompt": "Arrange the tokens into the formal announcement made by the Standing Committee chair: 'The Standing Committee will now conduct a vote on the draft resolution':",
                    "wordTokens": ["санал", "Байнгын", "хураалт", "явуулна", "хороо", "төслөөр", "тогтоолын"],
                    "correctTokenOrder": ["Байнгын", "хороо", "тогтоолын", "төслөөр", "санал", "хураалт", "явуулна"],
                    "correctAnswer": "Байнгын хороо тогтоолын төслөөр санал хураалт явуулна",
                    "acceptableAlternatives": ["Байнгын хороо тогтоолын төслөөр санал хураалт явуулна.", "Байнгын хороо тогтоолын төслөөр санал хураалтыг явуулна"],
                    "hint": "Subject (Байнгын хороо) -> Instrumental bill (тогтоолын төслөөр) -> Object (санал хураалт) -> Verb (явуулна).",
                    "explanation": "Subject: 'Байнгын хороо' (Standing Committee) + Topic instrument: 'тогтоолын төслөөр' (on the draft resolution) + Compound predicate: 'санал хураалт явуулна' (will conduct a vote).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Authoritative parliamentary motion phrasing.",
                        "onFailure": "Order: Байнгын -> хороо -> тогтоолын -> төслөөр -> санал -> хураалт -> явуулна."
                    },
                    "detailedGrammarNote": "'Санал хураалт явуулах' (literally 'to conduct collecting of opinions') is the technical legal terminology for casting ballots in parliament.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Байнгын хороо тогтоолын төслөөр санал хураалт явуулна.",
                        "slowSpeechSynthesisText": "Байнгын хороо тогтоолын төслөөр санал хураалт явуулна.",
                        "ipaTranscription": "/pæːŋɡiːŋ xɔrɔː tʰɔxtʰɔːɮiːŋ tʰɵsɮɵːr sanaɮ xʊraːɮtʰ jəwʊːɮnə/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Insertion: Demanding Sanctions and Accountability",
                    "modality": "PARLIAMENTARY_ACOUSTIC_DISSECTION",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["parliamentary_legal_idiom", "cloze_accuracy"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хариуцлага тооцох"],
                    "prompt": "Complete the MP's demand for executive accountability:\n\n'Хууль зөрчсөн албан тушаалтнуудад хатуу сахилгын _________ шаардаж байна.' (We demand the imposition of strict disciplinary accountability on officials who broke the law.)",
                    "stimulusTextCyrillic": "сахилгын _________ тооцохыг шаардаж байна",
                    "hint": "Recall the abstract noun formed with -лага from the verb for being responsible/bearing duty.",
                    "correctAnswer": "хариуцлага",
                    "acceptableAlternatives": ["хариуцлага", "Хариуцлага"],
                    "explanation": "'Сахилгын хариуцлага тооцох' (to impose disciplinary accountability / sanctions) is the standard legal collocation.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'сахилгын хариуцлага' is the precise civil service disciplinary term.",
                        "onFailure": "Remember that 'сахилгын хариуцлага тооцох' means to hold someone strictly accountable."
                    },
                    "detailedGrammarNote": "'Тооцох' (literally to calculate/reckon) idiomatically combines with 'хариуцлага' to mean holding an actor accountable.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хууль зөрчсөн албан тушаалтнуудад хатуу сахилгын хариуцлага тооцохыг шаардаж байна.",
                        "slowSpeechSynthesisText": "сахилгын хариуцлага тооцох.",
                        "ipaTranscription": "/xʊːɮʲ tsɵrtʃʰsəŋ aɮpəŋ tʰʊʃaːɮtʰnʊːtət xatʰʊː saxʲiɮɢiːŋ xarʲʊtsʰɮəɢ tʰɔːtsʰɔxiːɡ ʃaːrtətʃʰ pæːn/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 14: les_b2_156_02_topic_vs_contrastive_topic_syntax
        {
            "lessonId": "les_b2_156_02_topic_vs_contrastive_topic_syntax",
            "exercises": [
                {
                    "exerciseId": "ex_b2_156_02_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Functional Contrast: Thematic 'Бол' vs Adversative 'Харин'",
                    "modality": "TOPIC_CONTRASTIVE_DISCOURSE",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["information_structure_analysis", "topic_marker_distinction"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["бол", "харин"],
                    "prompt": "In academic and political Mongolian, what is the precise syntactic and pragmatic difference between the discourse particles 'бол' and 'харин'?",
                    "hint": "'Бол' introduces or grounds the theme; 'харин' pivots to introduce a sharp contrasting argument.",
                    "options": [
                        {"id": "part_diff_correct", "text": "'Бол' marks the established topic / baseline theme (As for X...); 'харин' introduces a contrastive topic or adversative shift (Whereas Y / On the other hand, Y...).", "cyrillic": "бол бол сэдэв заах, харин бол эсрэгцүүлэн тодотгох", "isCorrect": True, "explanation": "Correct! 'Бол' establishes the frame of reference; 'харин' introduces the contrasting counterpart."},
                        {"id": "part_diff_wrong1", "text": "'Бол' is only used in colloquial slang, while 'харин' is only used in ancient poetry.", "cyrillic": "Хэрэглээний ялгаа", "isCorrect": False, "explanation": "Incorrect. Both are vital across all modern registers."},
                        {"id": "part_diff_wrong2", "text": "'Бол' is a past tense suffix, while 'харин' is a question particle.", "cyrillic": "Цагийн нөхцөл", "isCorrect": False, "explanation": "Incorrect. Neither is a verbal tense suffix."}
                    ],
                    "correctAnswer": "'Бол' marks the established topic / baseline theme (As for X...); 'харин' introduces a contrastive topic or adversative shift (Whereas Y / On the other hand, Y...).",
                    "acceptableAlternatives": ["бол marks topic, харин marks contrastive topic", "сэдэв ба эсрэгцүүлсэн сэдэв"],
                    "explanation": "'Бол' marks the topical ground of a proposition, while 'харин' serves as a contrastive discourse marker setting up an antithetical balance.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Masterful grasp of Mongolian information packaging.",
                        "onFailure": "'Бол' establishes the theme; 'харин' creates the contrast."
                    },
                    "detailedGrammarNote": "Originating from conditional converb 'болбол' (if it becomes), 'бол' grammaticalized into a universal topic marker. 'Харин' functions as a sentential conjunction marking contrastive focus.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Төсвийн орлого бол бүрдсэн, харин зарлага нь хэтэрсэн байна.",
                        "slowSpeechSynthesisText": "бол ба харин.",
                        "ipaTranscription": "/tʰɵswiːŋ ɔrɮɔɡ pɔɮ pʰurtsəŋ, xarʲiŋ tsarɮəɢ nʲ xitərsəŋ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_02_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Syntax Insertion: Balancing Economic Policy Antithesis",
                    "modality": "TOPIC_CONTRASTIVE_DISCOURSE",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["antithetical_discourse_construction", "topic_particle_placement"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["инфляц", "эдийн засгийн өсөлт"],
                    "prompt": "Insert 'бол' and 'харин' correctly into the economist's commentary:\n\n'Уул уурхайн салбарын орлого [_____] нэмэгдсэн, [_____] иргэдийн бодит орлого буурсан байна.'",
                    "hint": "First clause establishes the baseline topic with 'бол'; second clause pivots with 'харин'.",
                    "options": [
                        {"id": "pair_bol_harin", "text": "бол / харин ('...орлого бол нэмэгдсэн, харин иргэдийн...')", "cyrillic": "бол / харин", "isCorrect": True, "explanation": "Correct! 'Орлого бол' frames the mining revenue; 'харин иргэдийн' pivots to the contrasting decline in household income."},
                        {"id": "pair_harin_bol", "text": "харин / бол", "cyrillic": "харин / бол", "isCorrect": False, "explanation": "Incorrect. You cannot introduce a contrast before the baseline topic is framed."},
                        {"id": "pair_bol_bol", "text": "бол / бол", "cyrillic": "бол / бол", "isCorrect": False, "explanation": "Incorrect. Lacks the necessary adversative connective punch."}
                    ],
                    "correctAnswer": "бол / харин ('...орлого бол нэмэгдсэн, харин иргэдийн...')",
                    "acceptableAlternatives": ["бол / харин", "бол, харин"],
                    "explanation": "Canonical contrastive structure: Topic Clause (X бол...) followed by Contrast Clause (харин Y...).",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Seamless economic argumentation balance.",
                        "onFailure": "Use 'бол' in the first clause and 'харин' in the second."
                    },
                    "detailedGrammarNote": "When 'харин' opens the second clause, it immediately shifts the listener's attention to the counter-thematic reality.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Уул уурхайн салбарын орлого бол нэмэгдсэн, харин иргэдийн бодит орлого буурсан байна.",
                        "slowSpeechSynthesisText": "орлого бол нэмэгдсэн, харин бодит орлого буурсан.",
                        "ipaTranscription": "/ʊːɮ ʊːrxæːŋ saɮpriːŋ ɔrɮɔɡ pɔɮ nʲiməɡtsʰəŋ, xarʲiŋ irɡətiːŋ pɔtʲitʰ ɔrɮɔɡ pʊːrsəŋ pæːn/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_02_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Restructuring Complex Contrastive Clause",
                    "modality": "TOPIC_CONTRASTIVE_DISCOURSE",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["multi_clause_syntax", "contrastive_ordering"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["хуулийн төсөл", "үзэл баримтлал", "хэрэгжилт"],
                    "prompt": "Reconstruct this analytical editorial sentence: 'As for the concept of the bill, it is correct, but as for its implementation, problems remain':",
                    "wordTokens": ["зөв", "бол", "асуудал", "төслийн", "Хуулийн", "үзэл", "харин", "хэрэгжилтэд", "байна", "баримтлал"],
                    "correctTokenOrder": ["Хуулийн", "төслийн", "үзэл", "баримтлал", "бол", "зөв", "харин", "хэрэгжилтэд", "асуудал", "байна"],
                    "correctAnswer": "Хуулийн төслийн үзэл баримтлал бол зөв, харин хэрэгжилтэд асуудал байна",
                    "acceptableAlternatives": ["Хуулийн төслийн үзэл баримтлал бол зөв, харин хэрэгжилтэд асуудал байна.", "Хуулийн төслийн үзэл баримтлал бол зөв харин хэрэгжилтэд асуудал байна"],
                    "hint": "Structure the sentence by first topicalizing the bill's conceptual validity with 'бол', then introducing the practical shortcomings with the contrastive conjunction 'харин'.",
                    "explanation": "Topic phrase: 'Хуулийн төслийн үзэл баримтлал бол зөв,' + Contrast phrase: 'харин хэрэгжилтэд асуудал байна'.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Balanced complex topic sentence assembled.",
                        "onFailure": "Follow the sequence: Хуулийн төслийн үзэл баримтлал бол зөв, харин хэрэгжилтэд асуудал байна."
                    },
                    "detailedGrammarNote": "Notice how 'бол' attaches directly to the nominal head 'баримтлал', while 'харин' leads the entire counter-clause.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хуулийн төслийн үзэл баримтлал бол зөв, харин хэрэгжилтэд асуудал байна.",
                        "slowSpeechSynthesisText": "үзэл баримтлал бол зөв, харин хэрэгжилтэд асуудал байна.",
                        "ipaTranscription": "/xʊːɮʲiːŋ tʰɵsɮiːŋ utsəɮ pʰarʲimtʰɮəɮ pɔɮ tsɵw, xarʲiŋ xirəkʰtʃʰiɮtʰət asʊːtəɮ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_02_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Discourse Editing: Correcting Inverted Topic Particles",
                    "modality": "TOPIC_CONTRASTIVE_DISCOURSE",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["textual_editing", "discourse_coherence"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["газар тариалан", "мал аж ахуй"],
                    "prompt": "An editor found this flawed line in an agrarian policy article:\n\n'*Харин газар тариалангийн салбар гантай байсан, бол мал аж ахуйн салбар өсөлттэй гарлаа.'\n\nWhy is this sentence stylistically inverted, and how should it be corrected?",
                    "hint": "'Харин' cannot precede an un-contrasted initial topic; 'бол' belongs in the first clause.",
                    "options": [
                        {"id": "edit_inverted", "text": "'Харин' was erroneously placed at the start of the first clause, and 'бол' was misplaced in the second. It must be: 'Газар тариалангийн салбар бол гантай байсан, харин мал аж ахуйн салбар өсөлттэй гарлаа.'", "cyrillic": "Байрыг нь солин засах", "isCorrect": True, "explanation": "Correct! Swapping them restores logical information hierarchy: Topic first (салбар бол...), Contrast second (харин...)."},
                        {"id": "edit_delete", "text": "Both words should be deleted because Mongolian syntax forbids all connectives.", "cyrillic": "Хасах", "isCorrect": False, "explanation": "Incorrect. Discourse particles are essential for coherent prose."},
                        {"id": "edit_tense", "text": "The error is only in the verb 'байсан', which should be future tense.", "cyrillic": "Цагийн алдаа", "isCorrect": False, "explanation": "Incorrect. The primary flaw is information packaging inversion."}
                    ],
                    "correctAnswer": "'Харин' was erroneously placed at the start of the first clause, and 'бол' was misplaced in the second. It must be: 'Газар тариалангийн салбар бол гантай байсан, харин мал аж ахуйн салбар өсөлттэй гарлаа.'",
                    "acceptableAlternatives": ["Газар тариалангийн салбар бол гантай байсан, харин мал аж ахуйн салбар өсөлттэй гарлаа."],
                    "explanation": "Topic markers must follow thematic order. You establish the first subject with 'бол', then introduce the antithetical subject with 'харин'.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Critical syntactic and rhetorical proofreading executed.",
                        "onFailure": "Swap 'харин' and 'бол' to preserve topic -> contrast ordering."
                    },
                    "detailedGrammarNote": "Placing 'харин' at the absolute beginning of an isolated text is only permissible if answering an explicit prior question from an interlocutor.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Газар тариалангийн салбар бол гантай байсан, харин мал аж ахуйн салбар өсөлттэй гарлаа.",
                        "slowSpeechSynthesisText": "салбар бол гантай байсан, харин мал аж ахуй өсөлттэй гарлаа.",
                        "ipaTranscription": "/ɢatsʰər tʰarʲiaɮəŋɡiːŋ saɮpər pɔɮ ɢəŋtʰæː pæːsəŋ, xarʲiŋ maɮ atʃʰ axʊeːŋ saɮpər ɵsɵɮtʰtʰeː ɢarɮaː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_156_02_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Nuance: Restricting Conditional vs Topic 'Бол'",
                    "modality": "TOPIC_CONTRASTIVE_DISCOURSE",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["functional_ambiguity_resolution", "cloze_insertion"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["хэрэв", "бол"],
                    "prompt": "In conditional clauses introduced by 'хэрэв' (if), 'бол' functions as the conditional apodosis anchor. Complete the sentence:\n\n'Хэрэв хууль батлагдвал бид үүнийг дагаж мөрдөнө. Харин батлагдахгүй ______ бид дахин өргөн барина.' (If the law is passed we will comply. But if it is not passed, we will re-submit.)",
                    "stimulusTextCyrillic": "Харин батлагдахгүй ______ бид дахин өргөн барина.",
                    "hint": "Insert the monosyllabic particle that creates a conditional protasis ('if not...') following a negative future-present participle.",
                    "correctAnswer": "бол",
                    "acceptableAlternatives": ["бол", "Бол"],
                    "explanation": "After negative verbal adjectives ('батлагдахгүй'), 'бол' functions as the conditional link ('if it is not passed').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'бол' acts as the conditional anchor after the negative participle.",
                        "onFailure": "Remember that 'бол' functions as the conditional anchor after '-хгүй'."
                    },
                    "detailedGrammarNote": "While 'бол' after nouns acts as a topic marker, following negative participles like '-хгүй' it acts as a conditional conjunction meaning 'if'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Харин батлагдахгүй бол бид дахин өргөн барина.",
                        "slowSpeechSynthesisText": "батлагдахгүй бол бид дахин өргөн барина.",
                        "ipaTranscription": "/xarʲiŋ pʰatʰɮəɢtəxɢuː pɔɮ pʰitʰ tʰaxʲiŋ ɵrɡɵŋ pʰarʲin/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 15: les_b2_166_06_b2_sec01_culminating_mastery_capstone
        {
            "lessonId": "les_b2_166_06_b2_sec01_culminating_mastery_capstone",
            "exercises": [
                {
                    "exerciseId": "ex_b2_166_06_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Multi-Source Policy Synthesis: Smog Abatement Dossier",
                    "modality": "MUNICIPAL_POLICY_CAPSTONE",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["policy_synthesis", "cross_document_evaluation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["агаарын бохирдол", "гэр хороолол", "дэд бүтэц", "сайжруулсан түлш"],
                    "prompt": "Synthesize these two divergent policy reports on Ulaanbaatar winter air pollution:\n\n[Эх сурвалж А - Хотын захиргаа]: 'Сайжруулсан түлшний чанар стандартыг чангатгаж, түгээлтийн сүлжээг өргөтгөснөөр утааг богино хугацаанд 30% бууруулах боломжтой.'\n[Эх сурвалж Б - Эдийн засгийн хүрээлэн]: 'Сайжруулсан түлш бол түр зуурын аргацаасан арга хэмжээ мөн. Гэр хорооллыг орон сууцжуулж, дулааны цахилгаан станцын шугамд бүрэн холбохоос нааш утааны асуудал сууриараа шийдэгдэхгүй.'\n\nWhich synthesis statement accurately integrates both perspectives?",
                    "hint": "Distinguish short-term mitigation (fuel standards) from long-term structural overhaul (housing infrastructure).",
                    "options": [
                        {"id": "synth_balanced", "text": "While enhanced fuel distribution provides an immediate short-term mitigation measure, permanent eradication of air pollution fundamentally requires capital-intensive infrastructure and comprehensive ger district housing re-development.", "cyrillic": "Богино болон урт хугацааны цогц бодлого", "isCorrect": True, "explanation": "Correct! Reconciles Source A's short-term mitigation with Source B's structural critique."},
                        {"id": "synth_market_only", "text": "Source A and Source B both recommend that fuel prices be deregulated immediately and left entirely to private market competition without municipal intervention.", "cyrillic": "Зах зээлийн зохицуулалтад бүрэн даатгах", "isCorrect": False, "explanation": "Incorrect. Neither source advocates unregulated market mechanisms; both call for specific public infrastructure or regulatory standards."},
                        {"id": "synth_relocation_only", "text": "Both reports conclude that residential fuel improvements are futile and suggest relocating the entire ger district population outside the city basin within two years.", "cyrillic": "Хүн амыг нийслэлээс нүүлгэн шилжүүлэх", "isCorrect": False, "explanation": "Incorrect. Neither report advocates forced or mass relocation; they focus on on-site grid connection, housing redevelopment, and cleaner fuels."}
                    ],
                    "correctAnswer": "While enhanced fuel distribution provides an immediate short-term mitigation measure, permanent eradication of air pollution fundamentally requires capital-intensive infrastructure and comprehensive ger district housing re-development.",
                    "acceptableAlternatives": ["While enhanced fuel distribution provides an immediate short-term mitigation measure", "Богино болон урт хугацааны цогц бодлого"],
                    "explanation": "Mastery synthesis demands extracting temporal and strategic nuances: immediate fuel standards vs long-term urban residential engineering.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Sophisticated multi-source policy synthesis.",
                        "onFailure": "Integrate both: short-term fuel controls + long-term infrastructure."
                    },
                    "detailedGrammarNote": "Synthesizing contrasting institutional sources requires concessive framing ('хэдий тийм боловч... суурь шийдэл нь...').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Сайжруулсан түлш бол түр зуурын арга хэмжээ бөгөөд суурь шийдэл нь гэр хорооллын дэд бүтцийг хөгжүүлэх явдал юм.",
                        "slowSpeechSynthesisText": "суурь шийдэл нь гэр хорооллын дэд бүтэц юм.",
                        "ipaTranscription": "/sæːtʃʰrʊːɮsəŋ tʰuɮʃ pɔɮ tʰur tsʊːriːŋ arɢə xitʃʰeː pɵɡɵːtʰ sʊːrʲ ʃiːtəɮ nʲ ɡer xɔrɔːɮɮiːŋ tʰetʰ pʊtsiːɡ xɵɡtʃuːɮəx jawtəɮ jʊm/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_166_06_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Argumentative Counter-Framing in Urban Transit Policy",
                    "modality": "MUNICIPAL_POLICY_CAPSTONE",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["counterargument_formulation", "policy_critique"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["түгжрэл", "автомашины дугаарын хязгаарлалт", "нийтийн тээвэр"],
                    "prompt": "The municipal administration argues: 'Хувийн автомашины тэгш, сондгой дугаарын хязгаарлалтыг ажлын 5 өдөр болгон чангатгавал замын түгжрэл бүрэн шийдэгдэнэ.' (If license plate rationing is expanded to all 5 weekdays, traffic congestion will be completely solved.)\n\nWhich counterargument exposes the underlying systemic weakness using high-register discourse?",
                    "hint": "Highlight that restricting cars without first expanding reliable bus alternatives merely strands citizens and fuels informal unlicensed taxi activity.",
                    "options": [
                        {"id": "counter_systemic", "text": "Нийтийн тээврийн хүртээмж, чанарыг дорвитой сайжруулахгүйгээр зөвхөн захиргааны хориг арга хэмжээ авах нь иргэдийн хөдөлгөөнийг боогдуулж, эдийн засгийн идэвхийг сааруулах сөрөг үргавартай. (Imposing administrative restrictions without radically improving the accessibility and quality of public transit will merely restrict citizen mobility and depress economic activity.)", "cyrillic": "Нийтийн тээврийг сайжруулахгүйгээр захиргааны хориг тавих нь сөрөг үргавартай", "isCorrect": True, "explanation": "Correct! Systemic counterargument linking administrative over-regulation to citizen mobility constraints and economic paralysis."},
                        {"id": "counter_fiscal", "text": "Замын хураамжийг нэмэгдүүлснээр төсөвт төвлөрөх хөрөнгө өсөж, шинэ зам тавих боломж бүрдэнэ гэж үзэх нь илүү оновчтой. (It is more appropriate to argue that raising road tolls will increase budget revenues and enable building new roadways.)", "cyrillic": "Замын хураамжийг нэмэгдүүлж шинэ зам барих", "isCorrect": False, "explanation": "Incorrect. This addresses supply-side highway financing rather than directly critiquing the systemic mobility impact of weekday plate rationing."},
                        {"id": "counter_telework", "text": "Төрийн бүх байгууллагын ажилтнуудыг зөвхөн цахимаар ажиллуулбал замын ачаалал шууд арилна. (If all government personnel transition exclusively to telework, traffic congestion will instantly dissipate.)", "cyrillic": "Төрийн байгууллагыг бүрэн зайнаас ажиллуулах", "isCorrect": False, "explanation": "Incorrect. This proposes a single sector shift that does not address broad public transit infrastructure or commercial freight movements."}
                    ],
                    "correctAnswer": "Нийтийн тээврийн хүртээмж, чанарыг дорвитой сайжруулахгүйгээр зөвхөн захиргааны хориг арга хэмжээ авах нь иргэдийн хөдөлгөөнийг боогдуулж, эдийн засгийн идэвхийг сааруулах сөрөг үргавартай. (Imposing administrative restrictions without radically improving the accessibility and quality of public transit will merely restrict citizen mobility and depress economic activity.)",
                    "acceptableAlternatives": ["Нийтийн тээврийн хүртээмжийг сайжруулахгүйгээр захиргааны хориг тавих нь сөрөг үргавартай"],
                    "explanation": "High-level counter-framing relies on causal converbs ('сайжруулахгүйгээр' = without improving) and formal terminology ('захиргааны хориг арга хэмжээ', 'сөрөг үр дагавар').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Incisive, evidence-based policy counterargument.",
                        "onFailure": "Frame the systemic counterargument around public transit deficits."
                    },
                    "detailedGrammarNote": "Negative converb -хгүйгээр⁴ ('сайжруулахгүйгээр') sets up a conditional prerequisite: doing A without first ensuring B will produce failure.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Нийтийн тээврийн хүртээмжийг сайжруулахгүйгээр захиргааны хориг тавих нь сөрөг үр дагавартай.",
                        "slowSpeechSynthesisText": "захиргааны хориг арга хэмжээ авах нь сөрөг үр дагавартай.",
                        "ipaTranscription": "/nʲiːtʰiːŋ tʰeːwriːŋ xʊrtʰeːmtʃʰiːɡ sæːtʃʰrʊːɮəxɢuːɡeːr tsaxʲirɢaːniː xɔrʲiɡ arɢə xitʃʰeː awəx nʲ sɵrɵɡ ʊr tʰaɢəwərtʰæː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_b2_166_06_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Urban Decentralization Policy Motto",
                    "modality": "MUNICIPAL_POLICY_CAPSTONE",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["urban_policy_syntax", "motto_formulation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["төвлөрлийг сааруулах", "дэд төв", "хөгжил"],
                    "prompt": "Reconstruct this strategic municipal planning objective: 'Decentralizing the city by establishing sub-centers is the key to sustainable urban development':",
                    "wordTokens": ["дэд", "хотыг", "байгуулан", "төв", "түлхүүр", "төвлөрлийг", "мөн", "тогтвортой", "сааруулах", "нь"],
                    "correctTokenOrder": ["дэд", "төв", "байгуулан", "хотыг", "төвлөрлийг", "сааруулах", "нь", "тогтвортой", "түлхүүр", "мөн"],
                    "correctAnswer": "дэд төв байгуулан хотыг төвлөрлийг сааруулах нь тогтвортой түлхүүр мөн",
                    "acceptableAlternatives": ["дэд төв байгуулан хотын төвлөрлийг сааруулах нь тогтвортой хөгжлийн түлхүүр мөн", "Дэд төв байгуулан хотын төвлөрлийг сааруулах нь тогтвортой хөгжлийн түлхүүр мөн."],
                    "hint": "By building sub-centers (дэд төв байгуулан) -> decentralizing the city (хотын төвлөрлийг сааруулах нь) -> key (түлхүүр мөн).",
                    "explanation": "'Дэд төв байгуулан' (establishing sub-centers) + 'хотын төвлөрлийг сааруулах нь' (decentralizing the city) + 'тогтвортой хөгжлийн түлхүүр мөн' (is the key to sustainable development).",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! High-register urban development policy objective assembled.",
                        "onFailure": "Sequence: дэд төв байгуулан -> хотын төвлөрлийг сааруулах нь -> түлхүүр мөн."
                    },
                    "detailedGrammarNote": "'Төвлөрлийг сааруулах' (literally 'to weaken the concentration / decentralize') is the canonical modern municipal planning term for urban decongestion.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Дэд төв байгуулан хотын төвлөрлийг сааруулах нь тогтвортой хөгжлийн түлхүүр мөн.",
                        "slowSpeechSynthesisText": "хотын төвлөрлийг сааруулах нь тогтвортой хөгжлийн түлхүүр.",
                        "ipaTranscription": "/tʰetʰ tʰɵw pæːɢʊːɮəŋ xɔtʰiːŋ tʰɵwɮɵrɮiːɡ saːrʊːɮəx nʲ tʰɔxtʰwɔrtʰɔe xɵɡtʃʰɮiːŋ tʰuɮxuːr mɵŋ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_b2_166_06_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Insertion: Public Green Space Mandate",
                    "modality": "MUNICIPAL_POLICY_CAPSTONE",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["municipal_regulation_lexicon", "cloze_accuracy"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ногоон байгууламж", "нэмэгдүүлэх"],
                    "prompt": "Fill in the standard administrative compound meaning 'green areas / landscaping' in this city building code:\n\n'Шинээр баригдах орон сууцны хотхоны 30-аас доошгүй хувьд _______ талбай төлөвлөх үүрэгтэй.' (Required to plan not less than 30% of new residential complexes as green areas.)",
                    "stimulusTextCyrillic": "30-аас доошгүй хувьд _______ талбай төлөвлөх",
                    "hint": "Recall the basic ecological color modifier applied to municipal lawns, parks, and tree plantings.",
                    "correctAnswer": "ногоон",
                    "acceptableAlternatives": ["ногоон", "Ногоон"],
                    "explanation": "'Ногоон байгууламж / ногоон талбай' (green spaces, urban landscaping) is the statutory term in Mongolian building and planning codes.",
                    "learnerFeedback": {
                        "onSuccess": "Гайхалтай! 'ногоон' талбай correctly inserted.",
                        "onFailure": "Remember that 'ногоон талбай' is the standard legal term for urban green space."
                    },
                    "detailedGrammarNote": "'Ногоон байгууламж' encompasses parks, lawns, urban foliage, and eco-buffer strips under Ulaanbaatar municipal standards.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Орон сууцны хотхоны гучин хувьд ногоон талбай төлөвлөх үүрэгтэй.",
                        "slowSpeechSynthesisText": "ногоон талбай төлөвлөх үүрэгтэй.",
                        "ipaTranscription": "/ɔrɔŋ sʊːtsʰniː xɔtʰxɔniː ɢʊtsʰəŋ xʊwʲtʰ nɔɢɔːŋ tʰaɮpæː tʰɵɮɵwɮɵx ʊːrəkʰtʰeː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_b2_166_06_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Capstone Holistic Policy Briefing Rubric",
                    "modality": "MUNICIPAL_POLICY_CAPSTONE",
                    "interactionPattern": "OPEN_RESPONSE_RUBRIC",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["capstone_policy_defense", "evidence_qualification"],
                    "grammarTargets": ["gram_b2_topic_bol_vs_contrastive_harin"],
                    "vocabularyTargets": ["бодлогын зөвлөмж", "төсөв", "хэрэгжүүлэх механизм"],
                    "prompt": "Read the learner's submitted policy memorandum on Ulaanbaatar waste management:\n\n'БОДЛОГЫН САНАМЖ БИЧИГ:\n1. Асуудлын тодорхойлолт: Нийслэлийн хэмжээнд жилд үүсэж буй 1.4 сая тонн хог хаягдлын 90 гаруй хувийг ил задгай булж байна. Энэ нь хөрс, гүний усыг ноцтой бохирдуулж байна.\n2. Сөрөг тал ба саад: Хог ангилан ялгах соёл бол төлөвшөөгүй, харин дахин боловсруулах үйлдвэрүүдийн хүчин чадал хангалтгүй байна.\n3. Шийдлийн хувилбар: Төрийн болон хувийн хэвшлийн түншлэлээр хог дахин боловсруулах эко парк байгуулж, ангилан ялгасан иргэдэд урамшуулал олгох механизмыг нэвтрүүлэх нь хамгийн оновчтой шийдэл мөн.'\n\nEvaluate this memorandum against criteria of: 1. Empirical diagnosis, 2. Use of contrastive topic markers (бол vs харин), 3. Feasibility of policy recommendation.",
                    "stimulusTextCyrillic": "БОДЛОГЫН САНАМЖ БИЧИГ ... Хог ангилан ялгах соёл бол төлөвшөөгүй, харин дахин боловсруулах үйлдвэрүүд...",
                    "correctAnswer": "Exemplary policy memorandum featuring quantitative diagnosis (1.4 million tons, 90%), flawless contrastive topic balance (соёл бол... харин хүчин чадал...), and viable public-private partnership recommendation.",
                    "acceptableAlternatives": ["Exemplary policy memorandum", "Шалгуурыг бүрэн хангасан", "Meets all criteria"],
                    "hint": "Check whether concrete numbers are cited, whether 'бол/харин' are used correctly, and whether actionable solutions are proposed.",
                    "explanation": "The memo meets all B2 capstone criteria: empirical ground (1.4 million tons), syntactic mastery of topic vs contrast ('соёл бол... харин...'), and realistic institutional mechanics (PPP eco-park).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Rigorous analytical evaluation of B2 capstone policy dossier.",
                        "onFailure": "Verify empirical evidence, 'бол/харин' contrast, and solution feasibility."
                    },
                    "detailedGrammarNote": "A 'Бодлогын санамж бичиг' (Policy Brief / Memorandum) represents the culmination of B2 civic and professional operational competence.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэхүү бодлогын санамж бичиг нь шалгуур үзүүлэлтийг бүрэн хангаж байна.",
                        "slowSpeechSynthesisText": "бодлогын санамж бичгийн үнэлгээ.",
                        "ipaTranscription": "/enəxuː pɔtɮɔɢiːŋ sanəmtʃʰ pʰitʃʰiɡ nʲ ʃaɮɢʊːr uutsʊːɮəɮtʰiːɡ pʰurəŋ xaŋɢətʃʰ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "RUBRIC_CRITERIA",
                        "rubricCriteria": [
                            {"criterion": "Empirical Problem Diagnosis", "points": 35, "description": "Accurately notes quantified data (1.4 million tons, 90% landfill)."},
                            {"criterion": "Contrastive Discourse Control", "points": 35, "description": "Verifies correct usage of 'бол' (culture) vs 'харин' (industrial capacity)."},
                            {"criterion": "Actionable Mechanism Feasibility", "points": 30, "description": "Confirms realistic PPP mechanism and citizen incentive structures."}
                        ]
                    }
                }
            ]
        }
    ]
