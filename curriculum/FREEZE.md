# Curriculum Architecture Freeze Document

**Status**: PERMANENTLY FROZEN  
**Freeze Timestamp**: 2026-09-24T06:48:38-07:00  
**Authority**: Lead Curriculum Architect & CEFR Standards Committee  

---

## 1. Absolute Immutability Directives

The entire curriculum architecture across all levels (**Pre-A1, A1, A2, B1, B2, C1, C2**) is strictly frozen. The following elements must **NEVER** be modified, deleted, shifted, renumbered, or recalculated:

1. **Units**:
   - Total Unit Count: 256 Units (comprising 15 Pre-A1 phonology & script units plus 241 CEFR A1–C2 units).
   - Unit identifiers (`unit_pre_a1_01_...` through `unit_c2_256_...`), CEFR classifications, and sequence within sections.
   - Section bounds and titles (26 Sections total: 2 Pre-A1, 5 A1, 5 A2, 4 B1, 4 B2, 3 C1, 3 C2).

2. **Lessons**:
   - Total Authoritative Lessons: **1,257 lessons** (Pre-A1 through C2).
   - Lesson IDs (`les_...`), sequence numbers within units (`sequenceWithinUnit`).
   - Lesson types (`grammar_introduction`, `reading`, `listening`, `spoken_production`, `writing`, `review`, etc.).
   - Pedagogical communicative outcomes and primary purposes.

3. **Lexical Allocation Budgets**:
   - Core and receptive lemma targets per unit and per lesson.
   - Core and receptive expression targets per unit and per lesson.
   - Exact mathematical parity across all blueprints.

4. **Grammar & Structural Progression**:
   - Morphosyntactic scope (`grammarIntroduced`, `grammarPracticed`, `grammarReviewed`).
   - Grammatical sequencing across CEFR tiers (from basic copula to Middle Mongolian case morphology and classical strophic versification).

5. **Prerequisite & Review DAG**:
   - `prerequisiteLessonIds`, `reviewsLessonIds`, and `reviewsUnitIds`.
   - Directed Acyclic Graph topology and cross-level articulation bridges.

6. **Objectives & Mastery Criteria**:
   - Communicative functions introduced, practiced, and reviewed.
   - Lesson-level success criteria, mastery evidence, and recommended exercise modalities.

---

## 2. Frozen Curriculum Assets & Verification Manifest

All files in `curriculum/blueprint/` and `curriculum/lesson_blueprints/` are cryptographically checksummed in:
- `curriculum/CURRICULUM_FREEZE_MANIFEST.json`

| CEFR Level | Units | Complete Blueprint File | Total Lessons | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pre-A1** | Units 001–015 (2 sections) | `curriculum/lesson_blueprints/preA1.json` | 73 | **FROZEN** |
| **A1** | Units 016–063 (5 sections) | `curriculum/lesson_blueprints/a1_complete.json` | 278 | **FROZEN** |
| **A2** | Units 064–111 (5 sections) | `curriculum/lesson_blueprints/a2_complete.json` | 233 | **FROZEN** |
| **B1** | Units 112–155 (4 sections) | `curriculum/lesson_blueprints/b1_complete.json` | 194 | **FROZEN** |
| **B2** | Units 156–197 (4 sections) | `curriculum/lesson_blueprints/b2_complete.json` | 188 | **FROZEN** |
| **C1** | Units 198–228 (3 sections) | `curriculum/lesson_blueprints/c1_complete.json` | 148 | **FROZEN** |
| **C2** | Units 229–256 (3 sections) | `curriculum/lesson_blueprints/c2_complete.json` | 143 | **FROZEN** |
| **Total** | **256 Units (Includes 15 Pre-A1 Units)** | — | **1,257 Lessons** | **FROZEN** |

---

## 3. Downstream Policy

Any downstream implementation phases (UI components, learner progression tracking, exercise content generation, audio synthesis, assessment engines, etc.) must treat these curriculum blueprints as immutable read-only contracts.
