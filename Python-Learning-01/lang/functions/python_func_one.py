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

"""
define a function return a value
"""
def getValue(firstValue,secondValue):
    result = firstValue + secondValue
    return result


"""
define a function with 'None'
"""
def evaluatedResult(firstV,secondV):
    if firstV == None and secondV == None:
        return None
    else:
        return firstV + secondV


"""
define a Python Function with one parameter.title()
"""

def mytitle(username):
    print("Hello, " + username.title())



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
    # hello('James')

    """
        main program will execute the function which is having 'return' clause
    """
    # result = getValue(8,12)
    # print(result)

    """
        function with None keyword
    """
    if evaluatedResult(None,None) == None:
        print('The Function return None')
    else:
        print('The Function return a Value ' + int(evaluatedResult(23,2)))

    print('=' * 40 + 'Passing another value to the Function ' + '=' * 40)
    if evaluatedResult(23,2) == None:
        print('The Function return None')
    else:
        result = evaluatedResult(23,2)
        print('The Result Value is ' + str(result))


    mytitle('Mark')