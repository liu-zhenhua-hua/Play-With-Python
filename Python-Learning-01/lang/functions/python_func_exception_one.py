#!/Users/tony/anaconda3/bin/python3


"""
Python Exception
"""

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')



print(spam(12))
print(spam(0))