#!/Users/tony/anaconda3/bin/python3

import re

"""
Python Regular Expression的Quantifier (可以用来表示重复出现的次数)

*     - 0 or More
+     - 1 or More
?     - 0 or More
{3}   - Exact Number
{3,4} - Range of Numbers(min, max)
"""

my_phone_numbers = """
233.900.1449
560-115-9534
890*145*8946
"""

"""
使用这种Regular Expression的Quantifier
"""

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') #
matches = pattern.finditer(my_phone_numbers)

for items in matches:
    print(items)

print("")
print("=" * 90)

my_name_list="""
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]')
matches = pattern.finditer(my_name_list)
for items in matches:
    print(items)