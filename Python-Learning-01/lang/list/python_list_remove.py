#!/Users/tony/anaconda3/bin/python3

"""
removing the values from lists with del statement.

del statement will delete values at an index in a list.

del 语句也可以删除普通的变量, 不过del最常用的还是删除list中的元素
"""

"""
del statement
"""
spam = ['cat','bat','rat','elephant']
print(spam)
del spam[1]
print(spam)
