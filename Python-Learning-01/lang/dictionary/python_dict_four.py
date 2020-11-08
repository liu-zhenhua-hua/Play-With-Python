#!/Users/tony/anaconda3/bin/python3


"""
dictionary get() method
"""

picnicItems = {'apples':5,'cups':4}

print('I am bringing ' + str(picnicItems.get('orange','None')) + ' oranges.')


spamDict = {'name':'Pooka','age':30}

if 'color' not in spamDict:
    spamDict['color'] = 'Black'

print(spamDict)

#============================================================================================

print("=" * 90)

"""
The setdefault() method is a nice shortcut to ensure that a key exists.

"""

messge = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in messge:
    count.setdefault(character,0)
    count[character] = count[character] + 1
print(count)