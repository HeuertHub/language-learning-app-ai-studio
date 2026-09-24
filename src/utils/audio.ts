/**
 * Robust Mongolian Cyrillic Audio System
 * Uses Web Speech Synthesis with targeted Cyrillic pitch/rate controls,
 * coupled with an Acoustic Phonetic Web Audio formant synthesis fallback.
 */

let audioCtx: AudioContext | null = null;

function getAudioContext(): AudioContext | null {
  if (typeof window === 'undefined') return null;
  if (!audioCtx) {
    const AudioContextClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (AudioContextClass) {
      audioCtx = new AudioContextClass();
    }
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// Phonetic formant lookup for distinctive Mongolian vowels (F1, F2)
const VOWEL_FORMANTS: Record<string, [number, number]> = {
  'а': [750, 1150],
  'э': [520, 1850],
  'и': [280, 2250],
  'о': [500, 920],
  'у': [320, 800],
  'ө': [480, 1520], // Mongolian front rounded open-mid [œ]
  'ү': [340, 1680], // Mongolian near-close front rounded [ʏ]
  'ы': [380, 1400],
  'я': [300, 2100],
  'е': [300, 2000],
  'ё': [450, 950],
  'ю': [320, 1500],
};

/**
 * Synthesizes acoustic phonetic formant tones for letters when speech synthesis voice isn't present
 */
function playAcousticFallback(text: string, rate: number = 1.0) {
  const ctx = getAudioContext();
  if (!ctx) return;

  const clean = text.toLowerCase().trim();
  const char = clean.charAt(0);
  const formants = VOWEL_FORMANTS[char] || [450, 1400];
  const duration = (0.45 / rate);

  const now = ctx.currentTime;
  const masterGain = ctx.createGain();
  masterGain.gain.setValueAtTime(0.001, now);
  masterGain.gain.exponentialRampToValueAtTime(0.18, now + 0.04);
  masterGain.gain.exponentialRampToValueAtTime(0.001, now + duration);
  masterGain.connect(ctx.destination);

  // Formant 1
  const osc1 = ctx.createOscillator();
  osc1.type = 'sine';
  osc1.frequency.setValueAtTime(formants[0], now);
  osc1.connect(masterGain);
  osc1.start(now);
  osc1.stop(now + duration);

  // Formant 2
  const osc2 = ctx.createOscillator();
  osc2.type = 'triangle';
  osc2.frequency.setValueAtTime(formants[1], now);
  const gain2 = ctx.createGain();
  gain2.gain.value = 0.5;
  osc2.connect(gain2);
  gain2.connect(masterGain);
  osc2.start(now);
  osc2.stop(now + duration);
}

/**
 * Speaks a Mongolian phrase or word using Web Speech Synthesis.
 * Falls back to acoustic formant synthesis if speech synthesis is unavailable.
 */
export function playMongolianAudio(
  text: string,
  rate: number = 1.0,
  onStart?: () => void,
  onEnd?: () => void
): void {
  if (typeof window === 'undefined') return;

  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel(); // cancel any active speech

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = rate; // 1.0 or 0.75
    utterance.pitch = 1.0;

    // Detect best voice: look for Mongolian 'mn', or Cyrillic-capable voice
    const voices = window.speechSynthesis.getVoices();
    const mnVoice = voices.find((v) => v.lang.startsWith('mn') || v.lang.includes('Mongol'));
    const ruVoice = voices.find((v) => v.lang.startsWith('ru'));
    const fallbackCyrillic = voices.find((v) => v.lang.includes('RU') || v.lang.includes('BG') || v.lang.includes('UK'));

    if (mnVoice) {
      utterance.voice = mnVoice;
      utterance.lang = mnVoice.lang;
    } else if (ruVoice) {
      utterance.voice = ruVoice;
      utterance.lang = 'ru-RU';
    } else if (fallbackCyrillic) {
      utterance.voice = fallbackCyrillic;
      utterance.lang = fallbackCyrillic.lang;
    } else {
      utterance.lang = 'mn-MN';
    }

    if (onStart) utterance.onstart = onStart;
    utterance.onend = () => {
      if (onEnd) onEnd();
    };
    utterance.onerror = () => {
      // Fallback to acoustic synthesis
      playAcousticFallback(text, rate);
      if (onEnd) onEnd();
    };

    window.speechSynthesis.speak(utterance);

    // Some browsers have bug where onstart doesn't fire promptly
    if (onStart) onStart();
    const estTimeMs = Math.max(800, (text.length * 90) / rate);
    setTimeout(() => {
      if (onEnd) onEnd();
    }, estTimeMs);
  } else {
    playAcousticFallback(text, rate);
    if (onStart) onStart();
    setTimeout(() => {
      if (onEnd) onEnd();
    }, 600);
  }
}
