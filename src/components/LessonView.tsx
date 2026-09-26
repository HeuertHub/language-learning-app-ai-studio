import React, { useState, useEffect } from 'react';
import type { Lesson, Unit, LevelCurriculum, Exercise } from '../types/curriculum';
import type { ExerciseDefinition, InteractionPattern } from '../types/exerciseEngine';
import { playMongolianAudio, getAudioSystemStatus, checkExerciseAudioAvailability } from '../utils/audio';
import {
  evaluateExerciseSubmission,
  type EvaluationOutcome,
  type SubmissionPayload,
} from '../utils/evaluationEngine';
import { curriculumService } from '../services/curriculumService';
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
  Layers,
  HelpCircle,
  FileText,
  VolumeX,
  Check,
  Link2,
  Unlink,
  X,
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

/**
 * Normalizes legacy or modern exercise representations into canonical ExerciseDefinition
 */
function toExerciseDefinition(raw: ExerciseDefinition | Exercise, index: number, lesson: Lesson, unit: Unit, level: LevelCurriculum): ExerciseDefinition {
  if ('interactionPattern' in raw) {
    return raw as ExerciseDefinition;
  }

  // Convert legacy Exercise to modern ExerciseDefinition
  const legacy = raw as Exercise;
  let pattern: InteractionPattern = 'MULTIPLE_CHOICE';
  if (legacy.type === 'AUDIO_DICTATION') pattern = 'AUDIO_DICTATION';
  else if (legacy.type === 'AUDIO_COMPREHENSION') pattern = 'AUDIO_COMPREHENSION';
  else if (legacy.type === 'SENTENCE_CONSTRUCTION') pattern = 'TOKEN_REARRANGEMENT';
  else if (legacy.type === 'GRAMMAR_APPLICATION') pattern = 'SUFFIX_ATTACHMENT';

  return {
    exerciseId: legacy.id,
    sequenceInLesson: index + 1,
    exerciseTitle: `Exercise ${index + 1}: ${legacy.prompt.slice(0, 30)}...`,
    modality: 'GRAMMAR_PRACTICE',
    interactionPattern: pattern,
    cognitiveComplexity: 'APPLY_MORPHOLOGY',
    skillTargets: ['morphology'],
    grammarTargets: [legacy.grammarPointId || 'grammar'],
    vocabularyTargets: [],
    prompt: legacy.prompt,
    stimulusTextCyrillic: legacy.cyrillicSentence,
    stimulusTranslation: legacy.englishTranslation,
    options: legacy.options?.map((o) => ({
      id: o.id,
      text: o.text,
      cyrillic: o.cyrillic,
      isCorrect: o.isCorrect,
      explanation: o.explanation,
    })),
    wordTokens: legacy.wordTokens,
    correctTokenOrder: legacy.correctTokenOrder,
    baseWord: legacy.baseWord,
    suffixOptions: legacy.suffixOptions,
    correctSuffix: legacy.correctSuffix,
    correctAnswer: legacy.correctAnswer || legacy.correctSuffix || '',
    hint: 'Review the grammatical rules in the orientation overview.',
    explanation: legacy.detailedGrammarNote,
    learnerFeedback: {
      onSuccess: 'Correct response.',
      onFailure: 'Review the grammar rule and examine the breakdown.',
    },
    detailedGrammarNote: legacy.detailedGrammarNote,
    audio: legacy.audioText
      ? {
          requiresAudio: true,
          speechSynthesisText: legacy.audioText,
          slowSpeechSynthesisText: legacy.slowAudioText,
          ipaTranscription: '',
        }
      : undefined,
    evaluation: {
      matchType: legacy.type === 'SENTENCE_CONSTRUCTION' ? 'TOKEN_ORDER' : 'NORMALIZED_TEXT',
    },
    lessonId: lesson.id,
    unitId: unit.id,
    cefrLevel: level.cefr,
  };
}

export const LessonView: React.FC<LessonViewProps> = ({
  lesson,
  unit,
  level,
  onBackToSyllabus,
  onCompleteLesson,
  audioSpeed,
}) => {
  const [phase, setPhase] = useState<'orientation' | 'exercise' | 'completed'>('orientation');
  const [exercises, setExercises] = useState<ExerciseDefinition[]>([]);
  const [currentExerciseIndex, setCurrentExerciseIndex] = useState(0);
  const [isLoadingExercises, setIsLoadingExercises] = useState(false);

  // User input states
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [selectedOptionIds, setSelectedOptionIds] = useState<string[]>([]);
  const [selectedSuffix, setSelectedSuffix] = useState<string | null>(null);
  const [textInput, setTextInput] = useState('');
  const [builtSentenceTokens, setBuiltSentenceTokens] = useState<string[]>([]);
  const [availableSentenceTokens, setAvailableSentenceTokens] = useState<string[]>([]);
  const [matchedPairs, setMatchedPairs] = useState<Record<string, string>>({});
  const [selectedPairLeft, setSelectedPairLeft] = useState<string | null>(null);
  const [showHint, setShowHint] = useState(false);
  const [rubricSelfChecks, setRubricSelfChecks] = useState<Record<string, boolean>>({});

  // Submission & evaluation states
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false);
  const [evaluationOutcome, setEvaluationOutcome] = useState<EvaluationOutcome | null>(null);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);

  // Session stats
  const [correctCount, setCorrectCount] = useState(0);
  const [attemptCount, setAttemptCount] = useState(0);
  const [sessionStartTime] = useState<number>(Date.now());

  const audioStatus = getAudioSystemStatus();

  // Load exercises for this lesson if not already bundled
  useEffect(() => {
    async function loadExercises() {
      setIsLoadingExercises(true);
      try {
        if (lesson.exercises && lesson.exercises.length > 0) {
          const defs = lesson.exercises.map((ex, idx) =>
            toExerciseDefinition(ex, idx, lesson, unit, level)
          );
          setExercises(defs);
        } else {
          // Fetch pilot exercises from service
          const pilotList = await curriculumService.getLessonExercises(lesson.id);
          if (pilotList && pilotList.length > 0) {
            setExercises(pilotList);
          } else {
            setExercises([]);
          }
        }
      } catch (err) {
        console.error('Error loading exercises:', err);
        setExercises([]);
      } finally {
        setIsLoadingExercises(false);
      }
    }
    loadExercises();
  }, [lesson, unit, level]);

  const currentExercise = exercises[currentExerciseIndex] as ExerciseDefinition | undefined;

  // Prepare input states whenever current exercise changes
  useEffect(() => {
    if (!currentExercise) return;

    setSelectedOptionId(null);
    setSelectedOptionIds([]);
    setSelectedSuffix(null);
    setTextInput('');
    setIsAnswerSubmitted(false);
    setEvaluationOutcome(null);
    setShowHint(false);
    setMatchedPairs({});
    setSelectedPairLeft(null);
    setRubricSelfChecks({});

    // Token rearrangement preparation
    if (currentExercise.interactionPattern === 'TOKEN_REARRANGEMENT' && currentExercise.wordTokens) {
      const shuffled = [...currentExercise.wordTokens].sort(() => Math.random() - 0.5);
      setAvailableSentenceTokens(shuffled);
      setBuiltSentenceTokens([]);
    }

    // Auto-play audio ONLY if audio is genuinely available (never auto-play when audio is unavailable or unsupported)
    const audioText = currentExercise.audio?.speechSynthesisText;
    if (
      (currentExercise.interactionPattern === 'AUDIO_DICTATION' ||
        currentExercise.interactionPattern === 'AUDIO_COMPREHENSION') &&
      audioText
    ) {
      const assessment = checkExerciseAudioAvailability(currentExercise, lesson);
      if (assessment.isAvailable) {
        playMongolianAudio(
          audioText,
          audioSpeed,
          () => setIsPlayingAudio(true),
          () => setIsPlayingAudio(false)
        );
      }
    }
  }, [currentExerciseIndex, currentExercise, phase, audioSpeed, lesson]);

  const handlePlayAudio = (text: string, customSpeed?: number) => {
    playMongolianAudio(
      text,
      customSpeed ?? audioSpeed,
      () => setIsPlayingAudio(true),
      () => setIsPlayingAudio(false)
    );
  };

  const handleToggleMultiSelectOption = (optionId: string) => {
    if (isAnswerSubmitted) return;
    setSelectedOptionIds((prev) =>
      prev.includes(optionId) ? prev.filter((id) => id !== optionId) : [...prev, optionId]
    );
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

    // Build authoritative submission payload
    const submission: SubmissionPayload = {
      selectedOptionId: selectedOptionId || undefined,
      selectedOptionIds: selectedOptionIds.length > 0 ? selectedOptionIds : undefined,
      textInput: textInput.trim(),
      arrangedTokens: builtSentenceTokens,
      selectedSuffix: selectedSuffix || undefined,
      matchedPairs,
    };

    // Evaluate using single authoritative evaluation engine
    const outcome = evaluateExerciseSubmission(currentExercise, submission);
    setEvaluationOutcome(outcome);
    setIsAnswerSubmitted(true);
    setAttemptCount((prev) => prev + 1);

    // Per Phase 3B.4: Qualitative rubric submissions must NOT increment objective correctness counts
    if (outcome.isCorrect && !outcome.isRubricQualitative) {
      setCorrectCount((prev) => prev + 1);
    }
  };

  const handleNextExercise = () => {
    if (currentExerciseIndex < exercises.length - 1) {
      setCurrentExerciseIndex((prev) => prev + 1);
    } else {
      // Completed all exercises in this lesson
      const elapsedMinutes = Math.max(1, Math.round((Date.now() - sessionStartTime) / 60000));
      setPhase('completed');
      const finalExerciseCorrect = evaluationOutcome?.isCorrect && !evaluationOutcome?.isRubricQualitative ? 1 : 0;
      onCompleteLesson({
        lessonId: lesson.id,
        unitId: unit.id,
        exercisesAttempted: attemptCount + 1,
        exercisesCorrect: correctCount + finalExerciseCorrect,
        minutesSpent: elapsedMinutes,
        vocabMasteredCount: lesson.vocabulary.length,
      });
    }
  };

  // Phase 1: Linguistic Orientation & Blueprint Foundations
  if (phase === 'orientation') {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
        <button
          type="button"
          onClick={onBackToSyllabus}
          className="inline-flex items-center gap-1.5 text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors mb-6"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Return to Curriculum Syllabus</span>
        </button>

        <div className="bg-white border border-stone-200 rounded-xl p-6 sm:p-8 shadow-xs space-y-8">
          {/* Header Metadata */}
          <div className="border-b border-stone-100 pb-6">
            <div className="flex items-center gap-2 text-xs font-mono text-stone-500 mb-1.5">
              <span className="px-1.5 py-0.5 rounded bg-stone-100 font-bold text-stone-700">
                {level.cefr}
              </span>
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

          {/* Primary Purpose & Communicative Outcome */}
          <div className="space-y-4">
            <h2 className="text-sm font-semibold uppercase tracking-wider text-stone-500 flex items-center gap-1.5">
              <BookOpen className="w-4 h-4 text-stone-700" />
              <span>Pedagogical Purpose & Objectives</span>
            </h2>
            <div className="bg-stone-50 border border-stone-200 rounded-lg p-5 text-sm leading-relaxed text-stone-800 space-y-3">
              <p className="font-medium text-stone-900">
                {lesson.primaryPurpose || lesson.grammarOverview.summary}
              </p>
              {lesson.communicativeOutcome && (
                <div className="text-xs font-mono text-stone-600 bg-white/80 p-2.5 rounded border border-stone-200">
                  <span className="font-bold text-stone-800">Target Outcome:</span> {lesson.communicativeOutcome}
                </div>
              )}
              {lesson.grammarOverview.keyPoints.length > 0 && (
                <ul className="space-y-2 pt-2 border-t border-stone-200/80">
                  {lesson.grammarOverview.keyPoints.map((point, idx) => (
                    <li key={idx} className="flex items-start gap-2 text-stone-700">
                      <span className="text-amber-700 font-bold text-xs mt-0.5">•</span>
                      <span>{point}</span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>

          {/* Audio Safety & Voice Notice */}
          <div className="p-3.5 bg-stone-50 rounded-lg border border-stone-200 flex items-center justify-between text-xs text-stone-600">
            <div className="flex items-center gap-2">
              <Volume2 className="w-4 h-4 text-stone-700 shrink-0" />
              <span>
                {audioStatus.hasMongolianVoice
                  ? `Native Mongolian audio voice active (${audioStatus.voiceName}).`
                  : 'Web Audio acoustic formant synthesizer active for Cyrillic phonemes. Non-Mongolian voices strictly blocked.'}
              </span>
            </div>
            <span className="font-mono text-[11px] px-2 py-0.5 bg-white border border-stone-200 rounded text-stone-700">
              Safe Voice Protocol
            </span>
          </div>

          {/* Action Row */}
          <div className="pt-4 border-t border-stone-200 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <span className="text-xs text-stone-500">
              {exercises.length > 0
                ? `${exercises.length} Interactive Pedagogical Exercises Prepared`
                : 'Curriculum blueprint loaded (Exercises available in certified pilot units).'}
            </span>

            {exercises.length > 0 ? (
              <button
                type="button"
                onClick={() => setPhase('exercise')}
                className="px-6 py-2.5 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs flex items-center justify-center gap-1.5"
              >
                <span>Begin Lesson Exercises</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            ) : (
              <button
                type="button"
                onClick={onBackToSyllabus}
                className="px-5 py-2 border border-stone-300 hover:bg-stone-100 rounded-md text-xs font-medium text-stone-700"
              >
                Return to Syllabus (Select Pilot Unit)
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // Phase 3: Completed Lesson Screen
  if (phase === 'completed') {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center space-y-6">
        <div className="w-16 h-16 bg-emerald-50 text-emerald-800 rounded-full flex items-center justify-center mx-auto border border-emerald-200">
          <CheckCircle2 className="w-8 h-8 text-emerald-700" />
        </div>
        <div className="space-y-2">
          <span className="text-xs font-mono uppercase tracking-wider text-stone-500">
            Lesson Completed
          </span>
          <h1 className="text-3xl font-serif font-bold text-stone-900">
            {lesson.title}
          </h1>
          <p className="text-stone-600 font-serif italic text-lg">
            {lesson.cyrillicTitle}
          </p>
        </div>

        <div className="bg-white border border-stone-200 rounded-xl p-6 shadow-2xs max-w-md mx-auto text-left space-y-3">
          <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider">
            Pedagogical Summary
          </div>
          <div className="flex justify-between text-sm border-b border-stone-100 pb-2">
            <span className="text-stone-600">Unit:</span>
            <span className="font-medium text-stone-900">Unit {unit.unitNumber} ({level.cefr})</span>
          </div>
          <div className="flex justify-between text-sm border-b border-stone-100 pb-2">
            <span className="text-stone-600">Exercises Practiced:</span>
            <span className="font-mono font-bold text-stone-900">{exercises.length}</span>
          </div>
          <div className="flex justify-between text-sm">
            <span className="text-stone-600">Status:</span>
            <span className="font-mono text-emerald-700 font-bold">Synchronized to Profile</span>
          </div>
        </div>

        <button
          type="button"
          onClick={onBackToSyllabus}
          className="px-6 py-2.5 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs inline-flex items-center gap-2"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to Curriculum Syllabus</span>
        </button>
      </div>
    );
  }

  // Phase 2: Interactive Exercise Execution
  if (!currentExercise) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center space-y-4">
        <p className="text-stone-600">No exercises found for this lesson blueprint.</p>
        <button
          type="button"
          onClick={() => setPhase('orientation')}
          className="px-4 py-2 border border-stone-300 rounded text-xs"
        >
          Return to Lesson Overview
        </button>
      </div>
    );
  }

  const pattern = currentExercise.interactionPattern;
  const audioText = currentExercise.audio?.speechSynthesisText;

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-8 space-y-6">
      {/* Top Header & Breadcrumbs */}
      <div className="flex items-center justify-between border-b border-stone-200 pb-3">
        <button
          type="button"
          onClick={() => setPhase('orientation')}
          className="inline-flex items-center gap-1.5 text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Lesson Overview</span>
        </button>
        <div className="flex items-center gap-2 text-xs font-mono text-stone-600">
          <span className="font-bold text-stone-800">
            Exercise {currentExerciseIndex + 1}
          </span>
          <span>of</span>
          <span>{exercises.length}</span>
          <span className="px-1.5 py-0.5 rounded bg-stone-100 text-[11px] font-bold text-stone-700">
            {currentExercise.cognitiveComplexity}
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-stone-200 h-1.5 rounded-full overflow-hidden">
        <div
          className="bg-stone-900 h-full rounded-full transition-all duration-300"
          style={{ width: `${((currentExerciseIndex + 1) / exercises.length) * 100}%` }}
        />
      </div>

      {/* Exercise Card */}
      <div className="bg-white border border-stone-200 rounded-xl p-6 sm:p-8 shadow-xs space-y-6">
        {/* Modality & Pattern Badges */}
        <div className="flex flex-wrap items-center justify-between gap-2 text-[11px] font-mono text-stone-500">
          <div className="flex items-center gap-1.5">
            <span className="px-2 py-0.5 rounded bg-stone-100 border border-stone-200 text-stone-700 font-semibold">
              {pattern}
            </span>
            <span className="text-stone-400">•</span>
            <span>{currentExercise.modality}</span>
          </div>
          {currentExercise.hint && (
            <button
              type="button"
              onClick={() => setShowHint(!showHint)}
              className="text-stone-500 hover:text-stone-800 flex items-center gap-1 underline underline-offset-2"
            >
              <HelpCircle className="w-3.5 h-3.5" />
              <span>{showHint ? 'Hide Hint' : 'Linguistic Hint'}</span>
            </button>
          )}
        </div>

        {/* Hint Box */}
        {showHint && currentExercise.hint && (
          <div className="p-3 bg-amber-50/70 border border-amber-200 rounded-lg text-xs text-amber-900 leading-relaxed">
            <span className="font-bold">Linguistic Guidance:</span> {currentExercise.hint}
          </div>
        )}

        {/* Exercise Prompt */}
        <div className="space-y-2">
          <h2 className="text-lg sm:text-xl font-serif font-bold text-stone-900 leading-snug">
            {currentExercise.prompt}
          </h2>
          {currentExercise.stimulusTextCyrillic && (
            <div className="p-4 bg-stone-50 rounded-lg border border-stone-200/80">
              <p className="text-xl sm:text-2xl font-serif font-bold text-stone-900">
                {currentExercise.stimulusTextCyrillic}
              </p>
              {currentExercise.stimulusTranslation && (
                <p className="text-xs text-stone-500 font-serif italic mt-1">
                  {currentExercise.stimulusTranslation}
                </p>
              )}
            </div>
          )}
        </div>

        {/* Audio Player Controls */}
        {audioText && (() => {
          const audioAssessment = checkExerciseAudioAvailability(currentExercise, lesson);
          if (!audioAssessment.isAvailable) {
            return (
              <div className="flex items-center gap-2.5 p-3 bg-amber-50/60 border border-amber-200 rounded-lg text-xs text-amber-950">
                <VolumeX className="w-4 h-4 text-amber-700 shrink-0" />
                <span className="font-medium">
                  {audioAssessment.statusMessage || 'Appropriate Mongolian audio unavailable (native recording pending)'}
                </span>
                <div className="text-[11px] text-stone-500 ml-auto truncate">
                  {currentExercise.audio?.ipaTranscription && (
                    <span className="font-mono text-stone-600">[{currentExercise.audio.ipaTranscription}]</span>
                  )}
                </div>
              </div>
            );
          }
          return (
            <div className="flex items-center gap-3 p-3 bg-stone-50 rounded-lg border border-stone-200">
              <button
                type="button"
                onClick={() => handlePlayAudio(audioText, audioSpeed)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-stone-900 text-stone-100 hover:bg-stone-800 text-xs font-medium transition-colors"
              >
                <Volume2 className="w-4 h-4" />
                <span>Listen</span>
              </button>
              <button
                type="button"
                onClick={() => handlePlayAudio(audioText, 0.75)}
                className="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-md bg-white border border-stone-300 text-stone-700 hover:bg-stone-100 text-xs font-mono font-medium transition-colors"
              >
                <span>0.75x Slow</span>
              </button>
              <div className="text-[11px] text-stone-500 ml-auto truncate">
                {currentExercise.audio?.ipaTranscription && (
                  <span className="font-mono text-stone-600">[{currentExercise.audio.ipaTranscription}]</span>
                )}
              </div>
            </div>
          );
        })()}

        {/* ========================================================================= */}
        {/* INTERACTION PATTERN RENDERERS */}
        {/* ========================================================================= */}

        {/* 1. MULTIPLE_CHOICE & AUDIO_COMPREHENSION */}
        {(pattern === 'MULTIPLE_CHOICE' || pattern === 'AUDIO_COMPREHENSION') && currentExercise.options && (
          <div className="space-y-2.5">
            {currentExercise.options.map((opt) => {
              const isSelected = selectedOptionId === opt.id;
              const isSubmitted = isAnswerSubmitted;
              const isCorrectOpt = opt.isCorrect;

              let btnStyle = 'border-stone-200 hover:bg-stone-50 bg-white text-stone-900';
              if (isSelected) {
                btnStyle = 'border-stone-900 bg-stone-50 ring-1 ring-stone-900 text-stone-900';
              }
              if (isSubmitted) {
                if (isCorrectOpt) {
                  btnStyle = 'border-emerald-600 bg-emerald-50/70 text-emerald-950 font-medium';
                } else if (isSelected && !isCorrectOpt) {
                  btnStyle = 'border-red-500 bg-red-50/70 text-red-950';
                }
              }

              return (
                <button
                  key={opt.id}
                  type="button"
                  disabled={isAnswerSubmitted}
                  onClick={() => setSelectedOptionId(opt.id)}
                  className={`w-full p-4 rounded-lg border text-left text-sm transition-all flex items-center justify-between ${btnStyle}`}
                >
                  <span className="font-serif font-medium">{opt.text}</span>
                  {opt.cyrillic && (
                    <span className="font-serif italic text-stone-500 text-xs mr-2">
                      ({opt.cyrillic})
                    </span>
                  )}
                  {isSubmitted && isCorrectOpt && (
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 ml-2" />
                  )}
                </button>
              );
            })}
          </div>
        )}

        {/* 2. MULTI_SELECT */}
        {pattern === 'MULTI_SELECT' && currentExercise.options && (
          <div className="space-y-2.5">
            <p className="text-xs text-stone-500 italic">Select all options that apply:</p>
            {currentExercise.options.map((opt) => {
              const isSelected = selectedOptionIds.includes(opt.id);
              const isSubmitted = isAnswerSubmitted;
              const isCorrectOpt = opt.isCorrect;

              let cardStyle = 'border-stone-200 hover:bg-stone-50 bg-white text-stone-900';
              if (isSelected) {
                cardStyle = 'border-stone-900 bg-stone-100/60 ring-1 ring-stone-900';
              }
              if (isSubmitted) {
                if (isCorrectOpt) {
                  cardStyle = 'border-emerald-600 bg-emerald-50 text-emerald-950';
                } else if (isSelected && !isCorrectOpt) {
                  cardStyle = 'border-red-500 bg-red-50 text-red-950';
                }
              }

              return (
                <button
                  key={opt.id}
                  type="button"
                  disabled={isAnswerSubmitted}
                  onClick={() => handleToggleMultiSelectOption(opt.id)}
                  className={`w-full p-3.5 rounded-lg border text-left text-sm transition-all flex items-center justify-between ${cardStyle}`}
                >
                  <div className="flex items-center gap-3">
                    <div
                      className={`w-4 h-4 rounded border flex items-center justify-center shrink-0 ${
                        isSelected ? 'bg-stone-900 border-stone-900 text-white' : 'border-stone-300 bg-white'
                      }`}
                    >
                      {isSelected && <Check className="w-3 h-3 stroke-[3]" />}
                    </div>
                    <span className="font-serif font-medium">{opt.text}</span>
                  </div>
                  {opt.cyrillic && (
                    <span className="font-serif text-xs text-stone-500">{opt.cyrillic}</span>
                  )}
                </button>
              );
            })}
          </div>
        )}

        {/* 3. PAIR_MATCHING (Genuine Multi-Pair Construction) */}
        {pattern === 'PAIR_MATCHING' && (
          <div className="space-y-6">
            <div className="flex items-center justify-between text-xs text-stone-500 pb-1 border-b border-stone-100">
              <span className="italic">
                Select an item on the left, then tap its matching partner on the right:
              </span>
              <span className="font-mono font-medium text-stone-700">
                Matched: {Object.keys(matchedPairs).length} / {(currentExercise.matchingPairs || []).length}
              </span>
            </div>

            {currentExercise.matchingPairs && currentExercise.matchingPairs.length > 0 ? (
              <div className="space-y-5">
                {/* Two-Column Matching Columns */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {/* Left-Side Column */}
                  <div className="space-y-2">
                    <span className="text-xs font-mono font-semibold uppercase text-stone-500 block mb-1">
                      Column A (Select Source):
                    </span>
                    <div className="space-y-2">
                      {currentExercise.matchingPairs.map((pair) => {
                        const isSelectedLeft = selectedPairLeft === pair.left;
                        const pairedRight = matchedPairs[pair.left];
                        const isPaired = !!pairedRight;

                        let cardStyle = 'border-stone-200 bg-white hover:border-stone-400 text-stone-900';
                        if (isSelectedLeft) {
                          cardStyle = 'border-stone-900 bg-stone-900 text-stone-100 ring-2 ring-stone-900 shadow-xs';
                        } else if (isPaired) {
                          cardStyle = 'border-stone-400 bg-stone-50 text-stone-900 font-medium';
                        }

                        return (
                          <button
                            key={pair.id || pair.left}
                            type="button"
                            disabled={isAnswerSubmitted}
                            onClick={() => {
                              if (isAnswerSubmitted) return;
                              setSelectedPairLeft(isSelectedLeft ? null : pair.left);
                            }}
                            className={`w-full p-3.5 rounded-lg border text-left transition-all flex items-center justify-between ${cardStyle}`}
                          >
                            <span className="text-base font-serif font-bold">{pair.left}</span>
                            {isPaired && (
                              <span className="inline-flex items-center gap-1 text-xs font-mono px-2 py-0.5 rounded bg-stone-200 text-stone-800">
                                <span>↔</span>
                                <span>{pairedRight}</span>
                              </span>
                            )}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Right-Side Column (Shuffled/Inverted order to prevent trivial adjacency) */}
                  <div className="space-y-2">
                    <span className="text-xs font-mono font-semibold uppercase text-stone-500 block mb-1">
                      Column B (Select Target):
                    </span>
                    <div className="space-y-2">
                      {[...currentExercise.matchingPairs]
                        .reverse()
                        .map((pair) => {
                          const targetRight = pair.right;
                          // Find if any left item is currently paired to this right item
                          const pairedLeft = Object.keys(matchedPairs).find(
                            (k) => matchedPairs[k] === targetRight
                          );
                          const isPaired = !!pairedLeft;

                          return (
                            <button
                              key={`right_${pair.id || targetRight}`}
                              type="button"
                              disabled={isAnswerSubmitted}
                              onClick={() => {
                                if (isAnswerSubmitted) return;
                                if (!selectedPairLeft) return;
                                // Pair selectedLeft with this targetRight
                                setMatchedPairs((prev) => ({
                                  ...prev,
                                  [selectedPairLeft]: targetRight,
                                }));
                                setSelectedPairLeft(null);
                              }}
                              className={`w-full p-3.5 rounded-lg border text-left transition-all flex items-center justify-between ${
                                isPaired
                                  ? 'border-stone-400 bg-stone-100 text-stone-900 font-medium'
                                  : selectedPairLeft
                                  ? 'border-stone-300 bg-white hover:border-stone-900 hover:bg-stone-50 cursor-pointer'
                                  : 'border-stone-200 bg-white text-stone-700 opacity-90'
                              }`}
                            >
                              <span className="text-base font-serif font-bold">{targetRight}</span>
                              {isPaired && (
                                <span className="inline-flex items-center gap-1 text-xs font-mono px-2 py-0.5 rounded bg-stone-200 text-stone-800">
                                  <span>{pairedLeft}</span>
                                  <span>↔</span>
                                </span>
                              )}
                            </button>
                          );
                        })}
                    </div>
                  </div>
                </div>

                {/* Constructed Pairs Workspace */}
                <div className="pt-2">
                  <div className="text-xs font-mono text-stone-500 uppercase tracking-wider mb-2 flex items-center justify-between">
                    <span>Constructed Grapheme Pairs:</span>
                    {Object.keys(matchedPairs).length > 0 && !isAnswerSubmitted && (
                      <button
                        type="button"
                        onClick={() => setMatchedPairs({})}
                        className="text-[11px] text-stone-500 hover:text-red-700 transition-colors"
                      >
                        Reset All Pairs
                      </button>
                    )}
                  </div>

                  {Object.keys(matchedPairs).length === 0 ? (
                    <div className="p-3.5 rounded-lg border border-dashed border-stone-300 text-xs text-stone-400 italic text-center">
                      No pairs constructed yet. Tap an item in Column A, then tap its corresponding item in Column B.
                    </div>
                  ) : (
                    <div className="flex flex-wrap gap-2.5">
                      {Object.entries(matchedPairs).map(([left, right]) => (
                        <div
                          key={left}
                          className="inline-flex items-center gap-2 px-3 py-1.5 rounded-md bg-stone-100 border border-stone-300 text-stone-900 text-xs font-mono"
                        >
                          <span className="font-serif font-bold text-sm">{left}</span>
                          <span className="text-stone-400">↔</span>
                          <span className="font-serif font-bold text-sm">{right}</span>
                          {!isAnswerSubmitted && (
                            <button
                              type="button"
                              onClick={() => {
                                setMatchedPairs((prev) => {
                                  const updated = { ...prev };
                                  delete updated[left];
                                  return updated;
                                });
                              }}
                              className="text-stone-400 hover:text-red-600 transition-colors ml-1 p-0.5"
                              title="Unlink pair"
                            >
                              <X className="w-3.5 h-3.5" />
                            </button>
                          )}
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ) : null}
          </div>
        )}

        {/* 4. TOKEN_REARRANGEMENT (Sentence Builder) */}
        {pattern === 'TOKEN_REARRANGEMENT' && (
          <div className="space-y-5">
            {/* Built Sentence Workspace */}
            <div>
              <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-2">
                Assembled Mongolian SOV Sentence:
              </div>
              <div className="min-h-[58px] p-3 rounded-lg border-2 border-dashed border-stone-300 bg-stone-50/60 flex flex-wrap gap-2 items-center">
                {builtSentenceTokens.length === 0 ? (
                  <span className="text-xs text-stone-400 italic">
                    Tap word tokens below in correct syntactic order...
                  </span>
                ) : (
                  builtSentenceTokens.map((token, idx) => (
                    <button
                      key={idx}
                      type="button"
                      disabled={isAnswerSubmitted}
                      onClick={() => handleRemoveToken(token, idx)}
                      className="px-3 py-1.5 rounded-md bg-stone-900 text-stone-100 font-serif text-sm font-medium hover:bg-stone-700 transition-colors"
                    >
                      {token}
                    </button>
                  ))
                )}
              </div>
            </div>

            {/* Available Tokens Pool */}
            <div>
              <div className="text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-2">
                Available Word Tokens:
              </div>
              <div className="flex flex-wrap gap-2">
                {availableSentenceTokens.map((token, idx) => (
                  <button
                    key={idx}
                    type="button"
                    disabled={isAnswerSubmitted}
                    onClick={() => handleSelectToken(token, idx)}
                    className="px-3 py-1.5 rounded-md bg-white border border-stone-300 text-stone-800 font-serif text-sm font-medium hover:bg-stone-100 transition-colors shadow-2xs active:scale-95"
                  >
                    {token}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* 5. SUFFIX_ATTACHMENT */}
        {pattern === 'SUFFIX_ATTACHMENT' && (
          <div className="space-y-4">
            <div className="p-4 bg-stone-50 rounded-lg border border-stone-200 text-center">
              <span className="text-xs font-mono text-stone-500 uppercase block mb-1">
                Stem / Base Word:
              </span>
              <span className="text-2xl font-serif font-bold text-stone-900">
                {currentExercise.baseWord}
              </span>
            </div>

            {currentExercise.suffixOptions && currentExercise.suffixOptions.length > 0 && (
              <div>
                <span className="text-xs font-mono text-stone-500 uppercase block mb-2">
                  Select Harmonic Suffix:
                </span>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                  {currentExercise.suffixOptions.map((suffix) => {
                    const isSelected = selectedSuffix === suffix;
                    return (
                      <button
                        key={suffix}
                        type="button"
                        disabled={isAnswerSubmitted}
                        onClick={() => setSelectedSuffix(suffix)}
                        className={`p-3 rounded-lg border text-center font-serif text-base font-medium transition-all ${
                          isSelected
                            ? 'border-stone-900 bg-stone-900 text-stone-100 shadow-xs'
                            : 'border-stone-200 bg-white hover:bg-stone-50 text-stone-900'
                        }`}
                      >
                        {suffix}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        )}

        {/* 6. CLOZE_TEXT & AUDIO_DICTATION */}
        {(pattern === 'CLOZE_TEXT' || pattern === 'AUDIO_DICTATION') && (
          <div className="space-y-4">
            {currentExercise.contextSentence && (
              <div className="p-3 bg-stone-50 rounded-lg border border-stone-200 font-serif text-base text-stone-800">
                {currentExercise.contextSentence}
              </div>
            )}

            <div>
              <label className="block text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1.5">
                Cyrillic Transcription Input:
              </label>
              <input
                type="text"
                value={textInput}
                disabled={isAnswerSubmitted}
                onChange={(e) => setTextInput(e.target.value)}
                placeholder="Type in Cyrillic script..."
                className="w-full px-4 py-2.5 border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-stone-900 font-serif text-lg text-stone-900 bg-white"
              />
            </div>

            {/* On-screen Cyrillic Keyboard */}
            {!isAnswerSubmitted && (
              <CyrillicKeyboard
                onInsertChar={(char: string) => setTextInput((prev) => prev + char)}
                onBackspace={() => setTextInput((prev) => prev.slice(0, -1))}
              />
            )}
          </div>
        )}

        {/* 7. OPEN_RESPONSE_RUBRIC / FREE_RESPONSE_RUBRIC */}
        {(pattern === 'OPEN_RESPONSE_RUBRIC' || pattern === 'FREE_RESPONSE_RUBRIC') && (
          <div className="space-y-4">
            <div>
              <label className="block text-xs font-mono font-medium text-stone-500 uppercase tracking-wider mb-1.5">
                Analytical Synthesis & Writing Response:
              </label>
              <textarea
                rows={4}
                value={textInput}
                disabled={isAnswerSubmitted}
                onChange={(e) => setTextInput(e.target.value)}
                placeholder="Compose your structured rhetorical or analytical critique in Mongolian Cyrillic..."
                className="w-full p-4 border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-stone-900 font-serif text-base text-stone-900 bg-white"
              />
            </div>

            {/* Criteria Preview */}
            {currentExercise.evaluation?.rubricCriteria && (
              <div className="p-3.5 bg-stone-50 rounded-lg border border-stone-200 space-y-2">
                <span className="text-xs font-mono font-semibold text-stone-700 uppercase">
                  Academic Rubric Criteria:
                </span>
                <ul className="text-xs text-stone-600 space-y-1">
                  {currentExercise.evaluation.rubricCriteria.map((c, i) => (
                    <li key={i} className="flex items-start gap-1.5">
                      <span className="text-stone-400">•</span>
                      <span>
                        <strong className="text-stone-800">{c.criterion || `Criterion ${i + 1}`}</strong> ({c.points} pts): {c.description}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        {/* ========================================================================= */}
        {/* EVALUATION FEEDBACK & PEDAGOGICAL BREAKDOWN */}
        {/* ========================================================================= */}
        {isAnswerSubmitted && evaluationOutcome && (
          <div
            className={`p-5 rounded-lg border space-y-4 animate-in fade-in duration-200 ${
              evaluationOutcome.isRubricQualitative
                ? 'bg-stone-50 border-stone-300 text-stone-900'
                : evaluationOutcome.isCorrect
                ? 'bg-emerald-50/70 border-emerald-200 text-emerald-950'
                : 'bg-red-50/70 border-red-200 text-red-950'
            }`}
          >
            <div className="flex items-start gap-3">
              {evaluationOutcome.isRubricQualitative ? (
                <FileText className="w-5 h-5 text-stone-700 shrink-0 mt-0.5" />
              ) : evaluationOutcome.isCorrect ? (
                <CheckCircle2 className="w-5 h-5 text-emerald-700 shrink-0 mt-0.5" />
              ) : (
                <AlertCircle className="w-5 h-5 text-red-700 shrink-0 mt-0.5" />
              )}
              <div className="space-y-1 flex-1">
                <div className="font-semibold text-sm">
                  {evaluationOutcome.isRubricQualitative
                    ? 'Response Submitted — Review Against Rubric'
                    : evaluationOutcome.isCorrect
                    ? 'Correct Analysis'
                    : 'Correction Required'}
                </div>
                <p className="text-xs sm:text-sm leading-relaxed">
                  {evaluationOutcome.feedbackMessage}
                </p>
              </div>
            </div>

            {/* Pair Matching Detailed Breakdown if applicable */}
            {pattern === 'PAIR_MATCHING' && evaluationOutcome.details?.pairs && (
              <div className="pt-3 border-t border-stone-200/80 space-y-2">
                <div className="text-xs font-mono font-semibold uppercase tracking-wider text-stone-700">
                  Pairing Validation Details:
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                  {(evaluationOutcome.details.pairs as Array<{ left: string; expectedRight: string; userRight: string; isMatch: boolean }>).map((p, idx) => (
                    <div
                      key={idx}
                      className={`p-2 rounded border flex items-center justify-between ${
                        p.isMatch ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : 'bg-red-50 border-red-200 text-red-900'
                      }`}
                    >
                      <span className="font-serif font-bold">{p.left} ↔ {p.userRight || '(None)'}</span>
                      <span className="text-[11px] font-mono">
                        {p.isMatch ? '✓ Correct' : `✗ Expected: ${p.expectedRight}`}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Qualitative Rubric Reflection Checklist */}
            {evaluationOutcome.isRubricQualitative && evaluationOutcome.rubricCriteria && (
              <div className="mt-4 pt-4 border-t border-stone-200 space-y-3">
                <div className="text-xs font-mono font-bold uppercase tracking-wider text-stone-800">
                  Learner Qualitative Self-Reflection Checklist:
                </div>
                <div className="space-y-2">
                  {evaluationOutcome.rubricCriteria.map((c, idx) => {
                    const cKey = c.criterionId || `crit_${idx}`;
                    const checked = rubricSelfChecks[cKey] || false;
                    return (
                      <label
                        key={idx}
                        className="flex items-start gap-2.5 text-xs text-stone-800 cursor-pointer"
                      >
                        <input
                          type="checkbox"
                          checked={checked}
                          onChange={(e) =>
                            setRubricSelfChecks((prev) => ({ ...prev, [cKey]: e.target.checked }))
                          }
                          className="rounded border-stone-300 text-stone-900 focus:ring-stone-600 mt-0.5"
                        />
                        <span>
                          <strong>{c.criterion || `Criterion ${idx + 1}`}</strong> ({c.points} pts): {c.description}
                        </span>
                      </label>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Scholarly Pedagogical Note */}
            {(currentExercise.detailedGrammarNote || currentExercise.explanation) && (
              <div className="pt-3 border-t border-emerald-200/60 text-xs text-stone-700 space-y-1">
                <span className="font-semibold text-stone-900 block">
                  Linguistic Explanation:
                </span>
                <p className="leading-relaxed">
                  {currentExercise.detailedGrammarNote || currentExercise.explanation}
                </p>
              </div>
            )}
          </div>
        )}

        {/* Action Button Row */}
        <div className="pt-4 border-t border-stone-200 flex items-center justify-between gap-3">
          <div className="text-xs text-stone-500 font-mono">
            {isAnswerSubmitted ? 'Response Evaluated' : 'Ready for Submission'}
          </div>

          {!isAnswerSubmitted ? (
            <button
              type="button"
              onClick={handleCheckAnswer}
              className="px-6 py-2.5 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs"
            >
              Submit Answer
            </button>
          ) : (
            <button
              type="button"
              onClick={handleNextExercise}
              className="px-6 py-2.5 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs flex items-center gap-1.5"
            >
              <span>{currentExerciseIndex < exercises.length - 1 ? 'Next Exercise' : 'Finish Lesson'}</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
