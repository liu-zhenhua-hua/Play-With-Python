#!/Users/tony/anaconda3/bin/python3

import re

"""
\b Word Boundary
\B Not a Word Boundary
"""

my_text_search = "Ha HaHa"

pattern = re.compile(r'\bHa')
matches = pattern.finditer(my_text_search)

for match in matches:
    print(match)