#!/Users/tony/anaconda3/bin/python3


import numpy as np


if __name__ == '__main__':
    print(np.__version__)

    lst = [1,2,3]
    lst[0] = "Linear-Algebra"
    print(lst)

    """
        creating numpy vector object
    """

    vectorFirst = np.array([1,2,3]) #将Python的list作为参数传入array中
    print(vectorFirst)

    # vectorFirst[0]="Linear" #会报错, numpy中的ndarray对象,只能存储同一种数据类型

    # print(type(vectorFirst))