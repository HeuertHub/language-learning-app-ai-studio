import json

# We will generate data_sec02.py
with open("scripts/data_sec02.py", "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Data authoring for B2 Section 02 (Units 167-176): Ecology, Climate, Dzud & Resource Economics."""\n\n')
    f.write("SEC02_LESSONS = []\n\n")

print("make_sec02.py skeleton ready")
