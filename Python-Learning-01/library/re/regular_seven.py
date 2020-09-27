#!/Users/tony/anaconda3/bin/python3

import re
"""
使用[],[89]匹配都是单一字符
[1-5],这个所要表达的是1-5这个范围 
"""

my_context = """
800-115-9534
900-115-9534
900.115.9534
"""

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(my_context)

for items in matches:
    print(items)

print("")
print("="*90)