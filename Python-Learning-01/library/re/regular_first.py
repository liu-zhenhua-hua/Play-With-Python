#!/Users/tony/anaconda3/bin/python3

import re

my_search_text = """
This is a search text defined in Python
"""

pattern = re.compile(r'in')
result = pattern.search(my_search_text)

if result is None:
    print("We can't find out anything")
else:
    print("We find out the result")

print("=" * 40 + " next regular expression " + "=" * 40)