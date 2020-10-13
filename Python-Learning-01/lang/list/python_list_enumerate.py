#!/Users/tony/anaconda3/bin/python3

"""
range(len(list)) 除了使用这个方法遍历, 还可以使用enumerate()函数来实现
enumerate() 返回两个值, list-index, list-value 索引和索引对应的值
在需要同时获取index和其对应的值的时候, enumerate()函数
"""


supplies = ['pens','staplers','flamethrowers','binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + 'in supplies is : ' + item)


