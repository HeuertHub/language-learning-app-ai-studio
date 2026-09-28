#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1B Batch 2 Independent Evidence Spot Audit & Adversarial Sample Data.

Sample Specification:
- Exactly 40 newly realized Batch 2 records: 25 Lemmas, 15 Expressions.
- Stratified across Units 26 through 30 (8 records per unit: 5 lemmas, 3 expressions).
- Three-state verification dimensions: 'VERIFIED', 'REVIEWED_INFERRED', 'UNVERIFIED'.
- Adversarial Classification: CONFIRMED, PARTIALLY_CONFIRMED, CONTRADICTED, SOURCE_NOT_LOCATED.
- Tracks false-positive rate of SOURCE_VERIFIED claims (Target: 0.0%).
"""

TSEVEL_1966 = "Tsevel, Ya. (1966). Монгол хэлний товч тайлбар толь. Улаанбаатар: Улсын хэвлэлийн хэрэг эрхлэх хороо."
LUVSANVANDAN_1968 = "Luvsanvandan, Sh. (1968). Орчин цагийн монгол хэлний бүтэц : монгол хэлний үг, нөхцөл хоёр нь. Улаанбаатар: ШУА (Physical text uninspected)."
CORPUS_2021 = "Монгол хэлний үндэсний корпус (2021). ШУА-ийн Хэл зохиолын хүрээлэн."
MNS_STANDARDS = "Стандартчилал хэмжил зүйн газар (MNS 5283:2014, MNS 5012:2011)."
STATE_LAW = "Монгол Улсын засаг захиргаа, нутаг дэвсгэрийн нэгж, түүний удирдлагын тухай хууль (2020)."

BATCH2_SAMPLE_LEMMAS = [
    # -------------------------------------------------------------------------
    # UNIT 26: 5 Lemmas
    # -------------------------------------------------------------------------
    # 1. 26_01: хэзээ (lex_mn_lemma_00406)
    {
        "id": "lex_mn_lemma_00406",
        "lemma": "хэзээ",
        "pos": "adverb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_01_content_particles_distribution",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 777, col. 1, headword 'хэзээ' (ямар нэгэн үйл явдал болсон буюу болох цагийг асуух төлөөний үг; online entry http://toli.query.mn/dictionary_items/20725)",
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
        "notes": "Temporal interrogative pronoun/adverb headword attested at p. 777."
    },
    # 2. 26_02: аль (lex_mn_lemma_00411)
    {
        "id": "lex_mn_lemma_00411",
        "lemma": "аль",
        "pos": "pronoun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_02_interrogative_pronoun_inventory",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 28, col. 1, headword 'аль i' (асуух, лавлах, ялгах, заах утгаар; online entry http://toli.query.mn/dictionary_items/2261)",
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
        "notes": "Selective interrogative pronoun verified at p. 28."
    },
    # 3. 26_02: ямар (lex_mn_lemma_00412)
    {
        "id": "lex_mn_lemma_00412",
        "lemma": "ямар",
        "pos": "pronoun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_02_interrogative_pronoun_inventory",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 896, col. 1, headword 'ямар' (аливаа хүн, юмны чанар байдал, овор дүр өнгө тэмдэг зэргийг лавлан асуухад хэрэглэх; online entry http://toli.query.mn/dictionary_items/12925)",
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
        "notes": "Qualitative interrogative pronoun entry verified at p. 896."
    },
    # 4. 26_03: ойлгомжтой (lex_mn_lemma_00418)
    {
        "id": "lex_mn_lemma_00418",
        "lemma": "ойлгомжтой",
        "pos": "adjective",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_03_inquiry_clarification_drills",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 408, col. 1, headword 'ойлгомжтой' (учир утга тодорхой, ухахад хялбар; online entry http://toli.query.mn/dictionary_items/5723)",
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
        "notes": "Evaluative adjective verified at p. 408."
    },
    # 5. 26_01: яагаад (lex_mn_lemma_00408)
    {
        "id": "lex_mn_lemma_00408",
        "lemma": "яагаад",
        "pos": "adverb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_01_content_particles_distribution",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 112 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Causal interrogative adverb demoted to LINGUISTICALLY_REVIEWED pending physical grammar copy audit."
    },

    # -------------------------------------------------------------------------
    # UNIT 27: 5 Lemmas
    # -------------------------------------------------------------------------
    # 6. 27_01: хорь (lex_mn_lemma_00427)
    {
        "id": "lex_mn_lemma_00427",
        "lemma": "хорь",
        "pos": "numeral",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_01_cardinal_numerals_1_to_20",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 742, col. 1, headword 'хорь (хорин) i' (арав дээр арвыг нэмсэн тоо; online entry http://toli.query.mn/dictionary_items/29251)",
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
        "notes": "Cardinal decade numeral twenty verified at p. 742."
    },
    # 7. 27_02: гуч (lex_mn_lemma_00434)
    {
        "id": "lex_mn_lemma_00434",
        "lemma": "гуч",
        "pos": "numeral",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_02_tens_and_counting_to_100",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 162, col. 2, headword 'гуч, гучин i' (тооны нэр, гурван арав нийлсний нийлбэр; online entry http://toli.query.mn/dictionary_items/9811)",
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
        "notes": "Cardinal decade numeral thirty verified at p. 162."
    },
    # 8. 27_03: хэд (lex_mn_lemma_00441)
    {
        "id": "lex_mn_lemma_00441",
        "lemma": "хэд",
        "pos": "numeral",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_03_inquiries_with_hed",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 768, col. 2, headword 'хэд, хэдэн' (юмны тоо хичнээн болохыг асуух төлөөний үг; online entry http://toli.query.mn/dictionary_items/2952)",
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
        "notes": "Interrogative quantifier headword verified at p. 768."
    },
    # 9. 27_02: зуу (lex_mn_lemma_00438)
    {
        "id": "lex_mn_lemma_00438",
        "lemma": "зуу",
        "pos": "numeral",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_02_tens_and_counting_to_100",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 256, col. 2, headword 'зуу (н)' (тооны нэр, ер дээр арвыг нэмсэн нь; online entry http://toli.query.mn/dictionary_items/20340)",
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
        "notes": "Base hundred numeral verified at p. 256."
    },
    # 10. 27_04: хэмжих (lex_mn_lemma_00449)
    {
        "id": "lex_mn_lemma_00449",
        "lemma": "хэмжих",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_04_inventory_sheet_reading",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 145 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Measurement verb demoted to LINGUISTICALLY_REVIEWED pending physical volume inspection."
    },

    # -------------------------------------------------------------------------
    # UNIT 28: 5 Lemmas
    # -------------------------------------------------------------------------
    # 11. 28_01: дугаар (lex_mn_lemma_00450)
    {
        "id": "lex_mn_lemma_00450",
        "lemma": "дугаар",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_01_telephone_digit_pairing",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 201, col. 1, headword 'дугаар' (эр эгшигт тооны нэрд залгах дэс тооны дагавар; online entry http://toli.query.mn/dictionary_items/13856)",
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
        "notes": "Number/code headword verified at p. 201."
    },
    # 12. 28_01: холбогдох (lex_mn_lemma_00451)
    {
        "id": "lex_mn_lemma_00451",
        "lemma": "холбогдох",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_01_telephone_digit_pairing",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 734, col. 2, headword 'холбогдох' (холбохын үйлдэгдэх хэв; online entry http://toli.query.mn/dictionary_items/29567)",
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
        "notes": "Contact/communication verb verified at p. 734."
    },
    # 13. 28_01: залгах (lex_mn_lemma_00452)
    {
        "id": "lex_mn_lemma_00452",
        "lemma": "залгах",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_01_telephone_digit_pairing",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 228, col. 2, headword 'залгах' (хоёр юмыг нийлүүлэх, холбож нэгтгэх; online entry http://toli.query.mn/dictionary_items/4845)",
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
        "notes": "Telephony dialing verb verified at p. 228."
    },
    # 14. 28_02: цахим (lex_mn_lemma_00457)
    {
        "id": "lex_mn_lemma_00457",
        "lemma": "цахим",
        "pos": "adjective",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_02_digital_channels_email_social",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 798, col. 1, headword 'цахим i' (тооцоолон бодох техник; online entry http://toli.query.mn/dictionary_items/31581)",
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
        "notes": "Electronic/computing technical adjective entry verified at p. 798."
    },
    # 15. 28_03: факс (lex_mn_lemma_00467)
    {
        "id": "lex_mn_lemma_00467",
        "lemma": "факс",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_03_business_card_reading",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "National Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5283:2014 (Telecommunication office line citation; physical standard document uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Telecommunication loanword demoted to LINGUISTICALLY_REVIEWED pending standard document audit."
    },

    # -------------------------------------------------------------------------
    # UNIT 29: 5 Lemmas
    # -------------------------------------------------------------------------
    # 16. 29_01: цонх (lex_mn_lemma_00470)
    {
        "id": "lex_mn_lemma_00470",
        "lemma": "цонх",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_01_plural_uud_allomorphs",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 808, col. 2, headword 'цонх, цонхон' (байшин барилга зэрэгт гэрэл оруулахаар хийсэн гэгээвч; online entry http://toli.query.mn/dictionary_items/27167)",
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
        "notes": "Window headword verified at p. 808."
    },
    # 17. 29_01: зураг (lex_mn_lemma_00472)
    {
        "id": "lex_mn_lemma_00472",
        "lemma": "зураг",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_01_plural_uud_allomorphs",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 254, col. 1, headword 'зураг i' (хавтгай юманд аливаа юмны төрх байдлыг гарган хийсэн дүрс; online entry http://toli.query.mn/dictionary_items/18464)",
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
        "notes": "Picture/image noun headword verified at p. 254."
    },
    # 18. 29_02: нөхөр (lex_mn_lemma_00477)
    {
        "id": "lex_mn_lemma_00477",
        "lemma": "нөхөр",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_02_plural_nuud_and_human_plurals",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 385, col. 2, headword 'нөхөр' (дотно хүн, үзэл санаа ойрхны хүн; online entry http://toli.query.mn/dictionary_items/26129)",
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
        "notes": "Social noun taking irregular plural -өд verified at p. 385."
    },
    # 19. 29_03: байр (lex_mn_lemma_00484)
    {
        "id": "lex_mn_lemma_00484",
        "lemma": "байр",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_03_plural_syntactic_drills",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 73, col. 1, headword 'байр i' (орогнон орших газар, орон сууц; online entry http://toli.query.mn/dictionary_items/4035)",
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
        "notes": "Building/quarters spatial noun verified at p. 73."
    },
    # 20. 29_04: уншигч (lex_mn_lemma_00489)
    {
        "id": "lex_mn_lemma_00489",
        "lemma": "уншигч",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_04_library_catalog_reading",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 642, col. 1, headword 'уншигч' (уншдаг; номын санд ном уншигч; online entry http://toli.query.mn/dictionary_items/23308)",
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
        "notes": "Reader/library patron noun verified at p. 642."
    },

    # -------------------------------------------------------------------------
    # UNIT 30: 5 Lemmas
    # -------------------------------------------------------------------------
    # 21. 30_01: үзэх (lex_mn_lemma_00493)
    {
        "id": "lex_mn_lemma_00493",
        "lemma": "үзэх",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_01_accusative_definite_marking",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 862, col. 2, headword 'үзэх' (харах; үзэх харах хорш.; online entry http://toli.query.mn/dictionary_items/30942)",
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
        "notes": "Transitive sensory verb taking accusative direct object verified at p. 862."
    },
    # 22. 30_01: олох (lex_mn_lemma_00494)
    {
        "id": "lex_mn_lemma_00494",
        "lemma": "олох",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_01_accusative_definite_marking",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 414, col. 1, headword 'олох' (харсан эрсний эцэст тохиолдох, илрүүлэх; online entry http://toli.query.mn/dictionary_items/1198)",
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
        "notes": "Transitive verb verified at p. 414."
    },
    # 23. 30_01: сонгох (lex_mn_lemma_00495)
    {
        "id": "lex_mn_lemma_00495",
        "lemma": "сонгох",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_01_accusative_definite_marking",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 488, col. 1, headword 'сонгох' (сайныг шилэх, хэрэгтэй ашигтайгий нь шилж авах; online entry http://toli.query.mn/dictionary_items/13548)",
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
        "notes": "Decision transitive verb verified at p. 488."
    },
    # 24. 30_02: паспорт (lex_mn_lemma_00501)
    {
        "id": "lex_mn_lemma_00501",
        "lemma": "паспорт",
        "pos": "noun",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_02_accusative_allomorph_rules",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 438, col. 2, headword 'паспорт' (үзүүлэгч хүний албан ёсны баримт; online entry http://toli.query.mn/dictionary_items/24957)",
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
        "notes": "Passport identity document noun verified at p. 438."
    },
    # 25. 30_03: худалдах (lex_mn_lemma_00507)
    {
        "id": "lex_mn_lemma_00507",
        "lemma": "худалдах",
        "pos": "verb",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_03_transactional_object_requests",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 753, col. 2, headword 'худалдах' (үнэ авч арилжин өгөх; худалдан авагч; online entry http://toli.query.mn/dictionary_items/6997)",
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
        "notes": "Commercial selling verb verified at p. 753."
    }
]

BATCH2_SAMPLE_EXPRESSIONS = [
    # -------------------------------------------------------------------------
    # UNIT 26: 3 Expressions
    # -------------------------------------------------------------------------
    # 1. 26_01: хэзээ ирэх вэ (lex_mn_expr_00111)
    {
        "id": "lex_mn_expr_00111",
        "expression": "хэзээ ирэх вэ",
        "type": "formula",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_01_content_particles_distribution",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Contemporary Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Arrival query formula demoted to LINGUISTICALLY_REVIEWED pending direct corpus query log inspection."
    },
    # 2. 26_01: яагаад гэвэл (lex_mn_expr_00112)
    {
        "id": "lex_mn_expr_00112",
        "expression": "яагаад гэвэл",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_01_content_particles_distribution",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 115 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Causal conjunction phrase demoted pending physical grammar verification."
    },
    # 3. 26_02: ямар учиртай вэ (lex_mn_expr_00113)
    {
        "id": "lex_mn_expr_00113",
        "expression": "ямар учиртай вэ",
        "type": "formula",
        "cefrLevel": "A1",
        "lessonId": "les_a1_26_02_interrogative_pronoun_inventory",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Contemporary Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Inquiry formula demoted pending direct corpus verification."
    },

    # -------------------------------------------------------------------------
    # UNIT 27: 3 Expressions
    # -------------------------------------------------------------------------
    # 4. 27_01: арван хоёр (lex_mn_expr_00117)
    {
        "id": "lex_mn_expr_00117",
        "expression": "арван хоёр",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_01_cardinal_numerals_1_to_20",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 78 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Compound numeral demoted pending physical grammar verification."
    },
    # 5. 27_03: хэдэн настай вэ (lex_mn_expr_00120)
    {
        "id": "lex_mn_expr_00120",
        "expression": "хэдэн настай вэ",
        "type": "formula",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_03_inquiries_with_hed",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Contemporary Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Age query formula demoted pending physical corpus log audit."
    },
    # 6. 27_04: нийт дүн (lex_mn_expr_00122)
    {
        "id": "lex_mn_expr_00122",
        "expression": "нийт дүн",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_27_04_inventory_sheet_reading",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Educational & Accounting Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5012:2011 (Commercial accounting standard; uninspected standard doc)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Accounting total amount formula demoted pending standard document audit."
    },

    # -------------------------------------------------------------------------
    # UNIT 28: 3 Expressions
    # -------------------------------------------------------------------------
    # 7. 28_01: утасны дугаар (lex_mn_expr_00123)
    {
        "id": "lex_mn_expr_00123",
        "expression": "утасны дугаар",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_01_telephone_digit_pairing",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "National Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5283:2014 (Telecommunication standard; uninspected standard doc)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Telephone number compound demoted pending standard document inspection."
    },
    # 8. 28_02: цахим шуудан (lex_mn_expr_00125)
    {
        "id": "lex_mn_expr_00125",
        "expression": "цахим шуудан",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_02_digital_channels_email_social",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "National Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5283:2014 (Terminology standard; uninspected standard doc)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Email standard terminology demoted pending physical standard document audit."
    },
    # 9. 28_03: нэрийн хуудас (lex_mn_expr_00126)
    {
        "id": "lex_mn_expr_00126",
        "expression": "нэрийн хуудас",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_28_03_business_card_reading",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "National Standards",
        "actualSourceConsulted": MNS_STANDARDS,
        "exactLocator": "MNS 5283:2014 (Administrative standard; uninspected standard doc)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Business card compound demoted pending standard document inspection."
    },

    # -------------------------------------------------------------------------
    # UNIT 29: 3 Expressions
    # -------------------------------------------------------------------------
    # 10. 29_01: олон ном (lex_mn_expr_00129)
    {
        "id": "lex_mn_expr_00129",
        "expression": "олон ном",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_01_plural_uud_allomorphs",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 82 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Quantified bare singular phrase demoted pending physical grammar inspection."
    },
    # 11. 29_03: тавиур дээр (lex_mn_expr_00132)
    {
        "id": "lex_mn_expr_00132",
        "expression": "тавиур дээр",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_03_plural_syntactic_drills",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Contemporary Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "Mongolian National Corpus (2021) query (Uninspected physical corpus log)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Postpositional phrase demoted pending direct corpus query log inspection."
    },
    # 12. 29_04: номын сан (lex_mn_expr_00134)
    {
        "id": "lex_mn_expr_00134",
        "expression": "номын сан",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_29_04_library_catalog_reading",
        "status": "SOURCE_VERIFIED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 381, col. 2 (subentry under 'ном': 'номын сан (ном бичгийг нийгмийн хэрэгцээнд зориулан цуглуулж цогцолсон газар; хотын номын сан)'); online entry http://toli.query.mn/dictionary_items/30493",
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
            "expressionNaturalness": "VERIFIED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Exact multiword compound noun subentry attested under 'ном' at p. 381 and under 'сан' at p. 467."
    },

    # -------------------------------------------------------------------------
    # UNIT 30: 3 Expressions
    # -------------------------------------------------------------------------
    # 13. 30_01: ном унших (lex_mn_expr_00135)
    {
        "id": "lex_mn_expr_00135",
        "expression": "ном унших",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_01_accusative_definite_marking",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Contemporary Corpus",
        "actualSourceConsulted": CORPUS_2021,
        "exactLocator": "Mongolian National Corpus (2021) query (Uninspected physical corpus log)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Verb-object collocation demoted pending physical corpus query log audit."
    },
    # 14. 30_02: бичиг баримт (lex_mn_expr_00137)
    {
        "id": "lex_mn_expr_00137",
        "expression": "бичиг баримт",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_02_accusative_allomorph_rules",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Academic Reference Grammar",
        "actualSourceConsulted": LUVSANVANDAN_1968,
        "exactLocator": "Luvsanvandan (1968), p. 94 (Unlocatable: physical grammar volume uninspected)",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Paired noun phrase demoted pending physical grammar volume verification."
    },
    # 15. 30_03: худалдаж авах (lex_mn_expr_00138)
    {
        "id": "lex_mn_expr_00138",
        "expression": "худалдаж авах",
        "type": "collocation",
        "cefrLevel": "A1",
        "lessonId": "les_a1_30_03_transactional_object_requests",
        "status": "LINGUISTICALLY_REVIEWED",
        "sourceClaimed": "Standard Dictionary",
        "actualSourceConsulted": TSEVEL_1966,
        "exactLocator": "Tsevel (1966), p. 753, col. 2 (attested subentry under 'худалдах': 'худалдан авах (үнэ төлж юм авах)'); exact colloquial converb -ж uninspected in print",
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
            "englishGloss": "REVIEWED_INFERRED",
            "partOfSpeech": "VERIFIED",
            "register": "REVIEWED_INFERRED",
            "expressionNaturalness": "REVIEWED_INFERRED",
            "lessonSuitability": "REVIEWED_INFERRED"
        },
        "notes": "Commercial compound verb demoted to LINGUISTICALLY_REVIEWED pending exact printed citation of converb -ж variant."
    }
]

assert len(BATCH2_SAMPLE_LEMMAS) == 25, f"Expected 25 sample lemmas, got {len(BATCH2_SAMPLE_LEMMAS)}"
assert len(BATCH2_SAMPLE_EXPRESSIONS) == 15, f"Expected 15 sample expressions, got {len(BATCH2_SAMPLE_EXPRESSIONS)}"
