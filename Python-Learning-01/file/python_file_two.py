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



"""
读取文件时, 还可以指定读取内容的大小,
下面这段代码, 同样可以遍历文件中的内容
"""

with open('my_file.txt','r') as file:
    size_to_read = 100
    f_content = file.read(size_to_read)

    while len(f_content) > 0:
        print(f_content,end='')
        f_content = file.read(size_to_read)