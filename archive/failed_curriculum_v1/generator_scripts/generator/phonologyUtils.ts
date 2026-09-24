import { RawLexiconItem } from './types';

// Helper to determine vowel harmony of Mongolian word
export function getMongolianVowelHarmony(word: string): 'masculine' | 'feminine' | 'neutral' {
  const lower = word.toLowerCase();
  const hasMasculine = /[аоуяёы]/.test(lower);
  const hasFeminine = /[эөүе]/.test(lower);

  if (hasMasculine && !hasFeminine) return 'masculine';
  if (hasFeminine && !hasMasculine) return 'feminine';
  if (hasMasculine && hasFeminine) return 'masculine'; // Usually governed by initial syllable in modern loans
  return 'neutral'; // Only 'и'
}

// Helper to generate approximate IPA for Mongolian Cyrillic
export function generateApproximateIPA(word: string): string {
  const map: Record<string, string> = {
    'а': 'a', 'б': 'p', 'в': 'w', 'г': 'ɡ', 'д': 't', 'е': 'jɛ', 'ё': 'jɔ',
    'ж': 't͡ʃ', 'з': 't͡s', 'и': 'i', 'й': 'i̯', 'к': 'kʰ', 'л': 'ɮ', 'м': 'm',
    'н': 'n', 'о': 'ɔ', 'ө': 'œ', 'п': 'pʰ', 'р': 'r', 'с': 's', 'т': 'tʰ',
    'у': 'ʊ', 'ү': 'ʏ', 'ф': 'f', 'х': 'x', 'ц': 't͡sʰ', 'ч': 't͡ʃʰ', 'ш': 'ʃ',
    'щ': 'ʃt͡ʃ', 'ъ': '', 'ы': 'iː', 'ь': 'ʲ', 'э': 'ɛ', 'ю': 'jʊ', 'я': 'ja'
  };

  let ipa = '';
  for (const ch of word.toLowerCase()) {
    ipa += map[ch] || ch;
  }
  return `[${ipa}]`;
}
