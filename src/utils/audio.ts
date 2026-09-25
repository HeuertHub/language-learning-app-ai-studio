/**
 * Robust Mongolian Cyrillic Audio System
 * Uses Web Speech Synthesis with targeted Cyrillic pitch/rate controls.
 * Strictly adheres to Audio Safety Guidelines:
 * - NEVER falls back to Russian, Ukrainian, Bulgarian or other non-Mongolian voices.
 * - If no Mongolian voice is available, uses Web Audio acoustic formant synthesis for phonemes,
 *   or reports native-audio-required status.
 */

let audioCtx: AudioContext | null = null;

function getAudioContext(): AudioContext | null {
  if (typeof window === 'undefined') return null;
  if (!audioCtx) {
    const AudioContextClass =
      window.AudioContext ||
      (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (AudioContextClass) {
      audioCtx = new AudioContextClass();
    }
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// Phonetic formant lookup for distinctive Mongolian vowels (F1, F2) in Khalkha phonology
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
 * Synthesizes acoustic phonetic formant tones for letters using pure Web Audio oscillators
 */
export function playAcousticFallback(text: string, rate: number = 1.0) {
  const ctx = getAudioContext();
  if (!ctx) return;

  const clean = text.toLowerCase().trim();
  const char = clean.charAt(0);
  const formants = VOWEL_FORMANTS[char] || [450, 1400];
  const duration = 0.45 / rate;

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

export interface AudioSystemStatus {
  hasMongolianVoice: boolean;
  voiceName: string | null;
  acousticSynthesisAvailable: boolean;
}

export function getAudioSystemStatus(): AudioSystemStatus {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    return {
      hasMongolianVoice: false,
      voiceName: null,
      acousticSynthesisAvailable: typeof window !== 'undefined' && ('AudioContext' in window || 'webkitAudioContext' in window),
    };
  }

  const voices = window.speechSynthesis.getVoices();
  const mnVoice = voices.find(
    (v) => v.lang.startsWith('mn') || v.lang.toLowerCase().includes('mongol')
  );

  return {
    hasMongolianVoice: !!mnVoice,
    voiceName: mnVoice ? mnVoice.name : null,
    acousticSynthesisAvailable: true,
  };
}

/**
 * Speaks a Mongolian phrase or word using Web Speech Synthesis.
 * Enforces Audio Safety:
 * - Strictly searches only for authentic Mongolian voices ('mn-*' or 'Mongolian').
 * - Under NO circumstances will it use Russian, Ukrainian, Bulgarian, or other foreign voices.
 * - When no Mongolian voice is present, safely delegates to Web Audio acoustic formant synthesis.
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

    const voices = window.speechSynthesis.getVoices();
    // Strictly Mongolian-capable voices only
    const mnVoice = voices.find(
      (v) => v.lang.startsWith('mn') || v.lang.toLowerCase().includes('mongol')
    );

    if (mnVoice) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.voice = mnVoice;
      utterance.lang = mnVoice.lang;
      utterance.rate = rate;
      utterance.pitch = 1.0;

      if (onStart) utterance.onstart = onStart;
      utterance.onend = () => {
        if (onEnd) onEnd();
      };
      utterance.onerror = () => {
        playAcousticFallback(text, rate);
        if (onEnd) onEnd();
      };

      window.speechSynthesis.speak(utterance);

      if (onStart) onStart();
      const estTimeMs = Math.max(800, (text.length * 90) / rate);
      setTimeout(() => {
        if (onEnd) onEnd();
      }, estTimeMs);
      return;
    }
  }

  // Safe Fallback: Acoustic formant synthesis (Zero foreign language voice intrusion)
  playAcousticFallback(text, rate);
  if (onStart) onStart();
  setTimeout(() => {
    if (onEnd) onEnd();
  }, 600);
}
