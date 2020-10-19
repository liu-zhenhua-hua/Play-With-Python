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

print("Feature Names \n{}".format(iris.feature_names))

print("Target Names \n{}".format(iris.target_names))


X = iris.data[:,:2] #取所有行, 但是前两列

print(X.shape)

# plt.scatter #散点图
plt.scatter(X[:,0],X[:,1]) #取出矩阵的第0列, 和第1列
plt.show()

y = iris.target
plt.scatter(X[y==0,0],X[y==0,1], color="red", marker="o")
plt.scatter(X[y==1,0],X[y==1,1], color="blue", marker="+")
plt.scatter(X[y==2,0],X[y==2,1], color="green", marker="X")
plt.show()