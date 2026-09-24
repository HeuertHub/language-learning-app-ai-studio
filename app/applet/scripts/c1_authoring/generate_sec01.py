# -*- coding: utf-8 -*-
"""Author Section 01 of CEFR C1: Constitutional Law, Governance & Statutory Drafting.
Units 198 to 207 (10 units, 47 lessons).
"""
import json
import os

# Unit 198: The 1992 Democratic Constitution of Mongolia (PL=24, RL=27, PE=8, RE=6)
# Unit 199: Archaic & Classical Jussives: -сугай/-сүгэй & -тугай/-түгэй (PL=24, RL=27, PE=8, RE=6)
# Unit 200: Statutory Drafting & Legal Framing Formulations (PL=24, RL=27, PE=8, RE=6)
# Unit 201: Appositive Titles, Epithets & Chancellery Preambles (PL=24, RL=27, PE=8, RE=6)
# Unit 202: Causative Nominalizations in Institutional Governance (PL=24, RL=27, PE=8, RE=6)
# Unit 203: Courtroom Argumentation: Prosecutor & Defense Appeals (PL=22, RL=26, PE=8, RE=6)
# Unit 204: Constitutional Court (Үндсэн Хуулийн Цэц) Jurisprudence (PL=22, RL=26, PE=8, RE=6)
# Unit 205: Bilateral Concession Contracts & Investment Disputes (PL=22, RL=26, PE=8, RE=6)
# Unit 206: Drafting Executive & Ministerial Decrees (PL=22, RL=26, PE=8, RE=6)
# Unit 207: Constitutional Jurisprudence Capstone: Supreme Court Appeal (PL=26, RL=30, PE=11, RE=8)

sec01_lessons = [
  # ----------------------------------------------------
  # UNIT 198: The 1992 Democratic Constitution of Mongolia (5 lessons)
  # ----------------------------------------------------
  {
    "lessonId": "les_c1_198_01_administrative_chancellery_syntax_intro",
    "unitId": "unit_c1_198_the_1992_democratic_constitution_of",
    "cefrLevel": "C1",
    "sequenceWithinUnit": 1,
    "title": "Morphosyntax: Administrative Chancellery Architecture & Complex Nominal Embeddings",
    "lessonType": "grammar_introduction",
    "primaryPurpose": "Introduce the syntactic architecture of formal state chancellery Mongolian, characterized by multi-tiered participial nominalizations, genitive agent embeddings, and preposed non-finite clausal modifiers preceding statutory head nouns.",
    "communicativeOutcome": "Deconstruct and parse high-register legal sentences exceeding 40 words, isolating the main statutory predicate from nested institutional subordinate clauses without ambiguity.",
    "objectivesIntroduced": [
      "obj_c1_198_01_parse_chancellery_nominalizations"
    ],
    "objectivesPracticed": [],
    "objectivesReviewed": [
      "obj_b2_191_01_identify_genitive_subject_alternation"
    ],
    "grammarIntroduced": [
      "gram_c1_administrative_chancellery_syntax"
    ],
    "grammarPracticed": [
      "gram_b2_participle_relative_subject_genitive_alternation"
    ],
    "grammarReviewed": [
      "gram_b1_reported_speech_indirect_tense_shift"
    ],
    "phonologyIntroduced": [],
    "phonologyPracticed": [],
    "phonologyReviewed": [],
    "communicativeFunctionsIntroduced": [
      "comm_c1_04_statutory_legislative_drafting"
    ],
    "communicativeFunctionsPracticed": [],
    "communicativeFunctionsReviewed": [
      "comm_b2_09_formal_policy_recommendations"
    ],
    "newProductiveLemmaTarget": 5,
    "newReceptiveLemmaTarget": 6,
    "newProductiveExpressionTarget": 2,
    "newReceptiveExpressionTarget": 1,
    "lexicalDomains": [
      "lex_c1_jurisprudence_constitutional_law"
    ],
    "previousVocabularyReused": [
      "үндсэн хууль",
      "төрийн байгуулал",
      "бүрэн эрх",
      "засаглал",
      "хууль тогтоох",
      "шүүх засаглал"
    ],
    "readingObjective": "",
    "listeningObjective": "",
    "writingObjective": "",
    "spokenProductionObjective": "",
    "registerTarget": "state chancellery statutory",
    "pragmaticTarget": "institutional legal authority",
    "prerequisiteLessonIds": [
      "les_b2_197_06_b2_vantage_culminating_academic_capstone"
    ],
    "reviewsLessonIds": [
      "les_b2_191_01_relative_subject_case_alternation_syntax_intro"
    ],
    "reviewsUnitIds": [
      "unit_b2_191_relative_clause_subject_genitive_no"
    ],
    "reviewReason": "Extends B2 genitive-nominative relative clause subject alternation directly into complex state constitutional syntax.",
    "audioSuitability": "none",
    "audioPurpose": null,
    "successCriteria": [
      "Accurately maps the dependency hierarchy in statutory clauses containing triple-nested participial modifiers",
      "Distinguishes the governing judicial predicate from descriptive subordinate criteria in constitutional articles"
    ],
    "masteryEvidence": "Diagrams and translates the syntactic structure of a 45-word constitutional article into plain analytical discourse without losing deontic force.",
    "recommendedExerciseModalities": [
      "discourse_analysis",
      "sentence_reordering"
    ]
  },
  {
    "lessonId": "les_c1_198_02_constitutional_articles_parsing_reading",
    "unitId": "unit_c1_198_the_1992_democratic_constitution_of",
    "cefrLevel": "C1",
    "sequenceWithinUnit": 2,
    "title": "Statutory Reading: Sovereign Rights & Constitutional Separation of Powers",
    "lessonType": "reading",
    "primaryPurpose": "Parse an unabridged 520-word excerpt from Chapter 1 and Chapter 3 of the 1992 Democratic Constitution of Mongolia, examining sovereign rights declarations, parliamentary prerogatives, and executive checks.",
    "communicativeOutcome": "Extract precise institutional boundaries, statutory caveats, and legislative checks from authoritative constitutional articles.",
    "objectivesIntroduced": [
      "obj_c1_198_02_interpret_constitutional_declarations"
    ],
    "objectivesPracticed": [
      "obj_c1_198_01_parse_chancellery_nominalizations"
    ],
    "objectivesReviewed": [],
    "grammarIntroduced": [],
    "grammarPracticed": [
      "gram_c1_administrative_chancellery_syntax"
    ],
    "grammarReviewed": [
      "gram_b2_modal_complex_obligation_uchirtai"
    ],
    "phonologyIntroduced": [],
    "phonologyPracticed": [],
    "phonologyReviewed": [],
    "communicativeFunctionsIntroduced": [],
    "communicativeFunctionsPracticed": [
      "comm_c1_04_statutory_legislative_drafting"
    ],
    "communicativeFunctionsReviewed": [
      "comm_b2_02_parliamentary_interpellation"
    ],
    "newProductiveLemmaTarget": 5,
    "newReceptiveLemmaTarget": 6,
    "newProductiveExpressionTarget": 2,
    "newReceptiveExpressionTarget": 1,
    "lexicalDomains": [
      "lex_c1_jurisprudence_constitutional_law"
    ],
    "previousVocabularyReused": [
      "төрийн тэргүүн",
      "парламент",
      "хууль зүйн хороо",
      "халдашгүй дархан байдал"
    ],
    "readingObjective": "Analyze complex constitutional provisions detailing the division of executive, legislative, and judicial sovereignty.",
    "listeningObjective": "",
    "writingObjective": "",
    "spokenProductionObjective": "",
    "registerTarget": "constitutional judicial",
    "pragmaticTarget": "statutory exegesis",
    "prerequisiteLessonIds": [
      "les_c1_198_01_administrative_chancellery_syntax_intro"
    ],
    "reviewsLessonIds": [
      "les_b2_190_01_complex_obligation_uchirtai_syntax_intro"
    ],
    "reviewsUnitIds": [
      "unit_b2_190_complex_modal_obligation_the_modal_"
    ],
    "reviewReason": "Synthesizes teleological obligation markers with constitutional mandate formulations.",
    "audioSuitability": "none",
    "audioPurpose": null,
    "successCriteria": [
      "Identifies the precise constitutional conditions under which the President may veto parliamentary statutes",
      "Extracts the legal distinction between supreme state power and delegated executive administration"
    ],
    "masteryEvidence": "Answers 4 complex analytical queries comparing Mongolian separation of powers against semi-presidential systems based on text citations.",
    "recommendedExerciseModalities": [
      "source_comparison",
      "claim_evidence_matching"
    ]
  },
  {
    "lessonId": "les_c1_198_03_sovereign_rights_commentary_writing",
    "unitId": "unit_c1_198_the_1992_democratic_constitution_of",
    "cefrLevel": "C1",
    "sequenceWithinUnit": 3,
    "title": "Legal Commentary Writing: Jurisprudential Analysis of Article 16 Fundamental Rights",
    "lessonType": "writing",
    "primaryPurpose": "Author a 420-word scholarly legal commentary analyzing the scope and limitations of citizen fundamental rights under Article 16 of the Constitution, deploying state chancellery syntax.",
    "communicativeOutcome": "Produce rigorous juristic prose evaluating how constitutional rights are balanced against public security and statutory limitations.",
    "objectivesIntroduced": [
      "obj_c1_198_03_author_juristic_commentary"
    ],
    "objectivesPracticed": [
      "obj_c1_198_01_parse_chancellery_nominalizations"
    ],
    "objectivesReviewed": [],
    "grammarIntroduced": [],
    "grammarPracticed": [
      "gram_c1_administrative_chancellery_syntax"
    ],
    "grammarReviewed": [
      "gram_b2_voice_stacking_causative_passive"
    ],
    "phonologyIntroduced": [],
    "phonologyPracticed": [],
    "phonologyReviewed": [],
    "communicativeFunctionsIntroduced": [],
    "communicativeFunctionsPracticed": [
      "comm_c1_04_statutory_legislative_drafting"
    ],
    "communicativeFunctionsReviewed": [
      "comm_b2_13_scholarly_synthesis"
    ],
    "newProductiveLemmaTarget": 5,
    "newReceptiveLemmaTarget": 5,
    "newProductiveExpressionTarget": 2,
    "newReceptiveExpressionTarget": 2,
    "lexicalDomains": [
      "lex_c1_jurisprudence_constitutional_law"
    ],
    "previousVocabularyReused": [
      "иргэний эрх",
      "эрх чөлөө",
      "үндэсний аюулгүй байдал",
      "хязгаарлалт",
      "хууль дээдлэх"
    ],
    "readingObjective": "",
    "listeningObjective": "",
    "writingObjective": "Draft an authoritative legal commentary structuring constitutional arguments with multi-tiered nominalizations and formal syntactic connectors.",
    "spokenProductionObjective": "",
    "registerTarget": "academic juristic chancellery",
    "pragmaticTarget": "principled constitutional reasoning",
    "prerequisiteLessonIds": [
      "les_c1_198_02_constitutional_articles_parsing_reading"
    ],
    "reviewsLessonIds": [
      "les_b2_197_04_strategic_academic_consultation_brief_writing"
    ],
    "reviewsUnitIds": [
      "unit_b2_197_b2_vantage_capstone_academic_sympos"
    ],
    "reviewReason": "Bridges B2 strategic consultation brief composition into formal constitutional law commentary.",
    "audioSuitability": "none",
    "audioPurpose": null,
    "successCriteria": [
      "Structures arguments with clear distinction between unalienable rights and statutory regulatory reservations",
      "Deploys at least 4 complex participial nominalization constructions without syntactic breakdown"
    ],
    "masteryEvidence": "Submits a 420-word legal analysis of property rights and mineral wealth ownership under Article 6 adhering to chancellery style.",
    "recommendedExerciseModalities": [
      "summary_writing",
      "paragraph_reconstruction"
    ]
  },
  {
    "lessonId": "les_c1_198_04_constitutional_order_deliberation_spoken",
    "unitId": "unit_c1_198_the_1992_democratic_constitution_of",
    "cefrLevel": "C1",
    "sequenceWithinUnit": 4,
    "title": "Deliberative Speaking: Defending Constitutional Balances in Judicial Reform",
    "lessonType": "spoken_production",
    "primaryPurpose": "Engage in an advanced 4-minute spoken juristic defense of constitutional checks and balances during proposed amendments to the Law on Courts.",
    "communicativeOutcome": "Articulate nuanced constitutional principles orally, refuting unconstitutional executive encroachment with measured diplomatic authority.",
    "objectivesIntroduced": [
      "obj_c1_198_04_defend_constitutional_integrity_orally"
    ],
    "objectivesPracticed": [
      "obj_c1_198_01_parse_chancellery_nominalizations"
    ],
    "objectivesReviewed": [],
    "grammarIntroduced": [],
    "grammarPracticed": [
      "gram_c1_administrative_chancellery_syntax"
    ],
    "grammarReviewed": [
      "gram_b2_conditionals_hypothetical_present"
    ],
    "phonologyIntroduced": [],
    "phonologyPracticed": [],
    "phonologyReviewed": [],
    "communicativeFunctionsIntroduced": [],
    "communicativeFunctionsPracticed": [
      "comm_c1_04_statutory_legislative_drafting"
    ],
    "communicativeFunctionsReviewed": [
      "comm_b2_10_high_stakes_negotiation"
    ],
    "newProductiveLemmaTarget": 5,
    "newReceptiveLemmaTarget": 5,
    "newProductiveExpressionTarget": 1,
    "newReceptiveExpressionTarget": 1,
    "lexicalDomains": [
      "lex_c1_jurisprudence_constitutional_law"
    ],
    "previousVocabularyReused": [
      "шүүхийн хараат бус байдал",
      "шүүгчийн халдашгүй эрх",
      "хууль зүйн үр дагавар"
    ],
    "readingObjective": "",
    "listeningObjective": "",
    "writingObjective": "",
    "spokenProductionObjective": "Deliver an unscripted, authoritative oral argumentation analyzing the constitutional validity of proposed judicial oversight reforms.",
    "registerTarget": "formal parliamentary judicial",
    "pragmaticTarget": "firm diplomatic contestation",
    "prerequisiteLessonIds": [
      "les_c1_198_03_sovereign_rights_commentary_writing"
    ],
    "reviewsLessonIds": [
      "les_b2_189_01_hypothetical_conditionals_syntax_intro"
    ],
    "reviewsUnitIds": [
      "unit_b2_189_hypothetical_conditionals_in_academ"
    ],
    "reviewReason": "Applies B2 hypothetical conditionals (-вал... болохсон) to test constitutional counterfactuals during oral argumentation.",
    "audioSuitability": "native_speaker_preferred",
    "audioPurpose": "Provide high-register courtroom oral argumentation model demonstrating judicial pacing and controlled oratorical pauses.",
    "successCriteria": [
      "Refutes executive overreach proposals by directly citing constitutional sovereignty articles without colloquialisms",
      "Maintains controlled oratorical cadence (130-150 wpm) with precise juristic vocabulary"
    ],
    "masteryEvidence": "Performs a 4-minute simulated testimony before the Parliamentary Legal Standing Committee defending judicial independence.",
    "recommendedExerciseModalities": [
      "oral_presentation_planning",
      "rebuttal_transformation"
    ]
  },
  {
    "lessonId": "les_c1_198_05_parliamentary_debates_on_basic_law_listening",
    "unitId": "unit_c1_198_the_1992_democratic_constitution_of",
    "cefrLevel": "C1",
    "sequenceWithinUnit": 5,
    "title": "Acoustic Dissection: Authentic 1991–1992 Constitutional Drafting Debates",
    "lessonType": "listening",
    "primaryPurpose": "Listen to a 4-minute historical audio recording of the People's Great Khural (Ардын Их Хурал) plenary session debating the balance between state symbols, human rights, and the presidency.",
    "communicativeOutcome": "Comprehend elevated historical political oratory delivered at natural speed (155-175 wpm), tracking diverging philosophies on state sovereignty.",
    "objectivesIntroduced": [
      "obj_c1_198_05_comprehend_historical_parliamentary_debates"
    ],
    "objectivesPracticed": [
      "obj_c1_198_01_parse_chancellery_nominalizations"
    ],
    "objectivesReviewed": [],
    "grammarIntroduced": [],
    "grammarPracticed": [
      "gram_c1_administrative_chancellery_syntax"
    ],
    "grammarReviewed": [
      "gram_b2_discourse_focus_particles_l_ch"
    ],
    "phonologyIntroduced": [],
    "phonologyPracticed": [],
    "phonologyReviewed": [],
    "communicativeFunctionsIntroduced": [],
    "communicativeFunctionsPracticed": [
      "comm_c1_04_statutory_legislative_drafting"
    ],
    "communicativeFunctionsReviewed": [
      "comm_b2_02_parliamentary_interpellation"
    ],
    "newProductiveLemmaTarget": 4,
    "newReceptiveLemmaTarget": 5,
    "newProductiveExpressionTarget": 1,
    "newReceptiveExpressionTarget": 1,
    "lexicalDomains": [
      "lex_c1_jurisprudence_constitutional_law"
    ],
    "previousVocabularyReused": [
      "ардын их хурал",
      "депутат",
      "төрийн сүлд",
      "түүхэн уламжлал",
      "тусгаар тогтнол"
    ],
    "readingObjective": "",
    "listeningObjective": "Extract competing constitutional drafting positions, ideological premises, and rhetorical appeals from archival parliamentary debates.",
    "writingObjective": "",
    "spokenProductionObjective": "",
    "registerTarget": "historical oratorical parliamentary",
    "pragmaticTarget": "historical debate exegesis",
    "prerequisiteLessonIds": [
      "les_c1_198_02_constitutional_articles_parsing_reading"
    ],
    "reviewsLessonIds": [
      "les_b2_184_01_limiting_scalar_particles_syntax_intro"
    ],
    "reviewsUnitIds": [
      "unit_b2_184_focus_particles_and_scalar_pragmati"
    ],
    "reviewReason": "Scrutinizes how scalar particles (ч, л) alter political stance during intense historical legislative votes.",
    "audioSuitability": "native_speaker_required",
    "audioPurpose": "Provide authentic uncleaned historical plenary recording with acoustic background resonance of the Government House chamber.",
    "successCriteria": [
      "Identifies the precise ideological divergence between advocates of a parliamentary system versus a strong presidential model",
      "Transcribes nuanced archaic and formal legislative expressions spoken under emotional debate conditions"
    ],
    "masteryEvidence": "Synthesizes the core points of dispute from three distinct deputy speeches and charts their final resolution into the adopted text.",
    "recommendedExerciseModalities": [
      "extended_listening_comprehension",
      "stance_identification"
    ]
  }
]

print(f"Generated Unit 198: {len(sec01_lessons)} lessons.")
EOF
python3 scripts/c1_authoring/generate_sec01.py
