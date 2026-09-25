import React, { useState, useEffect } from 'react';
import type { Lesson, Unit, LevelCurriculum, Exercise } from '../types/curriculum';
import { playMongolianAudio } from '../utils/audio';
import { normalizeEvaluationText } from '../utils/evaluationEngine';
import { CyrillicKeyboard } from './CyrillicKeyboard';
import {
  Volume2,
  ArrowLeft,
  CheckCircle2,
  AlertCircle,
  Clock,
  BookOpen,
  ChevronRight,
  RotateCcw,
  Sparkles,
  Award,
  Layers,
} from 'lucide-react';

interface LessonViewProps {
  lesson: Lesson;
  unit: Unit;
  level: LevelCurriculum;
  onBackToSyllabus: () => void;
  onCompleteLesson: (stats: {
    lessonId: string;
    unitId: string;
    exercisesAttempted: number;
    exercisesCorrect: number;
    minutesSpent: number;
    vocabMasteredCount: number;
  }) => void;
  audioSpeed: number;
}

export const LessonView: React.FC<LessonViewProps> = ({
  lesson,
  unit,
  level,
  onBackToSyllabus,
  onCompleteLesson,
  audioSpeed,
}) => {
  // Navigation states: 'orientation' (grammar intro) -> 'exercise' -> 'completed'
  const [phase, setPhase] = useState<'orientation' | 'exercise' | 'completed'>('orientation');
  const [currentExerciseIndex, setCurrentExerciseIndex] = useState(0);

  // User input states
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [selectedSuffix, setSelectedSuffix] = useState<string | null>(null);
  const [textInput, setTextInput] = useState('');
  const [builtSentenceTokens, setBuiltSentenceTokens] = useState<string[]>([]);
  const [availableSentenceTokens, setAvailableSentenceTokens] = useState<string[]>([]);

  // Submission & evaluation states
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false);
  const [isCurrentAnswerCorrect, setIsCurrentAnswerCorrect] = useState(false);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);

  // Session stats (no gamification, pure learning metrics)
  const [correctCount, setCorrectCount] = useState(0);
  const [attemptCount, setAttemptCount] = useState(0);
  const [sessionStartTime] = useState<number>(Date.now());

  const currentExercise = lesson.exercises[currentExerciseIndex] as Exercise | undefined;

  // Prepare exercise state whenever exercise changes
  useEffect(() => {
    if (!currentExercise) return;

    setSelectedOptionId(null);
    setSelectedSuffix(null);
    setTextInput('');
    setIsAnswerSubmitted(false);
    setIsCurrentAnswerCorrect(false);

    if (currentExercise.type === 'SENTENCE_CONSTRUCTION' && currentExercise.wordTokens) {
      // Shuffle tokens for sentence builder
      const shuffled = [...currentExercise.wordTokens].sort(() => Math.random() - 0.5);
      setAvailableSentenceTokens(shuffled);
      setBuiltSentenceTokens([]);
    }

    // Auto-play audio for audio exercises if desired
    if (
      (currentExercise.type === 'AUDIO_DICTATION' || currentExercise.type === 'AUDIO_COMPREHENSION') &&
      currentExercise.audioText
    ) {
      playMongolianAudio(
        currentExercise.audioText,
        audioSpeed,
        () => setIsPlayingAudio(true),
        () => setIsPlayingAudio(false)
      );
    }
  }, [currentExerciseIndex, phase, audioSpeed]);

  const handlePlayAudio = (text: string, customSpeed?: number) => {
    playMongolianAudio(
      text,
      customSpeed ?? audioSpeed,
      () => setIsPlayingAudio(true),
      () => setIsPlayingAudio(false)
    );
  };

  const handleInsertCyrillicChar = (char: string) => {
    setTextInput((prev) => prev + char);
  };

  const handleBackspaceCyrillicChar = () => {
    setTextInput((prev) => prev.slice(0, -1));
  };

  const handleSelectToken = (token: string, index: number) => {
    if (isAnswerSubmitted) return;
    setBuiltSentenceTokens((prev) => [...prev, token]);
    setAvailableSentenceTokens((prev) => prev.filter((_, i) => i !== index));
  };

  const handleRemoveToken = (token: string, index: number) => {
    if (isAnswerSubmitted) return;
    setAvailableSentenceTokens((prev) => [...prev, token]);
    setBuiltSentenceTokens((prev) => prev.filter((_, i) => i !== index));
  };

  const handleCheckAnswer = () => {
    if (!currentExercise || isAnswerSubmitted) return;

    let correct = false;

    switch (currentExercise.type) {
      case 'AUDIO_DICTATION': {
        const cleanUser = normalizeEvaluationText(textInput, { stripPunctuation: true, caseSensitive: false });
        const cleanExpected = normalizeEvaluationText(currentExercise.correctAnswer || '', { stripPunctuation: true, caseSensitive: false });
        correct = cleanUser === cleanExpected;
        break;
      }
      case 'AUDIO_COMPREHENSION':
      case 'PHONETIC_DISCRIMINATION':
      case 'VOCABULARY_MATCH':
      case 'TRANSLATION': {
        const chosen = currentExercise.options?.find((o) => o.id === selectedOptionId);
        correct = !!chosen?.isCorrect;
        break;
      }
      case 'SENTENCE_CONSTRUCTION': {
        const cleanUserTokens = builtSentenceTokens.map((t) =>
          normalizeEvaluationText(t, { stripPunctuation: true, caseSensitive: false })
        );
        const cleanExpectedTokens = (currentExercise.correctTokenOrder || []).map((t) =>
          normalizeEvaluationText(t, { stripPunctuation: true, caseSensitive: false })
        );
        correct =
          cleanUserTokens.length === cleanExpectedTokens.length &&
          cleanUserTokens.every((t, i) => t === cleanExpectedTokens[i]);
        break;
      }
      case 'GRAMMAR_APPLICATION': {
        correct = selectedSuffix === currentExercise.correctSuffix;
        break;
      }
    }

    setIsAnswerSubmitted(true);
    setIsCurrentAnswerCorrect(correct);
    setAttemptCount((prev) => prev + 1);
    if (correct) {
      setCorrectCount((prev) => prev + 1);
    }
  };

  const handleNextExercise = () => {
    if (currentExerciseIndex < lesson.exercises.length - 1) {
      setCurrentExerciseIndex((prev) => prev + 1);
    } else {
      // Completed all exercises in this lesson
      const elapsedMinutes = Math.max(1, Math.round((Date.now() - sessionStartTime) / 60000));
      setPhase('completed');
      onCompleteLesson({
        lessonId: lesson.id,
        unitId: unit.id,
        exercisesAttempted: attemptCount + 1,
        exercisesCorrect: correctCount + (isCurrentAnswerCorrect ? 1 : 0),
        minutesSpent: elapsedMinutes,
        vocabMasteredCount: lesson.vocabulary.length,
      });
    }
  };

  // Phase 1: Linguistic Orientation & Grammar Foundation
  if (phase === 'orientation') {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
        {/* Header Breadcrumb */}
        <button
          type="button"
          onClick={onBackToSyllabus}
          className="inline-flex items-center gap-1.5 text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors mb-6"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Return to Curriculum Syllabus</span>
        </button>

        <div className="bg-white border border-stone-200 rounded-xl p-6 sm:p-8 shadow-xs space-y-8">
          {/* Title and metadata */}
          <div className="border-b border-stone-100 pb-6">
            <div className="flex items-center gap-2 text-xs font-mono text-stone-500 mb-1.5">
              <span>{level.title}</span>
              <span>•</span>
              <span>Unit {unit.unitNumber}</span>
              <span>•</span>
              <span className="flex items-center gap-1">
                <Clock className="w-3 h-3" /> ~{lesson.estimatedMinutes} min study
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900">
              {lesson.title}
            </h1>
            <p className="font-serif italic text-stone-600 mt-1 text-lg">
              {lesson.cyrillicTitle}
            </p>
          </div>

          {/* Grammar Overview */}
          <div className="space-y-4">
            <h2 className="text-sm font-semibold uppercase tracking-wider text-stone-500 flex items-center gap-1.5">
              <BookOpen className="w-4 h-4 text-stone-700" />
              <span>Linguistic Explanation & Grammar Rules</span>
            </h2>
            <div className="bg-stone-50 border border-stone-200 rounded-lg p-5 text-sm leading-relaxed text-stone-800 space-y-3">
              <p className="font-medium text-stone-900">
                {lesson.grammarOverview.summary}
              </p>
              <ul className="space-y-2 pt-1 border-t border-stone-200/80">
                {lesson.grammarOverview.keyPoints.map((point, idx) => (
                  <li key={idx} className="flex items-start gap-2 text-stone-700">
                    <span className="text-amber-700 font-bold text-xs mt-0.5">•</span>
                    <span>{point}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Core Vocabulary Reference with Audio */}
          {lesson.vocabulary.length > 0 && (
            <div className="space-y-4">
              <h2 className="text-sm font-semibold uppercase tracking-wider text-stone-500">
                Lesson Vocabulary ({lesson.vocabulary.length} Terms)
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {lesson.vocabulary.map((voc) => (
                  <div
                    key={voc.id}
                    className="border border-stone-200 bg-stone-50/50 rounded-lg p-3.5 flex flex-col justify-between"
                  >
                    <div>
                      <div className="flex items-center justify-between">
                        <span className="text-lg font-serif font-bold text-stone-900">
                          {voc.cyrillic}
                        </span>
                        <div className="flex items-center gap-1">
                          <span className="text-[10px] font-mono text-stone-500 px-1.5 py-0.5 bg-stone-200 rounded">
                            {voc.genderHarmony}
                          </span>
                          <button
                            type="button"
                            onClick={() => handlePlayAudio(voc.cyrillic)}
                            className="p-1.5 rounded-md hover:bg-stone-200 text-stone-700 transition-colors"
                            title="Pronounce Cyrillic word"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>
                      </div>
                      <div className="text-xs font-mono text-stone-500 mt-0.5">
                        {voc.ipa}
                      </div>
                      <div className="text-sm font-medium text-stone-800 mt-1">
                        {voc.english}
                      </div>
                    </div>
                    <div className="mt-2.5 pt-2 border-t border-stone-200/60 text-xs text-stone-600">
                      <div className="font-serif font-medium text-stone-800">
                        {voc.exampleSentenceCyrillic}
                      </div>
                      <div className="text-stone-500 italic mt-0.5">
                        {voc.exampleSentenceEnglish}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Proceed Button */}
          <div className="pt-4 border-t border-stone-100 flex justify-end">
            <button
              type="button"
              onClick={() => setPhase('exercise')}
              className="inline-flex items-center gap-2 px-6 py-2.5 rounded-md bg-stone-900 hover:bg-stone-800 text-stone-100 text-sm font-medium transition-colors shadow-sm"
            >
              <span>Begin Interactive Exercises</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Phase 3: Lesson Mastery & Summary
  if (phase === 'completed') {
    const accuracy = attemptCount > 0 ? Math.round((correctCount / attemptCount) * 100) : 100;

    return (
      <div className="max-w-2xl mx-auto px-4 py-12">
        <div className="bg-white border border-stone-200 rounded-xl p-8 text-center shadow-sm space-y-6">
          <div className="w-16 h-16 bg-stone-100 text-stone-800 rounded-full flex items-center justify-center mx-auto border border-stone-300">
            <Award className="w-8 h-8 text-stone-700" />
          </div>

          <div className="space-y-1">
            <span className="text-xs font-mono uppercase tracking-wider text-stone-500 font-semibold">
              Curriculum Unit {unit.unitNumber}
            </span>
            <h2 className="text-2xl font-serif font-bold text-stone-900">
              Lesson Completed
            </h2>
            <p className="text-stone-600 text-sm max-w-md mx-auto">
              You have systematically reviewed and completed all grammatical exercises for{' '}
              <span className="font-serif font-semibold">{lesson.title}</span>.
            </p>
          </div>

          {/* Pure Completion Statistics (Zero Gamification) */}
          <div className="grid grid-cols-3 gap-3 bg-stone-50 border border-stone-200 rounded-lg p-4 text-left">
            <div>
              <div className="text-[11px] text-stone-500 uppercase font-medium">Accuracy</div>
              <div className="text-xl font-bold font-mono text-stone-900">{accuracy}%</div>
              <div className="text-[11px] text-stone-500">First-attempt mastery</div>
            </div>
            <div>
              <div className="text-[11px] text-stone-500 uppercase font-medium">Exercises</div>
              <div className="text-xl font-bold font-mono text-stone-900">
                {lesson.exercises.length} / {lesson.exercises.length}
              </div>
              <div className="text-[11px] text-stone-500">All completed</div>
            </div>
            <div>
              <div className="text-[11px] text-stone-500 uppercase font-medium">Terms Acquired</div>
              <div className="text-xl font-bold font-mono text-stone-900">
                {lesson.vocabulary.length}
              </div>
              <div className="text-[11px] text-stone-500">Added to lexicon</div>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-4 border-t border-stone-100">
            <button
              type="button"
              onClick={() => {
                setCurrentExerciseIndex(0);
                setCorrectCount(0);
                setAttemptCount(0);
                setPhase('orientation');
              }}
              className="w-full sm:w-auto px-4 py-2 border border-stone-300 rounded-md text-stone-700 hover:bg-stone-50 text-xs font-medium"
            >
              Review Orientation & Re-attempt
            </button>
            <button
              type="button"
              onClick={onBackToSyllabus}
              className="w-full sm:w-auto px-6 py-2 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium shadow-xs"
            >
              Return to Curriculum Syllabus
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Phase 2: Active Interactive Exercise
  if (!currentExercise) {
    return null;
  }

  const isCheckDisabled =
    (currentExercise.type === 'AUDIO_DICTATION' && textInput.trim().length === 0) ||
    ((currentExercise.type === 'AUDIO_COMPREHENSION' ||
      currentExercise.type === 'PHONETIC_DISCRIMINATION' ||
      currentExercise.type === 'VOCABULARY_MATCH' ||
      currentExercise.type === 'TRANSLATION') &&
      !selectedOptionId) ||
    (currentExercise.type === 'SENTENCE_CONSTRUCTION' && builtSentenceTokens.length === 0) ||
    (currentExercise.type === 'GRAMMAR_APPLICATION' && !selectedSuffix);

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-6 space-y-6">
      {/* Top Exercise Header & Progress Indicator */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => setPhase('orientation')}
          className="text-xs font-medium text-stone-500 hover:text-stone-800 flex items-center gap-1"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Lesson Overview</span>
        </button>

        {/* Academic Progress Meter */}
        <div className="flex items-center gap-2">
          <span className="text-xs font-mono font-medium text-stone-600">
            Exercise {currentExerciseIndex + 1} of {lesson.exercises.length}
          </span>
          <div className="w-32 h-2 bg-stone-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-stone-800 transition-all duration-300"
              style={{
                width: `${((currentExerciseIndex + 1) / lesson.exercises.length) * 100}%`,
              }}
            />
          </div>
        </div>
      </div>

      {/* Main Exercise Card */}
      <div className="bg-white border border-stone-200 rounded-xl p-6 sm:p-8 shadow-xs space-y-6">
        {/* Exercise Prompt */}
        <div className="space-y-1">
          <div className="text-[11px] font-mono uppercase tracking-wider text-stone-500 font-semibold">
            {currentExercise.type.replace('_', ' ')}
          </div>
          <h2 className="text-lg sm:text-xl font-serif font-bold text-stone-900">
            {currentExercise.prompt}
          </h2>
        </div>

        {/* Audio Player Component for Audio-Enabled Exercises */}
        {currentExercise.audioText && (
          <div className="p-4 rounded-lg bg-stone-50 border border-stone-200 flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => handlePlayAudio(currentExercise.audioText!)}
                disabled={isPlayingAudio}
                className="inline-flex items-center gap-2 px-3.5 py-2 rounded-md bg-stone-900 hover:bg-stone-800 text-stone-100 text-xs font-medium transition-colors active:scale-95 shadow-xs"
              >
                <Volume2 className="w-4 h-4" />
                <span>{isPlayingAudio ? 'Speaking...' : 'Listen Audio (1.0x)'}</span>
              </button>

              <button
                type="button"
                onClick={() => handlePlayAudio(currentExercise.audioText!, 0.75)}
                disabled={isPlayingAudio}
                className="inline-flex items-center gap-1.5 px-3 py-2 rounded-md bg-stone-200 hover:bg-stone-300 text-stone-700 text-xs font-mono font-medium transition-colors"
                title="Deliberate 0.75x slow articulation"
              >
                <span>Slow (0.75x)</span>
              </button>
            </div>

            <span className="text-xs text-stone-500 italic">
              Authentic Mongolian phonetics
            </span>
          </div>
        )}

        {/* Dynamic Exercise Body based on type */}

        {/* 1. Audio Dictation with Cyrillic Assistant Keyboard */}
        {currentExercise.type === 'AUDIO_DICTATION' && (
          <div className="space-y-4">
            <div>
              <label htmlFor="dictation-input" className="block text-xs font-medium text-stone-600 mb-1.5">
                Type the Cyrillic word or phrase you hear:
              </label>
              <input
                id="dictation-input"
                type="text"
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
                disabled={isAnswerSubmitted}
                placeholder="Бичих..."
                className="w-full text-lg font-serif px-4 py-3 rounded-lg border border-stone-300 focus:outline-hidden focus:ring-2 focus:ring-stone-800 bg-white"
                autoComplete="off"
                autoCapitalize="off"
              />
            </div>

            {!isAnswerSubmitted && (
              <CyrillicKeyboard
                onInsertChar={handleInsertCyrillicChar}
                onBackspace={handleBackspaceCyrillicChar}
              />
            )}
          </div>
        )}

        {/* 2. Multiple Choice / Comprehension / Phonetic / Matching */}
        {(currentExercise.type === 'AUDIO_COMPREHENSION' ||
          currentExercise.type === 'PHONETIC_DISCRIMINATION' ||
          currentExercise.type === 'VOCABULARY_MATCH' ||
          currentExercise.type === 'TRANSLATION') &&
          currentExercise.options && (
            <div className="space-y-2.5">
              {currentExercise.cyrillicSentence && (
                <div className="text-xl font-serif font-bold text-stone-900 bg-stone-50 p-4 rounded-lg border border-stone-200 text-center">
                  {currentExercise.cyrillicSentence}
                </div>
              )}
              <div className="grid grid-cols-1 gap-2.5">
                {currentExercise.options.map((opt) => {
                  const isSelected = selectedOptionId === opt.id;
                  let cardStyle = 'border-stone-200 bg-white hover:bg-stone-50 text-stone-800';

                  if (isAnswerSubmitted) {
                    if (opt.isCorrect) {
                      cardStyle = 'border-emerald-500 bg-emerald-50/70 text-emerald-950 font-medium';
                    } else if (isSelected && !opt.isCorrect) {
                      cardStyle = 'border-red-400 bg-red-50/70 text-red-950';
                    } else {
                      cardStyle = 'border-stone-200 bg-stone-50/50 text-stone-400 opacity-60';
                    }
                  } else if (isSelected) {
                    cardStyle = 'border-stone-900 bg-stone-100/90 text-stone-900 ring-1 ring-stone-900';
                  }

                  return (
                    <button
                      key={opt.id}
                      type="button"
                      disabled={isAnswerSubmitted}
                      onClick={() => setSelectedOptionId(opt.id)}
                      className={`p-4 rounded-lg border text-left transition-all flex items-center justify-between ${cardStyle}`}
                    >
                      <span className="text-sm">{opt.text}</span>
                      {opt.cyrillic && (
                        <span className="font-serif font-semibold text-stone-900 ml-2">
                          {opt.cyrillic}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            </div>
          )}

        {/* 3. Sentence Construction (SOV Word Order Assembly) */}
        {currentExercise.type === 'SENTENCE_CONSTRUCTION' && (
          <div className="space-y-5">
            {/* Answer builder staging area */}
            <div>
              <div className="text-xs font-medium text-stone-500 mb-2">
                Assembled Mongolian Clause (SOV Order):
              </div>
              <div className="min-h-[58px] p-3 rounded-lg border-2 border-dashed border-stone-300 bg-stone-50/70 flex flex-wrap items-center gap-2">
                {builtSentenceTokens.length === 0 ? (
                  <span className="text-xs text-stone-400 italic">
                    Click word tiles below in grammatical order...
                  </span>
                ) : (
                  builtSentenceTokens.map((token, idx) => (
                    <button
                      key={`${token}-${idx}`}
                      type="button"
                      disabled={isAnswerSubmitted}
                      onClick={() => handleRemoveToken(token, idx)}
                      className="px-3 py-1.5 rounded-md bg-stone-900 text-stone-100 font-serif text-sm font-medium hover:bg-stone-700 transition-colors"
                      title="Click to remove token"
                    >
                      {token}
                    </button>
                  ))
                )}
              </div>
            </div>

            {/* Available tokens */}
            <div>
              <div className="text-xs font-medium text-stone-500 mb-2">
                Available Word Tokens:
              </div>
              <div className="flex flex-wrap gap-2 min-h-[44px]">
                {availableSentenceTokens.map((token, idx) => (
                  <button
                    key={`${token}-${idx}`}
                    type="button"
                    disabled={isAnswerSubmitted}
                    onClick={() => handleSelectToken(token, idx)}
                    className="px-3.5 py-1.5 rounded-md border border-stone-300 bg-white hover:bg-stone-100 text-stone-900 font-serif text-sm font-medium transition-transform active:scale-95 shadow-2xs"
                  >
                    {token}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* 4. Grammar Suffix Application */}
        {currentExercise.type === 'GRAMMAR_APPLICATION' && (
          <div className="space-y-4">
            <div className="p-4 rounded-lg bg-stone-50 border border-stone-200 text-center">
              <span className="text-xs text-stone-500 uppercase font-mono block mb-1">Root Stem</span>
              <span className="text-2xl font-serif font-bold text-stone-900">
                {currentExercise.baseWord}
              </span>
              <span className="text-stone-400 mx-2 text-xl">+</span>
              <span className="text-2xl font-serif font-bold text-amber-800 underline decoration-dashed">
                {selectedSuffix || '[ ? ]'}
              </span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
              {currentExercise.suffixOptions?.map((suffix) => {
                const isSelected = selectedSuffix === suffix;
                let btnStyle = 'border-stone-200 bg-white hover:bg-stone-50 text-stone-800';

                if (isAnswerSubmitted) {
                  if (suffix === currentExercise.correctSuffix) {
                    btnStyle = 'border-emerald-500 bg-emerald-50 text-emerald-950 font-bold';
                  } else if (isSelected && suffix !== currentExercise.correctSuffix) {
                    btnStyle = 'border-red-400 bg-red-50 text-red-950';
                  } else {
                    btnStyle = 'border-stone-200 bg-stone-50 opacity-60 text-stone-400';
                  }
                } else if (isSelected) {
                  btnStyle = 'border-stone-900 bg-stone-100 ring-1 ring-stone-900 font-bold';
                }

                return (
                  <button
                    key={suffix}
                    type="button"
                    disabled={isAnswerSubmitted}
                    onClick={() => setSelectedSuffix(suffix)}
                    className={`py-3 px-2 rounded-lg border font-serif text-base text-center transition-all ${btnStyle}`}
                  >
                    {suffix}
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Feedback Rationale Box (Visible After Submission) */}
        {isAnswerSubmitted && (
          <div
            className={`p-4 rounded-lg border text-sm leading-relaxed ${
              isCurrentAnswerCorrect
                ? 'bg-emerald-50/70 border-emerald-300 text-emerald-950'
                : 'bg-amber-50/70 border-amber-300 text-amber-950'
            }`}
          >
            <div className="flex items-center gap-2 font-semibold text-xs uppercase tracking-wider mb-1.5">
              {isCurrentAnswerCorrect ? (
                <>
                  <CheckCircle2 className="w-4 h-4 text-emerald-700" />
                  <span>Correct — Linguistic Mastery</span>
                </>
              ) : (
                <>
                  <AlertCircle className="w-4 h-4 text-amber-800" />
                  <span>Pedagogical Analysis & Correction</span>
                </>
              )}
            </div>

            <p className="text-stone-800 text-xs sm:text-sm">
              {currentExercise.detailedGrammarNote}
            </p>

            {!isCurrentAnswerCorrect && currentExercise.correctAnswer && (
              <div className="mt-2 pt-2 border-t border-amber-200/80 text-xs font-mono text-stone-800">
                Correct Cyrillic: <span className="font-bold">{currentExercise.correctAnswer}</span>
              </div>
            )}
          </div>
        )}

        {/* Action Controls */}
        <div className="pt-4 border-t border-stone-100 flex items-center justify-between">
          <button
            type="button"
            onClick={() => setPhase('orientation')}
            className="text-xs text-stone-500 hover:text-stone-800 font-medium underline underline-offset-4"
          >
            Review Grammar Notes
          </button>

          <div>
            {!isAnswerSubmitted ? (
              <button
                type="button"
                disabled={isCheckDisabled}
                onClick={handleCheckAnswer}
                className="px-6 py-2.5 rounded-md bg-stone-900 hover:bg-stone-800 disabled:opacity-40 disabled:hover:bg-stone-900 text-stone-100 text-xs font-medium transition-colors shadow-xs"
              >
                Check Answer
              </button>
            ) : (
              <button
                type="button"
                onClick={handleNextExercise}
                className="inline-flex items-center gap-1.5 px-6 py-2.5 rounded-md bg-stone-900 hover:bg-stone-800 text-stone-100 text-xs font-medium transition-colors shadow-xs"
              >
                <span>
                  {currentExerciseIndex < lesson.exercises.length - 1
                    ? 'Continue to Next Exercise'
                    : 'Complete Lesson'}
                </span>
                <ChevronRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
