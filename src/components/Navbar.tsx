import React from 'react';
import { BookOpen, BarChart3, BookmarkCheck, FileText, Volume2, Cloud, Sparkles, Languages } from 'lucide-react';

export type NavTab = 'syllabus' | 'grammar' | 'dashboard' | 'notes';

interface NavbarProps {
  activeTab: NavTab;
  onTabChange: (tab: NavTab) => void;
  audioSpeed: number;
  onToggleAudioSpeed: () => void;
  isCloudConnected: boolean;
  activeCourseName: string;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  onTabChange,
  audioSpeed,
  onToggleAudioSpeed,
  isCloudConnected,
  activeCourseName,
}) => {
  const [showLangMenu, setShowLangMenu] = React.useState(false);

  return (
    <header className="border-b border-stone-200 bg-stone-50/95 sticky top-0 z-40 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Brand & Language Switcher */}
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2">
              <div className="w-9 h-9 rounded-lg bg-stone-900 text-stone-100 flex items-center justify-center font-serif text-lg font-bold border border-stone-700 shadow-sm">
                М
              </div>
              <div>
                <span className="font-serif font-bold text-stone-900 text-lg tracking-tight block leading-none">
                  Монгол Хэл
                </span>
                <span className="text-[11px] font-sans font-medium text-stone-500 tracking-wide uppercase">
                  Cyrillic Curriculum
                </span>
              </div>
            </div>

            {/* Modular Language Selector Badge */}
            <div className="relative ml-2 hidden sm:block">
              <button
                type="button"
                onClick={() => setShowLangMenu(!showLangMenu)}
                className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium rounded-full bg-stone-200/80 hover:bg-stone-200 text-stone-700 border border-stone-300 transition-colors"
                title="Modular Curriculum Selector"
              >
                <Languages className="w-3.5 h-3.5 text-stone-600" />
                <span>{activeCourseName}</span>
                <span className="text-[10px] text-stone-500 font-mono">A1–C1</span>
              </button>

              {showLangMenu && (
                <div className="absolute left-0 mt-1.5 w-64 bg-white border border-stone-200 rounded-lg shadow-lg p-2 text-xs z-50">
                  <div className="px-2 py-1 font-semibold text-stone-500 text-[10px] uppercase tracking-wider">
                    Course Registry (Modular Architecture)
                  </div>
                  <div className="p-2 rounded bg-stone-100 text-stone-900 font-medium flex items-center justify-between">
                    <span>🇲🇳 Mongolian (Cyrillic)</span>
                    <span className="text-[10px] bg-stone-800 text-stone-100 px-1.5 py-0.5 rounded">Active</span>
                  </div>
                  <div className="p-2 rounded text-stone-400 flex items-center justify-between mt-1 cursor-not-allowed">
                    <span>🇰🇿 Kazakh (Cyrillic)</span>
                    <span className="text-[10px] bg-stone-200 text-stone-500 px-1.5 py-0.5 rounded">Modular Ready</span>
                  </div>
                  <div className="p-2 rounded text-stone-400 flex items-center justify-between mt-0.5 cursor-not-allowed">
                    <span>Бур Бурят (Buryat Cyrillic)</span>
                    <span className="text-[10px] bg-stone-200 text-stone-500 px-1.5 py-0.5 rounded">Modular Ready</span>
                  </div>
                  <p className="text-[10px] text-stone-500 mt-2 px-1 leading-relaxed border-t border-stone-100 pt-1.5">
                    Engineered with extensible schemas to support additional Central Asian languages without code refactoring.
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Core Navigation Links */}
          <nav className="flex items-center space-x-1 sm:space-x-2">
            <button
              type="button"
              onClick={() => onTabChange('syllabus')}
              className={`px-3 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-colors flex items-center gap-1.5 ${
                activeTab === 'syllabus'
                  ? 'bg-stone-900 text-stone-100 shadow-sm'
                  : 'text-stone-600 hover:text-stone-900 hover:bg-stone-100'
              }`}
            >
              <BookOpen className="w-4 h-4" />
              <span>Syllabus</span>
            </button>

            <button
              type="button"
              onClick={() => onTabChange('grammar')}
              className={`px-3 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-colors flex items-center gap-1.5 ${
                activeTab === 'grammar'
                  ? 'bg-stone-900 text-stone-100 shadow-sm'
                  : 'text-stone-600 hover:text-stone-900 hover:bg-stone-100'
              }`}
            >
              <BookmarkCheck className="w-4 h-4" />
              <span>Grammar</span>
            </button>

            <button
              type="button"
              onClick={() => onTabChange('dashboard')}
              className={`px-3 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-colors flex items-center gap-1.5 ${
                activeTab === 'dashboard'
                  ? 'bg-stone-900 text-stone-100 shadow-sm'
                  : 'text-stone-600 hover:text-stone-900 hover:bg-stone-100'
              }`}
            >
              <BarChart3 className="w-4 h-4" />
              <span>Completion Stats</span>
            </button>

            <button
              type="button"
              onClick={() => onTabChange('notes')}
              className={`px-3 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-colors flex items-center gap-1.5 ${
                activeTab === 'notes'
                  ? 'bg-stone-900 text-stone-100 shadow-sm'
                  : 'text-stone-600 hover:text-stone-900 hover:bg-stone-100'
              }`}
            >
              <FileText className="w-4 h-4" />
              <span className="hidden sm:inline">Study Notes</span>
            </button>
          </nav>

          {/* Secondary Controls: Audio Speed & Cloud Sync */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onToggleAudioSpeed}
              className="inline-flex items-center gap-1 px-2.5 py-1 text-xs font-mono font-medium rounded-md border border-stone-300 bg-white hover:bg-stone-50 text-stone-700 transition-colors shadow-xs"
              title="Toggle audio pronunciation speed between normal (1.0x) and deliberate slow (0.75x) for deep phonetic focus"
            >
              <Volume2 className="w-3.5 h-3.5 text-stone-500" />
              <span>{audioSpeed}x</span>
            </button>

            <div
              className="inline-flex items-center gap-1 px-2 py-1 text-[11px] rounded-md bg-stone-100 border border-stone-200 text-stone-600"
              title={isCloudConnected ? "Cloud database active (Google Cloud Firestore)" : "Using durable local storage backup"}
            >
              <Cloud className={`w-3.5 h-3.5 ${isCloudConnected ? 'text-emerald-600' : 'text-stone-400'}`} />
              <span className="hidden md:inline font-mono">
                {isCloudConnected ? 'Firestore' : 'Local'}
              </span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
