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