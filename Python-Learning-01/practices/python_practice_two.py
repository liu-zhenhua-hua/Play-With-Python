#!/Users/tony/anaconda3/bin/python3

import re

"""
Python Regular Expression Python Program
"""

firstSearchText = """
Jack-k-k-k- Liu
"""

firstRegex = re.compile(r'(k-){4}')
firstMatched = firstRegex.search(firstSearchText)
print(firstMatched.group())