#!/Users/tony/anaconda3/bin/python3

import re

"""
\w  word characters, 这里的word characters 指的是这些(a-z, A-Z,0-9,_) 
\W  大写的W, 通常是小写w的反义, 
"""

my_search_text = """[]AW"""

pattern = re.compile(r'\W')
matches = pattern.finditer(my_search_text)
for items in matches:
    print(items)


print("=" * 40 + " next regular expression " + "=" * 40)

my_search_text = """[]AW"""
pattern = re.compile(r'\w')
matches = pattern.finditer(my_search_text)
for items in matches:
    print(items)