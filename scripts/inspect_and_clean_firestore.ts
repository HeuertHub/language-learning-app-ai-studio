import * as fs from 'fs';
import * as path from 'path';
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, getDoc, collection, getDocs, deleteDoc } from 'firebase/firestore';

async function main() {
  const configPath = path.join(process.cwd(), 'firebase-applet-config.json');
  const fbConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  const app = initializeApp(fbConfig);
  const db = getFirestore(app, fbConfig.firestoreDatabaseId);

  // Check specific test user paths in case they were written
  const testUids = ['local_learner', 'local_learner_fallback', 'dev_learner'];
  for (const uid of testUids) {
    try {
      const pDoc = await getDoc(doc(db, 'users', uid, 'progress', 'mongolian_cyrillic_comprehensive'));
      console.log(`User ${uid} progress doc exists:`, pDoc.exists());
      if (pDoc.exists()) {
        console.log(`User ${uid} progress data:`, pDoc.data());
      }
    } catch (e: any) {
      console.log(`User ${uid} progress query:`, e.code || e.message);
    }
  }

  // Check courses collection
  const courseDocRef = doc(db, 'courses', 'mongolian_cyrillic_comprehensive');
  const courseSnap = await getDoc(courseDocRef);
  console.log('\nCourse doc exists:', courseSnap.exists());
  
  const sectionsSnap = await getDocs(collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'sections'));
  console.log(`Sections count: ${sectionsSnap.size}`);
  sectionsSnap.forEach(s => {
    console.log(` - ${s.id}: ${s.data()?.title}`);
  });

  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
