import * as fs from "fs";
import { LessonBlueprint } from "./lessonBlueprintTypes";

// 1. Read existing pilotLessons.json
const rawData = fs.readFileSync("curriculum/pilot/pilotLessons.json", "utf-8");
const lessons: LessonBlueprint[] = JSON.parse(rawData);

console.log(`Loaded ${lessons.length} lessons. Beginning repair...`);

// Mapping of Unit ID to Lesson Array
const unitMap = new Map<string, LessonBlueprint[]>();
lessons.forEach(l => {
  if (!unitMap.has(l.unitId)) unitMap.set(l.unitId, []);
  unitMap.get(l.unitId)!.push(l);
});

// Helper to look up by prefix (e.g. "les_pre_a1_06_03" or "les_a1_16_06")
function getLes(idSub: string): LessonBlueprint {
  const l = lessons.find(x => x.lessonId.startsWith(idSub));
  if (!l) throw new Error(`Could not find lesson with identifier prefix: ${idSub}`);
  return l;
}

// =========================================================================
// STEP 1: CONVERT UNNECESSARY CHECKPOINTS INTO REAL LEARNING EXPERIENCES
// Keep genuine milestones as checkpoints:
//  - Unit 4 pos 5: Consonant/phoneme inventory milestone (Pre-A1 Script milestone 1) -> KEEP CHECKPOINT
//  - Unit 10 pos 6: Vowel Harmony Comprehensive Milestone (Major Phonology/Grammar hurdle) -> KEEP CHECKPOINT
//  - Unit 11 pos 5: Iotated Letters & Signs Milestone (Orthography complete) -> KEEP CHECKPOINT
//  - Unit 15 pos 5: Pre-A1 Integrated Environmental Literacy Benchmark Exam (Pre-A1 Capstone) -> KEEP CHECKPOINT
//  - Unit 19 pos 6: Polar Inquiries & Nominal Predication Synthesis (Mid-Section milestone) -> KEEP CHECKPOINT
//  - Unit 23 pos 6: A1 Section 1 Comprehensive Benchmark Examination (Section 1 Capstone) -> KEEP CHECKPOINT
// Total retained checkpoints: 6 (5.0% of 120 lessons).
// Convert the other 15 checkpoints into authentic learning experiences:
// =========================================================================

// Unit 3 pos 5: les_pre_a1_03_05
const u3_5 = getLes("les_pre_a1_03_05");
u3_5.lessonType = "listening_development";
u3_5.title = "Vowel Discrimination & Acoustic Ear Training: The 7 Vowels";
u3_5.primaryPurpose = "Develop acute auditory discrimination of the seven cardinal short vowels across minimal pairs in connected monosyllables and disyllables.";
u3_5.recommendedExerciseModalities = ["phonetic_discrimination", "dictation", "matching"];

// Unit 5 pos 4: les_pre_a1_05_04 (FLAG 1)
const u5_4 = getLes("les_pre_a1_05_04");
u5_4.lessonType = "writing";
u5_4.title = "Digital Composition Workshop: Typing Personal Names & Search Queries";
u5_4.primaryPurpose = "Apply keyboard touch-typing skills to practical digital tasks: composing short name searches, contact notes, and digital messaging.";
u5_4.communicativeOutcome = "Type search queries, names, and numbers into digital interfaces smoothly without keyboard-hunting.";
u5_4.recommendedExerciseModalities = ["typing", "short_answer_writing", "cloze"];

// Unit 6 pos 5: les_pre_a1_06_05
const u6_5 = getLes("les_pre_a1_06_05");
u6_5.lessonType = "dialogue_work";
u6_5.title = "Classroom Immersion Simulation: Following Teacher Directives & Counting";
u6_5.primaryPurpose = "Engage in an interactive classroom simulation following teacher instructions, exchanging numbers, and requesting clarification in Mongolian.";
u6_5.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "matching"];

// Unit 7 pos 5: les_pre_a1_07_05
const u7_5 = getLes("les_pre_a1_07_05");
u7_5.lessonType = "writing";
u7_5.title = "Form-Filling Workshop: Official Registration & Border ID Cards";
u7_5.primaryPurpose = "Guide learners through authentic administrative registration, filling out guest registry and conference badge cards accurately in Cyrillic.";
u7_5.recommendedExerciseModalities = ["typing", "short_answer_writing", "matching"];

// Unit 8 pos 5: les_pre_a1_08_05
const u8_5 = getLes("les_pre_a1_08_05");
u8_5.lessonType = "phonology_introduction";
u8_5.title = "Acoustic Minimal Pair Lab: Contrastive Vowel Duration Drills";
u8_5.primaryPurpose = "Solidify perception and production of phonemic vowel length contrasts through high-speed audio discrimination drills and vocalization.";
u8_5.recommendedExerciseModalities = ["phonetic_discrimination", "dictation", "matching"];

// Unit 9 pos 4: les_pre_a1_09_04
const u9_4 = getLes("les_pre_a1_09_04");
u9_4.lessonType = "reading_development";
u9_4.title = "Authentic Decoding Workshop: Reading Everyday Diphthong Stems";
u9_4.primaryPurpose = "Develop fluent, confident reading of high-frequency words containing diphthongs in authentic contextual sentences.";
u9_4.recommendedExerciseModalities = ["reading_comprehension", "matching", "cloze"];

// Unit 12 pos 5: les_pre_a1_12_05
const u12_5 = getLes("les_pre_a1_12_05");
u12_5.lessonType = "dialogue_work";
u12_5.title = "Survival Conversation Lab: Fluency in Initial Encounters & Farewells";
u12_5.primaryPurpose = "Engage in timed conversational roleplays executing natural greeting and parting rituals with native stress and syllable rhythm.";
u12_5.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "word_ordering"];

// Unit 13 pos 5: les_pre_a1_13_05
const u13_5 = getLes("les_pre_a1_13_05");
u13_5.lessonType = "dialogue_work";
u13_5.title = "Social Politeness Simulation: Navigating Everyday Courtesy & Apologies";
u13_5.primaryPurpose = "Practice authentic social etiquette in spontaneous real-world situations: thanking hosts, bumping into strangers, and accepting apologies.";
u13_5.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "matching"];

// Unit 14 pos 5: les_pre_a1_14_05
const u14_5 = getLes("les_pre_a1_14_05");
u14_5.lessonType = "reading_development";
u14_5.title = "Urban Navigation Workshop: Deciphering Street Architecture & Transit Signs";
u14_5.primaryPurpose = "Read authentic public transit schedules, entrance/exit signs, and commercial storefront notices in Ulaanbaatar.";
u14_5.recommendedExerciseModalities = ["reading_comprehension", "matching", "short_answer_writing"];

// Unit 16 pos 6: les_a1_16_06 (FLAG 3)
const u16_6 = getLes("les_a1_16_06");
u16_6.lessonType = "listening_development";
u16_6.title = "Connected Speech Lab: Tracking Daily Salutations & SOV Word Order";
u16_6.primaryPurpose = "Develop connected-discourse listening comprehension by tracking multi-turn greetings and parsing canonical SOV structure in native recorded audio.";
u16_6.communicativeOutcome = "Extract speaker identities, time-of-day greetings, and conversational intentions from multi-speaker dialogue tracks.";
u16_6.recommendedExerciseModalities = ["dictation", "role_play_response", "dialogue_completion"];

// Unit 17 pos 6: les_a1_17_06
const u17_6 = getLes("les_a1_17_06");
u17_6.lessonType = "dialogue_work";
u17_6.title = "Social Address Workshop: Roleplaying Register Shifts (Чи vs Та)";
u17_6.primaryPurpose = "Navigate dynamic conversational encounters requiring swift social register shifts between peers (чи), elders/officials (та), and group audiences (та нар).";
u17_6.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "word_ordering"];

// Unit 18 pos 6: les_a1_18_06
const u18_6 = getLes("les_a1_18_06");
u18_6.lessonType = "dialogue_work";
u18_6.title = "Participant Networking Simulation: Self-Introductions & Origin Exchange";
u18_6.primaryPurpose = "Engage in an international networking simulation, introducing oneself, asking peers about their hometowns, and verifying participant rosters.";
u18_6.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "short_answer_writing"];

// Unit 20 pos 6: les_a1_20_06
const u20_6 = getLes("les_a1_20_06");
u20_6.lessonType = "dialogue_work";
u20_6.title = "Interactive Workplace Tour: Deictic Identification & Object Inquiries";
u20_6.primaryPurpose = "Lead and participate in an office tour, pointing to equipment, furniture, and rooms using proximal and distal demonstratives.";
u20_6.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "word_ordering"];

// Unit 21 pos 6: les_a1_21_06 (FLAG 5)
const u21_6 = getLes("les_a1_21_06");
u21_6.lessonType = "dialogue_work";
u21_6.title = "Communicative Negation Workshop: Clarifying Misconceptions & Polite Corrections";
u21_6.primaryPurpose = "Engage in realistic conversational scenarios requiring active, polite correction of false assumptions regarding identity, nationality, and items.";
u21_6.communicativeOutcome = "Politely correct misunderstandings in real time using 'биш' and 'харин' without conversational friction.";
u21_6.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "word_ordering"];

// Unit 22 pos 5: les_a1_22_05
const u22_5 = getLes("les_a1_22_05");
u22_5.lessonType = "dialogue_work";
u22_5.title = "Social Departure & Host Gratitude Simulation";
u22_5.primaryPurpose = "Enact full farewell sequences when departing dinner parties, hotel reception desks, and offices with appropriate gratitude formulas.";
u22_5.recommendedExerciseModalities = ["role_play_response", "dialogue_completion", "matching"];

// =========================================================================
// STEP 2: REPAIR THE REMAINING FLAGGED LESSONS (FLAG 2, FLAG 4, FLAG 6)
// =========================================================================

// FLAG 6: les_pre_a1_15_01
const u15_1 = getLes("les_pre_a1_15_01");
u15_1.title = "Systematic Alphabet Audit: Staged Grapheme Decoding & Rapid Identification";
u15_1.primaryPurpose = "Conduct a structured diagnostic review of the 35 Cyrillic characters organized into three distinct structural cohorts: shared glyphs, distinct vowels, and palatalized/compound signs.";
u15_1.readingObjective = "Rapidly decode 3 staged blocks of letterforms (shared Latin-Cyrillic, Mongolian-specific vowels, and iotated/sign characters) with accurate phonetic vocalization.";
u15_1.successCriteria = [
  "Accurately name and vocalize all characters in each of the three structural alphabet cohorts.",
  "Distinguish uppercase and lowercase pairs across both handwritten and printed fonts."
];
u15_1.masteryEvidence = [
  "Instantly identifies Ө and Ү without vocal hesitation.",
  "Accurately transcribes letters into correct alphabetical groupings."
];

// FLAG 4: les_a1_18_01
const u18_1 = getLes("les_a1_18_01");
u18_1.title = "Unmarked Nominative Arguments & The Zero-Copula Predication Principle";
u18_1.primaryPurpose = "Establish the core principle of nominal equative clauses: in present tense, unmarked nominative subjects link directly to predicate nouns with zero auxiliary or copula verb.";
u18_1.readingObjective = "Read 5 basic equative sentences (Subject Noun + Predicate Noun) and identify the absence of any overt copular verb.";
u18_1.writingObjective = "Construct 4 minimal equative pairs linking personal pronouns with basic profession nouns.";
u18_1.successCriteria = [
  "Form 5 zero-copula sentences without inserting an auxiliary verb.",
  "Identify unmarked nominative subject and predicate nominal arguments correctly."
];

// FLAG 2: les_pre_a1_15_05
const u15_5 = getLes("les_pre_a1_15_05");
u15_5.primaryPurpose = "Administer the Pre-A1 literacy and survival capstone examination, assessing core Cyrillic decoding, vowel length discrimination, numbers 0-10, and formulaic greeting reception.";
u15_5.successCriteria = [
  "Accurately decode 10 authentic street and storefront signs.",
  "Identify spoken greetings and numbers 0-10 with native accuracy in audio comprehension tasks."
];
u15_5.masteryEvidence = [
  "Demonstrates complete, self-reliant decoding of standard Cyrillic print.",
  "Transcribes dictated basic words and numbers with high orthographic fidelity."
];

// =========================================================================
// STEP 3: RECONCILE LEXICAL BUDGETS PEDAGOGICALLY & INTRODUCE ZERO-VOCAB LESSONS
// Checkpoints, capstones, and pure dialogue/fluency synthesis should have 0 new vocabulary.
// Fix Unit 15 target mismatch: Authoritative target is Prod=10, Rec=4, ProdExp=3, RecExp=2.
// =========================================================================

unitMap.forEach((uLessons, uId) => {
  // Reset all to zero initially
  uLessons.forEach(l => {
    l.newProductiveLemmaTarget = 0;
    l.newReceptiveLemmaTarget = 0;
    l.newProductiveExpressionTarget = 0;
    l.newReceptiveExpressionTarget = 0;
  });

  if (uId === "unit_pre_a1_01_alphabet_consonants_intro") {
    // 4 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_02_mongolian_distinct_letters") {
    // 4 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 2; uLessons[1].newReceptiveLemmaTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_03_cardinal_short_vowels") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 2; uLessons[1].newReceptiveLemmaTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_04_consonants_inventory_stops") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 2; uLessons[1].newReceptiveLemmaTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_05_cyrillic_keyboard_mastery") {
    // 4 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_06_digits_and_classroom_prompts") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 4; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 4; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 0; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1; // ZERO productive
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_07_personal_names_and_identification") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_08_vowel_length_pairs") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 2; uLessons[1].newReceptiveLemmaTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_09_diphthongs_inventory") {
    // 4 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 2; uLessons[1].newReceptiveLemmaTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_10_masculine_feminine_harmony") {
    // 6 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_11_iotated_vowels_signs") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_12_survival_greetings_farewells") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_13_gratitude_apologies_politeness") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_14_public_signs_and_notices") {
    // 5 lessons. Target: Prod=8, Rec=3, ProdExp=2, RecExp=1
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 3; uLessons[1].newReceptiveLemmaTarget = 1; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 2; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_pre_a1_15_pre_a1_synthesis_and_literacy_capstone") {
    // 6 lessons. Authoritative Target: Prod=10, Rec=4, ProdExp=3, RecExp=2
    // Missing vocab allocated cleanly to early literacy & environment print lessons
    uLessons[0].newProductiveLemmaTarget = 3; uLessons[0].newReceptiveLemmaTarget = 1; uLessons[0].newProductiveExpressionTarget = 1; uLessons[0].newReceptiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 4; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 0; uLessons[3].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO (Capstone exam)
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO (Graduation roleplay)
  } else if (uId === "unit_a1_16_standard_salutations_time_of_day_gr") {
    // 6 lessons. Target: Prod=17, Rec=6, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1; uLessons[0].newReceptiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_17_personal_pronouns_direct_address_pr") {
    // 6 lessons. Target: Prod=17, Rec=6, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1; uLessons[3].newReceptiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_18_zero_copula_identity_origin_predica") {
    // 6 lessons. Target: Prod=19, Rec=7, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1; // FLAG 4 addressed
    uLessons[1].newProductiveLemmaTarget = 6; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 5; uLessons[2].newReceptiveLemmaTarget = 2; uLessons[2].newProductiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1; uLessons[3].newReceptiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_19_polar_inquiries_polar_question_part") {
    // 6 lessons. Target: Prod=17, Rec=6, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1; uLessons[3].newReceptiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO (Checkpoint)
  } else if (uId === "unit_a1_20_demonstrative_deixis_") {
    // 6 lessons. Target: Prod=17, Rec=6, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1; uLessons[3].newReceptiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_21_negative_nominal_assertion_the_copu") {
    // 6 lessons. Target: Prod=17, Rec=6, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 3; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1; uLessons[3].newReceptiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_22_formal_departure_social_gratitude_f") {
    // 5 lessons. Target: Prod=15, Rec=5, ProdExp=4, RecExp=2
    uLessons[0].newProductiveLemmaTarget = 5; uLessons[0].newReceptiveLemmaTarget = 2; uLessons[0].newProductiveExpressionTarget = 1; uLessons[0].newReceptiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 5; uLessons[1].newReceptiveLemmaTarget = 2; uLessons[1].newProductiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 3; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 2; uLessons[3].newReceptiveLemmaTarget = 0; uLessons[3].newProductiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
  } else if (uId === "unit_a1_23_section_synthesis_social_reception_") {
    // 6 lessons. Target: Prod=20, Rec=8, ProdExp=6, RecExp=3
    uLessons[0].newProductiveLemmaTarget = 7; uLessons[0].newReceptiveLemmaTarget = 3; uLessons[0].newProductiveExpressionTarget = 2; uLessons[0].newReceptiveExpressionTarget = 1;
    uLessons[1].newProductiveLemmaTarget = 7; uLessons[1].newReceptiveLemmaTarget = 3; uLessons[1].newProductiveExpressionTarget = 2; uLessons[1].newReceptiveExpressionTarget = 1;
    uLessons[2].newProductiveLemmaTarget = 4; uLessons[2].newReceptiveLemmaTarget = 1; uLessons[2].newProductiveExpressionTarget = 1; uLessons[2].newReceptiveExpressionTarget = 1;
    uLessons[3].newProductiveLemmaTarget = 2; uLessons[3].newReceptiveLemmaTarget = 1; uLessons[3].newProductiveExpressionTarget = 1;
    uLessons[4].newProductiveLemmaTarget = 0; uLessons[4].newReceptiveLemmaTarget = 0; // ZERO
    uLessons[5].newProductiveLemmaTarget = 0; uLessons[5].newReceptiveLemmaTarget = 0; // ZERO (Capstone exam)
  }
});

// =========================================================================
// STEP 4: SEPARATE COURSE SEQUENCE FROM TRUE PREREQUISITE DAG
// Replace linear single-chain [i-1] with true linguistic dependencies
// =========================================================================

lessons.forEach(l => {
  l.prerequisiteLessonIds = []; // clear artificial [i-1]
});

// Unit 1: Alphabet & Consonants Intro
getLes("les_pre_a1_01_01").prerequisiteLessonIds = []; // True curriculum entry point
getLes("les_pre_a1_01_02").prerequisiteLessonIds = [getLes("les_pre_a1_01_01").lessonId];
getLes("les_pre_a1_01_03").prerequisiteLessonIds = [getLes("les_pre_a1_01_01").lessonId, getLes("les_pre_a1_01_02").lessonId];
getLes("les_pre_a1_01_04").prerequisiteLessonIds = [getLes("les_pre_a1_01_03").lessonId];

// Unit 2: Distinct Letters Ө and Ү
getLes("les_pre_a1_02_01").prerequisiteLessonIds = [getLes("les_pre_a1_01_01").lessonId];
getLes("les_pre_a1_02_02").prerequisiteLessonIds = [getLes("les_pre_a1_02_01").lessonId];
getLes("les_pre_a1_02_03").prerequisiteLessonIds = [getLes("les_pre_a1_02_02").lessonId];
getLes("les_pre_a1_02_04").prerequisiteLessonIds = [getLes("les_pre_a1_01_04").lessonId, getLes("les_pre_a1_02_03").lessonId];

// Unit 3: Cardinal Short Vowels
getLes("les_pre_a1_03_01").prerequisiteLessonIds = [getLes("les_pre_a1_02_01").lessonId];
getLes("les_pre_a1_03_02").prerequisiteLessonIds = [getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_03_03").prerequisiteLessonIds = [getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_03_04").prerequisiteLessonIds = [getLes("les_pre_a1_01_03").lessonId, getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_03_05").prerequisiteLessonIds = [getLes("les_pre_a1_03_02").lessonId, getLes("les_pre_a1_03_04").lessonId];

// Unit 4: Consonant Inventory: Obstruents & Sonorants
getLes("les_pre_a1_04_01").prerequisiteLessonIds = [getLes("les_pre_a1_01_01").lessonId];
getLes("les_pre_a1_04_02").prerequisiteLessonIds = [getLes("les_pre_a1_04_01").lessonId];
getLes("les_pre_a1_04_03").prerequisiteLessonIds = [getLes("les_pre_a1_04_01").lessonId];
getLes("les_pre_a1_04_04").prerequisiteLessonIds = [getLes("les_pre_a1_01_04").lessonId, getLes("les_pre_a1_04_01").lessonId];
getLes("les_pre_a1_04_05").prerequisiteLessonIds = [getLes("les_pre_a1_04_02").lessonId, getLes("les_pre_a1_04_03").lessonId, getLes("les_pre_a1_03_01").lessonId];

// Unit 5: Keyboard Mastery (Depends on Script Units 1, 2, 4)
getLes("les_pre_a1_05_01").prerequisiteLessonIds = [getLes("les_pre_a1_01_01").lessonId, getLes("les_pre_a1_04_01").lessonId];
getLes("les_pre_a1_05_02").prerequisiteLessonIds = [getLes("les_pre_a1_02_01").lessonId, getLes("les_pre_a1_05_01").lessonId];
getLes("les_pre_a1_05_03").prerequisiteLessonIds = [getLes("les_pre_a1_05_02").lessonId];
getLes("les_pre_a1_05_04").prerequisiteLessonIds = [getLes("les_pre_a1_05_03").lessonId];

// Unit 6: Digits & Classroom Prompts
getLes("les_pre_a1_06_01").prerequisiteLessonIds = [getLes("les_pre_a1_01_03").lessonId];
getLes("les_pre_a1_06_02").prerequisiteLessonIds = [getLes("les_pre_a1_06_01").lessonId];
getLes("les_pre_a1_06_03").prerequisiteLessonIds = [getLes("les_pre_a1_01_03").lessonId];
getLes("les_pre_a1_06_04").prerequisiteLessonIds = [getLes("les_pre_a1_06_03").lessonId];
getLes("les_pre_a1_06_05").prerequisiteLessonIds = [getLes("les_pre_a1_06_02").lessonId, getLes("les_pre_a1_06_04").lessonId];

// Unit 7: Personal Names & Identification
getLes("les_pre_a1_07_01").prerequisiteLessonIds = [getLes("les_pre_a1_04_03").lessonId, getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_07_02").prerequisiteLessonIds = [getLes("les_pre_a1_07_01").lessonId];
getLes("les_pre_a1_07_03").prerequisiteLessonIds = [getLes("les_pre_a1_06_02").lessonId, getLes("les_pre_a1_07_01").lessonId];
getLes("les_pre_a1_07_04").prerequisiteLessonIds = [getLes("les_pre_a1_07_03").lessonId, getLes("les_pre_a1_05_03").lessonId];
getLes("les_pre_a1_07_05").prerequisiteLessonIds = [getLes("les_pre_a1_07_04").lessonId];

// Unit 8: Vowel Length Pairs
getLes("les_pre_a1_08_01").prerequisiteLessonIds = [getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_08_02").prerequisiteLessonIds = [getLes("les_pre_a1_08_01").lessonId];
getLes("les_pre_a1_08_03").prerequisiteLessonIds = [getLes("les_pre_a1_08_02").lessonId];
getLes("les_pre_a1_08_04").prerequisiteLessonIds = [getLes("les_pre_a1_08_03").lessonId];
getLes("les_pre_a1_08_05").prerequisiteLessonIds = [getLes("les_pre_a1_08_04").lessonId];

// Unit 9: Diphthongs Inventory
getLes("les_pre_a1_09_01").prerequisiteLessonIds = [getLes("les_pre_a1_08_01").lessonId];
getLes("les_pre_a1_09_02").prerequisiteLessonIds = [getLes("les_pre_a1_09_01").lessonId];
getLes("les_pre_a1_09_03").prerequisiteLessonIds = [getLes("les_pre_a1_09_02").lessonId];
getLes("les_pre_a1_09_04").prerequisiteLessonIds = [getLes("les_pre_a1_09_03").lessonId];

// Unit 10: Masculine & Feminine Harmony
getLes("les_pre_a1_10_01").prerequisiteLessonIds = [getLes("les_pre_a1_03_01").lessonId];
getLes("les_pre_a1_10_02").prerequisiteLessonIds = [getLes("les_pre_a1_10_01").lessonId];
getLes("les_pre_a1_10_03").prerequisiteLessonIds = [getLes("les_pre_a1_10_02").lessonId];
getLes("les_pre_a1_10_04").prerequisiteLessonIds = [getLes("les_pre_a1_10_01").lessonId, getLes("les_pre_a1_10_02").lessonId];
getLes("les_pre_a1_10_05").prerequisiteLessonIds = [getLes("les_pre_a1_10_03").lessonId, getLes("les_pre_a1_10_04").lessonId];
getLes("les_pre_a1_10_06").prerequisiteLessonIds = [getLes("les_pre_a1_10_05").lessonId];

// Unit 11: Iotated Vowels & Signs
getLes("les_pre_a1_11_01").prerequisiteLessonIds = [getLes("les_pre_a1_09_01").lessonId, getLes("les_pre_a1_10_01").lessonId];
getLes("les_pre_a1_11_02").prerequisiteLessonIds = [getLes("les_pre_a1_11_01").lessonId, getLes("les_pre_a1_10_06").lessonId];
getLes("les_pre_a1_11_03").prerequisiteLessonIds = [getLes("les_pre_a1_04_03").lessonId, getLes("les_pre_a1_11_01").lessonId];
getLes("les_pre_a1_11_04").prerequisiteLessonIds = [getLes("les_pre_a1_11_03").lessonId];
getLes("les_pre_a1_11_05").prerequisiteLessonIds = [getLes("les_pre_a1_11_02").lessonId, getLes("les_pre_a1_11_04").lessonId];

// Unit 12: Survival Greetings & Departures
getLes("les_pre_a1_12_01").prerequisiteLessonIds = [getLes("les_pre_a1_04_05").lessonId, getLes("les_pre_a1_08_01").lessonId];
getLes("les_pre_a1_12_02").prerequisiteLessonIds = [getLes("les_pre_a1_12_01").lessonId];
getLes("les_pre_a1_12_03").prerequisiteLessonIds = [getLes("les_pre_a1_12_02").lessonId];
getLes("les_pre_a1_12_04").prerequisiteLessonIds = [getLes("les_pre_a1_12_03").lessonId];
getLes("les_pre_a1_12_05").prerequisiteLessonIds = [getLes("les_pre_a1_12_04").lessonId];

// Unit 13: Gratitude & Apologies
getLes("les_pre_a1_13_01").prerequisiteLessonIds = [getLes("les_pre_a1_12_02").lessonId];
getLes("les_pre_a1_13_02").prerequisiteLessonIds = [getLes("les_pre_a1_13_01").lessonId];
getLes("les_pre_a1_13_03").prerequisiteLessonIds = [getLes("les_pre_a1_13_02").lessonId];
getLes("les_pre_a1_13_04").prerequisiteLessonIds = [getLes("les_pre_a1_13_02").lessonId];
getLes("les_pre_a1_13_05").prerequisiteLessonIds = [getLes("les_pre_a1_13_03").lessonId, getLes("les_pre_a1_13_04").lessonId];

// Unit 14: Public Signs & Notices
getLes("les_pre_a1_14_01").prerequisiteLessonIds = [getLes("les_pre_a1_04_04").lessonId, getLes("les_pre_a1_08_04").lessonId];
getLes("les_pre_a1_14_02").prerequisiteLessonIds = [getLes("les_pre_a1_14_01").lessonId];
getLes("les_pre_a1_14_03").prerequisiteLessonIds = [getLes("les_pre_a1_14_01").lessonId];
getLes("les_pre_a1_14_04").prerequisiteLessonIds = [getLes("les_pre_a1_14_02").lessonId];
getLes("les_pre_a1_14_05").prerequisiteLessonIds = [getLes("les_pre_a1_14_03").lessonId, getLes("les_pre_a1_14_04").lessonId];

// Unit 15: Pre-A1 Capstone
getLes("les_pre_a1_15_01").prerequisiteLessonIds = [getLes("les_pre_a1_11_05").lessonId];
getLes("les_pre_a1_15_02").prerequisiteLessonIds = [getLes("les_pre_a1_14_05").lessonId, getLes("les_pre_a1_15_01").lessonId];
getLes("les_pre_a1_15_03").prerequisiteLessonIds = [getLes("les_pre_a1_15_02").lessonId];
getLes("les_pre_a1_15_04").prerequisiteLessonIds = [getLes("les_pre_a1_07_05").lessonId, getLes("les_pre_a1_05_04").lessonId];
getLes("les_pre_a1_15_05").prerequisiteLessonIds = [getLes("les_pre_a1_15_03").lessonId, getLes("les_pre_a1_15_04").lessonId];
getLes("les_pre_a1_15_06").prerequisiteLessonIds = [getLes("les_pre_a1_13_05").lessonId, getLes("les_pre_a1_15_05").lessonId];

// =========================================================================
// A1 Section 1: Units 16 - 23
// =========================================================================

// Unit 16: Standard Salutations & Time-of-Day (Depends on Pre-A1 formulaic greetings + literacy)
getLes("les_a1_16_01").prerequisiteLessonIds = [getLes("les_pre_a1_15_05").lessonId];
getLes("les_a1_16_02").prerequisiteLessonIds = [getLes("les_a1_16_01").lessonId];
getLes("les_a1_16_03").prerequisiteLessonIds = [getLes("les_a1_16_01").lessonId];
getLes("les_a1_16_04").prerequisiteLessonIds = [getLes("les_a1_16_02").lessonId, getLes("les_a1_16_03").lessonId];
getLes("les_a1_16_05").prerequisiteLessonIds = [getLes("les_a1_16_04").lessonId];
getLes("les_a1_16_06").prerequisiteLessonIds = [getLes("les_a1_16_05").lessonId];

// Unit 17: Personal Pronouns & Direct Address (Depends on SOV baseline)
getLes("les_a1_17_01").prerequisiteLessonIds = [getLes("les_a1_16_01").lessonId];
getLes("les_a1_17_02").prerequisiteLessonIds = [getLes("les_a1_17_01").lessonId];
getLes("les_a1_17_03").prerequisiteLessonIds = [getLes("les_a1_17_02").lessonId];
getLes("les_a1_17_04").prerequisiteLessonIds = [getLes("les_a1_17_03").lessonId];
getLes("les_a1_17_05").prerequisiteLessonIds = [getLes("les_a1_17_04").lessonId];
getLes("les_a1_17_06").prerequisiteLessonIds = [getLes("les_a1_17_05").lessonId];

// Unit 18: Zero-Copula Identity & Origin (Depends on Pronouns Unit 17 + Vowel Harmony Unit 10 for ablative)
getLes("les_a1_18_01").prerequisiteLessonIds = [getLes("les_a1_17_01").lessonId];
getLes("les_a1_18_02").prerequisiteLessonIds = [getLes("les_a1_18_01").lessonId];
getLes("les_a1_18_03").prerequisiteLessonIds = [getLes("les_a1_18_02").lessonId, getLes("les_pre_a1_10_06").lessonId];
getLes("les_a1_18_04").prerequisiteLessonIds = [getLes("les_a1_18_03").lessonId];
getLes("les_a1_18_05").prerequisiteLessonIds = [getLes("les_a1_18_04").lessonId, getLes("les_a1_17_02").lessonId];
getLes("les_a1_18_06").prerequisiteLessonIds = [getLes("les_a1_18_05").lessonId];

// Unit 19: Polar Inquiries (Depends on Zero-Copula Predication Unit 18 + Vowel Harmony Unit 10)
getLes("les_a1_19_01").prerequisiteLessonIds = [getLes("les_a1_18_01").lessonId, getLes("les_pre_a1_10_06").lessonId];
getLes("les_a1_19_02").prerequisiteLessonIds = [getLes("les_a1_19_01").lessonId];
getLes("les_a1_19_03").prerequisiteLessonIds = [getLes("les_a1_19_01").lessonId, getLes("les_a1_18_02").lessonId];
getLes("les_a1_19_04").prerequisiteLessonIds = [getLes("les_a1_19_02").lessonId, getLes("les_a1_19_03").lessonId];
getLes("les_a1_19_05").prerequisiteLessonIds = [getLes("les_a1_19_04").lessonId];
getLes("les_a1_19_06").prerequisiteLessonIds = [getLes("les_a1_19_05").lessonId];

// Unit 20: Demonstrative Deixis (Depends on Zero Copula Unit 18 and Polar Inquiries Unit 19)
getLes("les_a1_20_01").prerequisiteLessonIds = [getLes("les_a1_18_01").lessonId];
getLes("les_a1_20_02").prerequisiteLessonIds = [getLes("les_a1_20_01").lessonId];
getLes("les_a1_20_03").prerequisiteLessonIds = [getLes("les_a1_20_01").lessonId, getLes("les_a1_19_01").lessonId];
getLes("les_a1_20_04").prerequisiteLessonIds = [getLes("les_a1_20_02").lessonId, getLes("les_a1_20_03").lessonId];
getLes("les_a1_20_05").prerequisiteLessonIds = [getLes("les_a1_20_04").lessonId, getLes("les_a1_17_02").lessonId];
getLes("les_a1_20_06").prerequisiteLessonIds = [getLes("les_a1_20_05").lessonId];

// Unit 21: Negative Nominal Assertion (Depends on Zero Copula Unit 18 and Polar Inquiries Unit 19)
getLes("les_a1_21_01").prerequisiteLessonIds = [getLes("les_a1_18_01").lessonId];
getLes("les_a1_21_02").prerequisiteLessonIds = [getLes("les_a1_21_01").lessonId];
getLes("les_a1_21_03").prerequisiteLessonIds = [getLes("les_a1_21_01").lessonId, getLes("les_a1_19_01").lessonId];
getLes("les_a1_21_04").prerequisiteLessonIds = [getLes("les_a1_21_02").lessonId, getLes("les_a1_20_04").lessonId];
getLes("les_a1_21_05").prerequisiteLessonIds = [getLes("les_a1_21_03").lessonId, getLes("les_pre_a1_13_05").lessonId];
getLes("les_a1_21_06").prerequisiteLessonIds = [getLes("les_a1_21_05").lessonId];

// Unit 22: Formal Departure & Social Gratitude (Builds on earlier greetings Unit 16 and politeness)
getLes("les_a1_22_01").prerequisiteLessonIds = [getLes("les_a1_16_02").lessonId];
getLes("les_a1_22_02").prerequisiteLessonIds = [getLes("les_a1_22_01").lessonId];
getLes("les_a1_22_03").prerequisiteLessonIds = [getLes("les_a1_22_01").lessonId, getLes("les_a1_22_02").lessonId];
getLes("les_a1_22_04").prerequisiteLessonIds = [getLes("les_a1_22_03").lessonId];
getLes("les_a1_22_05").prerequisiteLessonIds = [getLes("les_a1_22_04").lessonId];

// Unit 23: Section Synthesis: Social Reception (True capstone converging all threads!)
getLes("les_a1_23_01").prerequisiteLessonIds = [getLes("les_a1_16_05").lessonId, getLes("les_a1_17_02").lessonId];
getLes("les_a1_23_02").prerequisiteLessonIds = [getLes("les_a1_23_01").lessonId, getLes("les_a1_18_05").lessonId, getLes("les_a1_20_05").lessonId];
getLes("les_a1_23_03").prerequisiteLessonIds = [getLes("les_a1_23_02").lessonId, getLes("les_a1_19_05").lessonId, getLes("les_a1_21_05").lessonId];
getLes("les_a1_23_04").prerequisiteLessonIds = [getLes("les_a1_23_03").lessonId];
getLes("les_a1_23_05").prerequisiteLessonIds = [getLes("les_a1_23_04").lessonId, getLes("les_a1_22_04").lessonId];
getLes("les_a1_23_06").prerequisiteLessonIds = [getLes("les_a1_23_05").lessonId];

// =========================================================================
// STEP 5: ADD REVIEW HOOKS FOR 4 NEGLECTED PHONOLOGY TARGETS
// - phono_neutral_vowel_behavior
// - phono_iotated_vowels_behavior
// - phono_soft_and_hard_signs
// - phono_non_initial_reduction
// =========================================================================

if (!getLes("les_pre_a1_11_02").phonologyReviewed.includes("phono_neutral_vowel_behavior")) {
  getLes("les_pre_a1_11_02").phonologyReviewed.push("phono_neutral_vowel_behavior");
}
if (!getLes("les_a1_18_03").phonologyReviewed.includes("phono_neutral_vowel_behavior")) {
  getLes("les_a1_18_03").phonologyReviewed.push("phono_neutral_vowel_behavior");
}

if (!getLes("les_pre_a1_15_01").phonologyReviewed.includes("phono_iotated_vowels_behavior")) {
  getLes("les_pre_a1_15_01").phonologyReviewed.push("phono_iotated_vowels_behavior");
}
if (!getLes("les_a1_19_02").phonologyReviewed.includes("phono_iotated_vowels_behavior")) {
  getLes("les_a1_19_02").phonologyReviewed.push("phono_iotated_vowels_behavior");
}

if (!getLes("les_pre_a1_15_01").phonologyReviewed.includes("phono_soft_and_hard_signs")) {
  getLes("les_pre_a1_15_01").phonologyReviewed.push("phono_soft_and_hard_signs");
}
if (!getLes("les_pre_a1_15_03").phonologyReviewed.includes("phono_soft_and_hard_signs")) {
  getLes("les_pre_a1_15_03").phonologyReviewed.push("phono_soft_and_hard_signs");
}

if (!getLes("les_pre_a1_13_01").phonologyReviewed.includes("phono_non_initial_reduction")) {
  getLes("les_pre_a1_13_01").phonologyReviewed.push("phono_non_initial_reduction");
}
if (!getLes("les_a1_16_01").phonologyReviewed.includes("phono_non_initial_reduction")) {
  getLes("les_a1_16_01").phonologyReviewed.push("phono_non_initial_reduction");
}

// =========================================================================
// STEP 6: COMMUNICATIVE FUNCTIONS REVIEW FIELD POPULATION
// =========================================================================
function addCommRev(idSub: string, funcId: string) {
  const l = getLes(idSub);
  if (!l.communicativeFunctionsReviewed.includes(funcId)) {
    l.communicativeFunctionsReviewed.push(funcId);
  }
}

addCommRev("les_a1_16_05", "comm_pre_a1_01_exchange_survival_greetings");
addCommRev("les_a1_17_05", "comm_pre_a1_04_state_name_identify");
addCommRev("les_a1_18_05", "comm_a1_02_direct_address_honorific");
addCommRev("les_a1_21_05", "comm_pre_a1_02_express_gratitude_apologize");
addCommRev("les_a1_22_04", "comm_a1_01_time_greetings_salutations");
addCommRev("les_a1_23_01", "comm_a1_01_time_greetings_salutations");
addCommRev("les_a1_23_02", "comm_a1_03_predicate_identity_profession");
addCommRev("les_a1_23_03", "comm_a1_04_polar_confirmation");
addCommRev("les_a1_23_05", "comm_a1_06_formal_departures_gratitude");

// =========================================================================
// STEP 7: REMOVE UNNECESSARY ACCURACY PERCENTAGE TROPES IN SUCCESS CRITERIA
// =========================================================================
lessons.forEach(l => {
  l.successCriteria = l.successCriteria.map(sc => {
    return sc
      .replace(/with 100% accuracy/gi, "consistently and accurately")
      .replace(/with at least 90% accuracy/gi, "fluently and reliably")
      .replace(/with at least 80% accuracy/gi, "accurately")
      .replace(/achieve at least 90% on/gi, "successfully demonstrate mastery in")
      .replace(/achieve 100% on/gi, "confidently complete");
  });
});

// Write repaired data back to curriculum/pilot/pilotLessons.json
fs.writeFileSync("curriculum/pilot/pilotLessons.json", JSON.stringify(lessons, null, 2), "utf-8");
console.log("Repairs successfully written to curriculum/pilot/pilotLessons.json.");
