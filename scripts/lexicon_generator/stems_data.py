#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authentic Mongolian Word Roots and Expression Patterns
"""

# Rich inventory of authentic Mongolian lemmas across all POS categories:
# Verbs, Nouns, Adjectives, Adverbs, Pronouns, Numerals, Particles, Postpositions, Conjunctions

NOUN_STEMS = [
    # Kinship & Social
    ("өвөө", "grandfather", "kinship", "neutral"),
    ("эмээ", "grandmother", "kinship", "neutral"),
    ("наймаач", "merchant, trader", "social", "neutral"),
    ("малчин", "herder, pastoralist", "pastoral", "neutral"),
    ("жолооч", "driver", "transport", "neutral"),
    ("эмч", "doctor, physician", "medical", "neutral"),
    ("сувилагч", "nurse", "medical", "neutral"),
    ("инженер", "engineer", "technical", "neutral"),
    ("цагдаа", "police officer", "social", "neutral"),
    ("тогооч", "cook, chef", "culinary", "neutral"),
    ("үйлчлэгч", "server, attendant", "service", "neutral"),
    ("худалдагч", "shop assistant, seller", "commerce", "neutral"),
    ("захирал", "director, principal, CEO", "professional", "neutral"),
    ("ажилтан", "employee, worker", "professional", "neutral"),
    ("мэргэжилтэн", "specialist, expert", "professional", "neutral"),
    ("хөрш", "neighbor", "social", "neutral"),
    ("анд", "sworn friend, close friend", "social", "literary"),
    ("нөхөр", "friend, comrade, husband", "social", "neutral"),
    ("найз", "friend (informal)", "social", "informal"),
    ("хамт олон", "team, collective, colleagues", "social", "neutral"),
    ("иргэн", "citizen", "civics", "neutral"),
    ("хүн ам", "population", "civics", "neutral"),
    ("ард түмэн", "people, folk, nation", "civics", "neutral"),
    ("ястан", "ethnic group, sub-nationality", "culture", "neutral"),
    ("үндэстэн", "nationality, ethnic nation", "civics", "neutral"),
    
    # Body & Health
    ("толгой", "head", "body", "neutral"),
    ("нүд", "eye", "body", "neutral"),
    ("чих", "ear", "body", "neutral"),
    ("хамар", "nose", "body", "neutral"),
    ("ам", "mouth", "body", "neutral"),
    ("шүд", "tooth", "body", "neutral"),
    ("хэл", "tongue, language", "body", "neutral"),
    ("хоолой", "throat, voice", "body", "neutral"),
    ("хүзүү", "neck", "body", "neutral"),
    ("мөр", "shoulder", "body", "neutral"),
    ("гар", "hand, arm", "body", "neutral"),
    ("хөл", "foot, leg", "body", "neutral"),
    ("хуруу", "finger, toe", "body", "neutral"),
    ("нуруу", "back, spine", "body", "neutral"),
    ("цээж", "chest", "body", "neutral"),
    ("гэдэс", "belly, stomach", "body", "neutral"),
    ("зүрх", "heart", "body", "neutral"),
    ("элэг", "liver", "body", "neutral"),
    ("уушги", "lung", "body", "neutral"),
    ("бөөр", "kidney", "body", "neutral"),
    ("цус", "blood", "body", "neutral"),
    ("яс", "bone", "body", "neutral"),
    ("арьс", "skin, hide", "body", "neutral"),
    ("өвчин", "disease, illness, pain", "medical", "neutral"),
    ("эм", "medicine, medication, woman", "medical", "neutral"),
    ("эмийн сан", "pharmacy", "medical", "neutral"),
    ("эмнэлэг", "hospital, clinic", "medical", "neutral"),
    ("халуун", "fever, heat, hot", "medical", "neutral"),
    ("ханиад", "flu, common cold, cough", "medical", "neutral"),
    ("шарх", "wound, cut", "medical", "neutral"),
]

def get_noun_stems():
    return NOUN_STEMS
