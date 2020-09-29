#!/Users/tony/anaconda3/bin/python3

"""
Python Reading File
"""


"""
一次读取十个字符, end=结尾添加"*"
"""
with open('my_file.txt','r') as file:
    size_to_read = 10
    f_contents = file.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents,end='*')
        f_contents = file.read(size_to_read)



print("")

with open('my_file.txt','r') as file:
    size_to_read = 10
    f_contents = file.read(size_to_read)
    print(f_contents,end='')

    # file.seek(0)

    f_contents = file.read(size_to_read)
    print(f_contents, end='')

    file.tell()