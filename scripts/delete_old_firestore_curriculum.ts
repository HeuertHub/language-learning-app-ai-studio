import * as fs from 'fs';
import * as path from 'path';
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, getDoc, collection, getDocs, deleteDoc } from 'firebase/firestore';

async function main() {
  const configPath = path.join(process.cwd(), 'firebase-applet-config.json');
  const fbConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  const app = initializeApp(fbConfig);
  const db = getFirestore(app, fbConfig.firestoreDatabaseId);

  console.log('=== REMOVING OBSOLETE FIRESTORE DOCUMENTS ===');

  // 1. Delete section documents in subcollection
  const sectionsRef = collection(db, 'courses', 'mongolian_cyrillic_comprehensive', 'sections');
  const sectionsSnap = await getDocs(sectionsRef);
  console.log(`Found ${sectionsSnap.size} section documents to delete:`);

  for (const s of sectionsSnap.docs) {
    console.log(` Deleting section document: courses/mongolian_cyrillic_comprehensive/sections/${s.id}`);
    await deleteDoc(s.ref);
  }

  // 2. Delete parent course document
  const courseDocRef = doc(db, 'courses', 'mongolian_cyrillic_comprehensive');
  const courseSnap = await getDoc(courseDocRef);
  if (courseSnap.exists()) {
    console.log(' Deleting course document: courses/mongolian_cyrillic_comprehensive');
    await deleteDoc(courseDocRef);
  } else {
    console.log(' Course document already absent.');
  }

  // 3. Verify deletion
  const verifyCourse = await getDoc(courseDocRef);
  const verifySections = await getDocs(sectionsRef);
  console.log(`\nVerification:`);
  console.log(`Course doc exists: ${verifyCourse.exists()}`);
  console.log(`Section docs count: ${verifySections.size}`);

  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
