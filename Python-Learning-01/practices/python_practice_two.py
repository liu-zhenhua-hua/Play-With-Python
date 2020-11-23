#!/Users/tony/anaconda3/bin/python3

import re

"""
Python Regular Expression Python Program
"""

firstSearchText = """
Jack-k-k-k- Liu
"""

firstRegex = re.compile(r'(k-){4}') # (k-){4} will match k-k-k-k-, because, the group (k-) repeat 4 times, but k-k-k- will not.
firstMatched = firstRegex.search(firstSearchText)
print(firstMatched.group())