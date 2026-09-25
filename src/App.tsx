import React, { useState, useEffect } from 'react';
import { Navbar, type NavTab } from './components/Navbar';
import { SyllabusView } from './components/SyllabusView';
import { LessonView } from './components/LessonView';
import { ProgressDashboard } from './components/ProgressDashboard';
import { GrammarLibrary } from './components/GrammarLibrary';
import { StudyNotebook } from './components/StudyNotebook';
import { curriculumService } from './services/curriculumService';
import {
  initializeAuth,
  testFirestoreConnection,
} from './services/firebase';
import {
  fetchCourseProgress,
  persistCourseProgress,
  fetchUserStudyNotes,
  persistStudyNote,
  removeStudyNote,
} from './services/progressService';
import type {
  LanguageCourse,
  Lesson,
  Unit,
  LevelCurriculum,
  CourseCompletionStats,
  UserStudyNote,
} from './types/curriculum';
import { AlertCircle, RefreshCw } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState<NavTab>('syllabus');
  const [activeLessonContext, setActiveLessonContext] = useState<{
    lesson: Lesson;
    unit: Unit;
    level: LevelCurriculum;
  } | null>(null);

  const [course, setCourse] = useState<LanguageCourse | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [userId, setUserId] = useState<string>('local_learner');
  const [isCloudConnected, setIsCloudConnected] = useState<boolean>(false);
  const [audioSpeed, setAudioSpeed] = useState<number>(1.0);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Course Progress State
  const [progress, setProgress] = useState<CourseCompletionStats>({
    courseId: 'mongolian-comprehensive',
    userId: 'local_learner',
    completedLessonIds: [],
    completedUnitIds: [],
    masteredVocabCount: 0,
    totalExercisesAttempted: 0,
    totalExercisesCorrect: 0,
    timeSpentMinutes: 0,
    lastStudiedAt: new Date().toISOString(),
  });

  // User Study Notes State
  const [studyNotes, setStudyNotes] = useState<UserStudyNote[]>([]);

  const loadAuthoritativeCurriculum = async () => {
    setIsLoading(true);
    setLoadError(null);
    try {
      // Sourced exclusively from derived runtime assets in /public/data
      const fullCourse = await curriculumService.loadFullCourse();
      if (!fullCourse || !fullCourse.levels || fullCourse.levels.length === 0) {
        throw new Error(
          'Authoritative curriculum data could not be loaded from /data/curriculum_manifest.json or /data/course_full.json. Silent fallback to prototype data is prohibited.'
        );
      }
      setCourse(fullCourse);

      const user = await initializeAuth();
      setUserId(user.uid);

      const isOnline = await testFirestoreConnection();
      setIsCloudConnected(isOnline);

      // Fetch cloud course completion data
      const currentProgress = await fetchCourseProgress(fullCourse.id, user.uid);
      setProgress(currentProgress);

      // Fetch cloud study notes
      const notes = await fetchUserStudyNotes(user.uid);
      setStudyNotes(notes);
    } catch (err) {
      console.error('Curriculum loading failure:', err);
      setLoadError(
        err instanceof Error
          ? err.message
          : 'Failed to load derived frozen curriculum assets from /data. Production mode requires valid runtime assets.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadAuthoritativeCurriculum();
  }, []);

  const handleToggleAudioSpeed = () => {
    setAudioSpeed((prev) => (prev === 1.0 ? 0.75 : 1.0));
  };

  const handleSelectLesson = (lesson: Lesson, unit: Unit, level: LevelCurriculum) => {
    setActiveLessonContext({ lesson, unit, level });
  };

  const handleBackToSyllabus = () => {
    setActiveLessonContext(null);
  };

  const handleCompleteLesson = async (stats: {
    lessonId: string;
    unitId: string;
    exercisesAttempted: number;
    exercisesCorrect: number;
    minutesSpent: number;
    vocabMasteredCount: number;
  }) => {
    if (!course) return;

    const updatedCompletedLessons = Array.from(
      new Set([...progress.completedLessonIds, stats.lessonId])
    );

    // Check if entire unit is now completed
    const targetUnit = course.levels
      .flatMap((lvl) => lvl.units)
      .find((u) => u.id === stats.unitId);

    let updatedCompletedUnits = progress.completedUnitIds;
    if (targetUnit) {
      const allLessonsDone = targetUnit.lessons.every((l) =>
        updatedCompletedLessons.includes(l.id)
      );
      if (allLessonsDone) {
        updatedCompletedUnits = Array.from(
          new Set([...updatedCompletedUnits, stats.unitId])
        );
      }
    }

    const updatedProgress: CourseCompletionStats = {
      ...progress,
      userId,
      completedLessonIds: updatedCompletedLessons,
      completedUnitIds: updatedCompletedUnits,
      masteredVocabCount: progress.masteredVocabCount + stats.vocabMasteredCount,
      totalExercisesAttempted: progress.totalExercisesAttempted + stats.exercisesAttempted,
      totalExercisesCorrect: progress.totalExercisesCorrect + stats.exercisesCorrect,
      timeSpentMinutes: progress.timeSpentMinutes + stats.minutesSpent,
      lastStudiedAt: new Date().toISOString(),
    };

    setProgress(updatedProgress);
    await persistCourseProgress(updatedProgress);
  };

  const handleSaveNote = async (note: UserStudyNote) => {
    setStudyNotes((prev) => {
      const idx = prev.findIndex((n) => n.id === note.id);
      if (idx >= 0) {
        const copy = [...prev];
        copy[idx] = note;
        return copy;
      }
      return [note, ...prev];
    });

    await persistStudyNote({ ...note, userId });
  };

  const handleDeleteNote = async (noteId: string) => {
    setStudyNotes((prev) => prev.filter((n) => n.id !== noteId));
    await removeStudyNote(userId, noteId);
  };

  // Visible Production Error Gate
  if (loadError) {
    return (
      <div className="min-h-screen bg-stone-50 flex flex-col items-center justify-center p-6 text-center">
        <div className="max-w-md w-full bg-white border border-red-200 rounded-xl p-6 shadow-sm space-y-4">
          <div className="w-12 h-12 bg-red-50 text-red-700 rounded-full flex items-center justify-center mx-auto border border-red-200">
            <AlertCircle className="w-6 h-6" />
          </div>
          <div className="space-y-1">
            <h2 className="font-serif text-lg font-bold text-stone-900">
              Curriculum Data Unavailable
            </h2>
            <p className="text-xs text-red-800 leading-relaxed font-mono">
              {loadError}
            </p>
          </div>
          <p className="text-xs text-stone-500">
            Production mode does not silently fallback to obsolete prototype data. Please verify derived runtime assets are built in <code>/public/data/</code>.
          </p>
          <button
            type="button"
            onClick={loadAuthoritativeCurriculum}
            className="w-full py-2.5 px-4 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs flex items-center justify-center gap-2"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Retry Loading Authoritative Curriculum</span>
          </button>
        </div>
      </div>
    );
  }

  if (isLoading || !course) {
    return (
      <div className="min-h-screen bg-stone-50 flex flex-col items-center justify-center p-6 text-center">
        <div className="w-12 h-12 rounded-full border-2 border-stone-300 border-t-stone-800 animate-spin mb-4" />
        <h2 className="font-serif text-lg font-semibold text-stone-800">
          Монгол Хэлний Цогц Хөтөлбөр
        </h2>
        <p className="text-stone-500 text-xs mt-1 font-mono">
          Loading Authoritative Curriculum (Pre-A1 through C2)...
        </p>
      </div>
    );
  }

  // Derive counts dynamically from loaded course data
  const totalUnits = course.levels.reduce((acc, lvl) => acc + lvl.units.length, 0);
  const totalLessons = course.levels.reduce(
    (acc, lvl) => acc + lvl.units.reduce((uAcc, u) => uAcc + u.lessons.length, 0),
    0
  );

  return (
    <div className="min-h-screen flex flex-col bg-stone-50 text-stone-900 selection:bg-stone-200">
      {/* Universal Academic Navigation */}
      <Navbar
        activeTab={activeLessonContext ? 'syllabus' : activeTab}
        onTabChange={(tab) => {
          setActiveLessonContext(null);
          setActiveTab(tab);
        }}
        audioSpeed={audioSpeed}
        onToggleAudioSpeed={handleToggleAudioSpeed}
        isCloudConnected={isCloudConnected}
        activeCourseName={course.name}
      />

      {/* Main Content View Container */}
      <main className="flex-1 pb-16">
        {activeLessonContext ? (
          <LessonView
            lesson={activeLessonContext.lesson}
            unit={activeLessonContext.unit}
            level={activeLessonContext.level}
            onBackToSyllabus={handleBackToSyllabus}
            onCompleteLesson={handleCompleteLesson}
            audioSpeed={audioSpeed}
          />
        ) : activeTab === 'syllabus' ? (
          <SyllabusView
            course={course}
            progress={progress}
            onSelectLesson={handleSelectLesson}
            onOpenGrammarLibrary={() => setActiveTab('grammar')}
          />
        ) : activeTab === 'grammar' ? (
          <GrammarLibrary
            rules={course.masterGrammarReference}
            audioSpeed={audioSpeed}
          />
        ) : activeTab === 'dashboard' ? (
          <ProgressDashboard
            course={course}
            progress={progress}
            onNavigateToSyllabus={() => setActiveTab('syllabus')}
          />
        ) : activeTab === 'notes' ? (
          <StudyNotebook
            notes={studyNotes}
            userId={userId}
            onSaveNote={handleSaveNote}
            onDeleteNote={handleDeleteNote}
          />
        ) : null}
      </main>

      {/* Subtle Academic Footer with Dynamic Counts */}
      <footer className="border-t border-stone-200 bg-white py-6 text-stone-500 text-xs text-center">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div>
            <span className="font-serif font-semibold text-stone-700">Монгол Хэл</span>
            <span className="mx-2">•</span>
            <span>Comprehensive Mongolian Cyrillic Pedagogical System (Pre-A1–C2)</span>
          </div>
          <div className="font-mono text-[11px] text-stone-400">
            {totalUnits} Units • {totalLessons} Lessons • Pre-A1–C2 Continuum • Zero Gamification
          </div>
        </div>
      </footer>
    </div>
  );
}
