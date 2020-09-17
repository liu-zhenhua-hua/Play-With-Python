#!/Users/tony/anaconda3/bin/python3

import re

"""
\s Whitespace(space, tab, newline)
\S 同理与小写的s相对
"""

my_regular_text="""b\n
df
fdf
dfdf
dfdf
"""


pattern = re.compile(r'\s')
matches = pattern.finditer(my_regular_text)
for items in matches:
    print(items)


print("=" * 40 + " next regular expression " + "=" * 40)

my_regular_text="""b\n
df
fdf
dfdf
dfdf
"""

pattern = re.compile(r'\S')
matches = pattern.finditer(my_regular_text)
for items in matches:
    print(items)