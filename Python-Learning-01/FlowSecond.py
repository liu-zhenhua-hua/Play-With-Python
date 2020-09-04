'''
Python Flow Application
'''

alist = [(3,4),(6,8),(10,1)]
result = 0
for x,y in alist:
    result = result + (x * y)

print(result)


'''
enumerate
'''

blist = [1,3,-7,4,9,-5,4]
result = enumerate(blist)

print(result)

clist = [2,4,6,8]
dlist = [1,3,5,7]

print("================================================================")
eresult = zip(clist,dlist)
new_collection = tuple(eresult)
print(new_collection)
cresult = 0
for a,b in new_collection:
    cresult = cresult + (a + b)

print(cresult)

print("================================================================")

value = [1,2,3,4]
value_squared = []
for item in value:
    value_squared.append(item * item)

print(value_squared)