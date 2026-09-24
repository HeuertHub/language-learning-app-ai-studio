import {
  doc,
  getDoc,
  setDoc,
  collection,
  getDocs,
  deleteDoc,
  serverTimestamp,
} from 'firebase/firestore';
import { db, handleFirestoreError, OperationType } from './firebase';
import type { CourseCompletionStats, UserStudyNote } from '../types/curriculum';

const LOCAL_PROGRESS_KEY = 'mongolian_course_progress_';
const LOCAL_NOTES_KEY = 'mongolian_course_notes_';

// Check for and remove references to obsolete curriculum IDs (e.g. les_001, unit_001 from failed v1)
function sanitizeProgressIds(progress: CourseCompletionStats): CourseCompletionStats {
  const isFailedV1Id = (id: string) => /^les_\d{3}$/.test(id) || /^unit_\d{3}$/.test(id) || /^sec_\d{2}$/.test(id);
  const cleanLessons = (progress.completedLessonIds || []).filter(id => !isFailedV1Id(id));
  const cleanUnits = (progress.completedUnitIds || []).filter(id => !isFailedV1Id(id));

  return {
    ...progress,
    completedLessonIds: cleanLessons,
    completedUnitIds: cleanUnits,
  };
}

export function clearObsoleteCourseProgress(courseId: string = 'mongolian_cyrillic_comprehensive'): void {
  try {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.removeItem(`${LOCAL_PROGRESS_KEY}${courseId}`);
      localStorage.removeItem(`${LOCAL_PROGRESS_KEY}mongolian-cyrillic`);
    }
  } catch (e) {
    console.warn('Could not clear local storage progress:', e);
  }
}

export async function fetchCourseProgress(
  courseId: string,
  userId: string
): Promise<CourseCompletionStats> {
  const path = `users/${userId}/progress/${courseId}`;
  try {
    const docRef = doc(db, 'users', userId, 'progress', courseId);
    const snap = await getDoc(docRef);

    if (snap.exists()) {
      const data = snap.data();
      const rawProgress: CourseCompletionStats = {
        courseId,
        userId,
        completedLessonIds: data.completedLessonIds || [],
        completedUnitIds: data.completedUnitIds || [],
        masteredVocabCount: data.masteredVocabCount || 0,
        totalExercisesAttempted: data.totalExercisesAttempted || 0,
        totalExercisesCorrect: data.totalExercisesCorrect || 0,
        timeSpentMinutes: data.timeSpentMinutes || 0,
        lastStudiedAt: data.updatedAt?.toDate?.()?.toISOString() || new Date().toISOString(),
      };
      const progress = sanitizeProgressIds(rawProgress);
      // Cache locally
      localStorage.setItem(`${LOCAL_PROGRESS_KEY}${courseId}`, JSON.stringify(progress));
      return progress;
    }
  } catch (error) {
    console.warn('Firestore fetch failed, checking local backup:', error);
  }

  // Fallback to local storage if cloud is unreachable or first time
  const local = localStorage.getItem(`${LOCAL_PROGRESS_KEY}${courseId}`);
  if (local) {
    try {
      const parsed = JSON.parse(local);
      const sanitized = sanitizeProgressIds(parsed);
      if (sanitized.completedLessonIds.length !== parsed.completedLessonIds?.length) {
        localStorage.setItem(`${LOCAL_PROGRESS_KEY}${courseId}`, JSON.stringify(sanitized));
      }
      return sanitized;
    } catch {
      // ignore
    }
  }

  return {
    courseId,
    userId,
    completedLessonIds: [],
    completedUnitIds: [],
    masteredVocabCount: 0,
    totalExercisesAttempted: 0,
    totalExercisesCorrect: 0,
    timeSpentMinutes: 0,
    lastStudiedAt: new Date().toISOString(),
  };
}

export async function persistCourseProgress(
  progress: CourseCompletionStats
): Promise<void> {
  // Always update local cache instantly
  localStorage.setItem(
    `${LOCAL_PROGRESS_KEY}${progress.courseId}`,
    JSON.stringify(progress)
  );

  const path = `users/${progress.userId}/progress/${progress.courseId}`;
  try {
    const docRef = doc(db, 'users', progress.userId, 'progress', progress.courseId);
    await setDoc(
      docRef,
      {
        id: progress.courseId,
        courseId: progress.courseId,
        userId: progress.userId,
        completedLessonIds: progress.completedLessonIds,
        completedUnitIds: progress.completedUnitIds,
        masteredVocabCount: progress.masteredVocabCount,
        totalExercisesAttempted: progress.totalExercisesAttempted,
        totalExercisesCorrect: progress.totalExercisesCorrect,
        timeSpentMinutes: progress.timeSpentMinutes,
        updatedAt: serverTimestamp(),
      },
      { merge: true }
    );
  } catch (error) {
    console.error('Failed to sync course progress to Firestore:', error);
    // Don't crash UI, progress is saved in local cache
  }
}

export async function fetchUserStudyNotes(userId: string): Promise<UserStudyNote[]> {
  const path = `users/${userId}/notes`;
  try {
    const colRef = collection(db, 'users', userId, 'notes');
    const snapshot = await getDocs(colRef);
    const notes: UserStudyNote[] = [];
    snapshot.forEach((d) => {
      const data = d.data();
      notes.push({
        id: d.id,
        userId,
        title: data.title || '',
        cyrillicSnippet: data.cyrillicSnippet || '',
        content: data.content || '',
        tags: data.tags || [],
        createdAt: data.createdAt?.toDate?.()?.toISOString() || new Date().toISOString(),
        updatedAt: data.updatedAt?.toDate?.()?.toISOString(),
      });
    });
    localStorage.setItem(`${LOCAL_NOTES_KEY}${userId}`, JSON.stringify(notes));
    return notes;
  } catch (error) {
    console.warn('Firestore fetch notes error, falling back to local:', error);
  }

  const local = localStorage.getItem(`${LOCAL_NOTES_KEY}${userId}`);
  if (local) {
    try {
      return JSON.parse(local);
    } catch {
      // ignore
    }
  }
  return [];
}

export async function persistStudyNote(
  note: UserStudyNote
): Promise<void> {
  const path = `users/${note.userId}/notes/${note.id}`;
  try {
    const docRef = doc(db, 'users', note.userId, 'notes', note.id);
    await setDoc(
      docRef,
      {
        id: note.id,
        userId: note.userId,
        title: note.title,
        cyrillicSnippet: note.cyrillicSnippet || '',
        content: note.content,
        tags: note.tags,
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      },
      { merge: true }
    );
  } catch (error) {
    console.error('Firestore save note error:', error);
  }

  // Update local notes cache
  const local = localStorage.getItem(`${LOCAL_NOTES_KEY}${note.userId}`);
  const list: UserStudyNote[] = local ? JSON.parse(local) : [];
  const existingIdx = list.findIndex((n) => n.id === note.id);
  if (existingIdx >= 0) {
    list[existingIdx] = note;
  } else {
    list.unshift(note);
  }
  localStorage.setItem(`${LOCAL_NOTES_KEY}${note.userId}`, JSON.stringify(list));
}

export async function removeStudyNote(userId: string, noteId: string): Promise<void> {
  try {
    const docRef = doc(db, 'users', userId, 'notes', noteId);
    await deleteDoc(docRef);
  } catch (error) {
    console.warn('Firestore delete note note:', error);
  }

  const local = localStorage.getItem(`${LOCAL_NOTES_KEY}${userId}`);
  if (local) {
    try {
      const list: UserStudyNote[] = JSON.parse(local);
      const filtered = list.filter((n) => n.id !== noteId);
      localStorage.setItem(`${LOCAL_NOTES_KEY}${userId}`, JSON.stringify(filtered));
    } catch {
      // ignore
    }
  }
}
