#!/Users/tony/anaconda3/bin/python3

import re

"""
using parentheses will create groups in the regex object.
then use group() match object method to grab the matching text
from just one group
"""
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#nameListRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

phoneResult = phoneNumberRegex.search('My Phone Number is 415-555-4343')


"""
The first set of parentheses in a regex string will be group 1. The second set will be group 2. 
By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. 
Passing 0 or nothing to the group() method will return the entire matched text.

if you would like to retrieve all the groups at once, use the groups() method note the plural
"""
print(phoneResult.group(1))
print(phoneResult.group(2))
print(phoneResult.group(0))


mainNumber,secondNumber = phoneResult.groups() # multiple assignment tricks
print(mainNumber)


#===============================================================================================