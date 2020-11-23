#!/Users/tony/anaconda3/bin/python3


import re

"""
define a text variable
"""
search_text = """
My Phone Numbers:
345-789-3289 897-900-5568 808-111-9090
"""

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #regex object return to phoneRegex

phoneFetched = phoneRegex.finditer(search_text) #regexObject.finditer()

"""
iterate each items 
"""
for items in phoneFetched:
    print(items.group())


# phoneNumberFetched = phoneRegex.search(search_text)
# print(phoneNumberFetched.group())

print("=" * 90)

#===============================================================================================

sec_search_text = """
Phone Numbers List
345-789-3289
897-900-5568
808-111-9090
"""