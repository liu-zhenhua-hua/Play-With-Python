#!/Users/tony/anaconda3/bin/python3

g_number = 10 #global variable


def function_scope(firstv, secondv):
    print(g_number,firstv, secondv)
    globals()['g_number'] = 50
    print(g_number)




def spam():
    eggs = 90
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0



if __name__ == '__main__':
    function_scope(15, 20)
    print()
    spam()