#!/Users/tony/anaconda3/bin/python3

"""
function variable's scope
"""


"""
globals()
Return a dictionary representing the current global symbol table.
"""
global_a = 100
print(globals()['global_a'])

def spam():
    eggs = 80


def my_func_scope(first_value):
    """ first_value is local variable """
    first_value = first_value + 10
    return first_value

first_value = 10
print(my_func_scope(first_value))

print(first_value)