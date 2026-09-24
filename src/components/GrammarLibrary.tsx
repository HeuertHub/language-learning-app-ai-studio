import React, { useState } from 'react';
import type { GrammarRule } from '../types/curriculum';
import { playMongolianAudio } from '../utils/audio';
import { Volume2, BookOpen, Search, Layers, Sparkles, Filter, ChevronDown } from 'lucide-react';

interface GrammarLibraryProps {
  rules: GrammarRule[];
  audioSpeed: number;
}

// 35 Cyrillic letters with IPA and examples
const CYRILLIC_ALPHABET = [
  { letter: 'А а', ipa: '[a]', name: 'а', desc: 'Open back unrounded (masculine)' },
  { letter: 'Б б', ipa: '[p/b]', name: 'бэ', desc: 'Voiced bilabial plosive' },
  { letter: 'В в', ipa: '[w/v]', name: 'вэ', desc: 'Labiodental approximant' },
  { letter: 'Г г', ipa: '[ɡ/ɢ]', name: 'гэ', desc: 'Velar / uvular stop' },
  { letter: 'Д д', ipa: '[t/d]', name: 'дэ', desc: 'Alveolar stop' },
  { letter: 'Е е', ipa: '[jɛ/jo]', name: 'е', desc: 'Iotated front vowel' },
  { letter: 'Ё ё', ipa: '[jɔ]', name: 'ё', desc: 'Iotated back rounded vowel' },
  { letter: 'Ж ж', ipa: '[t͡ʃ/d͡ʒ]', name: 'жэ', desc: 'Post-alveolar affricate' },
  { letter: 'З з', ipa: '[t͡s/d͡z]', name: 'зэ', desc: 'Alveolar affricate' },
  { letter: 'И и', ipa: '[i]', name: 'и', desc: 'Close front neutral vowel' },
  { letter: 'Й й', ipa: '[i̯]', name: 'хагас и', desc: 'Palatal glide / diphthong maker' },
  { letter: 'К к', ipa: '[kʰ]', name: 'ка', desc: 'Aspirated voiceless velar stop' },
  { letter: 'Л л', ipa: '[ɬ/ɮ]', name: 'эл', desc: 'Lateral fricative (distinct Mongolian l)' },
  { letter: 'М м', ipa: '[m]', name: 'эм', desc: 'Bilabial nasal' },
  { letter: 'Н н', ipa: '[n/ŋ]', name: 'эн', desc: 'Alveolar nasal / velar nasal' },
  { letter: 'О о', ipa: '[ɔ]', name: 'о', desc: 'Open-mid back rounded (masculine)' },
  { letter: 'Ө ө', ipa: '[œ]', name: 'ө', desc: 'Open-mid front rounded (unique feminine)' },
  { letter: 'П п', ipa: '[pʰ]', name: 'пэ', desc: 'Aspirated voiceless bilabial stop' },
  { letter: 'Р р', ipa: '[r]', name: 'эр', desc: 'Alveolar trill / tap' },
  { letter: 'С с', ipa: '[s]', name: 'эс', desc: 'Voiceless alveolar fricative' },
  { letter: 'Т т', ipa: '[tʰ]', name: 'тэ', desc: 'Aspirated alveolar stop' },
  { letter: 'У у', ipa: '[ʊ]', name: 'у', desc: 'Near-close back rounded (masculine)' },
  { letter: 'Ү ү', ipa: '[ʏ]', name: 'ү', desc: 'Near-close front rounded (unique feminine)' },
  { letter: 'Ф ф', ipa: '[f]', name: 'фэ', desc: 'Voiceless labiodental fricative' },
  { letter: 'Х х', ipa: '[x]', name: 'хэ', desc: 'Voiceless velar fricative' },
  { letter: 'Ц ц', ipa: '[t͡sʰ]', name: 'цэ', desc: 'Aspirated alveolar affricate' },
  { letter: 'Ч ч', ipa: '[t͡ʃʰ]', name: 'чэ', desc: 'Aspirated post-alveolar affricate' },
  { letter: 'Ш ш', ipa: '[ʃ]', name: 'ша', desc: 'Voiceless postalveolar fricative' },
  { letter: 'Щ щ', ipa: '[ʃt͡ʃ]', name: 'ща', desc: 'In loanwords only' },
  { letter: 'Ъ ъ', ipa: '[-]', name: 'хатуугийн тэмдэг', desc: 'Hard sign (blocks palatalization)' },
  { letter: 'Ы ы', ipa: '[iː/ɨ]', name: 'эр үгийн ы', desc: 'Masculine long i / central unrounded' },
  { letter: 'Ь ь', ipa: '[ʲ]', name: 'зөөлний тэмдэг', desc: 'Soft sign (palatalizes preceding consonant)' },
  { letter: 'Э э', ipa: '[ɛ]', name: 'э', desc: 'Open-mid front unrounded (feminine)' },
  { letter: 'Ю ю', ipa: '[jʊ/jʏ]', name: 'ю', desc: 'Iotated rounded vowel' },
  { letter: 'Я я', ipa: '[ja]', name: 'я', desc: 'Iotated open back vowel' },
];

export const GrammarLibrary: React.FC<GrammarLibraryProps> = ({ rules, audioSpeed }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeSubTab, setActiveSubTab] = useState<'rules' | 'cases' | 'alphabet'>('rules');

  const filteredRules = rules.filter(
    (r) =>
      r.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      r.cyrillicTitle.toLowerCase().includes(searchTerm.toLowerCase()) ||
      r.summary.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-8">
      {/* Header */}
      <div className="border-b border-stone-200 pb-5">
        <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-stone-100 border border-stone-200 text-stone-600 text-[11px] font-mono mb-2">
          <span>Grammatical Reference Compendium</span>
          <span>•</span>
          <span>Morphology & Syntax</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900">
          Mongolian Grammar & Phonology Handbook
        </h1>
        <p className="text-stone-600 text-xs sm:text-sm mt-1 max-w-2xl">
          Exhaustive academic reference covering vowel harmony, the seven grammatical cases, verbal aspect, and the 35 Cyrillic phonemes.
        </p>

        {/* Sub-tabs & Search */}
        <div className="mt-6 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-1 bg-stone-100 p-1 rounded-lg border border-stone-200">
            <button
              type="button"
              onClick={() => setActiveSubTab('rules')}
              className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${
                activeSubTab === 'rules' ? 'bg-white text-stone-900 shadow-xs' : 'text-stone-600 hover:text-stone-900'
              }`}
            >
              Core Principles ({rules.length})
            </button>
            <button
              type="button"
              onClick={() => setActiveSubTab('cases')}
              className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${
                activeSubTab === 'cases' ? 'bg-white text-stone-900 shadow-xs' : 'text-stone-600 hover:text-stone-900'
              }`}
            >
              The 7 Grammatical Cases Matrix
            </button>
            <button
              type="button"
              onClick={() => setActiveSubTab('alphabet')}
              className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${
                activeSubTab === 'alphabet' ? 'bg-white text-stone-900 shadow-xs' : 'text-stone-600 hover:text-stone-900'
              }`}
            >
              35 Cyrillic Letters & Audio
            </button>
          </div>

          {activeSubTab === 'rules' && (
            <div className="relative w-full sm:w-64">
              <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
              <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search grammar topics..."
                className="w-full pl-8 pr-3 py-1.5 rounded-md border border-stone-300 text-xs bg-white focus:outline-hidden focus:ring-1 focus:ring-stone-800"
              />
            </div>
          )}
        </div>
      </div>

      {/* Subtab 1: Core Principles & Rules */}
      {activeSubTab === 'rules' && (
        <div className="space-y-6">
          {filteredRules.map((rule) => (
            <div
              key={rule.id}
              className="bg-white border border-stone-200 rounded-xl p-6 shadow-2xs space-y-4"
            >
              <div className="border-b border-stone-100 pb-3">
                <div className="flex items-center justify-between">
                  <h2 className="text-lg font-serif font-bold text-stone-900">
                    {rule.title}
                  </h2>
                  <span className="font-serif italic text-stone-500 text-sm">
                    {rule.cyrillicTitle}
                  </span>
                </div>
                <p className="text-xs text-stone-600 mt-1">
                  {rule.summary}
                </p>
              </div>

              {rule.formula && (
                <div className="bg-stone-50 border border-stone-200 rounded-lg p-3 text-xs font-mono text-stone-800">
                  <span className="font-bold text-stone-500 uppercase mr-2 text-[10px]">Formula:</span>
                  <span>{rule.formula}</span>
                </div>
              )}

              <p className="text-xs sm:text-sm text-stone-700 leading-relaxed">
                {rule.explanation}
              </p>

              {rule.examples.length > 0 && (
                <div className="space-y-2 pt-2">
                  <div className="text-[11px] font-mono uppercase tracking-wider text-stone-500 font-semibold">
                    Illustrative Morphological Examples:
                  </div>
                  <div className="space-y-2">
                    {rule.examples.map((ex, idx) => (
                      <div
                        key={idx}
                        className="bg-stone-50/60 border border-stone-200 rounded-lg p-3 text-xs flex items-start justify-between gap-3"
                      >
                        <div className="space-y-0.5">
                          <div className="font-serif font-bold text-stone-900 text-sm">
                            {ex.cyrillic}
                          </div>
                          <div className="text-stone-700">
                            {ex.english}
                          </div>
                          <div className="text-stone-500 text-[11px] font-mono">
                            {ex.breakdown}
                          </div>
                        </div>

                        <button
                          type="button"
                          onClick={() => playMongolianAudio(ex.cyrillic, audioSpeed)}
                          className="p-1.5 rounded-md hover:bg-stone-200 text-stone-700 transition-colors shrink-0"
                          title="Speak phrase"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Subtab 2: The 7 Cases Matrix */}
      {activeSubTab === 'cases' && (
        <div className="bg-white border border-stone-200 rounded-xl overflow-hidden shadow-2xs">
          <div className="p-5 border-b border-stone-200 bg-stone-50">
            <h2 className="font-serif font-bold text-stone-900 text-lg">
              The Seven Mongolian Grammatical Cases (Нэрийн 7 тийн ялгал)
            </h2>
            <p className="text-xs text-stone-600 mt-1">
              Every nominal modifier in Mongolian is governed through this agglutinative declension matrix.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="border-b border-stone-200 bg-stone-100 font-mono text-[11px] uppercase tracking-wider text-stone-600">
                  <th className="p-3">Case Name</th>
                  <th className="p-3">Cyrillic Name</th>
                  <th className="p-3">Harmonic Suffixes</th>
                  <th className="p-3">Semantic Function</th>
                  <th className="p-3">Example</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100 font-serif">
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">1. Nominative</td>
                  <td className="p-3 text-stone-700">Нэрлэх</td>
                  <td className="p-3 font-mono font-bold text-stone-900">Ø (unmarked)</td>
                  <td className="p-3 font-sans text-stone-600">Subject, general direct object, dictionary base form</td>
                  <td className="p-3 text-stone-900">ном (book), гэр (ger)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">2. Genitive</td>
                  <td className="p-3 text-stone-700">Харьяалах</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-ын, -ийн, -ны, -ний, -н</td>
                  <td className="p-3 font-sans text-stone-600">Possession, relationship, origin ("of")</td>
                  <td className="p-3 text-stone-900">номын (of book), гэрийн (of home)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">3. Accusative</td>
                  <td className="p-3 text-stone-700">Заах</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-ыг, -ийг, -г</td>
                  <td className="p-3 font-sans text-stone-600">Definite/specific direct object</td>
                  <td className="p-3 text-stone-900">номыг (the book), гэрийг (the ger)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">4. Dative-Locative</td>
                  <td className="p-3 text-stone-700">Өгөх орших</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-д, -т</td>
                  <td className="p-3 font-sans text-stone-600">Location ("in/at"), destination ("to"), recipient ("for")</td>
                  <td className="p-3 text-stone-900">гэрт (at home), хотод (in city)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">5. Ablative</td>
                  <td className="p-3 text-stone-700">Гарах</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-аас, -ээс, -оос, -өөс</td>
                  <td className="p-3 font-sans text-stone-600">Point of departure ("from"), material, comparison ("than")</td>
                  <td className="p-3 text-stone-900">гэрээс (from home), номоос (from book)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">6. Instrumental</td>
                  <td className="p-3 text-stone-700">Үйлдэх</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-аар, -ээр, -оор, -өөр</td>
                  <td className="p-3 font-sans text-stone-600">Instrument ("with/by"), transit vehicle, language</td>
                  <td className="p-3 text-stone-900">монголоор (in Mongolian), машинаар (by car)</td>
                </tr>
                <tr className="hover:bg-stone-50">
                  <td className="p-3 font-medium">7. Comitative</td>
                  <td className="p-3 text-stone-700">Хамтрах</td>
                  <td className="p-3 font-mono font-bold text-amber-800">-тай, -тэй, -той</td>
                  <td className="p-3 font-sans text-stone-600">Accompaniment ("with"), possession ("having/to have")</td>
                  <td className="p-3 text-stone-900">найзтай (with friend), номтой (has a book)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Subtab 3: Cyrillic Alphabet Table */}
      {activeSubTab === 'alphabet' && (
        <div className="bg-white border border-stone-200 rounded-xl p-6 shadow-2xs space-y-4">
          <div>
            <h2 className="font-serif font-bold text-stone-900 text-lg">
              The 35 Mongolian Cyrillic Letters & Audio Pronunciations
            </h2>
            <p className="text-xs text-stone-600 mt-1">
              Click the audio icon to listen to the accurate phonetic pronunciation of each letter.
            </p>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
            {CYRILLIC_ALPHABET.map((item) => (
              <div
                key={item.letter}
                className={`p-3 rounded-lg border flex flex-col justify-between ${
                  item.letter.includes('Ө') || item.letter.includes('Ү')
                    ? 'border-amber-300 bg-amber-50/50'
                    : 'border-stone-200 bg-stone-50/40'
                }`}
              >
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-lg font-serif font-bold text-stone-900">
                      {item.letter}
                    </span>
                    <button
                      type="button"
                      onClick={() => playMongolianAudio(item.name, audioSpeed)}
                      className="p-1 rounded hover:bg-stone-200 text-stone-700 transition-colors"
                      title={`Pronounce ${item.letter}`}
                    >
                      <Volume2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <div className="text-[11px] font-mono text-stone-500">
                    {item.ipa}
                  </div>
                  <div className="text-xs font-serif italic text-stone-700 mt-0.5">
                    "{item.name}"
                  </div>
                </div>
                <div className="text-[10px] text-stone-500 mt-2 line-clamp-2">
                  {item.desc}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
