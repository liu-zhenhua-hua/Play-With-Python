#!/Users/tony/anaconda3/bin/python3

"""
Define a Python Function
"""


def ask_info(prompt, retries=4, reminder="Please Try it Again "):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response ----- please be careful ~!~!~!~')
        print(reminder)


"""
to call above function
"""
# ask_info('Do you really want to quit? ')
# ask_info('OK to overwrite the file?', 2)
# ask_info('OK to overwrite the file? ', 2, 'Come on, only yes or no!')


"""
default values are evaluated at the point of function definition in the defining scope
Python函数的默认值, 是在定义函数时确定下来的
"""
i = 5


def my_default_value(arg=i):
    print(arg)


i = 6
my_default_value()


def adding_elements(a, L=[]):
    L.append(a)
    return L


print(adding_elements(1))
print(adding_elements(2))
print(adding_elements(3))
print(adding_elements(4))

"""
we can define mutable default value like this
"""


def append_value(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print("==========================================================================================")
print(append_value(11))
print(append_value(12))
print(append_value(13))
print(append_value(14))


print("==========================================================================================")


