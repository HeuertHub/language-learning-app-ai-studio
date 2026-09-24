# -*- coding: utf-8 -*-
import json

c1 = json.load(open('curriculum/lesson_blueprints/c1_complete.json'))
b2 = json.load(open('curriculum/lesson_blueprints/b2_complete.json'))
units = json.load(open('curriculum/blueprint/units/c1.json'))

sec01 = [l for l in c1 if 198 <= int(l['unitId'].split('_')[2]) <= 207]
sec02 = [l for l in c1 if 208 <= int(l['unitId'].split('_')[2]) <= 217]
sec03 = [l for l in c1 if 218 <= int(l['unitId'].split('_')[2]) <= 228]

def sample_section(sec_lessons, n=20):
    indices = [0, 1, 2, 3]
    middle = list(range(4, len(sec_lessons) - 4))
    step = len(middle) / 12
    middle_indices = [middle[int(i * step)] for i in range(12)]
    indices.extend(middle_indices)
    indices.extend([len(sec_lessons)-4, len(sec_lessons)-3, len(sec_lessons)-2, len(sec_lessons)-1])
    return [sec_lessons[i] for i in indices]

s1 = sample_section(sec01, 20)
s2 = sample_section(sec02, 20)
s3 = sample_section(sec03, 20)
all_sampled = s1 + s2 + s3

print("Total sampled:", len(all_sampled))

# Check grammar recurrence across all C1
grammars_c1 = [
    "gram_c1_legal_statutory_framing",
    "gram_c1_archaic_classical_jussives_khugai",
    "gram_c1_causative_passive_chains_legal_attribution",
    "gram_c1_impersonal_statutory_constructions",
    "gram_c1_academic_nominalization_frames",
    "gram_c1_academic_hedging_and_epistemic_stance",
    "gram_c1_journalistic_evidential_distancing",
    "gram_c1_rhetorical_inversion_and_clefting",
    "gram_c1_adversative_concessive_connectors_formal",
    "gram_c1_register_switching_matrix",
    "gram_c1_honorific_lexical_verbs",
    "gram_c1_honorific_suppletive_existentials",
    "gram_c1_honorific_nouns_and_somatic_terms",
    "gram_c1_honorific_humble_forms_object_elevation",
    "gram_c1_honorific_imperative_gtun_no_uu",
    "gram_c1_classical_converbs_vaas_khuits",
    "gram_c1_classical_temporal_khlaar",
    "gram_c1_classical_quotative_khemeen",
    "gram_c1_classical_participle_khui"
]

print("\n--- GRAMMAR RECURRENCE AUDIT ---")
for g in grammars_c1:
    intro = [l['lessonId'] for l in c1 if g in l['grammarIntroduced']]
    pract = [l['lessonId'] for l in c1 if g in l['grammarPracticed']]
    rev = [l['lessonId'] for l in c1 if g in l['grammarReviewed']]
    total_app = len(intro) + len(pract) + len(rev)
    print(f"{g:50s} Intro: {len(intro)} | Pract: {len(pract):2d} | Rev: {len(rev):2d} | Total: {total_app:2d}")
    if total_app < 2:
        print(f"  WARNING: Isolated grammar: {g}")

# Check Honorifics lessons
print("\n--- HONORIFICS UNITS INSPECTION ---")
hon_units = [u for u in units if "honorific" in u['unitId'] or "humble" in u['unitId'] or "imperative" in u['unitId']]
for u in hon_units:
    u_lessons = [l for l in c1 if l['unitId'] == u['unitId']]
    print(f"Unit {u['sequencePosition']}: {u['title']} ({len(u_lessons)} lessons)")
    for l in u_lessons:
        print(f"   [{l['lessonType']}] {l['lessonId']}: {l['title']}")
        print(f"      Pragmatic target: {l['pragmaticTarget']}")
        print(f"      Outcome: {l['communicativeOutcome'][:90]}...")
