#!/Users/tony/anaconda3/bin/python3

"""
Python Excetpion Process
"""

def process_alist(arg_alist,index):
    try:
        arg_alist[index]
    except IndexError:
        print("--- List index out of range")