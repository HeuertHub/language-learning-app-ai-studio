#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Detailed Tokenized Constituent & Morphological Breakdown for all 77 Pilot Expressions.
Each entry breaks down tokens, root lemmas, inflectional suffixes, resolved lemma IDs,
and intentionally unresolved non-pilot elements.
"""

# Format: index -> list of dicts:
# [{"token": ..., "rootLemma": ..., "resolvedLemmaId": ..., "inflectionalSuffixes": [...], "isUnresolved": bool, "notes": ...}]
CONSTITUENT_ANALYSIS = {
    0: [  # үсэг нүдлэх
        {"token": "үсэг", "rootLemma": "үсэг", "resolvedLemmaId": "lex_mn_lemma_00001", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun in unmarked accusative"},
        {"token": "нүдлэх", "rootLemma": "нүдлэх", "resolvedLemmaId": None, "inflectionalSuffixes": ["-лэх"], "isUnresolved": True, "notes": "Denominal verb derived from нүд (eye); verb slot not in pilot"}
    ],
    1: [  # ном унших
        {"token": "ном", "rootLemma": "ном", "resolvedLemmaId": "lex_mn_lemma_00005", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun"},
        {"token": "унших", "rootLemma": "унших", "resolvedLemmaId": "lex_mn_lemma_00047", "inflectionalSuffixes": ["-их"], "isUnresolved": False, "notes": "Infinitive action verb"}
    ],
    2: [  # гар барих
        {"token": "гар", "rootLemma": "гар", "resolvedLemmaId": "lex_mn_lemma_00009", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Anatomical direct object noun"},
        {"token": "барих", "rootLemma": "барих", "resolvedLemmaId": None, "inflectionalSuffixes": ["-их"], "isUnresolved": True, "notes": "Action verb 'to hold/grasp'; not in pilot lemma slots"}
    ],
    3: [  # үнэн үг
        {"token": "үнэн", "rootLemma": "үнэн", "resolvedLemmaId": "lex_mn_lemma_00016", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Attributive modifier adjective"},
        {"token": "үг", "rootLemma": "үг", "resolvedLemmaId": "lex_mn_lemma_00012", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head noun"}
    ],
    4: [  # өдрийн мэнд
        {"token": "өдрийн", "rootLemma": "өдөр", "resolvedLemmaId": "lex_mn_lemma_00015", "inflectionalSuffixes": ["-ийн"], "isUnresolved": False, "notes": "Genitive temporal noun"},
        {"token": "мэнд", "rootLemma": "мэнд", "resolvedLemmaId": "lex_mn_lemma_00135", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head salutation noun"}
    ],
    5: [  # сүүтэй цай
        {"token": "сүүтэй", "rootLemma": "сүү", "resolvedLemmaId": "lex_mn_lemma_00014", "inflectionalSuffixes": ["-тэй"], "isUnresolved": False, "notes": "Comitative-attributive suffix"},
        {"token": "цай", "rootLemma": "цай", "resolvedLemmaId": "lex_mn_lemma_00089", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head beverage noun"}
    ],
    6: [  # аав ээж
        {"token": "аав", "rootLemma": "аав", "resolvedLemmaId": "lex_mn_lemma_00023", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First element of dvandva compound"},
        {"token": "ээж", "rootLemma": "ээж", "resolvedLemmaId": "lex_mn_lemma_00024", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Second element of dvandva compound"}
    ],
    7: [  # уул ус
        {"token": "уул", "rootLemma": "уул", "resolvedLemmaId": "lex_mn_lemma_00031", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First coordinate element of hendiadys"},
        {"token": "ус", "rootLemma": "ус", "resolvedLemmaId": "lex_mn_lemma_00008", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Second coordinate element of hendiadys"}
    ],
    8: [  # гэртээ харих
        {"token": "гэртээ", "rootLemma": "гэр", "resolvedLemmaId": "lex_mn_lemma_00030", "inflectionalSuffixes": ["-т", "-ээ"], "isUnresolved": False, "notes": "Dative-locative case + reflexive possessive suffix"},
        {"token": "харих", "rootLemma": "харих", "resolvedLemmaId": None, "inflectionalSuffixes": ["-их"], "isUnresolved": True, "notes": "Motion verb 'to return'; non-pilot lemma"}
    ],
    9: [  # багшаас асуух
        {"token": "багшаас", "rootLemma": "багш", "resolvedLemmaId": "lex_mn_lemma_00034", "inflectionalSuffixes": ["-аас"], "isUnresolved": False, "notes": "Ablative source suffix"},
        {"token": "асуух", "rootLemma": "асуух", "resolvedLemmaId": "lex_mn_lemma_00244", "inflectionalSuffixes": ["-х"], "isUnresolved": False, "notes": "Infinitive verb"}
    ],
    10: [  # морь унах
        {"token": "морь", "rootLemma": "морь", "resolvedLemmaId": "lex_mn_lemma_00042", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Unmarked accusative direct object"},
        {"token": "унах", "rootLemma": "унах", "resolvedLemmaId": None, "inflectionalSuffixes": ["-ах"], "isUnresolved": True, "notes": "Verb 'to ride'; non-pilot lemma"}
    ],
    11: [  # таван хошуу мал
        {"token": "таван", "rootLemma": "тав", "resolvedLemmaId": "lex_mn_lemma_00062", "inflectionalSuffixes": ["-н"], "isUnresolved": False, "notes": "Attributive numeral form with unstable -n"},
        {"token": "хошуу", "rootLemma": "хошуу", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Noun 'snout/banner/point'; non-pilot lemma"},
        {"token": "мал", "rootLemma": "мал", "resolvedLemmaId": "lex_mn_lemma_00041", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head collective noun"}
    ],
    12: [  # үг бичих
        {"token": "үг", "rootLemma": "үг", "resolvedLemmaId": "lex_mn_lemma_00012", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun"},
        {"token": "бичих", "rootLemma": "бичих", "resolvedLemmaId": "lex_mn_lemma_00046", "inflectionalSuffixes": ["-их"], "isUnresolved": False, "notes": "Infinitive verb"}
    ],
    13: [  # цэг тавих
        {"token": "цэг", "rootLemma": "цэг", "resolvedLemmaId": "lex_mn_lemma_00050", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Punctuation direct object noun"},
        {"token": "тавих", "rootLemma": "тавих", "resolvedLemmaId": None, "inflectionalSuffixes": ["-их"], "isUnresolved": True, "notes": "Verb 'to put/place'; non-pilot lemma"}
    ],
    14: [  # хайлт хийх
        {"token": "хайлт", "rootLemma": "хайх", "resolvedLemmaId": "lex_mn_lemma_00053", "inflectionalSuffixes": ["-лт"], "isUnresolved": False, "notes": "Deverbal noun of хайх"},
        {"token": "хийх", "rootLemma": "хийх", "resolvedLemmaId": None, "inflectionalSuffixes": ["-их"], "isUnresolved": True, "notes": "Light verb 'to do/make'; non-pilot lemma"}
    ],
    15: [  # нэг хоёр
        {"token": "нэг", "rootLemma": "нэг", "resolvedLemmaId": "lex_mn_lemma_00057", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First cardinal numeral"},
        {"token": "хоёр", "rootLemma": "хоёр", "resolvedLemmaId": "lex_mn_lemma_00058", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Second cardinal numeral"}
    ],
    16: [  # тоо тоолох
        {"token": "тоо", "rootLemma": "тоо", "resolvedLemmaId": "lex_mn_lemma_00060", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Cognate accusative object"},
        {"token": "тоолох", "rootLemma": "тоолох", "resolvedLemmaId": None, "inflectionalSuffixes": ["-лох"], "isUnresolved": True, "notes": "Denominal verb of тоо; non-pilot lemma"}
    ],
    17: [  # анхааралтай сонсоорой
        {"token": "анхааралтай", "rootLemma": "анхаарах", "resolvedLemmaId": None, "inflectionalSuffixes": ["-л", "-тай"], "isUnresolved": True, "notes": "Deverbal noun with comitative suffix acting adverbially"},
        {"token": "сонсоорой", "rootLemma": "сонсох", "resolvedLemmaId": "lex_mn_lemma_00066", "inflectionalSuffixes": ["-оорой"], "isUnresolved": False, "notes": "Polite imperative suffix"}
    ],
    18: [  # нэр ус
        {"token": "нэр", "rootLemma": "нэр", "resolvedLemmaId": "lex_mn_lemma_00054", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First element of dvandva idiom"},
        {"token": "ус", "rootLemma": "ус", "resolvedLemmaId": "lex_mn_lemma_00008", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Second element of dvandva idiom"}
    ],
    19: [  # нэрээ дуудах
        {"token": "нэрээ", "rootLemma": "нэр", "resolvedLemmaId": "lex_mn_lemma_00054", "inflectionalSuffixes": ["-ээ"], "isUnresolved": False, "notes": "Reflexive possessive suffix"},
        {"token": "дуудах", "rootLemma": "дуудах", "resolvedLemmaId": "lex_mn_lemma_00071", "inflectionalSuffixes": ["-ах"], "isUnresolved": False, "notes": "Infinitive verb"}
    ],
    20: [  # иргэний үнэмлэх
        {"token": "иргэний", "rootLemma": "иргэн", "resolvedLemmaId": None, "inflectionalSuffixes": ["-ий"], "isUnresolved": True, "notes": "Genitive noun 'citizen'; non-pilot lemma"},
        {"token": "үнэмлэх", "rootLemma": "үнэмлэх", "resolvedLemmaId": "lex_mn_lemma_00263", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head noun 'identity document'"}
    ],
    21: [  # урт эгшиг
        {"token": "урт", "rootLemma": "урт", "resolvedLemmaId": "lex_mn_lemma_00078", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Modifier adjective"},
        {"token": "эгшиг", "rootLemma": "эгшиг", "resolvedLemmaId": "lex_mn_lemma_00002", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head linguistic noun"}
    ],
    22: [  # хоол идэх
        {"token": "хоол", "rootLemma": "хоол", "resolvedLemmaId": "lex_mn_lemma_00085", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object food noun"},
        {"token": "идэх", "rootLemma": "идэх", "resolvedLemmaId": None, "inflectionalSuffixes": ["-эх"], "isUnresolved": True, "notes": "Verb 'to eat'; non-pilot lemma"}
    ],
    23: [  # халуун хоол
        {"token": "халуун", "rootLemma": "халуун", "resolvedLemmaId": "lex_mn_lemma_00251", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Temperature attribute adjective"},
        {"token": "хоол", "rootLemma": "хоол", "resolvedLemmaId": "lex_mn_lemma_00085", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head food noun"}
    ],
    24: [  # цай уух
        {"token": "цай", "rootLemma": "цай", "resolvedLemmaId": "lex_mn_lemma_00089", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object beverage noun"},
        {"token": "уух", "rootLemma": "уух", "resolvedLemmaId": None, "inflectionalSuffixes": ["-х"], "isUnresolved": True, "notes": "Verb 'to drink'; non-pilot lemma"}
    ],
    25: [  # сайн найз
        {"token": "сайн", "rootLemma": "сайн", "resolvedLemmaId": "lex_mn_lemma_00133", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Evaluative adjective"},
        {"token": "найз", "rootLemma": "найз", "resolvedLemmaId": "lex_mn_lemma_00096", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head social noun"}
    ],
    26: [  # гэр бүл
        {"token": "гэр", "rootLemma": "гэр", "resolvedLemmaId": "lex_mn_lemma_00030", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First element of compound"},
        {"token": "бүл", "rootLemma": "бүл", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Noun 'family group'; non-pilot lemma"}
    ],
    27: [  # эр хүн
        {"token": "эр", "rootLemma": "эр", "resolvedLemmaId": "lex_mn_lemma_00100", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Modifier noun/adjective"},
        {"token": "хүн", "rootLemma": "хүн", "resolvedLemmaId": "lex_mn_lemma_00101", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head human noun"}
    ],
    28: [  # эмэгтэй хүн
        {"token": "эмэгтэй", "rootLemma": "эмэгтэй", "resolvedLemmaId": "lex_mn_lemma_00105", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Modifier gender noun/adjective"},
        {"token": "хүн", "rootLemma": "хүн", "resolvedLemmaId": "lex_mn_lemma_00101", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head human noun"}
    ],
    29: [  # махтай хоол
        {"token": "махтай", "rootLemma": "мах", "resolvedLemmaId": "lex_mn_lemma_00109", "inflectionalSuffixes": ["-тай"], "isUnresolved": False, "notes": "Comitative-attributive suffix"},
        {"token": "хоол", "rootLemma": "хоол", "resolvedLemmaId": "lex_mn_lemma_00085", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head food noun"}
    ],
    30: [  # замдаа сайн яваарай
        {"token": "замдаа", "rootLemma": "зам", "resolvedLemmaId": "lex_mn_lemma_00035", "inflectionalSuffixes": ["-д", "-аа"], "isUnresolved": False, "notes": "Dative-locative case + reflexive possessive suffix"},
        {"token": "сайн", "rootLemma": "сайн", "resolvedLemmaId": "lex_mn_lemma_00133", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Adverbial modifier 'well'"},
        {"token": "яваарай", "rootLemma": "явах", "resolvedLemmaId": "lex_mn_lemma_00111", "inflectionalSuffixes": ["-аарай"], "isUnresolved": False, "notes": "Polite imperative suffix on verb stem яв-"}
    ],
    31: [  # авч өгөх
        {"token": "авч", "rootLemma": "авах", "resolvedLemmaId": "lex_mn_lemma_00118", "inflectionalSuffixes": ["-ч"], "isUnresolved": False, "notes": "Imperfective converb suffix on stem ав-"},
        {"token": "өгөх", "rootLemma": "өгөх", "resolvedLemmaId": "lex_mn_lemma_00117", "inflectionalSuffixes": ["-х"], "isUnresolved": False, "notes": "Infinitive auxiliary benefactive verb"}
    ],
    32: [  # шинэ танил
        {"token": "шинэ", "rootLemma": "шинэ", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Adjective 'new'; non-pilot lemma"},
        {"token": "танил", "rootLemma": "танил", "resolvedLemmaId": "lex_mn_lemma_00119", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head social noun"}
    ],
    33: [  # үг хэлэх
        {"token": "үг", "rootLemma": "үг", "resolvedLemmaId": "lex_mn_lemma_00012", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun"},
        {"token": "хэлэх", "rootLemma": "хэлэх", "resolvedLemmaId": "lex_mn_lemma_00124", "inflectionalSuffixes": ["-эх"], "isUnresolved": False, "notes": "Infinitive vocal action verb"}
    ],
    34: [  # тод хэлэх
        {"token": "тод", "rootLemma": "тод", "resolvedLemmaId": "lex_mn_lemma_00128", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Adverbial manner modifier"},
        {"token": "хэлэх", "rootLemma": "хэлэх", "resolvedLemmaId": "lex_mn_lemma_00124", "inflectionalSuffixes": ["-эх"], "isUnresolved": False, "notes": "Infinitive verb"}
    ],
    35: [  # сайн ойлгох
        {"token": "сайн", "rootLemma": "сайн", "resolvedLemmaId": "lex_mn_lemma_00133", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Adverbial degree modifier"},
        {"token": "ойлгох", "rootLemma": "ойлгох", "resolvedLemmaId": "lex_mn_lemma_00131", "inflectionalSuffixes": ["-ох"], "isUnresolved": False, "notes": "Infinitive comprehension verb"}
    ],
    36: [  # сайн байна уу
        {"token": "сайн", "rootLemma": "сайн", "resolvedLemmaId": "lex_mn_lemma_00133", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Predicate evaluative adjective"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Present-imperfective finite suffix on stem бай-"},
        {"token": "уу", "rootLemma": "уу", "resolvedLemmaId": "lex_mn_lemma_00241", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polar interrogative particle"}
    ],
    37: [  # юу байна
        {"token": "юу", "rootLemma": "юу", "resolvedLemmaId": "lex_mn_lemma_00139", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Interrogative pronoun subject"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Present-imperfective finite suffix on stem бай-"}
    ],
    38: [  # өглөөний мэнд
        {"token": "өглөөний", "rootLemma": "өглөө", "resolvedLemmaId": "lex_mn_lemma_00141", "inflectionalSuffixes": ["-ний"], "isUnresolved": False, "notes": "Genitive temporal noun"},
        {"token": "мэнд", "rootLemma": "мэнд", "resolvedLemmaId": "lex_mn_lemma_00135", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head salutation noun"}
    ],
    39: [  # орохыг хориглоно
        {"token": "орохыг", "rootLemma": "орох", "resolvedLemmaId": None, "inflectionalSuffixes": ["-х", "-ыг"], "isUnresolved": True, "notes": "Future-participle nominalizer + accusative case; motion verb орох in non-pilot slot"},
        {"token": "хориглоно", "rootLemma": "хориглох", "resolvedLemmaId": None, "inflectionalSuffixes": ["-но"], "isUnresolved": True, "notes": "Transitive verb хориглох (to prohibit) with present modal -но; verb slot not in pilot"}
    ],
    40: [  # түргэн тусламж
        {"token": "түргэн", "rootLemma": "түргэн", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Adjective 'fast, urgent'; non-pilot lemma"},
        {"token": "тусламж", "rootLemma": "тусламж", "resolvedLemmaId": "lex_mn_lemma_00150", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head aid/assistance noun"}
    ],
    41: [  # түргэн дуудах
        {"token": "түргэн", "rootLemma": "түргэн", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Elliptical direct object for ambulance service"},
        {"token": "дуудах", "rootLemma": "дуудах", "resolvedLemmaId": "lex_mn_lemma_00071", "inflectionalSuffixes": ["-ах"], "isUnresolved": False, "notes": "Infinitive summon verb"}
    ],
    42: [  # монгол хэл сурах
        {"token": "монгол", "rootLemma": "монгол", "resolvedLemmaId": "lex_mn_lemma_00222", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Attributive ethnonym"},
        {"token": "хэл", "rootLemma": "хэл", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Language noun; non-pilot lemma slot"},
        {"token": "сурах", "rootLemma": "сурах", "resolvedLemmaId": "lex_mn_lemma_00155", "inflectionalSuffixes": ["-ах"], "isUnresolved": False, "notes": "Infinitive learning verb"}
    ],
    43: [  # үсэг таних
        {"token": "үсэг", "rootLemma": "үсэг", "resolvedLemmaId": "lex_mn_lemma_00001", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun"},
        {"token": "таних", "rootLemma": "таних", "resolvedLemmaId": None, "inflectionalSuffixes": ["-их"], "isUnresolved": True, "notes": "Verb 'to recognize/know'; non-pilot lemma"}
    ],
    44: [  # автобусны буудал
        {"token": "автобусны", "rootLemma": "автобус", "resolvedLemmaId": "lex_mn_lemma_00168", "inflectionalSuffixes": ["-ны"], "isUnresolved": False, "notes": "Genitive noun"},
        {"token": "буудал", "rootLemma": "буудал", "resolvedLemmaId": "lex_mn_lemma_00162", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head station/stop noun"}
    ],
    45: [  # төлбөр төлөх
        {"token": "төлбөр", "rootLemma": "төлбөр", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Deverbal noun 'payment'; non-pilot lemma"},
        {"token": "төлөх", "rootLemma": "төлөх", "resolvedLemmaId": None, "inflectionalSuffixes": ["-өх"], "isUnresolved": True, "notes": "Verb 'to pay'; non-pilot lemma"}
    ],
    46: [  # үнийн дүн
        {"token": "үнийн", "rootLemma": "үнэ", "resolvedLemmaId": "lex_mn_lemma_00165", "inflectionalSuffixes": ["-ийн"], "isUnresolved": False, "notes": "Genitive noun on stem үн-"},
        {"token": "дүн", "rootLemma": "дүн", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Accounting noun 'total/sum'; non-pilot lemma"}
    ],
    # Unit 16 to 20
    47: [  # үгийн дараалал
        {"token": "үгийн", "rootLemma": "үг", "resolvedLemmaId": "lex_mn_lemma_00012", "inflectionalSuffixes": ["-ийн"], "isUnresolved": False, "notes": "Genitive noun"},
        {"token": "дараалал", "rootLemma": "дараалал", "resolvedLemmaId": "lex_mn_lemma_00173", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head syntactic order noun"}
    ],
    48: [  # өгүүлбэр зохиох
        {"token": "өгүүлбэр", "rootLemma": "өгүүлбэр", "resolvedLemmaId": "lex_mn_lemma_00169", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object syntactic noun"},
        {"token": "зохиох", "rootLemma": "зохиох", "resolvedLemmaId": None, "inflectionalSuffixes": ["-ох"], "isUnresolved": True, "notes": "Verb 'to compose/construct'; non-pilot lemma"}
    ],
    49: [  # оройн мэнд хүргэе
        {"token": "оройн", "rootLemma": "орой", "resolvedLemmaId": "lex_mn_lemma_00142", "inflectionalSuffixes": ["-н"], "isUnresolved": False, "notes": "Genitive temporal noun"},
        {"token": "мэнд", "rootLemma": "мэнд", "resolvedLemmaId": "lex_mn_lemma_00135", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Salutation direct object noun"},
        {"token": "хүргэе", "rootLemma": "хүргэх", "resolvedLemmaId": "lex_mn_lemma_00177", "inflectionalSuffixes": ["-е"], "isUnresolved": False, "notes": "Optative-voluntative first person suffix"}
    ],
    50: [  # амар байна уу
        {"token": "амар", "rootLemma": "амар", "resolvedLemmaId": "lex_mn_lemma_00183", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Predicate stative noun/adjective"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Imperfective present verb"},
        {"token": "уу", "rootLemma": "уу", "resolvedLemmaId": "lex_mn_lemma_00241", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polar question particle"}
    ],
    51: [  # амар амгалан
        {"token": "амар", "rootLemma": "амар", "resolvedLemmaId": "lex_mn_lemma_00183", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "First element of hendiadys"},
        {"token": "амгалан", "rootLemma": "амгалан", "resolvedLemmaId": "lex_mn_lemma_00184", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Second element of hendiadys"}
    ],
    52: [  # уулзалт товлох
        {"token": "уулзалт", "rootLemma": "уулзалт", "resolvedLemmaId": "lex_mn_lemma_00189", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object noun"},
        {"token": "товлох", "rootLemma": "товлох", "resolvedLemmaId": None, "inflectionalSuffixes": ["-лох"], "isUnresolved": True, "notes": "Denominal verb of товч 'to schedule/abbreviate'; non-pilot lemma"}
    ],
    53: [  # би монгол хүн
        {"token": "би", "rootLemma": "би", "resolvedLemmaId": "lex_mn_lemma_00192", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Nominative personal subject pronoun"},
        {"token": "монгол", "rootLemma": "монгол", "resolvedLemmaId": "lex_mn_lemma_00222", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Attributive ethnonym"},
        {"token": "хүн", "rootLemma": "хүн", "resolvedLemmaId": "lex_mn_lemma_00101", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Predicate nominal head in zero-copula"}
    ],
    54: [  # ахмад хүнийг хүндэтгэх
        {"token": "ахмад", "rootLemma": "ахмад", "resolvedLemmaId": "lex_mn_lemma_00202", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Modifier adjective"},
        {"token": "хүнийг", "rootLemma": "хүн", "resolvedLemmaId": "lex_mn_lemma_00101", "inflectionalSuffixes": ["-ийг"], "isUnresolved": False, "notes": "Accusative definite case on stem хүн-"},
        {"token": "хүндэтгэх", "rootLemma": "хүндэтгэх", "resolvedLemmaId": "lex_mn_lemma_00178", "inflectionalSuffixes": ["-эх"], "isUnresolved": False, "notes": "Infinitive transitive verb"}
    ],
    55: [  # та гэж дуудах
        {"token": "та", "rootLemma": "та", "resolvedLemmaId": "lex_mn_lemma_00194", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polite direct address pronoun in direct quote"},
        {"token": "гэж", "rootLemma": "гэх", "resolvedLemmaId": None, "inflectionalSuffixes": ["-ж"], "isUnresolved": True, "notes": "Quotative converb of гэх; non-pilot lemma"},
        {"token": "дуудах", "rootLemma": "дуудах", "resolvedLemmaId": "lex_mn_lemma_00071", "inflectionalSuffixes": ["-ах"], "isUnresolved": False, "notes": "Infinitive appellation verb"}
    ],
    56: [  # та нар сайн байна уу
        {"token": "та", "rootLemma": "та", "resolvedLemmaId": "lex_mn_lemma_00194", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polite pronoun"},
        {"token": "нар", "rootLemma": "нар", "resolvedLemmaId": "lex_mn_lemma_00206", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Plural collective clitic"},
        {"token": "сайн", "rootLemma": "сайн", "resolvedLemmaId": "lex_mn_lemma_00133", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Predicate adjective"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Present auxiliary verb"},
        {"token": "уу", "rootLemma": "уу", "resolvedLemmaId": "lex_mn_lemma_00241", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polar interrogative particle"}
    ],
    57: [  # өөрийгөө танилцуулах
        {"token": "өөрийгөө", "rootLemma": "өөрөө", "resolvedLemmaId": "lex_mn_lemma_00198", "inflectionalSuffixes": ["-ийг", "-өө"], "isUnresolved": False, "notes": "Reflexive pronoun with accusative + reflexive possessive suffix"},
        {"token": "танилцуулах", "rootLemma": "танилцуулах", "resolvedLemmaId": None, "inflectionalSuffixes": ["-уулах"], "isUnresolved": True, "notes": "Causative infinitive verb 'to cause to be acquainted'; non-pilot verb slot"}
    ],
    58: [  # танилцсандаа баяртай байна
        {"token": "танилцсандаа", "rootLemma": "танилцах", "resolvedLemmaId": None, "inflectionalSuffixes": ["-сан", "-д", "-аа"], "isUnresolved": True, "notes": "Past verbal participle + dative + reflexive possessive"},
        {"token": "баяртай", "rootLemma": "баяр", "resolvedLemmaId": None, "inflectionalSuffixes": ["-тай"], "isUnresolved": True, "notes": "Noun 'joy' with comitative acting as predicate adjective"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Auxiliary copula verb"}
    ],
    59: [  # би оюутан
        {"token": "би", "rootLemma": "би", "resolvedLemmaId": "lex_mn_lemma_00192", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Nominative personal subject pronoun"},
        {"token": "оюутан", "rootLemma": "оюутан", "resolvedLemmaId": "lex_mn_lemma_00216", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Zero-copula nominal predicate"}
    ],
    60: [  # монгол улс
        {"token": "монгол", "rootLemma": "монгол", "resolvedLemmaId": "lex_mn_lemma_00222", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Attributive ethnonym"},
        {"token": "улс", "rootLemma": "улс", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Noun 'state/nation'; non-pilot lemma"}
    ],
    61: [  # гадаад орон
        {"token": "гадаад", "rootLemma": "гадаад", "resolvedLemmaId": "lex_mn_lemma_00228", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Attributive modifier adjective"},
        {"token": "орон", "rootLemma": "орон", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Noun 'country/land'; non-pilot lemma"}
    ],
    62: [  # хаанаас ирсэн бэ
        {"token": "хаанаас", "rootLemma": "хаанаас", "resolvedLemmaId": "lex_mn_lemma_00234", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Ablative locative interrogative pronoun"},
        {"token": "ирсэн", "rootLemma": "ирэх", "resolvedLemmaId": "lex_mn_lemma_00230", "inflectionalSuffixes": ["-сэн"], "isUnresolved": False, "notes": "Past verbal participle on stem ир-"},
        {"token": "бэ", "rootLemma": "бэ", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Content question interrogative particle after -н; non-pilot lemma"}
    ],
    63: [  # хурлын төлөөлөгч
        {"token": "хурлын", "rootLemma": "хурал", "resolvedLemmaId": "lex_mn_lemma_00238", "inflectionalSuffixes": ["-ын"], "isUnresolved": False, "notes": "Genitive noun on stem хурал-"},
        {"token": "төлөөлөгч", "rootLemma": "төлөөлөгч", "resolvedLemmaId": "lex_mn_lemma_00237", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head delegate noun"}
    ],
    64: [  # албан байгууллага
        {"token": "албан", "rootLemma": "алба", "resolvedLemmaId": None, "inflectionalSuffixes": ["-н"], "isUnresolved": True, "notes": "Attributive unstable -n form of алба (office/duty)"},
        {"token": "байгууллага", "rootLemma": "байгууллага", "resolvedLemmaId": "lex_mn_lemma_00239", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head institution noun"}
    ],
    65: [  # асуулт асуух
        {"token": "асуулт", "rootLemma": "асуулт", "resolvedLemmaId": "lex_mn_lemma_00243", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Cognate direct object noun"},
        {"token": "асуух", "rootLemma": "асуух", "resolvedLemmaId": "lex_mn_lemma_00244", "inflectionalSuffixes": ["-х"], "isUnresolved": False, "notes": "Infinitive verb"}
    ],
    66: [  # цай уух уу
        {"token": "цай", "rootLemma": "цай", "resolvedLemmaId": "lex_mn_lemma_00089", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Direct object beverage noun"},
        {"token": "уух", "rootLemma": "уух", "resolvedLemmaId": None, "inflectionalSuffixes": ["-х"], "isUnresolved": True, "notes": "Infinitive verb 'to drink'; non-pilot lemma"},
        {"token": "уу", "rootLemma": "уу", "resolvedLemmaId": "lex_mn_lemma_00241", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Polar interrogative particle"}
    ],
    67: [  # амттай байна
        {"token": "амттай", "rootLemma": "амттай", "resolvedLemmaId": "lex_mn_lemma_00250", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Evaluative predicate adjective"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Copula auxiliary verb"}
    ],
    68: [  # тийм ээ
        {"token": "тийм", "rootLemma": "тийм", "resolvedLemmaId": "lex_mn_lemma_00255", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Affirmative particle"},
        {"token": "ээ", "rootLemma": "ээ", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Emphatic conversational particle; non-pilot lemma"}
    ],
    69: [  # мөн байна
        {"token": "мөн", "rootLemma": "мөн", "resolvedLemmaId": "lex_mn_lemma_00257", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Equative confirmation particle"},
        {"token": "байна", "rootLemma": "байх", "resolvedLemmaId": "lex_mn_lemma_00134", "inflectionalSuffixes": ["-на"], "isUnresolved": False, "notes": "Auxiliary copula verb"}
    ],
    70: [  # тийм биш
        {"token": "тийм", "rootLemma": "тийм", "resolvedLemmaId": "lex_mn_lemma_00255", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Affirmative particle subject to negation"},
        {"token": "биш", "rootLemma": "биш", "resolvedLemmaId": "lex_mn_lemma_00258", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Nominal negative particle"}
    ],
    71: [  # энэ юу вэ
        {"token": "энэ", "rootLemma": "энэ", "resolvedLemmaId": "lex_mn_lemma_00264", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Proximal demonstrative subject pronoun"},
        {"token": "юу", "rootLemma": "юу", "resolvedLemmaId": "lex_mn_lemma_00139", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Interrogative predicate pronoun"},
        {"token": "вэ", "rootLemma": "вэ", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Content question particle after vowels/diphthongs; non-pilot lemma"}
    ],
    72: [  # эдгээр зүйлс
        {"token": "эдгээр", "rootLemma": "эдгээр", "resolvedLemmaId": "lex_mn_lemma_00271", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Proximal plural demonstrative pronoun"},
        {"token": "зүйлс", "rootLemma": "зүйл", "resolvedLemmaId": "lex_mn_lemma_00273", "inflectionalSuffixes": ["-с"], "isUnresolved": False, "notes": "Plural suffix -с on stem зүйл-"}
    ],
    73: [  # тэдгээр хүмүүс
        {"token": "тэдгээр", "rootLemma": "тэдгээр", "resolvedLemmaId": "lex_mn_lemma_00272", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Distal plural demonstrative pronoun"},
        {"token": "хүмүүс", "rootLemma": "хүн", "resolvedLemmaId": "lex_mn_lemma_00101", "inflectionalSuffixes": ["-үүс"], "isUnresolved": False, "notes": "Irregular plural suffix -үүс on stem хүн-"}
    ],
    74: [  # тэр хэн бэ
        {"token": "тэр", "rootLemma": "тэр", "resolvedLemmaId": "lex_mn_lemma_00195", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Distal demonstrative / 3rd person pronoun subject"},
        {"token": "хэн", "rootLemma": "хэн", "resolvedLemmaId": "lex_mn_lemma_00278", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Personal interrogative predicate pronoun"},
        {"token": "бэ", "rootLemma": "бэ", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Content question particle after -н; non-pilot lemma"}
    ],
    75: [  # ажлын өрөө
        {"token": "ажлын", "rootLemma": "ажил", "resolvedLemmaId": None, "inflectionalSuffixes": ["-ын"], "isUnresolved": True, "notes": "Genitive noun 'work'; non-pilot lemma"},
        {"token": "өрөө", "rootLemma": "өрөө", "resolvedLemmaId": "lex_mn_lemma_00285", "inflectionalSuffixes": [], "isUnresolved": False, "notes": "Head room noun"}
    ],
    76: [  # албан тасалгаа
        {"token": "албан", "rootLemma": "алба", "resolvedLemmaId": None, "inflectionalSuffixes": ["-н"], "isUnresolved": True, "notes": "Attributive unstable -n form of алба"},
        {"token": "тасалгаа", "rootLemma": "тасалгаа", "resolvedLemmaId": None, "inflectionalSuffixes": [], "isUnresolved": True, "notes": "Noun 'compartment/chamber'; non-pilot lemma"}
    ]
}
