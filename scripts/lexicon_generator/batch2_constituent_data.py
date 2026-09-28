#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1B Batch 2 Expression Constituent Analysis Data
Scope: Expressions 111 to 140 (indices 0 to 29 of Batch 2, global indices 110 to 139).

Maps each surface token to its canonical root lemma and resolved lemma slot ID
where that lemma has been realized in Pre-A1 or A1 (Units 16-30).
Explicitly marks isUnresolved: True for roots not yet introduced.
"""

BATCH2_CONSTITUENT_ANALYSIS = {
    # 0: хэзээ ирэх вэ (lex_mn_expr_00111)
    0: [
        {"token": "хэзээ", "rootLemma": "хэзээ", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00406", "isUnresolved": False, "gloss": "when"},
        {"token": "ирэх", "rootLemma": "ирэх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00230", "isUnresolved": False, "gloss": "to come"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00405", "isUnresolved": False, "gloss": "question particle"}
    ],
    # 1: яагаад гэвэл (lex_mn_expr_00112)
    1: [
        {"token": "яагаад", "rootLemma": "яагаад", "pos": "adverb", "resolvedLemmaId": "lex_mn_lemma_00408", "isUnresolved": False, "gloss": "why"},
        {"token": "гэвэл", "rootLemma": "гэх", "pos": "verb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "гэх", "gloss": "to say (conditional converb)"}
    ],
    # 2: ямар учиртай вэ (lex_mn_expr_00113)
    2: [
        {"token": "ямар", "rootLemma": "ямар", "pos": "pronoun", "resolvedLemmaId": "lex_mn_lemma_00412", "isUnresolved": False, "gloss": "what kind of"},
        {"token": "учиртай", "rootLemma": "учир", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "учир", "gloss": "reason, cause"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00405", "isUnresolved": False, "gloss": "question particle"}
    ],
    # 3: дахин хэлнэ үү (lex_mn_expr_00114)
    3: [
        {"token": "дахин", "rootLemma": "дахин", "pos": "adverb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "дахин", "gloss": "again"},
        {"token": "хэлнэ", "rootLemma": "хэлэх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00124", "isUnresolved": False, "gloss": "to say"},
        {"token": "үү", "rootLemma": "үү", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00242", "isUnresolved": False, "gloss": "polar question particle"}
    ],
    # 4: асуулт тавих (lex_mn_expr_00115)
    4: [
        {"token": "асуулт", "rootLemma": "асуулт", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00243", "isUnresolved": False, "gloss": "question"},
        {"token": "тавих", "rootLemma": "тавих", "pos": "verb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "тавих", "gloss": "to put, raise"}
    ],
    # 5: асуултад хариулах (lex_mn_expr_00116)
    5: [
        {"token": "асуултад", "rootLemma": "асуулт", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00243", "isUnresolved": False, "gloss": "question (dative)"},
        {"token": "хариулах", "rootLemma": "хариулах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00247", "isUnresolved": False, "gloss": "to answer"}
    ],
    # 6: арван хоёр (lex_mn_expr_00117)
    6: [
        {"token": "арван", "rootLemma": "арав", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00065", "isUnresolved": False, "gloss": "ten"},
        {"token": "хоёр", "rootLemma": "хоёр", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00058", "isUnresolved": False, "gloss": "two"}
    ],
    # 7: тоо тоолох (lex_mn_expr_00118)
    7: [
        {"token": "тоо", "rootLemma": "тоо", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00060", "isUnresolved": False, "gloss": "number"},
        {"token": "тоолох", "rootLemma": "тоолох", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00429", "isUnresolved": False, "gloss": "to count"}
    ],
    # 8: хорин тав (lex_mn_expr_00119)
    8: [
        {"token": "хорин", "rootLemma": "хорь", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00427", "isUnresolved": False, "gloss": "twenty"},
        {"token": "тав", "rootLemma": "тав", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00062", "isUnresolved": False, "gloss": "five"}
    ],
    # 9: хэдэн настай вэ (lex_mn_expr_00120)
    9: [
        {"token": "хэдэн", "rootLemma": "хэд", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00441", "isUnresolved": False, "gloss": "how many"},
        {"token": "настай", "rootLemma": "нас", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00076", "isUnresolved": False, "gloss": "age"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00405", "isUnresolved": False, "gloss": "question particle"}
    ],
    # 10: хэдэн төгрөг вэ (lex_mn_expr_00121)
    10: [
        {"token": "хэдэн", "rootLemma": "хэд", "pos": "numeral", "resolvedLemmaId": "lex_mn_lemma_00441", "isUnresolved": False, "gloss": "how many"},
        {"token": "төгрөг", "rootLemma": "төгрөг", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00166", "isUnresolved": False, "gloss": "tugrik"},
        {"token": "вэ", "rootLemma": "вэ", "pos": "particle", "resolvedLemmaId": "lex_mn_lemma_00405", "isUnresolved": False, "gloss": "question particle"}
    ],
    # 11: нийт дүн (lex_mn_expr_00122)
    11: [
        {"token": "нийт", "rootLemma": "нийт", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00446", "isUnresolved": False, "gloss": "total"},
        {"token": "дүн", "rootLemma": "дүн", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00432", "isUnresolved": False, "gloss": "amount, sum"}
    ],
    # 12: утасны дугаар (lex_mn_expr_00123)
    12: [
        {"token": "утасны", "rootLemma": "утас", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00153", "isUnresolved": False, "gloss": "telephone (genitive)"},
        {"token": "дугаар", "rootLemma": "дугаар", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00450", "isUnresolved": False, "gloss": "number"}
    ],
    # 13: утсаар ярих (lex_mn_expr_00124)
    13: [
        {"token": "утсаар", "rootLemma": "утас", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00153", "isUnresolved": False, "gloss": "telephone (instrumental)"},
        {"token": "ярих", "rootLemma": "ярих", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00351", "isUnresolved": False, "gloss": "to speak"}
    ],
    # 14: цахим шуудан (lex_mn_expr_00125)
    14: [
        {"token": "цахим", "rootLemma": "цахим", "pos": "adjective", "resolvedLemmaId": "lex_mn_lemma_00457", "isUnresolved": False, "gloss": "digital, electronic"},
        {"token": "шуудан", "rootLemma": "шуудан", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00164", "isUnresolved": False, "gloss": "post, mail"}
    ],
    # 15: нэрийн хуудас (lex_mn_expr_00126)
    15: [
        {"token": "нэрийн", "rootLemma": "нэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00054", "isUnresolved": False, "gloss": "name (genitive)"},
        {"token": "хуудас", "rootLemma": "хуудас", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00329", "isUnresolved": False, "gloss": "sheet, card"}
    ],
    # 16: албан тушаал (lex_mn_expr_00127)
    16: [
        {"token": "албан", "rootLemma": "алба", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00348", "isUnresolved": False, "gloss": "office, duty (attributive)"},
        {"token": "тушаал", "rootLemma": "тушаал", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00464", "isUnresolved": False, "gloss": "rank, position"}
    ],
    # 17: холбоо барих (lex_mn_expr_00128)
    17: [
        {"token": "холбоо", "rootLemma": "холбоо", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00469", "isUnresolved": False, "gloss": "connection, contact"},
        {"token": "барих", "rootLemma": "барих", "pos": "verb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "барих", "gloss": "to hold, maintain"}
    ],
    # 18: олон ном (lex_mn_expr_00129)
    18: [
        {"token": "олон", "rootLemma": "олон", "pos": "adjective", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "олон", "gloss": "many"},
        {"token": "ном", "rootLemma": "ном", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00005", "isUnresolved": False, "gloss": "book"}
    ],
    # 19: гэрийн эдлэл (lex_mn_expr_00130)
    19: [
        {"token": "гэрийн", "rootLemma": "гэр", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00030", "isUnresolved": False, "gloss": "home, ger (genitive)"},
        {"token": "эдлэл", "rootLemma": "эдлэл", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00473", "isUnresolved": False, "gloss": "goods, article"}
    ],
    # 20: ажлын хамт олон (lex_mn_expr_00131)
    20: [
        {"token": "ажлын", "rootLemma": "ажил", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "ажил", "gloss": "work (genitive)"},
        {"token": "хамт", "rootLemma": "хамт", "pos": "adverb", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "хамт", "gloss": "together"},
        {"token": "олон", "rootLemma": "олон", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "олон", "gloss": "collective, multitude"}
    ],
    # 21: тавиур дээр (lex_mn_expr_00132)
    21: [
        {"token": "тавиур", "rootLemma": "тавиур", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00486", "isUnresolved": False, "gloss": "shelf"},
        {"token": "дээр", "rootLemma": "дээр", "pos": "postposition", "resolvedLemmaId": "lex_mn_lemma_00381", "isUnresolved": False, "gloss": "on"}
    ],
    # 22: хайрцаг дотор (lex_mn_expr_00133)
    22: [
        {"token": "хайрцаг", "rootLemma": "хайрцаг", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00487", "isUnresolved": False, "gloss": "box"},
        {"token": "дотор", "rootLemma": "дотор", "pos": "postposition", "resolvedLemmaId": "lex_mn_lemma_00383", "isUnresolved": False, "gloss": "inside"}
    ],
    # 23: номын сан (lex_mn_expr_00134)
    23: [
        {"token": "номын", "rootLemma": "ном", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00005", "isUnresolved": False, "gloss": "book (genitive)"},
        {"token": "сан", "rootLemma": "сан", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00491", "isUnresolved": False, "gloss": "treasury, library collection"}
    ],
    # 24: ном унших (lex_mn_expr_00135)
    24: [
        {"token": "ном", "rootLemma": "ном", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00005", "isUnresolved": False, "gloss": "book"},
        {"token": "унших", "rootLemma": "унших", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00047", "isUnresolved": False, "gloss": "to read"}
    ],
    # 25: захидал бичих (lex_mn_expr_00136)
    25: [
        {"token": "захидал", "rootLemma": "захидал", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00324", "isUnresolved": False, "gloss": "letter"},
        {"token": "бичих", "rootLemma": "бичих", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00046", "isUnresolved": False, "gloss": "to write"}
    ],
    # 26: бичиг баримт (lex_mn_expr_00137)
    26: [
        {"token": "бичиг", "rootLemma": "бичиг", "pos": "noun", "resolvedLemmaId": None, "isUnresolved": True, "unresolvedRoot": "бичиг", "gloss": "writing, document"},
        {"token": "баримт", "rootLemma": "баримт", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00167", "isUnresolved": False, "gloss": "document, proof"}
    ],
    # 27: худалдаж авах (lex_mn_expr_00138)
    27: [
        {"token": "худалдаж", "rootLemma": "худалдах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00507", "isUnresolved": False, "gloss": "to sell (converb)"},
        {"token": "авах", "rootLemma": "авах", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00118", "isUnresolved": False, "gloss": "to take, buy"}
    ],
    # 28: мөнгө төлөх (lex_mn_expr_00139)
    28: [
        {"token": "мөнгө", "rootLemma": "мөнгө", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00442", "isUnresolved": False, "gloss": "money"},
        {"token": "төлөх", "rootLemma": "төлөх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00508", "isUnresolved": False, "gloss": "to pay"}
    ],
    # 29: захиалга өгөх (lex_mn_expr_00140)
    29: [
        {"token": "захиалга", "rootLemma": "захиалга", "pos": "noun", "resolvedLemmaId": "lex_mn_lemma_00513", "isUnresolved": False, "gloss": "order"},
        {"token": "өгөх", "rootLemma": "өгөх", "pos": "verb", "resolvedLemmaId": "lex_mn_lemma_00117", "isUnresolved": False, "gloss": "to give"}
    ],
}
