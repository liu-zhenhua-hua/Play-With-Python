#!/Users/tony/anaconda3/bin/python3

import numpy as np

zeros_array = np.zeros(10,dtype=int)
print(zeros_array)
print(zeros_array.dtype)


print("=" * 90)

print(np.zeros((3,5)))


zeros_array = np.zeros(shape=(3,5),dtype=int) #np.zeros 全0矩阵
print(zeros_array)
print(type(zeros_array))

print("=" * 90)

ones_array = np.ones(shape=(3,5),dtype=int) #np.ones 全1矩阵
print(ones_array)


print("=" * 90)

full_array = np.full(shape=(3,5),fill_value=777)
print(full_array)

full_array_again = np.full((3,5),666)
print(full_array_again)