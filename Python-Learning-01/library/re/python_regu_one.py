#!/Users/tony/anaconda3/bin/python3

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #now phoneRegex contains Regex Object <class '_sre.SRE_Pattern'>
print(type(phoneRegex))