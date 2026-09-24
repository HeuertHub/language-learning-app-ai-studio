import * as fs from 'fs';
import * as path from 'path';
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, setDoc, writeBatch } from 'firebase/firestore';
import { getAuth, signInAnonymously } from 'firebase/auth';

// Load config from root
const configPath = path.join(process.cwd(), 'firebase-applet-config.json');
if (!fs.existsSync(configPath)) {
  console.error('firebase-applet-config.json not found!');
  process.exit(1);
}

const firebaseConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
const app = initializeApp(firebaseConfig);
const db = getFirestore(app, firebaseConfig.firestoreDatabaseId);
const auth = getAuth(app);

async function uploadCurriculum() {
  console.log('Connecting to Firestore database:', firebaseConfig.firestoreDatabaseId);

  const publicDataDir = path.join(process.cwd(), 'public', 'data');
  const manifestPath = path.join(publicDataDir, 'curriculum_manifest.json');
  const sectionsDir = path.join(publicDataDir, 'sections');

  // 1. Upload Master Course Manifest
  console.log('Uploading course manifest to Firestore...');
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  await setDoc(doc(db, 'courses', manifest.courseId), manifest);
  console.log('Course manifest uploaded successfully.');

  // 2. Upload Section Documents
  const sectionFiles = fs.readdirSync(sectionsDir).filter(f => f.endsWith('.json'));
  console.log(`Uploading ${sectionFiles.length} sections to Firestore...`);

  for (const file of sectionFiles) {
    const secData = JSON.parse(fs.readFileSync(path.join(sectionsDir, file), 'utf-8'));
    console.log(`Writing section: ${secData.sectionId} - ${secData.title} (${secData.units.length} units)...`);
    
    let success = false;
    let attempts = 0;
    while (!success && attempts < 5) {
      attempts++;
      try {
        // Store section document under courses/mongolian_cyrillic_comprehensive/sections/{sectionId}
        await setDoc(doc(db, 'courses', manifest.courseId, 'sections', secData.sectionId), {
          sectionId: secData.sectionId,
          sectionNumber: secData.sectionNumber,
          title: secData.title,
          cyrillicTitle: secData.cyrillicTitle,
          cefr: secData.cefr,
          theme: secData.theme,
          description: secData.description,
          unitCount: secData.units.length,
          lessonCount: secData.units.reduce((acc: number, u: any) => acc + u.lessons.length, 0),
          unitsOverview: secData.units.map((u: any) => ({
            unitId: u.id,
            unitNumber: u.unitNumber,
            title: u.title,
            cyrillicTitle: u.cyrillicTitle,
            cefrLevel: u.cefrLevel,
            lessonCount: u.lessons.length,
            primaryGrammarTopic: u.primaryGrammarTopic
          }))
        });
        console.log(`Successfully stored ${secData.sectionId}`);
        success = true;
        await new Promise(r => setTimeout(r, 800));
      } catch (err: any) {
        if (attempts >= 5) {
          console.error(`Failed to store section ${secData.sectionId} after 5 attempts:`, err?.message || err);
          throw err;
        }
        console.warn(`Attempt ${attempts} failed for ${secData.sectionId}, retrying in ${attempts * 1500}ms...`);
        await new Promise(r => setTimeout(r, attempts * 1500));
      }
    }

  }


  console.log('All 16 sections uploaded to Firestore!');
  console.log('Firestore curriculum deployment complete.');
}

uploadCurriculum()
  .then(() => {
    console.log('Batch upload finished successfully.');
    process.exit(0);
  })
  .catch((err) => {
    console.error('Error uploading curriculum to Firestore:', err);
    process.exit(1);
  });
