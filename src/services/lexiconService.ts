/**
 * Phase 3C.0R Learner-Facing Lexicon Runtime Service
 * Enforces strict runtime filtering:
 * Only records with approved learner-facing lifecycle status
 * ('SOURCE_VERIFIED' | 'LINGUISTICALLY_REVIEWED') are loaded and returned.
 *
 * UNREALIZED or PLACEHOLDER_INVALID slots are strictly filtered out and never
 * exposed in vocabulary lists, search, or dashboards.
 */

import type {
  LexicalLemma,
  LexicalExpression,
  LessonLexiconLookupEntry,
  LexiconManifest,
} from '../types/lexicon';

class LexiconService {
  private lemmasCache: LexicalLemma[] | null = null;
  private expressionsCache: LexicalExpression[] | null = null;
  private lookupMapCache: Record<string, LessonLexiconLookupEntry> | null = null;
  private manifestCache: LexiconManifest | null = null;

  async getManifest(): Promise<LexiconManifest | null> {
    if (this.manifestCache) return this.manifestCache;
    try {
      const res = await fetch('/data/lexicon/lexicon_manifest.json');
      if (!res.ok) return null;
      this.manifestCache = await res.json();
      return this.manifestCache;
    } catch {
      return null;
    }
  }

  /**
   * Returns only learner-ready realized lemmas (LINGUISTICALLY_REVIEWED / SOURCE_VERIFIED).
   * Unrealized or invalid placeholder records are strictly filtered out.
   */
  async getLearnerLemmas(): Promise<LexicalLemma[]> {
    if (this.lemmasCache) return this.lemmasCache;
    try {
      const res = await fetch('/data/lexicon/lemmas_bundle.json');
      if (!res.ok) return [];
      const raw: LexicalLemma[] = await res.json();
      // Strict runtime gate: only approved learner-ready status
      this.lemmasCache = raw.filter(
        (l) =>
          (l.status === 'LINGUISTICALLY_REVIEWED' || l.status === 'SOURCE_VERIFIED') &&
          Boolean(l.lemma && l.gloss)
      );
      return this.lemmasCache;
    } catch {
      return [];
    }
  }

  /**
   * Returns only learner-ready realized expressions.
   */
  async getLearnerExpressions(): Promise<LexicalExpression[]> {
    if (this.expressionsCache) return this.expressionsCache;
    try {
      const res = await fetch('/data/lexicon/expressions_bundle.json');
      if (!res.ok) return [];
      const raw: LexicalExpression[] = await res.json();
      this.expressionsCache = raw.filter(
        (e) =>
          (e.status === 'LINGUISTICALLY_REVIEWED' || e.status === 'SOURCE_VERIFIED') &&
          Boolean(e.expression && e.gloss)
      );
      return this.expressionsCache;
    } catch {
      return [];
    }
  }

  /**
   * Returns the lesson lexicon lookup entry.
   */
  async getLessonLexiconMap(): Promise<Record<string, LessonLexiconLookupEntry>> {
    if (this.lookupMapCache) return this.lookupMapCache;
    try {
      const res = await fetch('/data/lexicon/lesson_lexicon_lookup.json');
      if (!res.ok) return {};
      this.lookupMapCache = await res.json();
      return this.lookupMapCache || {};
    } catch {
      return {};
    }
  }

  /**
   * Retrieves realized learner-ready vocabulary introduced in a specific lesson.
   */
  async getLearnerVocabularyForLesson(lessonId: string): Promise<{
    productiveLemmas: LexicalLemma[];
    receptiveLemmas: LexicalLemma[];
    productiveExpressions: LexicalExpression[];
    receptiveExpressions: LexicalExpression[];
  }> {
    const [allLemmas, allExprs, map] = await Promise.all([
      this.getLearnerLemmas(),
      this.getLearnerExpressions(),
      this.getLessonLexiconMap(),
    ]);

    const entry = map[lessonId];
    if (!entry) {
      return {
        productiveLemmas: [],
        receptiveLemmas: [],
        productiveExpressions: [],
        receptiveExpressions: [],
      };
    }

    const lemmaMap = new Map(allLemmas.map((l) => [l.id, l]));
    const exprMap = new Map(allExprs.map((e) => [e.id, e]));

    return {
      productiveLemmas: entry.productiveLemmaIds
        .map((id) => lemmaMap.get(id))
        .filter((l): l is LexicalLemma => Boolean(l)),
      receptiveLemmas: entry.receptiveLemmaIds
        .map((id) => lemmaMap.get(id))
        .filter((l): l is LexicalLemma => Boolean(l)),
      productiveExpressions: entry.productiveExpressionIds
        .map((id) => exprMap.get(id))
        .filter((e): e is LexicalExpression => Boolean(e)),
      receptiveExpressions: entry.receptiveExpressionIds
        .map((id) => exprMap.get(id))
        .filter((e): e is LexicalExpression => Boolean(e)),
    };
  }
}

export const lexiconService = new LexiconService();
