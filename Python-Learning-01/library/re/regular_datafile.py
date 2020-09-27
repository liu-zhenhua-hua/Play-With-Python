#!/Users/tony/anaconda3/bin/python3

import re

"""
[] 
"""

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

with open('data.txt','r',encoding='utf-8') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for items in matches:
        print(items)