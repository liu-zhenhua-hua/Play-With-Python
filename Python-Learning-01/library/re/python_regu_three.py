#!/Users/tony/anaconda3/bin/python3

import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batRegexResult = batRegex.search('Batmobile lost a wheel')

print(batRegexResult.group())