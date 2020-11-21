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

print(phoneResult.group(1))
print(phoneResult.group(2))