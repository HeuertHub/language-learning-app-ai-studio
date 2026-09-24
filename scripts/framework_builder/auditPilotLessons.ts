import { allPilotLessons } from "./compilePilot";
import { LessonBlueprint } from "./lessonBlueprintTypes";
import * as fs from "fs";

interface AuditIssue {
  type: string;
  lessonId: string;
  message: string;
}

const issues: AuditIssue[] = [];

// 1. Total lessons
console.log(`Auditing ${allPilotLessons.length} lesson blueprints across Pre-A1 (Units 1-15) and A1 Section 1 (Units 16-23)...`);

// 2. Uniqueness of Lesson IDs
const lessonIdSet = new Set<string>();
allPilotLessons.forEach(l => {
  if (lessonIdSet.has(l.lessonId)) {
    issues.push({ type: "DUPLICATE_LESSON_ID", lessonId: l.lessonId, message: "Duplicate lesson ID found." });
  }
  lessonIdSet.add(l.lessonId);
});

// 3. Uniqueness of Lesson Titles
const titleMap = new Map<string, string>();
allPilotLessons.forEach(l => {
  const normTitle = l.title.trim().toLowerCase();
  if (titleMap.has(normTitle)) {
    issues.push({ type: "DUPLICATE_TITLE", lessonId: l.lessonId, message: `Duplicate title with ${titleMap.get(normTitle)}: "${l.title}"` });
  } else {
    titleMap.set(normTitle, l.lessonId);
  }
});

// 4. Sequence within unit strictly 1..N
const unitLessonsMap = new Map<string, LessonBlueprint[]>();
allPilotLessons.forEach(l => {
  if (!unitLessonsMap.has(l.unitId)) unitLessonsMap.set(l.unitId, []);
  unitLessonsMap.get(l.unitId)!.push(l);
});

unitLessonsMap.forEach((lessons, uId) => {
  lessons.sort((a, b) => a.sequenceWithinUnit - b.sequenceWithinUnit);
  lessons.forEach((l, idx) => {
    if (l.sequenceWithinUnit !== idx + 1) {
      issues.push({
        type: "INVALID_SEQUENCE",
        lessonId: l.lessonId,
        message: `Unit ${uId} has invalid sequence: expected ${idx + 1}, got ${l.sequenceWithinUnit}`
      });
    }
  });
});

// 5. Check Prerequisite DAG validity
const allLessonIds = new Set(allPilotLessons.map(l => l.lessonId));
allPilotLessons.forEach(l => {
  l.prerequisiteLessonIds.forEach(pId => {
    if (!allLessonIds.has(pId)) {
      // Check if it is an external lesson outside pilot
      issues.push({
        type: "BROKEN_PREREQUISITE_EDGE",
        lessonId: l.lessonId,
        message: `Prerequisite ${pId} does not exist in pilot lesson pool.`
      });
    }
  });
});

// 6. Check Lesson Types distribution
const lessonTypeCounts: Record<string, number> = {};
allPilotLessons.forEach(l => {
  lessonTypeCounts[l.lessonType] = (lessonTypeCounts[l.lessonType] || 0) + 1;
});

// 7. Check Objective, Grammar, Phono, CommFunc distribution
let totalObjectivesIntro = 0;
let totalGrammarIntro = 0;
let totalPhonoIntro = 0;
let totalCommFuncIntro = 0;
let totalProdLemmas = 0;
let totalRecLemmas = 0;
let totalProdExp = 0;
let totalRecExp = 0;

allPilotLessons.forEach(l => {
  totalObjectivesIntro += l.objectivesIntroduced.length;
  totalGrammarIntro += l.grammarIntroduced.length;
  totalPhonoIntro += l.phonologyIntroduced.length;
  totalCommFuncIntro += l.communicativeFunctionsIntroduced.length;
  totalProdLemmas += l.newProductiveLemmaTarget;
  totalRecLemmas += l.newReceptiveLemmaTarget;
  totalProdExp += l.newProductiveExpressionTarget;
  totalRecExp += l.newReceptiveExpressionTarget;
});

// 8. Mechanical Templating Checks (identical purpose / communicativeOutcome strings)
const purposeMap = new Map<string, string>();
allPilotLessons.forEach(l => {
  const norm = l.primaryPurpose.trim().toLowerCase();
  if (purposeMap.has(norm)) {
    issues.push({
      type: "DUPLICATE_PURPOSE",
      lessonId: l.lessonId,
      message: `Duplicate purpose with ${purposeMap.get(norm)}`
    });
  } else {
    purposeMap.set(norm, l.lessonId);
  }
});

const outcomeMap = new Map<string, string>();
allPilotLessons.forEach(l => {
  const norm = l.communicativeOutcome.trim().toLowerCase();
  if (outcomeMap.has(norm)) {
    issues.push({
      type: "DUPLICATE_OUTCOME",
      lessonId: l.lessonId,
      message: `Duplicate outcome with ${outcomeMap.get(norm)}`
    });
  } else {
    outcomeMap.set(norm, l.lessonId);
  }
});

console.log("AUDIT RESULTS:");
console.log("- Total lessons:", allPilotLessons.length);
console.log("- Total units covered:", unitLessonsMap.size);
console.log("- Lesson types breakdown:", lessonTypeCounts);
console.log("- Total Objectives introduced:", totalObjectivesIntro);
console.log("- Total Grammar concepts introduced:", totalGrammarIntro);
console.log("- Total Phonology targets introduced:", totalPhonoIntro);
console.log("- Total Comm Functions introduced:", totalCommFuncIntro);
console.log("- Lexical targets sum across pilot:", {
  productiveLemmas: totalProdLemmas,
  receptiveLemmas: totalRecLemmas,
  productiveExpressions: totalProdExp,
  receptiveExpressions: totalRecExp
});

console.log("- Issues found:", issues.length);
if (issues.length > 0) {
  console.log(JSON.stringify(issues.slice(0, 10), null, 2));
} else {
  console.log("ZERO AUDIT DEFECTS: All IDs unique, all sequences valid, all prerequisites resolvable, zero template duplicates!");
}

// Unit by unit summary table
console.log("\nUNIT BY UNIT BREAKDOWN:");
unitLessonsMap.forEach((lessons, uId) => {
  const types = lessons.map(l => l.lessonType).join(", ");
  const prodLem = lessons.reduce((sum, l) => sum + l.newProductiveLemmaTarget, 0);
  const recLem = lessons.reduce((sum, l) => sum + l.newReceptiveLemmaTarget, 0);
  console.log(`- ${uId}: ${lessons.length} lessons | ProdLem=${prodLem}, RecLem=${recLem} | [${types}]`);
});
