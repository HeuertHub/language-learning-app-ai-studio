import * as fs from 'fs';
import * as path from 'path';

export function runCurriculumAudit() {
  const publicDataDir = path.join(process.cwd(), 'public', 'data');
  const manifestPath = path.join(publicDataDir, 'curriculum_manifest.json');
  const vocabPath = path.join(publicDataDir, 'vocabulary_lexicon.json');
  const sectionsDir = path.join(publicDataDir, 'sections');

  if (!fs.existsSync(manifestPath)) {
    throw new Error(`Manifest not found at ${manifestPath}. Run generateCurriculumMaster first.`);
  }

  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  const vocab = JSON.parse(fs.readFileSync(vocabPath, 'utf-8'));

  const sectionFiles = fs.readdirSync(sectionsDir).filter(f => f.endsWith('.json'));

  let verifiedTotalUnits = 0;
  let verifiedTotalLessons = 0;
  let verifiedTotalExercises = 0;
  const verifiedExercisesByType: Record<string, number> = {};
  const verifiedExercisesByCefr: Record<string, number> = {};

  for (const file of sectionFiles) {
    const secData = JSON.parse(fs.readFileSync(path.join(sectionsDir, file), 'utf-8'));
    verifiedTotalUnits += secData.units.length;

    for (const u of secData.units) {
      verifiedTotalLessons += u.lessons.length;
      for (const l of u.lessons) {
        verifiedTotalExercises += l.exercises.length;
        verifiedExercisesByCefr[secData.cefr] = (verifiedExercisesByCefr[secData.cefr] || 0) + l.exercises.length;
        for (const ex of l.exercises) {
          verifiedExercisesByType[ex.type] = (verifiedExercisesByType[ex.type] || 0) + 1;
        }
      }
    }
  }

  const results = {
    courseName: manifest.name,
    cefrStages: manifest.cefrLevels,
    cefrCount: manifest.cefrLevels.length,
    totalSections: sectionFiles.length,
    totalUnits: verifiedTotalUnits,
    totalLessons: verifiedTotalLessons,
    totalExercises: verifiedTotalExercises,
    totalVocabularyItems: vocab.length,
    exerciseDistributionByType: verifiedExercisesByType,
    exerciseDistributionByCEFR: verifiedExercisesByCefr,
    acceptanceCriteria: {
      '6 CEFR Stages (A1-C2)': manifest.cefrLevels.length === 6,
      '12-20 Major Sections': sectionFiles.length >= 12 && sectionFiles.length <= 20,
      '100-160 Units': verifiedTotalUnits >= 100 && verifiedTotalUnits <= 160,
      '600-1,000 Lessons': verifiedTotalLessons >= 600 && verifiedTotalLessons <= 1000,
      'At least 7,000 Exercises': verifiedTotalExercises >= 7000,
      'At least 3,000 Vocabulary Items': vocab.length >= 3000
    }
  };

  return results;
}

const audit = runCurriculumAudit();
console.log('=== MONGOLIAN CURRICULUM AUDIT REPORT ===');
console.log(JSON.stringify(audit, null, 2));

