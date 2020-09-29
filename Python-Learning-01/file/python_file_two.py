#!/Users/tony/anaconda3/bin/python3

"""
using Python context manager
"""
"""
使用下面的代码输出文件的全部内容
"""
with open('my_file.txt','r') as file:
    for line in file:
        print(line,end='')