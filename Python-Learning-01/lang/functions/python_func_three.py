#!/Users/tony/anaconda3/bin/python3

"""
*toppings 这里形参是一个空的元组, 调用这个函数时传入的任意数量的实参, 都会被收入到这个元组中
只传递一个实参, 也是一个元组
"""
def produce_pizza(*toppings):
    """ produce the pizza """
    print(toppings)



"""
调用可接收任意参数的函数 procduce_pizza
"""

produce_pizza('First-peper','Second-mushroom','Third-cheese')

print("=" * 90)

produce_pizza('Peper-Again')
