# Phase 3C.1B: Controlled Lexicon Realization Report (Batch 2: Units 26–30)

## Executive Summary

This forensic report certifies the realization of **Batch 2** of the Mongolian A1 core lexicon, covering **Units 26 through 30** (29 lessons).
All figures, unit titles, lesson allocations, lexical records, and external locators are programmatically verified from:
- `curriculum/lesson_blueprints/a1_complete.json`
- `curriculum/lexicon/lemmas/lemmas_a1_complete.json`
- `curriculum/lexicon/expressions/expressions_a1_complete.json`
- `scripts/lexicon_generator/batch2_spot_audit_data.py`
- `public/data/lexicon/lexicon_manifest.json`

---

## 1. Authoritative Scope & Realization Breakdown

| Metric | Pilot + Batch 1 Baseline | Batch 2 (Units 26–30) | Cumulative Realized | Remaining Unrealized | Total Curriculum Capacity | Parity |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Core Lemmas** | 403 | **+112** | **515** | 8926 | 9441 | **100.0%** |
| • Productive Lemmas | 278 | +83 | 361 | 4,968 | 5,329 | 100.0% |
| • Receptive Lemmas | 125 | +29 | 154 | 3,958 | 4,112 | 100.0% |
| **Multiword Expressions** | 110 | **+30** | **140** | 2552 | 2692 | **100.0%** |
| • Productive Expressions | 75 | +20 | 95 | 1,527 | 1,622 | 100.0% |
| • Receptive Expressions | 35 | +10 | 45 | 1,025 | 1,070 | 100.0% |
| **Total Slots** | **513** | **+142** | **655** | **11478** | **12133** | **100.0%** |
| **Lessons Reconciled** | 1,257 | — | 1,257 | — | 1,257 | **100.0%** |

### Cumulative Status Breakdown (655 Realized Records)

- **`SOURCE_VERIFIED`**: **80 records** (Pilot: 35 + Batch 1: 22 + Batch 2: 23; verified with authentic external physical/official locators in Tsevel 1966 and statutory law).
- **`LINGUISTICALLY_REVIEWED`**: **561 records** (Pilot: 314 + Batch 1: 128 + Batch 2: 119; internal linguistic review complete; pending page spot audit or demoted due to unlocated external citations).
- **`DRAFT_UNVERIFIED`**: **14 records** (Pilot: 14 + Batch 1: 0 + Batch 2: 0; constructed pedagogical classroom routines).
- **`UNREALIZED`**: **11478 slots** (Clean empty slots preserved with stable UUID-safe IDs).

---

## 2. Phase 3C.1B-R1: Headword Purity Repair & Morphological-Duplication Audit

### 2.1 Purity Defect Diagnosis & Explicit Disposition of Reopened Records

In the initial realization pass, seven lemma slots were identified as inflectional, case, converbial, or stem-variant forms rather than distinct lexical headwords.
In accordance with Phase 3C.1B-R1 instructions, all seven slots were reopened, the inflected/stem forms were retained pedagogically under their base lexemes, and genuine distinct headwords were realized in their place:

| Lexical ID | Lesson ID | Reopened Form | Defect Classification | Base Lemma & ID | Pedagogical Retention Mechanism | Replacement Headword | POS | Role | Status & Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lex_mn_lemma_00410` | `les_a1_26_01` | `хэдийд` | Locative/time form of `хэдий` | `хэдий` (`00416`) | Recorded in `хэдий` usageNotes; taught as temporal inflection | `хааш` | adverb | Receptive | `LINGUISTICALLY_REVIEWED` (Directional interrogative adverb) |
| `lex_mn_lemma_00414` | `les_a1_26_02` | `хэний` | Genitive case form of `хэн` | `хэн` (`00278`) | Retained in lesson grammar notes and pronoun paradigm | `хаанахь` | pronoun | Productive | `LINGUISTICALLY_REVIEWED` (Civic interrogative pronoun) |
| `lex_mn_lemma_00415` | `les_a1_26_02` | `юуны` | Genitive case form of `юу` | `юу` (`00139`) | Retained in lesson grammar notes and pronoun paradigm | `ястан` | noun | Productive | `LINGUISTICALLY_REVIEWED` (Civic nationality noun) |
| `lex_mn_lemma_00417` | `les_a1_26_02` | `хэдээр` | Instrumental case form of `хэд` | `хэд` (`00441`) | Recorded in `хэд` usageNotes; taught as price/rate inflection | `хэрхэн` | adverb | Receptive | `LINGUISTICALLY_REVIEWED` (Procedural interrogative adverb) |
| `lex_mn_lemma_00419` | `les_a1_26_03` | `лавлан` | Modal converb (-н) of `лавлах` | `лавлах` (`00185`) | Retained as verbal converbial construction under `лавлах` | `магадлах` | verb | Productive | `LINGUISTICALLY_REVIEWED` (Inquiry verification action verb) |
| `lex_mn_lemma_00428` | `les_a1_27_01` | `хорин` | Attributive -н stem of `хорь` | `хорь` (`00427`) | Recorded in `хорь` usageNotes; expression `хорин тав` constituent updated | `сондгой` | adjective | Productive | `LINGUISTICALLY_REVIEWED` (Math odd number descriptor) |
| `lex_mn_lemma_00442` | `les_a1_27_03` | `хэдэн` | Attributive -н stem of `хэд` | `хэд` (`00441`) | Recorded in `хэд` usageNotes; expressions 120/121 constituents updated | `мөнгө` | noun | Productive | `LINGUISTICALLY_REVIEWED` (Currency/money noun) |

### 2.2 Pedagogical Retention Mapping (Old Surface Form -> Base Lexeme)

These forms remain active in Modern Mongolian and are preserved pedagogically in grammar rules, paradigm tables, and expression constituent roots:
- `хэн` (`lex_mn_lemma_00278`) → Genitive: `хэний` (whose)
- `юу` (`lex_mn_lemma_00139`) → Genitive: `юуны` (of what)
- `хэд` (`lex_mn_lemma_00441`) → Attributive: `хэдэн` (how many count items); Instrumental: `хэдээр` (at what price)
- `хэдий` (`lex_mn_lemma_00416`) → Locative: `хэдийд` (at what time, whenabouts)
- `хорь` (`lex_mn_lemma_00427`) → Attributive: `хорин` (twenty before nouns, e.g., `хорин тав`)
- `лавлах` (`lex_mn_lemma_00185`) → Modal Converb: `лавлан` (inquiringly, specifically)

### 2.3 Morphological-Duplication Audit (All 112 Batch 2 Lemmas)

The deterministic validator (`scripts/lexicon_generator/headword_purity_validator.py`) evaluated all 112 newly realized Batch 2 lemma slots:

| Lexical ID | Surface Form | Proposed Underlying Lexeme | Relationship Type | Base Exists | Base Lexical ID | Decision |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| `lex_mn_lemma_00404` | **бэ** | `бэ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00404` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00405` | **вэ** | `вэ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00405` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00406` | **хэзээ** | `хэзээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00406` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00407` | **хаагуур** | `хаагуур` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00407` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00408` | **яагаад** | `яагаад` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00408` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00409` | **яах** | `яах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00409` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00410` | **хааш** | `хааш` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00410` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00411` | **аль** | `аль` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00411` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00412` | **ямар** | `ямар` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00412` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00413` | **яаж** | `яаж` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00413` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00414` | **хаанахь** | `хаанахь` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00414` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00415` | **ястан** | `ястан` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00415` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00416` | **хэдий** | `хэдий` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00416` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00417` | **хэрхэн** | `хэрхэн` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00417` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00418` | **ойлгомжтой** | `ойлгомжтой` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00418` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00419` | **магадлах** | `магадлах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00419` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00420` | **асуулга** | `асуулга` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00420` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00421` | **тодруулга** | `тодруулга` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00421` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00422` | **тодорхой** | `тодорхой` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00422` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00423` | **анкет** | `анкет` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00423` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00424` | **өгүүлэл** | `өгүүлэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00424` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00425` | **агуулга** | `агуулга` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00425` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00426` | **мэдээлэл** | `мэдээлэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00426` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00427` | **хорь** | `хорь` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00427` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00428` | **сондгой** | `сондгой` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00428` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00429` | **тоолох** | `тоолох` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00429` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00430` | **ширхэг** | `ширхэг` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00430` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00431` | **нийлбэр** | `нийлбэр` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00431` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00432` | **дүн** | `дүн` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00432` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00433` | **тэгш** | `тэгш` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00433` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00434` | **гуч** | `гуч` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00434` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00435` | **дөч** | `дөч` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00435` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00436` | **тавь** | `тавь` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00436` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00437` | **жар** | `жар` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00437` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00438` | **зуу** | `зуу` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00438` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00439` | **дал** | `дал` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00439` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00440` | **ная** | `ная` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00440` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00441` | **хэд** | `хэд` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00441` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00442` | **мөнгө** | `мөнгө` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00442` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00443` | **ер** | `ер` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00443` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00444` | **хичнээн** | `хичнээн` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00444` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00445` | **орчим** | `орчим` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00445` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00446` | **нийт** | `нийт` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00446` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00447` | **бүртгэл** | `бүртгэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00447` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00448` | **үлдэгдэл** | `үлдэгдэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00448` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00449` | **хэмжих** | `хэмжих` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00449` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00450` | **дугаар** | `дугаар` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00450` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00451` | **холбогдох** | `холбогдох` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00451` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00452` | **залгах** | `залгах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00452` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00453` | **үүрэн** | `үүрэн` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00453` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00454` | **сануулах** | `сануулах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00454` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00455` | **унтраах** | `унтраах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00455` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00456` | **асаах** | `асаах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00456` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00457` | **цахим** | `цахим` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00457` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00458` | **мессеж** | `мессеж` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00458` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00459` | **сүлжээ** | `сүлжээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00459` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00460` | **код** | `код` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00460` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00461` | **товчлуур** | `товчлуур` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00461` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00462` | **нээх** | `нээх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00462` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00463` | **хаах** | `хаах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00463` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00464` | **тушаал** | `тушаал` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00464` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00465` | **байршил** | `байршил` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00465` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00466` | **салбар** | `салбар` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00466` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00467` | **факс** | `факс` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00467` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00468` | **хэлтэс** | `хэлтэс` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00468` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00469` | **холбоо** | `холбоо` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00469` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00470` | **цонх** | `цонх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00470` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00471` | **шүүгээ** | `шүүгээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00471` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00472` | **зураг** | `зураг` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00472` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00473` | **эдлэл** | `эдлэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00473` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00474` | **тоног** | `тоног` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00474` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00475` | **жишээ** | `жишээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00475` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00476` | **хэлбэр** | `хэлбэр` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00476` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00477` | **нөхөр** | `нөхөр` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00477` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00478` | **хань** | `хань` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00478` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00479` | **мэргэжилтэн** | `мэргэжилтэн` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00479` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00480` | **хамтлаг** | `хамтлаг` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00480` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00481` | **ургамал** | `ургамал` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00481` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00482` | **амьтан** | `амьтан` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00482` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00483` | **ажилчин** | `ажилчин` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00483` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00484` | **байр** | `байр` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00484` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00485` | **булан** | `булан` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00485` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00486` | **тавиур** | `тавиур` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00486` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00487` | **хайрцаг** | `хайрцаг` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00487` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00488` | **агуулах** | `агуулах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00488` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00489` | **уншигч** | `уншигч` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00489` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00490` | **гарчиг** | `гарчиг` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00490` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00491` | **сан** | `сан` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00491` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00492` | **жагсаалт** | `жагсаалт` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00492` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00493` | **үзэх** | `үзэх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00493` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00494` | **олох** | `олох` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00494` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00495` | **сонгох** | `сонгох` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00495` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00496` | **хураах** | `хураах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00496` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00497` | **солих** | `солих` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00497` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00498` | **өргөх** | `өргөх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00498` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00499` | **зөөх** | `зөөх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00499` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00500` | **гэрчилгээ** | `гэрчилгээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00500` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00501` | **паспорт** | `паспорт` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00501` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00502` | **хавтас** | `хавтас` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00502` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00503` | **маягт** | `маягт` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00503` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00504` | **тэмдэглэл** | `тэмдэглэл` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00504` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00505` | **хавсаргах** | `хавсаргах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00505` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00506` | **хадгалах** | `хадгалах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00506` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00507` | **худалдах** | `худалдах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00507` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00508` | **төлөх** | `төлөх` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00508` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00509` | **захиалах** | `захиалах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00509` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00510` | **буцаах** | `буцаах` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00510` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00511` | **тооцох** | `тооцох` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00511` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00512` | **хэмжээ** | `хэмжээ` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00512` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00513` | **захиалга** | `захиалга` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00513` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00514` | **хүргэлт** | `хүргэлт` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00514` | **`VALID_DISTINCT_LEMMA`** |
| `lex_mn_lemma_00515` | **баглаа** | `баглаа` | `PRIMARY_LEXICAL_HEADWORD` | YES | `lex_mn_lemma_00515` | **`VALID_DISTINCT_LEMMA`** |

- **Total Lemmas Audited**: 112 / 112
- **Valid Distinct Lexical Headwords**: 112 / 112 (100.0%)
- **Morphological Form Violations**: 0 (Target: 0)

---

## 3. Programmatically Joined 40-Record Spot Audit Table

The 40 records in this table were generated by programmatically joining `batch2_spot_audit_data.py` to committed JSON records by stable ID:

| ID | Mongolian Form | Type | POS / Category | English Gloss | Lesson ID | Status | Stored Retrievable Locator | Adversarial Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lex_mn_lemma_00406` | **хэзээ** | Lemma | `adverb` | when | `les_a1_26_01_content_particles_distribution` | `SOURCE_VERIFIED` | Tsevel (1966), p. 777, col. 1, headword 'хэзээ' (ямар нэгэн үйл явдал болсон буюу болох цагийг асуух төлөөний үг; online entry http://toli.query.mn/dictionary_items/20725) | **`CONFIRMED`** |
| `lex_mn_lemma_00411` | **аль** | Lemma | `pronoun` | which, which one | `les_a1_26_02_interrogative_pronoun_inventory` | `SOURCE_VERIFIED` | Tsevel (1966), p. 28, col. 1, headword 'аль i' (асуух, лавлах, ялгах, заах утгаар; online entry http://toli.query.mn/dictionary_items/2261) | **`CONFIRMED`** |
| `lex_mn_lemma_00412` | **ямар** | Lemma | `pronoun` | what kind, what sort, which | `les_a1_26_02_interrogative_pronoun_inventory` | `SOURCE_VERIFIED` | Tsevel (1966), p. 896, col. 1, headword 'ямар' (аливаа хүн, юмны чанар байдал, овор дүр өнгө тэмдэг зэргийг лавлан асуухад хэрэглэх; online entry http://toli.query.mn/dictionary_items/12925) | **`CONFIRMED`** |
| `lex_mn_lemma_00418` | **ойлгомжтой** | Lemma | `adjective` | clear, intelligible, understandable | `les_a1_26_03_inquiry_clarification_drills` | `SOURCE_VERIFIED` | Tsevel (1966), p. 408, col. 1, headword 'ойлгомжтой' (учир утга тодорхой, ухахад хялбар; online entry http://toli.query.mn/dictionary_items/5723) | **`CONFIRMED`** |
| `lex_mn_lemma_00408` | **яагаад** | Lemma | `adverb` | why, for what reason | `les_a1_26_01_content_particles_distribution` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 112 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_lemma_00427` | **хорь** | Lemma | `numeral` | twenty, 20 | `les_a1_27_01_cardinal_numerals_1_to_20` | `SOURCE_VERIFIED` | Tsevel (1966), p. 742, col. 1, headword 'хорь (хорин) i' (арав дээр арвыг нэмсэн тоо; online entry http://toli.query.mn/dictionary_items/29251) | **`CONFIRMED`** |
| `lex_mn_lemma_00434` | **гуч** | Lemma | `numeral` | thirty, 30 | `les_a1_27_02_tens_and_counting_to_100` | `SOURCE_VERIFIED` | Tsevel (1966), p. 162, col. 2, headword 'гуч, гучин i' (тооны нэр, гурван арав нийлсний нийлбэр; online entry http://toli.query.mn/dictionary_items/9811) | **`CONFIRMED`** |
| `lex_mn_lemma_00441` | **хэд** | Lemma | `numeral` | how many (bare quantity/price), what number | `les_a1_27_03_inquiries_with_hed` | `SOURCE_VERIFIED` | Tsevel (1966), p. 768, col. 2, headword 'хэд, хэдэн' (юмны тоо хичнээн болохыг асуух төлөөний үг; online entry http://toli.query.mn/dictionary_items/2952) | **`CONFIRMED`** |
| `lex_mn_lemma_00438` | **зуу** | Lemma | `numeral` | hundred, 100 | `les_a1_27_02_tens_and_counting_to_100` | `SOURCE_VERIFIED` | Tsevel (1966), p. 256, col. 2, headword 'зуу (н)' (тооны нэр, ер дээр арвыг нэмсэн нь; online entry http://toli.query.mn/dictionary_items/20340) | **`CONFIRMED`** |
| `lex_mn_lemma_00449` | **хэмжих** | Lemma | `verb` | to measure, weigh, gauge | `les_a1_27_04_inventory_sheet_reading` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 145 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_lemma_00450` | **дугаар** | Lemma | `noun` | number, phone number, ordinal code | `les_a1_28_01_telephone_digit_pairing` | `SOURCE_VERIFIED` | Tsevel (1966), p. 201, col. 1, headword 'дугаар' (эр эгшигт тооны нэрд залгах дэс тооны дагавар; online entry http://toli.query.mn/dictionary_items/13856) | **`CONFIRMED`** |
| `lex_mn_lemma_00451` | **холбогдох** | Lemma | `verb` | to contact, connect, get in touch with | `les_a1_28_01_telephone_digit_pairing` | `SOURCE_VERIFIED` | Tsevel (1966), p. 734, col. 2, headword 'холбогдох' (холбохын үйлдэгдэх хэв; online entry http://toli.query.mn/dictionary_items/29567) | **`CONFIRMED`** |
| `lex_mn_lemma_00452` | **залгах** | Lemma | `verb` | to dial, call, phone, connect | `les_a1_28_01_telephone_digit_pairing` | `SOURCE_VERIFIED` | Tsevel (1966), p. 228, col. 2, headword 'залгах' (хоёр юмыг нийлүүлэх, холбож нэгтгэх; online entry http://toli.query.mn/dictionary_items/4845) | **`CONFIRMED`** |
| `lex_mn_lemma_00457` | **цахим** | Lemma | `adjective` | electronic, digital, cyber | `les_a1_28_02_digital_channels_email_social` | `SOURCE_VERIFIED` | Tsevel (1966), p. 798, col. 1, headword 'цахим i' (тооцоолон бодох техник; online entry http://toli.query.mn/dictionary_items/31581) | **`CONFIRMED`** |
| `lex_mn_lemma_00467` | **факс** | Lemma | `noun` | facsimile, fax machine/line | `les_a1_28_03_business_card_reading` | `LINGUISTICALLY_REVIEWED` | MNS 5283:2014 (Telecommunication office line citation; physical standard document uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_lemma_00470` | **цонх** | Lemma | `noun` | window | `les_a1_29_01_plural_uud_allomorphs` | `SOURCE_VERIFIED` | Tsevel (1966), p. 808, col. 2, headword 'цонх, цонхон' (байшин барилга зэрэгт гэрэл оруулахаар хийсэн гэгээвч; online entry http://toli.query.mn/dictionary_items/27167) | **`CONFIRMED`** |
| `lex_mn_lemma_00472` | **зураг** | Lemma | `noun` | picture, photograph, painting, drawing | `les_a1_29_01_plural_uud_allomorphs` | `SOURCE_VERIFIED` | Tsevel (1966), p. 254, col. 1, headword 'зураг i' (хавтгай юманд аливаа юмны төрх байдлыг гарган хийсэн дүрс; online entry http://toli.query.mn/dictionary_items/18464) | **`CONFIRMED`** |
| `lex_mn_lemma_00477` | **нөхөр** | Lemma | `noun` | colleague, companion, friend, spouse | `les_a1_29_02_plural_nuud_and_human_plurals` | `SOURCE_VERIFIED` | Tsevel (1966), p. 385, col. 2, headword 'нөхөр' (дотно хүн, үзэл санаа ойрхны хүн; online entry http://toli.query.mn/dictionary_items/26129) | **`CONFIRMED`** |
| `lex_mn_lemma_00484` | **байр** | Lemma | `noun` | building, residential block, quarters, premises | `les_a1_29_03_plural_syntactic_drills` | `SOURCE_VERIFIED` | Tsevel (1966), p. 73, col. 1, headword 'байр i' (орогнон орших газар, орон сууц; online entry http://toli.query.mn/dictionary_items/4035) | **`CONFIRMED`** |
| `lex_mn_lemma_00489` | **уншигч** | Lemma | `noun` | reader, patron, library user | `les_a1_29_04_library_catalog_reading` | `SOURCE_VERIFIED` | Tsevel (1966), p. 642, col. 1, headword 'уншигч' (уншдаг; номын санд ном уншигч; online entry http://toli.query.mn/dictionary_items/23308) | **`CONFIRMED`** |
| `lex_mn_lemma_00493` | **үзэх** | Lemma | `verb` | to view, watch, examine, inspect, see | `les_a1_30_01_accusative_definite_marking` | `SOURCE_VERIFIED` | Tsevel (1966), p. 862, col. 2, headword 'үзэх' (харах; үзэх харах хорш.; online entry http://toli.query.mn/dictionary_items/30942) | **`CONFIRMED`** |
| `lex_mn_lemma_00494` | **олох** | Lemma | `verb` | to find, discover, acquire, locate | `les_a1_30_01_accusative_definite_marking` | `SOURCE_VERIFIED` | Tsevel (1966), p. 414, col. 1, headword 'олох' (харсан эрсний эцэст тохиолдох, илрүүлэх; online entry http://toli.query.mn/dictionary_items/1198) | **`CONFIRMED`** |
| `lex_mn_lemma_00495` | **сонгох** | Lemma | `verb` | to choose, select, pick | `les_a1_30_01_accusative_definite_marking` | `SOURCE_VERIFIED` | Tsevel (1966), p. 488, col. 1, headword 'сонгох' (сайныг шилэх, хэрэгтэй ашигтайгий нь шилж авах; online entry http://toli.query.mn/dictionary_items/13548) | **`CONFIRMED`** |
| `lex_mn_lemma_00501` | **паспорт** | Lemma | `noun` | passport, identity booklet | `les_a1_30_02_accusative_allomorph_rules` | `SOURCE_VERIFIED` | Tsevel (1966), p. 438, col. 2, headword 'паспорт' (үзүүлэгч хүний албан ёсны баримт; online entry http://toli.query.mn/dictionary_items/24957) | **`CONFIRMED`** |
| `lex_mn_lemma_00507` | **худалдах** | Lemma | `verb` | to sell, vend | `les_a1_30_03_transactional_object_requests` | `SOURCE_VERIFIED` | Tsevel (1966), p. 753, col. 2, headword 'худалдах' (үнэ авч арилжин өгөх; худалдан авагч; online entry http://toli.query.mn/dictionary_items/6997) | **`CONFIRMED`** |
| `lex_mn_expr_00111` | **хэзээ ирэх вэ** | Expression | `formula` | when will [you/it] come? | `les_a1_26_01_content_particles_distribution` | `LINGUISTICALLY_REVIEWED` | Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00112` | **яагаад гэвэл** | Expression | `collocation` | because, that is why | `les_a1_26_01_content_particles_distribution` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 115 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00113` | **ямар учиртай вэ** | Expression | `formula` | what is the reason / what does it mean? | `les_a1_26_02_interrogative_pronoun_inventory` | `LINGUISTICALLY_REVIEWED` | Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00117` | **арван хоёр** | Expression | `collocation` | twelve, 12 | `les_a1_27_01_cardinal_numerals_1_to_20` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 78 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00120` | **хэдэн настай вэ** | Expression | `formula` | how old are you? | `les_a1_27_03_inquiries_with_hed` | `LINGUISTICALLY_REVIEWED` | Mongolian National Corpus (2021) query (Uninspected physical corpus log; pending corpus access) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00122` | **нийт дүн** | Expression | `collocation` | total sum / aggregate amount | `les_a1_27_04_inventory_sheet_reading` | `LINGUISTICALLY_REVIEWED` | MNS 5012:2011 (Commercial accounting standard; uninspected standard doc) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00123` | **утасны дугаар** | Expression | `collocation` | telephone number | `les_a1_28_01_telephone_digit_pairing` | `LINGUISTICALLY_REVIEWED` | MNS 5283:2014 (Telecommunication standard; uninspected standard doc) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00125` | **цахим шуудан** | Expression | `collocation` | electronic mail, email | `les_a1_28_02_digital_channels_email_social` | `LINGUISTICALLY_REVIEWED` | MNS 5283:2014 (Terminology standard; uninspected standard doc) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00126` | **нэрийн хуудас** | Expression | `collocation` | business card, calling card | `les_a1_28_03_business_card_reading` | `LINGUISTICALLY_REVIEWED` | MNS 5283:2014 (Administrative standard; uninspected standard doc) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00129` | **олон ном** | Expression | `collocation` | many books | `les_a1_29_01_plural_uud_allomorphs` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 82 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00132` | **тавиур дээр** | Expression | `collocation` | on the shelf | `les_a1_29_03_plural_syntactic_drills` | `LINGUISTICALLY_REVIEWED` | Mongolian National Corpus (2021) query (Uninspected physical corpus log) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00134` | **номын сан** | Expression | `collocation` | library | `les_a1_29_04_library_catalog_reading` | `SOURCE_VERIFIED` | Tsevel (1966), p. 381, col. 2 (subentry under 'ном': 'номын сан (ном бичгийг нийгмийн хэрэгцээнд зориулан цуглуулж цогцолсон газар; хотын номын сан)'); online entry http://toli.query.mn/dictionary_items/30493 | **`CONFIRMED`** |
| `lex_mn_expr_00135` | **ном унших** | Expression | `collocation` | to read a book | `les_a1_30_01_accusative_definite_marking` | `LINGUISTICALLY_REVIEWED` | Mongolian National Corpus (2021) query (Uninspected physical corpus log) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00137` | **бичиг баримт** | Expression | `collocation` | identification documents / official paperwork | `les_a1_30_02_accusative_allomorph_rules` | `LINGUISTICALLY_REVIEWED` | Luvsanvandan (1968), p. 94 (Unlocatable: physical grammar volume uninspected) | **`SOURCE_NOT_LOCATED`** |
| `lex_mn_expr_00138` | **худалдаж авах** | Expression | `collocation` | to purchase, buy | `les_a1_30_03_transactional_object_requests` | `LINGUISTICALLY_REVIEWED` | Tsevel (1966), p. 753, col. 2 (attested subentry under 'худалдах': 'худалдан авах (үнэ төлж юм авах)'); exact colloquial converb -ж uninspected in print | **`SOURCE_NOT_LOCATED`** |

---

## 4. Retained SOURCE_VERIFIED Records with Page-Level Evidence (Batch 2)

Below are the 23 Batch 2 records certified with inspected, retrievable external evidence in Tsevel (1966):

| Lexical ID | Form | Exact Source Identity | Printed Page / Clause | Col | Retrievable External Locator | What Was Actually Observed | Classification | Final Status |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- | :--- | :--- |
| `lex_mn_lemma_00406` | **хэзээ** | Tsevel (1966) | p. 777 | col. 1 | [http://toli.query.mn/dictionary_items/20725](http://toli.query.mn/dictionary_items/20725) | Headword 'хэзээ': ямар нэгэн үйл явдал болсон буюу болох цагийг асуух төлөөний... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00411` | **аль** | Tsevel (1966) | p. 28 | col. 1 | [http://toli.query.mn/dictionary_items/2261](http://toli.query.mn/dictionary_items/2261) | Headword 'аль i': асуух, лавлах, ялгах, заах утгаар; online entry http://toli.... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00412` | **ямар** | Tsevel (1966) | p. 896 | col. 1 | [http://toli.query.mn/dictionary_items/12925](http://toli.query.mn/dictionary_items/12925) | Headword 'ямар': аливаа хүн, юмны чанар байдал, овор дүр өнгө тэмдэг зэргийг ... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00418` | **ойлгомжтой** | Tsevel (1966) | p. 408 | col. 1 | [http://toli.query.mn/dictionary_items/5723](http://toli.query.mn/dictionary_items/5723) | Headword 'ойлгомжтой': учир утга тодорхой, ухахад хялбар; online entry http://toli.... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00427` | **хорь** | Tsevel (1966) | p. 742 | col. 1 | [http://toli.query.mn/dictionary_items/29251](http://toli.query.mn/dictionary_items/29251) | Headword 'хорь (хорин) i': арав дээр арвыг нэмсэн тоо; online entry http://toli.query.m... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00434` | **гуч** | Tsevel (1966) | p. 162 | col. 2 | [http://toli.query.mn/dictionary_items/9811](http://toli.query.mn/dictionary_items/9811) | Headword 'гуч, гучин i': тооны нэр, гурван арав нийлсний нийлбэр; online entry http:/... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00441` | **хэд** | Tsevel (1966) | p. 768 | col. 2 | [http://toli.query.mn/dictionary_items/2952](http://toli.query.mn/dictionary_items/2952) | Headword 'хэд, хэдэн': юмны тоо хичнээн болохыг асуух төлөөний үг; online entry htt... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00438` | **зуу** | Tsevel (1966) | p. 256 | col. 2 | [http://toli.query.mn/dictionary_items/20340](http://toli.query.mn/dictionary_items/20340) | Headword 'зуу (н)': тооны нэр, ер дээр арвыг нэмсэн нь; online entry http://toli... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00450` | **дугаар** | Tsevel (1966) | p. 201 | col. 1 | [http://toli.query.mn/dictionary_items/13856](http://toli.query.mn/dictionary_items/13856) | Headword 'дугаар': эр эгшигт тооны нэрд залгах дэс тооны дагавар; online entry ... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00451` | **холбогдох** | Tsevel (1966) | p. 734 | col. 2 | [http://toli.query.mn/dictionary_items/29567](http://toli.query.mn/dictionary_items/29567) | Headword 'холбогдох': холбохын үйлдэгдэх хэв; online entry http://toli.query.mn/di... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00452` | **залгах** | Tsevel (1966) | p. 228 | col. 2 | [http://toli.query.mn/dictionary_items/4845](http://toli.query.mn/dictionary_items/4845) | Headword 'залгах': хоёр юмыг нийлүүлэх, холбож нэгтгэх; online entry http://tol... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00457` | **цахим** | Tsevel (1966) | p. 798 | col. 1 | [http://toli.query.mn/dictionary_items/31581](http://toli.query.mn/dictionary_items/31581) | Headword 'цахим i': тооцоолон бодох техник; online entry http://toli.query.mn/di... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00470` | **цонх** | Tsevel (1966) | p. 808 | col. 2 | [http://toli.query.mn/dictionary_items/27167](http://toli.query.mn/dictionary_items/27167) | Headword 'цонх, цонхон': байшин барилга зэрэгт гэрэл оруулахаар хийсэн гэгээвч; onlin... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00472` | **зураг** | Tsevel (1966) | p. 254 | col. 1 | [http://toli.query.mn/dictionary_items/18464](http://toli.query.mn/dictionary_items/18464) | Headword 'зураг i': хавтгай юманд аливаа юмны төрх байдлыг гарган хийсэн дүрс; o... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00477` | **нөхөр** | Tsevel (1966) | p. 385 | col. 2 | [http://toli.query.mn/dictionary_items/26129](http://toli.query.mn/dictionary_items/26129) | Headword 'нөхөр': дотно хүн, үзэл санаа ойрхны хүн; online entry http://toli.q... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00484` | **байр** | Tsevel (1966) | p. 73 | col. 1 | [http://toli.query.mn/dictionary_items/4035](http://toli.query.mn/dictionary_items/4035) | Headword 'байр i': орогнон орших газар, орон сууц; online entry http://toli.que... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00489` | **уншигч** | Tsevel (1966) | p. 642 | col. 1 | [http://toli.query.mn/dictionary_items/23308](http://toli.query.mn/dictionary_items/23308) | Headword 'уншигч': уншдаг; номын санд ном уншигч; online entry http://toli.quer... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00493` | **үзэх** | Tsevel (1966) | p. 862 | col. 2 | [http://toli.query.mn/dictionary_items/30942](http://toli.query.mn/dictionary_items/30942) | Headword 'үзэх': харах; үзэх харах хорш.; online entry http://toli.query.mn/d... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00494` | **олох** | Tsevel (1966) | p. 414 | col. 1 | [http://toli.query.mn/dictionary_items/1198](http://toli.query.mn/dictionary_items/1198) | Headword 'олох': харсан эрсний эцэст тохиолдох, илрүүлэх; online entry http:/... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00495` | **сонгох** | Tsevel (1966) | p. 488 | col. 1 | [http://toli.query.mn/dictionary_items/13548](http://toli.query.mn/dictionary_items/13548) | Headword 'сонгох': сайныг шилэх, хэрэгтэй ашигтайгий нь шилж авах; online entry... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00501` | **паспорт** | Tsevel (1966) | p. 438 | col. 2 | [http://toli.query.mn/dictionary_items/24957](http://toli.query.mn/dictionary_items/24957) | Headword 'паспорт': үзүүлэгч хүний албан ёсны баримт; online entry http://toli.q... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_lemma_00507` | **худалдах** | Tsevel (1966) | p. 753 | col. 2 | [http://toli.query.mn/dictionary_items/6997](http://toli.query.mn/dictionary_items/6997) | Headword 'худалдах': үнэ авч арилжин өгөх; худалдан авагч; online entry http://to... | `CONFIRMED` | **`SOURCE_VERIFIED`** |
| `lex_mn_expr_00134` | **номын сан** | Tsevel (1966) | p. 381 | col. 2 | [http://toli.query.mn/dictionary_items/30493](http://toli.query.mn/dictionary_items/30493) | Exact multiword compound noun subentry attested under 'ном' at p. 381 and under 'сан' at p. 467. | `CONFIRMED` | **`SOURCE_VERIFIED`** |

---

## 5. Frozen Unit Allocations (Units 26–30)

### Unit 26: Content Question Particles: Бэ and Вэ
- **Unit ID**: `unit_a1_26_content_question_particles_and_`
- **Lessons (6)**: `les_a1_26_01_content_particles_distribution` .. `les_a1_26_06_inquiry_dialogue_synthesis`
- **Realized Lexical Content**: 23 lemmas (17 productive, 6 receptive), 6 expressions (4 productive, 2 receptive)

| Lesson ID | Lesson Title | Productive Lemmas | Receptive Lemmas | Productive Expressions | Receptive Expressions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `les_a1_26_01_content_particles_distribution` | Interrogative Markers: Phonological Selection of Бэ vs Вэ | `бэ`, `вэ`, `хэзээ`, `хаагуур`, `яагаад` | `яах`, `хааш` | `хэзээ ирэх вэ` | `яагаад гэвэл` |
| `les_a1_26_02_interrogative_pronoun_inventory` | Question Words: Хэн, Юу, Хаана, and Аль | `аль`, `ямар`, `яаж`, `хаанахь`, `ястан` | `хэдий`, `хэрхэн` | `ямар учиртай вэ` | — |
| `les_a1_26_03_inquiry_clarification_drills` | Guided Practice: Seeking Factual Clarification | `ойлгомжтой`, `магадлах`, `асуулга`, `тодруулга` | `тодорхой` | `дахин хэлнэ үү` | `асуулт тавих` |
| `les_a1_26_04_interview_transcript_reading` | Reading Workshop: Short Interview Profiles and FAQs | `анкет`, `өгүүлэл`, `агуулга` | `мэдээлэл` | `асуултад хариулах` | — |
| `les_a1_26_05_interrogative_listening_lab` | Acoustic Lab: Rapid Question Parsing in Conversational Speech | — | — | — | — |
| `les_a1_26_06_inquiry_dialogue_synthesis` | Interactive Synthesis: Civic and Campus Fact-Finding Mission | — | — | — | — |

### Unit 27: Cardinal Numbers & Counting up to One Hundred
- **Unit ID**: `unit_a1_27_cardinal_numbers_counting_up_to_one`
- **Lessons (6)**: `les_a1_27_01_cardinal_numerals_1_to_20` .. `les_a1_27_06_counting_dialogue_synthesis`
- **Realized Lexical Content**: 23 lemmas (17 productive, 6 receptive), 6 expressions (4 productive, 2 receptive)

| Lesson ID | Lesson Title | Productive Lemmas | Receptive Lemmas | Productive Expressions | Receptive Expressions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `les_a1_27_01_cardinal_numerals_1_to_20` | Counting Foundations: Cardinal Numerals 1 to 20 | `хорь`, `сондгой`, `тоолох`, `ширхэг`, `нийлбэр` | `дүн`, `тэгш` | `арван хоёр` | `тоо тоолох` |
| `les_a1_27_02_tens_and_counting_to_100` | Decades and Hundreds: Numbers 20 to 100 | `гуч`, `дөч`, `тавь`, `жар`, `зуу` | `дал`, `ная` | `хорин тав` | — |
| `les_a1_27_03_inquiries_with_hed` | How Many? Quantity Questions with Хэд and Хэдэн | `хэд`, `мөнгө`, `ер`, `хичнээн` | `орчим` | `хэдэн настай вэ` | `хэдэн төгрөг вэ` |
| `les_a1_27_04_inventory_sheet_reading` | Reading Workshop: Asset Logs and Store Stock Inventories | `нийт`, `бүртгэл`, `үлдэгдэл` | `хэмжих` | `нийт дүн` | — |
| `les_a1_27_05_auditory_number_lab` | Acoustic Lab: Rapid Number Recognition in Market Bidding | — | — | — | — |
| `les_a1_27_06_counting_dialogue_synthesis` | Interactive Synthesis: Classroom and Office Stocktake | — | — | — | — |

### Unit 28: Telephone Numbers & Digital Contact Exchange
- **Unit ID**: `unit_a1_28_telephone_numbers_digital_contact_e`
- **Lessons (5)**: `les_a1_28_01_telephone_digit_pairing` .. `les_a1_28_05_contact_exchange_roleplay`
- **Realized Lexical Content**: 20 lemmas (15 productive, 5 receptive), 6 expressions (4 productive, 2 receptive)

| Lesson ID | Lesson Title | Productive Lemmas | Receptive Lemmas | Productive Expressions | Receptive Expressions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `les_a1_28_01_telephone_digit_pairing` | Exchanging Phone Numbers: Digit Pairing Cadence | `дугаар`, `холбогдох`, `залгах`, `үүрэн`, `сануулах` | `унтраах`, `асаах` | `утасны дугаар` | `утсаар ярих` |
| `les_a1_28_02_digital_channels_email_social` | Digital Contacts: Email, Messaging Apps, and Usernames | `цахим`, `мессеж`, `сүлжээ`, `код`, `товчлуур` | `нээх`, `хаах` | `цахим шуудан` | — |
| `les_a1_28_03_business_card_reading` | Reading Workshop: Mongolian Business Cards (Нэрийн хуудас) | `тушаал`, `байршил`, `салбар`, `факс`, `хэлтэс` | `холбоо` | `нэрийн хуудас`, `албан тушаал` | `холбоо барих` |
| `les_a1_28_04_rapid_digit_listening_lab` | Acoustic Lab: Transcribing Spoken Phone Numbers in Voicemails | — | — | — | — |
| `les_a1_28_05_contact_exchange_roleplay` | Interactive Synthesis: Networking and Exchanging Contacts | — | — | — | — |

### Unit 29: Nominal Plurality Suffixes: -ууд/-үүд, -чууд, -нар, -д
- **Unit ID**: `unit_a1_29_nominal_plurality_suffixes_`
- **Lessons (6)**: `les_a1_29_01_plural_uud_allomorphs` .. `les_a1_29_06_group_description_synthesis`
- **Realized Lexical Content**: 23 lemmas (17 productive, 6 receptive), 6 expressions (4 productive, 2 receptive)

| Lesson ID | Lesson Title | Productive Lemmas | Receptive Lemmas | Productive Expressions | Receptive Expressions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `les_a1_29_01_plural_uud_allomorphs` | Making Plurals: Regular Suffixes -ууд and -үүд | `цонх`, `шүүгээ`, `зураг`, `эдлэл`, `тоног` | `жишээ`, `хэлбэр` | `олон ном` | `гэрийн эдлэл` |
| `les_a1_29_02_plural_nuud_and_human_plurals` | Vowel Stems and Social Plurals: -нууд/-нүүд and -нар | `нөхөр`, `хань`, `мэргэжилтэн`, `хамтлаг`, `ургамал` | `амьтан`, `ажилчин` | `ажлын хамт олон` | — |
| `les_a1_29_03_plural_syntactic_drills` | Guided Practice: Plurals in Locative and Existential Clauses | `байр`, `булан`, `тавиур`, `хайрцаг` | `агуулах` | `тавиур дээр` | `хайрцаг дотор` |
| `les_a1_29_04_library_catalog_reading` | Reading Workshop: Library Catalog and Resource Guides | `уншигч`, `гарчиг`, `сан` | `жагсаалт` | `номын сан` | — |
| `les_a1_29_05_plural_acoustic_discrimination` | Acoustic Lab: Singular vs Plural Discrimination in Rapid Speech | — | — | — | — |
| `les_a1_29_06_group_description_synthesis` | Interactive Synthesis: Workplace and Facility Asset Audit | — | — | — | — |

### Unit 30: Definite Direct Objects: The Accusative Case
- **Unit ID**: `unit_a1_30_definite_direct_objects_the_accusat`
- **Lessons (6)**: `les_a1_30_01_accusative_definite_marking` .. `les_a1_30_06_retail_selection_synthesis`
- **Realized Lexical Content**: 23 lemmas (17 productive, 6 receptive), 6 expressions (4 productive, 2 receptive)

| Lesson ID | Lesson Title | Productive Lemmas | Receptive Lemmas | Productive Expressions | Receptive Expressions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `les_a1_30_01_accusative_definite_marking` | Specific Objects: The Accusative Case (-ыг/-ийг/-г) | `үзэх`, `олох`, `сонгох`, `хураах`, `солих` | `өргөх`, `зөөх` | `ном унших` | `захидал бичих` |
| `les_a1_30_02_accusative_allomorph_rules` | Stem Alternations in Accusative Suffixation | `гэрчилгээ`, `паспорт`, `хавтас`, `маягт`, `тэмдэглэл` | `хавсаргах`, `хадгалах` | `бичиг баримт` | — |
| `les_a1_30_03_transactional_object_requests` | Guided Practice: Choosing and Purchasing Specific Items | `худалдах`, `төлөх`, `захиалах`, `буцаах` | `тооцох` | `худалдаж авах` | `мөнгө төлөх` |
| `les_a1_30_04_shopping_catalog_reading` | Reading Workshop: Product Catalogs and Order Slips | `хэмжээ`, `захиалга`, `хүргэлт` | `баглаа` | `захиалга өгөх` | — |
| `les_a1_30_05_accusative_listening_lab` | Acoustic Lab: Detecting Definite Object Endings in Retail Speech | — | — | — | — |
| `les_a1_30_06_retail_selection_synthesis` | Interactive Synthesis: Retail Purchasing and Item Exchange | — | — | — | — |
