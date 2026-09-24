# -*- coding: utf-8 -*-
"""Complete Authoring of C1 Section 01: Constitutional Law, Governance & Statutory Drafting.
Units 198 to 207 (10 units, 47 lessons).
"""
import json
import os

units_authoritative = json.load(open("curriculum/blueprint/units/c1.json", encoding="utf-8"))
u_map = {u["unitId"]: u for u in units_authoritative}

