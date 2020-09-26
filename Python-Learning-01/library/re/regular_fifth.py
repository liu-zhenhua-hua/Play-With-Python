#!/Users/tony/anaconda3/bin/python3

import re

"""
\b Word Boundary
\B Not a Word Boundary
^  -Beginning of a String
$  -End of a String
"""

my_text_search = "Ha HaHa"

pattern = re.compile(r'\bHa')
matches = pattern.finditer(my_text_search)

for match in matches:
    print(match)


print("=" * 40 + "\B Not a Word Boundary " + "="*40 )

not_boundary_pattern = re.compile(r'\BHa')
not_boundary_matches = not_boundary_pattern.finditer(my_text_search)

for matches in not_boundary_matches:
    print(matches)


print("=" * 40 + " ^,$ Regular Expression Language " + "="*40 )

my_sentence = 'Start a new Sentence and then bring it to an end'

my_sentence_pattern = re.compile(r'^Start')
my_sentence_matches = my_sentence_pattern.finditer(my_sentence)

for items in my_sentence_matches:
    print(items)