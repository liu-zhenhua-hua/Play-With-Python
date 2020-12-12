#!/Users/tony/anaconda3/bin/python3

import re

mySearchText = "MKZL79868687LKM"
firstRegex = re.compile(r'[A-Z0-9]+$')
firstResult = firstRegex.search(mySearchText)
print(firstResult.group())


mySecondSearch = "MMKmmk"
secondRegex = re.compile(r'[mmk]+',re.I)
secondResult = secondRegex.search(mySecondSearch)
print(secondResult.group())