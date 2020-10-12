#!/Users/tony/anaconda3/bin/python3

"""
Python List中的slice
spam[2]    : a List with index(one integer)
spam[1:4]  : a list with a slice(two integer)
spam[startIndex:endIndex(not include)], 不包含endIndex索引所对应的元素
"""


spam=['cat','bat','rat','elephant'] #定义一个list

print(spam[1:4]) #['bat','rat','elephant']

print(spam[0:4]) #print out the all elements of List


print("*" * 100)

spam=['cat','bat','rat','elephant']

print(spam[:2])

print(spam[-4:-1])


print('*' * 40 + 'len() function to calculate the length of list' + '*' * 40)

my_length_list = ['cat','bat','rat','elephant']

print(len(my_length_list))