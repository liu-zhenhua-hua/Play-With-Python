#!/User/tony/anaconda3/bin/python3

import random
import copy

alist = []  # declare a new list
alist.append('a')
alist.append('b')
alist.append('c')
alist.append('d')


print(alist)

pointerA = alist
pointerB = alist


alist.append('zz')

print(alist)

print("The id of pointerA " + str(id(pointerA)))
print("The id of pointerB " + str(id(pointerB)))

print(pointerA)
print(pointerB)

#===========================================================================

secondList = ['cat','bat','rat','elephant']

print(secondList)
secondList.clear()
print(secondList)


#===========================================================================
print("=" * 90)

thirdList = ['cat','bat','rat','elephant','python','Dell','Oracle','Linux']

for item in range(len(thirdList)):
    print(thirdList[item])

#==========================================================================
print("=" * 90)




fourList = ['cat','bat','rat','elephant','python']

for index,item in enumerate(fourList):
    print('Index ' + str(index) + ' animal is ' + item)

#==========================================================================
# print("=" * 90)


print('=============================== The List index, List slice ===============================')


fiveList = ['Python','Oracle','IBM','Google','Facebook','LinkedIn']

print('Index[0]  ' + fiveList[0])
print('Index[1]  ' + fiveList[1])
print('Index[:3] ' + str(fiveList[:3]))
print('Index[-4:-1] ' + str(fiveList[-4:-1]))


#==========================================================================

sixList = ['Python','Oracle','IBM','Google','Facebook','LinkedIn']

print('Random List''s Element : ' + random.choice(sixList))


print('before random.shuffle() ' + str(sixList))
random.shuffle(sixList) #random.shuffle() method
print('The random.shuffle() ' + str(sixList))


#==========================================================================


sevenList = ['cat','bat','rat','elephant']

print('The index of ''cat'' ' + str(sevenList.index('cat')))


#==========================================================================
#clear the elements of Python List

eightList = ['Python','Oracle','Linux','Ubuntu','Microsoft','Keyboard']

print('Before clear all the elements : ' + str(eightList))

eightList.clear()

print('After clear all the elements : ' + str(eightList))


del eightList[:] #del one empty Python List


#==========================================================================

aNumber = 56
bNumber = 78

print('aNumber is : ' + str(aNumber))
aNumber, bNumber = bNumber,aNumber

print('aNumber is : ' + str(aNumber))


#==========================================================================


aTupleFromList = tuple(['ab','no','rm','al'])

print('aTupleFromList is : ' + str(aTupleFromList))

print(type(aTupleFromList))
