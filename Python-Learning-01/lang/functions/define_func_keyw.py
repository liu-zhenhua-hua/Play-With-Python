#!/Users/tony/anaconda3/bin/python3

"""
define Python Function,
"""


"""
In a function call, keyword arguments must follow positional arguments.----> 这一点非常重要
传递keyword类型的参数, 必须与函数的定义相匹配, 但是彼此之间的顺序并不重要, 

result = calculate_value(**{'first': 10, 'second': 30})  **keywords --> 将dict作为参数传递到函数中   keywords argument
print(calculate_posi(*(45, 5)))                          *args      --> 将tuple作为参数传递到函数中, positional argument

{特别要注意: (*name must occur before **name.) }

"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(1000) # 1 positional argument
# parrot(voltage=1000) # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments
# parrot(action='VOOOOOM',voltage=1000000)

# parrot('a million', 'bereft of life', 'jump') # 3 positional arguments

# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


"""
define a function
"""


def calculate_value(first=3, second=5):
    return first + second


result = calculate_value(first=13, second=12)
print(result)

print("==========================================================================================")
result = calculate_value(**{'first': 10, 'second': 30})  # using ** to pass key value parameter
print(result)

print("==========================================================================================")


def calculate_posi(first, second):
    return first + second


print(calculate_posi(4, 5))
print(calculate_posi(*(45, 5)))  # using *() method to pass positional argument
