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
pattern = re.compile(r'\.') #just search the '.' please use \. escape the dot
#pattern = re.compile(r'\d') #Matching all digit in text_to_search
#pattern = re.compile(r'\w') #Word Character (a-z, A-Z,0-9,_)
#pattern = re.compile(r'\W') #Not a Word Character.
#pattern = re.compile(r'\bHa') #Word Boundary
#pattern = re.compile(r'\BHa') #Not a Word Boundary
#pattern = re.compile(r'^Start') #Begining of a String


matches = pattern.finditer(regular_text)

for match in matches:
    print(match)
