#!/Users/tony/anaconda3/bin/python3


# def spam():
#     print(eggs)
# eggs = 10
# spam()
# print(eggs)

"""
Local and Global Variables with Same Name
Technically, it's perfectly acceptable to use the same variable name for a global variable
remember avoid doing this. 
"""

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs) #print global