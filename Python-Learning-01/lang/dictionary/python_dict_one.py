#!/Users/tony/anaconda3/bin/python3



myCat={'size: ':'fat',' color: ':'gray',' disposition: ': 'loud'}

print(myCat)

#access value through the key

print('The Size of Cat : ' + myCat['size: '])

'''
Dictionaries can still use integer values as keys
'''

spam={12:'Luggage Combination', 43: 'The Answer'}

print('The Dictionary is : ' + spam[12])


'''
Unlike Lists, items in dictionaries are unordered. 
There is no 'first' item in a dictionary. 
'''

aListA = ['cat','dog','rat']
bListB = ['cat','rat','dog']

if (aListA == bListB):
    print('The Two List equals each other ')
else:
    print('The Two List are not equal ')


print('=' * 90)

#==========================================================================

cListC = ['cat','dog','rat']
dListD = ['cat','dog','rat']

if(cListC == dListD):
    print('cListC equals dListD ')
else:
    print('cListC did not equal dListD ')

#==========================================================================

'''
compare the the Dictionary
'''
aDict = {1:'Python',2:'CentOS',3:'Oracle'}
bDict = {1:'Python',3:'Oracle',2:'CentOS'}
'''
Two Dictionary are not ordered.
They can't be sliced like lists
'''
if(aDict == bDict):
    print('The Two Dictionary is same ')
else:
    print('The Two Dictionary is not same ')