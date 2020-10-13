#!/Users/tony/anaconda3/bin/python3

"""
The + operator combines two lists to create a new list value
and the * operator can be used with a list and an integer value
to replicate the list
"""

"""
使用 '+' 合并两个list
"""
alist = [1,3,5]
blist = [2,4,6]

print(alist + blist)

#========================================

print(['x','y','z'] * 4)

#========================================
spam = [12,56,90]
spam = spam + ['B','D','Z']
print(spam)

#========================================

myCatNames=[]

for i in range(10):
    myCatNames = myCatNames + [i]

print('The value of my List ')
for value in myCatNames:
    print(' ' + str(value))