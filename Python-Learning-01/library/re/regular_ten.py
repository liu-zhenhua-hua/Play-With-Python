#!/Users/tony/anaconda3/bin/python3

import re

"""
匹配email address
"""

my_email_list="""
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)

print("=" * 90)
"""
下面我们再将其余的email地址取出
"""

pattern = re.compile(r'[a-zA-Z0-9-.]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)

print("=" * 90)

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)