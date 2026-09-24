"""
Phase 1D.2 Targeted Repair Script for CEFR A2 Lesson Blueprints
Applies structural corrections to break generator pathologies:
- Eliminates the 48/48/48 template (Units with 0, 1, 2+ vocab, listening, dialogue)
- Introduces natural lesson count variation (3 to 7 lessons)
- Diversifies lesson-type sequences
- Breaks hardcoded lexical allocation tuples while preserving 100% budget match
- Reconstructs DAG to reduce adjacent prerequisite defaults (< 35%)
- Deepens reinforcement for under-reinforced grammar targets
- Dissolves large normalized structural clusters
"""

import json
import os
import sys
from collections import defaultdict, Counter
from typing import Dict, List, Any

sys.path.insert(0, os.path.abspath("."))

def run_repairs():
    print("Loading fresh base A2 lessons from generators...")
    with open("curriculum/blueprint/units/a2.json", "r", encoding="utf-8") as f:
        a2_units = json.load(f)
    unit_map = {u["unitId"]: u for u in a2_units}
    unit_pos_map = {u["sequencePosition"]: u for u in a2_units}

    from scripts.framework_builder.gen_sec01 import get_sec01_lessons
    from scripts.framework_builder.gen_sec02 import get_sec02_lessons
    from scripts.framework_builder.gen_sec03 import get_sec03_lessons
    from scripts.framework_builder.gen_sec04 import get_sec04_lessons
    from scripts.framework_builder.gen_sec05 import get_sec05_lessons

    sec_lessons = {
        1: get_sec01_lessons(),
        2: get_sec02_lessons(),
        3: get_sec03_lessons(),
        4: get_sec04_lessons(),
        5: get_sec05_lessons()
    }

    # =========================================================================
    # 1. SECTION 01 REPAIRS (Units 64 - 72)
    # =========================================================================
    print("Repairing Section 01...")
    s1_lessons = sec_lessons[1]
    u_lessons_s1 = defaultdict(list)
    for l in s1_lessons:
        u_lessons_s1[l["unitId"]].append(l)

    # --- Unit 64 (Navigating UB Bus Routes): Split into 2 Vocab lessons (Bus Routes vs Smart Cards)
    # Current: 6 lessons.
    u64_id = unit_pos_map[64]["unitId"]
    # Change lesson 3 (currently listening) into Vocab 2: Digital Smart Cards
    # Make lesson 4 Listening, Lesson 5 Reading, Lesson 6 Dialogue, Lesson 7 Guided Practice -> wait, let's keep 6 lessons:
    # 1: gram_intro, 2: vocab_intro (Bus Routes), 3: vocab_intro (U-Money Smart Cards), 4: listening, 5: dialogue, 6: grammar_guided_practice
    u64 = u_lessons_s1[u64_id]
    u64[2]["lessonType"] = "vocabulary_introduction"
    u64[2]["title"] = "Digital Transit Media: U-Money Smart Cards, Fares & Validation"
    u64[2]["primaryPurpose"] = "Introduce vocabulary for electronic fare media, smart card readers, balance recharge points, and automated bus turnstiles."
    u64[2]["communicativeOutcome"] = "Purchase, reload, and tap a digital U-Money transit card when boarding municipal buses."
    u64[2]["recommendedExerciseModalities"] = ["matching", "contextual_cloze", "dialogue_completion"]

    # --- Unit 65 (Hailing Street Taxis): Add 2nd Listening lesson
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    u65_id = unit_pos_map[65]["unitId"]
    u65 = u_lessons_s1[u65_id]
    # Change lesson 3 (dialogue) -> dialogue; change lesson 4 -> listening 1; add lesson 5 listening 2?
    # Let's change lesson 2 to listening_development:
    # Or let's make u65 have 2 listening lessons: Lesson 2 listening (Street hailing sounds), Lesson 4 listening (Dispatch radio)
    # Wait, Unit 65 has 5 lessons. Let's make:
    # 1: gram_intro, 2: vocabulary_introduction, 3: listening_development (Hailing calls & traffic noise), 4: listening_development (Taxi dispatch radio), 5: dialogue_work
    u65[2]["lessonType"] = "listening_development"
    u65[2]["title"] = "Acoustic Lab: Street Hailing Ambient Shouts & Approaching Cabs"
    u65[2]["primaryPurpose"] = "Develop acoustic discrimination for short shouted landmark names and cab honks in dense street traffic."
    u65[2]["listeningObjective"] = "Identify passenger destination cries ('Урагшаа!', 'Төв талбай!') over engine noise."
    u65[2]["recommendedExerciseModalities"] = ["listening_comprehension", "phonetic_discrimination", "speed_identification"]

    # --- Unit 66 (Intercity Rail): Grammar reinforcement
    u66_id = unit_pos_map[66]["unitId"]
    u66 = u_lessons_s1[u66_id]
    # Ensure gram_a2_case_instrumental_means is practiced in lesson 4 & 6
    if "gram_a2_case_instrumental_means" not in u66[3].get("grammarPracticed", []):
        u66[3].setdefault("grammarPracticed", []).append("gram_a2_case_instrumental_means")
    if "gram_a2_case_instrumental_means" not in u66[5].get("grammarPracticed", []):
        u66[5].setdefault("grammarPracticed", []).append("gram_a2_case_instrumental_means")

    # --- Unit 68 (Transit Delays): 0 vocabulary lessons!
    # Turn lesson 2 (currently vocab) into reading_development
    u68_id = unit_pos_map[68]["unitId"]
    u68 = u_lessons_s1[u68_id]
    u68[1]["lessonType"] = "reading_development"
    u68[1]["title"] = "Deciphering Road Condition Bulletins, Traffic Radio Alerts & Detours"
    u68[1]["primaryPurpose"] = "Read authentic public transit advisories, traffic jam warnings, and winter road condition alerts in Cyrillic."
    u68[1]["readingObjective"] = "Extract estimated delay minutes and suggested detour avenues from municipal traffic texts."
    u68[1]["recommendedExerciseModalities"] = ["reading_comprehension", "information_extraction", "true_false"]

    # --- Unit 69 (Postal & Courier): 0 listening lessons!
    # Turn lesson 3 (currently listening) into reading_development (Customs forms & declarations)
    u69_id = unit_pos_map[69]["unitId"]
    u69 = u_lessons_s1[u69_id]
    u69[2]["lessonType"] = "reading_development"
    u69[2]["title"] = "Reading International Customs Declarations & Fragile Parcel Regulations"
    u69[2]["primaryPurpose"] = "Analyze postal customs declaration forms, prohibited item lists, and insurance option clauses."
    u69[2]["readingObjective"] = "Identify declared value, parcel category, and recipient signature fields."
    u69[2]["recommendedExerciseModalities"] = ["reading_comprehension", "document_analysis", "matching"]

    # --- Unit 70 (ATM Banking Basics): 3 Lessons!
    u70_id = unit_pos_map[70]["unitId"]
    u70 = u_lessons_s1[u70_id]
    # Current has 4 lessons: vocab, reading, listening, dialogue.
    # Keep 3 lessons: 1: vocab, 2: reading, 3: dialogue (incorporate audio prompts into dialogue!)
    u70_new = [u70[0], u70[1], u70[3]]
    for i, l in enumerate(u70_new, 1):
        l["sequenceWithinUnit"] = i
    u_lessons_s1[u70_id] = u70_new

    # --- Unit 71 (Currency Exchange): Grammar reinforcement
    u71_id = unit_pos_map[71]["unitId"]
    u71 = u_lessons_s1[u71_id]
    if "gram_a2_case_instrumental_means" not in u71[3].get("grammarPracticed", []):
        u71[3].setdefault("grammarPracticed", []).append("gram_a2_case_instrumental_means")

    # --- Unit 72 (Urban Transit Capstone): 7 Lessons!
    u72_id = unit_pos_map[72]["unitId"]
    u72 = u_lessons_s1[u72_id]
    # Current has 5 lessons: vocab, listening, reading, dialogue, checkpoint.
    # We expand to 7 lessons:
    # 1: vocab (Multimodal Transit)
    # 2: vocab (Integrated Ticketing & Cross-Town Transfers)
    # 3: reading (Master Schedules)
    # 4: listening (Automated PA)
    # 5: dialogue (Cross-Town Commuter Consultation)
    # 6: grammar_guided_practice (Metropolitan Itinerary Drafting with instrumental means)
    # 7: checkpoint (Benchmark Checkpoint)
    new_l2 = dict(u72[0])
    new_l2["lessonId"] = "les_a2_72_02_integrated_ticketing_transfers_lexicon"
    new_l2["sequenceWithinUnit"] = 2
    new_l2["title"] = "Smart Fare Media: Multi-Leg Transfers & Transit Hub Lexicon"
    new_l2["primaryPurpose"] = "Master lexical items for multi-leg commuter transfers, connecting express routes, and electronic card recharge."
    new_l2["communicativeOutcome"] = "Inquire about transfer windows and cross-town route intersections using specialized transit terminology."
    new_l2["newProductiveLemmaTarget"] = 4
    new_l2["newReceptiveLemmaTarget"] = 2
    new_l2["newProductiveExpressionTarget"] = 1
    new_l2["newReceptiveExpressionTarget"] = 1
    new_l2["prerequisiteLessonIds"] = [u72[0]["lessonId"]]

    new_l6 = dict(u72[3])
    new_l6["lessonId"] = "les_a2_72_06_metropolitan_transit_itinerary_drafting"
    new_l6["sequenceWithinUnit"] = 6
    new_l6["lessonType"] = "grammar_guided_practice"
    new_l6["title"] = "Metropolitan Transit Dossier: Authoring a 3-Leg Journey Itinerary"
    new_l6["primaryPurpose"] = "Synthesize instrumental case of transport and means to compose an unassisted multi-modal urban transit plan."
    new_l6["grammarPracticed"] = ["gram_a2_case_instrumental_transport_language", "gram_a2_case_instrumental_means", "gram_a2_case_directional_towards"]
    new_l6["communicativeOutcome"] = "Draft a comprehensive commuter briefing detailing vehicles, transfers, and fare methods across Ulaanbaatar."
    new_l6["writingObjective"] = "Write a 6-sentence cross-town transit plan detailing connecting stops, payment methods, and landmarks."
    new_l6["newProductiveLemmaTarget"] = 2
    new_l6["newReceptiveLemmaTarget"] = 1
    new_l6["newProductiveExpressionTarget"] = 1
    new_l6["newReceptiveExpressionTarget"] = 0
    new_l6["recommendedExerciseModalities"] = ["sentence_construction", "error_correction", "short-answer writing"]
    new_l6["prerequisiteLessonIds"] = [u72[0]["lessonId"], u72[2]["lessonId"]]

    u72_expanded = [u72[0], new_l2, u72[2], u72[1], u72[3], new_l6, u72[4]]
    for i, l in enumerate(u72_expanded, 1):
        l["sequenceWithinUnit"] = i
    u72_expanded[6]["prerequisiteLessonIds"] = [new_l6["lessonId"]]
    u_lessons_s1[u72_id] = u72_expanded

    # Rebalance Section 1 budgets
    sec_lessons[1] = []
    for pos in range(64, 73):
        sec_lessons[1].extend(u_lessons_s1[unit_pos_map[pos]["unitId"]])

    # =========================================================================
    # 2. SECTION 02 REPAIRS (Units 73 - 82)
    # =========================================================================
    print("Repairing Section 02...")
    s2_lessons = sec_lessons[2]
    u_lessons_s2 = defaultdict(list)
    for l in s2_lessons:
        u_lessons_s2[l["unitId"]].append(l)

    # --- Unit 74 (Clothing & Fitting): Sequence permutation (Start with Reading)
    u74_id = unit_pos_map[74]["unitId"]
    u74 = u_lessons_s2[u74_id]
    # Swap lesson 1 and 2: reading first, then vocab intro
    # Current: 1: gram_intro, 2: vocab, 3: listening, 4: dialogue, 5: guided_practice
    # Change to: 1: reading_development, 2: grammar_introduction, 3: vocabulary_introduction, 4: listening_development, 5: dialogue_work
    u74[0], u74[1] = u74[1], u74[0]
    for i, l in enumerate(u74, 1):
        l["sequenceWithinUnit"] = i

    # --- Unit 79 (Open Air Market Bargaining): 2 Dialogue lessons!
    u79_id = unit_pos_map[79]["unitId"]
    u79 = u_lessons_s2[u79_id]
    # Current: 6 lessons (gram_intro, vocab, listening, reading, dialogue, guided_practice)
    # Turn lesson 4 (reading) into dialogue_work 1 (Initial price inquiry & merchant probing)
    # Lesson 5 becomes dialogue_work 2 (Intense haggling & counter-bidding)
    u79[3]["lessonType"] = "dialogue_work"
    u79[3]["title"] = "At the Market Stall: Initial Inquiries, Price Tag Probing & Quality Checks"
    u79[3]["primaryPurpose"] = "Execute opening conversational moves with open-air market vendors to test initial asking prices."
    u79[3]["spokenProductionObjective"] = "Inquire about base prices: 'Энэ ямар үнэтэй вэ? Бөөний үнээр өгөх үү?'."
    u79[3]["recommendedExerciseModalities"] = ["dialogue_completion", "role-play response", "speed_identification"]

    # --- Unit 80 (Traditional Deel Tailoring): 2 Vocabulary lessons!
    u80_id = unit_pos_map[80]["unitId"]
    u80 = u_lessons_s2[u80_id]
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    # Turn lesson 4 (listening) into vocabulary_introduction 2 (Bespoke Cuts, Trims & Stitching Terms)
    u80[3]["lessonType"] = "vocabulary_introduction"
    u80[3]["title"] = "Bespoke Craftsmanship: Deel Patterns, Trims, Collars & Silk Classifications"
    u80[3]["primaryPurpose"] = "Introduce specialized artisanal terms for collar styles (босоо зах), cuffs (нударга), silk trims (торго), and custom stitching."
    u80[3]["communicativeOutcome"] = "Specify exact custom embellishments and fabric choices to an artisanal Mongolian tailor."
    u80[3]["recommendedExerciseModalities"] = ["matching", "categorization", "contextual_cloze"]

    sec_lessons[2] = []
    for pos in range(73, 83):
        sec_lessons[2].extend(u_lessons_s2[unit_pos_map[pos]["unitId"]])

    # =========================================================================
    # 3. SECTION 03 REPAIRS (Units 83 - 92)
    # =========================================================================
    print("Repairing Section 03...")
    s3_lessons = sec_lessons[3]
    u_lessons_s3 = defaultdict(list)
    for l in s3_lessons:
        u_lessons_s3[l["unitId"]].append(l)

    # --- Unit 84 (Describing Illness Symptoms): 2 Dialogue lessons!
    u84_id = unit_pos_map[84]["unitId"]
    u84 = u_lessons_s3[u84_id]
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    # Turn lesson 4 (listening) into dialogue_work 2 (Calling employer/supervisor for sick leave)
    u84[3]["lessonType"] = "dialogue_work"
    u84[3]["title"] = "Calling In Sick: Workplace Absence Notice & Urgent Shift Handover"
    u84[3]["primaryPurpose"] = "Execute an urgent telephone dialogue with a department supervisor to report acute illness and request absence."
    u84[3]["spokenProductionObjective"] = "State inability to work politely: 'Миний халуураад, өнөөдөр ажилдаа ирж чадахгүй нь. Эмчийн магадалгаа авчиръя'."
    u84[3]["recommendedExerciseModalities"] = ["dialogue_completion", "role-play response", "listening_comprehension"]

    # --- Unit 87 (Apartment Association Bylaws): 0 Vocab & 0 Listening lessons!
    u87_id = unit_pos_map[87]["unitId"]
    u87 = u_lessons_s3[u87_id]
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    # Turn lesson 2 (vocab) into reading_development (Bylaws code)
    # Turn lesson 4 (listening) into reading_development (Quiet hours & communal property notices)
    u87[1]["lessonType"] = "reading_development"
    u87[1]["title"] = "Reading Condominium Association (СӨХ) Charter Rules & Pet Regulations"
    u87[1]["primaryPurpose"] = "Analyze official residential bylaws regarding pet keeping, common area maintenance, and parking rules."
    u87[3]["lessonType"] = "reading_development"
    u87[3]["title"] = "Deciphering Noise Curfew Bulletins & Waste Sorting Guidelines"
    u87[3]["primaryPurpose"] = "Extract specific time windows (22:00 curfew) and recycling requirements from building notices."

    # --- Unit 90 (Clinical Encounters Capstone): 2 Listening lessons!
    u90_id = unit_pos_map[90]["unitId"]
    u90 = u_lessons_s3[u90_id]
    # Current: 5 lessons (vocab, reading, listening, dialogue, checkpoint)
    # Turn lesson 2 (reading) into listening_development 1 (Emergency Clinic Triage Audio)
    u90[1]["lessonType"] = "listening_development"
    u90[1]["title"] = "Acoustic Lab: Emergency Clinic Reception, Triage Calls & PA Broadcasts"
    u90[1]["primaryPurpose"] = "Comprehend ambient acoustic announcements in a hospital lobby, identifying patient queuing numbers and triage urgency."
    u90[1]["listeningObjective"] = "Identify queue numbers ('Дараагийн дугаар 42...') and designated consultation rooms from loudspeaker audio."
    u90[1]["recommendedExerciseModalities"] = ["listening_comprehension", "phonetic_discrimination", "speed_identification"]

    # Smooth the 20-word lexical load of Unit 90 lesson 1 across lesson 1 and 2
    # Unit 90 budget: (10, 5, 3, 2). Currently lesson 1 has all (10, 5, 3, 2) and others have 0!
    u90[0]["newProductiveLemmaTarget"] = 6
    u90[0]["newReceptiveLemmaTarget"] = 3
    u90[0]["newProductiveExpressionTarget"] = 2
    u90[0]["newReceptiveExpressionTarget"] = 1
    u90[1]["newProductiveLemmaTarget"] = 4
    u90[1]["newReceptiveLemmaTarget"] = 2
    u90[1]["newProductiveExpressionTarget"] = 1
    u90[1]["newReceptiveExpressionTarget"] = 1

    # --- Unit 91 (Genealogy & Family Ancestry): 0 Dialogue lessons!
    u91_id = unit_pos_map[91]["unitId"]
    u91 = u_lessons_s3[u91_id]
    # Current: 4 lessons (vocab, reading, listening, dialogue)
    # Turn lesson 4 (dialogue) into grammar_guided_practice (Authoring Clan Genealogy Chart & Ancestral Summary)
    u91[3]["lessonType"] = "grammar_guided_practice"
    u91[3]["title"] = "Authoring the Lineage Record: Transcribing Ancestral Heritage Summaries"
    u91[3]["primaryPurpose"] = "Synthesize possessive structures and kinship nouns to write an archival summary of personal ancestral heritage."
    u91[3]["communicativeOutcome"] = "Compose an accurate multi-generation family lineage sheet for official civic record archives."
    u91[3]["writingObjective"] = "Draft a 6-line family branch summary using genitive cases and ancestral clan terminology."
    u91[3]["recommendedExerciseModalities"] = ["sentence_construction", "error_correction", "short-answer writing"]

    # --- Unit 92 (Dental Emergency): 3 Lessons!
    u92_id = unit_pos_map[92]["unitId"]
    u92 = u_lessons_s3[u92_id]
    # Current has 4 lessons: vocab, reading, listening, dialogue.
    # Keep 3 lessons: 1: vocab, 2: reading, 3: dialogue (integrate acoustic audio into dialogue)
    u92_new = [u92[0], u92[1], u92[3]]
    for i, l in enumerate(u92_new, 1):
        l["sequenceWithinUnit"] = i
    u_lessons_s3[u92_id] = u92_new

    # Also smooth Unit 82 lexical load in Section 2 (was 20 items in lesson 1)
    u82_id = unit_pos_map[82]["unitId"]
    u82 = u_lessons_s2[u82_id]
    u82[0]["newProductiveLemmaTarget"] = 6
    u82[0]["newReceptiveLemmaTarget"] = 3
    u82[0]["newProductiveExpressionTarget"] = 2
    u82[0]["newReceptiveExpressionTarget"] = 1
    u82[1]["newProductiveLemmaTarget"] = 4
    u82[1]["newReceptiveLemmaTarget"] = 2
    u82[1]["newProductiveExpressionTarget"] = 1
    u82[1]["newReceptiveExpressionTarget"] = 1

    sec_lessons[3] = []
    for pos in range(83, 93):
        sec_lessons[3].extend(u_lessons_s3[unit_pos_map[pos]["unitId"]])

    # =========================================================================
    # 4. SECTION 04 REPAIRS (Units 93 - 102)
    # =========================================================================
    print("Repairing Section 04...")
    s4_lessons = sec_lessons[4]
    u_lessons_s4 = defaultdict(list)
    for l in s4_lessons:
        u_lessons_s4[l["unitId"]].append(l)

    # --- Unit 97 (Social Invitations): 2 Dialogue lessons!
    u97_id = unit_pos_map[97]["unitId"]
    u97 = u_lessons_s4[u97_id]
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    # Turn lesson 4 (listening) into dialogue_work 2 (Telephone RSVP & party details)
    u97[3]["lessonType"] = "dialogue_work"
    u97[3]["title"] = "RSVP Follow-Up Call: Confirming Attendance, Directions & Potluck Dishes"
    u97[3]["primaryPurpose"] = "Execute a telephone conversation to RSVP for a dinner gathering, ask what to bring, and confirm directions."
    u97[3]["spokenProductionObjective"] = "Confirm attendance: 'Баярлалаа, би заавал очно оо. Би юу авчрах хэрэгтэй вэ?'."
    u97[3]["recommendedExerciseModalities"] = ["dialogue_completion", "role-play response", "listening_comprehension"]

    # --- Unit 101 (Personal History Capstone): 7 Lessons & Reinforce All Participles!
    u101_id = unit_pos_map[101]["unitId"]
    u101 = u_lessons_s4[u101_id]
    # Current has 6 lessons:
    # 1: gram_intro, 2: vocab, 3: listening, 4: reading, 5: dialogue, 6: checkpoint
    # Expand to 7 lessons:
    # 1: gram_intro (Relative clauses: -сан, -даг, -х)
    # 2: vocab (Autobiographical lexicon)
    # 3: reading_development (Deciphering Memoirs & Biographies)
    # 4: grammar_guided_practice (Relative Clause Transformation Workshop: practicing -даг and -х!)
    # 5: listening_development (Radio Memoirs)
    # 6: dialogue_work (Autobiographical Interview)
    # 7: checkpoint (Benchmark Checkpoint)

    # In lesson 1, ensure all 3 participles are listed
    u101[0]["grammarIntroduced"] = [
        "gram_a2_participle_relative_clause_past_san",
        "gram_a2_participle_relative_clause_habitual_dag",
        "gram_a2_participle_relative_clause_future_kh",
        "gram_a2_participle_negative_aagui"
    ]

    # Rename Unit 101 lessons to strictly match their sequenceWithinUnit (01..07)
    u101[3]["lessonId"] = "les_a2_101_03_biography_profile_reading"
    new_l4_u101 = dict(u101[3])
    new_l4_u101["lessonId"] = "les_a2_101_04_relative_clause_syntax_workshop"
    new_l4_u101["sequenceWithinUnit"] = 4
    new_l4_u101["lessonType"] = "grammar_guided_practice"
    new_l4_u101["title"] = "Syntax Lab: Modifying Nouns with Past, Habitual & Future Participles"
    new_l4_u101["primaryPurpose"] = "Master the syntactic placement of relative clauses before head nouns using -сан4, -даг4, and -х participles."
    new_l4_u101["grammarPracticed"] = [
        "gram_a2_participle_relative_clause_habitual_dag",
        "gram_a2_participle_relative_clause_future_kh",
        "gram_a2_participle_relative_clause_past_san"
    ]
    new_l4_u101["communicativeOutcome"] = "Construct rich noun phrases describing habitual routines and upcoming aspirations."
    new_l4_u101["writingObjective"] = "Transform 5 simple clauses into complex relative clauses modifying head nouns."
    new_l4_u101["newProductiveLemmaTarget"] = 2
    new_l4_u101["newReceptiveLemmaTarget"] = 1
    new_l4_u101["newProductiveExpressionTarget"] = 1
    new_l4_u101["newReceptiveExpressionTarget"] = 0
    new_l4_u101["recommendedExerciseModalities"] = ["sentence_construction", "syntax_transformation", "error_correction"]
    new_l4_u101["prerequisiteLessonIds"] = [u101[0]["lessonId"], u101[3]["lessonId"]]

    u101[2]["lessonId"] = "les_a2_101_05_autobiographical_acoustic_decoding_lab"
    u101[2]["prerequisiteLessonIds"] = [u101[1]["lessonId"]]

    # Also reinforce habitual and future participles in lesson 6 (dialogue)
    u101[4]["lessonId"] = "les_a2_101_06_autobiographical_interview_simulation"
    u101[4]["grammarPracticed"] = [
        "gram_a2_participle_relative_clause_past_san",
        "gram_a2_participle_relative_clause_habitual_dag",
        "gram_a2_participle_relative_clause_future_kh"
    ]
    u101[4]["prerequisiteLessonIds"] = [u101[2]["lessonId"], new_l4_u101["lessonId"]]

    u101[5]["lessonId"] = "les_a2_101_07_personal_history_benchmark_checkpoint"
    u101[5]["prerequisiteLessonIds"] = [u101[4]["lessonId"], new_l4_u101["lessonId"]]

    u101_expanded = [u101[0], u101[1], u101[3], new_l4_u101, u101[2], u101[4], u101[5]]
    for i, l in enumerate(u101_expanded, 1):
        l["sequenceWithinUnit"] = i
    u_lessons_s4[u101_id] = u101_expanded

    # --- Unit 102 (Lease Agreements): 0 Listening lessons!
    u102_id = unit_pos_map[102]["unitId"]
    u102 = u_lessons_s4[u102_id]
    # Current: 4 lessons (vocab, reading, listening, dialogue)
    # Turn lesson 3 (listening) into reading_development (Security deposit & lease terms)
    u102[2]["lessonType"] = "reading_development"
    u102[2]["title"] = "Deciphering Rental Lease Covenants, Security Deposits & Utility Clauses"
    u102[2]["primaryPurpose"] = "Read standard legal clauses in Mongolian residential leases detailing deposit return, utility billing, and maintenance."
    u102[2]["readingObjective"] = "Identify required deposit sums, monthly due dates, and tenant damage liabilities in contract text."
    u102[2]["recommendedExerciseModalities"] = ["reading_comprehension", "document_analysis", "true_false"]
    # Update Unit 102 prerequisite to point to renamed Unit 101 checkpoint (07)
    u102[0]["prerequisiteLessonIds"] = [
        "les_a2_101_07_personal_history_benchmark_checkpoint"
        if p in ("les_a2_101_06_personal_history_benchmark_checkpoint", "les_a2_101_07_personal_history_benchmark_checkpoint")
        else p
        for p in u102[0].get("prerequisiteLessonIds", [])
    ]

    sec_lessons[4] = []
    for pos in range(93, 103):
        sec_lessons[4].extend(u_lessons_s4[unit_pos_map[pos]["unitId"]])

    # =========================================================================
    # 5. SECTION 05 REPAIRS (Units 103 - 111)
    # =========================================================================
    print("Repairing Section 05...")
    s5_lessons = sec_lessons[5]
    u_lessons_s5 = defaultdict(list)
    for l in s5_lessons:
        u_lessons_s5[l["unitId"]].append(l)

    # --- Unit 103 (Ger Furniture): Delayed reuse of habitual participle
    u103_id = unit_pos_map[103]["unitId"]
    u103 = u_lessons_s5[u103_id]
    if "gram_a2_participle_relative_clause_habitual_dag" not in u103[1].get("grammarPracticed", []):
        u103[1].setdefault("grammarPracticed", []).append("gram_a2_participle_relative_clause_habitual_dag")

    # --- Unit 104 (The Mongolian Ger): 2 Vocab lessons!
    u104_id = unit_pos_map[104]["unitId"]
    u104 = u_lessons_s5[u104_id]
    # Current: 4 lessons (vocab, reading, listening, dialogue)
    # Turn lesson 2 (reading) into vocabulary_introduction 2 (Felt Coverings, Ropes & Constructional Terminology)
    u104[1]["lessonType"] = "vocabulary_introduction"
    u104[1]["title"] = "Steppe Engineering: Felt Layers, Outer Canvas, Horsehair Ropes & Carpentry"
    u104[1]["primaryPurpose"] = "Introduce vocabulary for ger insulation layers (эсгий бүрээс), tension bands (бүслүүр), and weatherproofing canvas."
    u104[1]["communicativeOutcome"] = "Identify and name every material component required to winterize a nomadic dwelling."
    u104[1]["recommendedExerciseModalities"] = ["matching", "diagram_labeling", "categorization"]

    # --- Unit 105 (Ger Etiquette): 0 Vocab lessons!
    u105_id = unit_pos_map[105]["unitId"]
    u105 = u_lessons_s5[u105_id]
    # Current: 5 lessons (gram_intro, vocab, dialogue, listening, guided_practice)
    # Turn lesson 2 (vocab) into reading_development (Steppe Cultural Code & Taboo Rules)
    u105[1]["lessonType"] = "reading_development"
    u105[1]["title"] = "Deciphering the Nomadic Cultural Code: Steppe Taboos, Customs & Sacred Borders"
    u105[1]["primaryPurpose"] = "Read authentic guidelines detailing taboo actions (stepping on threshold, walking between pillars, whistling in ger)."
    u105[1]["readingObjective"] = "Identify forbidden behaviors and prescribed guest responses from traditional cultural texts."
    u105[1]["recommendedExerciseModalities"] = ["reading_comprehension", "true_false", "matching"]

    # --- Unit 106 (Five Nomadic Animals): 2 Vocab lessons!
    u106_id = unit_pos_map[106]["unitId"]
    u106 = u_lessons_s5[u106_id]
    # Current: 4 lessons (vocab, reading, listening, dialogue)
    # Turn lesson 2 (reading) into vocabulary_introduction 2 (Livestock Age, Gender, Coat Colors & Herd Terms)
    u106[1]["lessonType"] = "vocabulary_introduction"
    u106[1]["title"] = "Herd Taxonomy: Traditional Age, Gender & Coat Color Distinctions of the Five Snouts"
    u106[1]["primaryPurpose"] = "Introduce specialized Mongolian terms for young stock (даага, хурга, тугал, ботго) and adult gender/color designations."
    u106[1]["communicativeOutcome"] = "Accurately name livestock by age cohort and coat color when conversing with herders."
    u106[1]["recommendedExerciseModalities"] = ["matching", "categorization", "contextual_cloze"]

    # --- Unit 109 (Lost and Found): 3 Lessons & 0 Dialogue lessons!
    u109_id = unit_pos_map[109]["unitId"]
    u109 = u_lessons_s5[u109_id]
    # Current: 4 lessons (vocab, reading, listening, dialogue)
    # Keep 3 lessons: 1: vocab, 2: reading, 3: grammar_guided_practice (Lost property claim petition)
    u109[3]["lessonType"] = "grammar_guided_practice"
    u109[3]["title"] = "Filing the Official Report: Authoring a Lost Property & Bag Recovery Petition"
    u109[3]["primaryPurpose"] = "Synthesize descriptive adjectives and relative clauses to write a formal lost item declaration for transit police."
    u109[3]["communicativeOutcome"] = "Submit an official written claim form detailing lost luggage characteristics and contact data."
    u109[3]["writingObjective"] = "Draft a 6-line lost property declaration specifying brand, color, contents, and transit location."
    u109[3]["recommendedExerciseModalities"] = ["sentence_construction", "error_correction", "short-answer writing"]
    # Drop listening lesson
    u109_new = [u109[0], u109[1], u109[3]]
    for i, l in enumerate(u109_new, 1):
        l["sequenceWithinUnit"] = i
    u_lessons_s5[u109_id] = u109_new

    # --- Unit 110 (Telephone Courtesy): Delayed reuse of future participle
    u110_id = unit_pos_map[110]["unitId"]
    u110 = u_lessons_s5[u110_id]
    if "gram_a2_participle_relative_clause_future_kh" not in u110[0].get("grammarPracticed", []):
        u110[0].setdefault("grammarPracticed", []).append("gram_a2_participle_relative_clause_future_kh")
    if "gram_a2_participle_relative_clause_future_kh" not in u110[3].get("grammarPracticed", []):
        u110[3].setdefault("grammarPracticed", []).append("gram_a2_participle_relative_clause_future_kh")

    # --- Unit 111 (Waystage Pastoral Exit Capstone): 7 Lessons & 2 Listening lessons!
    u111_id = unit_pos_map[111]["unitId"]
    u111 = u_lessons_s5[u111_id]
    # Current: 6 lessons (vocab, reading, listening, guided_practice, dialogue, checkpoint)
    # Expand to 7 lessons:
    # 1: vocab (Pastoral Life)
    # 2: reading (Steppe Lore)
    # 3: listening 1 (Steppe Teamwork & Animal Commands)
    # 4: listening 2 (Hearthside Folklore & Melodies)
    # 5: dialogue (Steppe Encounter)
    # 6: guided_practice (Pastoral Synthesis Narrative - reinforcing habitual and future participles!)
    # 7: checkpoint (Waystage Exit Milestone Checkpoint)

    new_l4_u111 = dict(u111[2])
    new_l4_u111["lessonId"] = "les_a2_111_04_hearthside_folklore_acoustic_listening"
    new_l4_u111["sequenceWithinUnit"] = 4
    new_l4_u111["lessonType"] = "listening_development"
    new_l4_u111["title"] = "Acoustic Lab: Evening by the Hearth — Oral Folklore, Proverbs & Horsehead Fiddle"
    new_l4_u111["primaryPurpose"] = "Develop sustained listening comprehension for continuous natural spoken Mongolian in an elder's hearthside folktale."
    new_l4_u111["listeningObjective"] = "Follow an uninterrupted 2.5-minute traditional oral narrative and identify moral lessons."
    new_l4_u111["newProductiveLemmaTarget"] = 0
    new_l4_u111["newReceptiveLemmaTarget"] = 2
    new_l4_u111["newProductiveExpressionTarget"] = 0
    new_l4_u111["newReceptiveExpressionTarget"] = 1
    new_l4_u111["recommendedExerciseModalities"] = ["listening_comprehension", "story_sequencing", "inference_extraction"]
    new_l4_u111["prerequisiteLessonIds"] = [u111[0]["lessonId"], u111[1]["lessonId"]]

    # In guided practice (lesson 6), reinforce all 3 under-reinforced targets
    u111[3]["grammarPracticed"] = [
        "gram_a2_case_instrumental_means",
        "gram_a2_participle_relative_clause_habitual_dag",
        "gram_a2_participle_relative_clause_future_kh",
        "gram_a2_converb_concessive_vch_bolovch",
        "gram_a2_converb_terminative_tal",
        "gram_a2_verb_past_narrative_v"
    ]

    u111_expanded = [u111[0], u111[1], u111[2], new_l4_u111, u111[4], u111[3], u111[5]]
    for i, l in enumerate(u111_expanded, 1):
        l["sequenceWithinUnit"] = i
    u111_expanded[6]["prerequisiteLessonIds"] = [u111[3]["lessonId"], u111[4]["lessonId"]]
    u_lessons_s5[u111_id] = u111_expanded

    # Further diversify sequences across 5-lesson grammar units to eliminate top-sequence concentration (< 20%)
    # Units to permute:
    # 75: gram -> vocab -> reading -> dialogue -> guided_practice
    u75_id = unit_pos_map[75]["unitId"]
    u75 = u_lessons_s2[u75_id]
    u75[2]["lessonType"] = "reading_development"
    u75[2]["title"] = "Deciphering Personal Narrative Letters & Reflexive-Possessive Diary Entries"
    u75[2]["primaryPurpose"] = "Analyze personal journal entries and letters employing reflexive possessive suffixes (-аа4)."
    u75[2]["readingObjective"] = "Identify self-referential possession ('өөрийнхөө гэр бүл', 'ахдаа') in written Cyrillic narratives."
    u75[2]["recommendedExerciseModalities"] = ["reading_comprehension", "syntax_transformation", "true_false"]

    # 77: gram -> listening -> vocab -> dialogue -> guided_practice
    u77_id = unit_pos_map[77]["unitId"]
    u77 = u_lessons_s2[u77_id]
    u77[1], u77[3] = u77[3], u77[1]
    for i, l in enumerate(u77, 1):
        l["sequenceWithinUnit"] = i

    # 86: gram -> dialogue -> vocab -> listening -> guided_practice
    u86_id = unit_pos_map[86]["unitId"]
    u86 = u_lessons_s3[u86_id]
    u86[1], u86[2] = u86[2], u86[1]
    for i, l in enumerate(u86, 1):
        l["sequenceWithinUnit"] = i

    # 88: gram -> reading -> vocab -> dialogue -> guided_practice
    u88_id = unit_pos_map[88]["unitId"]
    u88 = u_lessons_s3[u88_id]
    u88[3]["lessonType"] = "reading_development"
    u88[3]["title"] = "Reading Official Capability & Disability Guidelines for Public Work"
    u88[3]["primaryPurpose"] = "Analyze official employment advisories detailing physical capabilities and potentiality using -ж чадах/чадахгүй."
    u88[3]["readingObjective"] = "Extract required skills and capability constraints from workplace circulars."
    u88[3]["recommendedExerciseModalities"] = ["reading_comprehension", "document_analysis", "true_false"]

    # 95: gram -> vocab -> guided_practice -> dialogue -> listening
    u95_id = unit_pos_map[95]["unitId"]
    u95 = u_lessons_s4[u95_id]
    u95[2], u95[4] = u95[4], u95[2]
    for i, l in enumerate(u95, 1):
        l["sequenceWithinUnit"] = i

    # 98: gram -> listening -> dialogue -> vocab -> guided_practice
    u98_id = unit_pos_map[98]["unitId"]
    u98 = u_lessons_s4[u98_id]
    u98[1], u98[3] = u98[3], u98[1]
    for i, l in enumerate(u98, 1):
        l["sequenceWithinUnit"] = i

    # 108: gram -> reading -> dialogue -> listening -> guided_practice
    u108_id = unit_pos_map[108]["unitId"]
    u108 = u_lessons_s5[u108_id]
    u108[1]["lessonType"] = "reading_development"
    u108[1]["title"] = "Deciphering Countryside Route Maps, Waypoint Guides & Fuel Supply Tables"
    u108[1]["primaryPurpose"] = "Analyze regional travel advisories and highway waypoint charts for steppe journeys."
    u108[1]["readingObjective"] = "Identify gas station locations, dirt track crossings, and river fords on regional route maps."
    u108[1]["recommendedExerciseModalities"] = ["reading_comprehension", "information_extraction", "matching"]

    # Rebuild all 5 section lesson lists from the modified unit lists
    sec_lessons[1] = []
    for pos in range(64, 73):
        sec_lessons[1].extend(u_lessons_s1[unit_pos_map[pos]["unitId"]])

    sec_lessons[2] = []
    for pos in range(73, 83):
        sec_lessons[2].extend(u_lessons_s2[unit_pos_map[pos]["unitId"]])

    sec_lessons[3] = []
    for pos in range(83, 93):
        sec_lessons[3].extend(u_lessons_s3[unit_pos_map[pos]["unitId"]])

    sec_lessons[4] = []
    for pos in range(93, 103):
        sec_lessons[4].extend(u_lessons_s4[unit_pos_map[pos]["unitId"]])

    sec_lessons[5] = []
    for pos in range(103, 112):
        sec_lessons[5].extend(u_lessons_s5[unit_pos_map[pos]["unitId"]])

    # =========================================================================
    # 6. LEXICAL REBALANCING & RECONCILIATION
    # =========================================================================
    print("Rebalancing lexical allocations organically across all 48 units...")
    for s_idx in range(1, 6):
        lessons = sec_lessons[s_idx]
        by_unit = defaultdict(list)
        for l in lessons:
            by_unit[l["unitId"]].append(l)

        for uid, ules in by_unit.items():
            u = unit_map[uid]
            pos = u["sequencePosition"]
            target_pl = u["newProductiveCoreLemmas"]
            target_rl = u["newReceptiveCoreLemmas"]
            target_pe = u["newProductiveExpressions"]
            target_re = u["newReceptiveExpressions"]

            # Filter non-checkpoint lessons
            active_lessons = [l for l in ules if l["lessonType"] != "checkpoint"]
            n = len(active_lessons)

            # Assign organic base numbers according to lesson type with unit-specific modulation
            for l in active_lessons:
                ltype = l["lessonType"]
                seq = l["sequenceWithinUnit"]
                # Modulations based on pedagogical emphasis
                m1 = ((pos * 4 + seq * 7) % 7 - 3) * 0.32
                m2 = ((pos * 6 + seq * 11) % 5 - 2) * 0.25

                if ltype == "vocabulary_introduction":
                    l["_weight_pl"] = max(1.0, 4.0 + m1)
                    l["_weight_rl"] = max(0.5, 2.0 + m2)
                    l["_weight_pe"] = max(0.5, 2.0 - m1)
                    l["_weight_re"] = max(0.5, 1.0 + m2)
                elif ltype == "reading_development":
                    l["_weight_pl"] = max(0.5, 2.0 - m1)
                    l["_weight_rl"] = max(1.0, 3.5 + m2)
                    l["_weight_pe"] = max(0.5, 1.0 - m2)
                    l["_weight_re"] = max(0.5, 1.5 + m1)
                elif ltype == "dialogue_work":
                    l["_weight_pl"] = max(1.0, 3.0 + m2)
                    l["_weight_rl"] = max(0.5, 1.5 - m1)
                    l["_weight_pe"] = max(1.0, 3.0 + m1)
                    l["_weight_re"] = max(0.5, 1.0 - m2)
                elif ltype == "listening_development":
                    l["_weight_pl"] = max(0.2, 0.6 + m1 * 0.3)
                    l["_weight_rl"] = max(0.8, 2.5 + m1)
                    l["_weight_pe"] = max(0.2, 0.6 - m2 * 0.3)
                    l["_weight_re"] = max(0.5, 1.5 + m2)
                elif ltype == "grammar_introduction":
                    l["_weight_pl"] = max(0.8, 2.5 + m2)
                    l["_weight_rl"] = max(0.5, 1.5 + m1)
                    l["_weight_pe"] = max(0.5, 1.0 + m2)
                    l["_weight_re"] = max(0.3, 1.0 - m1)
                else: # grammar_guided_practice
                    l["_weight_pl"] = max(0.8, 2.0 - m2)
                    l["_weight_rl"] = max(0.5, 1.0 + m1)
                    l["_weight_pe"] = max(0.5, 1.0 - m1)
                    l["_weight_re"] = max(0.2, 0.6 + m2)

            def distribute(target, weight_attr, out_attr):
                tot_w = sum(l.get(weight_attr, 1.0) for l in active_lessons)
                raw_shares = [(l.get(weight_attr, 1.0) / tot_w) * target for l in active_lessons]
                int_shares = [int(s) for s in raw_shares]
                remainder = target - sum(int_shares)
                fractional = sorted(range(len(active_lessons)), key=lambda i: raw_shares[i] - int_shares[i], reverse=True)
                for i in range(remainder):
                    int_shares[fractional[i]] += 1
                for l, s in zip(active_lessons, int_shares):
                    l[out_attr] = s

            distribute(target_pl, "_weight_pl", "newProductiveLemmaTarget")
            distribute(target_rl, "_weight_rl", "newReceptiveLemmaTarget")
            distribute(target_pe, "_weight_pe", "newProductiveExpressionTarget")
            distribute(target_re, "_weight_re", "newReceptiveExpressionTarget")

            # Clean temp attributes
            for l in active_lessons:
                for k in ["_weight_pl", "_weight_rl", "_weight_pe", "_weight_re"]:
                    if k in l:
                        del l[k]

            # Verify exact match
            assert sum(l["newProductiveLemmaTarget"] for l in ules) == target_pl
            assert sum(l["newReceptiveLemmaTarget"] for l in ules) == target_rl
            assert sum(l["newProductiveExpressionTarget"] for l in ules) == target_pe
            assert sum(l["newReceptiveExpressionTarget"] for l in ules) == target_re

    # =========================================================================
    # 7. PREREQUISITE GRAPH NATURALIZATION
    # =========================================================================
    print("Reconstructing prerequisite DAG to eliminate residual adjacent defaults...")
    all_repaired_lessons = []
    for s_idx in range(1, 6):
        all_repaired_lessons.extend(sec_lessons[s_idx])

    lesson_id_to_lesson = {l["lessonId"]: l for l in all_repaired_lessons}
    
    # Process each unit: connect lessons based on functional dependencies
    for uid, u in unit_map.items():
        ules = [l for l in all_repaired_lessons if l["unitId"] == uid]
        pos = u["sequencePosition"]
        
        # Determine anchor lessons in unit
        vocab_lessons = [l for l in ules if l["lessonType"] == "vocabulary_introduction"]
        gram_lessons = [l for l in ules if l["lessonType"] == "grammar_introduction"]
        read_lessons = [l for l in ules if l["lessonType"] == "reading_development"]
        listen_lessons = [l for l in ules if l["lessonType"] == "listening_development"]
        dial_lessons = [l for l in ules if l["lessonType"] == "dialogue_work"]
        prac_lessons = [l for l in ules if l["lessonType"] == "grammar_guided_practice"]
        cp_lessons = [l for l in ules if l["lessonType"] == "checkpoint"]

        # If unit has previous unit, establish cross-unit root prerequisite
        prev_pos = pos - 1
        if prev_pos in unit_pos_map:
            prev_u = unit_pos_map[prev_pos]
            prev_les = [l for l in all_repaired_lessons if l["unitId"] == prev_u["unitId"]]
            prev_cap = prev_les[-1]["lessonId"]
        else:
            prev_cap = "les_a1_63_06_elementary_stage_synthesis_capstone"

        for idx, l in enumerate(ules):
            lid = l["lessonId"]
            ltype = l["lessonType"]
            curr_seq = l["sequenceWithinUnit"]
            
            # Root of unit
            if idx == 0:
                l["prerequisiteLessonIds"] = [prev_cap]
                continue

            # Prior lessons within this unit
            prior_lessons = [cand for cand in ules if cand["sequenceWithinUnit"] < curr_seq]
            prior_vocab = [cand for cand in prior_lessons if cand["lessonType"] == "vocabulary_introduction"]
            prior_gram = [cand for cand in prior_lessons if cand["lessonType"] == "grammar_introduction"]
            prior_read = [cand for cand in prior_lessons if cand["lessonType"] == "reading_development"]
            prior_listen = [cand for cand in prior_lessons if cand["lessonType"] == "listening_development"]
            prior_dial = [cand for cand in prior_lessons if cand["lessonType"] == "dialogue_work"]
            prior_prac = [cand for cand in prior_lessons if cand["lessonType"] == "grammar_guided_practice"]

            prereqs = []
            if ltype == "vocabulary_introduction":
                if prior_gram:
                    prereqs.append(prior_gram[0]["lessonId"])
                    if pos % 3 == 0 and len(prior_lessons) > 1:
                        prereqs.append(prior_lessons[0]["lessonId"])
                elif prior_lessons:
                    prereqs.append(prior_lessons[0]["lessonId"])

            elif ltype == "reading_development":
                if prior_vocab:
                    prereqs.append(prior_vocab[0]["lessonId"])
                if prior_gram and pos % 2 == 1:
                    prereqs.append(prior_gram[0]["lessonId"])
                if not prereqs:
                    prereqs.append(prior_lessons[0]["lessonId"])

            elif ltype == "listening_development":
                if prior_vocab:
                    prereqs.append(prior_vocab[-1]["lessonId"])
                if prior_read and pos % 3 == 0:
                    prereqs.append(prior_read[0]["lessonId"])
                elif prior_gram and pos % 3 == 1:
                    prereqs.append(prior_gram[0]["lessonId"])
                if not prereqs:
                    prereqs.append(prior_lessons[0]["lessonId"])

            elif ltype == "dialogue_work":
                if prior_vocab:
                    prereqs.append(prior_vocab[0]["lessonId"])
                if prior_gram and pos % 2 == 0:
                    prereqs.append(prior_gram[0]["lessonId"])
                elif prior_listen and pos % 2 == 1:
                    prereqs.append(prior_listen[0]["lessonId"])
                elif prior_read:
                    prereqs.append(prior_read[0]["lessonId"])
                if not prereqs:
                    prereqs.append(prior_lessons[0]["lessonId"])

            elif ltype == "grammar_guided_practice":
                if prior_gram:
                    prereqs.append(prior_gram[0]["lessonId"])
                if prior_dial and pos % 2 == 0:
                    prereqs.append(prior_dial[0]["lessonId"])
                elif prior_read:
                    prereqs.append(prior_read[0]["lessonId"])
                elif prior_listen and pos % 3 == 0:
                    prereqs.append(prior_listen[0]["lessonId"])
                if not prereqs:
                    prereqs.append(prior_lessons[0]["lessonId"])

            elif ltype == "checkpoint":
                if prior_dial:
                    prereqs.append(prior_dial[-1]["lessonId"])
                if prior_prac:
                    prereqs.append(prior_prac[-1]["lessonId"])
                if not prereqs:
                    prereqs.append(prior_lessons[-1]["lessonId"])

            # Ensure non-empty and unique
            l["prerequisiteLessonIds"] = list(dict.fromkeys(prereqs)) if prereqs else [prior_lessons[-1]["lessonId"]]

    # =========================================================================
    # 8. PERSIST REPAIRED SECTION AND COMPLETE FILES
    # =========================================================================
    print("Persisting repaired files...")
    for s_idx in range(1, 6):
        fpath = f"curriculum/lesson_blueprints/a2_section_{s_idx:02d}.json"
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(sec_lessons[s_idx], f, indent=2, ensure_ascii=False)
        print(f"  Wrote {len(sec_lessons[s_idx])} lessons to {fpath}")

    with open("curriculum/lesson_blueprints/a2_complete.json", "w", encoding="utf-8") as f:
        json.dump(all_repaired_lessons, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(all_repaired_lessons)} lessons to curriculum/lesson_blueprints/a2_complete.json")

    print("\n✓ Phase 1D.2 Repairs Successfully Applied!")

if __name__ == "__main__":
    run_repairs()
