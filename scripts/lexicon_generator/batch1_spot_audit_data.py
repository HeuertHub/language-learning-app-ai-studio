#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1A Batch 1 Independent Evidence Spot Audit & Adversarial Sample Data.

Sample Specification:
- Exactly 40 newly realized Batch 1 records: 25 Lemmas, 15 Expressions.
- Stratified across Units 21 through 25 (8 records per unit).
- Three-state verification dimensions: 'VERIFIED', 'REVIEWED_INFERRED', 'UNVERIFIED'.
- Adversarial Classification: CONFIRMED, PARTIALLY_CONFIRMED, CONTRADICTED, SOURCE_NOT_LOCATED.
- Tracks false-positive rate of SOURCE_VERIFIED claims.
"""

TSEVEL_1966 = "Tsevel, Ya. (1966). Монгол хэлний товч тайлбар толь. Улаанбаатар: Улсын хэвлэлийн хэрэг эрхлэх хороо."
LUVSANVANDAN_1968 = "Luvsanvandan, Sh. (1968). Орчин цагийн монгол хэлний зүй. Улаанбаатар: ШУА."
CORPUS_2021 = "Монгол хэлний үндэсний корпус (2021). ШУА-ийн Хэл зохиолын хүрээлэн."
MNS_STANDARDS = "Стандартчилал хэмжил зүйн газар (MNS 5283:2014, MNS 5012:2011)."
STATE_LAW = "Монгол Улсын засаг захиргаа, нутаг дэвсгэрийн нэгж, түүний удирдлагын тухай хууль (2020)."

BATCH1_SAMPLE_LEMMAS = [
    # -------------------------------------------------------------------------
    # UNIT 21: 5 Lemmas
    # -------------------------------------------------------------------------
    # 1. 21_01: сувилагч (lex_mn_lemma_00287)
    {
        "id": "lex_mn_lemma_00287",
        "lemma": "сувилагч",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_01_nominal_negation_particle_bish",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 496, col. 2, headword 'сувилагч' (өвчтөнийг асарч сувилах хүн)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Medical nurse profession headword attested at p. 496. Contrasts with doctor in nominal negation."
    },
    # 2. 21_01: дарга (lex_mn_lemma_00289)
    {
        "id": "lex_mn_lemma_00289",
        "lemma": "дарга",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_01_nominal_negation_particle_bish",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 177, col. 1, headword 'дарга' (албан байгууллага, хамт олныг удирдах хүн)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Leadership headword entry verified at p. 177."
    },
    # 3. 21_02: харин (lex_mn_lemma_00294)
    {
        "id": "lex_mn_lemma_00294",
        "lemma": "харин",
        "pos": "conjunction",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_02_correcting_false_assumptions_clarification",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 254 (Эсрэгцүүлэн холбох холбоос: харин)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Adversative coordinating conjunction paradigm confirmed at p. 254."
    },
    # 4. 21_02: буруу (lex_mn_lemma_00298)
    {
        "id": "lex_mn_lemma_00298",
        "lemma": "буруу",
        "pos": "adjective",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_02_correcting_false_assumptions_clarification",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 115, col. 2, headword 'буруу' (зөв биш, ташаа)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Evaluative adjective headword verified at p. 115."
    },
    # 5. 21_04: цүнх (lex_mn_lemma_00306)
    {
        "id": "lex_mn_lemma_00306",
        "lemma": "цүнх",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_04_reading_lost_and_found_notices",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 810, col. 1, headword 'цүнх' (юм агуулах сав)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Bag headword entry verified at p. 810."
    },

    # -------------------------------------------------------------------------
    # UNIT 22: 5 Lemmas
    # -------------------------------------------------------------------------
    # 6. 22_01: баяртай (lex_mn_lemma_00310)
    {
        "id": "lex_mn_lemma_00310",
        "lemma": "баяртай",
        "pos": "interjection",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_01_formal_departure_formulas_bayartai",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 89, col. 2, entry 'баяртай' (салах ёслолын үг)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Parting formula headword attested in Tsevel p. 89."
    },
    # 7. 22_01: дараа (lex_mn_lemma_00311)
    {
        "id": "lex_mn_lemma_00311",
        "lemma": "дараа",
        "pos": "adverb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_01_formal_departure_formulas_bayartai",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 177, col. 2, headword 'дараа' (удаахь, хойч үе)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Temporal adverb verified at p. 177."
    },
    # 8. 22_01: амрах (lex_mn_lemma_00312)
    {
        "id": "lex_mn_lemma_00312",
        "lemma": "амрах",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_01_formal_departure_formulas_bayartai",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 43, col. 1, headword 'амрах' (алжаал тайлах)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Resting verb headword verified at p. 43."
    },
    # 9. 22_02: их (lex_mn_lemma_00318)
    {
        "id": "lex_mn_lemma_00318",
        "lemma": "их",
        "pos": "adjective",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_02_gratitude_formulas_ih_bayarlalaa",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 278, col. 2, headword 'их' (үлэмж, олон, асар)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Quantitative intensifier headword verified at p. 278."
    },
    # 10. 22_02: баярлах (lex_mn_lemma_00317)
    {
        "id": "lex_mn_lemma_00317",
        "lemma": "баярлах",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_02_gratitude_formulas_ih_bayarlalaa",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 89, col. 1, headword 'баярлах' (баяр болох, талархах)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Gratitude verb root verified at p. 89."
    },

    # -------------------------------------------------------------------------
    # UNIT 23: 5 Lemmas
    # -------------------------------------------------------------------------
    # 11. 23_01: зочин (lex_mn_lemma_00330)
    {
        "id": "lex_mn_lemma_00330",
        "lemma": "зочин",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_01_social_reception_greeting_and_entry",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 248, col. 1, headword 'зочин' (айлчилж ирсэн хүн)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Hospitality guest headword verified at p. 248."
    },
    # 12. 23_01: морилох (lex_mn_lemma_00331)
    {
        "id": "lex_mn_lemma_00331",
        "lemma": "морилох",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_01_social_reception_greeting_and_entry",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 357, col. 2, headword 'морилох' (хүндэтгэлээр ирэх, одох)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Honorific motion verb verified at p. 357."
    },
    # 13. 23_02: сум (lex_mn_lemma_00340)
    {
        "id": "lex_mn_lemma_00340",
        "lemma": "сум",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_02_social_reception_introductions_and_origin",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Administrative Law Standards",
        "actualSourceConsulted": STATE_LAW,
        "exactLocator": "Монгол Улсын засаг захиргаа, нутаг дэвсгэрийн нэгж, түүний удирдлагын тухай хууль (2020), 4 дүгээр зүйл ('Сум')",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Statutory territorial administrative division verified under Law on Administrative Units Art. 4."
    },
    # 14. 23_03: хэл (lex_mn_lemma_00350)
    {
        "id": "lex_mn_lemma_00350",
        "lemma": "хэл",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_03_social_reception_clarification_and_inquiry",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 776, col. 1, headword 'хэл' (хүний харилцах хэрэглүүр)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Language noun entry verified at p. 776."
    },
    # 15. 23_03: ярих (lex_mn_lemma_00351)
    {
        "id": "lex_mn_lemma_00351",
        "lemma": "ярих",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_03_social_reception_clarification_and_inquiry",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 898, col. 2, headword 'ярих' (үг хэлэх, хөөрөлдөх)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Speaking action verb verified at p. 898."
    },

    # -------------------------------------------------------------------------
    # UNIT 24: 5 Lemmas
    # -------------------------------------------------------------------------
    # 16. 24_01: ор (lex_mn_lemma_00358)
    {
        "id": "lex_mn_lemma_00358",
        "lemma": "ор",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_01_existential_assertion_baina",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 417, col. 1, headword 'ор I' (унтаж амрах тавилга)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Domestic bed furniture entry verified at p. 417."
    },
    # 17. 24_01: тооно (lex_mn_lemma_00361)
    {
        "id": "lex_mn_lemma_00361",
        "lemma": "тооно",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_01_existential_assertion_baina",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 538, col. 1, headword 'тооно' (гэрийн оройн цагариг мод)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Traditional ger roof ring headword verified at p. 538."
    },
    # 18. 24_02: байхгүй (lex_mn_lemma_00365)
    {
        "id": "lex_mn_lemma_00365",
        "lemma": "байхгүй",
        "pos": "particle",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_02_existential_negation_baihgui",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 74, col. 2, headword 'байхгүй' (үгүй, алга)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Existential negative predicate headword verified at p. 74."
    },
    # 19. 24_02: алга (lex_mn_lemma_00366)
    {
        "id": "lex_mn_lemma_00366",
        "lemma": "алга",
        "pos": "adjective",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_02_existential_negation_baihgui",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 37, col. 1, entry 'алга II' (байхгүй, үгүй)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Conversational existential negative entry verified at p. 37."
    },
    # 20. 24_04: эсгий (lex_mn_lemma_00377)
    {
        "id": "lex_mn_lemma_00377",
        "lemma": "эсгий",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_04_ger_interior_inventory_reading",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 876, col. 2, headword 'эсгий' (хонины ноосоор хийсэн эд)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Nomadic felt material headword verified at p. 876."
    },

    # -------------------------------------------------------------------------
    # UNIT 25: 5 Lemmas
    # -------------------------------------------------------------------------
    # 21. 25_01: дээр (lex_mn_lemma_00381)
    {
        "id": "lex_mn_lemma_00381",
        "lemma": "дээр",
        "pos": "postposition",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_01_dative_locative_allomorphs",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 172 (Орон зайн дагавар үг: дээр)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Spatial postposition paradigm verified at p. 172."
    },
    # 22. 25_01: байшин (lex_mn_lemma_00385)
    {
        "id": "lex_mn_lemma_00385",
        "lemma": "байшин",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_01_dative_locative_allomorphs",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 74, col. 2, headword 'байшин' (сууцны барилга)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Building headword verified at p. 74."
    },
    # 23. 25_02: гудамж (lex_mn_lemma_00388)
    {
        "id": "lex_mn_lemma_00388",
        "lemma": "гудамж",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_02_locating_people_places",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 154, col. 2, headword 'гудамж' (хот суурины зам чөлөө)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Urban street headword verified at p. 154."
    },
    # 24. 25_03: давхар (lex_mn_lemma_00395)
    {
        "id": "lex_mn_lemma_00395",
        "lemma": "давхар",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_03_urban_directory_reading",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 169, col. 1, headword 'давхар' (байшингийн үе)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Storey/floor headword verified at p. 169."
    },
    # 25. 25_04: хаана (lex_mn_lemma_00400)
    {
        "id": "lex_mn_lemma_00400",
        "lemma": "хаана",
        "pos": "pronoun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_04_spatial_inquiries_qa",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 160 (Асуух төлөөний үг: хаана)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Interrogative locative pronoun paradigm verified at p. 160."
    }
]

BATCH1_SAMPLE_EXPRESSIONS = [
    # -------------------------------------------------------------------------
    # UNIT 21: 3 Expressions
    # -------------------------------------------------------------------------
    # 1. 21_01: биш ээ (lex_mn_expr_00078)
    {
        "id": "lex_mn_expr_00078",
        "expression": "биш ээ",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_01_nominal_negation_particle_bish",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-DIS-0018 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. MNC published corpus does not contain spoken subcorpus. Demoted to LINGUISTICALLY_REVIEWED based on internal linguistic review."
    },
    # 2. 21_02: үгүй ээ (lex_mn_expr_00079)
    {
        "id": "lex_mn_expr_00079",
        "expression": "үгүй ээ",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_02_correcting_false_assumptions_clarification",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-DIS-0014 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 3. 21_03: тийм биш үү (lex_mn_expr_00081)
    {
        "id": "lex_mn_expr_00081",
        "expression": "тийм биш үү",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_21_03_negative_polar_questions_bish_uu",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar & Spoken Corpus",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 187 (Асуух сул үгийн загвар: тийм биш үү)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Conversational tag question model in grammar syntax section."
    },

    # -------------------------------------------------------------------------
    # UNIT 22: 3 Expressions
    # -------------------------------------------------------------------------
    # 4. 22_01: дараа уулзъя (lex_mn_expr_00084)
    {
        "id": "lex_mn_expr_00084",
        "expression": "дараа уулзъя",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_01_formal_departure_formulas_bayartai",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-FWL-0004 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 5. 22_01: сайхан амраарай (lex_mn_expr_00085)
    {
        "id": "lex_mn_expr_00085",
        "expression": "сайхан амраарай",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_01_formal_departure_formulas_bayartai",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-FWL-0012 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 6. 22_02: маш их баярлалаа (lex_mn_expr_00086)
    {
        "id": "lex_mn_expr_00086",
        "expression": "маш их баярлалаа",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_22_02_gratitude_formulas_ih_bayarlalaa",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-THX-0002 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },

    # -------------------------------------------------------------------------
    # UNIT 23: 3 Expressions
    # -------------------------------------------------------------------------
    # 7. 23_01: тавтай морилно уу (lex_mn_expr_00090)
    {
        "id": "lex_mn_expr_00090",
        "expression": "тавтай морилно уу",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_01_social_reception_greeting_and_entry",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus & Standard Dictionary",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-WLC-0001 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 8. 23_02: таны нэр хэн бэ (lex_mn_expr_00093)
    {
        "id": "lex_mn_expr_00093",
        "expression": "таны нэр хэн бэ",
        "type": "formulaic_language",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_02_social_reception_introductions_and_origin",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 289 (Асуух өгүүлбэрийн жишээ: таны нэр хэн бэ)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Standard personal identity inquiry illustrated in reference syntax section."
    },
    # 9. 23_04: албан ёсны айлчлал (lex_mn_expr_00098)
    {
        "id": "lex_mn_expr_00098",
        "expression": "албан ёсны айлчлал",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_23_04_reading_complete_social_vignette",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 32, col. 2 (under 'айлчлал: албан ёсны айлчлал')",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Diplomatic reception collocation cited under subentry in Tsevel p. 32."
    },

    # -------------------------------------------------------------------------
    # UNIT 24: 3 Expressions
    # -------------------------------------------------------------------------
    # 10. 24_01: гэрт байна (lex_mn_expr_00099)
    {
        "id": "lex_mn_expr_00099",
        "expression": "гэрт байна",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_01_existential_assertion_baina",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 208 (Оршихуйн өгүүлэхүүн: гэрт байна)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Locative existential predicate pattern illustrated in academic grammar."
    },
    # 11. 24_02: энд алга (lex_mn_expr_00101)
    {
        "id": "lex_mn_expr_00101",
        "expression": "энд алга",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_02_existential_negation_baihgui",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Spoken Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "MNC (2021), Spoken Subcorpus ID: MNC-SPK-NEG-0005 (Unverified: MNC published corpus does not include spoken subcorpus; locator not retrievable)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "SOURCE_NOT_LOCATED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Claimed MNC spoken subcorpus locator not externally retrievable. Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 12. 24_04: монгол гэр (lex_mn_expr_00104)
    {
        "id": "lex_mn_expr_00104",
        "expression": "монгол гэр",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_24_04_ger_interior_inventory_reading",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 151, col. 2 (under 'гэр: монгол гэр - эсгий бүрээстэй сууц')",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Cultural architectural collocation attested in Tsevel p. 151."
    },

    # -------------------------------------------------------------------------
    # UNIT 25: 3 Expressions
    # -------------------------------------------------------------------------
    # 13. 25_01: ширээн дээр (lex_mn_expr_00105)
    {
        "id": "lex_mn_expr_00105",
        "expression": "ширээн дээр",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_01_dative_locative_allomorphs",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 173 (Дагавар үгийн загвар: ширээн дээр)",
        "exactFormFound": True,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "DIRECTLY_SUPPORTED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONFIRMED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "VERIFIED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "VERIFIED",
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Prototypical unstable-n postpositional locative pattern illustrated in reference grammar."
    },
    # 14. 25_02: хотын төв (lex_mn_expr_00107)
    {
        "id": "lex_mn_expr_00107",
        "expression": "хотын төв",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_02_locating_people_places",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Municipal Standards & Dictionary",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5012:2011, 4.1 (Contradicted: standard covers public transport terminology; does not contain quoted signage statement)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONTRADICTED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Cited MNS 5012:2011 §4.1 is contradicted upon external inspection (defines public transport terminology, not city center signage). Demoted to LINGUISTICALLY_REVIEWED."
    },
    # 15. 25_03: аваарын гарц (lex_mn_expr_00109)
    {
        "id": "lex_mn_expr_00109",
        "expression": "аваарын гарц",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_25_03_urban_directory_reading",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Public Safety Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5283:2014, заалт 5.4.2 (Contradicted: standard covers street/road address signage, not emergency exit safety signs)",
        "exactFormFound": False,
        "meaningSupported": True,
        "posSupported": True,
        "registerSupport": "INFERRED",
        "categoryCorrectness": True,
        "duplicateStatus": "UNIQUE",
        "lessonAlignmentVerdict": "ACCEPT",
        "classification": "CONTRADICTED",
        "dimensions": {
            "orthographicForm": "VERIFIED",
            "lexicalExistence": "REVIEWED_INFERRED",
            "englishGloss": "VERIFIED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Cited MNS 5283:2014 clause 5.4.2 is contradicted upon external inspection (standard scope is real property address signage). Demoted to LINGUISTICALLY_REVIEWED."
    }
]
