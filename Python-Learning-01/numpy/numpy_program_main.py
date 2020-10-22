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

    vectorFirst[0] = 9000

    print(vectorFirst)

    """
        numpy 创建零向量
    """

    print(np.zeros(5,dtype='int')) #np.zeros(5,dtype='int') np.zeros创建零向量, 默认是浮点数据类型, 5是维度
    print(np.ones(5,dtype='int')) #np.ones(5,dtype='int'), 创建5个1的向量
    print(np.full(5,666)) #np.full() 创建所有元素都一样的向量