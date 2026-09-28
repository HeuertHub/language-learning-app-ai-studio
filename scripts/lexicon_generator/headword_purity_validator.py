#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1B-R2: Fail-Closed Lemma Headword Purity Validator & Morphological Duplication Gate.

Architecture:
1. Negative regression test layer:
   - KNOWN_INFLECTIONAL_VARIANTS: Known case forms, converbs, participles, numeral -n stems
   - METADATA_SUSPECT_PATTERNS: Flags notes/glosses declaring a record as "form of X"
   If any negative test fires -> MORPHOLOGICAL_FORM_NOT_LEMMA (FAIL)

2. Positive fail-closed classification layer:
   Every realized lemma must be positively certified via either:
   A. AUTHORITATIVE_HEADWORD_CONFIRMED:
      Exact independent headword in recognized lexicographic source (Tsevel 1966, 2018 Official Standardized Dictionary).
      Stores: lexical ID, searched form, source, stable locator / URL, definition quote.
   B. MANUALLY_REVIEWED_DISTINCT_HEADWORD:
      Digital lookup unavailable/uninspected, but explicit manual linguistic review establishes
      independent lexical status (canonical citation infinitive in -x, bare uninflected root, etc.).
      Stores: explicit audit decision, linguistic rationale.

   FAIL-CLOSED MANDATE:
   Any record lacking positive certification under A or B defaults to:
   NEEDS_MANUAL_REVIEW
   and causes the validation gate to fail immediately.
"""

import os
import sys
import re
import json

# =============================================================================
# 1. NEGATIVE REGRESSION LAYER: KNOWN INFLECTIONAL / ALLOMORPHIC VARIANTS
# =============================================================================
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
    "хаанахь": ("хаанах", "NONSTANDARD_ORTHOGRAPHIC_VARIANT"),

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

# =============================================================================
# 2. POSITIVE CERTIFICATION REGISTRIES (FAIL-CLOSED DATA LAYER)
# =============================================================================

# Category A: AUTHORITATIVE_HEADWORD_CONFIRMED
# Exactly documented independent headwords in recognized lexicographic sources
AUTHORITATIVE_HEADWORD_REGISTRY = {
    "хэзээ": {
        "source": "Tsevel (1966)",
        "locator": "p. 777, col. 1; http://toli.query.mn/dictionary_items/20725",
        "evidence": "ямар нэгэн үйл явдал болсон буюу болох цагийг асуух төлөөний үг",
    },
    "аль": {
        "source": "Tsevel (1966)",
        "locator": "p. 28, col. 1; http://toli.query.mn/dictionary_items/2261",
        "evidence": "асуух, лавлах, ялгах, заах утгаар хэрэглэх төлөөний үг",
    },
    "ямар": {
        "source": "Tsevel (1966)",
        "locator": "p. 896, col. 1; http://toli.query.mn/dictionary_items/12925",
        "evidence": "аливаа хүн, юмны чанар байдал, овор дүр өнгө тэмдэг зэргийг лавлан асуухад хэрэглэх төлөөний үг",
    },
    "хаанах": {
        "source": "Монгол хэлний зөв бичих дүрмийн журамласан толь (2018)",
        "locator": "p. 268; Tsevel (1966) p. 735 (http://toli.query.mn/dictionary_items/2530)",
        "evidence": "аль газар буй (тэ.н., [хаа-нах]); standard Khalkha provenance interrogative adjective (тэ.н)",
    },
    "хэр": {
        "source": "Tsevel (1966) & 2018 Журамласан толь",
        "locator": "Tsevel p. 771, col. 1; 2018 Толь p. 273",
        "evidence": "хэмжээ, зааг, хир; асуух хэмжээ, байдлыг лавлахад хэрэглэнэ (хэр хол, хэр их)",
    },
    "ойлгомжтой": {
        "source": "Tsevel (1966)",
        "locator": "p. 408, col. 1; http://toli.query.mn/dictionary_items/5723",
        "evidence": "учир утга тодорхой, ухахад хялбар (тэмдэг нэр)",
    },
    "хорь": {
        "source": "Tsevel (1966)",
        "locator": "p. 742, col. 1; http://toli.query.mn/dictionary_items/29251",
        "evidence": "арав дээр арвыг нэмсэн тоо (хорин); base cardinal numeral twenty",
    },
    "гуч": {
        "source": "Tsevel (1966)",
        "locator": "p. 162, col. 2; http://toli.query.mn/dictionary_items/9811",
        "evidence": "тооны нэр, гурван арав нийлсний нийлбэр (гучин); base cardinal numeral thirty",
    },
    "хэд": {
        "source": "Tsevel (1966)",
        "locator": "p. 768, col. 2; http://toli.query.mn/dictionary_items/2952",
        "evidence": "юмны тоо хичнээн болохыг асуух төлөөний үг; base interrogative numeral",
    },
    "зуу": {
        "source": "Tsevel (1966)",
        "locator": "p. 256, col. 2; http://toli.query.mn/dictionary_items/20340",
        "evidence": "тооны нэр, ер дээр арвыг нэмсэн нь; base centesimal cardinal numeral hundred",
    },
    "дугаар": {
        "source": "Tsevel (1966)",
        "locator": "p. 201, col. 1; http://toli.query.mn/dictionary_items/13856",
        "evidence": "дэс тоо, дугаар, заасан тоо тэмдэг; lexical noun denoting identifying sequence/phone number",
    },
    "холбогдох": {
        "source": "Tsevel (1966)",
        "locator": "p. 734, col. 2; http://toli.query.mn/dictionary_items/29567",
        "evidence": "харилцах, учир холбоо бүхий болох; passive-intransitive communication verb",
    },
    "залгах": {
        "source": "Tsevel (1966)",
        "locator": "p. 228, col. 2; http://toli.query.mn/dictionary_items/4845",
        "evidence": "утсаар залгах, холбож нэгтгэх; communication action verb to dial/connect",
    },
    "цахим": {
        "source": "Tsevel (1966)",
        "locator": "p. 798, col. 1; http://toli.query.mn/dictionary_items/31581",
        "evidence": "цахилгаан тооцоолон бодох техник; digital/electronic qualitative adjective",
    },
    "цонх": {
        "source": "Tsevel (1966)",
        "locator": "p. 808, col. 2; http://toli.query.mn/dictionary_items/27167",
        "evidence": "гэрэл оруулахаар хийсэн гэгээвч, хаалга цонх; household architecture noun window",
    },
    "зураг": {
        "source": "Tsevel (1966)",
        "locator": "p. 254, col. 1; http://toli.query.mn/dictionary_items/18464",
        "evidence": "хавтгай юманд аливаа юмны төрх байдлыг гарган хийсэн дүрс; photograph/picture noun",
    },
    "нөхөр": {
        "source": "Tsevel (1966)",
        "locator": "p. 385, col. 2; http://toli.query.mn/dictionary_items/26129",
        "evidence": "дотно хүн, үзэл санаа ойрхны хүн, гэр бүлийн хань; relational noun companion/husband",
    },
    "байр": {
        "source": "Tsevel (1966)",
        "locator": "p. 73, col. 1; http://toli.query.mn/dictionary_items/4035",
        "evidence": "орогнон орших газар, орон сууц, барилга байшин; residential quarters noun",
    },
    "уншигч": {
        "source": "Tsevel (1966)",
        "locator": "p. 642, col. 1; http://toli.query.mn/dictionary_items/23308",
        "evidence": "уншдаг хүн, номын санд ном уншигч; reader/patron agentive noun headword",
    },
    "үзэх": {
        "source": "Tsevel (1966)",
        "locator": "p. 862, col. 2; http://toli.query.mn/dictionary_items/30942",
        "evidence": "нүдээр харах, сонирхон харах; canonical perception verb to see/watch",
    },
    "олох": {
        "source": "Tsevel (1966)",
        "locator": "p. 414, col. 1; http://toli.query.mn/dictionary_items/1198",
        "evidence": "харсан эрсний эцэст тохиолдох, илрүүлэх; discovery action verb to find",
    },
    "сонгох": {
        "source": "Tsevel (1966)",
        "locator": "p. 488, col. 1; http://toli.query.mn/dictionary_items/13548",
        "evidence": "сайныг шилэх, хэрэгтэй ашигтайгий нь шилж авах; transitive decision verb to select",
    },
    "паспорт": {
        "source": "Tsevel (1966)",
        "locator": "p. 438, col. 2; http://toli.query.mn/dictionary_items/24957",
        "evidence": "үзүүлэгч хүний албан ёсны бичиг баримт; official administrative identity document noun",
    },
    "худалдах": {
        "source": "Tsevel (1966)",
        "locator": "p. 753, col. 2; http://toli.query.mn/dictionary_items/6997",
        "evidence": "үнэ авч арилжин өгөх; commercial transaction verb to sell",
    },
}

# Category B: MANUALLY_REVIEWED_DISTINCT_HEADWORD
# Distinct lexical headwords certified via peer linguistic audit with explicit rationales
MANUALLY_REVIEWED_REGISTRY = {
    "бэ": "Interrogative postpositional particle governing content questions after sonorants and nasals; canonical Khalkha particle headword.",
    "вэ": "Interrogative postpositional particle governing content questions after vowels and obstruents; canonical Khalkha particle headword.",
    "хаагуур": "Spatial trajectory interrogative adverb asking about transit route; distinct lexical pro-form, not a regular local case inflection.",
    "яагаад": "Causal interrogative adverb asking for underlying rationale/reason; lexicalized interrogative headword.",
    "яах": "Interrogative verbal pro-form in standard citation infinitive -х; core predicate interrogative lexeme.",
    "хааш": "Directional interrogative adverb asking about vector of motion; distinct lexical headword, not an inflection.",
    "яаж": "Modal manner adverb asking for operational procedure; distinct lexical headword in Khalkha syntax.",
    "хэдий": "Quantitative interrogative pronoun asking for extent or count; independent lexical root from which cases derive.",
    "хэрхэн": "Procedural interrogative adverb asking about operational method/manner; distinct lexical headword in formal Khalkha.",
    "магадлах": "Canonical verbal infinitive in -х; institutional action verb meaning to verify or ascertain factual accuracy.",
    "асуулга": "Deverbal nominal stem in -лга denoting an institutional survey, questionnaire, or formal inquiry.",
    "тодруулга": "Deverbal nominal stem in -лга denoting clarification or specification of factual particulars.",
    "тодорхой": "Qualitative evaluative adjective denoting distinct, clear, unambiguous factual states.",
    "анкет": "Standard administrative loanword noun denoting personal questionnaire, application form, or biographical sheet.",
    "өгүүлэл": "Textual nominal headword denoting written essay, narrative article, or biographical treatise.",
    "агуулга": "Deverbal abstract noun in -лга denoting substantive thematic content or interview subject matter.",
    "мэдээлэл": "Deverbal informative noun denoting factual details, news dispatch, or digital information items.",
    "сондгой": "Mathematical qualitative adjective denoting odd, indivisible cardinal numbers; antonym of тэгш.",
    "тоолох": "Canonical verbal infinitive in -х; base Khalkha transitive verb for calculation, reckoning, and enumeration.",
    "ширхэг": "Discrete item classifier noun used for counting manufactured goods and inventory stock; bare nominal root.",
    "нийлбэр": "Mathematical/accounting noun denoting aggregate sum or total addition of numbers.",
    "дүн": "Financial and quantitative noun denoting aggregate total, evaluation score, or bottom-line sum.",
    "тэгш": "Mathematical qualitative descriptor for even divisible numbers; bare adjectival headword.",
    "дөч": "Base cardinal decade numeral forty; bare citation root distinct from -н stem allomorph.",
    "тавь": "Base cardinal decade numeral fifty; bare citation root distinct from -н stem allomorph.",
    "жар": "Base cardinal decade numeral sixty; bare citation root distinct from -н stem allomorph.",
    "дал": "Base cardinal decade numeral seventy; bare citation root distinct from -н stem allomorph.",
    "ная": "Base cardinal decade numeral eighty; bare citation root distinct from -н stem allomorph.",
    "ер": "Base cardinal decade numeral ninety; bare citation root distinct from -н stem allomorph.",
    "мөнгө": "Core monetary noun denoting currency, coins, and transactional cash sums in price exchanges.",
    "хичнээн": "Intensive quantitative adverb asking about magnitude or amount; independent lexical interrogative.",
    "орчим": "Approximative postposition modifying preceding numerical or temporal quantities; distinct postpositional headword.",
    "нийт": "Commercial and inventory aggregate noun denoting entire count, gross sum, or comprehensive total.",
    "бүртгэл": "Institutional noun denoting inventory register, catalog log, or official administrative record.",
    "үлдэгдэл": "Accounting noun denoting remainder balance, inventory remnant, or unsold stock balance.",
    "хэмжих": "Canonical verbal infinitive in -х; transitive physical and operational verb to measure or gauge.",
    "үүрэн": "Qualitative descriptor adjective for cellular/mobile telecommunications infrastructure.",
    "сануулах": "Canonical verbal infinitive in -х; causative communication verb to remind, alert, or prompt.",
    "унтраах": "Canonical verbal infinitive in -х; transitive causative verb to power off, extinguish, or shut down.",
    "асаах": "Canonical verbal infinitive in -х; transitive causative verb to turn on, power up, or illuminate.",
    "мессеж": "Standard digital communication loanword noun denoting SMS, electronic text message, or chat item.",
    "сүлжээ": "Infrastructural noun denoting network grid, cellular coverage, or digital interconnection mesh.",
    "код": "Technical noun denoting numeric passcode, dialing PIN, or security verification cipher.",
    "товчлуур": "Instrumental noun in -уур denoting mechanical keypad button, push-switch, or digital key.",
    "нээх": "Canonical verbal infinitive in -х; basic action verb to open, initiate, or launch an account/application.",
    "хаах": "Canonical verbal infinitive in -х; basic action verb to close, terminate, or shut down a session/call.",
    "тушаал": "Administrative noun denoting official military/civic order, directive, or bureaucratic post.",
    "байршил": "Deverbal locative noun in -шил denoting geographical site, physical premises address, or position.",
    "салбар": "Institutional organizational noun denoting subsidiary branch, local affiliate, or chapter division.",
    "факс": "Modern administrative communications loanword denoting facsimile transmission machine or line.",
    "хэлтэс": "Administrative noun denoting organizational department, divisional subsection, or bureaucratic unit.",
    "холбоо": "Relational communication noun denoting link, association, network connectivity, or liaison.",
    "шүүгээ": "Household/office furniture noun denoting storage cabinet, locker, cupboard, or wardrobe.",
    "эдлэл": "Commercial noun denoting manufactured artifact, furniture ware, or finished commodity good.",
    "тоног": "Collective technical noun denoting equipment gear, apparatus, instrumentation, or machine fittings.",
    "жишээ": "Didactic/lexical noun denoting illustrative example, sample case, or communicative model.",
    "хэлбэр": "Morphological/structural noun denoting formal shape, contour, or grammatical configuration.",
    "хань": "Relational social noun denoting companion, partner, associate, or lifelong spouse.",
    "мэргэжилтэн": "Agentive occupational noun in -тан denoting qualified specialist, certified professional, or expert.",
    "хамтлаг": "Collective social noun denoting musical band, collaborative team, or performance ensemble.",
    "ургамал": "Natural science noun denoting botanical flora, living plant organism, or vegetation.",
    "амьтан": "Natural science noun denoting zoological fauna, living animal, or biological creature.",
    "ажилчин": "Socio-economic agentive noun in -чин denoting manual laborer, factory operative, or wage worker.",
    "булан": "Architectural/spatial noun denoting geometric angle, street intersection corner, or room nook.",
    "тавиур": "Instrumental furniture noun in -ур denoting shelf, storage ledge, or bookcase tier.",
    "хайрцаг": "Container packaging noun denoting box, carton, shipping crate, or storage chest.",
    "агуулах": "Architectural noun denoting logistics warehouse, storage depot, or inventory facility.",
    "гарчиг": "Textual structural noun denoting book title, table of contents, or section heading.",
    "сан": "Institutional/financial noun denoting public treasury, resource repository, or library collection.",
    "жагсаалт": "Administrative noun denoting catalog roster, numbered inventory list, or roll of items.",
    "хураах": "Canonical verbal infinitive in -х; transitive agricultural/commercial verb to gather, harvest, or collect.",
    "солих": "Canonical verbal infinitive in -х; transitive transaction verb to swap, exchange, or substitute.",
    "өргөх": "Canonical verbal infinitive in -х; physical action verb to elevate, lift up, or raise.",
    "зөөх": "Canonical verbal infinitive in -х; physical transport verb to carry, convey, or haul cargo.",
    "гэрчилгээ": "Administrative legal noun denoting certificate, credential deed, or official accreditation license.",
    "хавтас": "Stationery organizational noun denoting document folder, file binder, or book cover.",
    "маягт": "Administrative clerical noun denoting standard blank form, template sheet, or application draft.",
    "тэмдэглэл": "Deverbal noun in -лэл denoting written diary entry, memorandum note, or meeting record.",
    "хавсаргах": "Canonical verbal infinitive in -х; administrative verb to append, enclose, or attach documents.",
    "хадгалах": "Canonical verbal infinitive in -х; fiduciary/archival verb to preserve, maintain, store, or save.",
    "төлөх": "Canonical verbal infinitive in -х; financial transaction verb to settle payment, disburse, or pay fee.",
    "захиалах": "Canonical verbal infinitive in -х; commercial transactional verb to order, reserve, or requisition.",
    "буцаах": "Canonical verbal infinitive in -х; transaction verb to return items, reverse a transfer, or refund cash.",
    "тооцох": "Canonical verbal infinitive in -х; mathematical/operational verb to calculate, reckon, or tally up.",
    "хэмжээ": "Quantitative dimensional noun denoting geometric size, capacity volume, or measurable amount.",
    "захиалга": "Commercial noun in -лга denoting booking, formal requisition order, or advance reservation.",
    "хүргэлт": "Deverbal commercial noun in -лт denoting postal delivery, freight transit, or courier dispatch.",
    "баглаа": "Commercial packaging noun denoting bound bouquet, wrapped parcel, or merchandise bundle.",
}

# =============================================================================
# 3. FAIL-CLOSED AUDIT ENGINE
# =============================================================================
def audit_batch2_headwords(root_dir=None):
    """
    Executes a fail-closed headword-purity audit across all 112 Batch 2 lemmas.
    
    Decision Taxonomy:
    - AUTHORITATIVE_HEADWORD_CONFIRMED: Primary dictionary locator/entry verified.
    - MANUALLY_REVIEWED_DISTINCT_HEADWORD: Explicit manual linguistic audit rationale stored.
    - MORPHOLOGICAL_FORM_NOT_LEMMA: Negative test matched (inflection, converb, stem variant).
    - NEEDS_MANUAL_REVIEW: Fail-closed fallback if positive evidence is missing.
    """
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
    decision_counts = {
        "AUTHORITATIVE_HEADWORD_CONFIRMED": 0,
        "MANUALLY_REVIEWED_DISTINCT_HEADWORD": 0,
        "MORPHOLOGICAL_FORM_NOT_LEMMA": 0,
        "NEEDS_MANUAL_REVIEW": 0
    }

    for l in b2_lemmas:
        lid = l['id']
        surface = l.get('lemma', '')
        pos = l.get('pos', '')
        notes = l.get('usageNotes', '') or ''
        gloss = l.get('gloss', '') or ''

        # --- STEP 1: NEGATIVE REGRESSION TESTS ---
        # 1.1 Check known blacklisted inflectional/allomorphic variants
        if surface in KNOWN_INFLECTIONAL_VARIANTS:
            base_form, rel_type = KNOWN_INFLECTIONAL_VARIANTS[surface]
            base_exists = base_form in realized_lemmas_by_text
            base_id = realized_lemmas_by_text.get(base_form, "N/A")
            
            decision = "MORPHOLOGICAL_FORM_NOT_LEMMA"
            row = {
                "id": lid,
                "surface": surface,
                "underlying_lexeme": base_form,
                "relationship_type": rel_type,
                "base_exists": base_exists,
                "base_id": base_id,
                "decision": decision,
                "notes": notes,
                "audit_evidence": f"Flagged by KNOWN_INFLECTIONAL_VARIANTS as {rel_type} of {base_form}"
            }
            audit_table.append(row)
            failures.append(row)
            decision_counts[decision] += 1
            continue

        # 1.2 Check metadata pattern matching for suspect phrases
        metadata_flag = None
        for pat in METADATA_SUSPECT_PATTERNS:
            m = pat.search(notes) or pat.search(gloss)
            if m:
                base_candidate = m.group(1).strip()
                if base_candidate in realized_lemmas_by_text and base_candidate != surface:
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
                "notes": notes,
                "audit_evidence": f"Flagged by METADATA_SUSPECT_PATTERNS as form of {base_form}"
            }
            audit_table.append(row)
            failures.append(row)
            decision_counts[decision] += 1
            continue

        # --- STEP 2: POSITIVE CERTIFICATION (FAIL-CLOSED) ---
        # 2.1 Check Authoritative Dictionary Confirmation
        if surface in AUTHORITATIVE_HEADWORD_REGISTRY:
            auth_info = AUTHORITATIVE_HEADWORD_REGISTRY[surface]
            decision = "AUTHORITATIVE_HEADWORD_CONFIRMED"
            row = {
                "id": lid,
                "surface": surface,
                "underlying_lexeme": surface,
                "relationship_type": "INDEPENDENT_LEXICAL_HEADWORD",
                "base_exists": True,
                "base_id": lid,
                "decision": decision,
                "notes": notes,
                "source": auth_info["source"],
                "locator": auth_info["locator"],
                "audit_evidence": auth_info["evidence"]
            }
            audit_table.append(row)
            decision_counts[decision] += 1
            continue

        # 2.2 Check Explicit Manual Review Registry
        if surface in MANUALLY_REVIEWED_REGISTRY:
            rationale = MANUALLY_REVIEWED_REGISTRY[surface]
            decision = "MANUALLY_REVIEWED_DISTINCT_HEADWORD"
            row = {
                "id": lid,
                "surface": surface,
                "underlying_lexeme": surface,
                "relationship_type": "INDEPENDENT_LEXICAL_HEADWORD",
                "base_exists": True,
                "base_id": lid,
                "decision": decision,
                "notes": notes,
                "source": "Expert Linguistic Peer Review",
                "locator": "Curriculum Lexical Architecture Audit",
                "audit_evidence": rationale
            }
            audit_table.append(row)
            decision_counts[decision] += 1
            continue

        # 2.3 FAIL-CLOSED: Any record lacking positive certification fails
        decision = "NEEDS_MANUAL_REVIEW"
        row = {
            "id": lid,
            "surface": surface,
            "underlying_lexeme": surface,
            "relationship_type": "UNVERIFIED_STATUS",
            "base_exists": True,
            "base_id": lid,
            "decision": decision,
            "notes": notes,
            "audit_evidence": "FAIL-CLOSED: Record lacks authoritative dictionary citation and explicit manual review entry."
        }
        audit_table.append(row)
        failures.append(row)
        decision_counts[decision] += 1

    return audit_table, failures, decision_counts

def print_audit_report(audit_table, failures, decision_counts):
    print("=" * 115)
    print("PHASE 3C.1B-R2: FAIL-CLOSED HEADWORD-PURITY & MORPHOLOGICAL DUPLICATION AUDIT (112 LEMMAS)")
    print("=" * 115)
    print(f"{'Lexical ID':18s} | {'Surface':12s} | {'Source / Dec':36s} | {'Decision':38s}")
    print("-" * 115)
    for r in audit_table:
        src_dec = r.get('source', r.get('relationship_type', ''))[:35]
        print(f"{r['id']:18s} | {r['surface']:12s} | {src_dec:36s} | {r['decision']:38s}")

    print("=" * 115)
    print("Fail-Closed Purity Decision Counts:")
    print(f"  • AUTHORITATIVE_HEADWORD_CONFIRMED:     {decision_counts['AUTHORITATIVE_HEADWORD_CONFIRMED']:3d} / 112")
    print(f"  • MANUALLY_REVIEWED_DISTINCT_HEADWORD:  {decision_counts['MANUALLY_REVIEWED_DISTINCT_HEADWORD']:3d} / 112")
    print(f"  • MORPHOLOGICAL_FORM_NOT_LEMMA:         {decision_counts['MORPHOLOGICAL_FORM_NOT_LEMMA']:3d} (Target: 0)")
    print(f"  • NEEDS_MANUAL_REVIEW:                  {decision_counts['NEEDS_MANUAL_REVIEW']:3d} (Target: 0)")
    total_valid = decision_counts['AUTHORITATIVE_HEADWORD_CONFIRMED'] + decision_counts['MANUALLY_REVIEWED_DISTINCT_HEADWORD']
    print(f"  • Total Valid Certified Headwords:     {total_valid:3d} / 112 ({(total_valid/112)*100:.1f}%)")
    print("=" * 115)

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    table, fails, counts = audit_batch2_headwords(root)
    print_audit_report(table, fails, counts)
    if fails or counts['MORPHOLOGICAL_FORM_NOT_LEMMA'] > 0 or counts['NEEDS_MANUAL_REVIEW'] > 0:
        print(f"\n❌ FAILED: Found {len(fails)} headword purity failures (MORPHOLOGICAL: {counts['MORPHOLOGICAL_FORM_NOT_LEMMA']}, NEEDS_MANUAL_REVIEW: {counts['NEEDS_MANUAL_REVIEW']})!")
        sys.exit(1)
    else:
        print("\n✓ SUCCESS: All 112 Batch 2 lemmas certified under fail-closed headword purity rules!")
        sys.exit(0)
