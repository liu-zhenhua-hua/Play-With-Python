'''
Python Function Program
'''

"""
We define a factorial function
"""
def fact(n):
    """Return the factorial of the given number"""
    if (n < 0 or n==0):
        return None
    else:
        r = 1
        while n > 0:
            r = r * n
            n = n-1
        return r



user_input = input("Please Input a Number : ")
number = int(user_input)
result = 0

if ((fact(number)) == None):
    print("User Input a invalid number ")
else:
    result = fact(number)

print("The Result is : " + str(result))

"""
define a function 
"""
def printMessage(msg):
    """Print Out the Message which pass the argument"""
    print(msg)


printMessage("Deep Learning")

"""
define a function to calculate two number
"""
def calculate(x,y):
    if (x, y < 0):
        return None
    else:
        return x + y
