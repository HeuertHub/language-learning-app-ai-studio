import type {
  LanguageCourse,
  LevelCurriculum,
  Unit,
  Lesson,
  CEFRLevel,
  GrammarRule,
} from '../types/curriculum';
import type { ExerciseDefinition } from '../types/exerciseEngine';

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
  totalVocabularyItems?: number;
  totalTargetProductiveLemmas?: number;
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
  private pilotExercisesCache: Record<string, ExerciseDefinition[]> | null = null;

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

  async getLessonExercises(lessonId: string): Promise<ExerciseDefinition[]> {
    if (!this.pilotExercisesCache) {
      try {
        const res = await fetch('/data/pilot_exercises.json');
        if (res.ok) {
          this.pilotExercisesCache = await res.json();
        } else {
          this.pilotExercisesCache = {};
        }
      } catch {
        this.pilotExercisesCache = {};
      }
    }
    return this.pilotExercisesCache?.[lessonId] || [];
  }

  // Preload and build comprehensive LanguageCourse object for SyllabusView
  async loadFullCourse(): Promise<LanguageCourse | null> {
    if (this.fullCourse) return this.fullCourse;

    // 1. Attempt fast single-bundle load from course_full.json
    try {
      const fullRes = await fetch('/data/course_full.json');
      if (fullRes.ok) {
        const data: LanguageCourse = await fullRes.json();
        if (data && data.levels && data.levels.length > 0) {
          // Authoritative masterGrammarReference derived strictly from frozen curriculum
          data.masterGrammarReference = data.masterGrammarReference || [];
          this.fullCourse = data;
          return this.fullCourse;
        }
      }
    } catch {
      // Fallback to manifest and section assembly
    }

    // 2. Fallback to section-by-section dynamic load
    const manifest = await this.getManifest();
    if (!manifest) {
      return null;
    }

    const cefrLevels: CEFRLevel[] = ['Pre-A1', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
    const CEFR_TITLES: Record<CEFRLevel, { title: string; cyrillic: string; desc: string; comp: string }> = {
      'Pre-A1': {
        title: 'Cyrillic Script Literacy & Primary Vowel Systems',
        cyrillic: 'Үсэг зүй ба авиан дуудлага',
        desc: 'Foundational grapheme-phoneme mastery of the 35 Cyrillic letters, vocalic harmony, and survival formulae.',
        comp: 'Can recognize and articulate all 35 Cyrillic characters, sound out syllables, and comprehend basic survival greetings.'
      },
      'A1': {
        title: 'Beginner Steppe Foundation',
        cyrillic: 'Анхан шат: Авиан зүй ба анхдагч хэлбэрүүд',
        desc: 'Core vowel harmony, zero copula equatives, dative-locative and accusative cases, and elemental nomadic interactions.',
        comp: 'Can introduce oneself, read Cyrillic fluently, form equative clauses, and navigate domestic greetings.'
      },
      'A2': {
        title: 'Elementary Pastoral & Environmental',
        cyrillic: 'Суурь шат: Ахуй амьдрал ба байгаль орчин',
        desc: 'Steppe geography, five domestic animals, ablative and instrumental cases, and reflexive possessive suffixes.',
        comp: 'Can describe pastoral settings, travel routes across Mongolia, and perform routine transactional exchanges.'
      },
      'B1': {
        title: 'Intermediate Conversational & Converbial',
        cyrillic: 'Дунд шат: Нийлмэл холбоос ба нүүдэлчин соёл',
        desc: 'Coordinating converbs (-ж/-ч, -аад), conditional clauses (-вал), concessives (-вч), and habitual past aspects.',
        comp: 'Can narrate sequential stories, articulate logical conditions, and discuss nomadic traditions.'
      },
      'B2': {
        title: 'Upper-Intermediate Syntactic & Analytical',
        cyrillic: 'Ахисан дунд шат: Үйлдэх хэв, түүх ба эдийн засаг',
        desc: 'Causative and passive voice transformations, periodic converb chaining, modern governance, ecology, and economy.',
        comp: 'Can understand historical discourse, explain economic and ecological challenges, and build complex sentences.'
      },
      'C1': {
        title: 'Advanced Stylistic & Honorific Register',
        cyrillic: 'Гүнзгий шат: Хүндэтгэлийн найруулга ба төрт ёс',
        desc: 'Elaborate Mongolian honorific system, ceremonial diplomatic rhetoric, philosophical treatises, and classical syntax.',
        comp: 'Can communicate in elevated diplomatic and formal registers and analyze classical academic publications.'
      },
      'C2': {
        title: 'Mastery: Steppe Literature, Epics & Philology',
        cyrillic: 'Төгс эзэмших шат: Монголын нууц товчоо ба туульс',
        desc: 'Secret History of the Mongols, heroic epics (Jangar, Geser), head-alliteration poetics, and archaic case appositions.',
        comp: 'Near-native scholarly mastery of literary Mongolian prose, epic meter, and classical philological texts.'
      }
    };

    // Load all sections
    const sectionPromises = manifest.sections.map((s) => this.getSection(s.sectionNumber));
    const loadedSections = (await Promise.all(sectionPromises)).filter((s): s is SectionData => s !== null);

    if (loadedSections.length === 0) {
      return null;
    }

    const levels: LevelCurriculum[] = cefrLevels.map((lvl) => {
      const secInLevel = loadedSections.filter((s) => s.cefr === lvl);
      const unitsInLevel: Unit[] = [];
      for (const s of secInLevel) {
        unitsInLevel.push(...s.units);
      }

      const meta = CEFR_TITLES[lvl];
      return {
        levelId: `lvl_${lvl.toLowerCase().replace('-', '_')}`,
        cefr: lvl,
        title: meta.title,
        cyrillicTitle: meta.cyrillic,
        description: meta.desc,
        targetCompetency: meta.comp,
        units: unitsInLevel,
      };
    });

    // Load authoritative derived grammar concepts
    let grammarRules: GrammarRule[] = [];
    try {
      const gRes = await fetch('/data/grammar_reference.json');
      if (gRes.ok) {
        grammarRules = await gRes.json();
      }
    } catch {
      grammarRules = [];
    }

    this.fullCourse = {
      id: manifest.courseId,
      name: manifest.name,
      cyrillicName: manifest.cyrillicName,
      script: manifest.script,
      description: manifest.description,
      cefrRange: 'Pre-A1 - C2',
      totalLevels: levels.length,
      levels,
      masterGrammarReference: grammarRules,
    };

    return this.fullCourse;
  }

  async getGrammarReference(): Promise<GrammarRule[]> {
    try {
      const res = await fetch('/data/grammar_reference.json');
      if (res.ok) {
        return await res.json();
      }
      return [];
    } catch {
      return [];
    }
  }
}

export const curriculumService = new CurriculumService();
