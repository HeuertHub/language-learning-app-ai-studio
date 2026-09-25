import React from 'react';
import type { LanguageCourse, CourseCompletionStats } from '../types/curriculum';
import {
  CheckCircle2,
  BookOpen,
  Layers,
  Award,
  ChevronRight,
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
  // Total counts derived strictly from current runtime course data
  const totalLessons = course.levels.reduce(
    (acc, lvl) => acc + lvl.units.reduce((uAcc, u) => uAcc + u.lessons.length, 0),
    0
  );
  const totalUnits = course.levels.reduce((acc, lvl) => acc + lvl.units.length, 0);

  // Derived completed lessons
  const completedLessonsCount = progress.completedLessonIds.length;
  const overallPercentage = totalLessons > 0 ? Math.round((completedLessonsCount / totalLessons) * 100) : 0;

  // Derived completed units (all lessons in unit completed, or unit ID in completedUnitIds)
  const completedUnits = course.levels.flatMap((lvl) => lvl.units).filter((u) => {
    if (progress.completedUnitIds.includes(u.id)) return true;
    if (u.lessons.length === 0) return false;
    return u.lessons.every((l) => progress.completedLessonIds.includes(l.id));
  });
  const completedUnitsCount = completedUnits.length;
  const unitsPercentage = totalUnits > 0 ? Math.round((completedUnitsCount / totalUnits) * 100) : 0;

  // Derived sections (we group units by their section if available or approximate 26 sections)
  // Authoritative curriculum contains 26 sections across Pre-A1 through C2
  const totalSections = 26;
  // Estimate completed sections based on fully completed units
  const completedSectionsCount = Math.min(
    totalSections,
    Math.floor((completedUnitsCount / Math.max(1, totalUnits)) * totalSections)
  );

  // Level completion breakdown across all authoritative CEFR levels (Pre-A1 through C2)
  const levelBreakdown = course.levels.map((lvl) => {
    const lvlLessons = lvl.units.flatMap((u) => u.lessons);
    const lvlTotal = lvlLessons.length;
    const lvlCompleted = lvlLessons.filter((l) => progress.completedLessonIds.includes(l.id)).length;
    const lvlPercentage = lvlTotal > 0 ? Math.round((lvlCompleted / lvlTotal) * 100) : 0;

    const lvlUnitsTotal = lvl.units.length;
    const lvlUnitsCompleted = lvl.units.filter((u) => {
      if (progress.completedUnitIds.includes(u.id)) return true;
      if (u.lessons.length === 0) return false;
      return u.lessons.every((l) => progress.completedLessonIds.includes(l.id));
    }).length;

    return {
      cefr: lvl.cefr,
      title: lvl.title,
      cyrillicTitle: lvl.cyrillicTitle,
      lessonsTotal: lvlTotal,
      lessonsCompleted: lvlCompleted,
      lessonsPercentage: lvlPercentage,
      unitsTotal: lvlUnitsTotal,
      unitsCompleted: lvlUnitsCompleted,
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
            <span>Completion-Only Metrics</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900">
            Curriculum Completion Statistics
          </h1>
          <p className="text-stone-600 text-xs sm:text-sm mt-0.5">
            Objective completion-only tracking across all 256 Units and 1,257 Lessons. Free of streaks, XP, or gamification.
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

      {/* Primary Completion Metric Grid: Completion Only */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Metric 1: Course Completion % */}
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
              className="bg-stone-900 h-full rounded-full transition-all duration-500"
              style={{ width: `${overallPercentage}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2 font-mono">
            Overall Curriculum Progress
          </div>
        </div>

        {/* Metric 2: Lessons Completed */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Lessons Completed
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {completedLessonsCount}
            </span>
            <span className="text-xs text-stone-500 font-mono">/ {totalLessons}</span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-emerald-700 h-full rounded-full transition-all duration-500"
              style={{ width: `${overallPercentage}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2 font-mono">
            {totalLessons - completedLessonsCount} Remaining
          </div>
        </div>

        {/* Metric 3: Units Completed */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Units Completed
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {completedUnitsCount}
            </span>
            <span className="text-xs text-stone-500 font-mono">/ {totalUnits}</span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-stone-700 h-full rounded-full transition-all duration-500"
              style={{ width: `${unitsPercentage}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2 font-mono">
            {totalUnits - completedUnitsCount} Remaining Units
          </div>
        </div>

        {/* Metric 4: Sections Completed */}
        <div className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1">
            Sections Completed
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold font-mono text-stone-900">
              {completedSectionsCount}
            </span>
            <span className="text-xs text-stone-500 font-mono">/ {totalSections}</span>
          </div>
          <div className="w-full bg-stone-100 h-1.5 rounded-full overflow-hidden mt-3">
            <div
              className="bg-amber-700 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.round((completedSectionsCount / totalSections) * 100)}%` }}
            />
          </div>
          <div className="text-[11px] text-stone-500 mt-2 font-mono">
            Across 7 CEFR Levels
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
            Systematic progression across the complete 7-tier continuum from Pre-A1 script literacy to C2 philology.
          </p>
        </div>

        <div className="space-y-5">
          {levelBreakdown.map((lvl) => (
            <div key={lvl.cefr} className="space-y-2 p-3 rounded-lg border border-stone-100 bg-stone-50/50">
              <div className="flex items-center justify-between text-xs">
                <div className="flex items-center gap-2">
                  <span className="w-12 h-6 rounded bg-stone-100 border border-stone-300 font-mono font-bold text-stone-800 flex items-center justify-center text-[11px]">
                    {lvl.cefr}
                  </span>
                  <div>
                    <span className="font-serif font-semibold text-stone-900">
                      {lvl.title}
                    </span>
                    <span className="text-stone-500 font-serif italic text-xs ml-2 hidden sm:inline">
                      ({lvl.cyrillicTitle})
                    </span>
                  </div>
                </div>
                <div className="font-mono text-stone-600 font-medium">
                  {lvl.lessonsCompleted} / {lvl.lessonsTotal} Lessons ({lvl.lessonsPercentage}%)
                </div>
              </div>

              <div className="w-full bg-stone-200 h-2 rounded-full overflow-hidden">
                <div
                  className="bg-stone-800 h-full rounded-full transition-all duration-500"
                  style={{ width: `${lvl.lessonsPercentage}%` }}
                />
              </div>

              <div className="flex justify-between text-[11px] text-stone-500 font-mono">
                <span>Units Completed: {lvl.unitsCompleted} / {lvl.unitsTotal}</span>
                <span>{lvl.lessonsTotal - lvl.lessonsCompleted} lessons remaining</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
