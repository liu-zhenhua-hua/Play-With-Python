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