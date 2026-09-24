import { Exercise, ExerciseOption, VocabularyItem, GrammarRule } from '../../src/types/curriculum';
import { RawLexiconItem, RawGrammarConcept } from './types';

// Deterministic exercise generation engine producing authentic interactive exercises for every lesson
export function generateExercisesForLesson(
  lessonId: string,
  lessonNumberInCourse: number,
  unitNumber: number,
  sectionNumber: number,
  cefr: 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2',
  vocabSubset: RawLexiconItem[],
  grammarRule: RawGrammarConcept,
  lessonTitle: string
): Exercise[] {
  const exercises: Exercise[] = [];

  // Pick primary vocabulary anchors for this lesson
  const v1 = vocabSubset[0] || {
    cyrillic: 'ном',
    english: 'book',
    ipa: 'nɔm',
    pos: 'noun',
    harmony: 'masculine',
    exampleCyrillic: 'Би ном уншдаг.',
    exampleEnglish: 'I read a book.'
  };
  const v2 = vocabSubset[1] || {
    cyrillic: 'сургууль',
    english: 'school',
    ipa: 'sʊrɡʊːɮ',
    pos: 'noun',
    harmony: 'masculine',
    exampleCyrillic: 'Сургууль том байна.',
    exampleEnglish: 'The school is big.'
  };
  const v3 = vocabSubset[2] || {
    cyrillic: 'багш',
    english: 'teacher',
    ipa: 'baɢʃ',
    pos: 'noun',
    harmony: 'masculine',
    exampleCyrillic: 'Багш хичээл заадаг.',
    exampleEnglish: 'The teacher teaches the lesson.'
  };
  const v4 = vocabSubset[3] || {
    cyrillic: 'гэр',
    english: 'ger / home',
    ipa: 'ɡir',
    pos: 'noun',
    harmony: 'feminine',
    exampleCyrillic: 'Гэртээ харилаа.',
    exampleEnglish: 'Returned to one\'s home.'
  };

  const isMasculine = v1.harmony === 'masculine';

  // 1. Audio Dictation (Cyrillic Transcription)
  exercises.push({
    id: `${lessonId}_ex_01`,
    type: 'AUDIO_DICTATION',
    prompt: `Listen attentively to the audio recording and transcribe the Cyrillic phrase accurately.`,
    audioText: v1.exampleCyrillic,
    slowAudioText: v1.exampleCyrillic.split(' ').join(' ... '),
    cyrillicSentence: v1.exampleCyrillic,
    englishTranslation: v1.exampleEnglish,
    correctAnswer: v1.exampleCyrillic.replace(/[.?!]/g, '').trim(),
    detailedGrammarNote: `In standard Khalkha Mongolian orthography, notice how the term "${v1.cyrillic}" adheres to ${v1.harmony} vowel harmony. The sentence follows canonical Subject-Object-Verb (SOV) order.`
  });

  // 2. Audio Comprehension (Meaning Selection)
  exercises.push({
    id: `${lessonId}_ex_02`,
    type: 'AUDIO_COMPREHENSION',
    prompt: `Listen to the spoken Mongolian statement and identify the correct analytical meaning.`,
    audioText: v2.exampleCyrillic,
    cyrillicSentence: v2.exampleCyrillic,
    englishTranslation: v2.exampleEnglish,
    options: [
      { id: 'opt_1', text: v2.exampleEnglish, isCorrect: true, explanation: 'Accurately captures the semantics and syntactic nuances of the spoken utterance.' },
      { id: 'opt_2', text: `The counterpart statement referring to ${v3.english}.`, isCorrect: false, explanation: `Incorrect subject; the speaker clearly uttered "${v2.cyrillic}".` },
      { id: 'opt_3', text: `A negative assertion denying the presence of ${v2.english}.`, isCorrect: false, explanation: 'The audio is an affirmative declarative clause without negation.' },
      { id: 'opt_4', text: `An interrogative inquiring about the location of ${v1.english}.`, isCorrect: false, explanation: 'No question particle (уу/үү/вэ/бэ) is present in the recorded sentence.' }
    ],
    detailedGrammarNote: `Listen for lexical vowel length and consonant assimilation. "${v2.cyrillic}" (${v2.ipa}) acts as the topical focus.`
  });

  // 3. Sentence Construction (SOV Syntax Builder)
  const tokens = v1.exampleCyrillic.replace(/[.?!]/g, '').split(' ');
  const shuffled = [...tokens].reverse(); // Simple reversal gives a scrambled order
  exercises.push({
    id: `${lessonId}_ex_03`,
    type: 'SENTENCE_CONSTRUCTION',
    prompt: `Construct the grammatically standard Mongolian sentence by arranging the word tiles in strict SOV syntax.`,
    englishTranslation: v1.exampleEnglish,
    wordTokens: shuffled,
    correctTokenOrder: tokens,
    cyrillicSentence: v1.exampleCyrillic,
    detailedGrammarNote: `Mongolian is a strictly head-final, left-branching language. Modifiers precede heads, direct objects precede transitive verbs, and finite predicates conclude the clause.`
  });

  // 4. Grammar Suffix Application (Harmonic Suffix Selection)
  const harmonicSuffixes = isMasculine
    ? ['-аас', '-ээс', '-оос', '-өөс']
    : ['-ээс', '-аас', '-өөс', '-оос'];
  const correctSuffix = isMasculine ? '-аас' : '-ээс';

  exercises.push({
    id: `${lessonId}_ex_04`,
    type: 'GRAMMAR_APPLICATION',
    prompt: `Attach the harmonically valid ablative case suffix ("from / out of") to the stem "${v1.cyrillic}".`,
    baseWord: v1.cyrillic,
    suffixOptions: harmonicSuffixes,
    correctSuffix: correctSuffix,
    options: harmonicSuffixes.map((suf, i) => ({
      id: `suf_${i}`,
      text: `${v1.cyrillic}${suf.replace('-', '')}`,
      isCorrect: suf === correctSuffix,
      explanation: suf === correctSuffix
        ? `Correct: "${v1.cyrillic}" is a ${v1.harmony} root and requires the harmonic matching suffix ${suf}.`
        : `Incorrect: Violates Mongolian vowel harmony principles for ${v1.harmony} roots.`
    })),
    detailedGrammarNote: `Vowel harmony in Mongolian dictates that back vowels (а, о, у) take back-vocalic suffixes, while front vowels (э, ө, ү) take front-vocalic suffixes. ${grammarRule.summary}`
  });

  // 5. Phonetic Discrimination (Acoustic Contrast)
  exercises.push({
    id: `${lessonId}_ex_05`,
    type: 'PHONETIC_DISCRIMINATION',
    prompt: `Listen and distinguish the phonemic contrast between masculine and feminine vowels in the audio prompt.`,
    audioText: `${v1.cyrillic} vs ${v4.cyrillic}`,
    options: [
      { id: 'p_1', text: `Root "${v1.cyrillic}" contains ${v1.harmony} back vowels.`, isCorrect: true, explanation: `Accurate phonological identification.` },
      { id: 'p_2', text: `Both roots share identical front-rounded vowel configurations.`, isCorrect: false, explanation: `Incorrect; Mongolian contrasts back and front vowel sets.` },
      { id: 'p_3', text: `The vowels are completely neutralized under Cyrillic stress rules.`, isCorrect: false, explanation: `Mongolian preserves vowel distinctions in initial syllables.` }
    ],
    detailedGrammarNote: `The initial syllable in Mongolian carries primary phonological prominence. Vowel quality in subsequent syllables is governed by harmony with this initial syllable.`
  });

  // 6. Translation (Cyrillic to English)
  exercises.push({
    id: `${lessonId}_ex_06`,
    type: 'TRANSLATION',
    prompt: `Translate the following authentic Mongolian sentence into English:`,
    cyrillicSentence: v3.exampleCyrillic,
    englishTranslation: v3.exampleEnglish,
    options: [
      { id: 'tr_1', text: v3.exampleEnglish, isCorrect: true },
      { id: 'tr_2', text: `The students greeted ${v3.english} warmly.`, isCorrect: false },
      { id: 'tr_3', text: `${v1.english} was purchased yesterday.`, isCorrect: false },
      { id: 'tr_4', text: `We are traveling towards ${v2.english}.`, isCorrect: false }
    ],
    detailedGrammarNote: `In this sentence, note how "${v3.cyrillic}" (${v3.pos}) forms the core thematic subject.`
  });

  // 7. Vocabulary Matching (Lexical Definition)
  exercises.push({
    id: `${lessonId}_ex_07`,
    type: 'VOCABULARY_MATCH',
    prompt: `Select the precise definition for the Mongolian term "${v1.cyrillic}" [${v1.ipa}].`,
    options: [
      { id: 'vm_1', text: `${v1.english} (${v1.pos})`, isCorrect: true, explanation: 'Accurate lexical definition.' },
      { id: 'vm_2', text: `${v2.english} (${v2.pos})`, isCorrect: false, explanation: 'Refers to another lexical concept.' },
      { id: 'vm_3', text: `${v3.english} (${v3.pos})`, isCorrect: false, explanation: 'Incorrect lexical translation.' },
      { id: 'vm_4', text: `${v4.english} (${v4.pos})`, isCorrect: false, explanation: 'Incorrect lexical translation.' }
    ],
    detailedGrammarNote: `"${v1.cyrillic}" is classified as a ${v1.pos} with ${v1.harmony} vowel harmony. Standard IPA transcription: /${v1.ipa}/.`
  });

  // 8. Reverse Translation (English to Cyrillic)
  exercises.push({
    id: `${lessonId}_ex_08`,
    type: 'TRANSLATION',
    prompt: `Choose the correct Mongolian Cyrillic rendering for: "${v4.exampleEnglish}"`,
    englishTranslation: v4.exampleEnglish,
    cyrillicSentence: v4.exampleCyrillic,
    options: [
      { id: 'rev_1', text: v4.exampleCyrillic, isCorrect: true },
      { id: 'rev_2', text: v1.exampleCyrillic, isCorrect: false },
      { id: 'rev_3', text: v2.exampleCyrillic, isCorrect: false },
      { id: 'rev_4', text: v3.exampleCyrillic, isCorrect: false }
    ],
    detailedGrammarNote: `Notice the morphological markers indicating aspect, location, and person.`
  });

  // 9. Sentence Construction 2 (Converb / Complex Clause)
  const compoundSentence = `${v1.cyrillic} аваад, ${v2.cyrillic} рүү явлаа`;
  const compoundEnglish = `Having taken the ${v1.english}, went towards the ${v2.english}.`;
  const compoundTokens = compoundSentence.split(' ');
  exercises.push({
    id: `${lessonId}_ex_09`,
    type: 'SENTENCE_CONSTRUCTION',
    prompt: `Assemble the compound clause featuring the perfective converb -аад/-ээд:`,
    englishTranslation: compoundEnglish,
    cyrillicSentence: compoundSentence,
    wordTokens: [...compoundTokens].reverse(),
    correctTokenOrder: compoundTokens,
    detailedGrammarNote: `The perfective converb -аад/-ээд marks an anterior action completed immediately prior to the matrix verb.`
  });

  // 10. Secondary Audio Dictation
  exercises.push({
    id: `${lessonId}_ex_10`,
    type: 'AUDIO_DICTATION',
    prompt: `Listen and transcribe the full conversational statement in Cyrillic:`,
    audioText: v3.exampleCyrillic,
    slowAudioText: v3.exampleCyrillic.split(' ').join(' ... '),
    cyrillicSentence: v3.exampleCyrillic,
    englishTranslation: v3.exampleEnglish,
    correctAnswer: v3.exampleCyrillic.replace(/[.?!]/g, '').trim(),
    detailedGrammarNote: `Check consonant assimilation and unaccented short vowel retention in intermediate syllables.`
  });

  // 11. Contextual Grammar Application
  exercises.push({
    id: `${lessonId}_ex_11`,
    type: 'GRAMMAR_APPLICATION',
    prompt: `Identify the syntactic role and inflectional ending used in "${v2.exampleCyrillic}".`,
    options: [
      { id: 'ga_1', text: `Demonstrates ${grammarRule.title} in declarative context.`, isCorrect: true, explanation: grammarRule.summary },
      { id: 'ga_2', text: `Employs an archaic vocative particle uncharacteristic of modern prose.`, isCorrect: false, explanation: 'The sentence uses standard contemporary modern Khalkha grammar.' },
      { id: 'ga_3', text: `Expresses counterfactual past conditionals.`, isCorrect: false, explanation: 'No counterfactual conditional morpheme (-сан бол) is present.' }
    ],
    detailedGrammarNote: `${grammarRule.cyrillicTitle}: ${grammarRule.summary}`
  });

  return exercises;
}
