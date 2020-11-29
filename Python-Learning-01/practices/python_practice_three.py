#!/Users/tony/anaconda3/bin/python3


import re

firstSearchText = """RoboCop eats baby food. BABY FOOD."""
firstRegex = re.compile(r'[aeiouAEIOU]')
firstResult = firstRegex.findall(firstSearchText)
print(firstResult)

"""
Regular Expression
"""

secondSearchText = "aeioDRmp"
secondRegex = re.compile(r'[^aeiouAEIOU]')
secondResult = secondRegex.findall(secondSearchText)
print(secondResult)


"""
Caret (^) Character and Dollar 
^ at the start of a regex to indicate that a match must occur 
at the beginning of the searched text.

$ at the end of the regex to indicate the string must end with this regular expression
"""

thirdSearchText = "Hello, Python Regular Expression"
thirdRegex = re.compile(r'^Hello')
thirdResult = thirdRegex.findall(thirdSearchText)

if thirdResult == None:
    print('We got Nothing')
else:
    print(thirdResult)

fourSearchText = "My Ticket Number is 47"
fourRegex = re.compile(r'\d$')
fourResult = fourRegex.findall(fourSearchText)
print(fourResult)


fiveSearchText = "My Ticket Number is Fourty Four"
fiveRegex = re.compile(r'\d$')
fiveResult = fiveRegex.findall(fiveSearchText)

if len(fiveResult) == 0:
    print("We got the Nothing")

"""
The r'^\d+$' regular expression string matches strings 
that both begin and end with one or more numeric characters. 
"""

sixSearchText = "235358900"
sixRegex = re.compile(r'^\d+$')
sixResult = sixRegex.findall(sixSearchText)

if len(sixResult) == 0:
    print('We got Nothing')
else:
    print(sixResult)









