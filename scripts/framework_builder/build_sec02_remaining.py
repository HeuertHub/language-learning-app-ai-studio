"""
Module providing Unit 28 and Unit 29 for Section 2.
"""

def add_units_28_and_29(u_map, lessons):
    # =========================================================================
    # UNIT 28: Telephone Numbers & Digital Contact Exchange (pos 28)
    # 5 Lessons | Targets: ProdLem=15, RecLem=5, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (5,1,2,1), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[28]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_28_01_telephone_digit_pairing",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Exchanging Phone Numbers: Digit Pairing Cadence",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce conventions for reading and dictating 8-digit Mongolian mobile numbers in standard four 2-digit pairs.",
            "communicativeOutcome": "State and dictate one's telephone number clearly using customary two-digit rhythmic grouping.",
            "objectivesIntroduced": ["obj_a1_28_01_dictate_paired_phone_numbers"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_27_02_count_decades_up_to_100"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": ["gram_a1_content_questions_be_ve"],
            "grammarReinforced": ["gram_a1_content_questions_be_ve"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_non_initial_reduction"],
            "communicativeFunctionsIntroduced": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["утас", "дугаар", "хэд"],
            "readingObjective": "Read printed business cards and digital advertisements displaying 8-digit phone numbers.",
            "listeningObjective": "Hear paired two-digit phone numbers (e.g. 9911-2233 as ерэн ес, арван нэг, хорин хоёр, гучин гурав).",
            "writingObjective": "Write down 4 dictated 8-digit telephone numbers in hyphenated pair format.",
            "spokenProductionObjective": "Recite a personal or institutional telephone number using paired number cadence.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear pacing with pauses between digit pairs to allow verification.",
            "prerequisiteLessonIds": ["les_a1_27_06_counting_dialogue_synthesis"],
            "reviewsLessonIds": ["les_a1_27_02_tens_and_counting_to_100"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Recycle two-digit decade numbers into practical telecommunications usage.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Rhythmic two-digit prosodic chunking with inter-pair pauses.",
            "successCriteria": [
                "Dictate 8-digit numbers in 4 two-digit groups (e.g. 88-12-34-56).",
                "Ask for contact details politely with 'Утасны дугаар тань хэд вэ?'."
            ],
            "masteryEvidence": [
                "Accurately transcribes 3 audio phone numbers without digit errors.",
                "Recites assigned phone number smoothly during oral prompt."
            ],
            "recommendedExerciseModalities": ["number_dictation", "cued_production", "matching"]
        },
        {
            "lessonId": "les_a1_28_02_digital_channels_email_social",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Digital Contacts: Email, Messaging Apps, and Usernames",
            "lessonType": "vocabulary_introduction",
            "primaryPurpose": "Introduce vocabulary for digital communication channels (и-мэйл, фэйсбүүк, хаяг, чат) and address symbols.",
            "communicativeOutcome": "Exchange email addresses and social messaging handles with peers and service personnel.",
            "objectivesIntroduced": ["obj_a1_28_02_exchange_digital_addresses"],
            "objectivesPracticed": ["obj_a1_28_01_dictate_paired_phone_numbers"],
            "objectivesReviewed": ["obj_a1_26_02_use_interrogative_pronouns"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_loanword_adaptation"],
            "phonologyReviewed": ["phono_vowel_harmony_intro"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["хаяг", "нэр", "утас"],
            "readingObjective": "Read contact information sections on social media profiles and business cards.",
            "listeningObjective": "Comprehend spoken spelling of email handles and contact domains.",
            "writingObjective": "Fill out a contact card with name, mobile number, and email address.",
            "spokenProductionObjective": "Spell out one's email address and handle in Mongolian discourse.",
            "registerTarget": "Everyday standard friendly and professional",
            "pragmaticTarget": "Offering digital contact alternatives when phone calling is inconvenient.",
            "prerequisiteLessonIds": ["les_a1_28_01_telephone_digit_pairing"],
            "reviewsLessonIds": ["les_a1_26_02_interrogative_pronoun_inventory"],
            "reviewsUnitIds": ["unit_a1_26_content_question_particles_and_"],
            "reviewReason": "Utilize 'ямар' and 'хэд' in contact inquiries (Ямар хаягтай вэ?).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Pronunciation of digital terms and international loanwords with Mongolian phonological adaptation.",
            "successCriteria": [
                "Pronounce '@' (at / гогцоо) and '.' (цэг) correctly in email dictation.",
                "Formulate questions asking for contact channels fluently."
            ],
            "masteryEvidence": [
                "Produces 'Таны и-мэйл хаяг юу вэ?' upon prompt.",
                "Transcribes digital handle dictation with zero typos."
            ],
            "recommendedExerciseModalities": ["dictation", "card_completion", "matching"]
        },
        {
            "lessonId": "les_a1_28_03_business_card_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Reading Workshop: Mongolian Business Cards (Нэрийн хуудас)",
            "lessonType": "reading_development",
            "primaryPurpose": "Read and analyze authentic Mongolian business cards (нэрийн хуудас) and civic directory listings.",
            "communicativeOutcome": "Extract professional titles, institutional affiliations, phone numbers, and physical addresses from business cards.",
            "objectivesIntroduced": ["obj_a1_28_03_read_business_cards"],
            "objectivesPracticed": [
                "obj_a1_28_01_dictate_paired_phone_numbers",
                "obj_a1_28_02_exchange_digital_addresses"
            ],
            "objectivesReviewed": ["obj_a1_25_03_read_building_directories"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_case_dative_locative_location"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_soft_and_hard_signs"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_05_asking_identity_origin"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 2, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["компани", "мэргэжил", "хот", "өрөө"],
            "readingObjective": "Read 4 diverse business cards representing an engineer, doctor, teacher, and entrepreneur.",
            "listeningObjective": None,
            "writingObjective": "Transcribe contact info from 3 business cards into a contact directory format.",
            "spokenProductionObjective": None,
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Understanding formal layout conventions of professional networking cards.",
            "prerequisiteLessonIds": ["les_a1_28_02_digital_channels_email_social"],
            "reviewsLessonIds": ["les_a1_25_03_urban_directory_reading"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine contact reading with previously learned spatial building addresses.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration reading professional titles with appropriate formal deference.",
            "successCriteria": [
                "Correctly locate the mobile phone number vs office landline on the card.",
                "Identify the company name and job title from visual hierarchy."
            ],
            "masteryEvidence": [
                "Fills out 4 contact profiles from business card scans with 100% accuracy.",
                "Identifies the abbreviations 'утас', 'факс', 'шуудан'."
            ],
            "recommendedExerciseModalities": ["document_scanning", "form_filling", "matching"]
        },
        {
            "lessonId": "les_a1_28_04_rapid_digit_listening_lab",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Acoustic Lab: Transcribing Spoken Phone Numbers in Voicemails",
            "lessonType": "listening_development",
            "primaryPurpose": "Transcribe spoken phone numbers and callback requests from recorded voicemail messages and announcements.",
            "communicativeOutcome": "Accurately record callback numbers left on voicemail messages without playback distortion.",
            "objectivesIntroduced": ["obj_a1_28_04_transcribe_voicemail_digits"],
            "objectivesPracticed": ["obj_a1_28_01_dictate_paired_phone_numbers"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_numerals_cardinal_1_100"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_oe_ue_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["утас", "дугаар", "ярих", "хэлэх"],
            "readingObjective": None,
            "listeningObjective": "Listen to 5 voicemail callback messages and write down the caller name and 8-digit phone number.",
            "writingObjective": "Transcribe 5 phone numbers into a telephone message slip.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Accurate message taking for third parties.",
            "prerequisiteLessonIds": ["les_a1_28_02_digital_channels_email_social"],
            "reviewsLessonIds": ["les_a1_27_05_auditory_number_lab"],
            "reviewsUnitIds": ["unit_a1_27_cardinal_numbers_counting_up_to_one"],
            "reviewReason": "Zero-vocabulary listening lab cementing auditory number transcription.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Authentic telephone audio filter with slight bandwidth compression.",
            "successCriteria": [
                "Transcribe 5 out of 5 phone numbers with zero digit inversions or omissions.",
                "Identify caller identity and reason for calling from brief voicemail audio."
            ],
            "masteryEvidence": [
                "Produces flawless message slips from audio prompts.",
                "Catches fast spoken number corrections ('Үгүй, 99 биш, 95')."
            ],
            "recommendedExerciseModalities": ["voicemail_transcription", "error_spotting", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_28_05_contact_exchange_roleplay",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Interactive Synthesis: Networking and Exchanging Contacts",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Simulate a networking reception where participants introduce themselves and exchange full contact dossiers.",
            "communicativeOutcome": "Politely ask for, provide, and verify phone numbers and messaging accounts in a social setting.",
            "objectivesIntroduced": ["obj_a1_28_05_execute_contact_exchange"],
            "objectivesPracticed": [
                "obj_a1_28_01_dictate_paired_phone_numbers",
                "obj_a1_28_02_exchange_digital_addresses"
            ],
            "objectivesReviewed": ["obj_a1_01_formal_greeting_morning_afternoon"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_content_questions_be_ve"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_stress_initial_and_full_vowels"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_11_counting_simple_quantities"],
            "communicativeFunctionsReviewed": ["comm_a1_01_formal_greeting_morning_afternoon"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_numbers_time_calendar"],
            "previousVocabularyReused": ["нэр", "ажил", "утас", "хаяг", "баяртай"],
            "readingObjective": "Read role profile cards with personal contact credentials.",
            "listeningObjective": "Comprehend partner's dictated contact numbers and read them back for confirmation.",
            "writingObjective": "Write 2 complete contact records collected during peer interviews.",
            "spokenProductionObjective": "Execute an 8-turn networking conversation exchanging full contact details.",
            "registerTarget": "Courteous standard professional",
            "pragmaticTarget": "Using two-handed business card etiquette and repeating numbers back to confirm accuracy.",
            "prerequisiteLessonIds": [
                "les_a1_28_03_business_card_reading",
                "les_a1_28_04_rapid_digit_listening_lab"
            ],
            "reviewsLessonIds": ["les_a1_28_01_telephone_digit_pairing"],
            "reviewsUnitIds": ["unit_a1_28_telephone_numbers_digital_contact_e"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 28 contact skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Natural conversational tempo with polite confirmation repetition.",
            "successCriteria": [
                "Perform standard read-back verification ('Таны утас 9911-2233 тийм үү?').",
                "Exchange all contact details fluently without communication breakdowns."
            ],
            "masteryEvidence": [
                "Completes reciprocal contact exchange within 90 seconds flawlessly.",
                "Both partners record identical phone numbers on their peer logs."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "peer_verification"]
        }
    ])

    # =========================================================================
    # UNIT 29: Nominal Plurality Suffixes: -ууд/-үүд, -нууд/-нүүд, -д, -с (pos 29)
    # 6 Lessons | Targets: ProdLem=17, RecLem=6, ProdExp=4, RecExp=2
    # Budget: (5,2,1,1), (5,2,1,0), (4,1,1,1), (3,1,1,0), (0,0,0,0), (0,0,0,0)
    # =========================================================================
    u = u_map[29]
    uid = u["unitId"]
    lessons.extend([
        {
            "lessonId": "les_a1_29_01_plural_uud_allomorphs",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 1,
            "title": "Making Plurals: Regular Suffixes -ууд and -үүд",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce regular nominal plural suffixes -ууд (back vowel) and -үүд (front vowel) attached to consonant-final inanimate stems.",
            "communicativeOutcome": "Formulate plural nouns referring to multiple objects and furnishings correctly adhering to vowel harmony.",
            "objectivesIntroduced": ["obj_a1_29_01_form_regular_plurals_uud"],
            "objectivesPracticed": [], "objectivesReviewed": ["obj_a1_24_01_affirm_existence_baina"],
            "grammarIntroduced": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarPracticed": [], "grammarReviewed": ["gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_existential_baina_baihgui"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_vowel_length_contrast"],
            "communicativeFunctionsIntroduced": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsPracticed": [], "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ном", "ширээ", "сандал", "дэвтэр"],
            "readingObjective": "Read simple plural sentences identifying items in living spaces (e.g. 'Номууд ширээн дээр байна').",
            "listeningObjective": "Hear the acoustic contrast between singular bare stems and plural suffixed nouns (дэвтэр vs дэвтрүүд).",
            "writingObjective": "Attach -ууд or -үүд to 6 singular consonant-final nouns based on vowel harmony.",
            "spokenProductionObjective": "State aloud the plurals of 4 common classroom and household items.",
            "registerTarget": "Everyday standard neutral",
            "pragmaticTarget": "Clear plural reference when specifying groups of identical entities.",
            "prerequisiteLessonIds": ["les_a1_28_05_contact_exchange_roleplay"],
            "reviewsLessonIds": ["les_a1_24_01_existential_assertion_baina"],
            "reviewsUnitIds": ["unit_a1_24_existential_assertion_vs_"],
            "reviewReason": "Combine newly pluralized nouns with existential predicate 'байна'.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Acoustic modeling of rounded long vowel harmony in -ууд vs -үүд.",
            "successCriteria": [
                "Select -ууд for back-vowel masculine stems and -үүд for front-vowel feminine stems.",
                "Accurately apply vowel syncope where required (дэвтэр -> дэвтрүүд)."
            ],
            "masteryEvidence": [
                "Produces 'номууд' and 'дэвтрүүд' with correct spelling and pronunciation.",
                "Remembers not to use plural suffixes after numerals (e.g. rejects 'хоёр номууд')."
            ],
            "recommendedExerciseModalities": ["suffix_attachment", "vowel_harmony_sorting", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_29_02_plural_nuud_and_human_plurals",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 2,
            "title": "Vowel Stems and Social Plurals: -нууд/-нүүд and -нар",
            "lessonType": "grammar_introduction",
            "primaryPurpose": "Introduce plural suffixes -нууд/-нүүд for vowel-final nouns and the associative/honorific collective plural marker -нар for human kinship and titles.",
            "communicativeOutcome": "Form plurals of vowel-final words and address groups of people politely (e.g. багш нар, эмч нар, хүүхдүүд).",
            "objectivesIntroduced": ["obj_a1_29_02_apply_nuud_and_nar_plurals"],
            "objectivesPracticed": ["obj_a1_29_01_form_regular_plurals_uud"],
            "objectivesReviewed": ["obj_a1_17_01_personal_pronouns"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarReviewed": ["gram_a1_nominal_predicate_zero_copula"],
            "grammarReinforced": ["gram_a1_nominal_predicate_zero_copula"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_03_introduce_peer_third_party"],
            "newProductiveLemmaTarget": 5, "newReceptiveLemmaTarget": 2,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["багш", "эмч", "оюутан", "хүүхэд", "ах"],
            "readingObjective": "Read short staff and student roster descriptions mentioning groups (багш нар, оюутнууд).",
            "listeningObjective": "Discriminate between individual titles and plural groups in speech (эмч vs эмч нар).",
            "writingObjective": "Write sentences contrasting vowel-stem plurals and kinship group terms.",
            "spokenProductionObjective": "Introduce a group of 3 professions or family members aloud.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Using -нар respectfully when referring to elders, teachers, and professionals.",
            "prerequisiteLessonIds": ["les_a1_29_01_plural_uud_allomorphs"],
            "reviewsLessonIds": ["les_a1_17_01_singular_pronouns_subject_slots"],
            "reviewsUnitIds": ["unit_a1_17_personal_pronouns_direct_address_pr"],
            "reviewReason": "Align third-person plural pronouns (тэд) with plural noun phrases (оюутнууд, багш нар).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Natural prosody linking nouns with independent collective marker 'нар'.",
            "successCriteria": [
                "Attach -нууд/-нүүд to vowel-final stems (өрөөнүүд, тоонууд).",
                "Apply separate word 'нар' for respected people and professions."
            ],
            "masteryEvidence": [
                "Selects 'багш нар' rather than *багшууд.",
                "Transforms 'хүүхэд' into irregular plural 'хүүхдүүд' accurately."
            ],
            "recommendedExerciseModalities": ["categorization", "sentence_transformation", "cloze_selection"]
        },
        {
            "lessonId": "les_a1_29_03_plural_syntactic_drills",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 3,
            "title": "Guided Practice: Plurals in Locative and Existential Clauses",
            "lessonType": "grammar_guided_practice",
            "primaryPurpose": "Automate combining plural nouns with dative-locative case markers (-уудад/-үүдэд) and existential predicates.",
            "communicativeOutcome": "Describe the presence, location, and absence of plural entities in complex environments.",
            "objectivesIntroduced": ["obj_a1_29_03_combine_plurals_with_cases"],
            "objectivesPracticed": [
                "obj_a1_29_01_form_regular_plurals_uud",
                "obj_a1_29_02_apply_nuud_and_nar_plurals"
            ],
            "objectivesReviewed": ["obj_a1_25_01_apply_dative_locative_suffixes"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_case_dative_locative_location"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_oe_ue_contrast"],
            "phonologyReviewed": ["phono_vowel_harmony_suffixes"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_12_location_simple_objects"],
            "newProductiveLemmaTarget": 4, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 1,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["өрөө", "сургууль", "танхим", "ном", "сандал"],
            "readingObjective": "Read campus facility descriptions identifying where multiple resources are located.",
            "listeningObjective": "Comprehend rapid spoken statements regarding locations of groups of people and items.",
            "writingObjective": "Construct 4 sentences combining plural nouns, locative case markers, and existential verbs.",
            "spokenProductionObjective": "Describe 3 groups of items currently present in a library or workshop.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Detailed spatial reporting of inventory distributions.",
            "prerequisiteLessonIds": ["les_a1_29_02_plural_nuud_and_human_plurals"],
            "reviewsLessonIds": ["les_a1_25_01_dative_locative_allomorphs"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Attach dative-locative case (-д/-т) onto pluralized noun bases (-уудад/-үүдэд).",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Clarity in multi-suffix phonological sequencing.",
            "successCriteria": [
                "Attach dative suffix -ад/-эдэд accurately onto plural stems (сандлуудад, өрөөнүүдэд).",
                "Ensure correct predicate agreement in SOV order."
            ],
            "masteryEvidence": [
                "Produces 'Эдгээр номууд өрөөнд байна' without hesitation.",
                "Identifies and corrects singular/plural mismatches in 5 test sentences."
            ],
            "recommendedExerciseModalities": ["sentence_construction", "error_spotting", "cued_production"]
        },
        {
            "lessonId": "les_a1_29_04_library_catalog_reading",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 4,
            "title": "Reading Workshop: Library Catalog and Resource Guides",
            "lessonType": "reading_development",
            "primaryPurpose": "Read and navigate university library section guides, catalog classifications, and archive descriptions.",
            "communicativeOutcome": "Locate desired book categories, reference materials, and study rooms from printed directories.",
            "objectivesIntroduced": ["obj_a1_29_04_read_library_catalogs"],
            "objectivesPracticed": ["obj_a1_29_01_form_regular_plurals_uud"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarReviewed": ["gram_a1_case_dative_locative_location"],
            "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_neutral_vowel_behavior"],
            "phonologyReviewed": [],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 3, "newReceptiveLemmaTarget": 1,
            "newProductiveExpressionTarget": 1, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ном", "толь", "сонин", "сэтгүүл", "давхар"],
            "readingObjective": "Read a 55-word library floor guide detailing locations of books, magazines, and dictionaries.",
            "listeningObjective": None,
            "writingObjective": "Write a short summary list of 4 resource collections found on each library floor.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard educational",
            "pragmaticTarget": "Independent academic navigation in institutional libraries.",
            "prerequisiteLessonIds": ["les_a1_29_03_plural_syntactic_drills"],
            "reviewsLessonIds": ["les_a1_25_03_urban_directory_reading"],
            "reviewsUnitIds": ["unit_a1_25_dative_locative_spatial_anchoring_s"],
            "reviewReason": "Combine library collection plurals with spatial floor coordinates.",
            "audioSuitability": "standard_speech_synthesis_acceptable",
            "audioPurpose": "Narration modeling academic library informational announcements.",
            "successCriteria": [
                "Identify floor locations for 4 distinct publication categories (номоуд, сэтгүүлүүд, толиуд).",
                "Answer 3 factual reading comprehension questions accurately."
            ],
            "masteryEvidence": [
                "Matches catalog headings to floor numbers with zero error.",
                "Translates 3 plural catalog entries accurately into English."
            ],
            "recommendedExerciseModalities": ["document_scanning", "matching", "short_answer"]
        },
        {
            "lessonId": "les_a1_29_05_plural_acoustic_discrimination",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 5,
            "title": "Acoustic Lab: Singular vs Plural Discrimination in Rapid Speech",
            "lessonType": "listening_development",
            "primaryPurpose": "Train the ear to differentiate singular nouns from reduced plural endings in natural conversational streams.",
            "communicativeOutcome": "Reliably detect whether a speaker is referring to one item/person or a group in fast discourse.",
            "objectivesIntroduced": ["obj_a1_29_05_discriminate_singular_plural_auditorily"],
            "objectivesPracticed": ["obj_a1_29_01_form_regular_plurals_uud"],
            "objectivesReviewed": [],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarReviewed": [], "grammarReinforced": [],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_non_initial_reduction"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": [],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["ном", "сандал", "багш", "оюутан", "хүүхэд"],
            "readingObjective": None,
            "listeningObjective": "Listen to 8 rapid sentences and classify each subject noun as singular [1] or plural [>1].",
            "writingObjective": "Record the heard singular/plural status on a rapid classification score sheet.",
            "spokenProductionObjective": None,
            "registerTarget": "Everyday standard colloquial",
            "pragmaticTarget": "Accurate quantity tracking without visual confirmation.",
            "prerequisiteLessonIds": ["les_a1_29_03_plural_syntactic_drills"],
            "reviewsLessonIds": ["les_a1_29_01_plural_uud_allomorphs"],
            "reviewsUnitIds": ["unit_a1_29_nominal_plurality_suffixes_"],
            "reviewReason": "Acoustic sharpening of plural suffix perception in continuous speech.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Realistic conversational recordings featuring natural reduction of unaccented plural vowels.",
            "successCriteria": [
                "Correctly classify 8 out of 8 spoken sentences into singular vs plural categories.",
                "Detect reduced -нууд/-нүүд endings even when spoken softly."
            ],
            "masteryEvidence": [
                "Identifies that 'хүүхдүүд' was spoken rather than 'хүүхэд' across 4 audio trials.",
                "Transcribes suffix endings with 100% orthographic accuracy."
            ],
            "recommendedExerciseModalities": ["binary_choice", "audio_transcription", "error_detection"]
        },
        {
            "lessonId": "les_a1_29_06_group_description_synthesis",
            "unitId": uid, "cefrLevel": "A1", "sequenceWithinUnit": 6,
            "title": "Interactive Synthesis: Workplace and Facility Asset Audit",
            "lessonType": "dialogue_work",
            "primaryPurpose": "Synthesize nominal plurals, numerals, and locative descriptions in a collaborative facility audit.",
            "communicativeOutcome": "Discuss, compare, and inventory groups of people and furnishings across multiple work areas.",
            "objectivesIntroduced": ["obj_a1_29_06_conduct_group_asset_dialogue"],
            "objectivesPracticed": [
                "obj_a1_29_01_form_regular_plurals_uud",
                "obj_a1_29_02_apply_nuud_and_nar_plurals",
                "obj_a1_29_03_combine_plurals_with_cases"
            ],
            "objectivesReviewed": ["obj_a1_27_01_count_cardinals_1_to_20"],
            "grammarIntroduced": [], "grammarPracticed": ["gram_a1_nominal_plural_uud_nuud"],
            "grammarReviewed": ["gram_a1_numerals_cardinal_1_100", "gram_a1_existential_baina_baihgui"],
            "grammarReinforced": ["gram_a1_numerals_cardinal_1_100"],
            "phonologyIntroduced": [], "phonologyPracticed": ["phono_vowel_harmony_suffixes"],
            "phonologyReviewed": ["phono_stress_initial_and_full_vowels"],
            "communicativeFunctionsIntroduced": [],
            "communicativeFunctionsPracticed": ["comm_a1_10_identifying_objects"],
            "communicativeFunctionsReviewed": ["comm_a1_11_counting_simple_quantities"],
            "newProductiveLemmaTarget": 0, "newReceptiveLemmaTarget": 0,
            "newProductiveExpressionTarget": 0, "newReceptiveExpressionTarget": 0,
            "lexicalDomains": ["lex_a1_housing_ger_household"],
            "previousVocabularyReused": ["өрөө", "ширээ", "сандал", "компьютер", "оюутнууд", "багш нар"],
            "readingObjective": "Read an audit briefing describing expected vs missing resources.",
            "listeningObjective": "Comprehend partner's verbal inventory report regarding various facility wings.",
            "writingObjective": "Draft a 4-sentence audit summary report using accurate plural nouns and locative endings.",
            "spokenProductionObjective": "Participate in an 8-turn roleplay comparing resources across two campuses.",
            "registerTarget": "Everyday standard courteous",
            "pragmaticTarget": "Collaborative professional reporting with clear distinction between single and multiple assets.",
            "prerequisiteLessonIds": [
                "les_a1_29_04_library_catalog_reading",
                "les_a1_29_05_plural_acoustic_discrimination"
            ],
            "reviewsLessonIds": ["les_a1_29_03_plural_syntactic_drills"],
            "reviewsUnitIds": ["unit_a1_29_nominal_plurality_suffixes_"],
            "reviewReason": "Zero-vocabulary interactive synthesis consolidating all Unit 29 plural skills.",
            "audioSuitability": "mongolian_voice_required",
            "audioPurpose": "Exemplary conversational exchange illustrating collaborative reporting.",
            "successCriteria": [
                "Maintain flawless distinction between numeral constructions (three chairs -> гурван сандал) and general plurals (chairs -> сандлууд).",
                "Use -нар respectfully with human professions throughout oral interaction."
            ],
            "masteryEvidence": [
                "Demonstrates zero instances of ungrammatical *гурван сандлууд during the 8-turn dialogue.",
                "Produces grammatically pristine written audit notes."
            ],
            "recommendedExerciseModalities": ["dialogue_roleplay", "information_gap", "audit_reconciliation"]
        }
    ])
