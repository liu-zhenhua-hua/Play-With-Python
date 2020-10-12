#!/Users/tony/anaconda3/bin/python3


"""
Changing the Value
"""

spam=['cat','bat','rat','elephant']

"""
通过索引修改list的值
"""
spam[1] = 'Tiger'
print(spam)

#====================================================
print('*' * 90)


spam=['cat','bat','rat','elephant']
spam[1] = 'Tiger'
spam[2] = spam[1]
print(spam)

