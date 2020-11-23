#!/Users/tony/anaconda3/bin/python3

import re

"""
character classes
"""

firstSearchText = """Thisisisis"""
firstRegex = re.compile(r'(is){3,3}')
firstMatched = firstRegex.search(firstSearchText)
print(firstMatched.group())


secondSearchText = """We are going to move ZXA report into zxq"""
secondRegex = re.compile(r'[ZXA]')
secondMatched = secondRegex.findall(secondSearchText)
print(secondMatched)