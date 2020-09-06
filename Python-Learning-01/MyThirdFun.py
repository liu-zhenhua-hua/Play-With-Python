'''
Pyhon Function
'''

"""
mutable object for function argument
"""

def my_fun(n,list1,list2):
    list1.append(3)
    list2 = [4,5,6]
    n += 1

x = 5
y = [1,2]
z = [4,5]

my_fun(x,y,z)

print(x)
print(y)
print(z)

print("=========================================")