import React from 'react';
import type { LanguageCourse, LevelCurriculum, Unit, Lesson, CourseCompletionStats, CEFRLevel } from '../types/curriculum';
import { CheckCircle2, Clock, BookOpen, ChevronRight, Play, Award, Sparkles, Filter } from 'lucide-react';

interface SyllabusViewProps {
  course: LanguageCourse;
  progress: CourseCompletionStats;
  onSelectLesson: (lesson: Lesson, unit: Unit, level: LevelCurriculum) => void;
  onOpenGrammarLibrary: () => void;
}

export const SyllabusView: React.FC<SyllabusViewProps> = ({
  course,
  progress,
  onSelectLesson,
  onOpenGrammarLibrary,
}) => {
  const [selectedCefr, setSelectedCefr] = React.useState<CEFRLevel | 'ALL'>('ALL');

  const filteredLevels = selectedCefr === 'ALL'
    ? course.levels
    : course.levels.filter((lvl) => lvl.cefr === selectedCefr);

  const totalLessons = course.levels.reduce(
    (acc, lvl) => acc + lvl.units.reduce((uAcc, u) => uAcc + u.lessons.length, 0),
    0
  );
  const completedCount = progress.completedLessonIds.length;
  const overallPct = totalLessons > 0 ? Math.round((completedCount / totalLessons) * 100) : 0;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      {/* Course Header Banner */}
      <div className="bg-white border border-stone-200 rounded-xl p-6 sm:p-8 shadow-xs mb-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center gap-2 px-2.5 py-1 rounded bg-stone-100 border border-stone-200 text-stone-700 text-xs font-mono">
              <span>{course.script}</span>
              <span>•</span>
              <span>CEFR {course.cefrRange}</span>
              <span>•</span>
              <span>Head-Final SOV Syntax</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900 tracking-tight">
              {course.cyrillicName}
            </h1>
            <p className="text-stone-600 text-sm sm:text-base max-w-2xl leading-relaxed">
              {course.description}
            </p>
          </div>

          {/* Academic Completion Dial */}
          <div className="flex items-center gap-4 bg-stone-50 border border-stone-200 rounded-lg p-4 shrink-0">
            <div className="w-16 h-16 rounded-full border-4 border-stone-200 flex items-center justify-center relative">
              <span className="font-mono text-base font-bold text-stone-900">{overallPct}%</span>
            </div>
            <div className="text-xs space-y-1">
              <div className="font-semibold text-stone-800 uppercase tracking-wider text-[10px]">
                Curriculum Mastery
              </div>
              <div className="text-stone-600 font-medium">
                {completedCount} of {totalLessons} Lessons Completed
              </div>
              <div className="text-stone-500 text-[11px]">
                {progress.timeSpentMinutes} Focus Minutes Logged
              </div>
            </div>
          </div>
        </div>

        {/* Level Filters */}
        <div className="mt-6 pt-5 border-t border-stone-100 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-1.5 flex-wrap">
            <span className="text-xs text-stone-500 font-medium mr-1 flex items-center gap-1">
              <Filter className="w-3.5 h-3.5" /> Filter Level:
            </span>
            {(['ALL', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2'] as const).map((level) => (
              <button
                key={level}
                type="button"
                onClick={() => setSelectedCefr(level)}
                className={`px-2.5 py-1 text-xs font-medium rounded transition-colors ${
                  selectedCefr === level
                    ? 'bg-stone-900 text-stone-100'
                    : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
                }`}
              >
                {level === 'ALL' ? 'Complete Course' : level}
              </button>
            ))}

          </div>

          <button
            type="button"
            onClick={onOpenGrammarLibrary}
            className="text-xs text-stone-700 hover:text-stone-950 font-medium underline underline-offset-4 flex items-center gap-1"
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>View 7 Grammatical Cases & Vowel Harmony Reference</span>
          </button>
        </div>
      </div>

      {/* Levels Curriculum Stack */}
      <div className="space-y-8">
        {filteredLevels.map((lvl) => (
          <section key={lvl.levelId} className="space-y-4">
            <div className="flex items-center justify-between border-b border-stone-200 pb-2.5">
              <div>
                <div className="flex items-center gap-2">
                  <span className="px-2 py-0.5 rounded text-[11px] font-mono font-bold bg-stone-200 text-stone-800">
                    {lvl.cefr}
                  </span>
                  <h2 className="text-lg sm:text-xl font-serif font-bold text-stone-900">
                    {lvl.title}
                  </h2>
                </div>
                <p className="text-xs text-stone-600 mt-0.5">
                  <span className="font-medium text-stone-700 font-serif mr-1">{lvl.cyrillicTitle}</span> — {lvl.targetCompetency}
                </p>
              </div>
            </div>

            {/* Units list */}
            <div className="space-y-4">
              {lvl.units.map((unit) => (
                <div
                  key={unit.id}
                  className="bg-white border border-stone-200 rounded-xl overflow-hidden shadow-2xs hover:border-stone-300 transition-colors"
                >
                  <div className="p-4 sm:p-5 bg-stone-50/70 border-b border-stone-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-mono font-semibold text-stone-500 uppercase">
                          Unit {unit.unitNumber}
                        </span>
                        <span className="text-stone-300">•</span>
                        <h3 className="font-serif font-semibold text-stone-900 text-base">
                          {unit.title}
                        </h3>
                      </div>
                      <p className="text-xs text-stone-600 mt-1">
                        {unit.description}
                      </p>
                    </div>
                    <div className="inline-flex items-center px-2.5 py-1 rounded bg-stone-200/70 text-stone-700 text-xs font-medium shrink-0 self-start sm:self-auto">
                      Topic: {unit.primaryGrammarTopic}
                    </div>
                  </div>

                  {/* Lessons list inside unit */}
                  <div className="divide-y divide-stone-100">
                    {unit.lessons.map((lesson) => {
                      const isCompleted = progress.completedLessonIds.includes(lesson.id);

                      return (
                        <div
                          key={lesson.id}
                          className="p-4 sm:px-6 hover:bg-stone-50/80 transition-colors flex flex-col sm:flex-row sm:items-center justify-between gap-4"
                        >
                          <div className="space-y-1.5 flex-1">
                            <div className="flex items-center gap-2.5 flex-wrap">
                              {isCompleted ? (
                                <span className="inline-flex items-center gap-1 text-emerald-700 text-xs font-medium">
                                  <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                                  <span>Mastered</span>
                                </span>
                              ) : (
                                <span className="inline-flex items-center gap-1 text-stone-500 text-xs font-medium">
                                  <span className="w-3.5 h-3.5 rounded-full border-2 border-stone-300 inline-block"></span>
                                  <span>Pending</span>
                                </span>
                              )}
                              <h4 className="font-serif font-medium text-stone-900 text-base">
                                {lesson.title}
                              </h4>
                              <span className="text-stone-500 text-xs font-serif italic">
                                ({lesson.cyrillicTitle})
                              </span>
                            </div>

                            <p className="text-xs text-stone-600 line-clamp-1 leading-relaxed">
                              {lesson.grammarOverview.summary}
                            </p>

                            <div className="flex items-center gap-3 text-[11px] text-stone-500 pt-0.5">
                              <span className="flex items-center gap-1">
                                <Clock className="w-3 h-3 text-stone-400" />
                                <span>~{lesson.estimatedMinutes} min deep study</span>
                              </span>
                              <span>•</span>
                              <span>{lesson.vocabulary.length} terms</span>
                              <span>•</span>
                              <span>{lesson.exercises.length} interactive exercises</span>
                            </div>
                          </div>

                          <button
                            type="button"
                            onClick={() => onSelectLesson(lesson, unit, lvl)}
                            className={`inline-flex items-center justify-center gap-1.5 px-4 py-2 text-xs font-medium rounded-md transition-all shrink-0 ${
                              isCompleted
                                ? 'bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-300'
                                : 'bg-stone-900 hover:bg-stone-800 text-stone-100 shadow-xs'
                            }`}
                          >
                            <Play className="w-3.5 h-3.5" />
                            <span>{isCompleted ? 'Review Lesson' : 'Begin Lesson'}</span>
                          </button>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
};
