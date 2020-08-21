import re

regular_text='''
435.908.1457
340.897.8889
135-900-8745
190-211-1098
'''

pattern = re.compile(r'\d{3}\.\d{3}\.\d{4}')
pattern = re.compile(r'\d{3}\-\d{3}\-\d{4}')
pattern = re.compile(r'abc') #Try this Regular Expression

matches = pattern.finditer(regular_text)

for match in matches:
    print(match)

