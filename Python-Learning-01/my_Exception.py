#!/Users/tony/anaconda3/bin/python3

"""
Python Excetpion Process
"""

def process_alist(arg_alist,index):
    try:
        arg_alist[index]
    except IndexError:
        print("Your List Index out of Range  ^_^")
        # raise IndexError("Your List Index out of Range  ^_^") #这是个很有意思的异常处理, 试试这个语句, 看看运行结果


alist = [5,9,10]

process_alist(alist,6)