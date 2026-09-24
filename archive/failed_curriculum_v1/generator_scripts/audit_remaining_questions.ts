import * as fs from 'fs';
import * as path from 'path';

const publicDataDir = path.join(process.cwd(), 'public', 'data');
const vocabList: any[] = JSON.parse(fs.readFileSync(path.join(publicDataDir, 'vocabulary_lexicon.json'), 'utf-8'));
const manifest: any = JSON.parse(fs.readFileSync(path.join(publicDataDir, 'curriculum_manifest.json'), 'utf-8'));
const sectionsDir = path.join(publicDataDir, 'sections');
const sectionFiles = fs.readdirSync(sectionsDir).filter(f => f.endsWith('.json')).sort();

const allLessons: any[] = [];
const allExercises: any[] = [];
for (const f of sectionFiles) {
  const s = JSON.parse(fs.readFileSync(path.join(sectionsDir, f), 'utf-8'));
  for (const u of s.units) {
    for (const l of u.lessons) {
      allLessons.push({ ...l, unitId: u.id, sectionId: s.sectionId, cefr: s.cefr });
      for (const ex of l.exercises) {
        allExercises.push({ ...ex, lessonId: l.id, unitId: u.id, sectionId: s.sectionId, cefr: s.cefr });
      }
    }
  }
}

console.log('=== 7. VOCABULARY AUDIT DETAILED ===');
let lemmas = 0;
let phrases = 0;
let properNouns = 0;
let particles = 0;
let inflectedForms = 0;

for (const v of vocabList) {
  const text = v.cyrillic.trim();
  if (text.includes(' ')) {
    phrases++;
  } else if (/^[А-ЯЁӨҮ]/.test(text) && !['Би', 'Чи', 'Та', 'Тэр', 'Бид', 'Та нар', 'Тэд'].includes(text)) {
    properNouns++;
  } else if (['уу', 'үү', 'юм', 'байна', 'боловч', 'бол', 'ч', 'л', 'даа', 'дээ', 'доо', 'дөө'].includes(text.toLowerCase())) {
    particles++;
  } else if (text.endsWith('аас') || text.endsWith('ээс') || text.endsWith('оос') || text.endsWith('өөс') ||
             text.endsWith('аар') || text.endsWith('ээр') || text.endsWith('оор') || text.endsWith('өөр') ||
             text.endsWith('ийг') || text.endsWith('ыг') || text.endsWith('тай') || text.endsWith('тэй') ||
             text.endsWith('гүй') || text.endsWith('лаа') || text.endsWith('лээ') || text.endsWith('лоо') ||
             text.endsWith('нүүд') || text.endsWith('үүд') || text.endsWith('чууд') || text.endsWith('нууд')) {
    inflectedForms++;
  } else {
    lemmas++;
  }
}
console.log('Lemmas:', lemmas);
console.log('Phrases:', phrases);
console.log('Proper Nouns:', properNouns);
console.log('Grammatical Particles:', particles);
console.log('Surface inflected forms:', inflectedForms);

// 9. Grammar Coverage Audit
console.log('\n=== 9. GRAMMAR CONCEPTS AUDIT ===');
const grammarMap = new Map<string, {
  id: string;
  title: string;
  cyrillic: string;
  cefr: string;
  introLesson: string;
  practiceLessons: Set<string>;
  exerciseCount: number;
}>();

for (const l of allLessons) {
  for (const r of l.grammarOverview.rules) {
    if (!grammarMap.has(r.id)) {
      grammarMap.set(r.id, {
        id: r.id,
        title: r.title,
        cyrillic: r.cyrillicTitle,
        cefr: l.cefr,
        introLesson: l.id,
        practiceLessons: new Set(),
        exerciseCount: 0
      });
    } else {
      grammarMap.get(r.id)!.practiceLessons.add(l.id);
    }
  }
}

for (const ex of allExercises) {
  if (ex.grammarConceptId && grammarMap.has(ex.grammarConceptId)) {
    grammarMap.get(ex.grammarConceptId)!.exerciseCount++;
  }
}

console.log('Total unique grammar concepts in lessons:', grammarMap.size);
for (const [id, data] of grammarMap) {
  console.log(`- [${data.cefr}] ${id}: "${data.title}" | Intro: ${data.introLesson} | Later practice lessons: ${data.practiceLessons.size} | Directly tagged exercises: ${data.exerciseCount}`);
}

// 10. Learning Dependency Audit
console.log('\n=== 10. LEARNING DEPENDENCY GRAPH AUDIT ===');
// Check if units or lessons contain prerequisite arrays or dependency fields
let unitsWithPrereqs = 0;
let lessonsWithPrereqs = 0;
for (const u of manifest.sections) {
  // check manifest
}
for (const s of sectionFiles) {
  const sData = JSON.parse(fs.readFileSync(path.join(sectionsDir, s), 'utf-8'));
  for (const u of sData.units) {
    if ((u as any).prerequisites && (u as any).prerequisites.length > 0) unitsWithPrereqs++;
    for (const l of u.lessons) {
      if ((l as any).prerequisites && (l as any).prerequisites.length > 0) lessonsWithPrereqs++;
    }
  }
}
console.log('Units with explicit prerequisite array:', unitsWithPrereqs);
console.log('Lessons with explicit prerequisite array:', lessonsWithPrereqs);

// 13. Fixed 11-exercise template
console.log('\n=== 13. FIXED 11-EXERCISE TEMPLATE CHECK ===');
const lessonsWith11 = allLessons.filter(l => l.exercises.length === 11).length;
console.log(`Lessons with exactly 11 exercises: ${lessonsWith11} / ${allLessons.length} (${(lessonsWith11/allLessons.length*100).toFixed(1)}%)`);

// Check exercise types per lesson
const typeSequences = new Set<string>();
for (const l of allLessons) {
  const seq = l.exercises.map((e: any) => e.type).join(' -> ');
  typeSequences.add(seq);
}
console.log('Distinct exercise type sequences across all 700 lessons:', typeSequences.size);
typeSequences.forEach(s => console.log('Sequence:', s));
