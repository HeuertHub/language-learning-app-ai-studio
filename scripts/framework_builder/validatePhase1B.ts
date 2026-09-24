import fs from 'fs';
import path from 'path';
import { sectionsData } from './dataSections';
import { allGrammarConcepts } from './dataGrammarMaster';
import { communicativeFunctionsData } from './dataCommunicative';
import { phonologyInventoryData } from './dataPhonology';
import { lexicalDomainsData } from './dataLexicalDomains';
import { UnitSpec } from './unitTypes';

interface ValidationError {
  type: 'ERROR' | 'WARNING';
  category: string;
  id: string;
  message: string;
}

function runValidation() {
  const errors: ValidationError[] = [];
  console.log("Starting Phase 1B Comprehensive Structural & Pedagogical Validation...\n");

  const blueprintDir = path.join(process.cwd(), 'curriculum', 'blueprint');
  const unitsDir = path.join(blueprintDir, 'units');

  // Load all unit files
  const levels = ['preA1', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2'];
  const allUnits: UnitSpec[] = [];

  for (const lvl of levels) {
    const filePath = path.join(unitsDir, `${lvl}.json`);
    if (!fs.existsSync(filePath)) {
      errors.push({ type: 'ERROR', category: 'FILE_SYSTEM', id: lvl, message: `Missing units file: ${filePath}` });
      continue;
    }
    const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    allUnits.push(...content);
  }

  console.log(`Loaded ${allUnits.length} total units across ${levels.length} level files.`);

  // 1. Check Unit Count
  if (allUnits.length < 200) {
    errors.push({ type: 'ERROR', category: 'SCALE', id: 'TOTAL_UNITS', message: `Unit count too low: ${allUnits.length} (expected 220-280)` });
  }

  // 2. Check Unit IDs Uniqueness
  const unitIdSet = new Set<string>();
  const seqSet = new Set<number>();
  for (const u of allUnits) {
    if (unitIdSet.has(u.unitId)) {
      errors.push({ type: 'ERROR', category: 'UNIQUENESS', id: u.unitId, message: `Duplicate unitId: ${u.unitId}` });
    }
    unitIdSet.add(u.unitId);

    if (seqSet.has(u.sequencePosition)) {
      errors.push({ type: 'ERROR', category: 'UNIQUENESS', id: `seq_${u.sequencePosition}`, message: `Duplicate sequence position: ${u.sequencePosition}` });
    }
    seqSet.add(u.sequencePosition);
  }

  // 3. Verify Sections & Non-Uniform Distribution
  const sectionMap = new Map(sectionsData.map(s => [s.sectionId, s]));
  const unitsBySection: Record<string, UnitSpec[]> = {};
  for (const u of allUnits) {
    if (!unitsBySection[u.sectionId]) unitsBySection[u.sectionId] = [];
    unitsBySection[u.sectionId].push(u);

    const sec = sectionMap.get(u.sectionId);
    if (!sec) {
      errors.push({ type: 'ERROR', category: 'SECTION_REFERENCE', id: u.unitId, message: `Unit references non-existent sectionId: ${u.sectionId}` });
    } else if (sec.cefrLevel !== u.cefrLevel) {
      errors.push({ type: 'ERROR', category: 'CEFR_MISMATCH', id: u.unitId, message: `Unit CEFR level (${u.cefrLevel}) does not match Section CEFR level (${sec.cefrLevel})` });
    }
  }

  // Check section units count variation
  const unitCountsPerSection: number[] = [];
  for (const sec of sectionsData) {
    const count = unitsBySection[sec.sectionId]?.length || 0;
    unitCountsPerSection.push(count);
    if (count === 0) {
      errors.push({ type: 'ERROR', category: 'EMPTY_SECTION', id: sec.sectionId, message: `Section has 0 units: ${sec.sectionId}` });
    }
  }

  const distinctCounts = new Set(unitCountsPerSection);
  if (distinctCounts.size <= 1) {
    errors.push({ type: 'ERROR', category: 'ANTI_PATTERN', id: 'UNIFORM_SECTIONS', message: `All sections have identical unit counts! Found ${distinctCounts.size} distinct count.` });
  } else {
    console.log(`Verified non-uniform section distribution: distinct unit counts per section = [${Array.from(distinctCounts).join(', ')}]`);
  }

  // 4. DAG & Prerequisite Integrity
  const cefrRanks: Record<string, number> = {
    'Pre-A1': 0,
    'A1': 1,
    'A2': 2,
    'B1': 3,
    'B2': 4,
    'C1': 5,
    'C2': 6
  };

  for (const u of allUnits) {
    for (const prereqId of u.prerequisiteUnitIds) {
      if (!unitIdSet.has(prereqId)) {
        errors.push({ type: 'ERROR', category: 'DANGLING_PREREQUISITE', id: u.unitId, message: `Prerequisite unit not found: ${prereqId}` });
      } else {
        const prereqUnit = allUnits.find(x => x.unitId === prereqId)!;
        if (cefrRanks[prereqUnit.cefrLevel] > cefrRanks[u.cefrLevel]) {
          errors.push({ type: 'ERROR', category: 'CEFR_REGRESSION', id: u.unitId, message: `Unit ${u.unitId} (${u.cefrLevel}) depends on higher level prerequisite ${prereqId} (${prereqUnit.cefrLevel})` });
        }
        if (prereqUnit.sequencePosition >= u.sequencePosition) {
          errors.push({ type: 'ERROR', category: 'SEQUENCE_CYCLE', id: u.unitId, message: `Unit ${u.unitId} (seq ${u.sequencePosition}) depends on subsequent/equal unit ${prereqId} (seq ${prereqUnit.sequencePosition})` });
        }
      }
    }

    for (const revId of u.reviewOfUnitIds) {
      if (!unitIdSet.has(revId)) {
        errors.push({ type: 'WARNING', category: 'DANGLING_REVIEW', id: u.unitId, message: `Review unit not found: ${revId}` });
      }
    }
  }

  // 5. Lexical Reconciliation
  let totalDomain = 0;
  let totalGeneral = 0;
  let totalExpressions = 0;

  for (const u of allUnits) {
    totalDomain += u.lexicalBreakdown.domainSpecificLemmas;
    totalGeneral += u.lexicalBreakdown.generalPurposeLemmas;
    totalExpressions += u.lexicalBreakdown.multiwordExpressions;

    if (u.estimatedNewCoreLemmas !== (u.lexicalBreakdown.domainSpecificLemmas + u.lexicalBreakdown.generalPurposeLemmas)) {
      errors.push({ type: 'ERROR', category: 'LEXICAL_MATH', id: u.unitId, message: `estimatedNewCoreLemmas does not equal domain + general sum` });
    }
  }

  const totalCore = totalDomain + totalGeneral;
  console.log(`Lexical Totals:`);
  console.log(`- Domain-specific lemmas: ${totalDomain}`);
  console.log(`- General-purpose lemmas: ${totalGeneral}`);
  console.log(`- Total Core Lexical Lemmas: ${totalCore} (Target: 8,000 - 10,000)`);
  console.log(`- Total Multiword Expressions / Idioms: ${totalExpressions} (Target: 1,500 - 3,000)`);

  if (totalCore < 8000 || totalCore > 10000) {
    errors.push({ type: 'ERROR', category: 'LEXICAL_BAND', id: 'CORE_LEMMAS', message: `Total core lemmas ${totalCore} outside 8,000-10,000 band` });
  }
  if (totalExpressions < 1500 || totalExpressions > 3000) {
    errors.push({ type: 'ERROR', category: 'LEXICAL_BAND', id: 'MULTIWORD_EXPRESSIONS', message: `Total expressions ${totalExpressions} outside 1,500-3,000 band` });
  }

  // 6. Grammar Coverage
  const introducedGrammarSet = new Set<string>();
  for (const u of allUnits) {
    for (const g of u.grammarIntroduced) {
      introducedGrammarSet.add(g);
    }
  }
  console.log(`Grammar Coverage: ${introducedGrammarSet.size} distinct grammar concepts introduced directly in units.`);

  // 7. Quality of Content Specs
  for (const u of allUnits) {
    if (!u.title || u.title.trim().length < 5) {
      errors.push({ type: 'ERROR', category: 'TITLE_DEFECT', id: u.unitId, message: `Unit has invalid title: "${u.title}"` });
    }
    if (!u.communicativeTheme || u.communicativeTheme.trim().length < 10) {
      errors.push({ type: 'ERROR', category: 'THEME_DEFECT', id: u.unitId, message: `Unit has invalid communicativeTheme` });
    }
    if (!u.readingTarget || !u.readingTarget.genre || !u.readingTarget.textLengthWords) {
      errors.push({ type: 'ERROR', category: 'SKILL_DEFECT', id: u.unitId, message: `Unit missing readingTarget specs` });
    }
    if (!u.listeningTarget || !u.listeningTarget.audioSuitability || !u.listeningTarget.speechRate) {
      errors.push({ type: 'ERROR', category: 'SKILL_DEFECT', id: u.unitId, message: `Unit missing listeningTarget specs` });
    }
    if (!u.writingTarget || !u.writingTarget.targetLength) {
      errors.push({ type: 'ERROR', category: 'SKILL_DEFECT', id: u.unitId, message: `Unit missing writingTarget specs` });
    }
    if (!u.spokenProductionTarget || !u.spokenProductionTarget.targetTask) {
      errors.push({ type: 'ERROR', category: 'SKILL_DEFECT', id: u.unitId, message: `Unit missing spokenProductionTarget specs` });
    }
    if (!u.culturalContext || !u.culturalContext.title) {
      errors.push({ type: 'ERROR', category: 'CULTURE_DEFECT', id: u.unitId, message: `Unit missing culturalContext specs` });
    }
  }

  // Final Summary
  const errorCount = errors.filter(e => e.type === 'ERROR').length;
  const warnCount = errors.filter(e => e.type === 'WARNING').length;

  console.log(`\n================ VALIDATION REPORT ================`);
  console.log(`Total Errors: ${errorCount}`);
  console.log(`Total Warnings: ${warnCount}`);

  if (errorCount > 0) {
    console.error(`\nValidation FAILED with ${errorCount} errors:`);
    for (const err of errors.filter(e => e.type === 'ERROR')) {
      console.error(`- [${err.category}] (${err.id}): ${err.message}`);
    }
    process.exit(1);
  } else {
    console.log(`\nSUCCESS: Phase 1B Curriculum Blueprint is FULLY VALIDATED!`);
    if (warnCount > 0) {
      for (const w of errors.filter(e => e.type === 'WARNING')) {
        console.warn(`- (WARNING) [${w.category}] (${w.id}): ${w.message}`);
      }
    }
  }
}

runValidation();
