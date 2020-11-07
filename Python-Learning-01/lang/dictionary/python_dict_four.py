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