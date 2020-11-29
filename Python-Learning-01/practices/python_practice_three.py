#!/Users/tony/anaconda3/bin/python3


import re

"""
This program is very important - review it carefully and frequently
"""

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
sixSearchTextWithinStr = "235678zxv8907"
sixSearchTextWithSpace = "344540 998668"
sixRegex = re.compile(r'^\d+$')
# sixResult = sixRegex.findall(sixSearchText)
# sixResult = sixRegex.findall(sixSearchTextWithinStr)
sixResult = sixRegex.findall(sixSearchTextWithSpace)
if len(sixResult) == 0:
    print('We got Nothing from Regex (r\'^\\d+\$\')')
else:
    print(sixResult)


#=========================================================================================

"""
The . (or dot) character in a regular expression is called a wildcard will match any 
Character except for a newline
Remember that the dot character will match just one character.
"""

theDotSearchText = "The cat in the hat"
theDotSearchRegex = re.compile(r'.at')
theDotResult = theDotSearchRegex.findall(theDotSearchText)

for elements in theDotResult:
    print(elements)

"""
.*   ---> Programmer can use the dot-star to match everything
Following is Example
.* uses greedy mode: that means It will always try to match as much text as possible
"""
dotStarText = "First Name:AI Last Name:Sweigart"
dotStarRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
dotStarResult = dotStarRegex.search(dotStarText)

print(dotStarResult.group(1))
print(dotStarResult.group(2))


greedyText = "<To serve man> for dinner.>"
greedyRegex = re.compile(r'<.*>')
greedyResult = greedyRegex.search(greedyText)
print(greedyResult.group())


nongreedyText = "<To serve man> for dinner.>"
nongreedyRegex = re.compile(r'<.*?>')
nongreedyResult = nongreedyRegex.search(nongreedyText)
print(nongreedyResult.group())


"""
Matching newlines with the Dot Character
re.DOTALL as second argument to re.compile(), will match all characters, 
including the newline character.
"""

newLineText = "Serve the public trust. \n Protect the innocent." \
        "Upload the law"
newLineRegex = re.compile('.*',re.DOTALL) #re.DOTALL second argument for matching newline.
newLineResult = newLineRegex.search(newLineText)

print(newLineResult.group())