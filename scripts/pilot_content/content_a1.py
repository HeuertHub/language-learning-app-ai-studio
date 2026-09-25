#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_a1_16_01_canonical_sov_architecture (Grammar Introduction)
2. les_a1_16_02_formal_time_greetings_mori (Vocabulary Introduction)
3. les_a1_16_05_reception_desk_simulation (Dialogue Work)
"""

def get_a1_exercises():
    return [
        # LESSON 4: les_a1_16_01_canonical_sov_architecture
        {
            "lessonId": "les_a1_16_01_canonical_sov_architecture",
            "exercises": [
                {
                    "exerciseId": "ex_a1_16_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Assembling Canonical SOV Word Order",
                    "modality": "SYNTAX_WORD_ORDERING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["sov_sentence_construction", "predicate_clause_final_placement"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["би", "ном", "уншина"],
                    "prompt": "Arrange the scrambled word tokens into a grammatically correct Mongolian declarative sentence: 'I will read a book'.",
                    "contextSentence": "Subject -> Object -> Finite Verb",
                    "wordTokens": ["уншина", "би", "ном"],
                    "correctTokenOrder": ["би", "ном", "уншина"],
                    "correctAnswer": "би ном уншина",
                    "acceptableAlternatives": ["Би ном уншина.", "Би ном уншина"],
                    "hint": "In Mongolian, the subject comes first, the direct object comes second, and the verb always stands at the end.",
                    "explanation": "Mongolian is strictly head-final with canonical Subject-Object-Verb (SOV) order. 'Би' (Subject) precedes 'ном' (Object), and 'уншина' (Verb) must terminate the clause.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! You placed the verb at the clause-final anchor.",
                        "onFailure": "Remember: Subject (Би) + Object (ном) + Verb (уншина)."
                    },
                    "detailedGrammarNote": "Modern Mongolian strictly prohibits English-style SVO ordering (*Би уншина ном). The finite predicate holds the absolute right edge of the sentence.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би ном уншина.",
                        "slowSpeechSynthesisText": "Би ном уншина.",
                        "ipaTranscription": "/pʰi nɔm ʊŋʃən/",
                        "speakerRole": "narrator",
                        "speechRate": 0.9
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Locating the Finite Predicate Slot",
                    "modality": "SYNTAX_WORD_ORDERING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["predicate_identification", "clause_architecture"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["багш", "сургууль", "ирнэ"],
                    "prompt": "In the sentence 'Багш маргааш сургууль дээр ирнэ' (The teacher will come to school tomorrow), which word occupies the finite predicate slot?",
                    "stimulusTextCyrillic": "Багш маргааш сургууль дээр ирнэ.",
                    "hint": "Look at the final word of the sentence that conveys the action/tense.",
                    "options": [
                        {"id": "opt_irne", "text": "ирнэ (will come) - Clause-final verb", "cyrillic": "ирнэ", "isCorrect": True, "explanation": "Correct! 'Ирнэ' is the finite verb in clause-final position."},
                        {"id": "opt_bagsh", "text": "багш (teacher) - Subject", "cyrillic": "багш", "isCorrect": False, "explanation": "Incorrect. 'Багш' is the subject in initial position."},
                        {"id": "opt_margaash", "text": "маргааш (tomorrow) - Temporal adverbial", "cyrillic": "маргааш", "isCorrect": False, "explanation": "Incorrect. 'Маргааш' is a temporal modifier."},
                        {"id": "opt_surguuli", "text": "сургууль дээр (at school) - Locative adverbial", "cyrillic": "сургууль дээр", "isCorrect": False, "explanation": "Incorrect. This is a postpositional locative phrase."}
                    ],
                    "correctAnswer": "ирнэ (will come) - Clause-final verb",
                    "acceptableAlternatives": ["ирнэ", "ирнэ."],
                    "explanation": "The finite verb 'ирнэ' (comes/will come) concludes the clause, serving as the syntactic head to which all preceding arguments link.",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! 'Ирнэ' is the predicate.",
                        "onFailure": "The predicate in Mongolian is the verb at the very end: 'ирнэ'."
                    },
                    "detailedGrammarNote": "Because Mongolian is head-final, modifiers (temporal, locative, direct objects) always precede the verb head, and attributive adjectives precede the noun head.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Багш маргааш сургууль дээр ирнэ.",
                        "slowSpeechSynthesisText": "Багш маргааш сургууль дээр ирнэ.",
                        "ipaTranscription": "/paɢʃ marɢaːʃ sʊrɢʊːɮ ter irən/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Head-Final Modifier Placement (Adjective + Noun)",
                    "modality": "SYNTAX_WORD_ORDERING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["modifier_head_alignment", "nominal_phrase_syntax"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["том", "гэр", "энэ"],
                    "prompt": "Which phrase correctly demonstrates the rule that demonstratives and descriptive adjectives must precede the head noun?",
                    "stimulusTextCyrillic": "Энэ том гэр",
                    "hint": "Demonstrative ('this') + Adjective ('big') + Noun ('ger').",
                    "options": [
                        {"id": "opt_correct", "text": "Энэ том гэр (This big ger)", "cyrillic": "Энэ том гэр", "isCorrect": True, "explanation": "Correct! Demonstrative 'Энэ' + Adjective 'том' + Head noun 'гэр'."},
                        {"id": "opt_wrong1", "text": "*Гэр том энэ", "cyrillic": "*Гэр том энэ", "isCorrect": False, "explanation": "Incorrect. Placing the noun before its modifiers violates head-final structure."},
                        {"id": "opt_wrong2", "text": "*Том гэр энэ", "cyrillic": "*Том гэр энэ", "isCorrect": False, "explanation": "Incorrect. The demonstrative 'энэ' must precede the adjective."},
                        {"id": "opt_wrong3", "text": "*Гэр энэ том", "cyrillic": "*Гэр энэ том", "isCorrect": False, "explanation": "Incorrect. Unnatural word order."}
                    ],
                    "correctAnswer": "Энэ том гэр (This big ger)",
                    "acceptableAlternatives": ["Энэ том гэр"],
                    "explanation": "In Mongolian noun phrases, the hierarchy is strictly Demonstrative -> Adjective -> Head Noun ('Энэ том гэр').",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Modifiers always precede the noun in Mongolian.",
                        "onFailure": "Remember: Demonstrative first, adjective second, noun last (Энэ том гэр)."
                    },
                    "detailedGrammarNote": "Unlike Romance languages where adjectives often follow the noun, Mongolic syntax requires all attributes to branch to the left of their head noun.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэ том гэр",
                        "slowSpeechSynthesisText": "Энэ том гэр",
                        "ipaTranscription": "/en tʰɔm ɡer/",
                        "speakerRole": "narrator",
                        "speechRate": 0.9
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Assembling Complex Clause with Temporal & Locative Arguments",
                    "modality": "SYNTAX_WORD_ORDERING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["complex_clause_sequencing", "argument_ordering"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["Дорж", "өнөөдөр", "хотод", "ирнэ"],
                    "prompt": "Reconstruct the scrambled words into a standard sentence: 'Dorj will arrive in the city today'.",
                    "wordTokens": ["ирнэ", "хотод", "Дорж", "өнөөдөр"],
                    "correctTokenOrder": ["Дорж", "өнөөдөр", "хотод", "ирнэ"],
                    "correctAnswer": "Дорж өнөөдөр хотод ирнэ",
                    "acceptableAlternatives": ["Өнөөдөр Дорж хотод ирнэ", "Дорж өнөөдөр хотод ирнэ."],
                    "hint": "Subject (Дорж) -> Time (өнөөдөр) -> Location (хотод) -> Verb (ирнэ).",
                    "explanation": "Standard neutral Mongolian order is Subject + Temporal Adverbial + Locative Adverbial + Verb: 'Дорж өнөөдөр хотод ирнэ'.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Perfect clause architecture.",
                        "onFailure": "Follow the sequence: Дорж -> өнөөдөр -> хотод -> ирнэ."
                    },
                    "detailedGrammarNote": "Time expressions may optionally topicalize to the very front ('Өнөөдөр Дорж хотод ирнэ'), but the verb 'ирнэ' must unconditionally remain at the end.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Дорж өнөөдөр хотод ирнэ.",
                        "slowSpeechSynthesisText": "Дорж өнөөдөр хотод ирнэ.",
                        "ipaTranscription": "/tɔrtʃ ɵnɵːtər xɔtʰət irən/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Syntax Error Spotting: SVO Transfer Interference",
                    "modality": "SYNTAX_WORD_ORDERING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["syntax_error_detection", "language_transfer_prevention"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["цай", "ууна", "би"],
                    "prompt": "A foreign learner wrote: '*Би ууна цай' (attempting to say 'I drink tea'). What is the error and how should it be corrected?",
                    "stimulusTextCyrillic": "*Би ууна цай -> Би цай ууна",
                    "hint": "The direct object 'цай' must come before the verb 'ууна'.",
                    "options": [
                        {"id": "err_1", "text": "The verb 'ууна' was placed before the object; it should be 'Би цай ууна'.", "cyrillic": "Би цай ууна", "isCorrect": True, "explanation": "Correct! English SVO was incorrectly transferred. Mongolian requires SOV: Би цай ууна."},
                        {"id": "err_2", "text": "The pronoun 'Би' is missing an accusative suffix.", "cyrillic": "Намайг", "isCorrect": False, "explanation": "Incorrect. 'Би' is the subject, correctly in the nominative."},
                        {"id": "err_3", "text": "'Цай' is a loanword and cannot take an object position.", "cyrillic": "Цай", "isCorrect": False, "explanation": "Incorrect. 'Цай' is perfectly normal native vocabulary."}
                    ],
                    "correctAnswer": "The verb 'ууна' was placed before the object; it should be 'Би цай ууна'.",
                    "acceptableAlternatives": ["Би цай ууна", "The verb 'ууна' was placed before the object"],
                    "explanation": "In English, verbs precede their objects (I drink tea), but in Mongolian, the object must precede the verb: 'Би цай ууна'.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! SVO must be converted to SOV: 'Би цай ууна'.",
                        "onFailure": "Mongolian always puts the object before the verb: Би цай ууна."
                    },
                    "detailedGrammarNote": "SVO transfer error is the single most common grammatical slip for beginning Mongolian learners from Indo-European language backgrounds.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би цай ууна.",
                        "slowSpeechSynthesisText": "Би цай ууна.",
                        "ipaTranscription": "/pʰi tsʰæː ʊːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 5: les_a1_16_02_formal_time_greetings_mori
        {
            "lessonId": "les_a1_16_02_formal_time_greetings_mori",
            "exercises": [
                {
                    "exerciseId": "ex_a1_16_02_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Diurnal Greeting Matching: Time of Day to Salutation",
                    "modality": "SALUTATION_REGISTER_MATCH",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "REMEMBER_RECOGNIZE",
                    "skillTargets": ["temporal_greeting_selection", "social_etiquette"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Өглөөний мэнд", "Өдрийн мэнд", "Оройн мэнд"],
                    "prompt": "It is 09:00 AM and you arrive at a Mongolian corporate office. What is the appropriate formal greeting?",
                    "stimulusTextCyrillic": "09:00 AM",
                    "hint": "'Өглөө' means morning.",
                    "options": [
                        {"id": "opt_ogloo", "text": "Өглөөний мэнд хүргэе! (Good morning!)", "cyrillic": "Өглөөний мэнд хүргэе!", "isCorrect": True, "explanation": "Correct! 'Өглөөний мэнд' is the polite greeting for the morning hours."},
                        {"id": "opt_odor", "text": "Өдрийн мэнд хүргэе! (Good afternoon!)", "cyrillic": "Өдрийн мэнд хүргэе!", "isCorrect": False, "explanation": "Incorrect. 'Өдрийн мэнд' is used around midday and afternoon (12:00-17:00)."},
                        {"id": "opt_oroi", "text": "Оройн мэнд хүргэе! (Good evening!)", "cyrillic": "Оройн мэнд хүргэе!", "isCorrect": False, "explanation": "Incorrect. 'Оройн мэнд' is used in the evening (after 18:00)."},
                        {"id": "opt_amraarai", "text": "Сайхан амраарай! (Have a good rest / Good night!)", "cyrillic": "Сайхан амраарай!", "isCorrect": False, "explanation": "Incorrect. This is a parting wish before sleeping."}
                    ],
                    "correctAnswer": "Өглөөний мэнд хүргэе! (Good morning!)",
                    "acceptableAlternatives": ["Өглөөний мэнд хүргэе!", "Өглөөний мэнд"],
                    "explanation": "'Өглөөний мэнд хүргэе' (literally: 'I deliver the peace/wellbeing of the morning') is the standard formal greeting before noon.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'Өглөөний мэнд хүргэе' is used in the morning.",
                        "onFailure": "At 09:00 AM use 'Өглөөний мэнд хүргэе'."
                    },
                    "detailedGrammarNote": "The greeting uses the genitive form of the time noun (өглөө -> өглөөний, өдөр -> өдрийн, орой -> оройн) modifying 'мэнд' (wellbeing), followed optionally by the performative verb 'хүргэе' (let me convey).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Өглөөний мэнд хүргэе!",
                        "slowSpeechSynthesisText": "Өглөөний мэнд хүргэе!",
                        "ipaTranscription": "/ɵɡɮɵːniː mentʰ xʊrɡiː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_02_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Formal Reciprocal Greeting Response",
                    "modality": "SALUTATION_REGISTER_MATCH",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["reciprocal_greeting_response", "polite_register_control"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Өдрийн мэнд", "Та сайн байна уу"],
                    "prompt": "A senior colleague greets you at 14:00 with: 'Өдрийн мэнд хүргэе!'. How should you respectfully reply?",
                    "stimulusTextCyrillic": "Ажилтан: Өдрийн мэнд хүргэе!",
                    "hint": "Echo the diurnal greeting and add a respectful inquiry about their wellbeing using 'Та'.",
                    "options": [
                        {"id": "opt_resp_polite", "text": "Өдрийн мэнд хүргэе, та сайн байна уу? (Good afternoon, are you well?)", "cyrillic": "Өдрийн мэнд хүргэе, та сайн байна уу?", "isCorrect": True, "explanation": "Correct! Echoing the time-specific greeting with the formal honorific inquiry 'та сайн байна уу?' is the polite gold standard."},
                        {"id": "opt_resp_casual", "text": "За, юу байна? (Yeah, what's up?)", "cyrillic": "За, юу байна?", "isCorrect": False, "explanation": "Incorrect. 'Юу байна' is informal slang inappropriate with senior colleagues."},
                        {"id": "opt_resp_parting", "text": "Баяртай, маргааш уулзъя. (Goodbye, see you tomorrow.)", "cyrillic": "Баяртай, маргааш уулзъя.", "isCorrect": False, "explanation": "Incorrect. This is a departure farewell, not an arrival greeting."}
                    ],
                    "correctAnswer": "Өдрийн мэнд хүргэе, та сайн байна уу? (Good afternoon, are you well?)",
                    "acceptableAlternatives": ["Өдрийн мэнд хүргэе, та сайн байна уу?", "Өдрийн мэнд, та сайн байна уу?"],
                    "explanation": "Mongolian communicative etiquette requires matching or elevating the politeness register of a diurnal greeting with 'Та сайн байна уу?'.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Respectful and culturally authentic response.",
                        "onFailure": "Reply politely with: 'Өдрийн мэнд хүргэе, та сайн байна уу?'."
                    },
                    "detailedGrammarNote": "Addressing an equal or senior requires the polite 2nd-person pronoun 'Та' (never informal 'чи') in business and administrative settings.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Өдрийн мэнд хүргэе, та сайн байна уу?",
                        "slowSpeechSynthesisText": "Өдрийн мэнд хүргэе, та сайн байна уу?",
                        "ipaTranscription": "/ɵtʰriːn mentʰ xʊrɡiː, tʰa sæːŋ pæːn ʊː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_02_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Cloze Insertion: Evening Salutation",
                    "modality": "SALUTATION_REGISTER_MATCH",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["cloze_accuracy", "genitive_time_derivation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Оройн мэнд"],
                    "prompt": "Fill in the blank with the correct genitive time word to complete the 19:00 PM greeting: '______ мэнд хүргэе!'.",
                    "contextSentence": "Цаг 19:00 болж байна. (The time is 19:00.)",
                    "stimulusTextCyrillic": "_______ мэнд хүргэе!",
                    "hint": "Recall how time-of-day nouns take the genitive attribute ending -н to modify 'мэнд' (wellbeing) for dusk hours.",
                    "correctAnswer": "Оройн",
                    "acceptableAlternatives": ["оройн", "ОРОЙН"],
                    "explanation": "'Оройн мэнд хүргэе!' means 'Good evening!'. The noun 'орой' adds -н to form the genitive attribute 'оройн'.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'Оройн мэнд хүргэе!' is complete.",
                        "onFailure": "Use the genitive form of 'орой' (evening) ending in -н: 'Оройн'."
                    },
                    "detailedGrammarNote": "Nouns ending in short diphthongs or vowels like 'орой' add '-н' to form the unstable genitive attribute ('оройн мэнд').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Оройн мэнд хүргэе!",
                        "slowSpeechSynthesisText": "Оройн мэнд хүргэе!",
                        "ipaTranscription": "/ɔrɔiŋ mentʰ xʊrɡiː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_02_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Acoustic Salutation Decoding in Public Broadcast",
                    "modality": "SALUTATION_REGISTER_MATCH",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["broadcast_greeting_comprehension", "time_inference"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["үзэгчид", "мэндчилгээ"],
                    "prompt": "Listen to the television news anchor opening the broadcast. At what time of day is this news program airing?",
                    "stimulusTextCyrillic": "Эрхэм хүндэт үзэгчид ээ, энэ өдрийн амар амгаланг айлтган мэндчилье.",
                    "hint": "Listen for 'энэ өдрийн' (of this day / afternoon).",
                    "options": [
                        {"id": "opt_afternoon", "text": "Midday / Afternoon (Өдрийн цаг)", "cyrillic": "Өдрийн цаг", "isCorrect": True, "explanation": "Correct! The anchor said 'энэ өдрийн амар амгалан' (peace of this day/afternoon)."},
                        {"id": "opt_morning", "text": "Early Morning (Өглөөний цаг)", "cyrillic": "Өглөөний цаг", "isCorrect": False, "explanation": "Incorrect. The anchor did not say өглөөний."},
                        {"id": "opt_night", "text": "Late Night (Шөнийн цаг)", "cyrillic": "Шөнийн цаг", "isCorrect": False, "explanation": "Incorrect. This is daytime broadcast greeting."}
                    ],
                    "correctAnswer": "Midday / Afternoon (Өдрийн цаг)",
                    "acceptableAlternatives": ["Өдрийн цаг", "Afternoon", "Midday"],
                    "explanation": "Anchors frequently use high-register ceremonial phrases like 'энэ өдрийн амар амгаланг айлтгая' for midday/afternoon transmissions.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! You caught 'энэ өдрийн' in formal broadcast speech.",
                        "onFailure": "The anchor said 'энэ өдрийн' which refers to the day/afternoon."
                    },
                    "detailedGrammarNote": "'Амар амгаланг айлтгая' is a classical ceremonial formula deriving from traditional epistolary conventions.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Эрхэм хүндэт үзэгчид ээ, энэ өдрийн амар амгаланг айлтган мэндчилье.",
                        "slowSpeechSynthesisText": "Эрхэм хүндэт үзэгчид ээ, энэ өдрийн амар амгаланг айлтган мэндчилье.",
                        "ipaTranscription": "/erxəm xʊntət utsəktsʰət eː, en ɵtriːn amər amɢaɮəŋ aæɮtʰɢən mentʰtʃiɮjiː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_02_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Register Appropriateness: Casual vs Formal Greetings",
                    "modality": "SALUTATION_REGISTER_MATCH",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["sociolinguistic_register_selection"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Сайн уу", "Өглөөний мэнд хүргэе"],
                    "prompt": "You meet your company CEO in the elevator. Which greeting demonstrates proper professional respect?",
                    "hint": "Avoid one-word peer greetings like 'Сайн уу'. Use full polite time-of-day phrases.",
                    "options": [
                        {"id": "reg_formal", "text": "Өглөөний мэнд хүргэе, захирал аа. (Good morning, Director.)", "cyrillic": "Өглөөний мэнд хүргэе, захирал аа.", "isCorrect": True, "explanation": "Correct! Formal diurnal greeting paired with respectful professional title + vocative particle."},
                        {"id": "reg_casual", "text": "Сайн уу, Батаа! (Hey, Bat!)", "cyrillic": "Сайн уу, Батаа!", "isCorrect": False, "explanation": "Incorrect. This is overly familiar peer slang inappropriate for executive staff."},
                        {"id": "reg_slang", "text": "Юу байна даа? (What's cookin'?)", "cyrillic": "Юу байна даа?", "isCorrect": False, "explanation": "Incorrect. Highly colloquial phrasing."}
                    ],
                    "correctAnswer": "Өглөөний мэнд хүргэе, захирал аа. (Good morning, Director.)",
                    "acceptableAlternatives": ["Өглөөний мэнд хүргэе, захирал аа."],
                    "explanation": "Addressing company leadership requires formal time salutations ('Өглөөний мэнд хүргэе') and title honorifics ('захирал аа').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Dignified and respectful executive communication.",
                        "onFailure": "Use 'Өглөөний мэнд хүргэе, захирал аа.' for formal leadership."
                    },
                    "detailedGrammarNote": "The vocative enclitic 'аа/ээ/оо/өө' attached to titles ('захирал аа', 'багш аа') signals respectful direct address in administrative communication.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Өглөөний мэнд хүргэе, захирал аа.",
                        "slowSpeechSynthesisText": "Өглөөний мэнд хүргэе, захирал аа.",
                        "ipaTranscription": "/ɵɡɮɵːniː mentʰ xʊrɡiː, tsaxʲirəɮ aː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 6: les_a1_16_05_reception_desk_simulation
        {
            "lessonId": "les_a1_16_05_reception_desk_simulation",
            "exercises": [
                {
                    "exerciseId": "ex_a1_16_05_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Reception Roleplay: Turn 1 Welcoming Inquiry",
                    "modality": "DIALOGUE_ROLEPLAY_COMPLETION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["reception_interaction", "polite_inquiry"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хүлээн авагч", "хэнтэй", "уулзах"],
                    "prompt": "You step up to the reception desk. The receptionist smiles and says: 'Сайн байна уу? Танд юугаар туслах вэ?'. What should you say if you have an appointment with Mr. Bold?",
                    "stimulusTextCyrillic": "Хүлээн авагч: Сайн байна уу? Танд юугаар туслах вэ?",
                    "hint": "Use the comitative case '-тай' (with) when expressing meeting someone: Болдтой уулзах.",
                    "options": [
                        {"id": "turn_1", "text": "Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм. (Hello. I have come to meet Director Bold.)", "cyrillic": "Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм.", "isCorrect": True, "explanation": "Correct! Natural and polite phrasing using intentional supine -хаар/хээр with comitative -тай."},
                        {"id": "turn_2", "text": "Болд хаана байна? Би шууд орлоо. (Where is Bold? I'm going in directly.)", "cyrillic": "Болд хаана байна? Би шууд орлоо.", "isCorrect": False, "explanation": "Incorrect. Impolite and violates visitor protocol."},
                        {"id": "turn_3", "text": "Би захирал биш. (I am not a director.)", "cyrillic": "Би захирал биш.", "isCorrect": False, "explanation": "Incorrect. Irrelevant response."}
                    ],
                    "correctAnswer": "Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм. (Hello. I have come to meet Director Bold.)",
                    "acceptableAlternatives": ["Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм.", "Би Болд захиралтай уулзахаар ирсэн."],
                    "explanation": "'[Name]-тай уулзахаар ирсэн' (I have come in order to meet [Name]) is the standard polite formula at Mongolian office receptions.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Polite and accurate visitor phrasing.",
                        "onFailure": "Say: 'Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм.'."
                    },
                    "detailedGrammarNote": "The supine verbal noun in -хаар⁴ ('уулзахаар') denotes the deliberate purpose of arriving ('ирсэн').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм.",
                        "slowSpeechSynthesisText": "Сайн байна уу. Би Болд захиралтай уулзахаар ирсэн юм.",
                        "ipaTranscription": "/sæːŋ pæːn ʊː. pʰi pɔɮtʰ tsaxʲirəɮtʰæː ʊːɮtsəxaːr irsəŋ jʊm/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_05_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Interpreting Polite Directives: 'Түр хүлээнэ үү'",
                    "modality": "DIALOGUE_ROLEPLAY_COMPLETION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["polite_imperative_comprehension", "reception_instructions"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["түр", "хүлээнэ үү", "сууна уу"],
                    "prompt": "The receptionist checks the register and says: 'За, та энд түр хүлээнэ үү. Би одоо мэдэгдье.' What did the receptionist ask you to do?",
                    "stimulusTextCyrillic": "Хүлээн авагч: За, та энд түр хүлээнэ үү. Би одоо мэдэгдье.",
                    "hint": "'Түр' means 'temporarily/for a moment', and 'хүлээнэ үү' means 'please wait'.",
                    "options": [
                        {"id": "dir_wait", "text": "Please wait here a moment while she notifies him.", "cyrillic": "Энд түр хүлээнэ үү", "isCorrect": True, "explanation": "Correct! 'Түр хүлээнэ үү' means 'please wait a moment'."},
                        {"id": "dir_leave", "text": "Please leave and come back next week.", "cyrillic": "Дараа ирнэ үү", "isCorrect": False, "explanation": "Incorrect. She asked you to wait briefly."},
                        {"id": "dir_call", "text": "Please call Director Bold on your phone right now.", "cyrillic": "Утсаар ярина уу", "isCorrect": False, "explanation": "Incorrect. She is notifying him herself."}
                    ],
                    "correctAnswer": "Please wait here a moment while she notifies him.",
                    "acceptableAlternatives": ["Please wait here a moment", "энд түр хүлээнэ үү"],
                    "explanation": "'Түр хүлээнэ үү' is a polite request utilizing the volitional directive ending -нэ үү/нө үү ('will you please wait a moment').",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! The receptionist asked you to wait briefly.",
                        "onFailure": "'Түр хүлээнэ үү' = Please wait a moment."
                    },
                    "detailedGrammarNote": "The polite request marker '-нэ үү/-нэ үү' attaches to verb stems to form soft directives appropriate in service interactions.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "За, та энд түр хүлээнэ үү. Би одоо мэдэгдье.",
                        "slowSpeechSynthesisText": "За, та энд түр хүлээнэ үү. Би одоо мэдэгдье.",
                        "ipaTranscription": "/tsa, tʰa entʰ tʰur xʊɮiːnə ʊː. pʰi ɔtɔː metəkjiː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_05_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Stating Identity and Company Affiliation",
                    "modality": "DIALOGUE_ROLEPLAY_COMPLETION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["self_introduction_syntax", "affiliation_statement"],
                    "grammarTargets": ["gram_a1_sov_word_order"],
                    "vocabularyTargets": ["компани", "төлөөлөгч", "би"],
                    "prompt": "When the receptionist asks 'Та нэр, байгууллагаа хэлнэ үү?' (Could you please state your name and organization?), assemble your reply: 'I am a representative from ABC company'.",
                    "wordTokens": ["ABC", "би", "төлөөлөгч", "компанийн"],
                    "correctTokenOrder": ["би", "ABC", "компанийн", "төлөөлөгч"],
                    "correctAnswer": "би ABC компанийн төлөөлөгч",
                    "acceptableAlternatives": ["Би ABC компанийн төлөөлөгч.", "Би ABC компанийн төлөөлөгч байна"],
                    "hint": "Subject (Би) + Genitive company (ABC компанийн) + Predicate noun (төлөөлөгч).",
                    "explanation": "Genitive modifiers precede the noun head: 'ABC компанийн төлөөлөгч' (ABC company's representative).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Accurate company affiliation phrasing.",
                        "onFailure": "Sequence: Би -> ABC -> компанийн -> төлөөлөгч."
                    },
                    "detailedGrammarNote": "Foreign corporate acronyms appear before the generic word 'компани', which carries the case suffix ('компанийн').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би Эй-Би-Си компанийн төлөөлөгч.",
                        "slowSpeechSynthesisText": "Би Эй-Би-Си компанийн төлөөлөгч.",
                        "ipaTranscription": "/pʰi eː-piː-siː xʰɔmpʰaniːŋ tʰɵɮɵːɮɵɡtʃʰ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_05_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Acoustic Dialogue Extraction: Visitor Log Data",
                    "modality": "DIALOGUE_ROLEPLAY_COMPLETION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["listening_detail_extraction", "reception_log_comprehension"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["өрөө", "давхар"],
                    "prompt": "Listen to the receptionist give directions to the visitor: 'Болд захирлын өрөө 3-р давхарт, 305 тоот.' On which floor and in which room number is the meeting?",
                    "stimulusTextCyrillic": "Болд захирлын өрөө 3-р давхарт, 305 тоот.",
                    "hint": "3-р давхар = 3rd floor; 305 тоот = room 305.",
                    "options": [
                        {"id": "loc_3_305", "text": "3rd floor, Room 305 (3-р давхарт, 305 тоот)", "cyrillic": "3-р давхарт, 305 тоот", "isCorrect": True, "explanation": "Correct! '3-р давхар' is 3rd floor and '305 тоот' is room 305."},
                        {"id": "loc_2_205", "text": "2nd floor, Room 205 (2-р давхарт, 205 тоот)", "cyrillic": "2-р давхарт, 205 тоот", "isCorrect": False, "explanation": "Incorrect. The audio stated 3-р давхар."},
                        {"id": "loc_5_300", "text": "5th floor, Room 300 (5-р давхарт, 300 тоот)", "cyrillic": "5-р давхарт, 300 тоот", "isCorrect": False, "explanation": "Incorrect. The numbers do not match."}
                    ],
                    "correctAnswer": "3rd floor, Room 305 (3-р давхарт, 305 тоот)",
                    "acceptableAlternatives": ["3rd floor, Room 305", "3-р давхарт, 305 тоот"],
                    "explanation": "Mongolian uses '-р/-дугаар' for ordinal numbers (3-р = гуравдугаар) and 'тоот' (numbered unit) for office and apartment rooms.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Floor and room number parsed accurately.",
                        "onFailure": "Listen for '3-р давхарт' (3rd floor) and '305 тоот' (room 305)."
                    },
                    "detailedGrammarNote": "Ordinal numeral abbreviation in Cyrillic uses a hyphen followed by 'р' (1-р, 2-р, 3-р) or 'дугаар/дүгээр'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Болд захирлын өрөө гуравдугаар давхарт, гурван зуун таван тоот.",
                        "slowSpeechSynthesisText": "Болд захирлын өрөө 3-р давхарт, 305 тоот.",
                        "ipaTranscription": "/pɔɮtʰ tsaxʲirɮiːŋ ɵrɵː ɢʊrəwtʊɢaːr tʰawxərtʰ, ɢʊrwəŋ tsʊːŋ tʰawəŋ tʰɔːtʰ/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a1_16_05_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Visitor Badge & Access Protocol Response",
                    "modality": "DIALOGUE_ROLEPLAY_COMPLETION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["civic_transaction_protocol", "polite_acknowledgment"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["үнэмлэх", "карт", "баярлалаа"],
                    "prompt": "The receptionist hands you a guest badge and says: 'Энэ зочны үнэмлэхийг зүүгээрэй' (Please wear this guest ID). What is the appropriate acknowledgment?",
                    "stimulusTextCyrillic": "Хүлээн авагч: Энэ зочны үнэмлэхийг зүүгээрэй.",
                    "hint": "Express gratitude and indicate you understand.",
                    "options": [
                        {"id": "ack_polite", "text": "Маш их баярлалаа, ойлголоо. (Thank you very much, understood.)", "cyrillic": "Маш их баярлалаа, ойлголоо.", "isCorrect": True, "explanation": "Correct! 'Баярлалаа, ойлголоо' is the courteous and expected acknowledgment."},
                        {"id": "ack_refusal", "text": "Үгүй, би зүүхгүй. (No, I won't wear it.)", "cyrillic": "Үгүй, би зүүхгүй.", "isCorrect": False, "explanation": "Incorrect. Uncooperative and socially unacceptable."},
                        {"id": "ack_confused", "text": "Энэ юу вэ? Би явж байна. (What is this? I am leaving.)", "cyrillic": "Энэ юу вэ? Би явж байна.", "isCorrect": False, "explanation": "Incorrect. Confused and inappropriate."}
                    ],
                    "correctAnswer": "Маш их баярлалаа, ойлголоо. (Thank you very much, understood.)",
                    "acceptableAlternatives": ["Маш их баярлалаа, ойлголоо.", "Баярлалаа"],
                    "explanation": "'Маш их баярлалаа' followed by 'ойлголоо' (understood) completes the security check-in exchange smoothly.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Seamless professional visitor etiquette.",
                        "onFailure": "Respond with gratitude: 'Маш их баярлалаа, ойлголоо.'."
                    },
                    "detailedGrammarNote": "The verb ending '-аарай⁴' ('зүүгээрэй') is the prescriptive imperative expressing polite instructions or invitations from an authority/host.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Маш их баярлалаа, ойлголоо.",
                        "slowSpeechSynthesisText": "Маш их баярлалаа, ойлголоо.",
                        "ipaTranscription": "/maʃ ix pajərɮəɮaː, ɔeɮɢɔɮɔː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        }
    ]
