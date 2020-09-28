#!/Users/tony/anaconda3/bin/python3

import re

"""
[1-5]表示范围的例子, 以及
[^] "^"在[]里就表示不包含
"""

my_context = """
1234567890
"""

pattern = re.compile(r'[1-5]')

matches = pattern.finditer(my_context)

for items in matches:
    print(items)

print("")
print("="*90)

my_second_context = """
cat
mat
pat
bat
"""

"""
除了bat, 其它的字符都被提取
"""

pattern = re.compile(r'[^b]at') #除了bat,其它符合条件的字符都被提取
matches = pattern.finditer(my_second_context)

for items in matches:
    print(items)
