#!/User/tony/anaconda3/bin/python3


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

print('Index[0] ' + fiveList[0])
print('Index[1] ' + fiveList[1])