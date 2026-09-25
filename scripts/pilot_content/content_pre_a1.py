#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pre-A1 Pilot Exercise Content for Phase 3B
3 Lessons:
1. les_pre_a1_01_01_shared_consonants_visual (Orthography)
2. les_pre_a1_02_02_auditory_discrimination_minimal_pairs (Phonology)
3. les_pre_a1_03_03_vowel_harmony_intro_roots (Grammar Introduction)
"""

def get_pre_a1_exercises():
    return [
        # LESSON 1: les_pre_a1_01_01_shared_consonants_visual
        {
            "lessonId": "les_pre_a1_01_01_shared_consonants_visual",
            "exercises": [
                {
                    "exerciseId": "ex_pre_a1_01_01_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Recognizing Shared Cyrillic Capital 'М'",
                    "modality": "ORTHOGRAPHY_RECOGNITION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "REMEMBER_RECOGNIZE",
                    "skillTargets": ["visual_grapheme_recognition", "cyrillic_letter_identification"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["М", "м"],
                    "prompt": "Identify the Cyrillic letter that represents the bilabial nasal consonant /m/ (equivalent in visual shape to Latin 'M').",
                    "stimulusTextCyrillic": "М",
                    "hint": "Look for the letter identical in form to the English uppercase 'M'.",
                    "options": [
                        {"id": "opt_1", "text": "М", "cyrillic": "М", "isCorrect": True, "explanation": "Correct! Cyrillic 'М' represents /m/ and shares its glyph form with Latin 'M'."},
                        {"id": "opt_2", "text": "И", "cyrillic": "И", "isCorrect": False, "explanation": "Incorrect. 'И' represents the vowel /i/, which looks like a reversed 'N'."},
                        {"id": "opt_3", "text": "П", "cyrillic": "П", "isCorrect": False, "explanation": "Incorrect. 'П' represents the voiceless stop /p/ (Greek Pi)."},
                        {"id": "opt_4", "text": "Л", "cyrillic": "Л", "isCorrect": False, "explanation": "Incorrect. 'Л' represents the lateral liquid /l/."}
                    ],
                    "correctAnswer": "М",
                    "acceptableAlternatives": ["М", "м"],
                    "explanation": "Cyrillic uppercase 'М' and lowercase 'м' represent the voiced bilabial nasal consonant /m/. It is visually identical to Latin 'M'.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! You correctly recognized Cyrillic 'М'.",
                        "onFailure": "Remember, Cyrillic 'М' looks identical to the Latin letter 'M'."
                    },
                    "detailedGrammarNote": "Modern Mongolian Cyrillic shares several glyphs directly with Latin: A, O, M, T, K. Consonant 'М' corresponds to the universal bilabial nasal phoneme [m].",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "М",
                        "slowSpeechSynthesisText": "М",
                        "ipaTranscription": "/m/",
                        "speakerRole": "narrator",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "EXACT",
                        "caseSensitive": True
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_01_01_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Matching Lowercase and Uppercase Shared Consonants",
                    "modality": "ORTHOGRAPHY_RECOGNITION",
                    "interactionPattern": "PAIR_MATCHING",
                    "cognitiveComplexity": "REMEMBER_RECOGNIZE",
                    "skillTargets": ["grapheme_case_pairing"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["Т", "т", "К", "к", "О", "о", "А", "а"],
                    "prompt": "Pair each uppercase Cyrillic letter with its exact lowercase partner for the shared letters Т, К, О, А.",
                    "stimulusTextCyrillic": "Т, К, О, А",
                    "hint": "Cyrillic lowercase letters generally mirror their uppercase shapes in reduced height.",
                    "options": [
                        {"id": "pair_t", "text": "Т -> т", "cyrillic": "Т - т", "isCorrect": True, "explanation": "Т matches lowercase т."},
                        {"id": "pair_k", "text": "К -> к", "cyrillic": "К - к", "isCorrect": True, "explanation": "К matches lowercase к."},
                        {"id": "pair_o", "text": "О -> о", "cyrillic": "О - о", "isCorrect": True, "explanation": "О matches lowercase о."},
                        {"id": "pair_a", "text": "А -> а", "cyrillic": "А - а", "isCorrect": True, "explanation": "А matches lowercase а."}
                    ],
                    "correctAnswer": "Т-т, К-к, О-о, А-а",
                    "acceptableAlternatives": ["Т:т, К:к, О:о, А:а", "Т-т К-к О-о А-а"],
                    "explanation": "In printed Cyrillic, letters like Т, К, О, and А have identical letterforms in uppercase and lowercase, varying only in font size.",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! All case pairings match correctly.",
                        "onFailure": "Check each letter: Т-т, К-к, О-о, А-а."
                    },
                    "detailedGrammarNote": "Unlike Latin handwriting where cursive 't' differs substantially from 'T', Mongolian Cyrillic print preserves the uniform bar top for both uppercase Т and lowercase т.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "Т, К, О, А",
                        "slowSpeechSynthesisText": "Т, К, О, А",
                        "ipaTranscription": "/t/, /k/, /ɔ/, /a/",
                        "speakerRole": "narrator",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_01_01_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Distinguishing True Consonant 'К' in Loanwords",
                    "modality": "ORTHOGRAPHY_RECOGNITION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["loanword_phonology_recognition"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["кино", "карт", "кофе"],
                    "prompt": "Which of the following common Mongolian loanwords begins with the shared Cyrillic consonant 'К'?",
                    "stimulusTextCyrillic": "кино",
                    "hint": "Think of the international word for cinema / movie.",
                    "options": [
                        {"id": "opt_kino", "text": "кино (cinema / movie)", "cyrillic": "кино", "isCorrect": True, "explanation": "Correct! 'кино' begins with Cyrillic 'к'."},
                        {"id": "opt_nom", "text": "ном (book)", "cyrillic": "ном", "isCorrect": False, "explanation": "Incorrect. 'ном' begins with 'н'."},
                        {"id": "opt_ger", "text": "гэр (home / yurta)", "cyrillic": "гэр", "isCorrect": False, "explanation": "Incorrect. 'гэр' begins with 'г'."},
                        {"id": "opt_us", "text": "ус (water)", "cyrillic": "ус", "isCorrect": False, "explanation": "Incorrect. 'ус' begins with vowel 'у'."}
                    ],
                    "correctAnswer": "кино",
                    "acceptableAlternatives": ["кино (cinema / movie)"],
                    "explanation": "Cyrillic 'К' appears predominantly in international loanwords in Mongolian such as 'кино' (movie), 'карт' (card), and 'кофе' (coffee).",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'кино' is spelled with initial Cyrillic 'к'.",
                        "onFailure": "Remember: 'кино' starts with 'к'."
                    },
                    "detailedGrammarNote": "Native Mongolian vocabulary uses 'г' and 'х' for velar and uvular stops/fricatives. The letter 'к' was introduced into the Cyrillic orthography primarily to accommodate 20th-century Russian and international loan vocabulary.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "кино",
                        "slowSpeechSynthesisText": "кино",
                        "ipaTranscription": "/kʲinɔ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.9
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_01_01_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Token Identification: Shared Letters in 'ТАМГА'",
                    "modality": "ORTHOGRAPHY_RECOGNITION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["grapheme_assembly", "spelling_decoding"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["тамга"],
                    "prompt": "Arrange the scrambled letters to spell the classical cultural word 'тамга' (seal/stamp), observing the shared consonants Т, М, and vowel А.",
                    "contextSentence": "Төрийн сүлд тамга (State seal and stamp)",
                    "wordTokens": ["г", "а", "т", "а", "м"],
                    "correctTokenOrder": ["т", "а", "м", "г", "а"],
                    "correctAnswer": "тамга",
                    "acceptableAlternatives": ["ТАМГА"],
                    "hint": "The word starts with 'т', followed by 'а' and 'м'.",
                    "explanation": "Т-а-м-г-а spells 'тамга' (seal, stamp). It contains shared consonants т and м along with back vowel а.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'тамга' assembled perfectly.",
                        "onFailure": "Follow the sequence: т -> а -> м -> г -> а."
                    },
                    "detailedGrammarNote": "'Тамга' is a historical and cultural term designating sovereign stamps, clan seals, and brand marks throughout Central Asia.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "тамга",
                        "slowSpeechSynthesisText": "тамга",
                        "ipaTranscription": "/tʰamɢa/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_01_01_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Acoustic Consonant Transcription: /t/ and /m/",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "AUDIO_DICTATION",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["phoneme_grapheme_mapping", "dictation_accuracy"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ном", "том"],
                    "prompt": "Listen to the spoken audio and type the two-letter word with shared consonant Т: 'то' or 'та'?",
                    "stimulusTextCyrillic": "та",
                    "hint": "Listen for the open low back vowel /a/ after /tʰ/.",
                    "correctAnswer": "та",
                    "acceptableAlternatives": ["Та", "ТА"],
                    "explanation": "The speaker pronounced 'та' (/tʰa/), which is also the formal second-person pronoun ('you').",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! You transcribed 'та' correctly.",
                        "onFailure": "Listen closely to the audio: 'т' followed by 'а' -> 'та'."
                    },
                    "detailedGrammarNote": "'Та' functions both as an orthographic syllable demonstrating consonants Т and А and as the essential polite pronoun of address in Mongolian.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "та",
                        "slowSpeechSynthesisText": "та",
                        "ipaTranscription": "/tʰa/",
                        "speakerRole": "female_native",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                }
            ]
        },

        # LESSON 2: les_pre_a1_02_02_auditory_discrimination_minimal_pairs
        {
            "lessonId": "les_pre_a1_02_02_auditory_discrimination_minimal_pairs",
            "exercises": [
                {
                    "exerciseId": "ex_pre_a1_02_02_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Auditory Minimal Pair Contrast: О vs Ө",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["acoustic_phonetic_discrimination", "vowel_backness_auditory"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["мод", "мөр"],
                    "prompt": "Listen to the audio recording. Did the speaker pronounce back rounded vowel word 'мод' (tree/wood) or front rounded vowel word 'мөр' (shoulder/path)?",
                    "stimulusTextCyrillic": "мөр",
                    "hint": "Notice whether the vowel resonance sounds deep and guttural (О) or mid-front and rounded (Ө).",
                    "options": [
                        {"id": "opt_mor", "text": "мөр (shoulder / line / path)", "cyrillic": "мөр", "isCorrect": True, "explanation": "Correct! The speaker pronounced the front rounded vowel /ө/ in 'мөр'."},
                        {"id": "opt_mod", "text": "мод (wood / tree)", "cyrillic": "мод", "isCorrect": False, "explanation": "Incorrect. 'мод' contains the back rounded vowel /ɔ/."}
                    ],
                    "correctAnswer": "мөр",
                    "acceptableAlternatives": ["мөр (shoulder / line / path)"],
                    "explanation": "Cyrillic 'Ө' represents the front mid-rounded vowel /ө/ [ɵ], contrasting with 'О' which represents the back low-mid rounded vowel [ɔ].",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! You distinguished the front vowel 'ө' in 'мөр'.",
                        "onFailure": "Listen to the tongue position: 'ө' is higher and forward compared to 'о'."
                    },
                    "detailedGrammarNote": "The phonemic contrast between back /ɔ/ and front /ө/ is fundamental to Khalkha phonology and governs root vowel harmony throughout the language.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "мөр",
                        "slowSpeechSynthesisText": "мөр",
                        "ipaTranscription": "/mɵr/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_02_02_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Auditory Discrimination: High Back 'У' vs High Front 'Ү'",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["high_vowel_discrimination", "minimal_pair_decoding"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ус", "үс"],
                    "prompt": "Listen carefully to the audio stimulus. Which word was spoken: 'ус' (water) or 'үс' (hair)?",
                    "stimulusTextCyrillic": "ус",
                    "hint": "The back vowel 'у' has a pharyngeal resonance /ʊ/, while 'ү' is a front close vowel /u/.",
                    "options": [
                        {"id": "opt_us", "text": "ус (water) - Back vowel У", "cyrillic": "ус", "isCorrect": True, "explanation": "Correct! The audio features the retracted back vowel /ʊ/ in 'ус'."},
                        {"id": "opt_ys", "text": "үс (hair) - Front vowel Ү", "cyrillic": "үс", "isCorrect": False, "explanation": "Incorrect. 'үс' has a higher, fronted vowel quality /u/."}
                    ],
                    "correctAnswer": "ус",
                    "acceptableAlternatives": ["ус", "ус (water)"],
                    "explanation": "Mongolian 'ус' (/ʊs/) uses the back rounded vowel У, whereas 'үс' (/us/) uses the front close rounded vowel Ү.",
                    "learnerFeedback": {
                        "onSuccess": "Зөв! That was 'ус' (water) with back vowel У.",
                        "onFailure": "The spoken token has a deeper back tongue position: 'ус'."
                    },
                    "detailedGrammarNote": "In Mongolian linguistic terminology, 'у' belongs to the masculine vowels (эр эгшиг), while 'ү' belongs to the feminine vowels (эм эгшиг). Conflating them changes word meaning completely.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "ус",
                        "slowSpeechSynthesisText": "ус",
                        "ipaTranscription": "/ʊs/",
                        "speakerRole": "female_native",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_02_02_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Phonetic Categorization: Sorting Spoken Roots by Vowel Backness",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["vowel_resonance_auditory_classification"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["сүү", "сур"],
                    "prompt": "Listen to the word: 'сүү' (milk). Does it contain a Front (feminine) vowel or a Back (masculine) vowel?",
                    "stimulusTextCyrillic": "сүү",
                    "hint": "The letter 'ү' is written with a vertical tick through the center and sounds like high front /u/.",
                    "options": [
                        {"id": "cat_front", "text": "Front (Эм эгшиг) - vowel Ү", "cyrillic": "Эм эгшиг", "isCorrect": True, "explanation": "Correct! 'сүү' features the long front rounded vowel үү."},
                        {"id": "cat_back", "text": "Back (Эр эгшиг) - vowel У", "cyrillic": "Эр эгшиг", "isCorrect": False, "explanation": "Incorrect. 'сүү' contains front vowel ү, not back vowel у."}
                    ],
                    "correctAnswer": "Front (Эм эгшиг) - vowel Ү",
                    "acceptableAlternatives": ["Front", "Эм эгшиг", "Front (Эм эгшиг)"],
                    "explanation": "'Сүү' (milk) is formed with the long front vowel 'үү', placing it squarely in the feminine (front) harmonic class.",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'Сүү' is an exemplary front-vowel root.",
                        "onFailure": "Remember: 'ү' belongs to the front (эм) vowel class."
                    },
                    "detailedGrammarNote": "Long vowels in Mongolian are orthographically represented by double letters (аа, ээ, оо, өө, уу, үүү). Their harmonic class matches their single counterpart.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "сүү",
                        "slowSpeechSynthesisText": "сүү",
                        "ipaTranscription": "/suː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_02_02_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Minimal Pair Dictation: Өдөр vs Үнэн",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "AUDIO_DICTATION",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["spelling_from_acoustic_stimulus", "front_vowel_transcription"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["өдөр"],
                    "prompt": "Listen to the word meaning 'day' and type the Cyrillic spelling using the front vowel Ө:",
                    "stimulusTextCyrillic": "өдөр",
                    "hint": "Transcribe the mid-front rounded vowel 'ө' followed by alveolar stop 'д' and coda 'р'.",
                    "correctAnswer": "өдөр",
                    "acceptableAlternatives": ["Өдөр", "ӨДӨР"],
                    "explanation": "'Өдөр' (/өдөр/ [ɵtər]) means 'day'. It exemplifies harmonic assimilation where both vowels are mid-front 'ө'.",
                    "learnerFeedback": {
                        "onSuccess": "Гайхалтай! You spelled 'өдөр' with exact Cyrillic letters.",
                        "onFailure": "Remember that the word for 'day' has front rounded vowels: 'өдөр'."
                    },
                    "detailedGrammarNote": "Non-initial vowels in Khalkha Mongolian undergo reduction, but orthography preserves the harmonic front vowel symbol 'ө'.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "өдөр",
                        "slowSpeechSynthesisText": "өдөр",
                        "ipaTranscription": "/ɵtər/",
                        "speakerRole": "male_native",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "CASE_INSENSITIVE"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_02_02_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Auditory Identification: Detecting the Odd Vowel Out",
                    "modality": "AUDITORY_DISCRIMINATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["auditory_pattern_recognition", "vowel_harmony_perception"],
                    "grammarTargets": [],
                    "vocabularyTargets": ["ус", "сум", "нут", "гэр"],
                    "prompt": "Three of these words contain back vowels (эр эгшиг). Which word contains a FRONT vowel (эм эгшиг)?",
                    "stimulusTextCyrillic": "ус, сум, нут, гэр",
                    "hint": "Listen for the unrounded front vowel 'э'.",
                    "options": [
                        {"id": "opt_ger", "text": "гэр (home) - vowel Э", "cyrillic": "гэр", "isCorrect": True, "explanation": "Correct! 'гэр' contains the front vowel 'э'."},
                        {"id": "opt_us", "text": "ус (water) - vowel У", "cyrillic": "ус", "isCorrect": False, "explanation": "Incorrect. 'ус' contains the back vowel 'у'."},
                        {"id": "opt_sum", "text": "сум (arrow/district) - vowel У", "cyrillic": "сум", "isCorrect": False, "explanation": "Incorrect. 'сум' contains back vowel 'у'."},
                        {"id": "opt_nut", "text": "нут (homeland root) - vowel У", "cyrillic": "нут", "isCorrect": False, "explanation": "Incorrect. 'нут' contains back vowel 'у'."}
                    ],
                    "correctAnswer": "гэр (home) - vowel Э",
                    "acceptableAlternatives": ["гэр", "гэр (home)"],
                    "explanation": "'Гэр' contains 'э', a front unrounded vowel. The other three words contain 'у', a back rounded vowel.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'Гэр' is the front-vowel word.",
                        "onFailure": "'гэр' has 'э' which is front; the others have 'у' which is back."
                    },
                    "detailedGrammarNote": "Front vowels in Mongolian are: э, ө, ү (and front variants of и). Back vowels are: а, о, у.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "ус, сум, нут, гэр",
                        "slowSpeechSynthesisText": "ус, сум, нут, гэр",
                        "ipaTranscription": "/ʊs, sʊm, nʊtʰ, ɡer/",
                        "speakerRole": "narrator",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                }
            ]
        },

        # LESSON 3: les_pre_a1_03_03_vowel_harmony_intro_roots
        {
            "lessonId": "les_pre_a1_03_03_vowel_harmony_intro_roots",
            "exercises": [
                {
                    "exerciseId": "ex_pre_a1_03_03_01",
                    "sequenceInLesson": 1,
                    "exerciseTitle": "Categorizing Core Roots: Masculine vs Feminine",
                    "modality": "VOWEL_HARMONY_CLASSIFICATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["vowel_harmony_classification", "root_analysis"],
                    "grammarTargets": ["gram_pre_a1_vowel_harmony_roots"],
                    "vocabularyTargets": ["гал", "гэр"],
                    "prompt": "Select the correct harmonic classification for the root word 'гал' (fire).",
                    "stimulusTextCyrillic": "гал",
                    "hint": "The vowel 'а' is a masculine back vowel.",
                    "options": [
                        {"id": "opt_masc", "text": "Masculine / Back (Эр үг) - vowel А", "cyrillic": "Эр үг", "isCorrect": True, "explanation": "Correct! 'гал' contains 'а', making it an 'эр үг' (masculine back-vowel word)."},
                        {"id": "opt_fem", "text": "Feminine / Front (Эм үг) - vowel Э", "cyrillic": "Эм үг", "isCorrect": False, "explanation": "Incorrect. 'гал' does not have front vowels."}
                    ],
                    "correctAnswer": "Masculine / Back (Эр үг) - vowel А",
                    "acceptableAlternatives": ["Эр үг", "Masculine", "Back", "Эр үг (Masculine / Back)"],
                    "explanation": "Because 'гал' contains the low back vowel 'а', it is classified as a masculine word (эр үг) and will take back-vowel suffixes (e.g. гал-аас, гал-ын).",
                    "learnerFeedback": {
                        "onSuccess": "Маш сайн! 'Гал' is an эр үг.",
                        "onFailure": "'а' is a back masculine vowel, so 'гал' is an эр үг."
                    },
                    "detailedGrammarNote": "Vowel harmony (эгшиг зохицох ёс) is the golden rule of Mongolian morphology: back-vowel roots only take back-vowel suffixes, and front-vowel roots only take front-vowel suffixes.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "гал",
                        "slowSpeechSynthesisText": "гал",
                        "ipaTranscription": "/ɢaɮ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_03_03_02",
                    "sequenceInLesson": 2,
                    "exerciseTitle": "Identifying Feminine (Эм) Root Words",
                    "modality": "VOWEL_HARMONY_CLASSIFICATION",
                    "interactionPattern": "MULTI_SELECT",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["harmonic_set_identification"],
                    "grammarTargets": ["gram_pre_a1_vowel_harmony_roots"],
                    "vocabularyTargets": ["гэр", "өвөл", "ном", "ус"],
                    "prompt": "Select ALL words below that belong to the FEMININE / FRONT vowel class (эм үг):",
                    "stimulusTextCyrillic": "гэр, өвөл, ном, ус",
                    "hint": "Look for words containing э, ө, or ү.",
                    "options": [
                        {"id": "opt_ger", "text": "гэр (home / yurta)", "cyrillic": "гэр", "isCorrect": True, "explanation": "Correct: 'гэр' contains front vowel 'э'."},
                        {"id": "opt_ovol", "text": "өвөл (winter)", "cyrillic": "өвөл", "isCorrect": True, "explanation": "Correct: 'өвөл' contains front vowel 'ө'."},
                        {"id": "opt_nom", "text": "ном (book)", "cyrillic": "ном", "isCorrect": False, "explanation": "Incorrect: 'ном' contains back vowel 'о'."},
                        {"id": "opt_us", "text": "ус (water)", "cyrillic": "ус", "isCorrect": False, "explanation": "Incorrect: 'ус' contains back vowel 'у'."}
                    ],
                    "correctAnswer": "гэр, өвөл",
                    "acceptableAlternatives": ["өвөл, гэр", "гэр өвөл"],
                    "explanation": "Both 'гэр' (vowel э) and 'өвөл' (vowel ө) are feminine front-vowel words (эм үг). 'Ном' and 'ус' contain back masculine vowels.",
                    "learnerFeedback": {
                        "onSuccess": "Сайн байна! 'гэр' and 'өвөл' are both feminine words.",
                        "onFailure": "Check the vowels: 'э' and 'ө' are feminine; 'о' and 'у' are masculine."
                    },
                    "detailedGrammarNote": "Feminine words take front harmonic suffix allomorphs such as -ээр/-өөр/-үүр, while masculine words take -аар/-оор/-уур.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "гэр, өвөл",
                        "slowSpeechSynthesisText": "гэр, өвөл",
                        "ipaTranscription": "/ɡer, ɵwɵɮ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "SET_EQUALITY"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_03_03_03",
                    "sequenceInLesson": 3,
                    "exerciseTitle": "Detecting Harmonic Violations in Nonce Words",
                    "modality": "VOWEL_HARMONY_CLASSIFICATION",
                    "interactionPattern": "MULTIPLE_CHOICE",
                    "cognitiveComplexity": "ANALYZE_SYNTAX",
                    "skillTargets": ["harmonic_constraint_detection"],
                    "grammarTargets": ["gram_pre_a1_vowel_harmony_roots"],
                    "vocabularyTargets": ["а", "э", "о", "ө"],
                    "prompt": "Which of the following hypothetical word roots VIOLATES Mongolian vowel harmony rules by mixing masculine and feminine vowels?",
                    "stimulusTextCyrillic": "*мадэ, малгай, нөхөр, охин",
                    "hint": "A single native root cannot contain both 'а' (masculine) and 'э' (feminine).",
                    "options": [
                        {"id": "opt_made", "text": "*мадэ (contains masculine 'а' and feminine 'э')", "cyrillic": "*мадэ", "isCorrect": True, "explanation": "Correct! Mixing back 'а' with front 'э' in a single stem is strictly prohibited by vowel harmony."},
                        {"id": "opt_malgai", "text": "малгай (all back vowels: а, а, ай)", "cyrillic": "малгай", "isCorrect": False, "explanation": "Incorrect. 'малгай' is fully harmonic (masculine)."},
                        {"id": "opt_nohor", "text": "нөхөр (all front rounded vowels: ө)", "cyrillic": "нөхөр", "isCorrect": False, "explanation": "Incorrect. 'нөхөр' is fully harmonic (feminine)."},
                        {"id": "opt_ohin", "text": "охин (neutral 'и' with back 'о')", "cyrillic": "охин", "isCorrect": False, "explanation": "Incorrect. The neutral vowel 'и' can freely occur with back vowels."}
                    ],
                    "correctAnswer": "*мадэ (contains masculine 'а' and feminine 'э')",
                    "acceptableAlternatives": ["*мадэ", "мадэ"],
                    "explanation": "Native Mongolian roots maintain strict vowel harmony: back vowels (а, о, у) never co-occur with front vowels (э, ө, ү). Therefore, '*мадэ' is impossible.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! '*мадэ' illegally mixes back 'а' and front 'э'.",
                        "onFailure": "Remember: Masculine and feminine vowels can never mix in a native root."
                    },
                    "detailedGrammarNote": "The only exception to pure harmonic separation is the neutral vowel 'и', which may appear in both masculine and feminine words without changing the dominant gender of the root.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "малгай, нөхөр, охин",
                        "slowSpeechSynthesisText": "малгай, нөхөр, охин",
                        "ipaTranscription": "/maɮɢæ, nɵxɵr, ɔxʲiŋ/",
                        "speakerRole": "narrator",
                        "speechRate": 0.85
                    },
                    "evaluation": {
                        "matchType": "EXACT"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_03_03_04",
                    "sequenceInLesson": 4,
                    "exerciseTitle": "Sorting Monosyllables by Gender Resonance",
                    "modality": "VOWEL_HARMONY_CLASSIFICATION",
                    "interactionPattern": "TOKEN_REARRANGEMENT",
                    "cognitiveComplexity": "APPLY_MORPHOLOGY",
                    "skillTargets": ["vowel_sorting", "lexical_phonology"],
                    "grammarTargets": ["gram_pre_a1_vowel_harmony_roots"],
                    "vocabularyTargets": ["нар", "сар", "гэр", "сүү"],
                    "prompt": "Arrange the tokens so that the two MASCULINE roots appear first, followed by the two FEMININE roots.",
                    "wordTokens": ["гэр", "сар", "сүү", "нар"],
                    "correctTokenOrder": ["нар", "сар", "гэр", "сүү"],
                    "correctAnswer": "нар, сар, гэр, сүү",
                    "acceptableAlternatives": ["сар, нар, гэр, сүү", "сар нар сүү гэр", "нар сар сүү гэр"],
                    "hint": "'нар' (sun) and 'сар' (moon) have vowel 'а' (masculine). 'гэр' and 'сүү' have front vowels (feminine).",
                    "explanation": "'Нар' and 'сар' contain 'а' (masculine/back). 'Гэр' and 'сүү' contain 'э' and 'ү' (feminine/front).",
                    "learnerFeedback": {
                        "onSuccess": "Төгс! Masculine (нар, сар) then feminine (гэр, сүү).",
                        "onFailure": "Group by vowel: нар & сар are masculine; гэр & сүү are feminine."
                    },
                    "detailedGrammarNote": "In Mongolian poetry and cosmology, 'нар сар' (sun and moon) are paired masculine celestial symbols, while 'гэр орон' anchors domestic life.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "нар, сар, гэр, сүү",
                        "slowSpeechSynthesisText": "нар, сар, гэр, сүү",
                        "ipaTranscription": "/nar, sar, ɡer, suː/",
                        "speakerRole": "narrator",
                        "speechRate": 0.8
                    },
                    "evaluation": {
                        "matchType": "TOKEN_ORDER"
                    }
                },
                {
                    "exerciseId": "ex_pre_a1_03_03_05",
                    "sequenceInLesson": 5,
                    "exerciseTitle": "Auditory Identification of Root Gender Harmony",
                    "modality": "VOWEL_HARMONY_CLASSIFICATION",
                    "interactionPattern": "AUDIO_COMPREHENSION",
                    "cognitiveComplexity": "UNDERSTAND_DISCRIMINATE",
                    "skillTargets": ["auditory_harmony_classification"],
                    "grammarTargets": ["gram_pre_a1_vowel_harmony_roots"],
                    "vocabularyTargets": ["морь"],
                    "prompt": "Listen to the word 'морь' (horse). Because it contains vowel 'о' with palatalized 'рь', what suffix set will it take?",
                    "stimulusTextCyrillic": "морь",
                    "hint": "'О' is a back masculine vowel with labial rounding.",
                    "options": [
                        {"id": "opt_masc_o", "text": "Masculine suffixes with back harmony (e.g. -оор/-ын: мориор)", "cyrillic": "Эр үг", "isCorrect": True, "explanation": "Correct! The root vowel 'о' dictates masculine rounded suffix harmony."},
                        {"id": "opt_fem_e", "text": "Feminine suffixes with front harmony (e.g. -ээр)", "cyrillic": "Эм үг", "isCorrect": False, "explanation": "Incorrect. 'О' is never feminine."}
                    ],
                    "correctAnswer": "Masculine suffixes with back harmony (e.g. -оор/-ын: мориор)",
                    "acceptableAlternatives": ["Эр үг", "Masculine", "мориор"],
                    "explanation": "'Морь' (/mɔrʲ/) has root vowel 'о'. The soft sign indicates palatalization of 'р', but the dominant vowel is 'о', demanding back masculine suffixes.",
                    "learnerFeedback": {
                        "onSuccess": "Яг зөв! 'Морь' takes masculine suffixes such as 'мориор'.",
                        "onFailure": "The primary vowel is 'о', which is masculine."
                    },
                    "detailedGrammarNote": "Palatalization (зөөлний тэмдэг ь) affects consonant articulation but does not alter the fundamental back/front harmonic classification of the root vowel.",
                    "audio": {
                        "requiresAudio": True,
                        "speechSynthesisText": "морь",
                        "slowSpeechSynthesisText": "морь",
                        "ipaTranscription": "/mɔrʲ/",
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
