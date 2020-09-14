#!/Users/tony/anaconda3/bin/python3

"""
define a Python Function
"""


def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any ', kind, '?')
    print("-- I'm sorry, we're all out of ", kind)
    for arg in arguments:
        print(arg)
    for kw in keywords:
        print(kw,":",keywords[kw])


cheeseshop("Limburger","It's very runny sir","It's really very very runny sir",
           shopkeeper = "Michael Palin",
           client="John Cheese",sketch="Cheese Shop Sketch")