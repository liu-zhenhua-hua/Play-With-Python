#!/Users/tony/anaconda3/bin/python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import datasets

iris = datasets.load_iris() #sklearn自己定义的一个数据集, 它所返回的类型类似python中的字典 一个Bunch对象
print(iris.keys())

print(iris.DESCR)

print(iris.data) #查看测试数据, iris.data是numpy的一个对象

# print(type(iris.data)) #<class 'numpy.ndarray'>

print("The Shape of iris's Data {}".format(iris.data.shape))