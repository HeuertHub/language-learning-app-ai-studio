import React, { useState, useEffect } from 'react';
import { Navbar, type NavTab } from './components/Navbar';
import { SyllabusView } from './components/SyllabusView';
import { LessonView } from './components/LessonView';
import { ProgressDashboard } from './components/ProgressDashboard';
import { GrammarLibrary } from './components/GrammarLibrary';
import { StudyNotebook } from './components/StudyNotebook';
import { MONGOLIAN_COURSE } from './data/mongolianCurriculum';
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

export default function App() {
  const [activeTab, setActiveTab] = useState<NavTab>('syllabus');
  const [activeLessonContext, setActiveLessonContext] = useState<{
    lesson: Lesson;
    unit: Unit;
    level: LevelCurriculum;
  } | null>(null);

  const [course, setCourse] = useState<LanguageCourse>(MONGOLIAN_COURSE);
  const [userId, setUserId] = useState<string>('local_learner');
  const [isCloudConnected, setIsCloudConnected] = useState<boolean>(false);
  const [audioSpeed, setAudioSpeed] = useState<number>(1.0);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Course Progress State
  const [progress, setProgress] = useState<CourseCompletionStats>({
    courseId: MONGOLIAN_COURSE.id,
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

  // Initial cloud handshake & full curriculum load
  useEffect(() => {
    async function setupApp() {
      setIsLoading(true);
      try {
        // Load production curriculum dataset (16 sections, 120 units, 700 lessons)
        const fullCourse = await curriculumService.loadFullCourse();
        if (fullCourse && fullCourse.levels.length > 0) {
          setCourse(fullCourse);
        }

        const user = await initializeAuth();
        setUserId(user.uid);

        const isOnline = await testFirestoreConnection();
        setIsCloudConnected(isOnline);

        // Fetch cloud course completion data
        const currentProgress = await fetchCourseProgress(MONGOLIAN_COURSE.id, user.uid);
        setProgress(currentProgress);

        // Fetch cloud study notes
        const notes = await fetchUserStudyNotes(user.uid);
        setStudyNotes(notes);
      } catch (err) {
        console.warn('Initialization note:', err);
      } finally {
        setIsLoading(false);
      }
    }

    setupApp();
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

  if (isLoading) {
    return (
      <div className="min-h-screen bg-stone-50 flex flex-col items-center justify-center p-6 text-center">
        <div className="w-12 h-12 rounded-full border-2 border-stone-300 border-t-stone-800 animate-spin mb-4" />
        <h2 className="font-serif text-lg font-semibold text-stone-800">
          Монгол Хэлний Цогц Хөтөлбөр
        </h2>
        <p className="text-stone-500 text-xs mt-1">
          Loading 16 Sections • 120 Units • 700 Lessons • 7,700 Interactive Exercises...
        </p>
      </div>
    );
  }

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

      {/* Subtle Academic Footer */}
      <footer className="border-t border-stone-200 bg-white py-6 text-stone-500 text-xs text-center">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div>
            <span className="font-serif font-semibold text-stone-700">Монгол Хэл</span>
            <span className="mx-2">•</span>
            <span>Comprehensive Mongolian Cyrillic Pedagogical System (A1–C2)</span>
          </div>
          <div className="font-mono text-[11px] text-stone-400">
            Deep-Focus Educational Platform • 700 Lessons • 7,700 Exercises • Zero Gamification
          </div>
        </div>
      </footer>
    </div>
  );
}
