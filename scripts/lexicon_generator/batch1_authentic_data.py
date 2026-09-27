#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3C.1A Controlled A1 Lexicon Realization — Batch 1 Authentic Mongolian Data
Scope: A1 absolute Units 21 through 25 inclusive.
Total: 117 authentic lemmas (lex_mn_lemma_00287 .. lex_mn_lemma_00403)
       33 authentic expressions (lex_mn_expr_00078 .. lex_mn_expr_00110)

Sources:
- Tsevel, Ya. (1966). Монгол хэлний товч тайлбар толь.
- Luvsanvandan, Sh. (1968). Орчин цагийн монгол хэлний зүй.
- Mongolian National Corpus (Монгол хэлний үндэсний корпус, 2021).
- Official Standards (MNS 5012:2011, MNS 5283:2014) and State Laws.
"""

BATCH1_LEMMAS = [
    # -------------------------------------------------------------------------
    # UNIT 21: Nominal Negation (Lessons 21_01 - 21_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_21_01_nominal_negation_particle_bish (P: 5, R: 2) -> 7 lemmas
    ("сувилагч", "nurse", "noun", "neutral", "masculine", "nominal", "STANDARD", "Healthcare professional role commonly contrasted with physician in medical settings.", 1),
    ("хуульч", "lawyer, jurist, legal counsel", "noun", "neutral", "masculine", "nominal", "STANDARD", "Legal professional title in workplace and civic contexts.", 1),
    ("дарга", "director, chief, head, boss", "noun", "neutral", "masculine", "nominal", "STANDARD", "Organizational leadership title frequent in workplace dialogue.", 1),
    ("барилгачин", "construction worker, builder", "noun", "neutral", "masculine", "nominal", "STANDARD", "Technical manual trade profession in urban development.", 1),
    ("худалдагч", "salesperson, shop clerk, cashier", "noun", "neutral", "masculine", "nominal", "STANDARD", "Commercial retail service role frequent in shopping dialogues.", 1),
    ("нягтлан", "accountant, bookkeeper", "noun", "neutral", "masculine", "nominal", "STANDARD", "Financial administrative profession in organizational contexts.", 1),
    ("менежер", "manager, administrative coordinator", "noun", "neutral", "masculine", "nominal", "STANDARD", "Modern corporate and hospitality administrative loanword.", 1),

    # les_a1_21_02_correcting_false_assumptions_clarification (P: 5, R: 2) -> 7 lemmas
    ("харин", "but, on the contrary, however, whereas", "conjunction", "neutral", "masculine", "invariable", "STANDARD", "Contrastive coordinating discourse connective introducing correction.", 1),
    ("англи", "English, Briton, British", "noun", "neutral", "masculine", "nominal", "STANDARD", "Nationality and language descriptor frequent in introductory clarification.", 1),
    ("герман", "German", "noun", "neutral", "masculine", "nominal", "STANDARD", "European nationality and origin term in international communication.", 1),
    ("франц", "French", "noun", "neutral", "masculine", "nominal", "STANDARD", "European nationality descriptor in educational and diplomatic rosters.", 1),
    ("буруу", "wrong, incorrect, mistaken", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Evaluative descriptor used in factual and linguistic correction.", 1),
    ("казах", "Kazakh", "noun", "neutral", "masculine", "nominal", "STANDARD", "Major indigenous ethnic minority nationality in Western Mongolia.", 1),
    ("польш", "Polish, Pole", "noun", "neutral", "masculine", "nominal", "STANDARD", "Central European nationality in student and diplomatic rosters.", 1),

    # les_a1_21_03_negative_polar_questions_bish_uu (P: 4, R: 1) -> 5 lemmas
    ("магадгүй", "perhaps, maybe, probably", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Epistemic modal adverb expressing possibility or tentative inference.", 1),
    ("үнэхээр", "truly, really, indeed, actually", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Intensifying confirmation adverb used in polar inquiries.", 1),
    ("захирал", "executive director, general manager, principal", "noun", "neutral", "masculine", "nominal", "STANDARD", "Executive leadership title in schools and corporate institutions.", 1),
    ("зөвхөн", "only, solely, exclusively", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Restrictive particle adverb used in identity delineation.", 1),
    ("мэдээж", "of course, naturally, certainly", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Evidential conversational discourse adverb confirming shared knowledge.", 1),

    # les_a1_21_04_reading_lost_and_found_notices (P: 3, R: 1) -> 4 lemmas
    ("цүнх", "bag, briefcase, backpack, satchel", "noun", "neutral", "masculine", "nominal", "STANDARD", "Everyday portable personal item frequent in lost-and-found notices.", 1),
    ("түлхүүр", "key", "noun", "neutral", "feminine", "nominal", "STANDARD", "Crucial security and domestic item frequent in property notices.", 1),
    ("түрийвч", "wallet, purse, billfold", "noun", "neutral", "feminine", "nominal", "STANDARD", "Essential monetary receptacle item in civic property administration.", 1),
    ("гээх", "to lose, misplace, drop", "verb", "neutral", "feminine", "verbal", "STANDARD", "Core transitive verbal root for losing property in public spaces.", 1),

    # -------------------------------------------------------------------------
    # UNIT 22: Formal Departure & Gratitude (Lessons 22_01 - 22_04) - 20 lemmas
    # -------------------------------------------------------------------------
    # les_a1_22_01_formal_departure_formulas_bayartai (P: 5, R: 2) -> 7 lemmas
    ("баяртай", "goodbye, farewell", "interjection", "neutral", "masculine", "invariable", "STANDARD", "Universal parting formula used across formal and informal registers.", 1),
    ("дараа", "after, later, next, afterward", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Temporal adverb used in parting promises of future encounter.", 1),
    ("амрах", "to rest, relax, take a vacation, sleep", "verb", "neutral", "masculine", "verbal", "STANDARD", "Action verb describing evening and leisure rest.", 1),
    ("сайхан", "fine, pleasant, good, beautiful", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Qualitative adjective central to well-wishing benedictions.", 1),
    ("маргааш", "tomorrow", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Deictic temporal adverb specifying next-day re-encounter.", 1),
    ("үдэш", "evening, twilight, dusk", "noun", "neutral", "feminine", "nominal", "STANDARD", "Temporal noun denoting late afternoon and evening interval.", 1),
    ("түр", "briefly, temporarily, for a while", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Aspectual adverb of short duration modifying parting routines.", 1),

    # les_a1_22_02_gratitude_formulas_ih_bayarlalaa (P: 5, R: 2) -> 7 lemmas
    ("баярлах", "to rejoice, be glad, thank", "verb", "neutral", "masculine", "verbal", "STANDARD", "Cognitive and emotive verb forming the morphological base of gratitude formulas.", 1),
    ("их", "much, great, very, large", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Intensifying quantitative adjective and adverb modifying expressions of thanks.", 1),
    ("маш", "very, extremely, highly", "adverb", "neutral", "masculine", "invariable", "STANDARD", "Preposed intensifying adverb indicating high degree.", 1),
    ("зүгээр", "fine, okay, nothing, no problem", "adjective", "neutral", "feminine", "adjectival", "STANDARD", "Conversational response formula demoting obligation in gratitude contexts.", 1),
    ("туслах", "to help, assist, aid", "verb", "neutral", "masculine", "verbal", "STANDARD", "Core transitive social cooperation verb motivating gratitude.", 1),
    ("гялайх", "to be thankful, rejoice, be pleased", "verb", "formal", "masculine", "verbal", "STANDARD", "Traditional verbal root expressing heartfelt appreciation in polite register.", 1),
    ("баяр", "joy, celebration, holiday, festival", "noun", "neutral", "masculine", "nominal", "STANDARD", "Nominal root denoting festive joy and gratefulness.", 1),

    # les_a1_22_03_reading_farewell_cards_email_signoffs (P: 3, R: 1) -> 4 lemmas
    ("захидал", "letter, missive, written correspondence", "noun", "neutral", "masculine", "nominal", "STANDARD", "Epistolary text type central to written greetings and departures.", 1),
    ("хүсэх", "to wish, desire, request, aspire", "verb", "neutral", "feminine", "verbal", "STANDARD", "Optative volitional verb framing parting wishes and benedictions.", 1),
    ("илгээх", "to send, dispatch, forward, transmit", "verb", "neutral", "feminine", "verbal", "STANDARD", "Communicative action verb for mailing correspondence and email.", 1),
    ("дугтуй", "envelope, wrapper", "noun", "neutral", "masculine", "nominal", "STANDARD", "Postal receptacle noun in formal correspondence.", 1),

    # les_a1_22_04_hotel_checkout_office_departure_roleplay (P: 2, R: 0) -> 2 lemmas
    ("тооцоо", "calculation, bill, invoice, settlement", "noun", "neutral", "masculine", "nominal", "STANDARD", "Commercial and hospitality account settlement noun.", 1),
    ("хуудас", "page, sheet, form, folium", "noun", "neutral", "masculine", "nominal", "STANDARD", "Administrative document page or checkout folio.", 1),

    # -------------------------------------------------------------------------
    # UNIT 23: Section Synthesis & Social Reception (Lessons 23_01 - 23_04) - 28 lemmas
    # -------------------------------------------------------------------------
    # les_a1_23_01_social_reception_greeting_and_entry (P: 7, R: 3) -> 10 lemmas
    ("зочин", "guest, visitor", "noun", "neutral", "masculine", "nominal", "STANDARD", "Core hospitality participant noun in household and official reception.", 1),
    ("морилох", "to proceed, visit, come (honorific)", "verb", "formal", "masculine", "verbal", "STANDARD", "High-respect honorific motion verb used to welcome guests.", 1),
    ("тавтай", "comfortably, pleasantly, welcome", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Hospitality modifier expressing comfort and welcoming atmosphere.", 1),
    ("дээшээ", "upward, toward the place of honor", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Spatial directive adverb inviting guests to the northern place of honor (khoimor).", 1),
    ("урих", "to invite, bid welcome, summon", "verb", "neutral", "masculine", "verbal", "STANDARD", "Social action verb for convening guests and hospitality offers.", 1),
    ("хоймор", "place of honor (north side of ger/room opposite door)", "noun", "neutral", "masculine", "nominal", "STANDARD", "Culturally sacred spatial seat of respect reserved for elders and guests.", 1),
    ("босго", "threshold, doorstep, sill", "noun", "neutral", "masculine", "nominal", "STANDARD", "Architectural entrance boundary governed by cultural respect protocols.", 1),
    ("гийчин", "guest, traveler, sojourner", "noun", "formal", "masculine", "nominal", "STANDARD", "Traditional literary and formal synonym for guest or traveler.", 1),
    ("айлчлах", "to pay a visit, call on, make a formal visit", "verb", "neutral", "masculine", "verbal", "STANDARD", "Sociolinguistic verb for guest visits between households or states.", 1),
    ("хүндэт", "honored, respected, venerable, dear", "adjective", "formal", "masculine", "adjectival", "STANDARD", "Honorific epistolary and social address attribute.", 1),

    # les_a1_23_02_social_reception_introductions_and_origin (P: 7, R: 3) -> 10 lemmas
    ("сум", "district, sum (rural administrative unit)", "noun", "neutral", "masculine", "nominal", "STANDARD", "Primary administrative sub-unit of a Mongolian province (aimag).", 1),
    ("бүс", "zone, region, belt, territory", "noun", "neutral", "feminine", "nominal", "STANDARD", "Geographic and economic regional subdivision noun.", 1),
    ("газар", "place, locality, land, ground", "noun", "neutral", "masculine", "nominal", "STANDARD", "Fundamental spatial noun specifying territory or geographical origin.", 1),
    ("тосгон", "village, settlement, rural township", "noun", "neutral", "masculine", "nominal", "STANDARD", "Rural population center and settlement denomination.", 1),
    ("уугуул", "native, indigenous, aboriginal, native-born", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Sociocultural descriptor denoting indigenous or birthplace identity.", 1),
    ("хөрш", "neighbor, adjacent resident", "noun", "neutral", "feminine", "nominal", "STANDARD", "Social relationship noun in residential communities.", 1),
    ("бүл", "family member, clan, household member", "noun", "neutral", "feminine", "nominal", "STANDARD", "Kinship and family composition noun.", 1),
    ("дипломат", "diplomat, diplomatic agent", "noun", "formal", "masculine", "nominal", "STANDARD", "Official international relations representative in diplomatic vignettes.", 1),
    ("алба", "official duty, service, state bureau, office", "noun", "formal", "masculine", "nominal", "STANDARD", "Public and civic administrative institutional duty noun.", 1),
    ("иргэн", "citizen, national, civilian", "noun", "neutral", "masculine", "nominal", "STANDARD", "Constitutional civil status noun in personal identification.", 1),

    # les_a1_23_03_social_reception_clarification_and_inquiry (P: 4, R: 1) -> 5 lemmas
    ("хэл", "language, tongue, speech", "noun", "neutral", "feminine", "nominal", "STANDARD", "Foundational linguistic noun in language ability inquiries.", 1),
    ("ярих", "to speak, talk, converse", "verb", "neutral", "masculine", "verbal", "STANDARD", "Core communicative action verb for spoken interaction.", 1),
    ("давтах", "to repeat, reiterate, practice, review", "verb", "neutral", "masculine", "verbal", "STANDARD", "Classroom and conversational clarification verb.", 1),
    ("хариулт", "answer, reply, response", "noun", "neutral", "masculine", "nominal", "STANDARD", "Communicative response noun paired with questions.", 1),
    ("тайлбарлах", "to explain, clarify, interpret, expound", "verb", "neutral", "masculine", "verbal", "STANDARD", "Pedagogical and conversational clarification verb.", 1),

    # les_a1_23_04_reading_complete_social_vignette (P: 2, R: 1) -> 3 lemmas
    ("түүх", "history, story, chronicle, narrative", "noun", "neutral", "feminine", "nominal", "STANDARD", "Narrative genre noun in comprehensive reading vignettes.", 1),
    ("ярилцлага", "interview, dialogue, conversation, discussion", "noun", "neutral", "masculine", "nominal", "STANDARD", "Structured conversational exchange noun in media and civic contexts.", 1),
    ("ёслол", "ceremony, ritual, formal observance, protocol", "noun", "formal", "masculine", "nominal", "STANDARD", "Formal reception protocol and state etiquette noun.", 1),

    # -------------------------------------------------------------------------
    # UNIT 24: Existential Assertion vs Negation (Lessons 24_01 - 24_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_24_01_existential_assertion_baina (P: 5, R: 2) -> 7 lemmas
    ("ор", "bed, couch, berth", "noun", "neutral", "masculine", "nominal", "STANDARD", "Primary domestic sleeping furniture item in ger and modern homes.", 1),
    ("зуух", "stove, hearth, furnace", "noun", "neutral", "masculine", "nominal", "STANDARD", "Central heating and cooking hearth of the traditional ger.", 1),
    ("авдар", "trunk, chest, wooden coffer", "noun", "neutral", "masculine", "nominal", "STANDARD", "Traditional carved wooden storage chest placed on northern perimeter.", 1),
    ("тооно", "toono, circular roof crown, smoke ring", "noun", "neutral", "masculine", "nominal", "STANDARD", "Central architectural roof ring permitting light and smoke egress in ger.", 1),
    ("багана", "pillar, post, central roof support column", "noun", "neutral", "masculine", "nominal", "STANDARD", "Structural twin columns supporting the toono crown of the ger.", 1),
    ("шал", "floor, flooring", "noun", "neutral", "masculine", "nominal", "STANDARD", "Interior floor foundation of buildings and floored gers.", 1),
    ("хана", "wall, lattice wall (hana) of ger", "noun", "neutral", "masculine", "nominal", "STANDARD", "Structural folding lattice wall section defining ger perimeter.", 1),

    # les_a1_24_02_existential_negation_baihgui (P: 5, R: 2) -> 7 lemmas
    ("байхгүй", "absent, there is no, nonexistent, unavailable", "particle", "neutral", "masculine", "invariable", "STANDARD", "Negative existential predicate particle contrasting with copular bish.", 1),
    ("алга", "absent, missing, there is none (conversational)", "adjective", "informal", "masculine", "adjectival", "STANDARD", "Spoken existential negative equivalent to baihgui denoting immediate visual absence.", 1),
    ("цаас", "paper, sheet of paper", "noun", "neutral", "masculine", "nominal", "STANDARD", "Basic office and stationery consumable in inventory checks.", 1),
    ("талх", "bread, loaf of bread", "noun", "neutral", "masculine", "nominal", "STANDARD", "Essential bakery food staple in household kitchen inventory.", 1),
    ("давс", "salt, table salt", "noun", "neutral", "masculine", "nominal", "STANDARD", "Primary condiment mineral staple in culinary inventory.", 1),
    ("хоосон", "empty, vacant, hollow, unoccupied", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Qualitative adjective describing depleted containers or vacant spaces.", 1),
    ("хомс", "scarce, meager, lacking, insufficient", "adjective", "formal", "masculine", "adjectival", "STANDARD", "Evaluative adjective denoting resource scarcity or shortage.", 1),

    # les_a1_24_03_polar_inquiries_existence (P: 4, R: 1) -> 5 lemmas
    ("бэлэн", "ready, prepared, available, on hand", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Readiness and immediate availability predicate in polar inquiries; e.g. өрөө бэлэн, бэлэн байна.", 1),
    ("чөлөөтэй", "free, vacant, unoccupied, unconstrained", "adjective", "neutral", "feminine", "adjectival", "STANDARD", "Attribute for vacant hotel rooms, open seats, or free schedules.", 1),
    ("зав", "free time, spare time, leisure", "noun", "neutral", "masculine", "nominal", "STANDARD", "Temporal availability noun used in personal schedule inquiries.", 1),
    ("боломж", "possibility, opportunity, feasibility, availability", "noun", "neutral", "masculine", "nominal", "STANDARD", "Abstract noun denoting situational feasibility or option.", 1),
    ("дуусах", "to finish, be depleted, expire, end", "verb", "neutral", "masculine", "verbal", "STANDARD", "Inchoative intransitive verb for exhausted supplies or ending time.", 1),

    # les_a1_24_04_ger_interior_inventory_reading (P: 3, R: 1) -> 4 lemmas
    ("эсгий", "felt, pressed wool felt", "noun", "neutral", "feminine", "nominal", "STANDARD", "Traditional nomadic insulating textile covering the ger frame.", 1),
    ("унь", "roof poles, rafters of ger", "noun", "neutral", "masculine", "nominal", "STANDARD", "Radial wooden poles connecting wall lattice to roof ring.", 1),
    ("үүд", "door, doorway, entrance, threshold", "noun", "neutral", "feminine", "nominal", "STANDARD", "Architectural entranceway facing traditionally south.", 1),
    ("хөшиг", "curtain, drapery, screen", "noun", "neutral", "feminine", "nominal", "STANDARD", "Fabric partition or window covering in domestic dwellings.", 1),

    # -------------------------------------------------------------------------
    # UNIT 25: Dative-Locative Spatial Anchoring (Lessons 25_01 - 25_04) - 23 lemmas
    # -------------------------------------------------------------------------
    # les_a1_25_01_dative_locative_allomorphs (P: 5, R: 2) -> 7 lemmas
    ("дээр", "on, upon, on top of, above", "postposition", "neutral", "feminine", "invariable", "STANDARD", "Primary relational spatial postposition governing genitive or bare stem.", 1),
    ("доор", "under, beneath, below, underneath", "postposition", "neutral", "masculine", "invariable", "STANDARD", "Spatial postposition denoting location beneath an object.", 1),
    ("дотор", "inside, within, interior to", "postposition", "neutral", "masculine", "invariable", "STANDARD", "Spatial postposition denoting interior containment.", 1),
    ("гадна", "outside, outdoors, exterior to", "postposition", "neutral", "masculine", "invariable", "STANDARD", "Spatial postposition denoting exterior location.", 1),
    ("байшин", "building, edifice, masonry house", "noun", "neutral", "masculine", "nominal", "STANDARD", "Permanent architecture noun contrasted with nomadic ger.", 1),
    ("дэргэд", "beside, next to, alongside, in the vicinity of", "postposition", "neutral", "feminine", "invariable", "STANDARD", "Spatial postposition indicating close lateral proximity.", 1),
    ("завсар", "interval, space between, gap, interstice", "noun", "neutral", "masculine", "nominal", "STANDARD", "Spatial interval between objects or structures.", 1),

    # les_a1_25_02_locating_people_places (P: 5, R: 2) -> 7 lemmas
    ("гудамж", "street, avenue, thoroughfare", "noun", "neutral", "masculine", "nominal", "STANDARD", "Urban transit thoroughfare noun in municipal navigation.", 1),
    ("талбай", "square, plaza, open area, field", "noun", "neutral", "masculine", "nominal", "STANDARD", "Urban civic open plaza (e.g., Sükhbaatar Square) or expanse.", 1),
    ("цэцэрлэг", "garden, public park, kindergarten", "noun", "neutral", "feminine", "nominal", "STANDARD", "Green urban amenity or early childhood educational facility.", 1),
    ("төв", "center, central, hub", "noun", "neutral", "feminine", "nominal", "STANDARD", "Spatial and organizational center of a city or district.", 1),
    ("үйлдвэр", "factory, manufacturing plant, mill, industry", "noun", "neutral", "feminine", "nominal", "STANDARD", "Industrial production facility in urban zoning.", 1),
    ("дүүрэг", "district, municipal borough", "noun", "neutral", "feminine", "nominal", "STANDARD", "Official municipal administrative division of the capital city Ulaanbaatar.", 1),
    ("хороо", "khoroo, sub-district, administrative neighborhood", "noun", "neutral", "masculine", "nominal", "STANDARD", "Primary neighborhood administrative subdivision of an urban district.", 1),

    # les_a1_25_03_urban_directory_reading (P: 4, R: 1) -> 5 lemmas
    ("давхар", "floor, storey, tier, layer", "noun", "neutral", "masculine", "nominal", "STANDARD", "Vertical building level noun essential for building directories.", 1),
    ("шат", "stairs, staircase, steps, ladder", "noun", "neutral", "masculine", "nominal", "STANDARD", "Vertical pedestrian circulation structure inside buildings.", 1),
    ("хаалга", "door, gate, portal, gateway", "noun", "neutral", "masculine", "nominal", "STANDARD", "Primary entrance aperture and room doorway in buildings.", 1),
    ("хэсэг", "section, department, division, part", "noun", "neutral", "feminine", "nominal", "STANDARD", "Organizational or structural section in building directories.", 1),
    ("лифт", "elevator, lift", "noun", "neutral", "feminine", "nominal", "STANDARD", "Modern mechanical vertical transit amenity in public buildings.", 1),

    # les_a1_25_04_spatial_inquiries_qa (P: 3, R: 1) -> 4 lemmas
    ("хаана", "where, in what place", "pronoun", "neutral", "masculine", "invariable", "STANDARD", "Core interrogative locative pronoun initiating spatial inquiries.", 1),
    ("баруун", "right, west, western", "adjective", "neutral", "masculine", "adjectival", "STANDARD", "Cardinal direction and egocentric lateral directional modifier.", 1),
    ("зүүн", "left, east, eastern", "adjective", "neutral", "feminine", "adjectival", "STANDARD", "Cardinal direction and egocentric lateral directional modifier.", 1),
    ("чигээрээ", "straight ahead, directly forward", "adverb", "neutral", "feminine", "invariable", "STANDARD", "Deictic trajectory adverb used in directional navigation instructions.", 1)
]

BATCH1_EXPRESSIONS = [
    # -------------------------------------------------------------------------
    # UNIT 21: Nominal Negation (6 expressions)
    # -------------------------------------------------------------------------
    # les_a1_21_01 (P: 1, R: 0)
    ("биш ээ", "no, it is not; not at all", "formulaic_language", "informal", ["биш", "ээ"], "Conversational particle routine firmly denying identity assertion."),
    # les_a1_21_02 (P: 1, R: 1)
    ("үгүй ээ", "no, oh no", "formulaic_language", "neutral", ["үгүй", "ээ"], "Polite formulaic response preceding correction of identity or facts."),
    ("харин тийм", "indeed so; on the contrary, yes; exactly", "formulaic_language", "neutral", ["харин", "тийм"], "Conversational discourse marker confirming a counter-assertion or realization."),
    # les_a1_21_03 (P: 1, R: 0)
    ("тийм биш үү", "isn't that so? aren't you? right?", "formulaic_language", "neutral", ["тийм", "биш", "үү"], "Conversational tag question seeking confirmation of expected fact."),
    # les_a1_21_04 (P: 1, R: 1)
    ("минийх биш", "not mine, doesn't belong to me", "collocation", "neutral", ["би", "биш"], "Possessive negation construction disclaiming ownership in lost-and-found."),
    ("гээсэн эд", "lost property, lost item, misplaced article", "collocation", "neutral", ["гээх", "эд"], "Civic administrative term denoting items registered in lost-and-found."),

    # -------------------------------------------------------------------------
    # UNIT 22: Formal Departure & Gratitude (6 expressions)
    # -------------------------------------------------------------------------
    # les_a1_22_01 (P: 1, R: 1)
    ("дараа уулзъя", "see you later, until next time", "formulaic_language", "neutral", ["дараа", "уулзах"], "Future-volitive departure formula promising future meeting."),
    ("сайхан амраарай", "have a good rest, sleep well", "formulaic_language", "neutral", ["сайхан", "амрах"], "Prescriptive evening and weekend benediction upon departure."),
    # les_a1_22_02 (P: 1, R: 0)
    ("маш их баярлалаа", "thank you very much, thank you so much", "formulaic_language", "neutral", ["маш", "их", "баярлах"], "High-gratitude social routine expressing deep appreciation to hosts and seniors."),
    # les_a1_22_03 (P: 1, R: 1)
    ("сайн яваарай", "have a safe trip, go well", "formulaic_language", "neutral", ["сайн", "явах"], "Traditional parting wish directed specifically to the person departing."),
    ("сайн сууж байгаарай", "stay well, take care of yourself", "formulaic_language", "neutral", ["сайн", "суух", "байх"], "Traditional parting wish directed specifically to the host or person remaining."),
    # les_a1_22_04 (P: 1, R: 0)
    ("түр баяртай", "bye for now, see you in a bit", "formulaic_language", "informal", ["түр", "баяртай"], "Conversational short-interval parting expression."),

    # -------------------------------------------------------------------------
    # UNIT 23: Section Synthesis & Social Reception (9 expressions)
    # -------------------------------------------------------------------------
    # les_a1_23_01 (P: 2, R: 1)
    ("тавтай морилно уу", "welcome! please enter honorifically", "formulaic_language", "formal", ["тавтай", "морилох", "уу"], "Traditional high-politeness welcome formula spoken at household or official threshold."),
    ("дээшээ суу", "please sit up in the place of honor, please take a seat", "formulaic_language", "neutral", ["дээшээ", "суух"], "Hospitality directive inviting guest to occupy seat of honor."),
    ("тавтай саатаарай", "please have a pleasant stay, enjoy your visit", "formulaic_language", "formal", ["тавтай", "саатах"], "Formal hospitable wish to guests at formal events or reception lodgings."),
    # les_a1_23_02 (P: 2, R: 1)
    ("таны нэр хэн бэ", "what is your name?", "formulaic_language", "neutral", ["та", "нэр", "хэн", "бэ"], "Polite standard social inquiry regarding individual's name."),
    ("аль нутаг вэ", "which region are you from? where is your home country?", "formulaic_language", "neutral", ["аль", "нутаг", "вэ"], "Sociocultural inquiry regarding geographic and regional origin."),
    ("хүндэт зочин", "honored guest, distinguished visitor", "collocation", "formal", ["хүндэт", "зочин"], "Formal protocol designation for invited guests."),
    # les_a1_23_03 (P: 1, R: 1)
    ("монголоор ярих", "to speak in Mongolian", "collocation", "neutral", ["монгол", "ярих"], "Instrumental language-use construction denoting spoken Mongolian proficiency."),
    ("сайн ойлгосонгүй", "I did not understand well; pardon?", "formulaic_language", "neutral", ["сайн", "ойлгох", "гүй"], "Polite conversational routine signaling comprehension difficulty."),
    # les_a1_23_04 (P: 1, R: 0)
    ("албан ёсны айлчлал", "official visit, formal diplomatic call", "collocation", "formal", ["алба", "ёс", "айлчлал"], "Civic and diplomatic narrative collocation denoting structured state reception."),

    # -------------------------------------------------------------------------
    # UNIT 24: Existential Assertion vs Negation (6 expressions)
    # -------------------------------------------------------------------------
    # les_a1_24_01 (P: 1, R: 1)
    ("гэрт байна", "is at home, is in the ger", "collocation", "neutral", ["гэр", "байх"], "Locative existential statement denoting home presence."),
    ("бэлэн байна", "is ready, is prepared, is available", "collocation", "neutral", ["бэлэн", "байх"], "Predicate formula confirming readiness of amenities, food, or service."),
    # les_a1_24_02 (P: 1, R: 0)
    ("энд алга", "is not here, missing here, there is none here", "collocation", "informal", ["энд", "алга"], "Immediate deictic negative statement noting local absence."),
    # les_a1_24_03 (P: 1, R: 1)
    ("байгаа юу", "is there any? do you have? is it available?", "formulaic_language", "neutral", ["байх", "юу"], "Conversational inquiry checking resource or room availability."),
    ("сул өрөө", "vacant room, available room, free room", "collocation", "neutral", ["сул", "өрөө"], "Hospitality terminology denoting unoccupied guest accommodation."),
    # les_a1_24_04 (P: 1, R: 0)
    ("монгол гэр", "Mongolian ger, yurt, traditional felt dwelling", "collocation", "neutral", ["монгол", "гэр"], "Canonical cultural collocation for the traditional nomadic felt architecture."),

    # -------------------------------------------------------------------------
    # UNIT 25: Dative-Locative Spatial Anchoring (6 expressions)
    # -------------------------------------------------------------------------
    # les_a1_25_01 (P: 1, R: 1)
    ("ширээн дээр", "on the table, upon the desk", "collocation", "neutral", ["ширээ", "дээр"], "Prototypical postpositional locative phrase with genitive/stem allomorph."),
    ("гэрийн гадна", "outside the ger, outdoors beside the house", "collocation", "neutral", ["гэр", "гадна"], "Spatial postpositional phrase indicating exterior proximity."),
    # les_a1_25_02 (P: 1, R: 0)
    ("хотын төв", "city center, downtown, central district", "collocation", "neutral", ["хот", "төв"], "Municipal geographic collocation designating downtown hub."),
    # les_a1_25_03 (P: 1, R: 1)
    ("нэгдүгээр давхар", "first floor, ground floor", "collocation", "neutral", ["нэг", "давхар"], "Ordinal floor designation central to building directories."),
    ("аваарын гарц", "emergency exit, fire exit", "collocation", "formal", ["аваар", "гарц"], "Statutory public safety sign indicating escape route."),
    # les_a1_25_04 (P: 1, R: 0)
    ("хаана байна вэ", "where is it located? where is it?", "formulaic_language", "neutral", ["хаана", "байх", "вэ"], "Standard interrogative locative formula requesting spatial directions.")
]
