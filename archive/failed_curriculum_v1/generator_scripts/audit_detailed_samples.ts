import * as fs from 'fs';
import * as path from 'path';

const publicDataDir = path.join(process.cwd(), 'public', 'data');
const sectionsDir = path.join(publicDataDir, 'sections');
const vocabPath = path.join(publicDataDir, 'vocabulary_lexicon.json');

const vocabList = JSON.parse(fs.readFileSync(vocabPath, 'utf-8'));
const sectionFiles = fs.readdirSync(sectionsDir).filter(f => f.endsWith('.json')).sort();

const allLessons: any[] = [];
const allExercises: any[] = [];

for (const f of sectionFiles) {
  const s = JSON.parse(fs.readFileSync(path.join(sectionsDir, f), 'utf-8'));
  for (const u of s.units) {
    for (const l of u.lessons) {
      allLessons.push({
        ...l,
        sectionId: s.sectionId,
        sectionTitle: s.title,
        unitId: u.id,
        unitTitle: u.title,
        unitNumber: u.unitNumber,
        cefr: s.cefr
      });
      for (const ex of l.exercises) {
        allExercises.push({
          ...ex,
          lessonId: l.id,
          lessonTitle: l.title,
          unitId: u.id,
          sectionId: s.sectionId,
          cefr: s.cefr
        });
      }
    }
  }
}

// 3. LESSON CONTENT AUDIT: 10 lessons (2 A1, 2 A2, 2 B1, 2 B2, 1 C1, 1 C2)
const a1Lessons = allLessons.filter(l => l.cefr === 'A1');
const a2Lessons = allLessons.filter(l => l.cefr === 'A2');
const b1Lessons = allLessons.filter(l => l.cefr === 'B1');
const b2Lessons = allLessons.filter(l => l.cefr === 'B2');
const c1Lessons = allLessons.filter(l => l.cefr === 'C1');
const c2Lessons = allLessons.filter(l => l.cefr === 'C2');

const selectedLessons = [
  a1Lessons[0],
  a1Lessons[Math.floor(a1Lessons.length / 2)],
  a2Lessons[0],
  a2Lessons[Math.floor(a2Lessons.length / 2)],
  b1Lessons[0],
  b1Lessons[Math.floor(b1Lessons.length / 2)],
  b2Lessons[0],
  b2Lessons[Math.floor(b2Lessons.length / 2)],
  c1Lessons[Math.floor(c1Lessons.length / 2)],
  c2Lessons[Math.floor(c2Lessons.length / 2)],
];

fs.writeFileSync(path.join(publicDataDir, 'audit_selected_lessons.json'), JSON.stringify(selectedLessons, null, 2));

// 4. EXERCISE AUDIT: 30 exercises across A1, A2, B1, B2, C1, C2 and types
const exTypes = ['AUDIO_DICTATION', 'AUDIO_COMPREHENSION', 'SENTENCE_CONSTRUCTION', 'GRAMMAR_APPLICATION', 'PHONETIC_DISCRIMINATION', 'TRANSLATION', 'VOCABULARY_MATCH'];
const selectedExercises: any[] = [];

for (const lvl of ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']) {
  const lvlEx = allExercises.filter(e => e.cefr === lvl);
  for (let i = 0; i < 5; i++) {
    const targetType = exTypes[i % exTypes.length];
    const match = lvlEx.find(e => e.type === targetType && !selectedExercises.some(s => s.id === e.id));
    if (match) selectedExercises.push(match);
    else if (lvlEx[i]) selectedExercises.push(lvlEx[i]);
  }
}

fs.writeFileSync(path.join(publicDataDir, 'audit_selected_exercises.json'), JSON.stringify(selectedExercises.slice(0, 30), null, 2));

// 14. QUALITY SPOT CHECK: 50 randomly selected exercises
const step = Math.floor(allExercises.length / 50);
const spotCheck50: any[] = [];
for (let i = 0; i < 50; i++) {
  spotCheck50.push(allExercises[i * step]);
}
fs.writeFileSync(path.join(publicDataDir, 'audit_spot_check_50.json'), JSON.stringify(spotCheck50, null, 2));

console.log('Sample audit datasets written successfully.');
