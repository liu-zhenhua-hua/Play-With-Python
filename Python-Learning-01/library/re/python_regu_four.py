#!/Users/tony/anaconda3/bin/python3


import re

"""
search() method will return a Match Object of the 'first' matched text in Searched String.
findall() return a Match Object but a list of Strings 
"""

"""
To summarize what the findall() method returns, remember the following:

When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, 
the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].


When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), 
the method findall() returns a list of tuples of strings (one string for each group), 
such as [('415', '555', '9999'), ('212', '555', '0000')].

"""

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no group
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has no group
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))