#!/Users/tony/anaconda3/bin/python3

import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#nameListRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

phoneResult = phoneNumberRegex.search('My Phone Number is 415-555-4343')

print(phoneResult.group(1))