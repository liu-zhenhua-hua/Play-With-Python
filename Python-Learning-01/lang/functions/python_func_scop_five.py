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

