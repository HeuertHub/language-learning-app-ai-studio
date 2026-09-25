#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C2 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_c2_229_01_khalkha_phonotactics_syntax_intro (Grammar Introduction)
2. les_c2_229_03_rush_hour_traffic_quarrel_listening (Listening)
3. les_c2_237_06_c2_sec01_culminating_operational_synthesis (Synthesis/Capstone)
"""

def get_c2_exercises():
    return [
        # LESSON 19: les_c2_229_01_khalkha_phonotactics_syntax_intro
        {
            "lessonId": "les_c2_229_01_khalkha_phonotactics_syntax_intro",
            "exercises": [
                {
                    "exerciseId": "ex_c2_229_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Khalkha Spoken Vowel Syncope & Sandhi Reduction",
                    "modality": "KHALKHA_PHONOTACTICS_DECODING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["spoken_khalkha_syncope", "phonotactic_sandhi_analysis"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["эгшиг гээгдэх", "хэлэх", "ажиллах"],
                    "prompt": "In fast, unscripted Khalkha conversational speech (170-190 wpm), non-initial short vowels in open syllables regularly undergo complete phonetic syncope (deletion). When a native speaker says the phrase written in Cyrillic as:\n\n'Та юу хийж байгаа юм бэ?' (What are you doing?)\n\nWhat is the authentic rapid spoken colloquial acoustic realization?",
                    "stimulusTextCyrillic": "Та юу хийж байгаа юм бэ? -> [юужийн / юу хийж бгаам бэ]",
                    "hint": "'Байгаа юм бэ' undergoes dramatic clitic coalescence and vowel reduction.",
                    "options": [
                        {"id": "real_fast", "text": "[Та юу хийж бгаам бэ?] or contracted [Та юужийн бэ?], where the auxiliary verb and copula coalesce into a monosyllabic nasalized diphthong [bgaːm / dʒiːŋ].", "cyrillic": "[юу хийж бгаам бэ] / [юужийн]", "isCorrect": True, "explanation": "Correct! Native Khalkha colloquial economy contracts 'байгаа юм' to [бгаам / жгаам] and combines 'хийж байна' to [хийжийн / хийж бна]."},
                        {"id": "real_epenthesis", "text": "[Та юу хийжэ байгаа вэ?], where an epenthetic vowel is inserted between the converb and the auxiliary without any elision or coalescence.", "cyrillic": "Жийрэг эгшигтэй задгай дуудах", "isCorrect": False, "explanation": "Incorrect. Khalkha does not insert epenthetic vowels between converb -ж and auxiliary 'байх'; it triggers elision instead."},
                        {"id": "real_archaic", "text": "[Та юуг хиймүй?], preserving classical written Mongolian synthetic verbal morphology in informal register.", "cyrillic": "Хуучин бичгийн хэлбэрээр", "isCorrect": False, "explanation": "Incorrect. Classical synthetic forms are not used in contemporary spoken Khalkha vernacular."}
                    ],
                    "correctAnswer": "[Та юу хийж бгаам бэ?] or contracted [Та юужийн бэ?], where the auxiliary verb and copula coalesce into a monosyllabic nasalized diphthong [bgaːm / dʒiːŋ].",
                    "acceptableAlternatives": ["[Та юу хийж бгаам бэ?]", "юу хийж бгаам бэ", "юужийн"],
                    "explanation": "At C2, mastery requires comprehending rapid acoustic reductions: 'байгаа юм бэ' -> [бгаам бэ], 'хийж байгаа' -> [хийж бга / хийжийн].",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Master-level insight into spoken Khalkha phonotactics.",
                        "onFailure": "Spoken Khalkha contracts 'байгаа юм бэ' to [бгаам бэ]."
                    },
                    "detailedGrammarNote": "Vowel syncope (богино эгшиг гээгдэх хууль) in spoken Khalkha deletes unstressed short vowels in open medial syllables, triggering consonant cluster assimilations.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Та одоо юу хийж байгаа юм бэ?",
                        "slowSpeechSynthesisText": "юу хийж бгаам бэ?",
                        "ipaTranscription": "/tʰa ɔtɔː jʊː xʲiːtʃʰ pɢaːm pe/",
                        "speakerRole": "male_native",
                        "speechRate": 1.2,
                        "acousticEnvironment": "fast_conversational"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Inter-Word Nasal Assimilation and Velar Sandhi",
                    "modality": "KHALKHA_PHONOTACTICS_DECODING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["nasal_assimilation_sandhi", "articulatory_phonology"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["өнөөдрийн сонин", "санхүү"],
                    "prompt": "When the genitive phrase 'өнөөдрийн сонин' (today's newspaper) is spoken at natural native tempo, what sandhi assimilation happens to the final coronal nasal /n/ before the following bilabial or alveolar onset?",
                    "stimulusTextCyrillic": "өнөөдрийн сонин -> [өнөөдрийн соним / сонин]",
                    "hint": "In fast Mongolian, final /n/ before labials assimilates to [m], and before velars assimilates to [ŋ].",
                    "options": [
                        {"id": "sandhi_nasal", "text": "Regressive place assimilation: Word-final coronal /n/ assimilates to the place of articulation of the adjacent consonant (e.g. becoming bilabial [m] before /b, p, m/, and velar [ŋ] in pause or before velars).", "cyrillic": "Залгах гийгүүлэгчийн байранд зохицох", "isCorrect": True, "explanation": "Correct! Khalkha final nasals undergo active place assimilation in fluent connected speech."},
                        {"id": "sandhi_devoicing", "text": "Progressive devoicing: The following initial voiced plosive (/b/ or /g/) is completely devoiced and aspirated by the preceding coronal nasal.", "cyrillic": "Дараах гийгүүлэгчийг дүлийрүүлэх", "isCorrect": False, "explanation": "Incorrect. Mongolian nasals are voiced sonorants and trigger regressive place assimilation, not progressive devoicing."},
                        {"id": "sandhi_total_elision", "text": "Complete nasal deletion without compensatory vowel nasalization, leaving an open syllable.", "cyrillic": "Бүрэн гээгдэх", "isCorrect": False, "explanation": "Incorrect. The coronal nasal does not delete across boundaries; it assimilates to the place of the succeeding consonant."}
                    ],
                    "correctAnswer": "Regressive place assimilation: Word-final coronal /n/ assimilates to the place of articulation of the adjacent consonant (e.g. becoming bilabial [m] before /b, p, m/, and velar [ŋ] in pause or before velars).",
                    "acceptableAlternatives": ["Regressive place assimilation", "Залгах гийгүүлэгчийн байранд зохицох"],
                    "explanation": "Coronal /n/ assimilates to bilabial [m] before labials (e.g. 'арван бууз' -> [арвам бууз]) and velar [ŋ] before velars ('арван гэр' -> [арваҥ гэр]).",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Profound articulatory phonetic analysis.",
                        "onFailure": "Final /n/ assimilates to the place of the following consonant."
                    },
                    "detailedGrammarNote": "This sandhi rule is so natural that native speakers execute it without conscious awareness, while non-natives who fail to assimilate sound conspicuously foreign.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Өнөөдрийн сонин дээр гарсан мэдээ.",
                        "slowSpeechSynthesisText": "өнөөдрийн сонин.",
                        "ipaTranscription": "/ɵnɵːtriːŋ sɔnʲiŋ tʰeːr ɢarsəŋ metiː/",
                        "speakerRole": "narrator",
                        "speechRate": 1.1
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Deciphering Colloquial Particle Contractions in Fast Dialogue",
                    "modality": "KHALKHA_PHONOTACTICS_DECODING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["clitic_coalescence", "colloquial_particle_decoding"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["гээд", "гээч", "байна"],
                    "prompt": "Listen to this rapid conversational retort:\n\n'Тэр чинь тийм биш гээ биз дээ?'\n\nWhat are the underlying formal grammatical components of 'гээ биз дээ'?",
                    "stimulusTextCyrillic": "гээ биз дээ",
                    "hint": "'Гээ' is contracted from 'гэж байна / гэсэн', and 'биз дээ' is the epistemic tag question marker.",
                    "options": [
                        {"id": "part_underlying", "text": "Quotative verb 'гэж байна / гэсэн' contracted into long vowel 'гээ' + epistemic confirmation tag 'биз дээ' (didn't they say / isn't that so?).", "cyrillic": "гэж байна / гэсэн + биз дээ", "isCorrect": True, "explanation": "Correct! 'Гээ' represents the spoken reduction of quotative 'гэж байна / гэсэн'."},
                        {"id": "part_durative", "text": "Imperfective durative aspectual suffix '-аа/-ээ' attached to the verb 'гэх' + imperative particle 'биз'.", "cyrillic": "Үйл үгийн үргэлжлэх хэлбэр", "isCorrect": False, "explanation": "Incorrect. 'Гээ' in this discourse position functions as a contracted quotative reportative clitic, not a durative aspect marker."},
                        {"id": "part_adverbial", "text": "Modal adverb 'гээд' acting as a causal conjunction + optative mood suffix '-сугай'.", "cyrillic": "Шалтгааны холбоос", "isCorrect": False, "explanation": "Incorrect. The construction is a conversational quotative contraction fused with the epistemic tag 'биз дээ'."}
                    ],
                    "correctAnswer": "Quotative verb 'гэж байна / гэсэн' contracted into long vowel 'гээ' + epistemic confirmation tag 'биз дээ' (didn't they say / isn't that so?).",
                    "acceptableAlternatives": ["гэж байна / гэсэн + биз дээ", "Quotative contraction + tag"],
                    "explanation": "In spoken Khalkha, quotative chains ('гэж хэлсэн / гэж байна') collapse into 'гээ', which pairs with particles like 'биз дээ', 'гээч', or 'дээ'.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Deep syntactic awareness of vernacular spoken reduction.",
                        "onFailure": "'гээ' is the colloquial contraction of quotative 'гэж байна / гэсэн'."
                    },
                    "detailedGrammarNote": "Quotative grammaticalization in Mongolic is extensive: 'гэж' (converb) -> 'гээд' -> 'гээ' (contracted clitic introducing indirect discourse or pragmatic stance).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Тэр чинь тийм биш гээ биз дээ?",
                        "slowSpeechSynthesisText": "тийм биш гээ биз дээ?",
                        "ipaTranscription": "/tʰer tʃʰiŋ tʰiːm pʰiʃ ɡeː pʲits tʰeː/",
                        "speakerRole": "female_native",
                        "speechRate": 1.15
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Token Assembly: Rapid Spoken Retort with Emphatic Clitics",
                    "modality": "KHALKHA_PHONOTACTICS_DECODING",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["spoken_pragmatics", "vernacular_word_order"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["юу гэсэн үг юм", "дээ"],
                    "prompt": "Reconstruct this natural, rapid idiomatic challenge: 'What on earth is that supposed to mean?!':",
                    "wordTokens": ["гэсэн", "юм", "Энэ", "үг", "чинь", "юу", "бэ"],
                    "correctTokenOrder": ["Энэ", "чинь", "юу", "гэсэн", "үг", "юм", "бэ"],
                    "correctAnswer": "Энэ чинь юу гэсэн үг юм бэ",
                    "acceptableAlternatives": ["Энэ чинь юу гэсэн үг юм бэ?", "Энэ чинь юу гэсэн үг вэ"],
                    "hint": "Demonstrative (Энэ) -> Discourse topic clitic (чинь) -> Interrogative (юу) -> Participle (гэсэн) -> Head noun (үг) -> Modal copula (юм) -> Interrogative particle (бэ).",
                    "explanation": "'Энэ чинь юу гэсэн үг юм бэ' is the quintessential idiomatic reaction challenging an unexpected, illogical, or offensive statement.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Native-like pragmatic exclamation assembled.",
                        "onFailure": "Order: Энэ -> чинь -> юу -> гэсэн -> үг -> юм -> бэ."
                    },
                    "detailedGrammarNote": "Second-person clitic 'чинь' acts here not as a literal pronoun but as an emotive discourse particle signaling astonishment or subjective involvement.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэ чинь одоо юу гэсэн үг юм бэ?!",
                        "slowSpeechSynthesisText": "юу гэсэн үг юм бэ?",
                        "ipaTranscription": "/en tʃʰiŋ ɔtɔː jʊː ɡissəŋ ʊɡ jʊm pe/",
                        "speakerRole": "male_native",
                        "speechRate": 1.2,
                        "acousticEnvironment": "agitated_conversation"
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Insertion: Rapid Conversational Emphatic 'Л Дээ'",
                    "modality": "KHALKHA_PHONOTACTICS_DECODING",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["pragmatic_particle_mastery", "conversational_nuance"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["л дээ"],
                    "prompt": "In fast colloquial debate, a speaker uses the restrictive restrictive particle 'л' fused with persuasive 'дээ' to concede a point while maintaining their ground: 'Тийм _______, гэхдээ үүнийг бас бодох хэрэгтэй.' Fill in the paired particle:",
                    "stimulusTextCyrillic": "Тийм _______, гэхдээ бас бодох хэрэгтэй.",
                    "hint": "Combine the monosyllabic restrictive focus clitic with the colloquial conversational agreement particle.",
                    "correctAnswer": "л дээ",
                    "acceptableAlternatives": ["л дээ", "Л дээ"],
                    "explanation": "'Тийм л дээ' (Well yes, sure / that's true of course) softens agreement before immediately pivoting with 'гэхдээ' (however).",
                    "learnerFeedback": {
                        "onSuccess": "Гайхалтай! 'л дээ' conveys the exact conversational concession.",
                        "onFailure": "Remember that 'л дээ' conveys nuanced conversational concession."
                    },
                    "detailedGrammarNote": "The particle cluster 'л дээ' combines restrictive focus 'л' with persuasive modal particle 'дээ' to establish nuanced pragmatic alignment.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Тийм л дээ, гэхдээ бид бодит байдлаа харах ёстой.",
                        "slowSpeechSynthesisText": "тийм л дээ.",
                        "ipaTranscription": "/tʰiːm ɮ tʰeː, kewxtʰeː pʰitʰ pɔtʲitʰ pæːtɮaː xərəx jɵstʰɔe/",
                        "speakerRole": "female_native",
                        "speechRate": 1.15
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 20: les_c2_229_03_rush_hour_traffic_quarrel_listening
        {
            "lessonId": "les_c2_229_03_rush_hour_traffic_quarrel_listening",
            "exercises": [
                {
                    "exerciseId": "ex_c2_229_03_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Acoustic Dissection: 180 wpm Traffic Altercation Claims",
                    "modality": "AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["high_speed_acoustic_comprehension", "argument_tracking_under_noise"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["эгнээ байр эзлэх", "гэрлэн дохио", "торгууль"],
                    "prompt": "Listen to an authentic 180 wpm recording of a heated altercation between a driver and a traffic police officer at the West Central Intersection (Баруун 4 зам) during evening gridlock:\n\nDriver: 'Хөөе цагдаа аа! Би ногоон гэрлээр орчихсон байсан байхгүй юу! Урд талын автобус гацаад таг зогсчихсон болохоос би яах юм бэ? Замын голоос ухралтай нь биш!'\nOfficer: 'Жолооч оо, уулзвар дээр түгжрэл үүссэн үед уулзвар луу нэвтрэхийг хориглосон дүрэм байгаа биз дээ? Бичиг баримтаа гаргаад ир!'\n\nWhat is the driver's core defensive legal justification for being stranded in the middle of the intersection?",
                    "stimulusTextCyrillic": "Би ногоон гэрлээр орчихсон ... урд талын автобус гацаад таг зогсчихсон болохоос би яах юм бэ?",
                    "hint": "The driver entered on green, but was blocked by a bus ahead that came to a dead halt ('таг зогссон').",
                    "options": [
                        {"id": "claim_bus_block", "text": "He lawfully entered on green, but was trapped when the bus in front came to an unexpected dead stop, making it physically impossible to proceed or reverse.", "cyrillic": "Ногоон гэрлээр орсон боловч урд талын автобус гацсан", "isCorrect": True, "explanation": "Correct! The driver claims lawful entry on green, blaming the entrapment entirely on the stalled bus ahead."},
                        {"id": "claim_signal_defect", "text": "He claims the traffic signal system was defective and switched instantaneously from green to red without any yellow warning phase.", "cyrillic": "Гэрлэн дохио алдаатай ажилласан гэх", "isCorrect": False, "explanation": "Incorrect. The driver specifically acknowledges entering on green, blaming the immobilized bus in front, not signal failure."},
                        {"id": "claim_emergency", "text": "He claims he was authorized to enter the gridlock because he was following an emergency escort vehicle.", "cyrillic": "Цуваа дагаж явсан гэх", "isCorrect": False, "explanation": "Incorrect. Fabricated excuse not in the audio dialogue."}
                    ],
                    "correctAnswer": "He lawfully entered on green, but was trapped when the bus in front came to an unexpected dead stop, making it physically impossible to proceed or reverse.",
                    "acceptableAlternatives": ["Lawfully entered on green but blocked by a bus", "ногоон гэрлээр орсон боловч урд талын автобус гацсан"],
                    "explanation": "The driver deploys the emphatic past perfect ('орчихсон байсан байхгүй юу') and impossibility modal ('ухралтай нь биш') to argue that traffic entrapment negated his volition.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Flawless extraction of high-speed colloquial claims under noise.",
                        "onFailure": "The driver argues he entered on green and was trapped by the bus ahead."
                    },
                    "detailedGrammarNote": "Impossibility idiom '-лтай нь биш⁴' ('ухралтай нь биш' = it's not as if I can reverse!) forcefully rejects unreasonable behavioral alternatives in heated verbal confrontations.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би ногоон гэрлээр орчихсон байсан байхгүй юу! Урд талын автобус гацаад таг зогсчихсон болохоос би яах юм бэ?",
                        "slowSpeechSynthesisText": "ногоон гэрлээр орчихсон байсан байхгүй юу.",
                        "ipaTranscription": "/pʰi nɔɢɔːŋ ɡerɮeːr ɔrtʃʰixsəŋ pæːsəŋ pæːxɢuː jʊː! ʊrtʰ tʰaɮiːŋ awtʰɔpʊs ɢatsʰaːtʰ tʰaɡ tsɔɡstʃʰixsəŋ pɔɮɔxɔːs pʰi jaːx jʊm pe/",
                        "speakerRole": "male_native",
                        "speechRate": 1.25,
                        "acousticEnvironment": "traffic_quarrel_horn_noise"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_03_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Decoding Epistemic Particle 'Байхгүй Юу' in Spontaneous Grievance",
                    "modality": "AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["pragmatic_particle_nuance", "conversational_epistemics"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["байхгүй юу", "болохоос"],
                    "prompt": "In the driver's agitated utterance: 'Би ногоон гэрлээр орчихсон байсан байхгүй юу!', what exact pragmatic force does the final clitic cluster 'байхгүй юу' convey?",
                    "stimulusTextCyrillic": "орчихсон байсан байхгүй юу!",
                    "hint": "'Байхгүй юу' asserts shared obviousness / 'Can't you see?! / You know damn well that...'.",
                    "options": [
                        {"id": "part_obviousness", "text": "Aggressive epistemic insistence on obvious shared reality: 'You know full well / As is completely obvious, I entered on green!'.", "cyrillic": "Мэдээжийн баримтыг эрс шаардан сануулах", "isCorrect": True, "explanation": "Correct! 'Байхгүй юу' asserts that the fact is glaringly self-evident to both speaker and listener."},
                        {"id": "part_absence", "text": "Literal negation indicating that the traffic light was physically missing from the pole.", "cyrillic": "Байхгүй гэсэн үгүйсгэл", "isCorrect": False, "explanation": "Incorrect. 'Байхгүй юу' is grammaticalized as an epistemic particle, not literal absence."},
                        {"id": "part_polite", "text": "Humble deference asking the officer for forgiveness.", "cyrillic": "Гуйлт", "isCorrect": False, "explanation": "Incorrect. The tone is defiant and self-justifying."}
                    ],
                    "correctAnswer": "Aggressive epistemic insistence on obvious shared reality: 'You know full well / As is completely obvious, I entered on green!'.",
                    "acceptableAlternatives": ["Aggressive epistemic insistence", "Мэдээжийн баримтыг сануулах"],
                    "explanation": "'Байхгүй юу' is an emphatic communicative clitic in spoken Khalkha demanding interlocutor acknowledgment of undeniable facts.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Masterful pragmatic analysis of 'байхгүй юу'.",
                        "onFailure": "'байхгүй юу' insists on an undeniable, obvious reality."
                    },
                    "detailedGrammarNote": "Despite having the surface form of negative caritive 'байхгүй' + interrogative 'юу', this construction functions purely as an assertive pragmatic stance marker.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би ногоон гэрлээр орчихсон байсан байхгүй юу!",
                        "slowSpeechSynthesisText": "орчихсон байсан байхгүй юу.",
                        "ipaTranscription": "/pʰi nɔɢɔːŋ ɡerɮeːr ɔrtʃʰixsəŋ pæːsəŋ pæːxɢuː jʊː/",
                        "speakerRole": "male_native",
                        "speechRate": 1.2
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_03_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Pinpointing Rhetorical De-escalation & Compliance Turning Point",
                    "modality": "AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["conflict_resolution_tracking", "conversational_turn_taking"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["за яахав", "бичиг баримт", "торгууль бичих"],
                    "prompt": "Listen to the continuation of the altercation:\n\nOfficer: 'Замын хөдөлгөөний дүрмийн 12.4-т түгжрэлтэй уулзвар луу орохыг хориглоно гэж заасан. Та журам зөрчсөн нь бичлэг дээр тодорхой харагдаж байна. Торгууль бичнэ.'\nDriver: 'За за, ах нь ойлголоо. Өнөөдөр яарч яваад л ийм юм болчихлоо. Торгуулиа бичүүлчихье. Харин оноо битгий хасаарай, гуйж байна шүү.'\n\nAt what exact point does the driver's stance switch from aggressive confrontation to pragmatic compliance and plea bargaining?",
                    "stimulusTextCyrillic": "За за, ах нь ойлголоо ... Торгуулиа бичүүлчихье. Харин оноо битгий хасаарай",
                    "hint": "Listen for 'За за, ах нь ойлголоо' where the driver adopts kinship self-address 'ах нь' and offers to accept the fine.",
                    "options": [
                        {"id": "turn_akhiin", "text": "When the driver says 'За за, ах нь ойлголоо'—shifting from shouting to adopting the familial persona 'ах нь' (older brother), conceding the ticket in exchange for begging the officer not to deduct demerit points.", "cyrillic": "За за ах нь ойлголоо гэхэд", "isCorrect": True, "explanation": "Correct! Adopting kinship address 'ах нь' instantly humanizes the interaction and opens pragmatic bargaining."},
                        {"id": "turn_code", "text": "When the officer cites Traffic Rule 12.4 and immediately writes a citation without allowing the driver to speak.", "cyrillic": "Цагдаа шууд торгууль бичихэд", "isCorrect": False, "explanation": "Incorrect. This is the officer's assertion of authority, not the driver's rhetorical turning point."},
                        {"id": "turn_denial", "text": "When the driver demands to see the officer's dashcam recording and threatens to appeal to the district police chief.", "cyrillic": "Даргын нэр барьж сүрдүүлэхэд", "isCorrect": False, "explanation": "Incorrect. The driver abandons threats and adopts an accommodating kinship persona ('ах нь')."}
                    ],
                    "correctAnswer": "When the driver says 'За за, ах нь ойлголоо'—shifting from shouting to adopting the familial persona 'ах нь' (older brother), conceding the ticket in exchange for begging the officer not to deduct demerit points.",
                    "acceptableAlternatives": ["At 'За за, ах нь ойлголоо'", "За за ах нь ойлголоо"],
                    "explanation": "In authentic Mongolian public confrontations, shifting to pseudo-kinship pronouns ('ах нь' / 'дүү нь') is the decisive sociolinguistic turning point for diffusing state confrontation and negotiating mitigation.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Extraordinary sociolinguistic perception of authentic Mongolian conflict de-escalation.",
                        "onFailure": "The turning point is 'За за, ах нь ойлголоо' (adoption of 'ах нь')."
                    },
                    "detailedGrammarNote": "Using self-reference 'ах нь' (literally 'his/her older brother') leverages cultural norms of filial seniority to appeal to the younger officer's compassion.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "За за, ах нь ойлголоо. Өнөөдөр яарч яваад л ийм юм болчихлоо. Торгуулиа бичүүлчихье.",
                        "slowSpeechSynthesisText": "За за, ах нь ойлголоо. Торгуулиа бичүүлчихье.",
                        "ipaTranscription": "/tsa tsa, ax nʲ ɔeɮɢɔɮɔː. ɵnɵːtər jaːrtʃʰ jəwaːtʰ ɮ iːm jʊm pɔɮtʃʰixɮɔː. tʰɔrɢʊːɮʲaː pʰitʃʰuːɮtʃʰixiː/",
                        "speakerRole": "male_native",
                        "speechRate": 1.1,
                        "acousticEnvironment": "traffic_deescalation"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_03_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Token Assembly: Mock Deference and Sarcastic Retort",
                    "modality": "AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["sarcasm_detection", "ironic_deference"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ухаантай хүн", "байх нь ээ"],
                    "prompt": "Reconstruct this biting, sarcastic retort uttered earlier by the driver: 'Oh, so you think you're the smartest person in the world, do you?!':",
                    "wordTokens": ["Та", "их", "хүн", "тийм", "байх", "ухаантай", "ээ", "нь"],
                    "correctTokenOrder": ["Та", "тийм", "их", "ухаантай", "хүн", "байх", "нь", "ээ"],
                    "correctAnswer": "Та тийм их ухаантай хүн байх нь ээ",
                    "acceptableAlternatives": ["Та тийм их ухаантай хүн байх нь ээ?", "Та тийм их ухаантай хүн байх нь ээ!"],
                    "hint": "Polite pronoun 'Та' -> degree modifier 'тийм их' -> 'ухаантай хүн' -> evidential copula 'байх нь ээ'.",
                    "explanation": "'Та тийм их ухаантай хүн байх нь ээ' uses mock evidential discovery ('байх нь ээ' = it turns out you are...) to drip with sarcastic contempt.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Bitter native sarcasm and evidential irony reconstructed.",
                        "onFailure": "Order: Та -> тийм -> их -> ухаантай -> хүн -> байх -> нь -> ээ."
                    },
                    "detailedGrammarNote": "The evidential combination of verbal noun in -х + possessive 'нь' + exclamatory vocative 'ээ' ('байх нь ээ') marks ironic realization of another's supposed superiority.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Та тийм их ухаантай хүн байх нь ээ?!",
                        "slowSpeechSynthesisText": "тийм их ухаантай хүн байх нь ээ.",
                        "ipaTranscription": "/tʰa tʰiːm ix ʊxaːŋtʰæː xun pæːx nʲ eː/",
                        "speakerRole": "male_native",
                        "speechRate": 1.15
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c2_229_03_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Insertion: Persuasive Plea Clitic 'Гуйж Байна Шүү'",
                    "modality": "AUTHENTIC_QUARREL_ACOUSTIC_ANALYSIS",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["plea_clitic_insertion", "emotive_particulate"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["гуйж байна шүү"],
                    "prompt": "Complete the driver's final pleading sentence to the police officer:\n\n'Энэ удаад сануулчих, дахиж алдаа гаргахгүй, ах нь хичээнгүйлэн ______ байна шүү.' (Let me off with a warning this once, I won't make a mistake again, your brother is earnestly begging you!)",
                    "stimulusTextCyrillic": "ах нь хичээнгүйлэн ______ байна шүү",
                    "hint": "Attach the imperfective converb suffix (-ж/-ч) to the verbal stem for entreating or asking earnestly.",
                    "correctAnswer": "гуйж",
                    "acceptableAlternatives": ["гуйж", "Гуйж"],
                    "explanation": "'Гуйж байна шүү' (I am begging you!) with modal converb 'гуйж' delivers the emotional plea.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'гуйж байна шүү' correctly inserted.",
                        "onFailure": "Remember that 'гуйж байна шүү' is the standard conversational plea formula."
                    },
                    "detailedGrammarNote": "The imperfective converb in -ж/-ч ('гуйж') coordinates with the auxiliary 'байна' and assertive particle 'шүү' in emotional appeals.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэ удаад сануулчих, ах нь хичээнгүйлэн гуйж байна шүү.",
                        "slowSpeechSynthesisText": "хичээнгүйлэн гуйж байна шүү.",
                        "ipaTranscription": "/en ʊtʰaːtʰ sanʊːɮtʃʰix, ax nʲ xitʃʰeːŋɡuːɮəŋ ɢʊetʃʰ pæːŋ ʃuː/",
                        "speakerRole": "male_native",
                        "speechRate": 1.1
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 21: les_c2_237_06_c2_sec01_culminating_operational_synthesis
        {
            "lessonId": "les_c2_237_06_c2_sec01_culminating_operational_synthesis",
            "exercises": [
                {
                    "exerciseId": "ex_c2_237_06_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Modernist Satire Dissection: Allegory and Subtext Extraction",
                    "modality": "MODERNIST_SATIRE_SYNTHESIS",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "EVALUATE_DISCOURSE",
                    "skillTargets": ["literary_subtext_extraction", "allegorical_satire_analysis"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ёгтлол", "далд утга", "нийгмийн шүүмжлэл"],
                    "prompt": "Read this excerpt from a contemporary Mongolian satirical short story regarding urban bureaucratic inertia:\n\n'Дарга ширээнийхээ араас өндийн, цонхоор цанталттай хотын саарал утааг харан санаа алдав. \"Манай хэлтэс энэ жил 400 хуудас тайлан үдэж, 80 удаагийн зөвлөгөөн зохион байгууллаа. Цаасан дээр бид аль хэдийн утаагаа ялж, ногоон төгөлд амьдарч байна. Харин энэ амьсгал боогдуулаад байгаа зүйл бол зүгээр л ард иргэдийн сэтгэл зүйн хий үзэгдэл төдий юм даа\" хэмээн тэмдэглэлийн дэвтэртээ алтан үзэгнийхээ хошууг нямбайлан арчив.'\n\nWhat is the biting core satirical irony deployed by the author?",
                    "stimulusTextCyrillic": "Цаасан дээр бид аль хэдийн утаагаа ялж ... ард иргэдийн сэтгэл зүйн хий үзэгдэл төдий юм даа",
                    "hint": "Analyze the grotesque chasm between fictitious paper success (400 pages of reports) and deadly physical reality (choking smog written off as citizen delusion).",
                    "options": [
                        {"id": "sat_chasm", "text": "Grotesque bureaucratic escapism: The official equates administrative paperwork with real-world problem-solving, absurdly dismissing lethal physical smog as a mere 'psychological hallucination' of the public while meticulously polishing his luxury golden pen.", "cyrillic": "Цаасан дээрх амжилтыг бодит амьдралтай хутгаж, асуудлыг үгүйсгэсэн ёгтлол", "isCorrect": True, "explanation": "Correct! The satire exposes how bureaucratic self-delusion and elite detachment reduce existential public crises to paper fictions."},
                        {"id": "sat_praise", "text": "Genuine praise of the department's energetic work in writing 400 pages of reports.", "cyrillic": "Ажлыг магтах", "isCorrect": False, "explanation": "Incorrect. The text is mordantly satirical, not laudatory."},
                        {"id": "sat_calligraphy", "text": "A nostalgic lament regarding the tragic decline of classical brush calligraphy and handwritten records in modern offices.", "cyrillic": "Бичгийн соёлыг дурсах", "isCorrect": False, "explanation": "Incorrect. The golden pen functions as an ironic symbol of bureaucratic detachment, not calligraphic nostalgia."}
                    ],
                    "correctAnswer": "Grotesque bureaucratic escapism: The official equates administrative paperwork with real-world problem-solving, absurdly dismissing lethal physical smog as a mere 'psychological hallucination' of the public while meticulously polishing his luxury golden pen.",
                    "acceptableAlternatives": ["Grotesque bureaucratic escapism", "Цаасан дээрх тайлангаар бодит байдлыг орлуулсан ёгтлол"],
                    "explanation": "Mastery in C2 requires perceiving how literary Khalkha wields understatement, institutional vocabulary ('зөвлөгөөн зохион байгуулах'), and symbolic imagery ('алтан үзэгний хошуу') for devastating social critique.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! Profound aesthetic and satirical decoding.",
                        "onFailure": "The satire skewers bureaucratic paper triumphs contrasted with suffocating reality."
                    },
                    "detailedGrammarNote": "Quotative 'хэмээн' followed by meticulous physical action ('нямбайлан арчив') underscores moral dissonance in classical Mongolian narrative prose.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Цаасан дээр бид аль хэдийн утаагаа ялж, ногоон төгөлд амьдарч байна.",
                        "slowSpeechSynthesisText": "цаасан дээр бид утаагаа ялжээ.",
                        "ipaTranscription": "/tsʰaːsəŋ tʰeːr pʰitʰ aɮ xitʃʰiːŋ ʊtʰaːɢaː jaɮtʃʰ, nɔɢɔːŋ tʰɵɡɵɮtʰ amʲtərtʃʰ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_237_06_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Interpreting Subverted Pastoral Metaphors in Urban Modernism",
                    "modality": "MODERNIST_SATIRE_SYNTHESIS",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["metaphorical_subversion", "cultural_inference"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["бэлчээр", "малын мөр", "түгжрэл"],
                    "prompt": "In modern Mongolian literary fiction, authors frequently invert traditional nomadic pastoral tropes to describe urban dystopia. When a poet describes Ulaanbaatar morning traffic as:\n\n'Хүлэг морьдын давхиа бус, төмөр сүргийн гацсан бэлчээр' (Not the galloping of steed-horses, but the stalled pasture of an iron herd)\n\nWhat cultural and existential tension is encapsulated by 'төмөр сүргийн гацсан бэлчээр'?",
                    "stimulusTextCyrillic": "төмөр сүргийн гацсан бэлчээр",
                    "hint": "'Төмөр сүрэг' (iron herd = cars) trapped in a 'гацсан бэлчээр' (gridlocked pasture = traffic-choked streets).",
                    "options": [
                        {"id": "meta_irony", "text": "Nomadic spatial alienation: Inverting the sacred steppe symbol of boundless freedom ('бэлчээр' - open pasture) and organic wealth ('сүрэг' - herd) into suffocating, immobile metal machinery gridlocked in urban concrete.", "cyrillic": "Нүүдэлчин ахуйн эрх чөлөөг суурин хотын түгжрэлтэй харшуулах", "isCorrect": True, "explanation": "Correct! Metaphorical clash between infinite steppe mobility and suffocating urban immobility."},
                        {"id": "meta_industrial", "text": "A technical description of agricultural tractor mechanization across rural pasturelands.", "cyrillic": "Хөдөө аж ахуйн техникийн шинэчлэл", "isCorrect": False, "explanation": "Incorrect. This is a poetic metaphor exploring urban gridlock, not agrarian machinery."},
                        {"id": "meta_meteorology", "text": "A meteorological warning predicting severe winter weather (зуд) threatening livestock across northern valleys.", "cyrillic": "Цаг агаарын зудын аюул", "isCorrect": False, "explanation": "Incorrect. The image subverts pastoral tropes for modern urban existential commentary."}
                    ],
                    "correctAnswer": "Nomadic spatial alienation: Inverting the sacred steppe symbol of boundless freedom ('бэлчээр' - open pasture) and organic wealth ('сүрэг' - herd) into suffocating, immobile metal machinery gridlocked in urban concrete.",
                    "acceptableAlternatives": ["Nomadic spatial alienation", "Нүүдэлчин ахуйг суурин түгжрэлтэй харшуулах"],
                    "explanation": "Contemporary Mongolian literature gains poignant rhetorical power by subverting nomad heritage concepts to articulate modern capitalist and urban dislocation.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Breathtaking cultural and metaphorical literary insight.",
                        "onFailure": "The poet contrasts infinite nomadic pasture with gridlocked urban traffic."
                    },
                    "detailedGrammarNote": "Nominal compound metaphors ('төмөр сүрэг') fuse ancient lexical roots with modern industrial realities without using explicit similes ('мэт/шиг').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Хүлэг морьдын давхиа бус, төмөр сүргийн гацсан бэлчээр.",
                        "slowSpeechSynthesisText": "төмөр сүргийн гацсан бэлчээр.",
                        "ipaTranscription": "/xuɮəkʰ mɔrʲtʰiːŋ tʰawxʲaː pʊs, tʰɵmɵr surɡiːŋ ɢatsʰsəŋ pʰeɮtʃʰeːr/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_c2_237_06_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Classical Aphoristic Synthesis on Truth & Power",
                    "modality": "MODERNIST_SATIRE_SYNTHESIS",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["gnomic_wisdom_synthesis", "parallel_clause_crafting"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["үнэн", "эрх мэдэл", "мөнх"],
                    "prompt": "Reconstruct this gnomic, parallel poetic aphorism on truth and temporal power:\n\n'Эрх мэдэл цагийн урсгалд хуучравч, эгэл үнэн мөнхийн наранд гэрэлтэнэ' (Though power withers in the flow of time, humble truth shines in the eternal sun):",
                    "wordTokens": ["урсгалд", "хуучравч", "үнэн", "мөнхийн", "Эрх", "гэрэлтэнэ", "цагийн", "наранд", "мэдэл", "эгэл"],
                    "correctTokenOrder": ["Эрх", "мэдэл", "цагийн", "урсгалд", "хуучравч", "эгэл", "үнэн", "мөнхийн", "наранд", "гэрэлтэнэ"],
                    "correctAnswer": "Эрх мэдэл цагийн урсгалд хуучравч, эгэл үнэн мөнхийн наранд гэрэлтэнэ",
                    "acceptableAlternatives": ["Эрх мэдэл цагийн урсгалд хуучравч, эгэл үнэн мөнхийн наранд гэрэлтэнэ.", "Эрх мэдэл цагийн урсгалд хуучравч эгэл үнэн мөнхийн наранд гэрэлтэнэ"],
                    "hint": "Reconstruct the parallel aphorism by placing the temporal power concessive hemistich first ('power withered in time'), followed by the enduring solar hemistich ('humble truth shining in the eternal sun').",
                    "explanation": "Alliterative and thematic balance: Clause 1 with concessive converb -вч ('хуучравч' = though it ages) + Clause 2 with finite predicate ('гэрэлтэнэ' = shines).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Sublime parallel alliterative Mongolian poetic syntax.",
                        "onFailure": "Follow the sequence: Эрх мэдэл цагийн урсгалд хуучравч, эгэл үнэн мөнхийн наранд гэрэлтэнэ."
                    },
                    "detailedGrammarNote": "Mongolian high-level literary rhetoric relies heavily on initial head-alliteration ('Эрх... эгэл...') and concessive converb symmetry (-вч).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Эрх мэдэл цагийн урсгалд хуучравч, эгэл үнэн мөнхийн наранд гэрэлтэнэ.",
                        "slowSpeechSynthesisText": "эгэл үнэн мөнхийн наранд гэрэлтэнэ.",
                        "ipaTranscription": "/erx metəɮ tsʰaɡiːŋ ʊrsɢəɮtʰ xʊːtʃʰrəwtʃʰ, eɡəɮ unəŋ mɵŋxiːŋ narəŋtʰ ɡerəɮtʰən/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_c2_237_06_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Cloze Insertion: High-Register Literary Concessive Converb -вч",
                    "modality": "MODERNIST_SATIRE_SYNTHESIS",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["literary_converb_mastery", "cloze_accuracy"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["боловч", "гэлээч"],
                    "prompt": "Complete the literary sentence using the single-word concessive converb of 'байх' (to be) formed with -вч:\n\n'Цаг агаар тэсгэм хүйтэн _______, хүмүүсийн сэтгэлийн илч дулаан хэвээр байв.' (Though the weather was bitterly cold, the warmth in people's hearts remained.)",
                    "stimulusTextCyrillic": "тэсгэм хүйтэн _______, сэтгэлийн илч дулаан хэвээр байв",
                    "hint": "Apply the literary synthetic concessive converb suffix (-вч) directly to the existential verbal stem 'бай-'.",
                    "correctAnswer": "байвч",
                    "acceptableAlternatives": ["байвч", "боловч"],
                    "explanation": "'Байвч' (although it was / albeit) is the classic high-register literary concessive converb.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'байвч' provides the exact literary concessive tone.",
                        "onFailure": "Remember that 'байвч' is the elevated literary concessive converb of 'байх'."
                    },
                    "detailedGrammarNote": "While spoken Mongolian uses 'хэдий ч' or 'боловч', elevated literary prose favors synthetic converbs in -вч directly attached to verbal roots ('байвч', 'ирэвч', 'өгүүлрүүн').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Цаг агаар тэсгэм хүйтэн байвч, хүмүүсийн сэтгэлийн илч дулаан байлаа.",
                        "slowSpeechSynthesisText": "хүйтэн байвч, сэтгэлийн илч дулаан.",
                        "ipaTranscription": "/tsʰaɡ aɢaːr tʰeskəm xuitʰəŋ pæːwtʃʰ, xumusʰiːŋ sitɡiɮiːŋ iɮtʃʰ tʰʊɮaːŋ pæːɮaː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_c2_237_06_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "C2 Culminating Literary Critique Defense Rubric",
                    "modality": "MODERNIST_SATIRE_SYNTHESIS",
                    "interactionPattern": "OPEN_RESPONSE_RUBRIC",
                    "cognitiveComplexity": "CREATE_RHETORIC",
                    "skillTargets": ["c2_literary_defense", "holistic_stylistic_evaluation"],
                    "grammarTargets": ["gram_c2_khalkha_rapid_phonotactics_sandhi"],
                    "vocabularyTargets": ["уран зохиолын шинжилгээ", "хэл найруулга", "утга соёл"],
                    "prompt": "Evaluate the learner's spoken defense excerpt analyzing the role of existential absurdity in modern Mongolian theater:\n\n'СҮҮЛИЙН ҮГ БА ШҮҮМЖЛЭЛТ ДҮГНЭЛТ:\nОрчин үеийн монгол жүжгийн зохиолд нүүдэлчдийн уламжлалт хөх тэнгэрийн үзэл ба орчин цагийн даяаршлын завсрын орон зайд хаягдсан хүний ганцаардал тод тусгалаа олжээ. Зохиолч Д.Батбаярын туурвилуудад баатрууд нь уламжлалт ёс заншлаа ч бүрэн тээж чаддаггүй, өрнийн суурин соёлд ч бүрэн уусаж чадалгүй хоёр ертөнцийн зааг дээр \"сүнсээ гээсэн мэт\" амьдардаг. Энэ бол зүгээр нэг хувь хүний эмгэнэл бус, бүхэл бүтэн үндэстний оюун санааны шилжилтийн үеийн гүн хямрал бөгөөд зохиолчийн шог хошин, ёгт хэл найруулга нь энэхүү шархыг улам бүр товойлгон илчилж байна.'\n\nEvaluate against C2 operational criteria: 1. Native-like stylistic fluency and rhetorical architecture, 2. Deep cultural and philosophical synthesis (nomadic vs westernized alienation), 3. Critical integration of literary aesthetics (dramaturgy, irony, tragicomedy).",
                    "stimulusTextCyrillic": "Орчин үеийн монгол жүжгийн зохиолд нүүдэлчдийн уламжлалт хөх тэнгэрийн үзэл ба даяаршлын завсар дахь хүний ганцаардал...",
                    "correctAnswer": "Master-level C2 capstone defense exhibiting native-like rhetorical majesty, deep philosophical articulation of the nomadic-global transition, and penetrating dramaturgical aesthetic critique.",
                    "acceptableAlternatives": ["Master-level C2 capstone defense", "Шалгуурыг бүрэн хангасан", "C2 Operational Mastery Verified"],
                    "hint": "Analyze whether the defense synthesizes philosophical cosmology with literary dramaturgical mechanics in pristine, native-level Mongolian prose.",
                    "explanation": "This response represents the apex of CEFR C2 operational proficiency: synthesizing philosophical depth ('хөх тэнгэрийн үзэл', 'оюун санааны шилжилт'), flawless high-register prose ('хоёр ертөнцийн зааг дээр'), and aesthetic literary dissection.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Extraordinary C2 operational synthesis and literary hermeneutics.",
                        "onFailure": "Verify cultural depth, philosophical synthesis, and rhetorical precision."
                    },
                    "detailedGrammarNote": "Compound philosophical nouns ('завсрын орон зай', 'оюун санааны шилжилт') matched with elevated converb constructions exemplify educated native discourse.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэхүү шүүмжлэлт дүгнэлт нь С2 түвшний уран зохиолын шинжилгээний шалгуурыг бүрэн хангаж байна.",
                        "slowSpeechSynthesisText": "уран зохиолын шинжилгээний шалгуурыг бүрэн хангасан.",
                        "ipaTranscription": "/enəxuː ʃuːmtʃʰɮəɮtʰ tʰuɡnəɮtʰ nʲ seː xɔjər tʰuwʃintʰiːŋ ʊrəŋ tsɔxʲɔːɮiːŋ ʃintʃʰiɮɡeːniː ʃaɮɢʊːriːɡ pʰurəŋ xaŋɢətʃʰ pæːn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "RUBRIC_CRITERIA",
                        "rubricCriteria": [
                            {"criterion": "Native-Like Rhetorical Majesty & Stylistic Control", "points": 35, "description": "Deploys pristine educated Mongolian without foreign syntactic calques."},
                            {"criterion": "Philosophical & Cultural Synthesis", "points": 35, "description": "Penetrates the historical tension between nomadic heritage and modern urban alienation."},
                            {"criterion": "Dramaturgical & Aesthetic Depth", "points": 30, "description": "Dissects the tragicomic and satirical mechanisms of the theatrical text."}
                        ]
                    }
                }
            ]
        }
    ]
