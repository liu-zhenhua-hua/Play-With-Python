#!/Users/tony/anaconda3/bin/python3

import re

"""
\b word boundary. 
\B not word boundary
"""


my_boundary_text = """Ha Ha HaHa"""

pattern = re.compile(r'\bHa')
matches = pattern.finditer(my_boundary_text)
for items in matches:
    print(items)