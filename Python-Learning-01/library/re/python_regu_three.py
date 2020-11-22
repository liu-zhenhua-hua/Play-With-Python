#!/Users/tony/anaconda3/bin/python3

import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batRegexResult = batRegex.search('Batmobile lost a wheel')

print(batRegexResult.group())
print(batRegexResult.group(1))

#===============================================================================================

"""
? -> precedes it as optional part of pattern
* -> match zero or more
+ -> at least once
"""

patternRegexOne = re.compile(r'Bat(wo)?man')
patternOneResult = patternRegexOne.search('This is our Batman')
print(patternOneResult.group())
patternOneResult = patternRegexOne.search('This is our Batwoman')
print(patternOneResult.group())