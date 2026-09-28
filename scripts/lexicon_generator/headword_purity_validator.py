#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1B-R1: Lemma Headword Purity Validator & Morphological Duplication Gate.

Validates that every realized lemma slot contains a genuine, distinct lexical headword,
and NOT:
- an inflectional/case form of an already realized lemma
- a converbial form of an already realized verb
- a participial form of an already realized verb
- an attributive / unstable-n stem allomorph of an already realized numeral/noun
- a derived surface variant already represented by another realized core lemma

Enforces:
1. Metadata-based relationship detection (usageNotes, gloss, morphology inspection)
2. Explicit mapping of known irregular, converbial, case, and stem-allomorph pairs
3. Exhaustive morphological-duplication table for all 112 Batch 2 lemmas
"""

import os
import sys
import re
import json

# Known irregular/inflectional/allomorphic pairs to guard against:
# Surface form -> (underlying_lexeme, relationship_type)
KNOWN_INFLECTIONAL_VARIANTS = {
    # Pronoun / Interrogative case forms
    "хэний": ("хэн", "GENITIVE_CASE"),
    "хэнийг": ("хэн", "ACCUSATIVE_CASE"),
    "хэнд": ("хэн", "DATIVE_LOCATIVE_CASE"),
    "хэнээс": ("хэн", "ABLATIVE_CASE"),
    "хэнээр": ("хэн", "INSTRUMENTAL_CASE"),
    "хэнтэй": ("хэн", "COMITATIVE_CASE"),
    "юуны": ("юу", "GENITIVE_CASE"),
    "юуг": ("юу", "ACCUSATIVE_CASE"),
    "юунд": ("юу", "DATIVE_LOCATIVE_CASE"),
    "юунаас": ("юу", "ABLATIVE_CASE"),
    "юугаар": ("юу", "INSTRUMENTAL_CASE"),
    "юутай": ("юу", "COMITATIVE_CASE"),
    "хэдийд": ("хэдий", "LOCATIVE_TIME_CASE"),
    "хэдийг": ("хэдий", "ACCUSATIVE_CASE"),
    "хэдээр": ("хэд", "INSTRUMENTAL_CASE"),
    "хэдэд": ("хэд", "DATIVE_LOCATIVE_CASE"),
    "хэдээс": ("хэд", "ABLATIVE_CASE"),

    # Numeral stem/allomorphic variants (-н stem forms)
    "нэгэн": ("нэг", "NUMERAL_N_STEM"),
    "хоёрхон": ("хоёр", "DIMINUTIVE_FORM"),
    "гурван": ("гурав", "NUMERAL_N_STEM"),
    "дөрвөн": ("дөрөв", "NUMERAL_N_STEM"),
    "таван": ("тав", "NUMERAL_N_STEM"),
    "зургаан": ("зургаа", "NUMERAL_N_STEM"),
    "долоон": ("долоо", "NUMERAL_N_STEM"),
    "найман": ("найм", "NUMERAL_N_STEM"),
    "есөн": ("ес", "NUMERAL_N_STEM"),
    "арван": ("арав", "NUMERAL_N_STEM"),
    "хорин": ("хорь", "NUMERAL_N_STEM"),
    "гучин": ("гуч", "NUMERAL_N_STEM"),
    "дөчин": ("дөч", "NUMERAL_N_STEM"),
    "тавин": ("тавь", "NUMERAL_N_STEM"),
    "жаран": ("жар", "NUMERAL_N_STEM"),
    "далан": ("дал", "NUMERAL_N_STEM"),
    "наян": ("ная", "NUMERAL_N_STEM"),
    "ерэн": ("ер", "NUMERAL_N_STEM"),
    "зуун": ("зуу", "NUMERAL_N_STEM"),
    "хэдэн": ("хэд", "NUMERAL_N_STEM"),

    # Converbial / Participial forms
    "лавлан": ("лавлах", "MODAL_CONVERB_N"),
    "байгаа": ("байх", "IMPERFECTIVE_PARTICIPLE_AA"),
    "байсны": ("байх", "PAST_PARTICIPLE_GENITIVE"),
    "байдгийн": ("байх", "HABITUAL_PARTICIPLE_GENITIVE"),
    "гэвэл": ("гэх", "CONDITIONAL_CONVERB_VAL"),
    "гэж": ("гэх", "IMPERFECT_CONVERB_J"),
    "болж": ("болох", "IMPERFECT_CONVERB_J"),
    "болбол": ("болох", "CONDITIONAL_CONVERB_BAL"),
    "ирж": ("ирэх", "IMPERFECT_CONVERB_J"),
    "ирээд": ("ирэх", "SUCCESSIVE_CONVERB_AAD"),
    "явж": ("явах", "IMPERFECT_CONVERB_J"),
    "яваад": ("явах", "SUCCESSIVE_CONVERB_AAD"),
    "яриад": ("ярих", "SUCCESSIVE_CONVERB_AAD"),
    "сурч": ("сурах", "IMPERFECT_CONVERB_CH"),
    "уншиж": ("унших", "IMPERFECT_CONVERB_J"),
    "бичиж": ("бичих", "IMPERFECT_CONVERB_J"),
}

METADATA_SUSPECT_PATTERNS = [
    re.compile(r'\bgenitive\s+(?:possessive\s+)?form\s+of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\binstrumental\s+(?:form\s+)?(?:of|based\s+on)\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\battributive\s+(?:stem\s+)?form\s+of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\bstem\s+form\s+of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\bconverb(?:ial)?\s+(?:form\s+)?of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\bparticiple\s+(?:form\s+)?of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\blocative\s+(?:interrogative\s+)?form\s+of\s+([^\s,.;]+)', re.IGNORECASE),
    re.compile(r'\bplural\s+(?:form\s+)?of\s+([^\s,.;]+)', re.IGNORECASE),
]

def audit_batch2_headwords(root_dir=None):
    if root_dir is None:
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    lemmas_bundle_path = os.path.join(root_dir, 'public', 'data', 'lexicon', 'lemmas_bundle.json')
    with open(lemmas_bundle_path, 'r', encoding='utf-8') as f:
        all_lemmas = json.load(f)

    # Realized lemma dictionary by lemma string: lemma -> id
    realized_lemmas_by_text = {}
    for l in all_lemmas:
        if l['status'] != 'UNREALIZED' and l.get('lemma'):
            realized_lemmas_by_text[l['lemma']] = l['id']

    # Batch 2 lemmas: indices 403 to 514 (IDs lex_mn_lemma_00404 to lex_mn_lemma_00515)
    b2_lemmas = all_lemmas[403:515]
    assert len(b2_lemmas) == 112, f"Expected 112 Batch 2 lemmas, got {len(b2_lemmas)}"

    audit_table = []
    failures = []

    for l in b2_lemmas:
        lid = l['id']
        surface = l.get('lemma', '')
        pos = l.get('pos', '')
        notes = l.get('usageNotes', '') or ''
        gloss = l.get('gloss', '') or ''

        # 1. Check known irregular/allomorphic mapping
        if surface in KNOWN_INFLECTIONAL_VARIANTS:
            base_form, rel_type = KNOWN_INFLECTIONAL_VARIANTS[surface]
            base_exists = base_form in realized_lemmas_by_text
            base_id = realized_lemmas_by_text.get(base_form, "N/A")
            
            decision = "MORPHOLOGICAL_FORM_NOT_LEMMA" if base_exists else "NEEDS_MANUAL_REVIEW"
            row = {
                "id": lid,
                "surface": surface,
                "underlying_lexeme": base_form,
                "relationship_type": rel_type,
                "base_exists": base_exists,
                "base_id": base_id,
                "decision": decision,
                "notes": notes
            }
            audit_table.append(row)
            failures.append(row)
            continue

        # 2. Check metadata patterns in notes and gloss
        metadata_flag = None
        for pat in METADATA_SUSPECT_PATTERNS:
            m = pat.search(notes) or pat.search(gloss)
            if m:
                base_candidate = m.group(1).strip()
                if base_candidate in realized_lemmas_by_text:
                    metadata_flag = (base_candidate, f"METADATA_DECLARED_FORM_OF_{base_candidate.upper()}")
                    break

        if metadata_flag:
            base_form, rel_type = metadata_flag
            base_id = realized_lemmas_by_text.get(base_form, "N/A")
            decision = "MORPHOLOGICAL_FORM_NOT_LEMMA"
            row = {
                "id": lid,
                "surface": surface,
                "underlying_lexeme": base_form,
                "relationship_type": rel_type,
                "base_exists": True,
                "base_id": base_id,
                "decision": decision,
                "notes": notes
            }
            audit_table.append(row)
            failures.append(row)
            continue

        # 3. Valid distinct lemma
        row = {
            "id": lid,
            "surface": surface,
            "underlying_lexeme": surface,
            "relationship_type": "PRIMARY_LEXICAL_HEADWORD",
            "base_exists": True,
            "base_id": lid,
            "decision": "VALID_DISTINCT_LEMMA",
            "notes": notes
        }
        audit_table.append(row)

    return audit_table, failures

def print_audit_report(audit_table, failures):
    print("=" * 110)
    print("PHASE 3C.1B-R1: BATCH 2 MORPHOLOGICAL-DUPLICATION & HEADWORD-PURITY AUDIT (112 LEMMAS)")
    print("=" * 110)
    print(f"{'Lexical ID':18s} | {'Surface':12s} | {'Underlying Lexeme':18s} | {'Rel Type':26s} | {'Base ID':18s} | {'Decision':24s}")
    print("-" * 110)
    for r in audit_table:
        print(f"{r['id']:18s} | {r['surface']:12s} | {r['underlying_lexeme']:18s} | {r['relationship_type']:26s} | {r['base_id']:18s} | {r['decision']:24s}")

    print("=" * 110)
    print(f"Audit Summary:")
    print(f"  • Total Lemmas Audited:                  {len(audit_table):3d} / 112")
    valid_count = sum(1 for r in audit_table if r['decision'] == 'VALID_DISTINCT_LEMMA')
    print(f"  • Valid Distinct Lexical Headwords:      {valid_count:3d} / 112 ({(valid_count/112)*100:.1f}%)")
    print(f"  • Morphological Form Violations:         {len(failures):3d} (Target: 0)")
    print("=" * 110)

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    table, fails = audit_batch2_headwords(root)
    print_audit_report(table, fails)
    if fails:
        print(f"\n❌ FAILED: Found {len(fails)} morphological-duplication / headword-purity failures in Batch 2!")
        sys.exit(1)
    else:
        print("\n✓ SUCCESS: All 112 Batch 2 lemmas certified as genuine, distinct lexical headwords!")
        sys.exit(0)
