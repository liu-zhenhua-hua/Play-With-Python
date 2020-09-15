#!/Users/tony/anaconda3/bin/python3

import re

"""
\d Matches any Unicode decimal digit  它的效果等同于 [0-9]
\D Matches any character which is not a decimal digit. [^0-9]
"""

my_search_text = """
9879-NBC
1250-SPR
"""

pattern = re.compile(r'\D')
matches = pattern.finditer(my_search_text)

for items in matches:
    print(items)


