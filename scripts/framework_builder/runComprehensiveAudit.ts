import * as fs from "fs";
import { LessonBlueprint } from "./lessonBlueprintTypes";

const filePath = process.argv[2] || "curriculum/pilot/pilotLessons.json";
console.log(`Auditing file: ${filePath}`);
const rawData = fs.readFileSync(filePath, "utf-8");
const lessons: LessonBlueprint[] = JSON.parse(rawData);

console.log("=================================================================");
console.log("PHASE 1C.1 POST-REPAIR FORENSIC VERIFICATION AUDIT");
console.log("=================================================================");

// 1. Total Records & Basic Counts
console.log(`Total Lesson Records: ${lessons.length}`);
const preA1Lessons = lessons.filter(l => l.cefrLevel === "Pre-A1");
const a1Lessons = lessons.filter(l => l.cefrLevel === "A1");
console.log(`Pre-A1 Lessons: ${preA1Lessons.length}`);
console.log(`A1 Section 1 Lessons: ${a1Lessons.length}`);

// 2. Lesson Type Distribution & Checkpoint Density
const typeCounts: Record<string, number> = {};
lessons.forEach(l => {
  typeCounts[l.lessonType] = (typeCounts[l.lessonType] || 0) + 1;
});
console.log("\nLesson Type Distribution:");
Object.entries(typeCounts).sort((a, b) => b[1] - a[1]).forEach(([type, count]) => {
  const pct = ((count / lessons.length) * 100).toFixed(1);
  console.log(`  - ${type.padEnd(25)}: ${count.toString().padStart(3)} (${pct}%)`);
});

const checkpointCount = typeCounts["checkpoint"] || 0;
const checkpointPct = ((checkpointCount / lessons.length) * 100).toFixed(1);
console.log(`\nCheckpoint Density: ${checkpointCount} / ${lessons.length} (${checkpointPct}%)`);
console.log(`Target: ~5-10% (Reduced from 17.5% / 21 checkpoints)`);

// 3. DAG Structure Metrics
let totalPrereqEdges = 0;
let linearIndexMinus1Count = 0;
let branchingInNodes = 0;
let branchingOutNodes = 0;
let trueRoots = 0;

const outDegree: Record<string, number> = {};
lessons.forEach(l => {
  totalPrereqEdges += l.prerequisiteLessonIds.length;
  if (l.prerequisiteLessonIds.length === 0) {
    trueRoots++;
  } else if (l.prerequisiteLessonIds.length > 1) {
    branchingInNodes++;
  }
  l.prerequisiteLessonIds.forEach(pId => {
    outDegree[pId] = (outDegree[pId] || 0) + 1;
  });
});

Object.values(outDegree).forEach(deg => {
  if (deg > 1) branchingOutNodes++;
});

// Check how many are strictly [lessonIndex - 1]
lessons.forEach((l, idx) => {
  if (idx > 0 && l.prerequisiteLessonIds.length === 1 && l.prerequisiteLessonIds[0] === lessons[idx - 1].lessonId) {
    linearIndexMinus1Count++;
  }
});

console.log("\nPrerequisite DAG Analysis:");
console.log(`  - Total Directed Edges: ${totalPrereqEdges}`);
console.log(`  - True Curriculum Roots (In-Degree = 0): ${trueRoots}`);
console.log(`  - Convergent Branching Nodes (In-Degree > 1): ${branchingInNodes}`);
console.log(`  - Divergent Branching Nodes (Out-Degree > 1): ${branchingOutNodes}`);
console.log(`  - Sequential [i-1] Adjacency Retained: ${linearIndexMinus1Count} / ${lessons.length} (${((linearIndexMinus1Count / lessons.length) * 100).toFixed(1)}%)`);

// Check for cycles in DAG
function hasCycles(): boolean {
  const visited = new Set<string>();
  const recStack = new Set<string>();
  const idMap = new Map<string, LessonBlueprint>();
  lessons.forEach(l => idMap.set(l.lessonId, l));

  function isCyclic(id: string): boolean {
    if (!visited.has(id)) {
      visited.add(id);
      recStack.add(id);
      const l = idMap.get(id);
      if (l) {
        for (const p of l.prerequisiteLessonIds) {
          if (!visited.has(p) && isCyclic(p)) return true;
          else if (recStack.has(p)) return true;
        }
      }
    }
    recStack.delete(id);
    return false;
  }

  for (const l of lessons) {
    if (isCyclic(l.lessonId)) return true;
  }
  return false;
}
console.log(`  - DAG Cycle Check: ${hasCycles() ? "FAIL (Cycle detected)" : "PASS (Acyclic Graph)"}`);

// 4. Lexical Allocation & Zero-Vocab Lessons
let zeroVocabLessons = 0;
lessons.forEach(l => {
  if (l.newProductiveLemmaTarget === 0 && l.newReceptiveLemmaTarget === 0 &&
      l.newProductiveExpressionTarget === 0 && l.newReceptiveExpressionTarget === 0) {
    zeroVocabLessons++;
  }
});
console.log(`\nLexical Load Distribution:`);
console.log(`  - Lessons with 0 New Vocabulary (Pure Integration/Synthesis): ${zeroVocabLessons} / ${lessons.length} (${((zeroVocabLessons / lessons.length) * 100).toFixed(1)}%)`);

// 5. Macro-Skills Focus
let readingDominant = 0;
let listeningDominant = 0;
let writingDominant = 0;
let speakingDominant = 0;

lessons.forEach(l => {
  if (l.lessonType.includes("reading")) readingDominant++;
  if (l.lessonType.includes("listening")) listeningDominant++;
  if (l.lessonType.includes("writing")) writingDominant++;
  if (l.lessonType.includes("dialogue") || l.lessonType.includes("spoken")) speakingDominant++;
});

console.log(`\nMacro-Skill Distribution:`);
console.log(`  - Reading Focus Lessons: ${readingDominant}`);
console.log(`  - Listening Focus Lessons: ${listeningDominant}`);
console.log(`  - Writing Focus Lessons: ${writingDominant}`);
console.log(`  - Dialogue / Spoken Production Lessons: ${speakingDominant}`);

// 6. Longitudinal Phonology & Grammar Reinforcement Verification
const targets = [
  "phono_neutral_vowel_behavior",
  "phono_iotated_vowels_behavior",
  "phono_soft_and_hard_signs",
  "phono_non_initial_reduction",
  "gram_a1_nominal_negation_bish"
];

console.log("\nLongitudinal Review & Reinforcement Targets:");
targets.forEach(t => {
  let introduced = 0;
  let reviewed = 0;
  lessons.forEach(l => {
    if (l.phonologyIntroduced.includes(t) || l.grammarIntroduced.includes(t)) introduced++;
    if (l.phonologyReviewed.includes(t) || l.grammarReinforced.includes(t)) reviewed++;
  });
  console.log(`  - Target ${t.padEnd(32)}: Introduced in ${introduced} lessons, Reviewed/Reinforced in ${reviewed} lessons`);
});

// 7. Success Criteria Qualitative Audit
let tropeCount = 0;
lessons.forEach(l => {
  l.successCriteria.forEach(sc => {
    if (sc.includes("100%") || sc.includes("90%") || sc.includes("80%")) tropeCount++;
  });
});
console.log(`\nRemaining Arbitrary Percentage Tropes in Success Criteria: ${tropeCount}`);

