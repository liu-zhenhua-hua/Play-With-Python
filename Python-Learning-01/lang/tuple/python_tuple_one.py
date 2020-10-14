#!/Users/tony/anaconda3/bin/python3

"""
Python Tuple Data Type
"""

spam = ('Hello',) # Tuple spam contain only one value
spam_list = ['a','b','c',] # ,list 或者 tuple 在最后一个元素之后加上',' 是合法的语法
print(type(spam))
print(type(spam_list))


"""
list(), tuple()这两个函数返回list 或者tuple
"""

tuple_spam = tuple(['cat','dog'])
print(tuple_spam)

list_spam = list(('cat','dog','apple'))
print(list_spam)