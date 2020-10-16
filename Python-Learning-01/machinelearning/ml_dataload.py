#!/Users/tony/anaconda3/bin/python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import datasets

iris = datasets.load_iris() #sklearn自己定义的一个数据集, 它所返回的类型类似python中的字典Bunch对象
print(iris.keys())