#!/Users/tony/anaconda3/bin/python3

"""
Python List
"""

spam=['cat','bat','rat','elephant']
print(spam[0]) #index 只能是整数, 不能是浮点数

print(spam[int(2.1)]) #int() 转化成整数

alist = ['cat','bat','rat','element']

# print(type(alist))


"""
包含list的list
"""
spam = [['cat','bat'],[10,20,30,40,50]]
print(spam[0])

print("*" * 100)

"""
index可以是负数
"""
spam=[12,10,42,33,88,16,73,77]
print(spam[-1])
print(spam[-2])


print("*" * 100)