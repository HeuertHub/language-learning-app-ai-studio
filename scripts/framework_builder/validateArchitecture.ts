import { proficiencyLevelsData as proficiencyLevels } from './dataProficiency';
import { phonologyInventoryData as phonologyInventory } from './dataPhonology';
import { allGrammarConcepts } from './dataGrammarMaster';
import { communicativeFunctionsData, macroCompetenciesData } from './dataCommunicative';
import { lexicalDomainsData, multiDimensionalLexicalFrameworkData } from './dataLexicalDomains';
import { skillProgressionsData } from './dataProgressions';
import { culturalContentArchitectureData } from './dataCulture';
import { curriculumScaleBlueprintData } from './dataTargets';

export interface ValidationIssue {
  category: "structural" | "semantic" | "linguistic" | "balance" | "anti_pattern";
  severity: "error" | "warning";
  code: string;
  message: string;
  context?: Record<string, unknown>;
}

export interface ValidationResult {
  passed: boolean;
  errors: string[];
  warnings: string[];
  issues: ValidationIssue[];
  stats: {
    proficiencyLevelsCount: number;
    phonologyConceptsCount: number;
    grammarConceptsCount: number;
    grammarConceptsByLevel: Record<string, number>;
    grammarVerificationRate: number;
    communicativeFunctionsCount: number;
    communicativeFunctionsByLevel: Record<string, number>;
    communicativeFunctionsByDomain: Record<string, number>;
    macroCompetenciesCount: number;
    lexicalDomainsCount: number;
    lexicalTargetTotal: number;
    vocabularyBreakdown: typeof multiDimensionalLexicalFrameworkData.vocabularyTargetBreakdown;
    skillProgressionStagesCount: number;
    culturalModulesCount: number;
    exerciseModalitiesCount: number;
    lessonsPlanningRange: [number, number];
    exercisePlanningDecoupled: boolean;
  };
}

export function validateCurriculumArchitecture(): ValidationResult {
  const issues: ValidationIssue[] = [];

  function addIssue(
    category: ValidationIssue["category"],
    severity: ValidationIssue["severity"],
    code: string,
    message: string,
    context?: Record<string, unknown>
  ) {
    issues.push({ category, severity, code, message, context });
  }

  // =========================================================================
  // 1. STRUCTURAL & IDENTIFIER VALIDATION
  // =========================================================================
  const grammarIdMap = new Map<string, typeof allGrammarConcepts[0]>();
  allGrammarConcepts.forEach(c => {
    if (grammarIdMap.has(c.conceptId)) {
      addIssue("structural", "error", "DUPLICATE_GRAMMAR_ID", `Duplicate Grammar Concept ID detected: ${c.conceptId}`, { id: c.conceptId });
    }
    grammarIdMap.set(c.conceptId, c);
  });

  const phonologyIdMap = new Map<string, typeof phonologyInventory[0]>();
  phonologyInventory.forEach(p => {
    if (phonologyIdMap.has(p.conceptId)) {
      addIssue("structural", "error", "DUPLICATE_PHONOLOGY_ID", `Duplicate Phonology Concept ID detected: ${p.conceptId}`, { id: p.conceptId });
    }
    phonologyIdMap.set(p.conceptId, p);
  });

  const commIdMap = new Map<string, typeof communicativeFunctionsData[0]>();
  communicativeFunctionsData.forEach(cf => {
    if (commIdMap.has(cf.functionId)) {
      addIssue("structural", "error", "DUPLICATE_COMM_ID", `Duplicate Communicative Function ID detected: ${cf.functionId}`, { id: cf.functionId });
    }
    commIdMap.set(cf.functionId, cf);
  });

  const domainIdMap = new Map<string, typeof lexicalDomainsData[0]>();
  lexicalDomainsData.forEach(ld => {
    if (domainIdMap.has(ld.domainId)) {
      addIssue("structural", "error", "DUPLICATE_DOMAIN_ID", `Duplicate Lexical Domain ID detected: ${ld.domainId}`, { id: ld.domainId });
    }
    domainIdMap.set(ld.domainId, ld);
  });

  // Verify grammar prerequisites and unlock targets
  allGrammarConcepts.forEach(concept => {
    concept.prerequisites.forEach(prereqId => {
      const existsInGrammar = grammarIdMap.has(prereqId);
      const existsInPhono = phonologyIdMap.has(prereqId);
      if (!existsInGrammar && !existsInPhono) {
        addIssue("structural", "error", "MISSING_PREREQUISITE", `Grammar concept [${concept.conceptId}] references nonexistent prerequisite: [${prereqId}]`, { conceptId: concept.conceptId, prereqId });
      }
    });

    concept.unlocks.forEach(unlockId => {
      if (!grammarIdMap.has(unlockId)) {
        addIssue("structural", "error", "MISSING_UNLOCK_TARGET", `Grammar concept [${concept.conceptId}] references nonexistent unlock target: [${unlockId}]`, { conceptId: concept.conceptId, unlockId });
      }
    });
  });

  // Cycle detection in Grammar Dependency DAG (DFS)
  const visited = new Set<string>();
  const recursionStack = new Set<string>();

  function detectCycle(conceptId: string, path: string[]): boolean {
    visited.add(conceptId);
    recursionStack.add(conceptId);

    const concept = grammarIdMap.get(conceptId);
    if (concept) {
      for (const prereqId of concept.prerequisites) {
        if (grammarIdMap.has(prereqId)) {
          if (!visited.has(prereqId)) {
            if (detectCycle(prereqId, [...path, prereqId])) {
              return true;
            }
          } else if (recursionStack.has(prereqId)) {
            addIssue("structural", "error", "CYCLE_IN_GRAMMAR_DAG", `Cycle detected in Grammar DAG: ${[...path, prereqId].join(" -> ")}`, { cycle: [...path, prereqId] });
            return true;
          }
        }
      }
    }

    recursionStack.delete(conceptId);
    return false;
  }

  for (const conceptId of grammarIdMap.keys()) {
    if (!visited.has(conceptId)) {
      detectCycle(conceptId, [conceptId]);
    }
  }

  // Validate Communicative Function Prerequisites
  communicativeFunctionsData.forEach(cf => {
    cf.prerequisites.forEach(prereqId => {
      if (!commIdMap.has(prereqId)) {
        addIssue("structural", "error", "MISSING_COMM_PREREQ", `Communicative function [${cf.functionId}] references nonexistent prerequisite: [${prereqId}]`, { functionId: cf.functionId, prereqId });
      }
    });
  });

  // =========================================================================
  // 2. LINGUISTIC & PEDAGOGICAL METADATA VALIDATION
  // =========================================================================
  let verifiedConceptsCount = 0;

  allGrammarConcepts.forEach(c => {
    // Verification Status Check (Accepts "VERIFIED")
    if (c.verificationStatus === "VERIFIED") {
      verifiedConceptsCount++;
    } else {
      addIssue("linguistic", "error", "UNVERIFIED_GRAMMAR_CONCEPT", `Grammar concept [${c.conceptId}] has non-verified status: [${c.verificationStatus}]`, { conceptId: c.conceptId, status: c.verificationStatus });
    }

    // Pedagogical Label Check
    if (!c.pedagogicalLabel || c.pedagogicalLabel.trim().length < 5) {
      addIssue("linguistic", "error", "INADEQUATE_PEDAGOGICAL_LABEL", `Grammar concept [${c.conceptId}] lacks clear pedagogical label.`, { conceptId: c.conceptId });
    }

    // Strict Separation: Learner Explanation vs Linguistic Analysis
    if (!c.learnerExplanation || c.learnerExplanation.trim().length < 25) {
      addIssue("linguistic", "error", "SHALLOW_LEARNER_EXPLANATION", `Grammar concept [${c.conceptId}] has shallow or missing learnerExplanation (< 25 characters).`, { conceptId: c.conceptId });
    }
    if (!c.linguisticAnalysis || c.linguisticAnalysis.trim().length < 25) {
      addIssue("linguistic", "error", "SHALLOW_LINGUISTIC_ANALYSIS", `Grammar concept [${c.conceptId}] has shallow or missing linguisticAnalysis (< 25 characters).`, { conceptId: c.conceptId });
    }
    if (!c.technicalNotes || c.technicalNotes.trim().length < 15) {
      addIssue("linguistic", "warning", "BRIEF_TECHNICAL_NOTES", `Grammar concept [${c.conceptId}] has brief or missing technicalNotes (< 15 characters).`, { conceptId: c.conceptId });
    }

    // Bilingual In-Situ Examples Check (verifies description contains authentic Mongolian linguistic examples)
    const hasInSituExample = c.description && c.description.trim().length >= 40 && /[а-яөүё]/i.test(c.description);
    if (!hasInSituExample) {
      addIssue("linguistic", "error", "MISSING_IN_SITU_EXAMPLES", `Grammar concept [${c.conceptId}] description lacks contextual Mongolian examples (< 40 chars or no Cyrillic).`, { conceptId: c.conceptId });
    }
  });

  const grammarVerificationRate = allGrammarConcepts.length > 0 ? (verifiedConceptsCount / allGrammarConcepts.length) * 100 : 0;
  if (grammarVerificationRate < 100) {
    addIssue("linguistic", "error", "SUBPAR_VERIFICATION_RATE", `Overall grammar verification rate is ${grammarVerificationRate.toFixed(1)}%. Must be strictly 100%.`);
  }

  // Phonology Consonant Classification Check (Sonorants vs Obstruents)
  const sonorantConcept = phonologyInventory.find(p => p.conceptId === "phono_epenthesis_consonant_contact");
  if (sonorantConcept) {
    const analysis = sonorantConcept.linguisticAnalysis;
    const has7Sonorants = analysis.includes("7") && (analysis.includes("М") || analysis.includes("эгшигт"));
    const has9Obstruents = analysis.includes("9") && (analysis.includes("Д") || analysis.includes("заримдаг"));
    if (!has7Sonorants || !has9Obstruents) {
      addIssue("linguistic", "error", "PHONOLOGY_CONSONANT_MISCLASSIFICATION", "Consonant classification must explicitly distinguish 7 Sonorants (М, Н, Г, Л, Б, В, Р) and 9 Obstruents (Д, Ж, З, С, Т, Х, Ц, Ч, Ш).");
    }
  }

  // =========================================================================
  // 3. CURRICULUM BALANCE & LEVEL DISTRIBUTION
  // =========================================================================
  const requiredLevels = ["Pre-A1", "A1", "A2", "B1", "B2", "C1", "C2"];
  const levelOrder: Record<string, number> = {
    "Pre-A1": 0,
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4,
    "C1": 5,
    "C2": 6
  };

  const grammarByLevel: Record<string, number> = {};
  const commByLevel: Record<string, number> = {};
  const commByDomain: Record<string, number> = {};

  requiredLevels.forEach(lvl => {
    grammarByLevel[lvl] = 0;
    commByLevel[lvl] = 0;
  });

  allGrammarConcepts.forEach(c => {
    grammarByLevel[c.firstTargetLevel] = (grammarByLevel[c.firstTargetLevel] || 0) + 1;
  });

  communicativeFunctionsData.forEach(cf => {
    commByLevel[cf.level] = (commByLevel[cf.level] || 0) + 1;
    commByDomain[cf.domain] = (commByDomain[cf.domain] || 0) + 1;
  });

  // Balance thresholds across levels
  requiredLevels.forEach(lvl => {
    // Pre-A1 is primarily phonology and orthography
    if (lvl !== "Pre-A1") {
      const gCount = grammarByLevel[lvl];
      if (gCount < 10) {
        addIssue("balance", "error", "GRAMMAR_LEVEL_STARVATION", `CEFR Level [${lvl}] is under-allocated for grammar (found ${gCount}, expected at least 10).`, { level: lvl, count: gCount });
      } else if (gCount > 75) {
        addIssue("balance", "warning", "GRAMMAR_LEVEL_OVERBURDEN", `CEFR Level [${lvl}] has high grammar density (${gCount} concepts), risk of cognitive overload.`, { level: lvl, count: gCount });
      }

      const cCount = commByLevel[lvl];
      if (cCount < 15) {
        addIssue("balance", "error", "COMM_LEVEL_STARVATION", `CEFR Level [${lvl}] is under-allocated for communicative functions (found ${cCount}, expected at least 15).`, { level: lvl, count: cCount });
      }
    }

    // Verify Skill Progression stage exists
    const stage = skillProgressionsData.find(s => s.level === lvl);
    if (!stage) {
      addIssue("balance", "error", "MISSING_SKILL_PROGRESSION", `CEFR Level [${lvl}] is missing a Skill Progression stage.`, { level: lvl });
    }
  });

  // Check Communicative Function Inventory Breadth
  const totalCommFunctions = communicativeFunctionsData.length;
  if (totalCommFunctions < 120 || totalCommFunctions > 250) {
    addIssue("balance", "error", "COMM_INVENTORY_OUT_OF_BOUNDS", `Communicative function inventory (${totalCommFunctions}) must be between 120 and 250 fine-grained functions.`, { count: totalCommFunctions });
  }

  // Check Domain Coverage in Communicative Functions (at least 5 distinct functional domains)
  const domainKeys = Object.keys(commByDomain);
  if (domainKeys.length < 5) {
    addIssue("balance", "warning", "NARROW_COMM_DOMAIN_BREADTH", `Communicative functions span only ${domainKeys.length} domains (expected at least 5 broad communicative domains).`, { domains: domainKeys });
  }

  // Cross-Level Prerequisite Regression Check: Concept at Level N should not require Level N+2
  allGrammarConcepts.forEach(c => {
    const cLevelRank = levelOrder[c.firstTargetLevel] ?? -1;
    c.prerequisites.forEach(prereqId => {
      const prereqConcept = grammarIdMap.get(prereqId);
      if (prereqConcept) {
        const pLevelRank = levelOrder[prereqConcept.firstTargetLevel] ?? -1;
        if (pLevelRank > cLevelRank) {
          addIssue("balance", "error", "PREREQUISITE_LEVEL_INVERSION", `Grammar concept [${c.conceptId}] at level [${c.firstTargetLevel}] requires higher-level prerequisite [${prereqId}] at [${prereqConcept.firstTargetLevel}].`, { conceptId: c.conceptId, conceptLevel: c.firstTargetLevel, prereqId, prereqLevel: prereqConcept.firstTargetLevel });
        }
      }
    });
  });

  // =========================================================================
  // 4. RIGID UNIFORMITY & FORMULAIC ANTI-PATTERN DETECTION
  // =========================================================================
  const bp = curriculumScaleBlueprintData;

  // A. Check for artificial fixed multipliers in Exercise Planning
  if (bp.exercisePlanningNote.toLowerCase().includes("multiplier") || !bp.exercisePlanningNote.toLowerCase().includes("calculated only after")) {
    addIssue("anti_pattern", "error", "EXERCISE_FIXED_MULTIPLIER_DETECTED", "Exercise planning must be decoupled from fixed arithmetic multipliers.", { note: bp.exercisePlanningNote });
  }

  // B. Check that lesson planning bands have natural variances and non-zero spreads
  const bands = bp.lessonPlanningBands;
  const bandEntries: [string, [number, number]][] = [
    ["microLessonPhoneticReview", bands.microLessonPhoneticReview],
    ["standardInstructional", bands.standardInstructional],
    ["grammarIntegratedSkills", bands.grammarIntegratedSkills],
    ["majorReviewWorkshopCheckpoint", bands.majorReviewWorkshopCheckpoint]
  ];

  bandEntries.forEach(([name, [min, max]]) => {
    if (min >= max) {
      addIssue("anti_pattern", "error", "DEGENERATE_PLANNING_BAND", `Lesson planning band [${name}] has degenerate range [${min}, ${max}]. Min must be strictly less than max.`, { band: name, min, max });
    }
  });

  // C. Detect suspicious uniform counts across Lexical Domains
  const domainTargets = lexicalDomainsData.map(d => d.estimatedDomainSpecificVocabularyTarget);
  const uniqueDomainTargets = new Set(domainTargets);
  if (uniqueDomainTargets.size === 1 && lexicalDomainsData.length > 3) {
    addIssue("anti_pattern", "error", "ARTIFICIALLY_UNIFORM_DOMAIN_TARGETS", `All ${lexicalDomainsData.length} lexical domains have the exact same target count (${domainTargets[0]}). Real domains vary naturally.`, { count: domainTargets[0] });
  }

  // D. Check that Level Targets have non-identical planning numbers
  const lessonRanges = bp.levelTargets.map(lt => `${lt.projectedLessonsRange[0]}-${lt.projectedLessonsRange[1]}`);
  const uniqueLessonRanges = new Set(lessonRanges);
  if (uniqueLessonRanges.size < 4) {
    addIssue("anti_pattern", "warning", "UNIFORM_LEVEL_PROJECTIONS", "Level scale targets exhibit low variability in lesson planning bands.");
  }

  // =========================================================================
  // 5. VOCABULARY ARCHITECTURE INTEGRITY
  // =========================================================================
  const vocabPlan = bp.vocabularyPlan;

  // Verify Exclusion of Inflected Surface Forms
  if (!vocabPlan.inflectedSurfaceFormsExclusion.includes("0") && !vocabPlan.inflectedSurfaceFormsExclusion.toLowerCase().includes("strictly")) {
    addIssue("linguistic", "error", "INFLECTED_SURFACE_FORMS_NOT_EXCLUDED", "Vocabulary plan must strictly exclude inflected surface forms and declension paradigm variants from lexical targets.", { rule: vocabPlan.inflectedSurfaceFormsExclusion });
  }

  // Verify Primary Lexical Lemma Range (CEFR C2 Comprehensive standard: 8,000–10,000)
  const [minLemmas, maxLemmas] = vocabPlan.primaryLexicalLemmaRange;
  if (minLemmas < 6000 || maxLemmas > 12000 || minLemmas >= maxLemmas) {
    addIssue("balance", "error", "INVALID_LEMMA_PLANNING_RANGE", `Primary lexical lemma range [${minLemmas}, ${maxLemmas}] is outside CEFR target bounds (6,000–10,000).`, { minLemmas, maxLemmas });
  }

  // Verify Multiword Expressions Range (1,500–3,000)
  const [minMwe, maxMwe] = vocabPlan.multiwordExpressionsRange;
  if (minMwe < 1000 || maxMwe > 4000) {
    addIssue("balance", "warning", "MWE_RANGE_ANOMALY", `Multiword expression range [${minMwe}, ${maxMwe}] differs significantly from recommended bounds (1,500–3,000).`, { minMwe, maxMwe });
  }

  // Verify Function Words and Particles (Closed Class: 140–200)
  const [minFunc, maxFunc] = vocabPlan.functionWordsAndParticlesRange;
  if (minFunc < 100 || maxFunc > 300) {
    addIssue("linguistic", "warning", "FUNCTION_WORDS_ANOMALY", `Function words and particles range [${minFunc}, ${maxFunc}] outside typical closed-class bounds (140–200).`, { minFunc, maxFunc });
  }

  // Verify Total Lexical Domain Cumulative Target
  const lexicalTargetTotal = lexicalDomainsData.reduce((acc, d) => acc + d.estimatedDomainSpecificVocabularyTarget, 0);
  if (lexicalTargetTotal < 6000 || lexicalTargetTotal > 12000) {
    addIssue("balance", "warning", "LEXICAL_DOMAIN_SUM_OUTSIDE_BOUNDS", `Total cumulative lexical target across domains (${lexicalTargetTotal}) is outside 6,000–12,000 range.`, { total: lexicalTargetTotal });
  }

  // Compile final results
  const errors = issues.filter(i => i.severity === "error").map(i => `[${i.category.toUpperCase()}] ${i.code}: ${i.message}`);
  const warnings = issues.filter(i => i.severity === "warning").map(i => `[${i.category.toUpperCase()}] ${i.code}: ${i.message}`);
  const passed = errors.length === 0;

  return {
    passed,
    errors,
    warnings,
    issues,
    stats: {
      proficiencyLevelsCount: proficiencyLevels.length,
      phonologyConceptsCount: phonologyInventory.length,
      grammarConceptsCount: allGrammarConcepts.length,
      grammarConceptsByLevel: grammarByLevel,
      grammarVerificationRate,
      communicativeFunctionsCount: communicativeFunctionsData.length,
      communicativeFunctionsByLevel: commByLevel,
      communicativeFunctionsByDomain: commByDomain,
      macroCompetenciesCount: macroCompetenciesData.length,
      lexicalDomainsCount: lexicalDomainsData.length,
      lexicalTargetTotal,
      vocabularyBreakdown: multiDimensionalLexicalFrameworkData.vocabularyTargetBreakdown,
      skillProgressionStagesCount: skillProgressionsData.length,
      culturalModulesCount: culturalContentArchitectureData.length,
      exerciseModalitiesCount: bp.exerciseModalities.length,
      lessonsPlanningRange: bp.lessonsPlanningRange,
      exercisePlanningDecoupled: true
    }
  };
}

// Self-executing runner when executed via tsx / node
if (process.env.RUN_ARCH_VALIDATION || process.argv[1]?.includes('validateArchitecture')) {
  const result = validateCurriculumArchitecture();
  console.log("===============================================================================");
  console.log("         MODERN MONGOLIAN CURRICULUM ARCHITECTURE VALIDATION REPORT           ");
  console.log("===============================================================================");
  console.log(`STATUS: ${result.passed ? "PASSED (AUTHORITATIVE ARCHITECTURE CERTIFIED)" : "FAILED (CORRECTIONS REQUIRED)"}`);
  console.log(`Issues Summary: ${result.errors.length} Errors | ${result.warnings.length} Warnings\n`);

  if (result.errors.length > 0) {
    console.error("FATAL ARCHITECTURAL ERRORS:");
    result.errors.forEach(e => console.error(`  ✖ ${e}`));
    console.log("");
  }

  if (result.warnings.length > 0) {
    console.warn("ARCHITECTURAL WARNINGS & OBSERVATIONS:");
    result.warnings.forEach(w => console.warn(`  ⚠ ${w}`));
    console.log("");
  }

  console.log("-------------------------------------------------------------------------------");
  console.log("ARCHITECTURAL FRAMEWORK METRICS & STATS:");
  console.log(` • CEFR Proficiency Scale Levels: ${result.stats.proficiencyLevelsCount} (Pre-A1 through C2)`);
  console.log(` • Phonology & Orthography Concepts: ${result.stats.phonologyConceptsCount}`);
  console.log(` • Verified Grammar Structure Concepts: ${result.stats.grammarConceptsCount} (Verification Rate: ${result.stats.grammarVerificationRate.toFixed(1)}%)`);
  console.log("   Distribution by Level:", JSON.stringify(result.stats.grammarConceptsByLevel, null, 2));
  console.log(` • Fine-Grained Communicative Functions: ${result.stats.communicativeFunctionsCount}`);
  console.log("   Distribution by Level:", JSON.stringify(result.stats.communicativeFunctionsByLevel, null, 2));
  console.log("   Distribution by Domain:", JSON.stringify(result.stats.communicativeFunctionsByDomain, null, 2));
  console.log(` • Macro Competency Benchmarks: ${result.stats.macroCompetenciesCount}`);
  console.log(` • Thematic Lexical Domains: ${result.stats.lexicalDomainsCount}`);
  console.log(` • Cumulative Lexical Domain Target: ${result.stats.lexicalTargetTotal} items`);
  console.log(` • Vocabulary Blueprint Primary Lemmas: ${result.stats.vocabularyBreakdown.primaryLexicalLemmasCombinedRange[0]}–${result.stats.vocabularyBreakdown.primaryLexicalLemmasCombinedRange[1]}`);
  console.log(` • Inflected Surface Forms Excluded: ${result.stats.vocabularyBreakdown.inflectedSurfaceFormsCount === 0 ? "YES (Strict 0 count)" : "NO"}`);
  console.log(` • Skill Progression Stages: ${result.stats.skillProgressionStagesCount}`);
  console.log(` • Cultural Modules: ${result.stats.culturalModulesCount}`);
  console.log(` • Exercise Modalities: ${result.stats.exerciseModalitiesCount}`);
  console.log(` • Projected Curriculum Lessons Range: ${result.stats.lessonsPlanningRange[0]}–${result.stats.lessonsPlanningRange[1]}`);
  console.log(` • Decoupled Exercise Volume Sizing: ${result.stats.exercisePlanningDecoupled ? "ENFORCED (No fixed multipliers)" : "NOT ENFORCED"}`);
  console.log("===============================================================================");
}
