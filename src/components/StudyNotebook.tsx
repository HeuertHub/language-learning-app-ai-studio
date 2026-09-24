import React, { useState } from 'react';
import type { UserStudyNote } from '../types/curriculum';
import { CyrillicKeyboard } from './CyrillicKeyboard';
import { Plus, Trash2, Tag, BookMarked, Search, Calendar } from 'lucide-react';

interface StudyNotebookProps {
  notes: UserStudyNote[];
  userId: string;
  onSaveNote: (note: UserStudyNote) => Promise<void>;
  onDeleteNote: (noteId: string) => Promise<void>;
}

export const StudyNotebook: React.FC<StudyNotebookProps> = ({
  notes,
  userId,
  onSaveNote,
  onDeleteNote,
}) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState('');
  const [cyrillicSnippet, setCyrillicSnippet] = useState('');
  const [content, setContent] = useState('');
  const [tagInput, setTagInput] = useState('cases');
  const [searchFilter, setSearchFilter] = useState('');
  const [activeInputField, setActiveInputField] = useState<'snippet' | 'content'>('snippet');

  const handleCreateNew = () => {
    setTitle('');
    setCyrillicSnippet('');
    setContent('');
    setTagInput('vowel-harmony');
    setIsEditing(true);
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return;

    const tags = tagInput
      .split(',')
      .map((t) => t.trim().toLowerCase().replace(/^#/, ''))
      .filter(Boolean);

    const newNote: UserStudyNote = {
      id: `note_${Date.now()}`,
      userId,
      title: title.trim(),
      cyrillicSnippet: cyrillicSnippet.trim(),
      content: content.trim(),
      tags,
      createdAt: new Date().toISOString(),
    };

    await onSaveNote(newNote);
    setIsEditing(false);
  };

  const handleInsertCyrillic = (char: string) => {
    if (activeInputField === 'snippet') {
      setCyrillicSnippet((prev) => prev + char);
    } else {
      setContent((prev) => prev + char);
    }
  };

  const handleBackspaceCyrillic = () => {
    if (activeInputField === 'snippet') {
      setCyrillicSnippet((prev) => prev.slice(0, -1));
    } else {
      setContent((prev) => prev.slice(0, -1));
    }
  };

  const filteredNotes = notes.filter(
    (n) =>
      n.title.toLowerCase().includes(searchFilter.toLowerCase()) ||
      n.content.toLowerCase().includes(searchFilter.toLowerCase()) ||
      (n.cyrillicSnippet && n.cyrillicSnippet.toLowerCase().includes(searchFilter.toLowerCase())) ||
      n.tags.some((t) => t.toLowerCase().includes(searchFilter.toLowerCase()))
  );

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 space-y-6">
      {/* Header */}
      <div className="border-b border-stone-200 pb-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-stone-100 border border-stone-200 text-stone-600 text-[11px] font-mono mb-1">
            <span>Cloud Repository</span>
            <span>•</span>
            <span>Personal Annotations</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900">
            Learner Linguistic Study Notebook
          </h1>
          <p className="text-stone-600 text-xs sm:text-sm mt-0.5">
            Store personalized grammatical observations, Cyrillic syntax notes, and mnemonics in Google Cloud Firestore.
          </p>
        </div>

        {!isEditing && (
          <button
            type="button"
            onClick={handleCreateNew}
            className="inline-flex items-center gap-1.5 px-4 py-2 bg-stone-900 text-stone-100 hover:bg-stone-800 rounded-md text-xs font-medium transition-colors shadow-xs shrink-0 self-start sm:self-auto"
          >
            <Plus className="w-4 h-4" />
            <span>New Study Note</span>
          </button>
        )}
      </div>

      {/* Editor Modal/Form */}
      {isEditing && (
        <form onSubmit={handleSave} className="bg-white border border-stone-300 rounded-xl p-6 shadow-sm space-y-4">
          <div className="flex items-center justify-between border-b border-stone-100 pb-3">
            <h2 className="font-serif font-bold text-stone-900 text-lg">
              Draft Linguistic Annotation
            </h2>
            <button
              type="button"
              onClick={() => setIsEditing(false)}
              className="text-xs text-stone-500 hover:text-stone-800"
            >
              Cancel
            </button>
          </div>

          <div>
            <label className="block text-xs font-medium text-stone-700 mb-1">
              Note Title:
            </label>
            <input
              type="text"
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Quad-harmonic variations of the Ablative Case"
              className="w-full text-sm px-3 py-2 rounded-md border border-stone-300 bg-white focus:ring-1 focus:ring-stone-800 focus:outline-hidden"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-stone-700 mb-1">
              Target Cyrillic Phrase or Stem (Optional):
            </label>
            <input
              type="text"
              value={cyrillicSnippet}
              onFocus={() => setActiveInputField('snippet')}
              onChange={(e) => setCyrillicSnippet(e.target.value)}
              placeholder="e.g. Улаанбаатараас, сурч байна"
              className="w-full font-serif text-base px-3 py-2 rounded-md border border-stone-300 bg-white focus:ring-1 focus:ring-stone-800 focus:outline-hidden"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-stone-700 mb-1">
              Linguistic Explanation & Rule Reflection:
            </label>
            <textarea
              required
              rows={4}
              value={content}
              onFocus={() => setActiveInputField('content')}
              onChange={(e) => setContent(e.target.value)}
              placeholder="Record your grammatical breakdown, vowel patterns, or observations..."
              className="w-full text-sm px-3 py-2 rounded-md border border-stone-300 bg-white focus:ring-1 focus:ring-stone-800 focus:outline-hidden"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-stone-700 mb-1">
              Categorical Tags (comma-separated):
            </label>
            <input
              type="text"
              value={tagInput}
              onChange={(e) => setTagInput(e.target.value)}
              placeholder="cases, vowel-harmony, converb, ger-culture"
              className="w-full text-xs font-mono px-3 py-2 rounded-md border border-stone-300 bg-white focus:ring-1 focus:ring-stone-800 focus:outline-hidden"
            />
          </div>

          {/* Cyrillic keyboard assistance */}
          <div className="pt-2">
            <div className="text-[11px] text-stone-500 mb-1">
              Click to insert Cyrillic letters into active field ({activeInputField === 'snippet' ? 'Cyrillic Phrase' : 'Explanation'}):
            </div>
            <CyrillicKeyboard
              onInsertChar={handleInsertCyrillic}
              onBackspace={handleBackspaceCyrillic}
            />
          </div>

          <div className="pt-3 border-t border-stone-100 flex justify-end gap-2">
            <button
              type="button"
              onClick={() => setIsEditing(false)}
              className="px-4 py-2 border border-stone-300 text-stone-700 text-xs font-medium rounded-md hover:bg-stone-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-5 py-2 bg-stone-900 text-stone-100 text-xs font-medium rounded-md hover:bg-stone-800 shadow-xs"
            >
              Save to Cloud Repository
            </button>
          </div>
        </form>
      )}

      {/* Notes List with Search */}
      <div className="space-y-4">
        <div className="flex items-center justify-between gap-4">
          <div className="relative flex-1 max-w-sm">
            <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
            <input
              type="text"
              value={searchFilter}
              onChange={(e) => setSearchFilter(e.target.value)}
              placeholder="Search personal notes..."
              className="w-full pl-8 pr-3 py-1.5 rounded-md border border-stone-300 text-xs bg-white focus:outline-hidden focus:ring-1 focus:ring-stone-800"
            />
          </div>
          <span className="text-xs text-stone-500 font-mono">
            {filteredNotes.length} {filteredNotes.length === 1 ? 'Note' : 'Notes'}
          </span>
        </div>

        {filteredNotes.length === 0 ? (
          <div className="bg-white border border-stone-200 rounded-xl p-8 text-center text-stone-500 text-xs space-y-2">
            <BookMarked className="w-8 h-8 text-stone-300 mx-auto" />
            <p>No study notes found. Create your first note to record personal grammatical insights.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredNotes.map((note) => (
              <div
                key={note.id}
                className="bg-white border border-stone-200 rounded-xl p-5 shadow-2xs flex flex-col justify-between space-y-3"
              >
                <div>
                  <div className="flex items-start justify-between gap-2">
                    <h3 className="font-serif font-bold text-stone-900 text-base">
                      {note.title}
                    </h3>
                    <button
                      type="button"
                      onClick={() => onDeleteNote(note.id)}
                      className="p-1 text-stone-400 hover:text-red-700 transition-colors"
                      title="Delete note"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>

                  {note.cyrillicSnippet && (
                    <div className="my-2 p-2 bg-stone-50 rounded border border-stone-200 font-serif font-bold text-stone-900 text-base">
                      {note.cyrillicSnippet}
                    </div>
                  )}

                  <p className="text-xs text-stone-700 leading-relaxed whitespace-pre-wrap mt-2">
                    {note.content}
                  </p>
                </div>

                <div className="pt-3 border-t border-stone-100 flex items-center justify-between text-[11px] text-stone-400">
                  <div className="flex items-center gap-1 flex-wrap">
                    {note.tags.map((t) => (
                      <span
                        key={t}
                        className="px-1.5 py-0.5 rounded bg-stone-100 text-stone-600 font-mono text-[10px]"
                      >
                        #{t}
                      </span>
                    ))}
                  </div>

                  <span className="flex items-center gap-1">
                    <Calendar className="w-3 h-3" />
                    <span>{new Date(note.createdAt).toLocaleDateString()}</span>
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
