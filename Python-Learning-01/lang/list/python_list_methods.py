#!/Users/tony/anaconda3/bin/python3

"""
list methods
index()
"""

spam = ['hello','hi','Howdy','Heyas']

print(spam.index('hello')) #返回值的索引, 如果存在重复值, 返回第一个值的索引

# spam.index('Monday')#不存在, 程序报错



"""
向list中添加元素
append(), list尾部追加新元素
insert(), 在list指定位置添加新元素
"""
my_list=['cat','dog','bat','chicken']
my_list.append('Qt')

print(my_list)

"""
remove() 从list中删除元素
"""
my_list=['cat','dog','bat','chicken']
my_list.remove('bat') #del 语句得知道元素的索引值 del my_list[1]
# my_list.remove('xdog') 删除不存在的元素, 报错, 如果有重复值, 删除第一个元素

