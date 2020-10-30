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