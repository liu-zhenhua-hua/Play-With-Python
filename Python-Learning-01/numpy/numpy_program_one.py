#!/Users/tony/anaconda3/bin/python3

import numpy as np

zeros_array = np.zeros(10,dtype=int)
print(zeros_array)
print(zeros_array.dtype)


print("=" * 90)

print(np.zeros((3,5)))


zeros_array = np.zeros(shape=(3,5),dtype=int)
print(zeros_array)
print(type(zeros_array))