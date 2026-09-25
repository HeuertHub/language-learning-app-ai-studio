#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A2 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_a2_64_01_instrumental_transport_allomorphs (Grammar Introduction)
2. les_a2_64_04_route_maps_schedules_reading (Reading Development)
3. les_a2_65_03_in_cab_navigation_dialogue (Listening Development)
"""

def get_a2_exercises():
    return [
        # LESSON 7: les_a2_64_01_instrumental_transport_allomorphs
        {
            "lessonId": "les_a2_64_01_instrumental_transport_allomorphs",
            "exercises": [
                {
                    "exerciseId": "ex_a2_64_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Instrumental Case Suffix Selection for Transport",
                    "modality": "CASE_SUFFIX_APPLICATION",
                    "interactionPattern": "SUFFIX_ATTACHMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["instrumental_case_allomorphy", "vowel_harmony_transport"],
                    "grammarTargets": ["gram_a2_instrumental_case_transport"],
                    "vocabularyTargets": ["автобус", "автобусаар"],
                    "prompt": "Attach the correct harmonic allomorph of the instrumental case suffix (-аар/-ээр/-оор/-өөр) to the transport noun 'автобус' (bus):",
                    "baseWord": "автобус",
                    "suffixOptions": ["-аар", "-ээр", "-оор", "-өөр"],
                    "correctSuffix": "-аар",
                    "correctAnswer": "автобусаар",
                    "acceptableAlternatives": ["автобусаар", "-аар"],
                    "hint": "Determine whether 'автобус' has masculine back or feminine front vowels, and attach the corresponding four-fold instrumental suffix without rounding.",
                    "explanation": "Because 'автобус' ends in a consonant following back vowel 'у', it attaches the masculine unrounded instrumental suffix '-аар', yielding 'автобусаар' (by bus).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'автобусаар' is correct.",
                        "onFailure": "Back vowel 'у' takes '-аар' -> 'автобусаар'."
                    },
                    "detailedGrammarNote": "The four-fold instrumental case suffix (-аар⁴) designates the means of transportation or instrument. Suffix vowel selection is governed by the vowel of the preceding syllable.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би автобусаар явна.",
                        "slowSpeechSynthesisText": "Би автобусаар явна.",
                        "ipaTranscription": "/pʰi awtʰɔpʊsaːr jawn/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Rounded Vowel Harmony in Instrumental: 'Онгоц'",
                    "modality": "CASE_SUFFIX_APPLICATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["rounding_harmony_application"],
                    "grammarTargets": ["gram_a2_instrumental_case_transport"],
                    "vocabularyTargets": ["онгоц", "онгоцоор"],
                    "prompt": "How do you say 'by airplane' using the noun 'онгоц' and the instrumental case suffix?",
                    "stimulusTextCyrillic": "онгоц",
                    "hint": "The root has vowel 'о', so the suffix must also be rounded 'оор'.",
                    "options": [
                        {"id": "opt_ongotsoor", "text": "онгоцоор (by airplane)", "cyrillic": "онгоцоор", "isCorrect": True, "explanation": "Correct! Labial harmony dictates '-оор' after 'о'."},
                        {"id": "opt_ongotsaar", "text": "*онгоцаар", "cyrillic": "*онгоцаар", "isCorrect": False, "explanation": "Incorrect. Violates rounding harmony (must be -оор after short 'о')."},
                        {"id": "opt_ongotseer", "text": "*онгоцоор", "cyrillic": "*онгоцоор", "isCorrect": False, "explanation": "Incorrect. '-ээр' is front unrounded."},
                        {"id": "opt_ongotsoor_front", "text": "*онгоцөөр", "cyrillic": "*онгоцөөр", "isCorrect": False, "explanation": "Incorrect. 'өөр' is front rounded."}
                    ],
                    "correctAnswer": "онгоцоор (by airplane)",
                    "acceptableAlternatives": ["онгоцоор"],
                    "explanation": "In Khalkha Mongolian, the non-high vowels 'о' and 'ө' enforce labial rounding harmony: after 'о', the suffix must be '-оор' ('онгоцоор').",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! 'онгоцоор' follows labial rounding harmony.",
                        "onFailure": "After 'о', use '-оор' -> 'онгоцоор'."
                    },
                    "detailedGrammarNote": "Rounding harmony (уруулын зохицол) requires suffixes with non-high vowels (а, э, о, ө) to match the rounding of a preceding stem 'о' or 'ө'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Бид Улаанбаатар руу онгоцоор ниссэн.",
                        "slowSpeechSynthesisText": "Бид Улаанбаатар руу онгоцоор ниссэн.",
                        "ipaTranscription": "/pʰitʰ ʊɮaːŋpaːtʰər rʊː ɔŋɢətsʰɔːr nissəŋ/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Foot Transit vs Instrumental Vehicle Contrast",
                    "modality": "CASE_SUFFIX_APPLICATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["locomotion_lexical_idiom", "case_selection"],
                    "grammarTargets": ["gram_a2_instrumental_case_transport"],
                    "vocabularyTargets": ["явган", "машинаар"],
                    "prompt": "To say 'I go to work on foot (walking)', which form is grammatically correct in Mongolian?",
                    "hint": "The adverbial 'явган' (on foot) does NOT take the instrumental suffix '-аар'.",
                    "options": [
                        {"id": "opt_yavgan", "text": "Би явган явдаг. (I go on foot.)", "cyrillic": "Би явган явдаг.", "isCorrect": True, "explanation": "Correct! 'Явган явах' is an idiomatic bare adverbial construction meaning 'to walk/go on foot'."},
                        {"id": "opt_yavganaara", "text": "*Би явганаар явдаг.", "cyrillic": "*Би явганаар явдаг.", "isCorrect": False, "explanation": "Incorrect. Native speakers never attach the instrumental suffix to 'явган'."},
                        {"id": "opt_huluur", "text": "*Би хөлөөрөө явдаг.", "cyrillic": "*Би хөлөөрөө явдаг.", "isCorrect": False, "explanation": "Incorrect. Literal 'by foot' is not standard transit phrasing."}
                    ],
                    "correctAnswer": "Би явган явдаг. (I go on foot.)",
                    "acceptableAlternatives": ["Би явган явдаг.", "явган явдаг"],
                    "explanation": "While vehicles take the instrumental case ('машинаар', 'автобусаар'), pedestrian transit is expressed with the bare root adverb 'явган' + verb.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'явган явах' takes no case suffix.",
                        "onFailure": "'явган' is used without '-аар': 'Би явган явдаг.'."
                    },
                    "detailedGrammarNote": "'Явган' functions as a Manner Adverbial directly preceding the motion verb without nominal case morphology.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би өдөр бүр ажилдаа явган явдаг.",
                        "slowSpeechSynthesisText": "Би өдөр бүр ажилдаа явган явдаг.",
                        "ipaTranscription": "/pʰi ɵtər pʰur atʃʰiɮtʰaː jawɢəŋ jawtəɡ/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Token Assembly: Daily Commute Description",
                    "modality": "CASE_SUFFIX_APPLICATION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["commute_sentence_synthesis", "adverbial_case_ordering"],
                    "grammarTargets": ["gram_a2_instrumental_case_transport", "gram_a1_sov_word_order"],
                    "vocabularyTargets": ["ажилдаа", "машинаар", "явдаг", "би"],
                    "prompt": "Arrange the tokens to form: 'I go to my work by car':",
                    "wordTokens": ["явдаг", "би", "машинаар", "ажилдаа"],
                    "correctTokenOrder": ["би", "ажилдаа", "машинаар", "явдаг"],
                    "correctAnswer": "би ажилдаа машинаар явдаг",
                    "acceptableAlternatives": ["Би ажилдаа машинаар явдаг.", "Би машинаар ажилдаа явдаг"],
                    "hint": "Subject (би) -> Destination (ажилдаа) -> Means (машинаар) -> Verb (явдаг).",
                    "explanation": "Canonical ordering places the directional goal and the instrumental means of transit before the habitual verb 'явдаг'.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Proper word order with instrumental case 'машинаар'.",
                        "onFailure": "Order: би -> ажилдаа -> машинаар -> явдаг."
                    },
                    "detailedGrammarNote": "'Машинаар' attaches '-аар' to 'машин' (car). The reflex-possessive dative-locative 'ажилдаа' indicates 'to one's own work'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Би ажилдаа машинаар явдаг.",
                        "slowSpeechSynthesisText": "Би ажилдаа машинаар явдаг.",
                        "ipaTranscription": "/pʰi atʃʰiɮtʰaː maʃiŋaːr jawtəɡ/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Acoustic Transit Suffix Dictation",
                    "modality": "CASE_SUFFIX_APPLICATION",
                    "interactionPattern": "AUDIO_DICTATION",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["acoustic_case_recognition", "spelling_accuracy"],
                    "grammarTargets": ["gram_a2_instrumental_case_transport"],
                    "vocabularyTargets": ["галт тэргээр"],
                    "prompt": "Listen to the audio sentence: 'Бид Дархан руу _______ явсан' (We went to Darkhan by train). Type the missing word for 'by train':",
                    "stimulusTextCyrillic": "галт тэргээр",
                    "hint": "Identify the two-word compound for 'train' and attach the appropriate front unrounded instrumental case ending with vowel syncope.",
                    "correctAnswer": "галт тэргээр",
                    "acceptableAlternatives": ["галт тэргээр", "Галт тэргээр"],
                    "explanation": "'Галт тэрэг' (train, literally 'fire vehicle') ends in front-vowel 'тэрэг', taking front unrounded instrumental '-ээр' -> 'галт тэргээр'.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'галт тэргээр' spelled accurately.",
                        "onFailure": "Remember: 'галт тэрэг' takes front suffix -ээр with vowel syncope -> 'галт тэргээр'."
                    },
                    "detailedGrammarNote": "Stems ending in 'г' preserve the consonant before the long vowel suffix: тэрэг + -ээр -> тэргээр (with short vowel syncope).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Бид Дархан руу галт тэргээр явсан.",
                        "slowSpeechSynthesisText": "галт тэргээр",
                        "ipaTranscription": "/ɢaɮtʰ tʰirɡeːr/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 8: les_a2_64_04_route_maps_schedules_reading
        {
            "lessonId": "les_a2_64_04_route_maps_schedules_reading",
            "exercises": [
                {
                    "exerciseId": "ex_a2_64_04_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Extracting Operating Hours from Bus Stop Schedule",
                    "modality": "TRANSIT_SCHEDULE_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["timetable_decoding", "temporal_information_extraction"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["эхлэх цаг", "дуусах цаг", "чиглэл"],
                    "prompt": "Read the bus route timetable posted at a shelter in Ulaanbaatar:\n\n[Ч:1 ЧИГЛЭЛ]\n- Эхлэх цаг: 06:30\n- Дуусах цаг: 22:30\n- Хүлээх хугацаа: 8-12 минут\n\nWhat is the earliest departure time (эхлэх цаг) for this route?",
                    "stimulusTextCyrillic": "Эхлэх цаг: 06:30, Дуусах цаг: 22:30",
                    "hint": "'Эхлэх' means 'to start / begin'.",
                    "options": [
                        {"id": "time_0630", "text": "06:30 AM", "cyrillic": "06:30", "isCorrect": True, "explanation": "Correct! 'Эхлэх цаг: 06:30' denotes start of service at 06:30."},
                        {"id": "time_2230", "text": "22:30 PM", "cyrillic": "22:30", "isCorrect": False, "explanation": "Incorrect. 22:30 is the closing time (дуусах цаг)."},
                        {"id": "time_0812", "text": "08:12 AM", "cyrillic": "8-12 минут", "isCorrect": False, "explanation": "Incorrect. 8-12 is the interval headway in minutes."}
                    ],
                    "correctAnswer": "06:30 AM",
                    "acceptableAlternatives": ["06:30", "6:30"],
                    "explanation": "'Эхлэх цаг' means departure start time. The schedule states 06:30.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 06:30 is the start time.",
                        "onFailure": "'Эхлэх цаг' = starting time (06:30)."
                    },
                    "detailedGrammarNote": "Verbal nouns in -х ('эхлэх', 'дуусах', 'хүлээх') function as attributive nouns modifying 'цаг' (time) and 'хугацаа' (duration).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Энэ автобусны эхлэх цаг өглөө зургаан цаг гучин минут.",
                        "slowSpeechSynthesisText": "Эхлэх цаг: 06:30.",
                        "ipaTranscription": "/exɮəx tsʰaɡ tsʊrɢaːŋ tsʰaɡ ɢʊtsʰəŋ mʲinʊtʰ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.9
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_04_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Interpreting Bus Stop Headway & Wait Times",
                    "modality": "TRANSIT_SCHEDULE_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["headway_comprehension", "transit_intervals"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["хүлээх хугацаа", "минут"],
                    "prompt": "According to the sign: 'Хүлээх хугацаа: 8-12 минут' (Waiting duration: 8-12 minutes), how often does a bus arrive during normal operating hours?",
                    "stimulusTextCyrillic": "Хүлээх хугацаа: 8-12 минут",
                    "hint": "'Хугацаа' means duration or interval.",
                    "options": [
                        {"id": "hw_freq", "text": "Every 8 to 12 minutes", "cyrillic": "8-12 минут тутамд", "isCorrect": True, "explanation": "Correct! The bus frequency interval is between 8 and 12 minutes."},
                        {"id": "hw_trip", "text": "The entire trip takes only 8 minutes", "cyrillic": "Явах хугацаа", "isCorrect": False, "explanation": "Incorrect. 'Хүлээх' means waiting, not traveling."},
                        {"id": "hw_delay", "text": "The bus is delayed by 12 hours", "cyrillic": "Хоцролт", "isCorrect": False, "explanation": "Incorrect. The text refers to minutes between buses."}
                    ],
                    "correctAnswer": "Every 8 to 12 minutes",
                    "acceptableAlternatives": ["Every 8 to 12 minutes", "8-12 минут"],
                    "explanation": "'Хүлээх хугацаа' indicates headway frequency between successive transit vehicles.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! You understood headway intervals.",
                        "onFailure": "'Хүлээх хугацаа' = waiting time (8-12 minutes)."
                    },
                    "detailedGrammarNote": "'Хүлээх' derives from the verb 'хүлээ-' (to wait). The suffix '-х' forms the future/habitual participle functioning here as an adjective.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Автобус хоорондын хүлээх хугацаа наймаас арван хоёр минут байна.",
                        "slowSpeechSynthesisText": "Хүлээх хугацаа 8-12 минут.",
                        "ipaTranscription": "/xʊɮiːx xʊɢatsʰaː næːmaːs arwəŋ xɔjər mʲinʊtʰ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_04_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "U-Money Electronic Card Notice Deciphering",
                    "modality": "TRANSIT_SCHEDULE_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["civic_signage_comprehension", "imperative_notice_reading"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["уншуулах", "карт", "бэлэн мөнгө"],
                    "prompt": "Read the red warning banner on the bus door:\n\n'Бэлэн мөнгө авахгүй. Та U-Money картаа заавал уншуулна уу.'\n\nWhat does this notice instruct passengers to do?",
                    "stimulusTextCyrillic": "Бэлэн мөнгө авахгүй. Та U-Money картаа заавал уншуулна уу.",
                    "hint": "'Бэлэн мөнгө' is cash; 'уншуулах' means to tap/scan a card.",
                    "options": [
                        {"id": "umoney_tap", "text": "Cash is not accepted; you must tap your U-Money card.", "cyrillic": "U-Money картаа заавал уншуулна уу", "isCorrect": True, "explanation": "Correct! Cash ('бэлэн мөнгө') is rejected and tapping the smart card is mandatory ('заавал')."},
                        {"id": "umoney_cash", "text": "You can pay with cash or card freely.", "cyrillic": "Бэлэн мөнгө авна", "isCorrect": False, "explanation": "Incorrect. 'Бэлэн мөнгө авахгүй' means cash is NOT accepted."},
                        {"id": "umoney_free", "text": "Transit is completely free today.", "cyrillic": "Үнэгүй", "isCorrect": False, "explanation": "Incorrect. You must pay via card."}
                    ],
                    "correctAnswer": "Cash is not accepted; you must tap your U-Money card.",
                    "acceptableAlternatives": ["Cash is not accepted; you must tap your U-Money card.", "U-Money картаа заавал уншуулна уу"],
                    "explanation": "'Бэлэн мөнгө авахгүй' (No cash accepted). 'Та U-Money картаа заавал уншуулна уу' (Please be sure to scan your U-Money card).",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Cashless bus transit rule understood.",
                        "onFailure": "Notice states: No cash accepted, tap your U-Money card."
                    },
                    "detailedGrammarNote": "'Уншуулах' is the causative form of 'унших' (to read). In transit tech, it means 'to have the machine read / to tap' a card.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Бэлэн мөнгө авахгүй. Та Ю-Мани картаа заавал уншуулна уу.",
                        "slowSpeechSynthesisText": "Бэлэн мөнгө авахгүй. Та Ю-Мани картаа заавал уншуулна уу.",
                        "ipaTranscription": "/pʰeɮəŋ mɵŋɡ əwəxɢuː. tʰa jʊː-manʲi xʰartʰaː tsaːwəɮ ʊŋʃʊːɮnə ʊː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_04_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Route Orientation: Eastbound vs Westbound Directions",
                    "modality": "TRANSIT_SCHEDULE_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["directional_terminology", "route_map_navigation"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["баруун тийш", "зүүн тийш"],
                    "prompt": "You are at 'Сүхбаатарын талбай' and want to go towards the Officers' Palace (Офицеруудын ордон), which is located in the eastern part of Ulaanbaatar. Which platform direction should you board?",
                    "hint": "'Зүүн' means East; 'тийш' is the directive postposition ('towards').",
                    "options": [
                        {"id": "dir_east", "text": "Зүүн тийш явах чиглэл (Eastbound direction)", "cyrillic": "Зүүн тийш", "isCorrect": True, "explanation": "Correct! Officers' Palace is located in the East ('зүүн тийш')."},
                        {"id": "dir_west", "text": "Баруун тийш явах чиглэл (Westbound direction)", "cyrillic": "Баруун тийш", "isCorrect": False, "explanation": "Incorrect. 'Баруун тийш' heads toward Dragon Terminal (Драгон) in the West."},
                        {"id": "dir_south", "text": "Хойшоо явах чиглэл (Northbound direction)", "cyrillic": "Хойшоо", "isCorrect": False, "explanation": "Incorrect. Heading towards 7 Buudal in the North."}
                    ],
                    "correctAnswer": "Зүүн тийш явах чиглэл (Eastbound direction)",
                    "acceptableAlternatives": ["Зүүн тийш", "Зүүн тийш явах чиглэл"],
                    "explanation": "Ulaanbaatar main transit axes run East-West along Peace Avenue (Энхтайваны өргөн чөлөө). 'Зүүн тийш' means towards the East.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'Зүүн тийш' is eastbound.",
                        "onFailure": "East is 'зүүн', so look for 'Зүүн тийш'."
                    },
                    "detailedGrammarNote": "Direction in Mongolian combines the cardinal point noun with the directive postposition 'тийш/тийшээ' (towards).",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Офицеруудын ордон руу зүүн тийш явах автобусанд сууна.",
                        "slowSpeechSynthesisText": "Зүүн тийш явах автобус.",
                        "ipaTranscription": "/tsuːŋ tʰiːʃ jəwəx awtʰɔpʊs/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_64_04_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Transit Disruption Notice Reading Comprehension",
                    "modality": "TRANSIT_SCHEDULE_READING",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["disruption_notice_comprehension", "public_service_announcements"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["замын засвар", "түр зогсохгүй", "тойрч явах"],
                    "prompt": "Read this municipal transit bulletin:\n\n'Замын засварын ажилтай холбогдуулан 9-р сарын 25-ны өдөр Ч:5 чиглэлийн автобус Төв Шуудангийн зогсоолд түр зогсохгүй. Нарны замаар тойрч явна.'\n\nWhy will the Ch:5 bus bypass the Central Post Office stop today?",
                    "stimulusTextCyrillic": "Замын засварын ажилтай холбогдуулан ... Төв Шуудангийн зогсоолд түр зогсохгүй.",
                    "hint": "'Замын засвар' means road repair.",
                    "options": [
                        {"id": "dis_repair", "text": "Due to road repair work, it will detour via Sun Road and not stop at Central Post Office.", "cyrillic": "Замын засварын улмаас зогсохгүй", "isCorrect": True, "explanation": "Correct! 'Замын засварын ажилтай холбогдуулан' = in connection with road repairs."},
                        {"id": "dis_inspection", "text": "Scheduled route inspection: The line is undergoing scheduled mechanical testing and route audit.", "cyrillic": "Шугам замын үзлэг шалгалтын улмаас", "isCorrect": False, "explanation": "Incorrect. The notice specifically states road repair work (замын засвар)."},
                        {"id": "dis_holiday", "text": "It is a national holiday and all buses are suspended.", "cyrillic": "Баяр", "isCorrect": False, "explanation": "Incorrect. Service is running but detouring."}
                    ],
                    "correctAnswer": "Due to road repair work, it will detour via Sun Road and not stop at Central Post Office.",
                    "acceptableAlternatives": ["Due to road repair work", "Замын засварын ажилтай холбогдуулан"],
                    "explanation": "'Замын засвар' = road repair. The notice explains that Ch:5 will detour via Narны зам (Sun Road) without stopping at Central Post Office.",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Complex municipal disruption notice decoded accurately.",
                        "onFailure": "The notice states the bus detours due to road repairs (замын засвар)."
                    },
                    "detailedGrammarNote": "The chancellery postpositional phrase '-тай холбогдуулан' (in connection with / due to) governs nominalized cause phrases in administrative notices.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Замын засварын ажилтай холбогдуулан автобус Төв Шууданд зогсохгүй.",
                        "slowSpeechSynthesisText": "Замын засварын ажилтай холбогдуулан түр зогсохгүй.",
                        "ipaTranscription": "/tsamiːŋ tsaswəriːŋ atʃʰiɮtʰæː xɔɮpɔɢtʰʊːɮəŋ awtʰɔpʊs tʰɵw ʃʊːtəŋtʰ tsɔɡsɔxɢuː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 9: les_a2_65_03_in_cab_navigation_dialogue
        {
            "lessonId": "les_a2_65_03_in_cab_navigation_dialogue",
            "exercises": [
                {
                    "exerciseId": "ex_a2_65_03_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Acoustic Dissection: Micro-Turn Commands in Cab",
                    "modality": "ACOUSTIC_MICRO_DIRECTION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["in_cab_listening_comprehension", "spatial_turn_directives"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["баруун гар тийшээ", "эргээрэй"],
                    "prompt": "Listen to the passenger giving a directional command to the taxi driver:\n\n'Ах аа, энэ уулзвараар баруун гар тийшээ эргээрэй.'\n\nWhich direction did the passenger instruct the driver to turn?",
                    "stimulusTextCyrillic": "Ах аа, энэ уулзвараар баруун гар тийшээ эргээрэй.",
                    "hint": "'Баруун гар тийшээ' = to the right hand side.",
                    "options": [
                        {"id": "turn_right", "text": "Turn right at this intersection (Баруун гар тийшээ)", "cyrillic": "Баруун гар тийшээ эргээрэй", "isCorrect": True, "explanation": "Correct! 'Баруун' is right and 'эргээрэй' is please turn."},
                        {"id": "turn_left", "text": "Turn left at this intersection (Зүүн гар тийшээ)", "cyrillic": "Зүүн гар тийшээ эргээрэй", "isCorrect": False, "explanation": "Incorrect. Left is 'зүүн гар тийшээ'."},
                        {"id": "turn_straight", "text": "Go straight through the intersection (Шулуун яваарай)", "cyrillic": "Шулуун яваарай", "isCorrect": False, "explanation": "Incorrect. Straight is 'чигээрээ / шулуун'."}
                    ],
                    "correctAnswer": "Turn right at this intersection (Баруун гар тийшээ)",
                    "acceptableAlternatives": ["Turn right", "Баруун гар тийшээ эргээрэй", "Баруун гар тийшээ"],
                    "explanation": "'Баруун гар тийшээ эргээрэй' means 'Please turn right'. 'Уулзвараар' uses the instrumental case denoting passage through the intersection.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'Баруун' is right.",
                        "onFailure": "Listen for 'баруун гар тийшээ' (to the right)."
                    },
                    "detailedGrammarNote": "In Mongolian taxi parlance, addresses like 'Ах аа' (older brother / sir) are universally polite colloquial vocatives for male drivers.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Ах аа, энэ уулзвараар баруун гар тийшээ эргээрэй.",
                        "slowSpeechSynthesisText": "Энэ уулзвараар баруун гар тийшээ эргээрэй.",
                        "ipaTranscription": "/ax aː, en ʊːɮtswəraːr pʰarʊːŋ ɡar tʰiːʃeː erɡeːreː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85,
                        "acousticEnvironment": "in_cab_ambient_traffic"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_65_03_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Stop Command Relative to Traffic Light Threshold",
                    "modality": "ACOUSTIC_MICRO_DIRECTION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["threshold_postposition_comprehension", "stopping_instructions"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["гэрлэн дохио", "өнгөрөөд", "зогсоорой"],
                    "prompt": "Listen to the passenger instruction: 'Гэрлэн дохио өнгөрөөд замын хажууд зогсоорой.' Where should the driver pull over?",
                    "stimulusTextCyrillic": "Гэрлэн дохио өнгөрөөд замын хажууд зогсоорой.",
                    "hint": "'Өнгөрөөд' means 'having passed / past', and 'замын хажууд' means 'at the side of the road'.",
                    "options": [
                        {"id": "loc_past_light", "text": "Right past the traffic light, on the side of the road.", "cyrillic": "Гэрлэн дохио өнгөрөөд", "isCorrect": True, "explanation": "Correct! Converb '-өөд' in 'өнгөрөөд' indicates action sequence: pass the light first, then stop roadside."},
                        {"id": "loc_before_light", "text": "Before reaching the traffic light in the middle lane.", "cyrillic": "Гэрлэн дохионы наана", "isCorrect": False, "explanation": "Incorrect. 'Өнгөрөөд' means past the light."},
                        {"id": "loc_u_turn", "text": "Make a U-turn at the traffic light.", "cyrillic": "Буцаж эргэх", "isCorrect": False, "explanation": "Incorrect. No U-turn requested."}
                    ],
                    "correctAnswer": "Right past the traffic light, on the side of the road.",
                    "acceptableAlternatives": ["Right past the traffic light", "Гэрлэн дохио өнгөрөөд"],
                    "explanation": "'Гэрлэн дохио' (traffic light) + 'өнгөрөөд' (having passed) + 'замын хажууд зогсоорой' (please stop at the roadside).",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Accurate comprehension of motion converb 'өнгөрөөд'.",
                        "onFailure": "'Өнгөрөөд' means after passing the light."
                    },
                    "detailedGrammarNote": "The successive converb in -аад⁴ ('өнгөрөөд') expresses sequential action: after performing the first action, immediately execute the second.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Гэрлэн дохио өнгөрөөд замын хажууд зогсоорой.",
                        "slowSpeechSynthesisText": "Гэрлэн дохио өнгөрөөд замын хажууд зогсоорой.",
                        "ipaTranscription": "/ɡerɮəŋ tʰɔxʲɔː ɵŋɡɵrɵːtʰ tsamiːŋ xatʃʊːtʰ tsɔɡsɔːreː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_65_03_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Token Assembly: Straight Ahead Micro-Direction",
                    "modality": "ACOUSTIC_MICRO_DIRECTION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["spontaneous_direction_giving", "imperative_assembly"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["шулуун", "гүүр", "даваад", "яваарай"],
                    "prompt": "Assemble the tokens to tell the driver: 'Cross the bridge and keep going straight':",
                    "wordTokens": ["яваарай", "даваад", "гүүр", "шулуун"],
                    "correctTokenOrder": ["гүүр", "даваад", "шулуун", "яваарай"],
                    "correctAnswer": "гүүр даваад шулуун яваарай",
                    "acceptableAlternatives": ["Гүүр даваад шулуун яваарай.", "гүүр даваад чигээрээ яваарай"],
                    "hint": "Bridge (гүүр) -> having crossed (даваад) -> straight (шулуун) -> please go (яваарай).",
                    "explanation": "Object noun + sequential converb 'даваад' precedes the manner adverb 'шулуун' and imperative 'яваарай'.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! Natural navigation command formed.",
                        "onFailure": "Sequence: гүүр -> даваад -> шулуун -> яваарай."
                    },
                    "detailedGrammarNote": "'Давах' means to cross over (a mountain pass, hill, or bridge). With converb '-аад', it coordinates the route action.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Гүүр даваад шулуун яваарай.",
                        "slowSpeechSynthesisText": "Гүүр даваад шулуун яваарай.",
                        "ipaTranscription": "/ɡuːr tʰawaːtʰ ʃʊɮʊːŋ jəwaːreː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_a2_65_03_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Fare Negotiation Under Ambient Street Noise",
                    "modality": "ACOUSTIC_MICRO_DIRECTION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["street_hail_listening", "numeral_fare_comprehension"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["километр", "хэд", "мянган төгрөг"],
                    "prompt": "Listen to the street hail exchange through traffic noise:\n\nPassenger: 'Багшийн дээд хүртэл явах уу?'\nDriver: 'За суучих. Нэг километр нь хоёр мянган төгрөг шүү.'\n\nWhat is the driver's rate per kilometer?",
                    "stimulusTextCyrillic": "Нэг километр нь хоёр мянган төгрөг шүү.",
                    "hint": "2000 = хоёр мянга.",
                    "options": [
                        {"id": "fare_2000", "text": "2,000 MNT per kilometer", "cyrillic": "2000 төгрөг", "isCorrect": True, "explanation": "Correct! 'Хоёр мянган төгрөг' is 2,000 MNT."},
                        {"id": "fare_1500", "text": "1,500 MNT per kilometer", "cyrillic": "1500 төгрөг", "isCorrect": False, "explanation": "Incorrect. Driver specified 2000 MNT."},
                        {"id": "fare_3000", "text": "3,000 MNT flat rate", "cyrillic": "3000 төгрөг", "isCorrect": False, "explanation": "Incorrect. Rate is 2000 per km."}
                    ],
                    "correctAnswer": "2,000 MNT per kilometer",
                    "acceptableAlternatives": ["2,000 MNT", "2000", "хоёр мянга"],
                    "explanation": "The unofficial street taxi driver agreed to drive ('За суучих') and quoted 2,000 MNT per kilometer ('хоёр мянган төгрөг').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! Street taxi fare extracted through noise.",
                        "onFailure": "Driver stated: 'Хоёр мянган төгрөг' = 2,000 MNT."
                    },
                    "detailedGrammarNote": "In informal street hailing (гар өргөх), drivers state their per-kilometer rate followed by emphatic particle 'шүү' ('хоёр мянган төгрөг шүү').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "За суучих. Нэг километр нь хоёр мянган төгрөг шүү.",
                        "slowSpeechSynthesisText": "Нэг километр нь хоёр мянган төгрөг шүү.",
                        "ipaTranscription": "/tsa sʊːtʃʰix. nʲeɡ xʲiɮɔmʲetʰər nʲ xɔjər mʲaŋɢəŋ tʰɵɡrɵɡ ʃuː/",
                        "speakerRole": "male_native",
                        "speechRate": 0.9,
                        "acousticEnvironment": "street_traffic_noise"
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_a2_65_03_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Cloze Insertion: Landmark-Relative Stop Instruction",
                    "modality": "ACOUSTIC_MICRO_DIRECTION",
                    "interactionPattern": "CLOZE_TEXT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["spatial_postposition_cloze", "in_cab_prompt"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["урд талд", "зогсох"],
                    "prompt": "You want the driver to stop in front of the central Department Store (Их Дэлгүүр). Fill in the spatial postposition for 'in front of':\n\n'Их Дэлгүүрийн ______ талд буулгаад өгөөрэй.'",
                    "stimulusTextCyrillic": "Их Дэлгүүрийн ______ талд буулгаад өгөөрэй.",
                    "hint": "Consider the cardinal/spatial antonym of 'хойд' (back/north) commonly used in Mongolian urban directions for frontal location.",
                    "correctAnswer": "урд",
                    "acceptableAlternatives": ["урд", "Урд"],
                    "explanation": "'Урд талд' means 'in front of / on the south side'. Combined with 'буулгаад өгөөрэй' (please drop me off).",
                    "learnerFeedback": {
                        "onSuccess": "Гайхалтай! 'урд талд' is the precise spatial postposition.",
                        "onFailure": "Remember that 'урд талд' expresses 'in front of' (opposite of 'хойд талд')."
                    },
                    "detailedGrammarNote": "Postpositions of orientation (урд талд, ард талд, баруун талд, зүүн талд) systematically govern preceding nouns in the genitive case ('Их Дэлгүүрийн').",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Их Дэлгүүрийн урд талд буулгаад өгөөрэй.",
                        "slowSpeechSynthesisText": "Их Дэлгүүрийн урд талд буулгаад өгөөрэй.",
                        "ipaTranscription": "/ix tʰeɮɡuːriːŋ ʊrtʰ tʰaɮtʰ pʊːɮɢaːtʰ ɵɡɵːreː/",
                        "speakerRole": "female_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        }
    ]
