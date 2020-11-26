#!/Users/tony/anaconda3/bin/python3


import re

firstSearchText = """RoboCop eats baby food. BABY FOOD."""
firstRegex = re.compile(r'[aeiouAEIOU]')
firstResult = firstRegex.findall(firstSearchText)
print(firstResult)