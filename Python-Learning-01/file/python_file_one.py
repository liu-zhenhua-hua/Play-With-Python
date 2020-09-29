#!/Users/tony/anaconda3/bin/python3

"""
Python File Object
"""

f = open('my_file.txt','r') #built-in function open()

print(f.name)
print(f.mode)

f.close() #close the file release the source.
print("="*90)
"""
using Python context manager
使用Python context manager
with context manager 可以打开文件
使用完文件,同时也关闭了文件, 都是由context manager来进行管理
"""

with open('my_file.txt','r') as file:
    f_contents = file.read()
    print(f_contents)

print("="*90)
"""
看看下面这段代码
"""
with open('my_file.txt','r') as file:
    pass

print(file.closed)
print(f.read())