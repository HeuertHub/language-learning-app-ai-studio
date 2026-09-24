import * as fs from 'fs';
import * as path from 'path';

const rootDir = process.cwd();
const archiveDir = path.join(rootDir, 'archive', 'failed_curriculum_v1');
const archiveDataDir = path.join(archiveDir, 'data');
const archiveScriptsDir = path.join(archiveDir, 'generator_scripts');

fs.mkdirSync(archiveDataDir, { recursive: true });
fs.mkdirSync(archiveScriptsDir, { recursive: true });

console.log('=== 1. ARCHIVING AND REMOVING PUBLIC DATA FILES ===');

const publicDataDir = path.join(rootDir, 'public', 'data');
if (fs.existsSync(publicDataDir)) {
  const dataFiles = fs.readdirSync(publicDataDir);
  for (const item of dataFiles) {
    const srcPath = path.join(publicDataDir, item);
    const destPath = path.join(archiveDataDir, item);

    if (fs.lstatSync(srcPath).isDirectory()) {
      // Move directory
      console.log(`Moving directory: public/data/${item} -> archive/failed_curriculum_v1/data/${item}`);
      fs.cpSync(srcPath, destPath, { recursive: true });
      fs.rmSync(srcPath, { recursive: true, force: true });
    } else {
      // Move file
      console.log(`Moving file: public/data/${item} -> archive/failed_curriculum_v1/data/${item}`);
      fs.copyFileSync(srcPath, destPath);
      fs.unlinkSync(srcPath);
    }
  }
}

console.log('\n=== 2. ARCHIVING AND REMOVING GENERATOR & AUDIT SCRIPTS ===');

const scriptsDir = path.join(rootDir, 'scripts');
const scriptsToArchive = [
  'generator',
  'auditCurriculum.ts',
  'audit_deep_inspection.ts',
  'audit_detailed_samples.ts',
  'audit_remaining_questions.ts',
  'uploadCurriculumToFirestore.ts'
];

for (const item of scriptsToArchive) {
  const srcPath = path.join(scriptsDir, item);
  if (fs.existsSync(srcPath)) {
    const destPath = path.join(archiveScriptsDir, item);
    if (fs.lstatSync(srcPath).isDirectory()) {
      console.log(`Moving directory: scripts/${item} -> archive/failed_curriculum_v1/generator_scripts/${item}`);
      fs.cpSync(srcPath, destPath, { recursive: true });
      fs.rmSync(srcPath, { recursive: true, force: true });
    } else {
      console.log(`Moving file: scripts/${item} -> archive/failed_curriculum_v1/generator_scripts/${item}`);
      fs.copyFileSync(srcPath, destPath);
      fs.unlinkSync(srcPath);
    }
  }
}

console.log('\n=== 3. VERIFYING REMOVAL FROM PUBLIC/DATA ===');
if (fs.existsSync(publicDataDir)) {
  const remaining = fs.readdirSync(publicDataDir);
  console.log(`Remaining files in public/data: [${remaining.join(', ')}]`);
} else {
  console.log(`public/data directory is empty/cleared.`);
}

console.log('\n=== 4. ARCHIVE CONTENTS VERIFICATION ===');
console.log('Archived data items:', fs.readdirSync(archiveDataDir));
console.log('Archived generator script items:', fs.readdirSync(archiveScriptsDir));
if (fs.existsSync(path.join(archiveDataDir, 'sections'))) {
  console.log('Archived sections count:', fs.readdirSync(path.join(archiveDataDir, 'sections')).length);
}

process.exit(0);
