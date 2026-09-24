import type { CommunicativeFunctionSpec } from './dataCommunicative_A1';
import { communicativeA1Data } from './dataCommunicative_A1';
import { communicativeA2Data } from './dataCommunicative_A2';
import { communicativeB1B2Data } from './dataCommunicative_B1_B2';
import { communicativeC1C2Data } from './dataCommunicative_C1_C2';

export type { CommunicativeFunctionSpec };

/**
 * 145 Authoritative Fine-Grained Communicative Functions
 * Spanning Pre-A1 through C2 levels of Modern Standard Mongolian.
 * Organized across Interpersonal, Transactional, Informational, Narrative,
 * Academic, Professional, Cultural, and Ceremonial domains.
 */
export const communicativeFunctionsData: CommunicativeFunctionSpec[] = [
  ...communicativeA1Data,
  ...communicativeA2Data,
  ...communicativeB1B2Data,
  ...communicativeC1C2Data
];

/**
 * Macro Competencies (28 overarching curricular benchmarks)
 * Preserved for broad level-stage planning and cross-referencing.
 */
export interface MacroCompetencySpec {
  macroId: string;
  name: string;
  mongolianName: string;
  level: string;
  domain: string;
  prerequisites?: string[];
  description: string;
  fineGrainedFunctionIds: string[];
}

export const macroCompetenciesData: MacroCompetencySpec[] = [
  {
    macroId: "macro_a1_social_survival",
    name: "A1 Social Survival & Formality",
    mongolianName: "Анхан шатны харилцааны суурь",
    level: "A1",
    domain: "Interpersonal",
    description: "Master formulaic greetings, respectful elder salutations, departures, apologies, and basic personal identification.",
    fineGrainedFunctionIds: [
      "comm_a1_01_formulaic_greetings",
      "comm_a1_02_formal_elder_greetings",
      "comm_a1_03_departures_farewells",
      "comm_a1_04_expressing_gratitude",
      "comm_a1_05_apologies_pardon",
      "comm_a1_06_self_introduction_name",
      "comm_a1_07_origin_nationality",
      "comm_a1_08_professions_occupations",
      "comm_a1_09_introducing_others"
    ]
  },
  {
    macroId: "macro_a1_physical_environment",
    name: "A1 Physical Environment & Quantities",
    mongolianName: "Орчин тойрон, эд зүйлс, тоо ширхэг",
    level: "A1",
    domain: "Informational",
    description: "Identify everyday objects, establish possession, describe spatial location, and count items up to 100.",
    fineGrainedFunctionIds: [
      "comm_a1_10_identifying_objects",
      "comm_a1_11_ownership_possession",
      "comm_a1_12_location_simple_objects",
      "comm_a1_13_numbers_counting_1_to_100",
      "comm_a1_14_phone_numbers_contact"
    ]
  },
  {
    macroId: "macro_a1_food_and_commerce",
    name: "A1 Food, Beverage & Commerce",
    mongolianName: "Хоол хүнс ба худалдаа",
    level: "A1",
    domain: "Transactional",
    description: "Order traditional Mongolian dishes, inquire about ingredients/meats, purchase groceries, and settle bills.",
    fineGrainedFunctionIds: [
      "comm_a1_17_ordering_basic_food",
      "comm_a1_18_ordering_drinks_tea",
      "comm_a1_19_inquiring_food_ingredients",
      "comm_a1_20_asking_bill_payment",
      "comm_a1_21_grocery_market_quantities",
      "comm_a1_22_shopping_clothing_sizes",
      "comm_a1_23_bargaining_clarifying_price"
    ]
  },
  {
    macroId: "macro_a1_time_routines_transport",
    name: "A1 Time, Daily Life & Movement",
    mongolianName: "Цаг хугацаа, өдрийн дэглэм ба тээвэр",
    level: "A1",
    domain: "Transactional",
    description: "Ask/tell clock time, manage schedules, describe daily routines, hail transport, and navigate city streets.",
    fineGrainedFunctionIds: [
      "comm_a1_24_asking_clock_time",
      "comm_a1_25_days_of_the_week",
      "comm_a1_26_dates_months_calendar",
      "comm_a1_27_daily_routines_morning_evening",
      "comm_a1_28_asking_directions_street",
      "comm_a1_29_taking_public_bus",
      "comm_a1_30_hailing_street_taxi"
    ]
  },
  {
    macroId: "macro_a2_housing_and_hospitality",
    name: "A2 Housing & Steppe Hospitality",
    mongolianName: "Орон байр ба хөдөөгийн зочломтгой зан",
    level: "A2",
    domain: "Cultural",
    description: "Rent living quarters, describe ger/apartment layouts, follow guest etiquette, and understand livestock culture.",
    fineGrainedFunctionIds: [
      "comm_a2_04_renting_apartment_housing",
      "comm_a2_05_describing_home_rooms_furniture",
      "comm_a2_14_countryside_ger_visiting_etiquette",
      "comm_a2_15_nomadic_livestock_five_animals"
    ]
  },
  {
    macroId: "macro_a2_personal_history_and_social",
    name: "A2 Extended Family, Narrative & Social Interactions",
    mongolianName: "Хамаатан садан, дурсамж ба нийгмийн харилцаа",
    level: "A2",
    domain: "Narrative",
    description: "Introduce extended kinship, narrate past weekend and childhood memories, and extend/decline invitations.",
    fineGrainedFunctionIds: [
      "comm_a2_01_describing_extended_family",
      "comm_a2_02_describing_appearance_clothing",
      "comm_a2_03_describing_personality_character",
      "comm_a2_06_weekend_activities_past",
      "comm_a2_07_childhood_hometown_memories",
      "comm_a2_08_vacation_travel_experiences",
      "comm_a2_09_making_accepting_invitations",
      "comm_a2_10_declining_invitations_excuses"
    ]
  },
  {
    macroId: "macro_a2_practical_survival_services",
    name: "A2 Healthcare, Logistics & Services",
    mongolianName: "Эрүүл мэнд, үйлчилгээний байгууллага",
    level: "A2",
    domain: "Transactional",
    description: "Report symptoms to doctors, purchase medicine, buy train/bus tickets, use post and bank services, and report lost items.",
    fineGrainedFunctionIds: [
      "comm_a2_11_scheduling_rescheduling_meetings",
      "comm_a2_12_medical_symptoms_doctor",
      "comm_a2_13_buying_medicine_pharmacy",
      "comm_a2_17_giving_multistep_directions",
      "comm_a2_18_buying_bus_train_tickets",
      "comm_a2_19_postal_and_parcel_services",
      "comm_a2_20_banking_atm_currency_exchange",
      "comm_a2_28_describing_lost_items"
    ]
  },
  {
    macroId: "macro_b1_opinion_discourse_causality",
    name: "B1 Opinion Discourse & Logical Causality",
    mongolianName: "Байр суурь, шалтгаант холбоо, учир зүй",
    level: "B1",
    domain: "Informational",
    description: "Express nuanced opinions, respectful disagreement, logical causality, purpose statements, and hypothetical conditions.",
    fineGrainedFunctionIds: [
      "comm_b1_03_expressing_opinions_agreements",
      "comm_b1_04_respectful_disagreement",
      "comm_b1_05_making_causal_arguments",
      "comm_b1_06_stating_purpose_long_term_goals",
      "comm_b1_07_relaying_hearsay_news",
      "comm_b1_08_speculating_visual_evidence",
      "comm_b1_25_hypothetical_present_wishes"
    ]
  },
  {
    macroId: "macro_b1_professional_and_cultural",
    name: "B1 Professional Engagement & Cultural Heritage",
    mongolianName: "Мэргэжлийн харилцаа ба соёлын өв",
    level: "B1",
    domain: "Cultural",
    description: "Participate in job interviews, write formal emails, understand Tsagaan Sar and Naadam rituals, and discuss ecology.",
    fineGrainedFunctionIds: [
      "comm_b1_09_participating_job_interview",
      "comm_b1_10_writing_formal_email_letter",
      "comm_b1_13_discussing_environmental_issues",
      "comm_b1_14_traditional_celebrations_tsagaan_sar",
      "comm_b1_15_naadam_festival_three_games",
      "comm_b1_23_comparing_city_country_lifestyles",
      "comm_b1_24_discussing_education_career_path"
    ]
  },
  {
    macroId: "macro_b2_scholarly_debate_critique",
    name: "B2 Scholarly Debate, Essays & Policy Critique",
    mongolianName: "Эрдэм шинжилгээ, мэтгэлцээн, бодлогын шүүмж",
    level: "B2",
    domain: "Academic",
    prerequisites: ["macro_b1_opinion_discourse_causality"],
    description: "Participate in formal debates, write counter-theses, critique municipal policies, analyze macro trends, and moderate panels.",
    fineGrainedFunctionIds: [
      "comm_b2_01_participating_formal_debates",
      "comm_b2_02_academic_essay_concessions",
      "comm_b2_03_counterfactual_regrets",
      "comm_b2_04_analyzing_social_trends",
      "comm_b2_06_evaluating_public_policies",
      "comm_b2_07_delivering_prepared_presentations",
      "comm_b2_08_handling_qa_sessions",
      "comm_b2_09_moderating_group_discussions",
      "comm_b2_11_summarizing_complex_articles"
    ]
  },
  {
    macroId: "macro_b2_commercial_and_analytical",
    name: "B2 Commercial Negotiation & Analytical Chains",
    mongolianName: "Худалдааны хэлэлцээ ба дүн шинжилгээ",
    level: "B2",
    domain: "Professional",
    description: "Negotiate business contracts, interpret legal clauses, detail causal cascades, and explain quantitative data.",
    fineGrainedFunctionIds: [
      "comm_b2_05_business_negotiations_terms",
      "comm_b2_10_drafting_press_releases",
      "comm_b2_12_expository_causal_chains",
      "comm_b2_13_expressing_proportional_growth",
      "comm_b2_14_discourse_topic_framing",
      "comm_b2_15_employing_emphatic_nuance",
      "comm_b2_16_legal_contract_comprehension",
      "comm_b2_20_interpreting_graphs_statistics",
      "comm_b2_25_strategic_consultation"
    ]
  },
  {
    macroId: "macro_c1_executive_and_legislative",
    name: "C1 Executive, Protocol & Statutory Authority",
    mongolianName: "Төрийн ёслол, хууль тогтоомж, бодлогын баримт бичиг",
    level: "C1",
    domain: "Professional",
    description: "Master high-honorific registers, diplomatic protocol, legislative decree drafting, appellate legal arguments, and ministerial white papers.",
    fineGrainedFunctionIds: [
      "comm_c1_01_honorific_elder_conversations",
      "comm_c1_02_diplomatic_official_receptions",
      "comm_c1_03_drafting_executive_decrees",
      "comm_c1_04_statutory_legislative_drafting",
      "comm_c1_09_high_level_policy_briefs",
      "comm_c1_10_rhetorical_speechwriting",
      "comm_c1_11_courtroom_legal_argumentation",
      "comm_c1_12_consecutive_interpreting_support"
    ]
  },
  {
    macroId: "macro_c1_epistemic_and_philosophical",
    name: "C1 Epistemic Modesty & Philosophical Investigation",
    mongolianName: "Шинжлэх ухааны магадлал, гүн ухааны эрэл хайгуул",
    level: "C1",
    domain: "Academic",
    description: "Conduct peer review, modulate claims with epistemic hedging, debate ontology (-хуй), and evaluate literary translations.",
    fineGrainedFunctionIds: [
      "comm_c1_05_academic_peer_review",
      "comm_c1_06_hedging_scientific_claims",
      "comm_c1_07_investigative_journalism_reports",
      "comm_c1_08_philosophical_discourse",
      "comm_c1_13_editorial_counter_argumentation",
      "comm_c1_14_navigating_subtle_social_hierarchies",
      "comm_c1_15_literary_translation_evaluation"
    ]
  },
  {
    macroId: "macro_c2_colloquial_and_satirical_virtuosity",
    name: "C2 Colloquial Wit, Sarcasm & Omni-Register Agility",
    mongolianName: "Егөөдөл, хошигнол ба найруулгын төгс шилжилт",
    level: "C2",
    domain: "Interpersonal",
    description: "Deploy rapid colloquial banter, steppe irony, somatic idioms, satirical feuilletons, and fluid floor-holding in high-speed talk.",
    fineGrainedFunctionIds: [
      "comm_c2_01_rapid_colloquial_banter",
      "comm_c2_02_conversational_repair_turn_taking",
      "comm_c2_03_humor_sarcasm_irony",
      "comm_c2_04_somatic_steppe_idioms",
      "comm_c2_05_satirical_cultural_critique",
      "comm_c2_08_omni_register_agility"
    ]
  },
  {
    macroId: "macro_c2_poetic_philological_heritage",
    name: "C2 Poetic Mastery, Philology & Ceremonial Eloquence",
    mongolianName: "Яруу найраг, эх бичгийн ухаан, зан үйлийн үг хэллэг",
    level: "C2",
    domain: "Ceremonial",
    description: "Compose alliterative verse (толгой холболт), parse 13th-century Secret History excerpts, perform praise odes (магтаал) and ceremonial blessings (ерөөл).",
    fineGrainedFunctionIds: [
      "comm_c2_06_literary_polyphony_writing",
      "comm_c2_07_constitutional_court_parsing",
      "comm_c2_09_metric_alliterative_poetry",
      "comm_c2_10_secret_history_philological_reading",
      "comm_c2_11_ceremonial_blessings_performance",
      "comm_c2_12_praise_poetry_chanting",
      "comm_c2_13_proverbial_gnomic_deployment",
      "comm_c2_14_pan_mongolian_dialect_comprehension",
      "comm_c2_15_creative_mastery_authorial_voice"
    ]
  }
];
