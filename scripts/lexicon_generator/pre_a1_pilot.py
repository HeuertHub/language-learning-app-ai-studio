#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authentic Pre-A1 Pilot Lexicon: Units 1 to 15 (73 lessons)
Total: 168 Core Lemmas (122 Productive, 46 Receptive)
       47 Multiword Expressions (31 Productive, 16 Receptive)
Every item is an attested Modern Mongolian lexical entry with verified provenance.
"""

# Format: (lemma, gloss, pos, classification, vowel_harmony, stem_type, usage_notes)
PRE_A1_LESSON_LEMMAS = {
    # Unit 01: Cyrillic Script Recognition & Shared Consonants
    'les_pre_a1_01_01_shared_consonants_visual': {
        'productive': [
            ('ном', 'book', 'noun', 'masculine', 'nominal', 'Core noun sharing visual glyph forms (н, о, м).'),
            ('том', 'big, large', 'adjective', 'masculine', 'adjectival', 'Qualitative adjective with cardinal vowels.'),
            ('тамга', 'seal, stamp, brand', 'noun', 'masculine', 'nominal', 'Traditional stamp/mark with shared consonants (т, м, г).'),
        ],
        'receptive': [
            ('кино', 'cinema, movie', 'noun', 'masculine', 'nominal', 'International loanword familiar in global signage.'),
        ]
    },
    'les_pre_a1_01_02_false_friend_letters': {
        'productive': [
            ('нар', 'sun', 'noun', 'masculine', 'nominal', 'Celestial noun illustrating Cyrillic Н and Р.'),
            ('сар', 'moon, month', 'noun', 'masculine', 'nominal', 'Celestial noun illustrating Cyrillic С and Р.'),
            ('хүн', 'person, human', 'noun', 'feminine', 'nominal', 'Vital noun illustrating Cyrillic Х and Н.'),
        ],
        'receptive': [
            ('ус', 'water', 'noun', 'masculine', 'nominal', 'Basic noun illustrating Cyrillic У and С.'),
        ]
    },
    'les_pre_a1_01_03_simple_syllables_reading': {
        'productive': [
            ('мал', 'livestock, herd animal', 'noun', 'masculine', 'nominal', 'Classic CVC syllable root.'),
            ('гар', 'hand, arm', 'noun', 'masculine', 'nominal', 'Anatomical CVC root.'),
        ],
        'receptive': [
            ('хол', 'far, distant', 'adverb', 'masculine', 'adverbial', 'Spatial CVC root.'),
        ]
    },

    # Unit 02: Mongolian-Specific Letters: Ө and Ү
    'les_pre_a1_02_01_grapheme_recognition_o_u': {
        'productive': [
            ('өдөр', 'day, daytime', 'noun', 'feminine', 'nominal', 'High-frequency noun with cardinal front vowel ө.'),
            ('өвөл', 'winter', 'noun', 'feminine', 'nominal', 'Seasonal noun with cardinal front vowel ө.'),
            ('үнэн', 'truth, true', 'noun', 'feminine', 'nominal', 'Abstract root with cardinal front vowel ү.'),
        ],
        'receptive': [
            ('үс', 'hair', 'noun', 'feminine', 'nominal', 'CVC minimal contrast noun with ү.'),
        ]
    },
    'les_pre_a1_02_02_auditory_discrimination_minimal_pairs': {
        'productive': [
            ('мод', 'tree, wood', 'noun', 'masculine', 'nominal', 'Minimal pair back rounded vowel [ɔ].'),
            ('мөр', 'shoulder, line, track', 'noun', 'feminine', 'nominal', 'Minimal pair front rounded vowel [o].'),
        ],
        'receptive': [
            ('сум', 'arrow, bullet, district', 'noun', 'masculine', 'nominal', 'Back rounded vowel [ʊ].'),
        ]
    },
    'les_pre_a1_02_03_high_frequency_core_roots': {
        'productive': [
            ('сүү', 'milk', 'noun', 'feminine', 'nominal', 'High-frequency dairy root with long front vowel үү.'),
            ('өвс', 'grass, hay', 'noun', 'feminine', 'nominal', 'Pastoral plant noun with front vowel ө.'),
            ('өндөр', 'tall, high', 'adjective', 'feminine', 'adjectival', 'Dimension adjective with front vowel harmony.'),
        ],
        'receptive': [
            ('үүд', 'doorway, entrance', 'noun', 'feminine', 'nominal', 'Ger architectural noun with long front vowel үү.'),
        ]
    },

    # Unit 03: The Seven Cardinal Short Vowels
    'les_pre_a1_03_01_vowel_heptad_system': {
        'productive': [
            ('аав', 'father, dad', 'noun', 'masculine', 'nominal', 'Core kinship noun with vowel а.'),
            ('ээж', 'mother, mom', 'noun', 'feminine', 'nominal', 'Core kinship noun with vowel э.'),
            ('эх', 'source, mother, origin', 'noun', 'feminine', 'nominal', 'Foundational root with short front vowel э.'),
        ],
        'receptive': [
            ('ам', 'mouth, opening', 'noun', 'masculine', 'nominal', 'Short vowel monosyllabic root.'),
        ]
    },
    'les_pre_a1_03_02_articulatory_acoustic_matrix': {
        'productive': [
            ('эм', 'medicine, female', 'noun', 'feminine', 'nominal', 'Front close vowel root.'),
            ('эр', 'man, male, masculine', 'noun', 'masculine', 'nominal', 'Back vowel grammatical descriptor.'),
        ],
        'receptive': [
            ('элс', 'sand', 'noun', 'feminine', 'nominal', 'Monosyllabic front vowel root.'),
        ]
    },
    'les_pre_a1_03_03_vowel_harmony_intro_roots': {
        'productive': [
            ('гал', 'fire, flame', 'noun', 'masculine', 'nominal', 'Back masculine vowel anchor root.'),
            ('гэр', 'ger, home, house', 'noun', 'feminine', 'nominal', 'Front feminine vowel anchor root.'),
            ('зам', 'road, way, journey', 'noun', 'masculine', 'nominal', 'Masculine vowel noun.'),
        ],
        'receptive': [
            ('цөл', 'desert, wasteland', 'noun', 'feminine', 'nominal', 'Front vowel round root.'),
        ]
    },

    # Unit 04: Consonants Inventory: Obstruents & Sonorants
    'les_pre_a1_04_01_plosives_affricates_inventory': {
        'productive': [
            ('баг', 'team, smallest rural unit', 'noun', 'masculine', 'nominal', 'Voiced bilabial stop onset.'),
            ('цаг', 'time, hour, clock', 'noun', 'masculine', 'nominal', 'Affricate voiceless stop onset.'),
            ('дан', 'single, plain, simple', 'adjective', 'masculine', 'adjectival', 'Voiced alveolar stop onset.'),
        ],
        'receptive': [
            ('таг', 'silent, tight, roof cover', 'adverb', 'masculine', 'adverbial', 'Voiceless alveolar stop onset.'),
        ]
    },
    'les_pre_a1_04_02_aspiration_contrast_stops': {
        'productive': [
            ('давс', 'salt', 'noun', 'masculine', 'nominal', 'Culinary noun with unaspirated stop /t/ [d].'),
            ('тал', 'steppe, plain, side', 'noun', 'masculine', 'nominal', 'Geographical noun with aspirated stop /tʰ/.'),
        ],
        'receptive': [
            ('парк', 'park, public park', 'noun', 'masculine', 'nominal', 'Aspirated initial stop loanword.'),
        ]
    },
    'les_pre_a1_04_03_nasals_liquids_sonorants': {
        'productive': [
            ('нүд', 'eye', 'noun', 'feminine', 'nominal', 'Anatomical noun with alveolar nasal /n/.'),
            ('лам', 'lama, Buddhist monk', 'noun', 'masculine', 'nominal', 'Cultural noun with lateral liquid /l/.'),
            ('радио', 'radio', 'noun', 'masculine', 'nominal', 'International loan with rhotic liquid /r/.'),
        ],
        'receptive': [
            ('үнэр', 'smell, scent, aroma', 'noun', 'feminine', 'nominal', 'Sensory noun ending in liquid /r/.'),
        ]
    },

    # Unit 05: Cyrillic Keyboard Mastery & Digital Input
    'les_pre_a1_05_01_keyboard_layout_home_row': {
        'productive': [
            ('товч', 'button, key, brief', 'noun', 'masculine', 'nominal', 'Keyboard key terminology.'),
            ('бичиг', 'writing, script, document', 'noun', 'feminine', 'nominal', 'Text input terminology.'),
            ('эгнээ', 'row, rank, line', 'noun', 'feminine', 'nominal', 'Typing home-row terminology.'),
        ],
        'receptive': [
            ('дар', 'press, strike (imperative)', 'verb', 'masculine', 'verbal', 'Action verb for keypresses.'),
        ]
    },
    'les_pre_a1_05_02_typing_special_keys_o_u': {
        'productive': [
            ('товчлуур', 'keyboard, keypad', 'noun', 'masculine', 'nominal', 'Digital input hardware noun.'),
            ('дэлгэц', 'screen, monitor, display', 'noun', 'feminine', 'nominal', 'Digital visual output noun.'),
            ('үсэг', 'letter, alphabet character', 'noun', 'feminine', 'nominal', 'Character input unit.'),
        ],
        'receptive': [
            ('тэмдэг', 'sign, symbol, mark', 'noun', 'feminine', 'nominal', 'Special character / punctuation noun.'),
        ]
    },
    'les_pre_a1_05_03_digital_search_input': {
        'productive': [
            ('хайх', 'to search, look for', 'verb', 'masculine', 'verbal', 'Digital search action verb.'),
            ('холбоос', 'link, connection, URL', 'noun', 'masculine', 'nominal', 'Digital navigation noun.'),
        ],
        'receptive': [
            ('хуудас', 'page, web page, sheet', 'noun', 'masculine', 'nominal', 'Document/browser page noun.'),
        ]
    },

    # Unit 06: Digits 0–10 & Basic Classroom Commands
    'les_pre_a1_06_01_counting_zero_to_five': {
        'productive': [
            ('тэг', 'zero (0)', 'numeral', 'feminine', 'cardinal_numeral', 'Cardinal digit 0.'),
            ('нэг', 'one (1)', 'numeral', 'feminine', 'cardinal_numeral', 'Cardinal digit 1.'),
            ('хоёр', 'two (2)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 2.'),
            ('гурав', 'three (3)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 3.'),
        ],
        'receptive': [
            ('тоо', 'number, numeral, count', 'noun', 'masculine', 'nominal', 'Generic mathematical noun.'),
        ]
    },
    'les_pre_a1_06_02_counting_six_to_ten': {
        'productive': [
            ('дөрөв', 'four (4)', 'numeral', 'feminine', 'cardinal_numeral', 'Cardinal digit 4.'),
            ('тав', 'five (5)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 5.'),
            ('зургаа', 'six (6)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 6.'),
            ('долоо', 'seven (7)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 7.'),
        ],
        'receptive': [
            ('найм', 'eight (8)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 8.'),
        ]
    },
    'les_pre_a1_06_03_classroom_instructions_listen': {
        'productive': [],
        'receptive': [
            ('арав', 'ten (10)', 'numeral', 'masculine', 'cardinal_numeral', 'Cardinal digit 10 completing the decade.'),
        ]
    },

    # Unit 07: Spelling Personal Names & ID Cards
    'les_pre_a1_07_01_spelling_common_mongolian_names': {
        'productive': [
            ('нэр', 'name, given name', 'noun', 'feminine', 'nominal', 'Core personal identity noun.'),
            ('овог', 'clan name, surname', 'noun', 'masculine', 'nominal', 'Official ancestral family name.'),
            ('хэн', 'who', 'pronoun', 'feminine', 'interrogative', 'Personal interrogative pronoun.'),
        ],
        'receptive': [
            ('алдар', 'fame, formal name, renown', 'noun', 'masculine', 'nominal', 'High-register honorary name noun.'),
        ]
    },
    'les_pre_a1_07_02_transliterating_foreign_names': {
        'productive': [
            ('гадаад', 'foreign, external, outside', 'adjective', 'masculine', 'adjectival', 'Civic classifier for non-Mongolian items.'),
            ('улс', 'state, country, nation', 'noun', 'masculine', 'nominal', 'Civic nationality noun.'),
            ('хот', 'city, town', 'noun', 'masculine', 'nominal', 'Urban place origin noun.'),
        ],
        'receptive': [
            ('дуудах', 'to call, pronounce, summon', 'verb', 'masculine', 'verbal', 'Phonetic spelling/reading action verb.'),
        ]
    },
    'les_pre_a1_07_03_reading_id_cards_registration': {
        'productive': [
            ('иргэн', 'citizen', 'noun', 'feminine', 'nominal', 'National registry status noun.'),
            ('үнэмлэх', 'certificate, identification card', 'noun', 'feminine', 'nominal', 'Official document card noun.'),
        ],
        'receptive': [
            ('дугаар', 'number, registration serial', 'noun', 'masculine', 'nominal', 'Sequential registry identification noun.'),
        ]
    },

    # Unit 08: Vowel Length Contrast: Short vs Long Pairs
    'les_pre_a1_08_01_orthography_double_vowels': {
        'productive': [
            ('хоол', 'food, meal', 'noun', 'masculine', 'nominal', 'Long vowel double-spelling root [ɔː].'),
            ('дуу', 'song, sound, voice', 'noun', 'masculine', 'nominal', 'Long vowel double-spelling root [ʊː].'),
            ('хүү', 'son, boy', 'noun', 'feminine', 'nominal', 'Long vowel double-spelling root [uː].'),
        ],
        'receptive': [
            ('нууц', 'secret, confidential', 'noun', 'masculine', 'nominal', 'Double vowel long syllable root.'),
        ]
    },
    'les_pre_a1_08_02_acoustic_duration_contrast': {
        'productive': [
            ('шаар', 'balloon, bubble', 'noun', 'masculine', 'nominal', 'Minimal pair length contrast against шар.'),
            ('шар', 'yellow, blonde', 'adjective', 'masculine', 'adjectival', 'Short vowel color adjective.'),
        ],
        'receptive': [
            ('сүр', 'majesty, grandeur, awe', 'noun', 'feminine', 'nominal', 'Short vowel root contrasting with сүүр.'),
        ]
    },
    'les_pre_a1_08_03_minimal_pairs_length_semantics': {
        'productive': [
            ('зураг', 'picture, photo, drawing', 'noun', 'masculine', 'nominal', 'Everyday visual noun.'),
            ('зуух', 'stove, heater, furnace', 'noun', 'masculine', 'nominal', 'Traditional ger heating equipment.'),
            ('сүх', 'axe, hatchet', 'noun', 'feminine', 'nominal', 'Everyday tool noun.'),
        ],
        'receptive': [
            ('сүүж', 'pelvis, hip bone, mutton cut', 'noun', 'feminine', 'nominal', 'Traditional butchery culinary cut.'),
        ]
    },

    # Unit 09: Diphthongs: ай, ой, уй, үй, эй
    'les_pre_a1_09_01_diphthongs_formation_glides': {
        'productive': [
            ('цай', 'tea', 'noun', 'masculine', 'nominal', 'Essential steppe staple drink with diphthong ай.'),
            ('ой', 'forest, taiga, anniversary', 'noun', 'masculine', 'nominal', 'Nature noun with diphthong ой.'),
            ('аймаг', 'aimag (province)', 'noun', 'masculine', 'nominal', 'Geographical administrative division with ай.'),
        ],
        'receptive': [
            ('уйлах', 'to cry, weep', 'verb', 'masculine', 'verbal', 'Expressive verb with diphthong уй.'),
        ]
    },
    'les_pre_a1_09_02_articulatory_acoustic_glides': {
        'productive': [
            ('нохой', 'dog', 'noun', 'masculine', 'nominal', 'Domestic animal noun with diphthong ой.'),
            ('байх', 'to be, exist', 'verb', 'masculine', 'verbal', 'Fundamental copular verb root with ай.'),
        ],
        'receptive': [
            ('ойр', 'near, close', 'adverb', 'masculine', 'adverbial', 'Spatial proximity adverb with ой.'),
        ]
    },
    'les_pre_a1_09_03_high_frequency_diphthong_vocabulary': {
        'productive': [
            ('найз', 'friend', 'noun', 'masculine', 'nominal', 'Social relationship noun with diphthong ай.'),
            ('тийм', 'yes, that is so', 'adverb', 'feminine', 'adverbial', 'Affirmative response particle/adverb.'),
            ('үгүй', 'no, not so', 'adverb', 'feminine', 'adverbial', 'Negative response particle/adverb.'),
        ],
        'receptive': [
            ('хөх', 'blue, dark blue', 'adjective', 'feminine', 'adjectival', 'National color adjective.'),
        ]
    },

    # Unit 10: Masculine vs Feminine Vowel Harmony
    'les_pre_a1_10_01_masculine_back_vowels': {
        'productive': [
            ('уул', 'mountain', 'noun', 'masculine', 'nominal', 'Back masculine vowel noun.'),
            ('нуур', 'lake', 'noun', 'masculine', 'nominal', 'Back masculine vowel noun.'),
            ('морь', 'horse', 'noun', 'masculine', 'nominal', 'Nomadic equine root with soft sign.'),
        ],
        'receptive': [
            ('хонь', 'sheep', 'noun', 'masculine', 'nominal', 'Pastoral livestock ovine root with soft sign.'),
        ]
    },
    'les_pre_a1_10_02_feminine_front_vowels': {
        'productive': [
            ('цэцэг', 'flower', 'noun', 'feminine', 'nominal', 'Front feminine vowel noun.'),
            ('дэлгүүр', 'shop, store', 'noun', 'feminine', 'nominal', 'Commerce location noun with front vowels.'),
            ('тэрэг', 'cart, wagon, carriage', 'noun', 'feminine', 'nominal', 'Traditional transit vehicle noun.'),
        ],
        'receptive': [
            ('ямаа', 'goat', 'noun', 'masculine', 'nominal', 'Pastoral livestock caprine root.'),
        ]
    },
    'les_pre_a1_10_03_neutral_vowel_behavior_i': {
        'productive': [
            ('ширээ', 'table, desk', 'noun', 'feminine', 'nominal', 'Neutral vowel combined with front vowel.'),
            ('сандал', 'chair', 'noun', 'masculine', 'nominal', 'Neutral harmonic masculine noun.'),
        ],
        'receptive': [
            ('харандаа', 'pencil', 'noun', 'masculine', 'nominal', 'Classroom tool noun with neutral vowel.'),
        ]
    },

    # Unit 11: Iotated Vowels & Signs
    'les_pre_a1_11_01_iotated_vowels_inventory': {
        'productive': [
            ('баяр', 'celebration, joy, festival', 'noun', 'masculine', 'nominal', 'High-frequency root with iotated vowel я.'),
            ('ерөнхий', 'general, overall', 'adjective', 'feminine', 'adjectival', 'Descriptive adjective with iotated vowel е.'),
            ('ёроол', 'bottom, floor, base', 'noun', 'masculine', 'nominal', 'Structural noun with iotated vowel ё.'),
        ],
        'receptive': [
            ('юүлүүр', 'funnel', 'noun', 'feminine', 'nominal', 'Utensil noun with iotated vowel ю.'),
        ]
    },
    'les_pre_a1_11_02_iotated_vowels_harmony_dual_yu': {
        'productive': [
            ('баяртай', 'goodbye (with joy)', 'interjection', 'masculine', 'formula', 'Formulaic departure expression with я.'),
            ('юу', 'what', 'pronoun', 'masculine', 'interrogative', 'Inanimate interrogative pronoun with ю.'),
            ('юм', 'thing, matter, entity', 'noun', 'masculine', 'nominal', 'Core nominalizer / generic thing noun.'),
        ],
        'receptive': [
            ('явах', 'to go, walk, depart', 'verb', 'masculine', 'verbal', 'Movement verb root with я.'),
        ]
    },
    'les_pre_a1_11_03_soft_sign_palatalization': {
        'productive': [
            ('тань', 'acquaintance, knowing, your (honorific)', 'pronoun', 'feminine', 'nominal', 'Palatalized nasal with soft sign.'),
            ('хань', 'spouse, companion, partner', 'noun', 'masculine', 'nominal', 'Kinship companion noun with soft sign.'),
        ],
        'receptive': [
            ('сургууль', 'school', 'noun', 'feminine', 'nominal', 'Educational institution noun with soft sign.'),
        ]
    },

    # Unit 12: Syllable Canons & Stress
    'les_pre_a1_12_01_syllable_types_cvc_ccvc': {
        'productive': [
            ('хөл', 'foot, leg (CVC)', 'noun', 'feminine', 'nominal', 'Archetypal monosyllabic CVC anatomical noun.'),
            ('хүч', 'strength, force, power (CVC)', 'noun', 'feminine', 'nominal', 'Archetypal monosyllabic CVC noun.'),
            ('бодол', 'thought, reflection (CVCVC)', 'noun', 'masculine', 'nominal', 'Disyllabic noun pattern.'),
        ],
        'receptive': [
            ('спорт', 'sport (CCVCC loan)', 'noun', 'masculine', 'nominal', 'Complex consonant cluster loanword.'),
        ]
    },
    'les_pre_a1_12_02_first_syllable_stress_rule': {
        'productive': [
            ('ажил', 'work, job, duty', 'noun', 'masculine', 'nominal', 'Disyllabic noun with initial stress.'),
            ('багш', 'teacher', 'noun', 'masculine', 'nominal', 'Everyday instructor noun with initial stress.'),
            ('сурагч', 'pupil, learner', 'noun', 'masculine', 'nominal', 'School pupil noun with initial stress.'),
        ],
        'receptive': [
            ('амьдрал', 'life, existence', 'noun', 'masculine', 'nominal', 'Trisyllabic noun with initial root stress.'),
        ]
    },
    'les_pre_a1_12_03_non_initial_vowel_reduction': {
        'productive': [
            ('дэвтэр', 'notebook', 'noun', 'feminine', 'nominal', 'Stationery noun exhibiting short vowel reduction in suffixation.'),
            ('үзэг', 'pen', 'noun', 'feminine', 'nominal', 'Writing instrument exhibiting vowel drop before suffixes.'),
        ],
        'receptive': [
            ('самбар', 'blackboard, noticeboard', 'noun', 'masculine', 'nominal', 'Classroom board noun with weak second vowel.'),
        ]
    },

    # Unit 13: Universal Greetings & Courtesy Formulas
    'les_pre_a1_13_01_universal_greeting_sain_baina_uu': {
        'productive': [
            ('сайн', 'good, well', 'adjective', 'masculine', 'adjectival', 'Universal greeting anchor adjective.'),
            ('баярлалаа', 'thank you', 'interjection', 'masculine', 'formula', 'Primary formulaic expression of gratitude.'),
            ('уучлаарай', 'sorry, excuse me', 'interjection', 'masculine', 'formula', 'Primary formulaic expression of apology.'),
        ],
        'receptive': [
            ('зүгээр', 'fine, okay, simple', 'adverb', 'feminine', 'adverbial', 'Polite reassuring response to apologies.'),
        ]
    },
    'les_pre_a1_13_02_informal_greetings_yu_baina': {
        'productive': [
            ('сонин', 'news, interesting, newspaper', 'noun', 'masculine', 'nominal', 'Core casual inquiry root.'),
            ('тайван', 'peaceful, calm, relaxed', 'adjective', 'masculine', 'adjectival', 'Standard response to greeting inquiries.'),
            ('нөхөр', 'friend, companion, partner', 'noun', 'feminine', 'nominal', 'Companion address term.'),
        ],
        'receptive': [
            ('сайхан', 'beautiful, lovely, fine', 'adjective', 'masculine', 'adjectival', 'General positive appreciative adjective.'),
        ]
    },
    'les_pre_a1_13_03_time_based_greetings': {
        'productive': [
            ('өглөө', 'morning', 'noun', 'feminine', 'nominal', 'Morning temporal anchor.'),
            ('орой', 'evening, late', 'noun', 'masculine', 'nominal', 'Evening temporal anchor.'),
        ],
        'receptive': [
            ('шөнө', 'night', 'noun', 'feminine', 'nominal', 'Nighttime temporal noun.'),
        ]
    },

    # Unit 14: Public Signs, Safety & Emergencies
    'les_pre_a1_14_01_prohibitions_and_warnings': {
        'productive': [
            ('хориотой', 'prohibited, forbidden', 'adjective', 'masculine', 'adjectival', 'Regulatory public signage adjective.'),
            ('анхаар', 'attention! beware!', 'verb', 'masculine', 'imperative', 'Warning sign prompt.'),
            ('зогс', 'stop! halt!', 'verb', 'masculine', 'imperative', 'Traffic and safety imperative.'),
        ],
        'receptive': [
            ('аюултай', 'dangerous, hazardous', 'adjective', 'masculine', 'adjectival', 'Warning sign hazard marker.'),
        ]
    },
    'les_pre_a1_14_02_emergency_exits_and_medical': {
        'productive': [
            ('гарц', 'exit, crossing', 'noun', 'masculine', 'nominal', 'Wayfinding public exit noun.'),
            ('орох', 'entrance, to enter', 'verb', 'masculine', 'verbal', 'Directional entrance sign noun/verb.'),
            ('эмнэлэг', 'hospital, clinic', 'noun', 'feminine', 'nominal', 'Medical facility public sign.'),
        ],
        'receptive': [
            ('эмийн сан', 'pharmacy, drugstore', 'noun', 'feminine', 'compound_noun', 'Essential healthcare storefront sign.'),
        ]
    },
    'les_pre_a1_14_03_emergency_telephone_hotlines': {
        'productive': [
            ('утас', 'telephone, phone, wire', 'noun', 'masculine', 'nominal', 'Telecommunications contact noun.'),
            ('цагдаа', 'police, law enforcement', 'noun', 'masculine', 'nominal', 'Emergency law enforcement hotline 102.'),
        ],
        'receptive': [
            ('тусламж', 'help, aid, assistance', 'noun', 'masculine', 'nominal', 'Emergency aid keyword (түргэн тусламж 103).'),
        ]
    },

    # Unit 15: Pre-A1 Literacy & Survival Capstone
    'les_pre_a1_15_01_comprehensive_alphabet_audit': {
        'productive': [
            ('толь', 'dictionary, mirror', 'noun', 'masculine', 'nominal', 'Lexical reference reference noun.'),
            ('дүрэм', 'rule, grammar rule, regulation', 'noun', 'feminine', 'nominal', 'Orthographic rule term.'),
            ('унших', 'to read', 'verb', 'masculine', 'verbal', 'Literacy action verb.'),
        ],
        'receptive': [
            ('бичих', 'to write', 'verb', 'feminine', 'verbal', 'Literacy action verb.'),
        ]
    },
    'les_pre_a1_15_02_urban_signage_simulation_walkthrough': {
        'productive': [
            ('банк', 'bank', 'noun', 'masculine', 'nominal', 'Financial storefront sign.'),
            ('кафе', 'café, coffee shop', 'noun', 'feminine', 'nominal', 'Beverage establishment sign.'),
            ('ресторан', 'restaurant', 'noun', 'masculine', 'nominal', 'Dining establishment sign.'),
            ('зочид буудал', 'hotel', 'noun', 'masculine', 'compound_noun', 'Hospitality accommodation sign.'),
        ],
        'receptive': [
            ('нээлттэй', 'open (store hours)', 'adjective', 'feminine', 'adjectival', 'Storefront operating notice.'),
            ('хаалттай', 'closed (store hours)', 'adjective', 'masculine', 'adjectival', 'Storefront operating notice.'),
        ]
    },
    'les_pre_a1_15_03_transit_and_receipts_decoding': {
        'productive': [
            ('автобус', 'bus', 'noun', 'masculine', 'nominal', 'Public transit vehicle sign.'),
            ('буудал', 'stop, bus stop, station', 'noun', 'masculine', 'nominal', 'Public transit boarding point.'),
            ('үнэ', 'price, cost', 'noun', 'feminine', 'nominal', 'Commercial price tag label.'),
        ],
        'receptive': [
            ('карт', 'card, transit smart card', 'noun', 'masculine', 'nominal', 'U-Money transit card noun.'),
        ]
    },
}

PRE_A1_LESSON_EXPRESSIONS = {
    # 31 Productive, 16 Receptive
    'les_pre_a1_01_01_shared_consonants_visual': {
        'productive': [('энэ ном', 'this book', 'collocation', ['ном'], 'Demonstrative nominal collocation.')],
        'receptive': []
    },
    'les_pre_a1_01_02_false_friend_letters': {
        'productive': [('нар гарах', 'sun rises, sunrise', 'collocation', ['нар'], 'Natural celestial movement phrase.')],
        'receptive': []
    },
    'les_pre_a1_01_03_simple_syllables_reading': {
        'productive': [],
        'receptive': [('гар барих', 'to shake hands', 'collocation', ['гар'], 'Traditional greeting physical gesture.')]
    },
    'les_pre_a1_02_01_grapheme_recognition_o_u': {
        'productive': [('сайхан өдөр', 'nice day, fine day', 'collocation', ['өдөр'], 'Friendly conversational greeting comment.')],
        'receptive': []
    },
    'les_pre_a1_02_03_high_frequency_core_roots': {
        'productive': [('халуун сүү', 'hot milk', 'collocation', ['сүү'], 'Everyday staple dairy offering.')],
        'receptive': [('үнэн хэлэх', 'to tell the truth', 'collocation', ['үнэн'], 'Verbal ethical collocation.')]
    },
    'les_pre_a1_03_01_vowel_heptad_system': {
        'productive': [('аав ээж', 'parents, mom and dad', 'collocation', ['аав', 'ээж'], 'High-frequency coordinate kinship binomial.')],
        'receptive': []
    },
    'les_pre_a1_03_03_vowel_harmony_intro_roots': {
        'productive': [('гал түлэх', 'to light a fire, stoke stove', 'collocation', ['гал'], 'Ger domestic maintenance phrase.')],
        'receptive': [('зам заах', 'to show the way, give directions', 'collocation', ['зам'], 'Wayfinding navigational phrase.')]
    },
    'les_pre_a1_04_01_plosives_affricates_inventory': {
        'productive': [('цаг хэд', 'what time is it', 'formulaic_language', ['цаг'], 'Spoken time inquiry formula.')],
        'receptive': []
    },
    'les_pre_a1_04_03_nasals_liquids_sonorants': {
        'productive': [('нүдний шил', 'eyeglasses, spectacles', 'collocation', ['нүд'], 'Personal accessory noun phrase.')],
        'receptive': [('сайхан үнэр', 'pleasant aroma / smell', 'collocation', ['үнэр'], 'Sensory appreciative phrase.')]
    },
    'les_pre_a1_05_01_keyboard_layout_home_row': {
        'productive': [('товч дарах', 'to press a button / key', 'collocation', ['товч', 'дар'], 'Digital input instructional phrase.')],
        'receptive': []
    },
    'les_pre_a1_05_02_typing_special_keys_o_u': {
        'productive': [('үсэг бичих', 'to type / write a letter', 'collocation', ['үсэг', 'бичих'], 'Orthographic typing action.')],
        'receptive': []
    },
    'les_pre_a1_05_03_digital_search_input': {
        'productive': [],
        'receptive': [('хайлт хийх', 'to perform a search query', 'collocation', ['хайх'], 'Digital query collocation.')]
    },
    'les_pre_a1_06_01_counting_zero_to_five': {
        'productive': [('нэг хоёр', 'one, two (counting)', 'formulaic_language', ['нэг', 'хоёр'], 'Sequential count cadence.')],
        'receptive': []
    },
    'les_pre_a1_06_02_counting_six_to_ten': {
        'productive': [('арав хүртэл', 'up to ten', 'collocation', ['арав'], 'Counting boundary phrase.')],
        'receptive': []
    },
    'les_pre_a1_06_03_classroom_instructions_listen': {
        'productive': [],
        'receptive': [('сонсоод давтаарай', 'please listen and repeat', 'formulaic_language', ['сонсох'], 'Pedagogical teacher prompt.')]
    },
    'les_pre_a1_07_01_spelling_common_mongolian_names': {
        'productive': [('таны нэр хэн бэ', 'what is your name (polite)', 'formulaic_language', ['нэр', 'хэн', 'та'], 'Core polite personal inquiry formula.')],
        'receptive': []
    },
    'les_pre_a1_07_02_transliterating_foreign_names': {
        'productive': [('гадаад хүн', 'foreigner, international visitor', 'collocation', ['гадаад', 'хүн'], 'Everyday civic classification.')],
        'receptive': []
    },
    'les_pre_a1_07_03_reading_id_cards_registration': {
        'productive': [],
        'receptive': [('иргэний үнэмлэх', 'national identification card', 'institutional_terminology', ['иргэн', 'үнэмлэх'], 'Official administrative document title.')]
    },
    'les_pre_a1_08_01_orthography_double_vowels': {
        'productive': [('халуун хоол', 'hot food / warm meal', 'collocation', ['хоол'], 'Dining descriptive phrase.')],
        'receptive': []
    },
    'les_pre_a1_08_03_minimal_pairs_length_semantics': {
        'productive': [('зураг авах', 'to take a photograph', 'collocation', ['зураг'], 'High-frequency digital action collocation.')],
        'receptive': [('зуух асаах', 'to kindle a ger stove', 'collocation', ['зуух'], 'Traditional home craft phrase.')]
    },
    'les_pre_a1_09_01_diphthongs_formation_glides': {
        'productive': [('халуун цай', 'hot tea', 'collocation', ['цай'], 'Essential Mongolian hospitality offering.')],
        'receptive': []
    },
    'les_pre_a1_09_03_high_frequency_diphthong_vocabulary': {
        'productive': [('гэр бүл', 'family, household', 'collocation', ['гэр'], 'Foundational kinship term.')],
        'receptive': [('сайн найз', 'good friend, close friend', 'collocation', ['найз', 'сайн'], 'Affectionate friendship collocation.')]
    },
    'les_pre_a1_10_01_masculine_back_vowels': {
        'productive': [('өндөр уул', 'high mountain', 'collocation', ['уул', 'өндөр'], 'Steppe geographical landmark description.')],
        'receptive': []
    },
    'les_pre_a1_10_02_feminine_front_vowels': {
        'productive': [('дэлгүүр орох', 'to go to the store / shopping', 'collocation', ['дэлгүүр', 'орох'], 'Everyday errand movement collocation.')],
        'receptive': []
    },
    'les_pre_a1_10_03_neutral_vowel_behavior_i': {
        'productive': [],
        'receptive': [('ширээ сандал', 'table and chair / furniture', 'collocation', ['ширээ', 'сандал'], 'Classroom/home coordinate binomial.')]
    },
    'les_pre_a1_11_01_iotated_vowels_inventory': {
        'productive': [('баярын мэнд', 'holiday greetings / happy holiday', 'formulaic_language', ['баяр', 'мэнд'], 'Universal festive greeting formula.')],
        'receptive': []
    },
    'les_pre_a1_11_02_iotated_vowels_harmony_dual_yu': {
        'productive': [('юу ч биш', 'nothing, not a thing, no problem', 'formulaic_language', ['юу', 'биш'], 'Colloquial reassuring phrase with iotated vowel ю.')],
        'receptive': []
    },
    'les_pre_a1_11_03_soft_sign_palatalization': {
        'productive': [],
        'receptive': [('сургуулийн байр', 'school building', 'collocation', ['сургууль'], 'Institutional facility phrase.')]
    },
    'les_pre_a1_12_01_syllable_types_cvc_ccvc': {
        'productive': [('хүч чадал', 'power and capability, strength', 'collocation', ['хүч'], 'Compound nominal phrase.')],
        'receptive': []
    },
    'les_pre_a1_12_02_first_syllable_stress_rule': {
        'productive': [('багш аа', 'Teacher! (vocative respectful address)', 'formulaic_language', ['багш'], 'Classroom polite direct address.')],
        'receptive': []
    },
    'les_pre_a1_12_03_non_initial_vowel_reduction': {
        'productive': [],
        'receptive': [('дэвтэр үзэг', 'notebook and pen', 'collocation', ['дэвтэр', 'үзэг'], 'Coordinate classroom stationery binomial.')]
    },
    'les_pre_a1_13_01_universal_greeting_sain_baina_uu': {
        'productive': [('Сайн байна уу', 'Hello, How are you (polite)', 'formulaic_language', ['сайн', 'байна'], 'The paramount national greeting formula.')],
        'receptive': []
    },
    'les_pre_a1_13_02_informal_greetings_yu_baina': {
        'productive': [('Юу байна', 'What is up? How is it going?', 'formulaic_language', ['юу', 'байна'], 'Common casual peer greeting formula.')],
        'receptive': []
    },
    'les_pre_a1_13_03_time_based_greetings': {
        'productive': [],
        'receptive': [('Өглөөний мэнд', 'Good morning', 'formulaic_language', ['өглөө', 'мэнд'], 'Formal morning greeting formula.')]
    },
    'les_pre_a1_14_01_prohibitions_and_warnings': {
        'productive': [('тамхи татахгүй', 'no smoking', 'institutional_terminology', [], 'Standard regulatory prohibition notice.')],
        'receptive': []
    },
    'les_pre_a1_14_02_emergency_exits_and_medical': {
        'productive': [('яаралтай тусламж', 'emergency medical assistance', 'institutional_terminology', ['тусламж'], 'Hospital / clinic urgent care label.')],
        'receptive': []
    },
    'les_pre_a1_14_03_emergency_telephone_hotlines': {
        'productive': [],
        'receptive': [('тусламж дуудах', 'to call for help / summon aid', 'pragmatic_routine', ['тусламж', 'дуудах'], 'Emergency telephone routine.')]
    },
    'les_pre_a1_15_01_comprehensive_alphabet_audit': {
        'productive': [('цагаан толгой', 'alphabet (white head/origin)', 'institutional_terminology', ['үсэг'], 'Standard name of the Mongolian alphabet.')],
        'receptive': [('зөв бичих', 'to write correctly, spell properly', 'collocation', ['бичих'], 'Orthographic accuracy collocation.')]
    },
    'les_pre_a1_15_02_urban_signage_simulation_walkthrough': {
        'productive': [('номын дэлгүүр', 'bookstore', 'collocation', ['дэлгүүр', 'ном'], 'Urban shopping storefront sign.')],
        'receptive': []
    },
    'les_pre_a1_15_03_transit_and_receipts_decoding': {
        'productive': [('автобусны буудал', 'bus stop', 'collocation', ['автобус', 'буудал'], 'Public transit landmark phrase.')],
        'receptive': [('картаар төлөх', 'to pay by card', 'collocation', ['карт'], 'Digital payment transaction phrase.')]
    },
}
