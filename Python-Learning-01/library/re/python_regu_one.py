#!/Users/tony/anaconda3/bin/python3

import re
"""
Regular Expression Matching
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function (Remember to use a raw string)
3. Pass the String you want to search into the Regex Object's search() Method. This returns a Match Object
4. Call the Match Object's group() method to return a string of the actual matched text.
"""

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #now phoneRegex contains Regex Object <class '_sre.SRE_Pattern'>

myResult = phoneRegex.search('My Number is 415-555-4243')

print('Phone Number is : ' + myResult.group())

print('=' * 90)

