import React from 'react';
import type { LanguageCourse, CourseCompletionStats } from '../types/curriculum';
import {
  CheckCircle2,
  Clock,
  BookOpen,
  PieChart,
  BarChart2,
  Layers,
  Award,
  Calendar,
  Sparkles,
} from 'lucide-react';

interface ProgressDashboardProps {
  course: LanguageCourse;
  progress: CourseCompletionStats;
  onNavigateToSyllabus: () => void;
}

export const ProgressDashboard: React.FC<ProgressDashboardProps> = ({
  course,
  progress,
  onNavigateToSyllabus,
}) => {
  // Aggregate statistics
  const totalLessons = course.levels.reduce(
    (acc, lvl) => acc + lvl.units.reduce((uAcc, u) => uAcc + u.lessons.length, 0),
    0
  );
  const totalUnits = course.levels.reduce((acc, lvl) => acc + lvl.units.length, 0);
  const completedLessonsCount = progress.completedLessonIds.length;
  const overallPercentage = totalLessons > 0 ? Math.round((completedLessonsCount / totalLessons) * 100) : 0;

  const totalExercisesAttempted = progress.totalExercisesAttempted;
  const totalExercisesCorrect = progress.totalExercisesCorrect;
  const retentionAccuracy =
    totalExercisesAttempted > 0
      ? Math.round((totalExercisesCorrect / totalExercisesAttempted) * 100)
      : 100;

  // Level completion breakdown
  const levelBreakdown = course.levels.map((lvl) => {
    const lvlLessons = lvl.units.flatMap((u) => u.lessons);
    const lvlTotal = lvlLessons.length;
    const lvlCompleted = lvlLessons.filter((l) => progress.completedLessonIds.includes(l.id)).length;
    const lvlPercentage = lvlTotal > 0 ? Math.round((lvlCompleted / lvlTotal) * 100) : 0;
    return {
      cefr: lvl.cefr,
      title: lvl.title,
      cyrillicTitle: lvl.cyrillicTitle,
      total: lvlTotal,
      completed: lvlCompleted,
      percentage: lvlPercentage,
    };
  });

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-8">
      {/* Dashboard Title */}
      <div className="border-b border-stone-200 pb-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-stone-100 border border-stone-200 text-stone-600 text-[11px] font-mono mb-1">
            <span>Pedagogical Registry</span>
            <span>•</span>
            <span>Cloud Synced</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900">
            Curriculum Completion Statistics
          </h1>
          <p className="text-stone-600 text-xs sm:text-sm mt-0.5">
            Objective metrics tracking your systematic mastery of the Mongolian language without gamification or artificial metrics.
          </p>
        </div>

        <button
          type="button"
          onClick={onNavigateToSyllabus}
          className="self-start sm:self-auto px-4 py-2 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs"
        >
          Open Curriculum Syllabus
        </button>
      </div>

      {/* Primary Completion Metric Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Overall Completion */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Course Completion
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {overallPercentage}%
            </span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-stone-800 h-full rounded-full transition-all duration-500"
              style={{ width: `${overallPercentage}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2">
            {completedLessonsCount} of {totalLessons} Lessons Finished
          </div>
        </div>

        {/* Exercises & Retention Rate */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Retention Accuracy
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {retentionAccuracy}%
            </span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-emerald-700 h-full rounded-full transition-all duration-500"
              style={{ width: `${retentionAccuracy}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2">
            {totalExercisesCorrect} of {totalExercisesAttempted} Correct In-Session
          </div>
        </div>

        {/* Mastered Vocabulary */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Lexicon Acquired
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {progress.masteredVocabCount}
            </span>
            <span className="text-xs text-stone-500">Cyrillic terms</span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-stone-600 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.min(100, (progress.masteredVocabCount / 60) * 100)}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2">
            Phonetically mapped words
          </div>
        </div>

        {/* Deep Focus Time */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Focus Study Log
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {progress.timeSpentMinutes}
            </span>
            <span className="text-xs text-stone-500">Minutes</span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-amber-700 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.min(100, (progress.timeSpentMinutes / 120) * 100)}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2">
            Cumulative linguistic analysis
          </div>
        </div>
      </div>

      {/* Level by Level Completion Breakdown */}
      <div className="bg-white border border-stone-200 rounded-xl p-6 shadow-2xs space-y-6">
        <div>
          <h2 className="text-base font-serif font-bold text-stone-900">
            Completion by CEFR Competency Level
          </h2>
          <p className="text-xs text-stone-500 mt-0.5">
            Progress through the standard CEFR continuum from foundational orthography to upper-division discourse.
          </p>
        </div>

        <div className="space-y-4">
          {levelBreakdown.map((lvl) => (
            <div key={lvl.cefr} className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <div className="flex items-center gap-2">
                  <span className="w-7 h-5 rounded bg-stone-100 border border-stone-300 font-mono font-bold text-stone-800 flex items-center justify-center text-[11px]">
                    {lvl.cefr}
                  </span>
                  <span className="font-serif font-medium text-stone-900">
                    {lvl.title}
                  </span>
                </div>
                <div className="font-mono text-stone-600">
                  {lvl.completed} / {lvl.total} Lessons ({lvl.percentage}%)
                </div>
              </div>

              <div className="w-full bg-stone-100 h-2 rounded-full overflow-hidden">
                <div
                  className="h-full bg-stone-800 rounded-full transition-all duration-500"
                  style={{ width: `${lvl.percentage}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Detailed Syllabus Audit Checklist */}
      <div className="bg-white border border-stone-200 rounded-xl p-6 shadow-2xs space-y-4">
        <div>
          <h2 className="text-base font-serif font-bold text-stone-900">
            Complete Syllabus Mastery Checklist
          </h2>
          <p className="text-xs text-stone-500 mt-0.5">
            Full audit trail of all course components and your recorded completion status.
          </p>
        </div>

        <div className="divide-y divide-stone-100 border-t border-stone-200">
          {course.levels.map((lvl) => (
            <div key={lvl.levelId} className="py-4 space-y-2">
              <div className="text-xs font-mono font-bold text-stone-700 uppercase">
                {lvl.cefr} — {lvl.title}
              </div>

              <div className="space-y-1.5 pl-2">
                {lvl.units.flatMap((u) => u.lessons).map((lesson) => {
                  const isDone = progress.completedLessonIds.includes(lesson.id);

                  return (
                    <div
                      key={lesson.id}
                      className="flex items-center justify-between text-xs py-1 px-2 rounded hover:bg-stone-50"
                    >
                      <div className="flex items-center gap-2">
                        {isDone ? (
                          <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                        ) : (
                          <span className="w-4 h-4 rounded-full border border-stone-300 inline-block shrink-0" />
                        )}
                        <span className={`font-medium ${isDone ? 'text-stone-900' : 'text-stone-500'}`}>
                          {lesson.title}
                        </span>
                        <span className="font-serif italic text-stone-400">
                          ({lesson.cyrillicTitle})
                        </span>
                      </div>

                      <span
                        className={`text-[11px] font-mono px-2 py-0.5 rounded ${
                          isDone
                            ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                            : 'bg-stone-100 text-stone-500'
                        }`}
                      >
                        {isDone ? 'Mastered' : 'Unstarted'}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
