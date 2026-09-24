import React from 'react';

interface CyrillicKeyboardProps {
  onInsertChar: (char: string) => void;
  onBackspace: () => void;
  className?: string;
}

// Special Mongolian Cyrillic characters highlighted, plus quick access layout
const SPECIAL_MONGOLIAN = ['ө', 'ү', 'ё', 'ъ', 'ь', 'й', 'ж', 'з', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я'];

const FULL_ALPHABET_ROW1 = ['ф', 'ц', 'у', 'ж', 'э', 'н', 'г', 'ш', 'щ', 'з', 'к', 'ъ'];
const FULL_ALPHABET_ROW2 = ['й', 'ы', 'б', 'ө', 'а', 'х', 'р', 'о', 'л', 'д', 'п'];
const FULL_ALPHABET_ROW3 = ['я', 'ч', 'ё', 'с', 'м', 'и', 'т', 'ь', 'в', 'ю', 'ү'];

export const CyrillicKeyboard: React.FC<CyrillicKeyboardProps> = ({
  onInsertChar,
  onBackspace,
  className = '',
}) => {
  const [showFull, setShowFull] = React.useState(false);

  return (
    <div className={`border border-stone-200 bg-stone-100/90 rounded-xl p-2.5 shadow-sm text-stone-800 ${className}`}>
      <div className="flex items-center justify-between mb-2 text-xs font-medium text-stone-600">
        <span className="flex items-center gap-1.5">
          <span className="inline-block w-2 h-2 rounded-full bg-amber-600"></span>
          <span>Cyrillic Script Input Assistant</span>
        </span>
        <button
          type="button"
          onClick={() => setShowFull(!showFull)}
          className="text-xs text-stone-700 hover:text-stone-950 underline underline-offset-2"
        >
          {showFull ? 'Show Essential Letters' : 'Show Full Keyboard'}
        </button>
      </div>

      {!showFull ? (
        <div className="flex flex-wrap gap-1.5 items-center">
          {SPECIAL_MONGOLIAN.map((char) => (
            <button
              key={char}
              type="button"
              onClick={() => onInsertChar(char)}
              className={`min-w-[34px] h-[34px] px-2 text-sm font-semibold rounded-md border transition-all active:scale-95 ${
                char === 'ө' || char === 'ү'
                  ? 'bg-amber-100/90 border-amber-300 text-amber-900 shadow-sm hover:bg-amber-200'
                  : 'bg-white border-stone-300 text-stone-800 hover:bg-stone-50'
              }`}
              title={`Insert letter ${char} (${char.toUpperCase()})`}
            >
              {char}
            </button>
          ))}
          <button
            type="button"
            onClick={onBackspace}
            className="min-w-[44px] h-[34px] px-2.5 text-xs font-medium rounded-md border border-stone-300 bg-stone-200 hover:bg-stone-300 text-stone-700 active:scale-95"
            title="Backspace"
          >
            ⌫
          </button>
        </div>
      ) : (
        <div className="space-y-1.5">
          <div className="flex justify-center gap-1">
            {FULL_ALPHABET_ROW1.map((char) => (
              <button
                key={char}
                type="button"
                onClick={() => onInsertChar(char)}
                className="w-7 h-8 text-xs font-semibold rounded border border-stone-300 bg-white hover:bg-stone-50 active:scale-95 text-stone-800"
              >
                {char}
              </button>
            ))}
          </div>
          <div className="flex justify-center gap-1">
            {FULL_ALPHABET_ROW2.map((char) => (
              <button
                key={char}
                type="button"
                onClick={() => onInsertChar(char)}
                className={`w-7 h-8 text-xs font-semibold rounded border active:scale-95 ${
                  char === 'ө'
                    ? 'bg-amber-100 border-amber-300 text-amber-900 font-bold'
                    : 'border-stone-300 bg-white hover:bg-stone-50 text-stone-800'
                }`}
              >
                {char}
              </button>
            ))}
          </div>
          <div className="flex justify-center gap-1">
            {FULL_ALPHABET_ROW3.map((char) => (
              <button
                key={char}
                type="button"
                onClick={() => onInsertChar(char)}
                className={`w-7 h-8 text-xs font-semibold rounded border active:scale-95 ${
                  char === 'ү'
                    ? 'bg-amber-100 border-amber-300 text-amber-900 font-bold'
                    : 'border-stone-300 bg-white hover:bg-stone-50 text-stone-800'
                }`}
              >
                {char}
              </button>
            ))}
            <button
              type="button"
              onClick={onBackspace}
              className="px-2 h-8 text-xs font-medium rounded border border-stone-300 bg-stone-200 hover:bg-stone-300 text-stone-700 active:scale-95"
            >
              ⌫
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
