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
(443)-770-4321
"""

secondPhoneRegex = re.compile(r'\(\d\d\d\)-')
secondMatchedPhone = secondPhoneRegex.search(sec_search_text)
print(secondMatchedPhone.group())

print("=" * 90)

#===============================================================================================

"""
? Optional Matching.
* Zero or More.
+ One or More
"""

third_search_text = """
How I met your monther Session-1
Batwoman, Jack-Li
Jack-k-k-k-M
"""
thirdRegex = re.compile(r'Bat(wo)?man') # ? Example
thirdMatched = thirdRegex.search(third_search_text)

if thirdMatched is None:
    print('We did not find any thing')
else:
    print(thirdMatched.group())

