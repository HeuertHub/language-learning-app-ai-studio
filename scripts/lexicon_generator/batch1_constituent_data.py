#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1A Batch 1 Expression Constituent Analysis Data
Scope: Expressions 78 to 110 (indices 0 to 32 of Batch 1, global indices 77 to 109).

Maps each surface token to its canonical root lemma and resolved lemma slot ID
where that lemma has been realized in Pre-A1 or A1 (Units 16-25).
Explicitly marks isUnresolved: True for roots not yet introduced.
"""

BATCH1_CONSTITUENT_ANALYSIS = {
    # 0: биш ээ (lex_mn_expr_00078)
    0: [
        {"token": "биш", "rootLemma": "биш", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00258", "isUnresolved": False, "gloss": "not (nominal negation)"},
        {"token": "ээ", "rootLemma": "ээ", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "ээ", "gloss": "emphatic conversational particle"}
    ],
    # 1: үгүй ээ (lex_mn_expr_00079)
    1: [
        {"token": "үгүй", "rootLemma": "үгүй", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00256", "isUnresolved": False, "gloss": "no (negative answer particle)"},
        {"token": "ээ", "rootLemma": "ээ", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "ээ", "gloss": "emphatic conversational particle"}
    ],
    # 2: харин тийм (lex_mn_expr_00080)
    2: [
        {"token": "харин", "rootLemma": "харин", "pos": "conjunction", "resolvedLemmaId": "lex_mn_lemma_00294", "isUnresolved": False, "gloss": "but, on the contrary"},
        {"token": "тийм", "rootLemma": "тийм", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00255", "isUnresolved": False, "gloss": "yes, so, thus"}
    ],
    # 3: тийм биш үү (lex_mn_expr_00081)
    3: [
        {"token": "тийм", "rootLemma": "тийм", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00255", "isUnresolved": False, "gloss": "so, thus"},
        {"token": "биш", "rootLemma": "биш", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00258", "isUnresolved": False, "gloss": "not"},
        {"token": "үү", "rootLemma": "үү", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00242", "isUnresolved": False, "gloss": "polar question particle (front-vowel)"}
    ],
    # 4: минийх биш (lex_mn_expr_00082)
    4: [
        {"token": "минийх", "rootLemma": "би", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00192", "isUnresolved": False, "gloss": "mine (1st person pronoun possessive-attributive)"},
        {"token": "биш", "rootLemma": "биш", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00258", "isUnresolved": False, "gloss": "not"}
    ],
    # 5: гээсэн эд (lex_mn_expr_00083)
    5: [
        {"token": "гээсэн", "rootLemma": "гээх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00309", "isUnresolved": False, "gloss": "lost (perfect past participle)"},
        {"token": "эд", "rootLemma": "эд", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00275", "isUnresolved": False, "gloss": "item, property, article"}
    ],
    # 6: дараа уулзъя (lex_mn_expr_00084)
    6: [
        {"token": "дараа", "rootLemma": "дараа", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00311", "isUnresolved": False, "gloss": "later, afterward"},
        {"token": "уулзъя", "rootLemma": "уулзах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00136", "isUnresolved": False, "gloss": "to meet (volitive -ya)"}
    ],
    # 7: сайхан амраарай (lex_mn_expr_00085)
    7: [
        {"token": "сайхан", "rootLemma": "сайхан", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00313", "isUnresolved": False, "gloss": "fine, pleasant, good"},
        {"token": "амраарай", "rootLemma": "амрах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00312", "isUnresolved": False, "gloss": "to rest, sleep (prescriptive -aarai)"}
    ],
    # 8: маш их баярлалаа (lex_mn_expr_00086)
    8: [
        {"token": "маш", "rootLemma": "маш", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00319", "isUnresolved": False, "gloss": "very, extremely"},
        {"token": "их", "rootLemma": "их", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00318", "isUnresolved": False, "gloss": "much, great"},
        {"token": "баярлалаа", "rootLemma": "баярлах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00317", "isUnresolved": False, "gloss": "to be glad, thank (past confirmation -laa)"}
    ],
    # 9: сайн яваарай (lex_mn_expr_00087)
    9: [
        {"token": "сайн", "rootLemma": "сайн", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00133", "isUnresolved": False, "gloss": "well, good"},
        {"token": "яваарай", "rootLemma": "явах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00111", "isUnresolved": False, "gloss": "to go, travel (prescriptive -aarai)"}
    ],
    # 10: сайн сууж байгаарай (lex_mn_expr_00088)
    10: [
        {"token": "сайн", "rootLemma": "сайн", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00133", "isUnresolved": False, "gloss": "well, good"},
        {"token": "сууж", "rootLemma": "суух", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00186", "isUnresolved": False, "gloss": "to sit, stay, reside (converb -j)"},
        {"token": "байгаарай", "rootLemma": "байх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00134", "isUnresolved": False, "gloss": "to be (prescriptive -aarai auxiliary)"}
    ],
    # 11: түр баяртай (lex_mn_expr_00089)
    11: [
        {"token": "түр", "rootLemma": "түр", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00316", "isUnresolved": False, "gloss": "temporarily, briefly"},
        {"token": "баяртай", "rootLemma": "баяртай", "pos": "interjection", "resolvedLemmaId": "lex_mn_lemma_00310", "isUnresolved": False, "gloss": "goodbye, farewell"}
    ],
    # 12: тавтай морилно уу (lex_mn_expr_00090)
    12: [
        {"token": "тавтай", "rootLemma": "тавтай", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00332", "isUnresolved": False, "gloss": "comfortably, welcome"},
        {"token": "морилно", "rootLemma": "морилох", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00331", "isUnresolved": False, "gloss": "to proceed honorifically (indicative -n)"},
        {"token": "уу", "rootLemma": "уу", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00241", "isUnresolved": False, "gloss": "polite request enclitic"}
    ],
    # 13: дээшээ суу (lex_mn_expr_00091)
    13: [
        {"token": "дээшээ", "rootLemma": "дээшээ", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00333", "isUnresolved": False, "gloss": "upward, toward seat of honor"},
        {"token": "суу", "rootLemma": "суух", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00186", "isUnresolved": False, "gloss": "to sit (imperative)"}
    ],
    # 14: тавтай саатаарай (lex_mn_expr_00092)
    14: [
        {"token": "тавтай", "rootLemma": "тавтай", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00332", "isUnresolved": False, "gloss": "comfortably, pleasantly"},
        {"token": "саатаарай", "rootLemma": "саатах", "pos": "verb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "саатах", "gloss": "to linger, stay, visit (prescriptive -aarai)"}
    ],
    # 15: таны нэр хэн бэ (lex_mn_expr_00093)
    15: [
        {"token": "таны", "rootLemma": "та", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00194", "isUnresolved": False, "gloss": "your (polite genitive)"},
        {"token": "нэр", "rootLemma": "нэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00054", "isUnresolved": False, "gloss": "name"},
        {"token": "хэн", "rootLemma": "хэн", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00278", "isUnresolved": False, "gloss": "who"},
        {"token": "бэ", "rootLemma": "бэ", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "бэ", "gloss": "content question particle (consonant stem)"}
    ],
    # 16: аль нутаг вэ (lex_mn_expr_00094)
    16: [
        {"token": "аль", "rootLemma": "аль", "pos": "pronoun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "аль", "gloss": "which, what"},
        {"token": "нутаг", "rootLemma": "нутаг", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00233", "isUnresolved": False, "gloss": "homeland, country, birthplace"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "вэ", "gloss": "content question particle (vowel stem)"}
    ],
    # 17: хүндэт зочин (lex_mn_expr_00095)
    17: [
        {"token": "хүндэт", "rootLemma": "хүндэт", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00339", "isUnresolved": False, "gloss": "honored, respected"},
        {"token": "зочин", "rootLemma": "зочин", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00330", "isUnresolved": False, "gloss": "guest, visitor"}
    ],
    # 18: монголоор ярих (lex_mn_expr_00096)
    18: [
        {"token": "монголоор", "rootLemma": "монгол", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00222", "isUnresolved": False, "gloss": "in Mongolian (instrumental -aar)"},
        {"token": "ярих", "rootLemma": "ярих", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00351", "isUnresolved": False, "gloss": "to speak, talk"}
    ],
    # 19: сайн ойлгосонгүй (lex_mn_expr_00097)
    19: [
        {"token": "сайн", "rootLemma": "сайн", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00133", "isUnresolved": False, "gloss": "well, good"},
        {"token": "ойлгосонгүй", "rootLemma": "ойлгох", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00131", "isUnresolved": False, "gloss": "to understand (negative past -sangui)"},
        {"token": "гүй", "rootLemma": "гүй", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "гүй", "gloss": "negative past suffix/particle"}
    ],
    # 20: албан ёсны айлчлал (lex_mn_expr_00098)
    20: [
        {"token": "албан", "rootLemma": "алба", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00348", "isUnresolved": False, "gloss": "official, state duty"},
        {"token": "ёсны", "rootLemma": "ёс", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00113", "isUnresolved": False, "gloss": "custom, rule, law (genitive -ny)"},
        {"token": "айлчлал", "rootLemma": "айлчлал", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "айлчлал", "gloss": "visit, call, diplomatic mission"}
    ],
    # 21: гэрт байна (lex_mn_expr_00099)
    21: [
        {"token": "гэрт", "rootLemma": "гэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00030", "isUnresolved": False, "gloss": "at home, in the ger (dative-locative -t)"},
        {"token": "байна", "rootLemma": "байх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00134", "isUnresolved": False, "gloss": "is, exists (imperfective present)"}
    ],
    # 22: бэлэн байна (lex_mn_expr_00100)
    22: [
        {"token": "бэлэн", "rootLemma": "бэлэн", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00372", "isUnresolved": False, "gloss": "ready, prepared, available"},
        {"token": "байна", "rootLemma": "байх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00134", "isUnresolved": False, "gloss": "is, exists"}
    ],
    # 23: энд алга (lex_mn_expr_00101)
    23: [
        {"token": "энд", "rootLemma": "энд", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00266", "isUnresolved": False, "gloss": "here, in this place"},
        {"token": "алга", "rootLemma": "алга", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00366", "isUnresolved": False, "gloss": "absent, missing, none"}
    ],
    # 24: байгаа юу (lex_mn_expr_00102)
    24: [
        {"token": "байгаа", "rootLemma": "байх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00134", "isUnresolved": False, "gloss": "to be, exist (imperfective participle -aa)"},
        {"token": "юу", "rootLemma": "юу", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00139", "isUnresolved": False, "gloss": "interrogative availability particle"}
    ],
    # 25: сул өрөө (lex_mn_expr_00103)
    25: [
        {"token": "сул", "rootLemma": "сул", "pos": "adjective", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "сул", "gloss": "vacant, free, empty"},
        {"token": "өрөө", "rootLemma": "өрөө", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00285", "isUnresolved": False, "gloss": "room"}
    ],
    # 26: монгол гэр (lex_mn_expr_00104)
    26: [
        {"token": "монгол", "rootLemma": "монгол", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00222", "isUnresolved": False, "gloss": "Mongol, Mongolian"},
        {"token": "гэр", "rootLemma": "гэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00030", "isUnresolved": False, "gloss": "ger, yurt, traditional home"}
    ],
    # 27: ширээн дээр (lex_mn_expr_00105)
    27: [
        {"token": "ширээн", "rootLemma": "ширээ", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00283", "isUnresolved": False, "gloss": "table, desk (unstable -n stem)"},
        {"token": "дээр", "rootLemma": "дээр", "pos": "postposition", "resolvedLemmaId": "lex_mn_lemma_00381", "isUnresolved": False, "gloss": "on, upon, on top of"}
    ],
    # 28: гэрийн гадна (lex_mn_expr_00106)
    28: [
        {"token": "гэрийн", "rootLemma": "гэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00030", "isUnresolved": False, "gloss": "of the ger/house (genitive -iin)"},
        {"token": "гадна", "rootLemma": "гадна", "pos": "postposition", "resolvedLemmaId": "lex_mn_lemma_00384", "isUnresolved": False, "gloss": "outside, exterior to"}
    ],
    # 29: хотын төв (lex_mn_expr_00107)
    29: [
        {"token": "хотын", "rootLemma": "хот", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00231", "isUnresolved": False, "gloss": "of the city (genitive -yn)"},
        {"token": "төв", "rootLemma": "төв", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00391", "isUnresolved": False, "gloss": "center, downtown hub"}
    ],
    # 30: нэгдүгээр давхар (lex_mn_expr_00108)
    30: [
        {"token": "нэгдүгээр", "rootLemma": "нэг", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00057", "isUnresolved": False, "gloss": "first (ordinal numeral)"},
        {"token": "давхар", "rootLemma": "давхар", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00395", "isUnresolved": False, "gloss": "floor, storey"}
    ],
    # 31: аваарын гарц (lex_mn_expr_00109)
    31: [
        {"token": "аваарын", "rootLemma": "аваар", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "аваар", "gloss": "accident, emergency (genitive -yn)"},
        {"token": "гарц", "rootLemma": "гарц", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00148", "isUnresolved": False, "gloss": "exit, gateway"}
    ],
    # 32: хаана байна вэ (lex_mn_expr_00110)
    32: [
        {"token": "хаана", "rootLemma": "хаана", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00400", "isUnresolved": False, "gloss": "where, in what place"},
        {"token": "байна", "rootLemma": "байх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00134", "isUnresolved": False, "gloss": "is, exists"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "вэ", "gloss": "content interrogative particle"}
    ]
}
