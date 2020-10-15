#!/Users/tony/anaconda3/bin/python3

import numpy as np

"""
Python's range() function
"""
alist = [i for i in range(0,20,2)]
print(alist)

"""
numpy 中存在arange() 与python中的range()类似, 类似是因为step 步长可以是浮点数
linspace(start,end) 这里返回的结果是包含start和end的值
"""
print(np.arange(10))
print(np.arange(0,10,2))
print(np.arange(0,5,0.4))

print("=" * 90)

print(np.linspace(0,20,11,dtype=int)) #步长是2, 0 ~ 20 需要11个数
print(np.linspace(0,20,6,dtype=int))
print(np.linspace(0,21,8,dtype=int))