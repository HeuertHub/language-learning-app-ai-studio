#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curated Rich Mongolian Lexicon Dictionary for Phase 3C.0
Organized by semantic themes and CEFR levels.
"""

from typing import List, Tuple, Dict, Any

# Structure: List of tuples (cyrillic, gloss, pos, domain, register, morphology)

LEXICAL_DOMAINS = {
    'phonology_literacy': [
        ('цагаан толгой', 'alphabet', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('үсэг', 'letter, alphabet character', 'noun', 'phonology', 'neutral', 'nominal'),
        ('эгшиг', 'vowel', 'noun', 'phonology', 'neutral', 'nominal'),
        ('гийгүүлэгч', 'consonant', 'noun', 'phonology', 'neutral', 'nominal'),
        ('авиа', 'speech sound, phoneme', 'noun', 'phonology', 'neutral', 'nominal'),
        ('үе', 'syllable, joint, era', 'noun', 'phonology', 'neutral', 'nominal'),
        ('үг', 'word, speech', 'noun', 'phonology', 'neutral', 'nominal'),
        ('богино эгшиг', 'short vowel', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('урт эгшиг', 'long vowel', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('хос эгшиг', 'diphthong', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('эр эгшиг', 'masculine / back vowel', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('эм эгшиг', 'feminine / front vowel', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('саармаг эгшиг', 'neutral vowel', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('эгшиг зохицох', 'vowel harmony', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('хатуугийн тэмдэг', 'hard sign (ъ)', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('зөөлний тэмдэг', 'soft sign (ь)', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('дараалал', 'order, sequence, alphabetical order', 'noun', 'phonology', 'neutral', 'deverbal_noun'),
        ('дуудах', 'to pronounce, to call', 'verb', 'phonology', 'neutral', 'verbal_infinitive'),
        ('бичих', 'to write', 'verb', 'phonology', 'neutral', 'verbal_infinitive'),
        ('унших', 'to read', 'verb', 'phonology', 'neutral', 'verbal_infinitive'),
        ('сонсох', 'to listen, hear', 'verb', 'phonology', 'neutral', 'verbal_infinitive'),
        ('ярих', 'to speak, converse', 'verb', 'phonology', 'neutral', 'verbal_infinitive'),
        ('өгүүлбэр', 'sentence', 'noun', 'phonology', 'neutral', 'nominal'),
        ('дүрэм', 'rule, grammar rule', 'noun', 'phonology', 'neutral', 'nominal'),
        ('зөв бичих дүрэм', 'orthography, spelling rule', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('толь бичиг', 'dictionary', 'noun', 'phonology', 'neutral', 'compound_noun'),
        ('дасгал', 'exercise, drill', 'noun', 'phonology', 'neutral', 'nominal'),
        ('жишээ', 'example', 'noun', 'phonology', 'neutral', 'nominal'),
        ('тайлбар', 'explanation, note', 'noun', 'phonology', 'neutral', 'nominal'),
        ('утга', 'meaning, sense, significance', 'noun', 'phonology', 'neutral', 'nominal'),
    ]
}

def get_lexical_domains():
    return LEXICAL_DOMAINS
