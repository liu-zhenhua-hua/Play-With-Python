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

"""
Python’s regular expressions are greedy by default,
"""
secondSearchText="""HzHzHzHzHz"""
secondRegex = re.compile(r'(Hz){3,5}') #greedy match, return 5 times of 'Hz'
secondMatched = secondRegex.search(secondSearchText)
print(secondMatched.group())


thirdSearchText = """HzHzHzHzHzHzHzHzHz""" #non-greedy model, also called lazy mode
thirdRegex = re.compile(r'(Hz){3,5}?') #non-gready model, also called Lazy mode
thirdMatched = thirdRegex.search(thirdSearchText)
print(thirdMatched.group())


fourthSearchText = """This is Batwoman, Batman"""
fourthRegex = re.compile(r'Bat(wo)?man')
fourthMatched = fourthRegex.search(fourthSearchText)
print(fourthMatched.group())