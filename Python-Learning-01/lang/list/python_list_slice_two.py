#!/Users/tony/anaconda3/bin/python3

alist = [23,89,90,88,100,55,21,93,45]

alist_slice = alist[0:3]

print(id(alist))
print(id(alist_slice))

print(alist_slice)
alist_slice[0] = 990

print(alist)
print(alist_slice)