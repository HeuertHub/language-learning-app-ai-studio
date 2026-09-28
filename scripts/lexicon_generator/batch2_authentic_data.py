#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1B Controlled A1 Lexicon Realization — Batch 2 Authentic Mongolian Data
Scope: A1 absolute Units 26 through 30 inclusive.
Total: 112 authentic lemmas (lex_mn_lemma_00404 .. lex_mn_lemma_00515)
       30 authentic expressions (lex_mn_expr_00111 .. lex_mn_expr_00140)

Sources:
- Tsevel, Ya. (1966). Монгол хэлний товч тайлбар толь.
- Luvsanvandan, Sh. (1968). Орчин цагийн монгол хэлний бүтэц.
- Mongolian National Corpus (Монгол хэлний үндэсний корпус, 2021).
- Official Standards (MNS 5283:2014, MNS 5012:2011) and State Laws.
"""

BATCH2_LEMMAS = [
    # -------------------------------------------------------------------------
    # UNIT 26: Question Particles & Pronouns (Lessons 26_01 - 26_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_26_01_content_particles_distribution (P: 5, R: 2) -> 7 lemmas
    ("бэ", "question particle (after sonorants and nasals)", "particle", "neutral", "masculine", "invariable", "STANDARD", "Interrogative question particle in content questions after m, n, ng, l stems.", 1),
    ("вэ", "question particle (after vowels and obstruents)", "particle", "neutral", "masculine", "invariable", "STANDARD", "Interrogative question particle in content questions after vowels and non-nasal consonants.", 1),
    ("хэзээ", "when", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Temporal interrogative pronoun/adverb asking about time of occurrence.", 1),
    ("хаагуур", "which way, through where, along where", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Spatial trajectory interrogative asking about route or path.", 1),
    ("яагаад", "why, for what reason", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Causal interrogative asking for reason, explanation, or cause.", 1),
    ("яах", "to do what, how to act", "verb", "neutral", "masculine", "verbal", "STANDARD", "Interrogative verbal pro-form asking about action or procedure.", 1),
    ("хааш", "whither, where to, in which direction", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Directional interrogative adverb asking about orientation or destination of motion.", 1),

    # les_a1_26_02_interrogative_pronoun_inventory (P: 5, R: 2) -> 7 lemmas
    ("аль", "which, which one", "pronoun", "neutral", "feminine", "nominal", "STANDARD", "Selective interrogative pronoun asking to choose among alternatives.", 1),
    ("ямар", "what kind, what sort, which", "pronoun", "neutral", "masculine", "nominal", "STANDARD", "Qualitative interrogative pronoun asking about attributes, nature, or species.", 1),
    ("яаж", "how, in what manner", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Modal manner adverb interrogative asking about mechanism or method.", 1),
    ("хаанахь", "originating from where, belonging to which place", "pronoun", "neutral", "masculine", "nominal", "STANDARD", "Civic interrogative pronoun inquiring about geographical or jurisdictional provenance.", 1),
    ("ястан", "ethnicity, national subgroup", "noun", "neutral", "masculine", "nominal", "STANDARD", "Civic classification noun denoting nationality or ethnic sub-affiliation in personal profiles.", 1),
    ("хэдий", "how much, how many", "pronoun", "neutral", "feminine", "nominal", "STANDARD", "Quantitative interrogative asking about amount, extent, or degree; inflects to temporal locative хэдийд (at what time, whenabouts).", 1),
    ("хэрхэн", "how, in what manner, by what means", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Procedural interrogative adverb asking about manner, mechanism, or operational approach.", 1),

    # les_a1_26_03_inquiry_clarification_drills (P: 4, R: 1) -> 5 lemmas
    ("ойлгомжтой", "clear, intelligible, understandable", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Evaluative predicate confirming comprehension of an explanation.", 1),
    ("магадлах", "to verify, confirm, ascertain factual accuracy", "verb", "neutral", "masculine", "verbal", "STANDARD", "Action verb for verifying information, checking facts, and confirming accuracy in inquiries.", 1),
    ("асуулга", "questionnaire, survey, interrogation form", "noun", "neutral", "masculine", "nominal", "STANDARD", "Institutional noun denoting structured civic or academic inquiry form.", 1),
    ("тодруулга", "clarification, specification, elucidation", "noun", "neutral", "masculine", "nominal", "STANDARD", "Noun denoting the act or result of making a factual point clear.", 1),
    ("тодорхой", "definite, clear, specific, distinct", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Qualitative adjective expressing clear, unambiguous facts.", 1),

    # les_a1_26_04_interview_transcript_reading (P: 3, R: 1) -> 4 lemmas
    ("анкет", "application form, questionnaire, personal profile", "noun", "neutral", "masculine", "nominal", "STANDARD", "Administrative loanword for biographical survey or visa form.", 1),
    ("өгүүлэл", "article, essay, treatise, narrative", "noun", "neutral", "feminine", "nominal", "STANDARD", "Textual noun denoting short published article or profile narrative.", 1),
    ("агуулга", "content, substance, theme", "noun", "neutral", "masculine", "nominal", "STANDARD", "Noun denoting the semantic or textual content of an interview.", 1),
    ("мэдээлэл", "information, data, news report", "noun", "neutral", "feminine", "nominal", "STANDARD", "Broad informative noun denoting factual details in media profiles.", 1),

    # -------------------------------------------------------------------------
    # UNIT 27: Cardinal Numbers Counting Up to 100 (Lessons 27_01 - 27_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_27_01_cardinal_numerals_1_to_20 (P: 5, R: 2) -> 7 lemmas
    ("хорь", "twenty, 20", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal numeral designating the base decade twenty; has attributive unstable-n stem form хорин used before modified nouns and unit classifiers.", 1),
    ("сондгой", "odd (number), uneven, unpaired", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Mathematical and counting descriptor for odd, non-divisible numbers, paired with тэгш.", 1),
    ("тоолох", "to count, reckon, calculate", "verb", "neutral", "masculine", "verbal", "STANDARD", "Action verb for counting objects, items, or inventory stock.", 1),
    ("ширхэг", "piece, unit, item classifier", "noun", "neutral", "feminine", "nominal", "STANDARD", "Universal counting classifier for discrete manufactured items.", 1),
    ("нийлбэр", "sum, total, aggregate", "noun", "neutral", "feminine", "nominal", "STANDARD", "Mathematical and financial aggregate of added numbers.", 1),
    ("дүн", "total sum, amount, score, result", "noun", "neutral", "masculine", "nominal", "STANDARD", "Financial and numerical total amount on receipts and logs.", 1),
    ("тэгш", "even (number); level, flat, equal", "adjective", "neutral", "feminine", "adjectival", "STANDARD", "Mathematical descriptor for divisible even numbers.", 1),

    # les_a1_27_02_tens_and_counting_to_100 (P: 5, R: 2) -> 7 lemmas
    ("гуч", "thirty, 30", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal decade numeral thirty.", 1),
    ("дөч", "forty, 40", "numeral", "neutral", "feminine", "nominal", "STANDARD", "Cardinal decade numeral forty.", 1),
    ("тавь", "fifty, 50", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal decade numeral fifty.", 1),
    ("жар", "sixty, 60", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal decade numeral sixty.", 1),
    ("зуу", "hundred, 100", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Base centesimal numeral hundred.", 1),
    ("дал", "seventy, 70", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal decade numeral seventy.", 1),
    ("ная", "eighty, 80", "numeral", "neutral", "masculine", "nominal", "STANDARD", "Cardinal decade numeral eighty.", 1),

    # les_a1_27_03_inquiries_with_hed (P: 4, R: 1) -> 5 lemmas
    ("хэд", "how many (bare quantity/price), what number", "numeral", "neutral", "feminine", "nominal", "STANDARD", "Interrogative cardinal numeral asking for quantity; has attributive unstable-n stem form хэдэн (how many, several) and instrumental case form хэдээр (at what price, by how much).", 1),
    ("мөнгө", "money, currency, coin, cash", "noun", "neutral", "feminine", "nominal", "STANDARD", "Core monetary noun denoting currency, coins, and transaction sums in price inquiries.", 1),
    ("ер", "ninety, 90", "numeral", "neutral", "feminine", "nominal", "STANDARD", "Cardinal decade numeral ninety.", 1),
    ("хичнээн", "how much, how many, so much", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Intensive quantitative interrogative asking about amount.", 1),
    ("орчим", "approximately, around, about", "postposition", "neutral", "masculine", "invariable", "STANDARD", "Approximative postposition following numerical expressions.", 1),

    # les_a1_27_04_inventory_sheet_reading (P: 3, R: 1) -> 4 lemmas
    ("нийт", "total, gross, aggregate, altogether", "noun", "neutral", "feminine", "nominal", "STANDARD", "Commercial and inventory aggregate denoting entire count.", 1),
    ("бүртгэл", "registration, record, inventory sheet", "noun", "neutral", "feminine", "nominal", "STANDARD", "Official accounting registry of assets and supplies.", 1),
    ("үлдэгдэл", "remainder, remnant, stock balance", "noun", "neutral", "feminine", "nominal", "STANDARD", "Warehouse and accounting balance of remaining goods.", 1),
    ("хэмжих", "to measure, weigh, gauge", "verb", "neutral", "feminine", "verbal", "STANDARD", "Operational verb for determining physical dimensions or quantities.", 1),

    # -------------------------------------------------------------------------
    # UNIT 28: Telephone & Digital Contacts (Lessons 28_01 - 28_03) - 20 lemmas
    # -------------------------------------------------------------------------
    # les_a1_28_01_telephone_digit_pairing (P: 5, R: 2) -> 7 lemmas
    ("дугаар", "number, phone number, ordinal code", "noun", "neutral", "masculine", "nominal", "STANDARD", "Numerical identifier used for phone lines, rooms, and vehicles.", 1),
    ("холбогдох", "to contact, connect, get in touch with", "verb", "neutral", "masculine", "verbal", "STANDARD", "Reciprocal/passive verb for telephone and digital communication.", 1),
    ("залгах", "to dial, call, phone, connect", "verb", "neutral", "masculine", "verbal", "STANDARD", "Core telecommunication verb for placing a phone call.", 1),
    ("үүрэн", "cellular, mobile", "adjective", "neutral", "feminine", "nominal", "STANDARD", "Attributive adjective specifying cellular/mobile network telephony.", 1),
    ("сануулах", "to remind, prompt, alert", "verb", "neutral", "masculine", "verbal", "STANDARD", "Communication verb for prompting a contact or follow-up note.", 1),
    ("унтраах", "to switch off, turn off, shut down", "verb", "neutral", "masculine", "verbal", "STANDARD", "Operational verb for turning off mobile phones in civic venues.", 1),
    ("асаах", "to turn on, switch on, power up", "verb", "neutral", "masculine", "verbal", "STANDARD", "Operational verb for activating electronic communication devices.", 1),

    # les_a1_28_02_digital_channels_email_social (P: 5, R: 2) -> 7 lemmas
    ("цахим", "electronic, digital, cyber", "adjective", "neutral", "masculine", "nominal", "STANDARD", "Modern technical adjective for digital services and communications.", 1),
    ("мессеж", "text message, SMS, digital message", "noun", "neutral", "feminine", "nominal", "STANDARD", "Everyday loanword for short messaging and chat communications.", 1),
    ("сүлжээ", "network, web, cellular coverage", "noun", "neutral", "feminine", "nominal", "STANDARD", "Telecommunication and internet infrastructure network.", 1),
    ("код", "code, PIN code, digital passcode, dial code", "noun", "neutral", "masculine", "nominal", "STANDARD", "Numerical security or routing code in digital communication.", 1),
    ("товчлуур", "key, button, keypad button", "noun", "neutral", "masculine", "nominal", "STANDARD", "Physical or on-screen keypad button on phones and terminals.", 1),
    ("нээх", "to open, launch, create (account/app)", "verb", "neutral", "feminine", "verbal", "STANDARD", "Action verb for opening applications, accounts, or channels.", 1),
    ("хаах", "to close, shut down, exit (app/call)", "verb", "neutral", "masculine", "verbal", "STANDARD", "Action verb for closing applications or terminating calls.", 1),

    # les_a1_28_03_business_card_reading (P: 5, R: 1) -> 6 lemmas
    ("тушаал", "order, command; official post, rank, position", "noun", "neutral", "masculine", "nominal", "STANDARD", "Official post, organizational title, or administrative order.", 1),
    ("байршил", "location, premises, site address", "noun", "neutral", "masculine", "nominal", "STANDARD", "Civic geographical noun specifying institutional location.", 1),
    ("салбар", "branch, subsidiary, division, chapter", "noun", "neutral", "masculine", "nominal", "STANDARD", "Organizational noun denoting regional or departmental branch office.", 1),
    ("факс", "facsimile, fax machine/line", "noun", "neutral", "masculine", "nominal", "STANDARD", "Telecommunication office line identifier on business cards.", 1),
    ("хэлтэс", "department, division, administrative section", "noun", "neutral", "feminine", "nominal", "STANDARD", "Organizational sub-unit in corporate and government rosters.", 1),
    ("холбоо", "connection, link, relation, communication", "noun", "neutral", "masculine", "nominal", "STANDARD", "Contact and communication connection in professional directories.", 1),

    # -------------------------------------------------------------------------
    # UNIT 29: Nominal Plurality Suffixes (Lessons 29_01 - 29_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_29_01_plural_uud_allomorphs (P: 5, R: 2) -> 7 lemmas
    ("цонх", "window", "noun", "neutral", "masculine", "nominal", "STANDARD", "Architectural noun illustrating regular plural suffixation (цонхнууд).", 1),
    ("шүүгээ", "cabinet, cupboard, wardrobe, locker", "noun", "neutral", "feminine", "nominal", "STANDARD", "Domestic furnishing noun taking regular plural -нүүд.", 1),
    ("зураг", "picture, photograph, painting, drawing", "noun", "neutral", "masculine", "nominal", "STANDARD", "Visual cultural object noun taking regular plural -ууд (зургууд).", 1),
    ("эдлэл", "manufactured goods, furniture piece, artifact", "noun", "neutral", "feminine", "nominal", "STANDARD", "Product noun taking regular plural -үүд.", 1),
    ("тоног", "equipment, gear, apparatus, fittings", "noun", "neutral", "masculine", "nominal", "STANDARD", "Technical equipment noun taking regular plural -ууд.", 1),
    ("жишээ", "example, illustration, sample", "noun", "neutral", "feminine", "nominal", "STANDARD", "Pedagogical noun denoting exemplary grammatical instances.", 1),
    ("хэлбэр", "form, shape, grammatical variant", "noun", "neutral", "feminine", "nominal", "STANDARD", "Morphological and physical shape noun.", 1),

    # les_a1_29_02_plural_nuud_and_human_plurals (P: 5, R: 2) -> 7 lemmas
    ("нөхөр", "colleague, companion, friend, spouse", "noun", "neutral", "feminine", "nominal", "STANDARD", "Social noun taking irregular human plural suffix -өд (нөхөд).", 1),
    ("хань", "companion, partner, friend, spouse", "noun", "neutral", "masculine", "nominal", "STANDARD", "Intimate social partner noun taking collective plural нар.", 1),
    ("мэргэжилтэн", "specialist, professional, expert", "noun", "neutral", "feminine", "nominal", "STANDARD", "Professional noun taking plural -үүд / -нүүд.", 1),
    ("хамтлаг", "group, team, band, ensemble", "noun", "neutral", "masculine", "nominal", "STANDARD", "Collective noun denoting musical or collaborative ensemble.", 1),
    ("ургамал", "plant, flora, vegetation", "noun", "neutral", "masculine", "nominal", "STANDARD", "Biological collective noun taking plural -ууд.", 1),
    ("амьтан", "animal, living creature, fauna", "noun", "neutral", "masculine", "nominal", "STANDARD", "Biological collective noun taking plural -д / -ууд (амьтад).", 1),
    ("ажилчин", "worker, laborer, factory hand", "noun", "neutral", "masculine", "nominal", "STANDARD", "Manual trade laborer noun taking plural -д / -ууд.", 1),

    # les_a1_29_03_plural_syntactic_drills (P: 4, R: 1) -> 5 lemmas
    ("байр", "building, residential block, quarters, premises", "noun", "neutral", "masculine", "nominal", "STANDARD", "Spatial noun frequent in campus and residential locative plurals.", 1),
    ("булан", "corner, nook, angle", "noun", "neutral", "masculine", "nominal", "STANDARD", "Spatial architectural noun hosting objects in room corners.", 1),
    ("тавиур", "shelf, rack, stand, bookshelf", "noun", "neutral", "masculine", "nominal", "STANDARD", "Domestic/office storage furniture taking locative plurals.", 1),
    ("хайрцаг", "box, carton, chest, crate", "noun", "neutral", "masculine", "nominal", "STANDARD", "Storage container noun hosting plural supplies.", 1),
    ("агуулах", "warehouse, storage room, depot", "noun", "neutral", "masculine", "nominal", "STANDARD", "Facility noun housing collective plural inventories.", 1),

    # les_a1_29_04_library_catalog_reading (P: 3, R: 1) -> 4 lemmas
    ("уншигч", "reader, patron, library user", "noun", "neutral", "feminine", "nominal", "STANDARD", "Human user noun frequent in library catalog and loan guides.", 1),
    ("гарчиг", "title, heading, table of contents", "noun", "neutral", "masculine", "nominal", "STANDARD", "Bibliographic noun denoting chapter or book title.", 1),
    ("сан", "fund, treasury, repository, library collection", "noun", "neutral", "masculine", "nominal", "STANDARD", "Institutional noun forming component of library compound.", 1),
    ("жагсаалт", "list, register, roll, catalog roster", "noun", "neutral", "masculine", "nominal", "STANDARD", "Systematic itemized bibliographic and inventory register.", 1),

    # -------------------------------------------------------------------------
    # UNIT 30: Definite Direct Objects & Accusative Case (Lessons 30_01 - 30_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_30_01_accusative_definite_marking (P: 5, R: 2) -> 7 lemmas
    ("үзэх", "to view, watch, examine, inspect, see", "verb", "neutral", "feminine", "verbal", "STANDARD", "Core transitive sensory verb taking definite accusative object.", 1),
    ("олох", "to find, discover, acquire, locate", "verb", "neutral", "masculine", "verbal", "STANDARD", "Transitive verb taking definite direct object in search contexts.", 1),
    ("сонгох", "to choose, select, pick", "verb", "neutral", "masculine", "verbal", "STANDARD", "Transitive decision verb governing specific accusative target.", 1),
    ("хураах", "to collect, gather, harvest", "verb", "neutral", "masculine", "verbal", "STANDARD", "Transitive verb for gathering items, fees, or documents.", 1),
    ("солих", "to exchange, swap, replace, trade", "verb", "neutral", "masculine", "verbal", "STANDARD", "Commercial and retail transaction verb governing traded object.", 1),
    ("өргөх", "to lift, raise, elevate", "verb", "neutral", "feminine", "verbal", "STANDARD", "Physical handling transitive verb taking direct object.", 1),
    ("зөөх", "to carry, transport, move", "verb", "neutral", "feminine", "verbal", "STANDARD", "Physical handling and transit verb for shifting furniture/assets.", 1),

    # les_a1_30_02_accusative_allomorph_rules (P: 5, R: 2) -> 7 lemmas
    ("гэрчилгээ", "certificate, credential, license", "noun", "neutral", "feminine", "nominal", "STANDARD", "Official document noun illustrating vowel-stem accusative (-г).", 1),
    ("паспорт", "passport, identity booklet", "noun", "neutral", "masculine", "nominal", "STANDARD", "Civic identity noun illustrating consonant-stem accusative (-ыг).", 1),
    ("хавтас", "folder, binder, book cover", "noun", "neutral", "masculine", "nominal", "STANDARD", "Office stationery noun taking accusative -ыг.", 1),
    ("маягт", "form, blank, application sheet", "noun", "neutral", "masculine", "nominal", "STANDARD", "Administrative document blank taking accusative -ыг.", 1),
    ("тэмдэглэл", "notes, memorandum, diary entry", "noun", "neutral", "feminine", "nominal", "STANDARD", "Written textual record taking accusative -ийг.", 1),
    ("хавсаргах", "to attach, enclose, append", "verb", "neutral", "masculine", "verbal", "STANDARD", "Administrative action verb for attaching document to petition.", 1),
    ("хадгалах", "to keep, store, save, preserve", "verb", "neutral", "masculine", "verbal", "STANDARD", "Custodial verb for safeguarding documents or valuables.", 1),

    # les_a1_30_03_transactional_object_requests (P: 4, R: 1) -> 5 lemmas
    ("худалдах", "to sell, vend", "verb", "neutral", "masculine", "verbal", "STANDARD", "Commercial transaction verb contrasting with buying.", 1),
    ("төлөх", "to pay, settle payment", "verb", "neutral", "feminine", "verbal", "STANDARD", "Financial transaction verb governing fee/money direct object.", 1),
    ("захиалах", "to order, reserve, book", "verb", "neutral", "masculine", "verbal", "STANDARD", "Transactional verb for ordering goods, services, or books.", 1),
    ("буцаах", "to return, give back, refund", "verb", "neutral", "masculine", "verbal", "STANDARD", "Retail customer service verb for returning merchandise.", 1),
    ("тооцох", "to calculate, charge, consider, reckon", "verb", "neutral", "masculine", "verbal", "STANDARD", "Accounting verb for billing or computing transactional totals.", 1),

    # les_a1_30_04_shopping_catalog_reading (P: 3, R: 1) -> 4 lemmas
    ("хэмжээ", "size, dimension, measure, quantity", "noun", "neutral", "feminine", "nominal", "STANDARD", "Product attribute noun in retail catalogs and clothing orders.", 1),
    ("захиалга", "order, reservation, requisition", "noun", "neutral", "masculine", "nominal", "STANDARD", "Commercial purchase order noun taking accusative suffix.", 1),
    ("хүргэлт", "delivery, shipping service", "noun", "neutral", "feminine", "nominal", "STANDARD", "Logistical shipping service noun in commercial catalogs.", 1),
    ("баглаа", "package, bundle, bouquet, parcel", "noun", "neutral", "masculine", "nominal", "STANDARD", "Retail parcel noun denoting packaged purchases.", 1),
]

BATCH2_EXPRESSIONS = [
    # -------------------------------------------------------------------------
    # UNIT 26: Question Expressions (Lessons 26_01 - 26_04) - 6 expressions
    # -------------------------------------------------------------------------
    # les_a1_26_01 (P: 1, R: 1)
    ("хэзээ ирэх вэ", "when will [you/it] come?", "formula", "neutral", [2, -1, 1], "Core interrogative formula asking about expected arrival."),
    ("яагаад гэвэл", "because, that is why", "collocation", "neutral", [4], "Discourse causal conjunction connecting explanatory clause."),

    # les_a1_26_02 (P: 1, R: 0)
    ("ямар учиртай вэ", "what is the reason / what does it mean?", "formula", "neutral", [8, -1, 1], "Inquiry formula asking for the underlying justification or reason."),

    # les_a1_26_03 (P: 1, R: 1)
    ("дахин хэлнэ үү", "please say it again", "formula", "neutral", [-1], "Polite clarification request formula in acoustic and instructional encounters."),
    ("асуулт тавих", "to ask/raise a question", "collocation", "neutral", [-1, -1], "Collocation for posing a question in formal or educational discourse."),

    # les_a1_26_04 (P: 1, R: 0)
    ("асуултад хариулах", "to answer a question", "collocation", "neutral", [-1, -1], "Verb-phrase collocation for responding to inquiries or interviews."),

    # -------------------------------------------------------------------------
    # UNIT 27: Counting & Quantity Expressions (Lessons 27_01 - 27_04) - 6 expressions
    # -------------------------------------------------------------------------
    # les_a1_27_01 (P: 1, R: 1)
    ("арван хоёр", "twelve, 12", "collocation", "neutral", [-1, -1], "Compound cardinal numeral expression."),
    ("тоо тоолох", "to count numbers", "collocation", "neutral", [-1, 25], "Cognate object verbal collocation for arithmetic counting."),

    # les_a1_27_02 (P: 1, R: 0)
    ("хорин тав", "twenty-five, 25", "collocation", "neutral", [24, -1], "Compound cardinal numeral combining base decade and five."),

    # les_a1_27_03 (P: 1, R: 1)
    ("хэдэн настай вэ", "how old are you?", "formula", "neutral", [38, -1, 1], "Standard social question formula inquiring about biological age."),
    ("хэдэн төгрөг вэ", "how many tugriks / how much is it?", "formula", "neutral", [38, -1, 1], "Everyday transactional question formula for monetary price."),

    # les_a1_27_04 (P: 1, R: 0)
    ("нийт дүн", "total sum / aggregate amount", "collocation", "neutral", [42, 28], "Financial and accounting ledger collocation for overall total."),

    # -------------------------------------------------------------------------
    # UNIT 28: Telephone & Digital Expressions (Lessons 28_01 - 28_03) - 6 expressions
    # -------------------------------------------------------------------------
    # les_a1_28_01 (P: 1, R: 1)
    ("утасны дугаар", "telephone number", "collocation", "neutral", [-1, 46], "Genitive compound noun specifying telecommunication number."),
    ("утсаар ярих", "to speak on the phone", "collocation", "neutral", [-1, -1], "Instrumental case verbal phrase for telephone conversation."),

    # les_a1_28_02 (P: 1, R: 0)
    ("цахим шуудан", "electronic mail, email", "collocation", "neutral", [53, -1], "Standard terminology for digital email service."),

    # les_a1_28_03 (P: 2, R: 1)
    ("нэрийн хуудас", "business card, calling card", "collocation", "neutral", [-1, -1], "Standard compound for professional visiting and contact card."),
    ("албан тушаал", "job title, official position", "collocation", "neutral", [-1, -1], "Civic and corporate terminology for organizational role."),
    ("холбоо барих", "to keep in contact / get in touch", "collocation", "neutral", [-1, -1], "Standard phrase for initiating or maintaining communication."),

    # -------------------------------------------------------------------------
    # UNIT 29: Nominal Plurality Expressions (Lessons 29_01 - 29_04) - 6 expressions
    # -------------------------------------------------------------------------
    # les_a1_29_01 (P: 1, R: 1)
    ("олон ном", "many books", "collocation", "neutral", [-1, -1], "Quantified noun phrase illustrating bare singular after олон."),
    ("гэрийн эдлэл", "household furniture / domestic goods", "collocation", "neutral", [-1, 69], "Domestic goods compound phrase taking plural forms."),

    # les_a1_29_02 (P: 1, R: 0)
    ("ажлын хамт олон", "workplace colleagues / staff collective", "collocation", "neutral", [-1, -1, -1], "Collective social phrase for workplace coworkers."),

    # les_a1_29_03 (P: 1, R: 1)
    ("тавиур дээр", "on the shelf", "collocation", "neutral", [82, -1], "Locative postpositional phrase indicating spatial positioning."),
    ("хайрцаг дотор", "inside the box", "collocation", "neutral", [83, -1], "Locative postpositional phrase indicating internal enclosure."),

    # les_a1_29_04 (P: 1, R: 0)
    ("номын сан", "library", "collocation", "neutral", [-1, 87], "Core civic institutional compound for library repository."),

    # -------------------------------------------------------------------------
    # UNIT 30: Accusative Definite Expressions (Lessons 30_01 - 30_04) - 6 expressions
    # -------------------------------------------------------------------------
    # les_a1_30_01 (P: 1, R: 1)
    ("ном унших", "to read a book", "collocation", "neutral", [-1, -1], "Transitive verb-object collocation."),
    ("захидал бичих", "to write a letter", "collocation", "neutral", [-1, -1], "Transitive verb-object collocation."),

    # les_a1_30_02 (P: 1, R: 0)
    ("бичиг баримт", "identification documents / official paperwork", "collocation", "neutral", [-1, -1], "Paired noun phrase for civil credentials and paperwork."),

    # les_a1_30_03 (P: 1, R: 1)
    ("худалдаж авах", "to purchase, buy", "collocation", "neutral", [103, -1], "Compound converb verbal construction for commercial buying."),
    ("мөнгө төлөх", "to pay money", "collocation", "neutral", [-1, 104], "Transactional verb-object collocation."),

    # les_a1_30_04 (P: 1, R: 0)
    ("захиалга өгөх", "to place an order", "collocation", "neutral", [109, -1], "Standard commercial collocation for submitting a purchase order."),
]

assert len(BATCH2_LEMMAS) == 112, f"Expected 112 lemmas, got {len(BATCH2_LEMMAS)}"
assert len(BATCH2_EXPRESSIONS) == 30, f"Expected 30 expressions, got {len(BATCH2_EXPRESSIONS)}"
