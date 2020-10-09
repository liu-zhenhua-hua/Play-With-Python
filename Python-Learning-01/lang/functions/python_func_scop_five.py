#!/Users/tony/anaconda3/bin/python3

"""
The global statement

global eggs -> it tells Python, "In this function, eggs refers to the global variable,
so don't create a local variable with this name
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)


"""
There are four rules to tell whether a variable is in a local scope or global scope.

1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
2. If there is a global statement for that variable in a function, it is a global variable.
3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
4. But if the variable is not used in an assignment statement, it is a global variable.

"""


