#!/Users/tony/anaconda3/bin/python3

"""
Python Function definition
"""

def concat_string(*args, sep):
    return sep.join(args)


print(concat_string(*('Google','Mail','Search'),sep="/"))