import * as fs from 'fs';
import * as path from 'path';
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, getDoc, collection, getDocs } from 'firebase/firestore';

async function main() {
  const publicDataDir = path.join(process.cwd(), 'public', 'data');
  const manifestPath = path.join(publicDataDir, 'curriculum_manifest.json');
  const vocabPath = path.join(publicDataDir, 'vocabulary_lexicon.json');
  const sectionsDir = path.join(publicDataDir, 'sections');

  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  const vocabList: any[] = JSON.parse(fs.readFileSync(vocabPath, 'utf-8'));
  const sectionFiles = fs.readdirSync(sectionsDir).filter(f => f.endsWith('.json')).sort();

  const allSections: any[] = [];
  const allUnits: any[] = [];
  const allLessons: any[] = [];
  const allExercises: any[] = [];

  for (const f of sectionFiles) {
    const s = JSON.parse(fs.readFileSync(path.join(sectionsDir, f), 'utf-8'));
    allSections.push(s);
    for (const u of s.units) {
      allUnits.push({ ...u, sectionId: s.sectionId, sectionNumber: s.sectionNumber, cefr: s.cefr });
      for (const l of u.lessons) {
        allLessons.push({ ...l, unitId: u.id, unitNumber: u.unitNumber, sectionId: s.sectionId, cefr: s.cefr });
        for (const ex of l.exercises) {
          allExercises.push({ ...ex, lessonId: l.id, unitId: u.id, sectionId: s.sectionId, cefr: s.cefr });
        }
      }
    }
  }

  console.log('=== 1. RECORD COUNTS & PHYSICAL STORAGE ===');
  console.log('Sections:', allSections.length);
  console.log('Units:', allUnits.length);
  console.log('Lessons:', allLessons.length);
  console.log('Exercises:', allExercises.length);
  console.log('Vocabulary records:', vocabList.length);

  // Vocabulary properties check
  let missingDef = 0;
  let missingPos = 0;
  let missingExample = 0;
  const cyrillicMap = new Map<string, any>();
  const duplicates: string[] = [];

  for (const v of vocabList) {
    if (!v.english || v.english.trim() === '') missingDef++;
    if (!v.partOfSpeech || v.partOfSpeech.trim() === '') missingPos++;
    if (!v.exampleSentenceCyrillic || v.exampleSentenceCyrillic.trim() === '') missingExample++;
    const key = v.cyrillic.trim().toLowerCase();
    if (cyrillicMap.has(key)) {
      duplicates.push(v.cyrillic);
    } else {
      cyrillicMap.set(key, v);
    }
  }
  console.log('Unique Cyrillic forms:', cyrillicMap.size);
  console.log('Duplicate Cyrillic forms:', duplicates.length);
  console.log('Missing definition:', missingDef);
  console.log('Missing POS:', missingPos);
  console.log('Missing example sentence:', missingExample);

  // Fast Vocabulary occurrence index
  console.log('\n=== VOCABULARY USAGE & RECYCLING ===');
  // Tokenize all exercises
  const vocabUsageMap = new Map<string, { count: number; lessons: Set<string>; firstLesson: string }>();
  for (const v of vocabList) {
    vocabUsageMap.set(v.cyrillic.toLowerCase(), { count: 0, lessons: new Set(), firstLesson: '' });
  }

  // Check lesson vocabulary explicitly
  for (const l of allLessons) {
    for (const v of l.vocabulary) {
      const entry = vocabUsageMap.get(v.cyrillic.toLowerCase());
      if (entry) {
        if (!entry.firstLesson) entry.firstLesson = l.id;
        entry.lessons.add(l.id);
      }
    }
  }

  // Fast text search across all exercises concatenated per lesson
  for (const l of allLessons) {
    const lessonText = JSON.stringify(l.exercises).toLowerCase();
    for (const v of vocabList) {
      const term = v.cyrillic.toLowerCase();
      if (lessonText.includes(term)) {
        const entry = vocabUsageMap.get(term);
        if (entry) {
          entry.count += 1;
          entry.lessons.add(l.id);
        }
      }
    }
  }

  let count0 = 0, count1 = 0, count2to3 = 0, count4to9 = 0, count10plus = 0;
  const countsArr: number[] = [];
  for (const [_, data] of vocabUsageMap) {
    countsArr.push(data.count);
    if (data.count === 0) count0++;
    else if (data.count === 1) count1++;
    else if (data.count <= 3) count2to3++;
    else if (data.count <= 9) count4to9++;
    else count10plus++;
  }
  countsArr.sort((a, b) => a - b);
  const medianUse = countsArr[Math.floor(countsArr.length / 2)];

  console.log(`Appearances in exercises:`);
  console.log(`  0 times: ${count0} (${(count0 / vocabList.length * 100).toFixed(1)}%)`);
  console.log(`  1 time: ${count1} (${(count1 / vocabList.length * 100).toFixed(1)}%)`);
  console.log(`  2-3 times: ${count2to3} (${(count2to3 / vocabList.length * 100).toFixed(1)}%)`);
  console.log(`  4-9 times: ${count4to9} (${(count4to9 / vocabList.length * 100).toFixed(1)}%)`);
  console.log(`  10+ times: ${count10plus} (${(count10plus / vocabList.length * 100).toFixed(1)}%)`);
  console.log(`  Median appearance count: ${medianUse}`);

  // 5. Template Duplication Audit
  console.log('\n=== 5. TEMPLATE DUPLICATION AUDIT ===');
  const exactPrompts = new Set(allExercises.map(e => e.prompt.trim()));
  const exactAnswerSets = new Set(allExercises.map(e => JSON.stringify({
    ans: e.correctAnswer,
    suf: e.correctSuffix,
    tokens: e.correctTokenOrder,
    opts: e.options?.map((o: any) => o.text)
  })));

  console.log('Total exercises:', allExercises.length);
  console.log('Unique exact prompts:', exactPrompts.size);
  console.log('Unique exact answer sets:', exactAnswerSets.size);

  const normalizedTemplates = allExercises.map(e => {
    return e.prompt
      .replace(/"[^"]+"/g, '<QUOTE>')
      .replace(/[А-Яа-яЁёӨөҮү]+/g, '<CYRILLIC>')
      .replace(/\d+/g, '<NUM>')
      .trim();
  });
  const uniqueNormalized = new Set(normalizedTemplates);
  console.log('Unique normalized prompt templates:', uniqueNormalized.size);
  console.log('Average exercises per template:', (allExercises.length / uniqueNormalized.size).toFixed(2));

  const templateClusters: Record<string, number> = {};
  for (const t of normalizedTemplates) {
    templateClusters[t] = (templateClusters[t] || 0) + 1;
  }
  const sortedClusters = Object.entries(templateClusters).sort((a, b) => b[1] - a[1]);
  console.log('Largest template cluster count:', sortedClusters[0]?.[1]);
  console.log('Largest cluster template:', sortedClusters[0]?.[0]);
  console.log('Top 5 template clusters:');
  sortedClusters.slice(0, 5).forEach(([t, c]) => console.log(`   [${c}] ${t}`));

  let inClusterGt10 = 0;
  for (const [_, count] of sortedClusters) {
    if (count > 10) inClusterGt10 += count;
  }
  console.log(`Exercises in template clusters > 10: ${inClusterGt10} (${(inClusterGt10 / allExercises.length * 100).toFixed(1)}%)`);

  // 6. Lesson Uniqueness
  console.log('\n=== 6. LESSON UNIQUENESS ===');
  const uniqueTitles = new Set(allLessons.map(l => l.title.trim()));
  const uniqueCyrillicTitles = new Set(allLessons.map(l => l.cyrillicTitle.trim()));
  const uniqueSummaries = new Set(allLessons.map(l => l.grammarOverview.summary.trim()));
  console.log('Unique lesson titles:', uniqueTitles.size);
  console.log('Unique cyrillic titles:', uniqueCyrillicTitles.size);
  console.log('Unique grammar overview summaries:', uniqueSummaries.size);

  // 12. CEFR Depth
  console.log('\n=== 12. CEFR DEPTH ===');
  for (const lvl of ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']) {
    const secLvl = allSections.filter(s => s.cefr === lvl);
    const unitLvl = allUnits.filter(u => u.cefr === lvl);
    const lesLvl = allLessons.filter(l => l.cefr === lvl);
    const exLvl = allExercises.filter(e => e.cefr === lvl);

    const vocabSet = new Set<string>();
    for (const l of lesLvl) {
      for (const v of l.vocabulary) {
        vocabSet.add(v.cyrillic);
      }
    }

    const dictation = exLvl.filter(e => e.type === 'AUDIO_DICTATION').length;
    const comprehension = exLvl.filter(e => e.type === 'AUDIO_COMPREHENSION').length;
    const phonetic = exLvl.filter(e => e.type === 'PHONETIC_DISCRIMINATION').length;
    const sentence = exLvl.filter(e => e.type === 'SENTENCE_CONSTRUCTION').length;
    const grammarApp = exLvl.filter(e => e.type === 'GRAMMAR_APPLICATION').length;
    const translation = exLvl.filter(e => e.type === 'TRANSLATION').length;
    const vocabMatch = exLvl.filter(e => e.type === 'VOCABULARY_MATCH').length;

    console.log(`CEFR ${lvl}:`);
    console.log(`   Sections: ${secLvl.length}, Units: ${unitLvl.length}, Lessons: ${lesLvl.length}, Exercises: ${exLvl.length}`);
    console.log(`   Unique Vocab in lessons: ${vocabSet.size}`);
    console.log(`   Audio Dictation: ${dictation}, Audio Comp: ${comprehension}, Phonetic: ${phonetic}`);
    console.log(`   Sentence Construction: ${sentence}, Grammar App: ${grammarApp}`);
    console.log(`   Translation: ${translation}, Vocab Match: ${vocabMatch}`);
  }

  // 2. Firestore Audit
  console.log('\n=== 2. FIRESTORE AUDIT ===');
  const configPath = path.join(process.cwd(), 'firebase-applet-config.json');
  const fbConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  const app = initializeApp(fbConfig);
  const db = getFirestore(app, fbConfig.firestoreDatabaseId);

  const courseSnap = await getDoc(doc(db, 'courses', 'mongolian_cyrillic_comprehensive'));
  console.log('Document "courses/mongolian_cyrillic_comprehensive" exists:', courseSnap.exists());
  if (courseSnap.exists()) {
    console.log('   Course Document fields:', Object.keys(courseSnap.data() || {}));
  }

  const sectionsSnap = await getDocs(collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'sections'));
  console.log('Collection "courses/mongolian_cyrillic_comprehensive/sections" document count:', sectionsSnap.size);

  const unitsSnap = await getDocs(collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'units'));
  console.log('Collection "courses/mongolian_cyrillic_comprehensive/units" document count:', unitsSnap.size);

  const lessonsSnap = await getDocs(collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'lessons'));
  console.log('Collection "courses/mongolian_cyrillic_comprehensive/lessons" document count:', lessonsSnap.size);

  const exercisesSnap = await getDocs(collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'exercises'));
  console.log('Collection "courses/mongolian_cyrillic_comprehensive/exercises" document count:', exercisesSnap.size);

  const vocabSnap = await getDocs(collection(db, 'lexicon'));
  console.log('Collection "lexicon" document count:', vocabSnap.size);

  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
