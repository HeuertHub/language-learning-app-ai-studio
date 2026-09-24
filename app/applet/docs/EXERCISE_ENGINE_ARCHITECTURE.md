# Phase 3A: Exercise Engine Architecture Specification

**Status**: ARCHITECTURE APPROVED (PHASE 3A)  
**Author**: Lead System Architect & Educational Engine Specialist  
**Target Platform**: AI Studio Learning Platform (React/TypeScript, Vite, Firestore)  
**Curriculum Status**: FROZEN & IMMUTABLE (Pre-A1 through C2, 1,257 Lessons)  

---

## 1. Executive Overview & Core Architectural Tenets

The Exercise Engine is the runtime generation, validation, and delivery pipeline responsible for transforming frozen lesson blueprints into interactive learner experiences. It is governed by three foundational invariants:

1. **Curriculum Immutability**: The lesson blueprints (`curriculum/lesson_blueprints/*`) and unit blueprints (`curriculum/blueprint/*`) are read-only upstream contracts. The engine never modifies, reallocates, resequences, or recalculates curriculum parameters.
2. **Pedagogical Modality Specialization**: There is no "universal exercise template". Different lesson modalities (e.g., *grammar introduction*, *archival listening*, *philological exegesis*, *ceremonial speaking*) require distinct cognitive interaction models, answer evaluation pipelines, and feedback loops.
3. **Multi-Stage Quality Gating**: Every generated exercise must pass a 10-point automated validation gate before it can be stored in the exercise bank or served to learners.

---

## 2. Comprehensive Exercise Data Schemas

The TypeScript interfaces defining learner-facing content are formalized in `src/types/exerciseEngine.ts`. Below is the complete schema architecture:

### 2.1 Identity & Linkage
```typescript
interface ExerciseIdentity {
  exerciseId: string;          // Formatted: exe_{cefr}_{unitSeq:03d}_{lessonSeq:02d}_{itemSeq:02d}_{taxonomy}
  version: string;             // Semantic versioning (e.g., '1.0.0')
  status: 'draft' | 'validated' | 'active' | 'deprecated';
  checksumSha256: string;      // Deterministic SHA-256 hash of the entire content payload
  lessonId: string;            // Strict foreign key -> frozen lesson blueprint (e.g., les_c2_248_01_...)
  unitId: string;              // Strict foreign key -> frozen unit blueprint
  sectionId: string;           // Strict foreign key -> frozen section
  cefrLevel: 'Pre-A1' | 'A1' | 'A2' | 'B1' | 'B2' | 'C1' | 'C2';
  exerciseModality: ExerciseModality;
  exerciseTaxonomy: ExerciseTaxonomyType;
}
```

### 2.2 Pedagogical Target Schema
```typescript
interface ExercisePedagogicalTarget {
  primarySkill: SkillTargetDomain;
  secondarySkills: SkillTargetDomain[];
  grammarTarget?: {
    ruleIdentifier: string;
    morphemeTarget: string;
    harmonicClass: 'masculine_back' | 'feminine_front' | 'neutral';
    pedagogicalSummary: string;
  };
  vocabularyTarget?: {
    productiveLemmas: string[];
    receptiveLemmas: string[];
    collocationsOrExpressions: string[];
  };
  objectiveReference: string; // Direct citation of frozen lesson communicative outcome or objective
}
```

### 2.3 Prompt Payload Schema
```typescript
interface ExercisePromptPayload {
  instructionCyrillic: string;
  instructionEnglish: string;
  stimulusType: 'text' | 'audio' | 'dialogue' | 'archival_quote' | 'philological_gloss' | 'none';
  stimulusTextCyrillic?: string;
  stimulusTextEnglish?: string;
  dialogueTurns?: Array<{
    speaker: string;
    textCyrillic: string;
    textEnglish?: string;
  }>;
  audioStimulusId?: string;
  culturalOrPragmaticContext?: string;
}
```

### 2.4 Answer Payload & Evaluator Schema
```typescript
interface ExerciseAnswerPayload {
  evaluatorType: EvaluatorType;
  // Multiple Choice / Discrimination / Ranking
  options?: ExerciseOptionItem[];
  distractorAnalyses?: DistractorAnalysis[];
  // Syntactic Builder / Token Arrangement (SOV free-topic permutations)
  wordTokens?: string[];
  validTokenPermutations?: string[][];
  // Morphological Suffix Fill (Agglutinative slot attachment)
  baseStemCyrillic?: string;
  targetMorpheme?: string;
  acceptableMorphemeVariants?: string[];
  // Free Text / Oratorical / Rubric
  canonicalAnswers?: string[];
  acceptableVariations?: string[];
  regexValidationPatterns?: string[];
  requiredKeywords?: string[];
  disallowedElements?: string[];
}
```

### 2.5 Remediation & Feedback Schema
```typescript
interface ExerciseRemediationPayload {
  hints: ProgressiveHint[]; // 3-stage scaffolding: metalinguistic nudge -> structural scaffold -> near-solution
  detailedExplanations: {
    ruleCitation: string;
    primaryExplanation: string;
    etymologicalOrSociolinguisticNote?: string;
  };
  distractorAnalyses?: Array<{
    optionId: string;
    text: string;
    errorCategory: string;
    pedagogicalExplanation: string;
  }>;
}
```

### 2.6 Evaluation Rules Schema
```typescript
interface ExerciseEvaluationRules {
  ignorePunctuation: boolean;
  ignoreWhitespace: boolean;
  caseSensitive: boolean;
  enforceVowelLength: boolean;
  allowConsonantAssimilationAlternates: boolean;
  allowAlternativeWordOrderSOV: boolean;
  passingScorePercent: number;
}
```

---

## 3. Exercise Generation Framework by Lesson Modality

To prevent template homogenization, exercise generation pipelines are segregated into 8 specialized modality subsystems:

```
                                  [Frozen Lesson Blueprint]
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
             [Modality Router]                           [Lexical/Grammar Quota]
                       │                                           │
  ┌────────────┬───────┴────┬───────────┬───────────┬──────────────┤
  ▼            ▼            ▼           ▼           ▼              ▼
[Vocab]     [Grammar]   [Reading]   [Listening] [Speaking] [Writing/Capstone]
Pipeline    Pipeline    Pipeline    Pipeline    Pipeline      Pipeline
```

### 3.1 Vocabulary Lessons (`vocabulary`)
- **Focus**: Semantic networks, antonym/synonym fine grading, harmonic categorization, somatic metaphor integration.
- **Taxonomy**: `vowel_harmony_categorization`, `somatic_idiom_application`, `collocational_pairing`, `synonym_nuance_ranking`.
- **Generation Logic**: 
  - Never generate isolated English-to-Mongolian flashcard pairs.
  - Require context-rich collocations (e.g., *морь унах* vs *морь сойх*).
  - Test register tiering (e.g., everyday *хэлэх* vs respectful *айлтгах* vs high ceremonial *айлдвар*).

### 3.2 Grammar Introduction Lessons (`grammar_introduction`)
- **Focus**: Inductive discovery of new morphosyntactic patterns followed by structural isolate manipulation.
- **Taxonomy**: `morpheme_attachment_drill`, `case_government_selection`, `cloze_grammatical_matrix`.
- **Generation Logic**:
  - Present authentic minimal pairs showing semantic change upon suffix application (e.g., ablative *-аас* source vs dative-locative *-д* position).
  - Explicit distractor modeling around vowel harmony violations (e.g., offering front-vowel *-ээс* for a back-vowel stem like *ном* to verify morphological rule acquisition).

### 3.3 Grammar Practice Lessons (`grammar_practice`)
- **Focus**: Complex clause chaining, converbial subordination, syntactic transformation, and SOV clause building.
- **Taxonomy**: `converb_clause_linkage`, `voice_valency_transformation`, `sov_syntactic_reordering`.
- **Generation Logic**:
  - Present multi-clause sentence stitching using imperfect converbs (*-ж/-ч*), modal converbs (*-н*), and conditional converbs (*-бал/-бэл*).
  - Validates alternative topicalized SOV orders (e.g., SOV, OSV with emphatic topicalization) while rejecting verb-medial or verb-initial non-poetic forms.

### 3.4 Reading Lessons (`reading`)
- **Focus**: Textual deconstruction, narrative voice identification, intertextual cultural referencing, macro-discourse comprehension.
- **Taxonomy**: `intertextual_reading_analysis`, `subtext_irony_decoding`, `philological_gloss_exegesis`.
- **Generation Logic**:
  - Stimulus consists of full authentic excerpts (e.g., Natsagdorj, Tudev, Secret History, legal codes).
  - Questions evaluate tone, stance, presupposition, and rhetorical function rather than simple factual word retrieval.

### 3.5 Listening Lessons (`listening`)
- **Focus**: Acoustic comprehension of connected speech, phonotactic assimilation, dialectal variation, and archival audio decoding.
- **Taxonomy**: `audio_dialogue_inference`, `acoustic_dialect_discrimination`, `phonemic_discrimination`.
- **Generation Logic**:
  - Pre-A1/A1: Minimal phonemic pairs (*Ө* vs *Ү*, *Ц* vs *Ч*, short vs long vowels).
  - B2/C1/C2: Natural speech rate (150–180 wpm), overlapping dialogue, elliptical colloquial speech, or epic throat-singing recitation.
  - Multi-tiered listening tasks: global gist -> specific pragmatic inference -> acoustic transcription.

### 3.6 Speaking Lessons (`spoken_production` / `spoken_interaction`)
- **Focus**: Prosodic delivery, oratorical pacing, honorific framing, ceremonial blessings, and argumentative floor defense.
- **Taxonomy**: `oratorical_framing_delivery`, `ceremonial_blessing_formulation`, `register_level_matching`.
- **Generation Logic**:
  - Structured prompt with explicit communicative constraints (audience, register, required honorifics, prohibited informal markers).
  - Multi-tier rubric: Phonetic accuracy, syntactic complexity, lexical appropriateness, prosodic pacing.

### 3.7 Writing Lessons (`writing`)
- **Focus**: Genre-specific written production, official epistolary norms, comparative scholarly essays, gnomic poetry composition.
- **Taxonomy**: `guided_epistolary_composition`, `discourse_refutation_builder`, `proverbial_clinching_synthesis`.
- **Generation Logic**:
  - Guided writing prompts providing situational background and formal communicative deliverables.
  - Evaluated against keyword inclusion, morphological case accuracy, converb clause coherence, and absence of anachronisms.

### 3.8 Synthesis & Capstone Lessons (`synthesis_capstone`)
- **Focus**: Multi-skill realistic simulations that fuse oral oratory, deep reading comprehension, and structural mastery.
- **Taxonomy**: Multi-stage scenario matrices (e.g., simulating a diplomatic envoy negotiating a pasture agreement or defending a doctoral thesis on steppe philology).

---

## 4. Quality Validation Framework (10-Point Automated & Expert Gate)

Before any exercise payload is admitted to the active learner bank, it must pass through the `ExerciseValidatorPipeline`:

```
[Raw Generated Exercise]
          │
          ▼
┌───────────────────────────────────────────────┐
│ 1. Linguistic & Cyrillic Orthography Engine    │
│ 2. Vowel Harmony & Morphosyntax Checker       │
│ 3. CEFR Complexity & Lexile Classifier        │
│ 4. Blueprint Objective & Outcome Matcher      │
│ 5. Lexical Budget & Prerequisite Auditor      │
│ 6. Answer Key Solvability & Uniqueness Test    │
│ 7. Distractor Quality & Pedagogy Auditor      │
│ 8. Ambiguity & Polysemy Filter                │
│ 9. Anti-Fatigue & Template Divergence Check   │
│ 10. Difficulty Monotonicity Calibration       │
└───────────────────────────────────────────────┘
          │
     [Pass All 10?]
     ├── Yes ──► Status: "validated" ──► Exercise Bank
     └── No  ──► Status: "rejected"  ──► Remediation Queue
```

### Gate 1: Linguistic & Cyrillic Orthography Engine
- Enforces official Mongolian State Orthographic Dictionary standards (74-rule canon).
- Verifies yotated vowel behavior (*я, е, ё, ю*), soft/hard signs (*ь, ъ*), vowel preservation in suffixation, and terminal consonant assimilation (*н, г, р, с, т, б*).

### Gate 2: Vowel Harmony & Morphosyntax Checker
- Computes harmonic class of root stems:
  - Masculine (Back): *а, о, у*
  - Feminine (Front): *э, ө, ү*
  - Neutral: *и*
- Rejects any exercise containing vowel discordance (e.g., *\*гар-ээс* instead of *гар-аас*).

### Gate 3: CEFR Appropriateness Classifier
- Analyzes syntactic parse tree: clausal nesting depth, dependency length, and word count.
- Enforces level ceilings (e.g., A1 cannot contain nested concessive-conditional converb chains; C2 must feature complex discourse markers).

### Gate 4: Blueprint Objective & Outcome Matcher
- Verifies that the exercise directly targets at least one declared objective, grammar rule, or communicative function listed in the frozen lesson blueprint.

### Gate 5: Lexical Budget & Prerequisite Auditor
- Verifies that all non-glossed vocabulary in prompts and expected answers belongs either to the current lesson's target vocabulary or to prerequisite lessons in the frozen DAG.

### Gate 6: Answer Key Solvability & Uniqueness Test
- An automated headless solver executes the exercise.
- For multiple choice: exactly one option must be unambiguously correct.
- For open-ended: canonical answers must satisfy all regex and syntactic rubrics without false rejections.

### Gate 7: Distractor Quality & Pedagogy Auditor
- Eliminates "throwaway" or absurd distractors.
- Every distractor must represent a real, documented learner interlanguage pitfall (e.g., false friends, case government confusion, front/back harmony confusion) and include a pedagogically illuminating explanation.

### Gate 8: Ambiguity & Polysemy Filter
- Cross-references semantic frames to ensure the prompt provides sufficient contextual framing so that only the intended linguistic form is correct.

### Gate 9: Anti-Fatigue & Template Divergence Check
- Calculates token n-gram Jaccard distance against all existing exercises in the same unit.
- If similarity exceeds 0.70, the exercise is flagged for excessive template repetition.

### Gate 10: Difficulty Monotonicity Calibration
- Computes Bloom's cognitive demand rank and linguistic density, confirming alignment with the CEFR level progression.

---

## 5. Audio Generation Architecture

The audio pipeline bridges synthetic web audio and native human studio recordings based on CEFR level and lesson purpose:

```
                          [Audio Requirement Analyzer]
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
     [Tier 1: Neural TTS]                          [Tier 2: Studio Audio]
   (Pre-A1 - B1 Routine Drills)                 (B2 - C2, Archival, Epics)
                │                                             │
                ▼                                             ▼
  • Web SpeechSynthesis API                     • Native Steppe Speakers (M/F)
  • Google Cloud Neural2 / Gemini Audio         • Archival Historical Fieldwork
  • Configurable WPM (0.75x - 1.25x)            • Throat Singing & Morin Khuur
                │                                             │
                └──────────────────────┬──────────────────────┘
                                       ▼
                       [Audio Playback & Metadata Pack]
                       • WebVTT Word-Level Timestamps
                       • Phonetic Stress & Pitch Contours
                       • Acoustic Environment Tagging
```

### 5.1 Playback Metadata Specification
Every audio asset is paired with an immutable JSON metadata envelope:
- `durationMs`: Total duration in milliseconds.
- `speechRateWpm`: Words per minute (110 wpm for Pre-A1/A1; 140 wpm for B1; 175+ wpm for C1/C2).
- `wordTimestamps`: Array of `{ word: string, startMs: number, endMs: number }` for live karaoke-style transcript tracking.
- `acousticProfile`: Clean studio, conversational ambient, or archival analog grain.

### 5.2 Pronunciation & Speech Evaluation Interface
For speaking exercises:
1. Client-side audio recording via MediaRecorder API (16kHz PCM / Opus).
2. Phonetic token alignment against expected IPA sequence.
3. Scoring dimensions:
   - Phonemic accuracy (vowel length distinction: *хар* vs *хаар*).
   - Vowel harmony acoustic resonance (F1/F2 formants for *ө* vs *ү*).
   - Intonation and clausal cadence.

---

## 6. The Difficulty Model: Pre-A1 → C2 Progression

The engine scales item difficulty monotonically across 5 independent vectors:

| Dimension | Pre-A1 → A1 | A2 → B1 | B2 → C1 | C2 Mastery |
| :--- | :--- | :--- | :--- | :--- |
| **Linguistic Complexity** | Single Cyrillic graphemes, simple CVC roots, basic copula. | Agglutinative chains (root + 2 suffixes), primary converbs (*-ж, -аад*). | Multi-clause sentences, secondary converbs (*-магц, -тал*), complex voice. | Classical strophic poetry, archaic suffixes (*-да, -болтугай*), stelae prose. |
| **Cognitive Demand** | Recall, identification, phonetic discrimination. | Rule application, sentence combination, routine information retrieval. | Stance analysis, bias detection, nuanced argument synthesis. | Deconstruction of satire, philosophical theorization, sovereign authorship. |
| **Ambiguity & Subtext** | Zero ambiguity; binary true/false, direct pairing. | Low ambiguity; clear semantic context, minimal polysemy. | Moderate ambiguity; implicit stance, hedging, ironic understatement. | High cultural subtext; caustic sarcasm, double entendre, gnomic allegories. |
| **Discourse Scope** | Isolated letters and individual words (1–5 tokens). | Simple sentences and formulaic dialogues (10–30 tokens). | Multi-paragraph narratives and formal lectures (100–300 tokens). | Extended philosophical treatises, full epic cantos, archival audio (500+ tokens). |
| **Register Expectations** | Standard pedagogical neutral. | Informal colloquial vs. standard polite everyday. | Formal administrative, journalistic, academic, and business. | Epic rhapsodic, imperial epigraphic, liturgical Buddhist, sovereign oratorical. |

---

## 7. Exercise Anti-Pattern Prevention Safeguards

To maintain premier pedagogical integrity, the engine enforces strict structural constraints against common ed-tech anti-patterns:

1. **Anti-Flashcard Mandate**: Isolated translation drills ("What is the Mongolian word for horse?") are strictly prohibited beyond Pre-A1. All vocabulary must be exercised in collocational or situational context.
2. **Dynamic Exercise Budgets**: Exercise counts per lesson are not hardcoded to an arbitrary number (e.g., 10). Instead, exercise quotas are mathematically derived from the lesson's target density (e.g., a high-density grammar intro generates 6–8 deep multi-step exercises; a capstone generates 3–4 complex multi-phase simulations).
3. **Contextual Authenticity Guard**: Synthetic, artificial sentences ("The green elephant reads a newspaper") are rejected. All sentences must reflect authentic nomadic, urban, historical, or modern Mongolian communicative contexts.
4. **Plausible Distractor Principle**: Distractors must never be random filler words from unrelated lexical domains. Distractors must share the same grammatical part of speech and represent plausible cognitive errors.
5. **Direct Objective Coupling**: An exercise cannot be generated unless its primary skill and target rule map 1:1 with the parent lesson blueprint's `communicativeFunctionsIntroduced`, `grammarIntroduced`, or `lexicalDomains`.

---

## 8. Database & Storage Architecture

The content storage model decouples immutable curriculum blueprints from generated exercise instances, learner tracking, and future language expansions:

```
[Firestore Root]
  │
  ├── /curriculum_blueprints/              (IMMUTABLE UPSTREAM CONTRACT)
  │     └── {levelId}/                     (e.g., 'c2')
  │           └── units / lessons
  │
  ├── /exercise_banks/                     (AUDITED GENERATED CONTENT)
  │     └── {courseId}/                    (e.g., 'mongolian_c2_v1')
  │           └── lessons/{lessonId}/
  │                 └── exercises/{exerciseId}
  │
  ├── /learner_profiles/                   (USER STATE & SRS PROGRESS)
  │     └── {userId}/
  │           ├── lesson_mastery/{lessonId}
  │           ├── spaced_repetition_queue/
  │           └── exercise_attempts/{attemptId}
  │
  └── /audio_registry/                     (AUDIO ASSET CATALOG)
        └── {audioId} -> { storageUrl, timestamps, transcript, acousticProfile }
```

### Modular Scalability for Future Languages
The data model uses a polymorphic course abstraction:
- `courseId: string` (e.g., `khalkha_mongolian`, `kazakh`, `buryat`, `classical_mongolian`).
- `script: string` (e.g., `Cyrillic`, `Mongol_Bichig`, `Latin`, `Arabic`).
- Morphological engine hooks: Pluggable morphological analyzers (`HarmonicAnalyzerInterface`) allow the same validator pipeline to evaluate vowel harmony in Turkic or other Mongolic languages without rewriting core UI or progression logic.

---

## 9. Pilot Strategy & Rollout Plan

To ensure absolute stability, no full-scale exercise generation will take place until a strict pilot validation phase is executed.

### 9.1 Pilot Scope (31 Diverse Lessons)
The pilot will cover a representative cross-section of all 7 CEFR levels and all 8 lesson modalities:

| Level | Unit | Lessons Selected | Modalities Tested |
| :--- | :--- | :--- | :--- |
| **Pre-A1** | Unit 001 | 5 lessons | Phonemic discrimination, Cyrillic graphemes, vowel harmony sorting. |
| **A1** | Unit 001 | 5 lessons | Case attachment (*-д/-т*), SOV word ordering, formulaic greetings. |
| **B1** | Unit 106 | 5 lessons | Converb chaining (*-ж байх*), pastoral travel dialogue, cloze matrices. |
| **C1** | Unit 201 | 5 lessons | Bureaucratic register, diplomatic note composition, rapid audio inference. |
| **C2** | Unit 229 | 5 lessons | Steppe satire deconstruction, somatic idioms, unscripted oral debate. |
| **C2** | Unit 256 | 6 lessons | Capstone synthesis, *The Secret History* exegesis, monumental manifesto writing. |
| **Total** | **6 Units** | **31 Lessons (~180–220 Exercises)** | **All 8 Modalities & All 25 Taxonomy Types** |

### 9.2 Validation & Audit Pipeline
1. **Automated Validation**: 100% of pilot exercises must pass the 10-point automated gate.
2. **Linguistic Peer Review**: Native Mongolian linguist audits every prompt, distractor explanation, and audio transcript.
3. **Headless Solver Simulation**: Automated test harness executes all exercises, verifying that passing scores are achievable and zero false rejections occur.
4. **Distractor Discrimination Audit**: Statistical point-biserial correlation analysis ensuring distractors effectively differentiate learner proficiency.

### 9.3 Approval & Production Rollout Gating
Production rollout across the remaining 1,226 lessons will commence only after the Pilot Audit Report achieves:
- Zero critical orthographic/grammatical errors.
- 100% adherence to frozen vocabulary budgets.
- Automated solver pass rate of 100% on valid keys.
- Formal sign-off on Phase 3A architecture.
