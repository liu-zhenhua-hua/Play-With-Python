#!/Users/tony/anaconda3/bin/python3

import re
"""
metacharacter (special character)
转义字符 \ 将这些特殊的字符, 作为pattern的一部分
正则表达式中的特殊字符, 
1)  . 这个表示任意字符, 不包括新行  
2)  ^ 
"""
my_search_text = """
This is a search text defined in Python
"""

pattern = re.compile(r'in')
result = pattern.search(my_search_text)

if result is None:
    print("We can't find out anything")
else:
    print("We find out the result")
    print(my_search_text[26:28])

print("=" * 40 + " next regular expression " + "=" * 40)


my_second_text = """
abcdefg.45"""

pattern = re.compile(r'\.')
result = pattern.finditer(my_second_text)

for match in result:
    print(match)


print("=" * 40 + " next regular expression " + "=" * 40)


my_search_urls="""www.coreray.com
ocw.mit.edu,pc.tsinghua.edu"""

pattern = re.compile(r'\.edu')

matches = pattern.finditer(my_search_urls)

for items in matches:
    print(items)