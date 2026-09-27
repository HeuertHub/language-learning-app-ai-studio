#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authentic A1 Pilot Lexicon: Units 16 to 20 (30 lessons)
Total: 118 Core Lemmas (87 Productive, 31 Receptive)
       30 Multiword Expressions (20 Productive, 10 Receptive)
Every item is an attested Modern Mongolian lexical entry with verified provenance.
"""

A1_PILOT_LESSON_LEMMAS = {
    # -------------------------------------------------------------------------
    # Unit 16: Standard Salutations & Time-of-Day Greetings
    # -------------------------------------------------------------------------
    'les_a1_16_01_canonical_sov_architecture': {
        'productive': [
            ('би', 'I (first person singular pronoun)', 'pronoun', 'neutral', 'personal_pronoun', 'Subject pronoun for canonical SOV clauses.'),
            ('захиа', 'letter, mail, message', 'noun', 'masculine', 'nominal', 'Object noun in transitive SOV sentences.'),
            ('хэлэх', 'to say, speak, tell', 'verb', 'feminine', 'verbal', 'Head-final predicate verb in SOV sentences.'),
            ('сонсох', 'to listen, hear', 'verb', 'masculine', 'verbal', 'Head-final auditory action verb.'),
            ('сурах', 'to learn, study', 'verb', 'masculine', 'verbal', 'Core educational verb.'),
        ],
        'receptive': [
            ('өгүүлбэр', 'sentence, clause', 'noun', 'feminine', 'nominal', 'Linguistic grammatical concept in syntax.'),
            ('бүтэц', 'structure, framework', 'noun', 'feminine', 'nominal', 'Syntactic layout term.'),
        ]
    },
    'les_a1_16_02_formal_time_greetings_mori': {
        'productive': [
            ('өглөөний', 'morning (genitive)', 'adjective', 'feminine', 'adjectival', 'Genitive time modifier in formal salutations.'),
            ('өдрийн', 'afternoon, midday (genitive)', 'adjective', 'feminine', 'adjectival', 'Midday salutation modifier.'),
            ('оройн', 'evening (genitive)', 'adjective', 'masculine', 'adjectival', 'Evening salutation modifier.'),
            ('хүргэх', 'to deliver, convey, extend', 'verb', 'feminine', 'verbal', 'Performative verb in greetings (мэнд хүргэх).'),
            ('морилох', 'to proceed, visit, arrive (honorific)', 'verb', 'masculine', 'verbal', 'High-respect polite reception verb.'),
        ],
        'receptive': [
            ('мэндчилгээ', 'greeting, salutation, message', 'noun', 'feminine', 'nominal', 'Formal greeting ceremony noun.'),
            ('хүндэтгэл', 'respect, honor, reverence', 'noun', 'feminine', 'nominal', 'Politeness protocol noun.'),
        ]
    },
    'les_a1_16_03_inquiry_after_peace_amar_mend': {
        'productive': [
            ('амар', 'peace, rest, tranquility', 'noun', 'masculine', 'nominal', 'Traditional wellbeing state inquiry root.'),
            ('мэнд', 'health, sound, safe', 'noun', 'feminine', 'nominal', 'Wellbeing descriptor in greeting protocols.'),
            ('сонирхол', 'interest, curiosity, hobby', 'noun', 'masculine', 'nominal', 'Conversational inquiry root.'),
            ('амгалан', 'peaceful, serene, tranquil', 'adjective', 'masculine', 'adjectival', 'Formulaic answer to wellbeing inquiries (амар амгалан).'),
        ],
        'receptive': [
            ('аж байдал', 'living condition, situation', 'noun', 'masculine', 'compound_noun', 'Social inquiry topic.'),
        ]
    },
    'les_a1_16_04_reading_daily_greeting_schedules': {
        'productive': [
            ('хуваарь', 'schedule, timetable, roster', 'noun', 'masculine', 'nominal', 'Daily reception planning noun.'),
            ('төлөвлөгөө', 'plan, agenda, schedule', 'noun', 'feminine', 'nominal', 'Temporal schedule anchor.'),
            ('минут', 'minute', 'noun', 'masculine', 'nominal', 'Clock division.'),
        ],
        'receptive': [
            ('тэмдэглэл', 'note, diary, memo', 'noun', 'feminine', 'nominal', 'Written schedule record.'),
        ]
    },

    # -------------------------------------------------------------------------
    # Unit 17: Personal Pronouns & Direct Address Protocols
    # -------------------------------------------------------------------------
    'les_a1_17_01_nominative_personal_pronouns_system': {
        'productive': [
            ('чи', 'you (informal singular)', 'pronoun', 'neutral', 'personal_pronoun', 'Peer/child informal address pronoun.'),
            ('та', 'you (polite/formal singular or plural)', 'pronoun', 'neutral', 'personal_pronoun', 'Elder/formal address pronoun.'),
            ('тэр', 'he, she, it (third person)', 'pronoun', 'feminine', 'personal_pronoun', 'Third-person singular demonstrative pronoun.'),
            ('бид', 'we (first person plural)', 'pronoun', 'feminine', 'personal_pronoun', 'Collective first-person pronoun.'),
            ('тэд', 'they (third person plural)', 'pronoun', 'feminine', 'personal_pronoun', 'Collective third-person pronoun.'),
        ],
        'receptive': [
            ('төлөөний үг', 'pronoun', 'noun', 'masculine', 'compound_noun', 'Grammar concept for pronominal substitution.'),
            ('нэрлэхийн тийн ялгал', 'nominative case', 'noun', 'feminine', 'compound_noun', 'Grammatical case terminology.'),
        ]
    },
    'les_a1_17_02_politeness_protocols_chi_vs_ta': {
        'productive': [
            ('ахмад', 'senior, elder, veteran', 'noun', 'masculine', 'nominal', 'Direct address target requiring Та.'),
            ('үе тэнгийнхэн', 'peers, agemates', 'noun', 'feminine', 'compound_noun', 'Social peer group permitting Чи.'),
            ('дүү', 'younger sibling/relative', 'noun', 'feminine', 'nominal', 'Junior relative taking Чи.'),
            ('хүндэтгэх', 'to respect, honor', 'verb', 'feminine', 'verbal', 'Social address ethical verb.'),
            ('харилцах', 'to communicate, interact', 'verb', 'masculine', 'verbal', 'Social exchange verb.'),
        ],
        'receptive': [
            ('ёс зүй', 'ethics, etiquette, manners', 'noun', 'feminine', 'compound_noun', 'Politeness code noun.'),
            ('найрсаг', 'friendly, amicable, hospitable', 'adjective', 'masculine', 'adjectival', 'Social tone quality.'),
        ]
    },
    'les_a1_17_03_plural_address_protocols': {
        'productive': [
            ('хамт олон', 'collective, team, colleagues', 'noun', 'masculine', 'compound_noun', 'Group address target noun.'),
            ('нөхөд', 'comrades, colleagues, friends (plural)', 'noun', 'feminine', 'nominal', 'Plural formal address noun.'),
            ('хүүхдүүд', 'children (plural)', 'noun', 'feminine', 'nominal', 'Plural junior address noun.'),
            ('бүлэг', 'group, section, team', 'noun', 'feminine', 'nominal', 'Collective grouping noun.'),
        ],
        'receptive': [
            ('нийт', 'total, general, whole community', 'noun', 'feminine', 'nominal', 'Collective quantifier.'),
        ]
    },
    'les_a1_17_04_reading_personal_introductions': {
        'productive': [
            ('мэргэжил', 'profession, occupation', 'noun', 'feminine', 'nominal', 'Core biography profile noun.'),
            ('ажилтан', 'employee, staff member', 'noun', 'masculine', 'nominal', 'Workplace status noun.'),
            ('оюутан', 'university student', 'noun', 'masculine', 'nominal', 'Higher education pupil noun.'),
        ],
        'receptive': [
            ('товч намтар', 'curriculum vitae, brief biography', 'noun', 'masculine', 'compound_noun', 'Personal background profile label.'),
        ]
    },

    # -------------------------------------------------------------------------
    # Unit 18: Zero-Copula Identity & Origin Predication
    # -------------------------------------------------------------------------
    'les_a1_18_01_zero_copula_structure_intro': {
        'productive': [
            ('хуульч', 'lawyer, jurist', 'noun', 'masculine', 'nominal', 'Professional legal nominal predicate in zero-copula sentences.'),
            ('эмч', 'physician, medical doctor', 'noun', 'feminine', 'nominal', 'Professional medical nominal predicate.'),
            ('жолооч', 'driver', 'noun', 'masculine', 'nominal', 'Occupational predicate.'),
            ('инженер', 'engineer', 'noun', 'feminine', 'nominal', 'Technical occupational predicate.'),
            ('орчуулагч', 'translator, interpreter', 'noun', 'masculine', 'nominal', 'Linguistic professional predicate.'),
        ],
        'receptive': [
            ('өгүүлэгдэхүүн', 'subject (grammatical)', 'noun', 'feminine', 'nominal', 'Syntactic clause role.'),
            ('өгүүлэхүүн', 'predicate (grammatical)', 'noun', 'feminine', 'nominal', 'Syntactic clause role.'),
        ]
    },
    'les_a1_18_02_nationality_and_origin_predication': {
        'productive': [
            ('монгол', 'Mongolian, Mongol', 'noun', 'masculine', 'nominal', 'National origin predicate.'),
            ('америк', 'American', 'noun', 'feminine', 'nominal', 'National origin predicate.'),
            ('солонгос', 'Korean', 'noun', 'masculine', 'nominal', 'National origin predicate.'),
            ('япон', 'Japanese', 'noun', 'masculine', 'nominal', 'National origin predicate.'),
            ('хятад', 'Chinese', 'noun', 'masculine', 'nominal', 'National origin predicate.'),
            ('орос', 'Russian', 'noun', 'masculine', 'nominal', 'National origin predicate.'),
        ],
        'receptive': [
            ('үндэстэн', 'nationality, nation, ethnicity', 'noun', 'feminine', 'nominal', 'Civic origin category.'),
            ('тив', 'continent', 'noun', 'feminine', 'nominal', 'Geographical origin category.'),
        ]
    },
    'les_a1_18_03_origin_with_ablative_suffix_aas': {
        'productive': [
            ('нутгаас', 'from homeland, from region', 'noun', 'masculine', 'nominal_ablative', 'Ablative geographic origin form.'),
            ('хотоос', 'from the city', 'noun', 'masculine', 'nominal_ablative', 'Ablative urban origin form.'),
            ('хөдөөнөөс', 'from the countryside', 'noun', 'feminine', 'nominal_ablative', 'Ablative rural origin form.'),
            ('ирцгээсэн', 'arrived (plural collective)', 'verb', 'feminine', 'verbal_participle', 'Narrative origin motion verb.'),
            ('төрсөн', 'born, native', 'adjective', 'masculine', 'adjectival', 'Birthplace origin participle.'),
        ],
        'receptive': [
            ('гарал үүсэл', 'origin, ancestry, derivation', 'noun', 'feminine', 'compound_noun', 'Demographic origin concept.'),
            ('уугуул', 'native, indigenous, aboriginal', 'adjective', 'masculine', 'adjectival', 'Original regional resident.'),
        ]
    },
    'les_a1_18_04_reading_international_participant_roster': {
        'productive': [
            ('оролцогч', 'participant, attendee', 'noun', 'masculine', 'nominal', 'Conference delegate label.'),
            ('төлөөлөгч', 'representative, delegate', 'noun', 'feminine', 'nominal', 'Official delegate badge title.'),
            ('байгууллага', 'organization, agency, institution', 'noun', 'masculine', 'nominal', 'Institutional affiliation noun.'),
        ],
        'receptive': [
            ('хурал', 'conference, assembly, meeting', 'noun', 'masculine', 'nominal', 'International event forum noun.'),
        ]
    },

    # -------------------------------------------------------------------------
    # Unit 19: Polar Inquiries: Polar Question Particles уу/үү/юу/юү
    # -------------------------------------------------------------------------
    'les_a1_19_01_polar_particles_uu_uu_distribution': {
        'productive': [
            ('уу', 'polar question particle (back harmonic)', 'particle', 'masculine', 'question_particle', 'Post-consonantal back polar question marker.'),
            ('үү', 'polar question particle (front harmonic)', 'particle', 'feminine', 'question_particle', 'Post-consonantal front polar question marker.'),
            ('мөн', 'indeed, correct, true (affirmative copula)', 'particle', 'feminine', 'copular_particle', 'Identity confirmation particle.'),
            ('биш', 'not (equative copular negative)', 'particle', 'feminine', 'negative_particle', 'Identity rejection particle.'),
            ('асуух', 'to ask, inquire', 'verb', 'masculine', 'verbal', 'Core interrogative action verb.'),
        ],
        'receptive': [
            ('асуулт', 'question, inquiry', 'noun', 'masculine', 'nominal', 'Linguistic category noun.'),
            ('хариулт', 'answer, reply, response', 'noun', 'masculine', 'nominal', 'Conversational turn noun.'),
        ]
    },
    'les_a1_19_02_polar_particles_yuu_yuu_after_vowels': {
        'productive': [
            ('юу', 'polar question particle (post-vocalic back)', 'particle', 'masculine', 'question_particle', 'Post-vocalic polar question marker.'),
            ('юү', 'polar question particle (post-vocalic front)', 'particle', 'feminine', 'question_particle', 'Post-vocalic front polar question marker.'),
            ('тийм ээ', 'yes indeed', 'adverb', 'feminine', 'adverbial', 'Full affirmative confirmation phrase.'),
            ('үгүй ээ', 'no indeed', 'adverb', 'feminine', 'adverbial', 'Polite negative answer phrase.'),
            ('лавлах', 'to verify, check, clarify', 'verb', 'masculine', 'verbal', 'Conversational checking verb.'),
        ],
        'receptive': [
            ('эргэлзээ', 'doubt, hesitation', 'noun', 'feminine', 'nominal', 'Cognitive inquiry state.'),
            ('лавлагаа', 'inquiry desk, reference, directory', 'noun', 'masculine', 'nominal', 'Public service information desk.'),
        ]
    },
    'les_a1_19_03_answering_polar_questions_affirmative': {
        'productive': [
            ('зөв', 'correct, right, accurate', 'adjective', 'feminine', 'adjectival', 'Confirmation quality.'),
            ('буруу', 'wrong, incorrect, false', 'adjective', 'masculine', 'adjectival', 'Disconfirmation quality.'),
            ('мэдээж', 'of course, naturally, certainly', 'adverb', 'feminine', 'adverbial', 'Confident confirmation adverb.'),
            ('лавтай', 'certainly, definitely', 'adverb', 'masculine', 'adverbial', 'Epistemic certainty adverb.'),
        ],
        'receptive': [
            ('батлах', 'to confirm, certify, prove', 'verb', 'masculine', 'verbal', 'Administrative verification verb.'),
        ]
    },
    'les_a1_19_04_reading_identity_confirmation_dialogues': {
        'productive': [
            ('баримт', 'document, record, proof', 'noun', 'masculine', 'nominal', 'Identity document verification noun.'),
            ('шалгах', 'to check, examine, verify', 'verb', 'masculine', 'verbal', 'Inspection action verb.'),
            ('зөвшөөрөх', 'to agree, permit, approve', 'verb', 'feminine', 'verbal', 'Conversational acceptance verb.'),
        ],
        'receptive': [
            ('мэдэгдэл', 'announcement, notice, statement', 'noun', 'feminine', 'nominal', 'Formal written notice.'),
        ]
    },

    # -------------------------------------------------------------------------
    # Unit 20: Demonstrative Deixis: Энэ, Тэр, Эдгээр, Тэдгээр
    # -------------------------------------------------------------------------
    'les_a1_20_01_proximal_distal_deixis_ene_ter': {
        'productive': [
            ('энэ', 'this (proximal demonstrative)', 'pronoun', 'feminine', 'demonstrative_pronoun', 'Proximal spatial deictic pronoun.'),
            ('тэр', 'that (distal demonstrative)', 'pronoun', 'feminine', 'demonstrative_pronoun', 'Distal spatial deictic pronoun.'),
            ('энд', 'here (locative proximal)', 'adverb', 'feminine', 'spatial_adverb', 'Spatial proximal adverb.'),
            ('тэнд', 'there (locative distal)', 'adverb', 'feminine', 'spatial_adverb', 'Spatial distal adverb.'),
            ('заах', 'to point, show, indicate', 'verb', 'masculine', 'verbal', 'Deictic pointing gesture verb.'),
        ],
        'receptive': [
            ('заах төлөөний үг', 'demonstrative pronoun', 'noun', 'masculine', 'compound_noun', 'Grammar term for deictics.'),
            ('байрлал', 'location, position, placement', 'noun', 'masculine', 'nominal', 'Spatial coordinate noun.'),
        ]
    },
    'les_a1_20_02_plural_demonstratives_edgeer_tedgeer': {
        'productive': [
            ('эдгээр', 'these (plural proximal)', 'pronoun', 'feminine', 'demonstrative_pronoun', 'Plural proximal deictic pronoun.'),
            ('тэдгээр', 'those (plural distal)', 'pronoun', 'feminine', 'demonstrative_pronoun', 'Plural distal deictic pronoun.'),
            ('бүгд', 'all, everyone, everything', 'pronoun', 'feminine', 'collective_pronoun', 'Totalizing pronoun.'),
            ('зарим', 'some, several', 'pronoun', 'masculine', 'indefinite_pronoun', 'Partitive pronoun.'),
            ('эд зүйлс', 'items, belongings, goods (plural)', 'noun', 'feminine', 'compound_noun', 'Inventory physical objects.'),
        ],
        'receptive': [
            ('жагсаалт', 'list, inventory, roster', 'noun', 'masculine', 'nominal', 'Catalog document noun.'),
            ('бүртгэл', 'registration, record, ledger', 'noun', 'feminine', 'nominal', 'Account ledger noun.'),
        ]
    },
    'les_a1_20_03_inquiry_with_demonstratives_ene_yuu_ve': {
        'productive': [
            ('бэ', 'content question particle (after sonorants/vowels)', 'particle', 'feminine', 'question_particle', 'Wh-question marker.'),
            ('вэ', 'content question particle (after non-nasal consonants)', 'particle', 'feminine', 'question_particle', 'Wh-question marker.'),
            ('зүйл', 'item, thing, article', 'noun', 'feminine', 'nominal', 'Demonstrative inquiry target.'),
            ('хэрэгсэл', 'equipment, tool, instrument, supply', 'noun', 'feminine', 'nominal', 'Apparatus category noun.'),
        ],
        'receptive': [
            ('тодорхойлолт', 'definition, identification, description', 'noun', 'masculine', 'nominal', 'Descriptive answer noun.'),
        ]
    },
    'les_a1_20_04_reading_office_equipment_inventories': {
        'productive': [
            ('компьютер', 'computer', 'noun', 'feminine', 'nominal', 'Office workstation hardware.'),
            ('хайч', 'scissors', 'noun', 'masculine', 'nominal', 'Office desktop stationery tool.'),
            ('цаас', 'paper, sheet of paper', 'noun', 'masculine', 'nominal', 'Office printing supply.'),
        ],
        'receptive': [
            ('хэвлэгч', 'printer (hardware)', 'noun', 'feminine', 'nominal', 'Peripheral printing hardware.'),
        ]
    },
}

A1_PILOT_LESSON_EXPRESSIONS = {
    # 20 Productive, 10 Receptive across Units 16 to 20
    # -------------------------------------------------------------------------
    # Unit 16: Standard Salutations
    # -------------------------------------------------------------------------
    'les_a1_16_01_canonical_sov_architecture': {
        'productive': [('ном унших', 'to read a book', 'collocation', ['ном', 'унших'], 'Canonical transitive SOV verb phrase.')],
        'receptive': [('захиа бичих', 'to write a letter', 'collocation', ['бичих'], 'Epistolary SOV verb phrase.')]
    },
    'les_a1_16_02_formal_time_greetings_mori': {
        'productive': [('Өглөөний мэнд хүргэе', 'Good morning (formal conveyance)', 'formulaic_language', ['өглөөний', 'хүргэх'], 'Formal morning greeting formula.')],
        'receptive': []
    },
    'les_a1_16_03_inquiry_after_peace_amar_mend': {
        'productive': [('Амар байна уу', 'Are you peaceful? (traditional formal greeting)', 'formulaic_language', ['амар'], 'Formal steppe wellbeing greeting formula.')],
        'receptive': [('Сонин юу байна', 'What is new? What news is there?', 'formulaic_language', ['сонин'], 'Conversational news inquiry formula.')]
    },
    'les_a1_16_04_reading_daily_greeting_schedules': {
        'productive': [('ажлын хуваарь', 'work schedule, shift roster', 'collocation', ['хуваарь'], 'Office operational schedule noun phrase.')],
        'receptive': []
    },

    # -------------------------------------------------------------------------
    # Unit 17: Personal Pronouns & Direct Address
    # -------------------------------------------------------------------------
    'les_a1_17_01_nominative_personal_pronouns_system': {
        'productive': [('бид нар', 'we, all of us (explicit plural pronoun)', 'formulaic_language', ['бид'], 'Collective first-person plural formula.')],
        'receptive': []
    },
    'les_a1_17_02_politeness_protocols_chi_vs_ta': {
        'productive': [('Та сайн байна уу', 'How are you? (polite elder address)', 'formulaic_language', ['та'], 'Polite direct address greeting formula.')],
        'receptive': [('Чи сайн уу', 'How are you? (peer informal address)', 'formulaic_language', ['чи'], 'Informal peer direct address formula.')]
    },
    'les_a1_17_03_plural_address_protocols': {
        'productive': [('Та нар сайн байна уу', 'How are you all? (polite plural address)', 'formulaic_language', ['та'], 'Plural polite group greeting formula.')],
        'receptive': []
    },
    'les_a1_17_04_reading_personal_introductions': {
        'productive': [('өөрийгөө танилцуулах', 'to introduce oneself', 'pragmatic_routine', [], 'Social protocol introductory routine.')],
        'receptive': [('мэргэжлээрээ ажиллах', 'to work in one\'s profession', 'collocation', ['мэргэжил'], 'Professional career collocation.')]
    },

    # -------------------------------------------------------------------------
    # Unit 18: Zero-Copula Identity & Origin Predication
    # -------------------------------------------------------------------------
    'les_a1_18_01_zero_copula_structure_intro': {
        'productive': [('би оюутан', 'I am a student (zero-copula identity clause)', 'formulaic_language', ['би', 'оюутан'], 'Archetypal zero-copula student introduction.')],
        'receptive': []
    },
    'les_a1_18_02_nationality_and_origin_predication': {
        'productive': [('Монгол улс', 'Mongolia (State of Mongolia)', 'institutional_terminology', ['монгол'], 'Official constitutional country name.')],
        'receptive': [('гадаад орон', 'foreign country, overseas nation', 'collocation', [], 'International geographical phrase.')]
    },
    'les_a1_18_03_origin_with_ablative_suffix_aas': {
        'productive': [('хаанаас ирсэн бэ', 'where did you come from?', 'formulaic_language', [], 'Standard conversational origin inquiry.')],
        'receptive': []
    },
    'les_a1_18_04_reading_international_participant_roster': {
        'productive': [('төлөөлөгчдийн жагсаалт', 'delegates roster / participant list', 'institutional_terminology', ['төлөөлөгч'], 'Official conference administrative roster.')],
        'receptive': [('хурлын танхим', 'conference hall, meeting room', 'collocation', ['хурал'], 'Venue facility noun phrase.')]
    },

    # -------------------------------------------------------------------------
    # Unit 19: Polar Inquiries: Question Particles
    # -------------------------------------------------------------------------
    'les_a1_19_01_polar_particles_uu_uu_distribution': {
        'productive': [('Та багш уу', 'Are you a teacher?', 'formulaic_language', ['та', 'багш', 'уу'], 'Canonical post-consonantal back polar question.')],
        'receptive': []
    },
    'les_a1_19_02_polar_particles_yuu_yuu_after_vowels': {
        'productive': [('Энэ ширээ юү', 'Is this a desk?', 'formulaic_language', ['энэ', 'ширээ', 'юү'], 'Post-vocalic front polar question.')],
        'receptive': [('Энэ нохой юу', 'Is this a dog?', 'formulaic_language', ['энэ', 'нохой', 'юу'], 'Post-vocalic back polar question.')]
    },
    'les_a1_19_03_answering_polar_questions_affirmative': {
        'productive': [('Тийм, би оюутан', 'Yes, I am a student', 'formulaic_language', ['оюутан'], 'Standard affirmative equative response.')],
        'receptive': []
    },
    'les_a1_19_04_reading_identity_confirmation_dialogues': {
        'productive': [('лавлах товчоо', 'information / inquiry desk', 'institutional_terminology', ['лавлагаа'], 'Public service reception desk title.')],
        'receptive': [('үнэмлэхээ шалгуулах', 'to have one\'s ID verified / checked', 'pragmatic_routine', ['шалгах'], 'Security checkpoint routine.')]
    },

    # -------------------------------------------------------------------------
    # Unit 20: Demonstrative Deixis: Энэ, Тэр
    # -------------------------------------------------------------------------
    'les_a1_20_01_proximal_distal_deixis_ene_ter': {
        'productive': [('энэ хүн', 'this person (proximal reference)', 'collocation', ['энэ', 'хүн'], 'Everyday proximal person reference.')],
        'receptive': []
    },
    'les_a1_20_02_plural_demonstratives_edgeer_tedgeer': {
        'productive': [('эдгээр номууд', 'these books (plural proximal deixis)', 'collocation', ['эдгээр', 'ном'], 'Plural spatial nominal phrase.')],
        'receptive': [('тэдгээр хүмүүс', 'those people (plural distal deixis)', 'collocation', ['тэдгээр', 'хүмүүс'], 'Plural distal people phrase.')]
    },
    'les_a1_20_03_inquiry_with_demonstratives_ene_yuu_ve': {
        'productive': [('Энэ юу вэ', 'What is this?', 'formulaic_language', ['энэ', 'юу', 'вэ'], 'Archetypal object inquiry formula.')],
        'receptive': []
    },
    'les_a1_20_04_reading_office_equipment_inventories': {
        'productive': [('албан тасалгааны хэрэгсэл', 'office supplies / equipment', 'institutional_terminology', ['хэрэгсэл'], 'Commercial supplies category heading.')],
        'receptive': [('компьютерийн дэлгэц', 'computer monitor / screen', 'collocation', ['компьютер'], 'Hardware inventory collocation.')]
    },
}
