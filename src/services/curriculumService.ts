import type {
  LanguageCourse,
  LevelCurriculum,
  Unit,
  Lesson,
  CEFRLevel,
  GrammarRule,
  Exercise
} from '../types/curriculum';
import { MASTER_GRAMMAR_RULES } from '../data/mongolianCurriculum';

export interface SectionSummary {
  sectionId: string;
  sectionNumber: number;
  title: string;
  cyrillicTitle: string;
  cefr: CEFRLevel;
  theme: string;
  description: string;
  unitCount: number;
  startUnit: number;
  endUnit: number;
  lessonCount: number;
  exerciseCount: number;
  file: string;
}

export interface CurriculumManifest {
  courseId: string;
  name: string;
  cyrillicName: string;
  script: string;
  description: string;
  cefrLevels: CEFRLevel[];
  totalSections: number;
  totalUnits: number;
  totalLessons: number;
  totalExercises: number;
  totalVocabularyItems: number;
  sections: SectionSummary[];
}

export interface SectionData {
  sectionId: string;
  sectionNumber: number;
  title: string;
  cyrillicTitle: string;
  cefr: CEFRLevel;
  theme: string;
  description: string;
  units: Unit[];
}

class CurriculumService {
  private manifest: CurriculumManifest | null = null;
  private sectionCache: Map<string, SectionData> = new Map();
  private fullCourse: LanguageCourse | null = null;

  async getManifest(): Promise<CurriculumManifest | null> {
    if (this.manifest) return this.manifest;
    try {
      const res = await fetch('/data/curriculum_manifest.json');
      if (!res.ok) {
        return null;
      }
      this.manifest = await res.json();
      return this.manifest;
    } catch {
      return null;
    }
  }

  async getSection(sectionNumber: number): Promise<SectionData | null> {
    const key = `section-${String(sectionNumber).padStart(2, '0')}`;
    if (this.sectionCache.has(key)) {
      return this.sectionCache.get(key)!;
    }

    try {
      const res = await fetch(`/data/sections/${key}.json`);
      if (!res.ok) {
        return null;
      }
      const data: SectionData = await res.json();
      this.sectionCache.set(key, data);
      return data;
    } catch {
      return null;
    }
  }

  // Preload and build comprehensive LanguageCourse object for SyllabusView
  async loadFullCourse(): Promise<LanguageCourse | null> {
    if (this.fullCourse) return this.fullCourse;

    const manifest = await this.getManifest();
    if (!manifest) {
      return null;
    }
    
    // Group sections by CEFR
    const cefrLevels: CEFRLevel[] = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
    const CEFR_TITLES: Record<CEFRLevel, { title: string; cyrillic: string; desc: string; comp: string }> = {
      A1: {
        title: 'Beginner Steppe Foundation',
        cyrillic: 'Анхан шат: Авиан зүй ба анхдагч хэлбэрүүд',
        desc: 'Mastery of 35 Cyrillic letters, masculine/feminine vowel harmony, zero copula equatives, and core dative/accusative cases.',
        comp: 'Can introduce oneself, read Cyrillic fluently, form equative clauses, and navigate domestic greetings.'
      },
      A2: {
        title: 'Elementary Pastoral & Environmental',
        cyrillic: 'Суурь шат: Ахуй амьдрал ба байгаль орчин',
        desc: 'Steppe geography, five domestic animals, ablative/instrumental cases, and reflexive possessive suffixes.',
        comp: 'Can describe pastoral settings, travel routes across Mongolia, and perform routine transactional exchanges.'
      },
      B1: {
        title: 'Intermediate Conversational & Converbial',
        cyrillic: 'Дунд шат: Нийлмэл холбоос ба нүүдэлчин соёл',
        desc: 'Coordinating converbs (-ж/-ч, -аад), conditional clauses (-вал), concessives (-вч), and habitual past aspects.',
        comp: 'Can narrate sequential stories, articulate logical conditions, and discuss nomadic traditions.'
      },
      B2: {
        title: 'Upper-Intermediate Syntactic & Analytical',
        cyrillic: 'Ахисан дунд шат: Үйлдэх хэв, түүх ба эдийн засаг',
        desc: 'Causative and passive voice transformations, periodic converb chaining, modern governance, ecology, and economy.',
        comp: 'Can understand historical discourse, explain economic and ecological challenges, and build complex sentences.'
      },
      C1: {
        title: 'Advanced Stylistic & Honorific Register',
        cyrillic: 'Гүнзгий шат: Хүндэтгэлийн найруулга ба төрт ёс',
        desc: 'Elaborate Mongolian honorific system, ceremonial diplomatic rhetoric, philosophical treaties, and classical syntax.',
        comp: 'Can communicate in elevated diplomatic and formal registers and analyze classical academic publications.'
      },
      C2: {
        title: 'Mastery: Steppe Literature, Epics & Philology',
        cyrillic: 'Төгс эзэмших шат: Монголын нууц товчоо ба туульс',
        desc: 'Secret History of the Mongols, heroic epics (Jangar, Geser), head-alliteration poetics, and archaic case appositions.',
        comp: 'Near-native scholarly mastery of literary Mongolian prose, epic meter, and classical philological texts.'
      }
    };

    // Load initial sections (e.g. all 16 sections) to form complete curriculum tree
    const sectionPromises = manifest.sections.map(s => this.getSection(s.sectionNumber));
    const loadedSections = (await Promise.all(sectionPromises)).filter((s): s is SectionData => s !== null);

    const levels: LevelCurriculum[] = cefrLevels.map(lvl => {
      const secInLevel = loadedSections.filter(s => s.cefr === lvl);
      const unitsInLevel: Unit[] = [];
      for (const s of secInLevel) {
        unitsInLevel.push(...s.units);
      }

      const meta = CEFR_TITLES[lvl];
      return {
        levelId: `lvl_${lvl.toLowerCase()}`,
        cefr: lvl,
        title: meta.title,
        cyrillicTitle: meta.cyrillic,
        description: meta.desc,
        targetCompetency: meta.comp,
        units: unitsInLevel
      };
    });

    this.fullCourse = {
      id: manifest.courseId,
      name: manifest.name,
      cyrillicName: manifest.cyrillicName,
      script: manifest.script,
      description: manifest.description,
      cefrRange: 'A1 - C2',
      totalLevels: levels.length,
      levels,
      masterGrammarReference: MASTER_GRAMMAR_RULES
    };

    return this.fullCourse;
  }
}

export const curriculumService = new CurriculumService();
