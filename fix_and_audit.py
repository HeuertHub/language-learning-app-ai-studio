import json
import os
import math
from collections import Counter, defaultdict

# 1. Load parts
with open('u156_out.json') as f:
    u156 = json.load(f)

with open('u157_u158_out.json') as f:
    u157_158 = json.load(f)

with open('u159_u160_out.json') as f:
    u159_160 = json.load(f)

with open('u161_u162_out.json') as f:
    u161_162 = json.load(f)

with open('u163_u164_u165_u166_out.json') as f:
    u163_166 = json.load(f)

all_lessons = u156 + u157_158 + u159_160 + u161_162 + u163_166

# Sort strictly by unit sequencePosition then sequenceWithinUnit
with open('curriculum/blueprint/units/b2.json') as f:
    b2_units_raw = json.load(f)
    unit_seq_map = {u['unitId']: u['sequencePosition'] for u in b2_units_raw}
    b2_units_dict = {u['unitId']: u for u in b2_units_raw}

all_lessons.sort(key=lambda x: (unit_seq_map[x['unitId']], x['sequenceWithinUnit']))

multi_parent_map = {
    "les_b2_156_05_legislative_reform_commentary_writing": [
        "les_b2_156_04_parliamentary_interpellation_speech",
        "les_b2_156_03_electoral_reform_white_paper_reading"
    ],
    "les_b2_157_04_public_hearing_advocacy_speech": [
        "les_b2_157_03_townhall_testimony_listening",
        "les_b2_157_02_exclusive_focus_particle_syntax"
    ],
    "les_b2_157_05_civic_petition_drafting_workshop": [
        "les_b2_157_04_public_hearing_advocacy_speech",
        "les_b2_157_01_civil_protest_manifesto_reading"
    ],
    "les_b2_158_01_discourse_converb_chaining_analysis": [
        "les_b2_157_05_civic_petition_drafting_workshop",
        "les_b1_155_05_documentary_voiceover_script_writing"
    ],
    "les_b2_158_04_spontaneous_chaining_oral_briefing": [
        "les_b2_158_03_policy_investigation_brief_writing",
        "les_b2_158_02_investigative_podcast_listening"
    ],
    "les_b2_159_04_switch_reference_narrative_speaking": [
        "les_b2_159_03_tribunal_testimony_listening",
        "les_b2_159_01_switch_reference_morphosyntax_intro"
    ],
    "les_b2_159_05_comparative_agency_brief_writing": [
        "les_b2_159_04_switch_reference_narrative_speaking",
        "les_b2_159_02_regulatory_dispute_reading"
    ],
    "les_b2_160_04_keynote_persuasive_presentation": [
        "les_b2_160_03_structured_position_paper_writing",
        "les_b2_160_02_parliamentary_keynote_listening"
    ],
    "les_b2_161_05_systemic_cause_effect_report_writing": [
        "les_b2_161_04_executive_causal_briefing_speech",
        "les_b2_161_02_economic_impact_assessment_reading"
    ],
    "les_b2_162_04_nuanced_stance_spoken_interaction": [
        "les_b2_162_03_political_op_ed_discourse_reading",
        "les_b2_162_02_particles_pragmatic_syntax_intro"
    ],
    "les_b2_162_05_polemical_op_ed_rebuttal_writing": [
        "les_b2_162_04_nuanced_stance_spoken_interaction",
        "les_b2_162_03_political_op_ed_discourse_reading"
    ],
    "les_b2_163_04_timed_oxford_debate_simulation": [
        "les_b2_163_03_point_by_point_rebuttal_writing",
        "les_b2_163_02_parliamentary_cross_examination_listening"
    ],
    "les_b2_164_04_press_briefing_delivery_spoken": [
        "les_b2_164_03_crisis_press_release_drafting",
        "les_b2_164_02_spokesperson_briefing_listening"
    ],
    "les_b2_165_04_panel_consensus_synthesis_writing": [
        "les_b2_165_03_panel_moderation_simulation",
        "les_b2_165_01_moderator_discourse_dossier_reading"
    ],
    "les_b2_166_04_municipal_policy_brief_drafting": [
        "les_b2_166_03_stakeholder_position_synthesis_writing",
        "les_b2_166_01_municipal_urban_masterplan_reading"
    ],
    "les_b2_166_05_parliamentary_standing_committee_hearing": [
        "les_b2_166_04_municipal_policy_brief_drafting",
        "les_b2_166_02_public_hearing_zoning_dispute_listening"
    ],
    "les_b2_166_06_b2_sec01_culminating_mastery_capstone": [
        "les_b2_166_05_parliamentary_standing_committee_hearing",
        "les_b2_166_04_municipal_policy_brief_drafting",
        "les_b2_165_04_panel_consensus_synthesis_writing"
    ]
}

for l in all_lessons:
    lid = l['lessonId']
    if lid in multi_parent_map:
        l['prerequisiteLessonIds'] = multi_parent_map[lid]

# Ensure output directory exists
os.makedirs('curriculum/lesson_blueprints', exist_ok=True)
output_path = 'curriculum/lesson_blueprints/b2_section_01.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_lessons, f, indent=2, ensure_ascii=False)

print(f"Serialized {len(all_lessons)} lessons to {output_path}")

# ==============================================================================
# AUDIT CHECKS
# ==============================================================================

# 1. Lexical Reconciliation Audit
print("\n=== 1. LEXICAL RECONCILIATION AUDIT ===")
unit_lex_calc = defaultdict(lambda: {'PL': 0, 'RL': 0, 'PE': 0, 'RE': 0})
for l in all_lessons:
    uid = l['unitId']
    unit_lex_calc[uid]['PL'] += l['newProductiveLemmaTarget']
    unit_lex_calc[uid]['RL'] += l['newReceptiveLemmaTarget']
    unit_lex_calc[uid]['PE'] += l['newProductiveExpressionTarget']
    unit_lex_calc[uid]['RE'] += l['newReceptiveExpressionTarget']

sec01_units = [u for u in b2_units_raw if u['unitId'] in unit_lex_calc]
mismatch_count = 0
for u in sec01_units:
    uid = u['unitId']
    calc = unit_lex_calc[uid]
    auth_pl = u['newProductiveCoreLemmas']
    auth_rl = u['newReceptiveCoreLemmas']
    auth_pe = u['newProductiveExpressions']
    auth_re = u['newReceptiveExpressions']
    
    pl_match = calc['PL'] == auth_pl
    rl_match = calc['RL'] == auth_rl
    pe_match = calc['PE'] == auth_pe
    re_match = calc['RE'] == auth_re
    
    if not (pl_match and rl_match and pe_match and re_match):
        mismatch_count += 1
        print(f"MISMATCH in {uid}: Calc={calc} vs Auth={(auth_pl, auth_rl, auth_pe, auth_re)}")
    else:
        print(f"MATCH: Unit {u['sequencePosition']} ({u['title']}): PL={calc['PL']}/{auth_pl}, RL={calc['RL']}/{auth_rl}, PE={calc['PE']}/{auth_pe}, RE={calc['RE']}/{auth_re}")

print(f"Total Unit Lexical Mismatches: {mismatch_count}")

# 2. Lesson-Count Distribution Audit
print("\n=== 2. LESSON-COUNT DISTRIBUTION AUDIT ===")
unit_lesson_counts = [len([l for l in all_lessons if l['unitId'] == u['unitId']]) for u in sec01_units]
count_dist = Counter(unit_lesson_counts)
print(f"Unit counts breakdown: {sorted(count_dist.items())}")
print(f"Min lessons: {min(unit_lesson_counts)}")
print(f"Max lessons: {max(unit_lesson_counts)}")
mean_count = sum(unit_lesson_counts) / len(unit_lesson_counts)
variance = sum((x - mean_count) ** 2 for x in unit_lesson_counts) / len(unit_lesson_counts)
std_dev = math.sqrt(variance)
sorted_counts = sorted(unit_lesson_counts)
median_count = sorted_counts[len(sorted_counts)//2]
print(f"Mean: {mean_count:.2f}, Median: {median_count}, Std Dev: {std_dev:.2f}")

# 3. Lesson-Type Distribution Audit
print("\n=== 3. LESSON-TYPE DISTRIBUTION AUDIT ===")
type_counts = Counter(l['lessonType'] for l in all_lessons)
for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c} ({c/len(all_lessons)*100:.1f}%)")

# 4. Exercise Recommendation Distribution Audit
print("\n=== 4. EXERCISE RECOMMENDATION AUDIT ===")
modality_counts = [len(l['recommendedExerciseModalities']) for l in all_lessons]
mod_dist = Counter(modality_counts)
print(f"Exercise recommendations per lesson distribution: {sorted(mod_dist.items())}")
all_modalities = Counter([m for l in all_lessons for m in l['recommendedExerciseModalities']])
print(f"Modality frequencies: {sorted(all_modalities.items(), key=lambda x: -x[1])}")

# 5. Unit Sequence Distribution Audit
print("\n=== 5. UNIT SEQUENCE DIVERSITY AUDIT ===")
unit_patterns = {}
for u in sec01_units:
    u_lessons = [l for l in all_lessons if l['unitId'] == u['unitId']]
    pattern = tuple(l['lessonType'] for l in u_lessons)
    unit_patterns[u['sequencePosition']] = pattern
    print(f"Unit {u['sequencePosition']}: {' -> '.join(pattern)}")

pattern_dist = Counter(unit_patterns.values())
print(f"Unique sequence patterns: {len(pattern_dist)} out of {len(sec01_units)} units")

# 6. DAG Connectivity & Acyclicity Audit
print("\n=== 6. DAG CONNECTIVITY & ACYCLICITY AUDIT ===")
lesson_ids = set(l['lessonId'] for l in all_lessons)
# Also include B1 anchor
lesson_ids.add("les_b1_155_06_b1_level_culminating_mastery_capstone")
lesson_ids.add("les_b1_155_05_documentary_voiceover_script_writing")

adj = defaultdict(list)
in_degree = defaultdict(int)
multi_parent_count = 0
cross_unit_edge_count = 0
total_edges = 0

for l in all_lessons:
    lid = l['lessonId']
    preds = l['prerequisiteLessonIds']
    total_edges += len(preds)
    if len(preds) > 1:
        multi_parent_count += 1
    for p in preds:
        if p not in lesson_ids:
            print(f"ERROR: Missing prerequisite reference {p} in lesson {lid}")
        adj[p].append(lid)
        in_degree[lid] += 1
        # Check cross-unit
        p_unit = [x['unitId'] for x in all_lessons if x['lessonId'] == p]
        if p_unit and p_unit[0] != l['unitId']:
            cross_unit_edge_count += 1
        elif p.startswith("les_b1_"):
            cross_unit_edge_count += 1

print(f"Total prerequisite edges: {total_edges}")
print(f"Multi-parent nodes: {multi_parent_count}")
print(f"Cross-unit edges: {cross_unit_edge_count}")

# Check DAG acyclicity using Kahn's algorithm
q = [lid for lid in lesson_ids if in_degree[lid] == 0]
visited_count = 0
while q:
    curr = q.pop(0)
    visited_count += 1
    for nxt in adj[curr]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.append(nxt)

is_acyclic = visited_count == len(lesson_ids)
print(f"DAG Acyclicity check: {is_acyclic} (Visited {visited_count}/{len(lesson_ids)} nodes)")

# 7. Review Relationships Audit
print("\n=== 7. REVIEW RELATIONSHIPS AUDIT ===")
total_review_lessons = sum(len(l['reviewsLessonIds']) for l in all_lessons)
total_review_units = sum(len(l['reviewsUnitIds']) for l in all_lessons)
b1_review_links = sum(1 for l in all_lessons for r in l['reviewsLessonIds'] if r.startswith('les_b1_'))
print(f"Total review lesson edges: {total_review_lessons}")
print(f"Total review unit edges: {total_review_units}")
print(f"B1 cross-level review edges: {b1_review_links}")

# 8. Grammar Coverage & Reuse Audit
print("\n=== 8. GRAMMAR COVERAGE & REUSE AUDIT ===")
introduced_grammar = [g for l in all_lessons for g in l['grammarIntroduced']]
print(f"Grammar concepts introduced in Sec 01: {introduced_grammar}")
for g in introduced_grammar:
    practiced = [l['lessonId'] for l in all_lessons if g in l['grammarPracticed']]
    reviewed = [l['lessonId'] for l in all_lessons if g in l['grammarReviewed']]
    print(f"  {g}: Practiced in {len(practiced)} lessons, Reviewed in {len(reviewed)} lessons")

# 9. Communicative Functions Audit
print("\n=== 9. COMMUNICATIVE FUNCTIONS AUDIT ===")
cf_intro = Counter(cf for l in all_lessons for cf in l['communicativeFunctionsIntroduced'])
cf_prac = Counter(cf for l in all_lessons for cf in l['communicativeFunctionsPracticed'])
cf_rev = Counter(cf for l in all_lessons for cf in l['communicativeFunctionsReviewed'])
print(f"Communicative functions introduced: {dict(cf_intro)}")
print(f"Communicative functions practiced: {dict(cf_prac)}")
print(f"Communicative functions reviewed: {dict(cf_rev)}")

# 10. Pragmatic and Register Target Audit
print("\n=== 10. PRAGMATIC & REGISTER AUDIT ===")
pragmatics = Counter(l['pragmaticTarget'] for l in all_lessons)
registers = Counter(l['registerTarget'] for l in all_lessons)
print(f"Pragmatic targets: {dict(pragmatics)}")
print(f"Register targets: {dict(registers)}")

# 11. Phonology Audit
print("\n=== 11. PHONOLOGY AUDIT ===")
phono_intro = Counter(p for l in all_lessons for p in l['phonologyIntroduced'])
phono_prac = Counter(p for l in all_lessons for p in l['phonologyPracticed'])
phono_rev = Counter(p for l in all_lessons for p in l['phonologyReviewed'])
print(f"Phonology introduced: {dict(phono_intro)}")
print(f"Phonology practiced: {dict(phono_prac)}")
print(f"Phonology reviewed: {dict(phono_rev)}")

# 12. Audio Requirements Audit
print("\n=== 12. AUDIO REQUIREMENTS AUDIT ===")
audio_dist = Counter(l['audioSuitability'] for l in all_lessons)
print(f"Audio suitability distribution: {dict(audio_dist)}")
none_audio_with_purpose = [l['lessonId'] for l in all_lessons if l['audioSuitability'] == 'none' and l['audioPurpose'] is not None]
print(f"Lessons with audioSuitability='none' but non-null audioPurpose: {len(none_audio_with_purpose)}")
