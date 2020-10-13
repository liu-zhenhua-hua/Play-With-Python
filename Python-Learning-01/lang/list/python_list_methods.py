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

"""
sort() list的元素排序
Python关于list的sort()方法需要注意的三点:
1. sort(), 是直接对调用它的list进行排序, sort()没有返回值, spam=spam.sort() 这样写是错误的
2. sort(), 不能对既包含number又包含strings的list进行排序, Python不知道如何对它们进行比对
3. sort(), 使用"ASCIIbetical order"对strings进行排序, 这就意味着大写字面排在小写字面之前,
   如果想按照字母序排序, sort(key=str.lower)这样调用
"""


"""
reverse() list.reverse()
"""