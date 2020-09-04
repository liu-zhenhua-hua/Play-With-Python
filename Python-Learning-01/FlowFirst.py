'''
Python Flow Control Program
'''

anumber = 10

while anumber < 20:
    anumber = anumber + 2
else:
    print("The Execution was done ")


print(anumber)

print("====================== bnumber ======================= ")

bnumber = 10

while bnumber < 100:
    bnumber = bnumber + 10
    if (bnumber == 50):
        break;

print(bnumber)

print("====================== cnumber [if-elif-else statement] ======================= ")

cnumber = 5

if cnumber > 50:
    print(cnumber)
elif cnumber > 60:
    print(cnumber)
elif cnumber > 70:
    print(cnumber)
elif cnumber > 80:
    print(cnumber)
else:
    print(cnumber)

print("======================== dnumber [for search ] ================================")

'''
Using for statement to list the element of List
'''
alist = [89,23,19,22,54,88,100]
for x in alist:
    print(x)

"""
rang函数
"""

blist = ['A','B','C','D','E','F']

dnumber = range(len(blist))

print(dnumber)

clist = [3,4,5,6,8,10,22,56,100,155]

print(list(range(3,7)))

print("================================================================================")

somelist = [(1,2),(3,7)]
result = 0
for i in somelist:
    result = result + (i[0] * i[1])

print(result)

print("================================================================================")


