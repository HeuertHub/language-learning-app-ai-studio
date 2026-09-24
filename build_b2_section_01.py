import json
import os
import math
from collections import Counter, defaultdict

# Ensure directory exists
os.makedirs('curriculum/lesson_blueprints', exist_ok=True)

# Load units
with open('curriculum/blueprint/units/b2.json') as f:
    b2_units_raw = json.load(f)
    b2_units = {u['unitId']: u for u in b2_units_raw}

# We define the 51 pedagogical lesson specifications for Units 156-166.
