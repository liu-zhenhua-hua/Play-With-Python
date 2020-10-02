#!/Users/tony/anaconda3/bin/python3

"""
define a Python Function
"""

def hello():
    print('Howdy!')
    print('Howdy!')
    print('Hello World')

"""
define a function with parameters:
"""
def hello(name):
    print('Hello, ' + name)


if __name__ == '__main__':
    """
        main program will execute the function with two times
    """
    # hello()
    # print("")
    # hello()
    """
        main program will execute the function which is having one parameter
    """
    hello('James')