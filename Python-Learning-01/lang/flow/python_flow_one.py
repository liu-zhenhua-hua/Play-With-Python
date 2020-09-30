#!/Users/tony/anaconda3/bin/python

"""
Python Flow Control Program
"""

spam = True
junk_mail = True

if spam == True and junk_mail==True:
    print("The First Condition is True")
else:
    print("The Condition is False")



"""
Mixing Boolean and Comparison Operators
"""

print("=" * 20 + "Mixing Boolean and Comparison Operators" + "=" * 20)

firstNumber = 4
secondNumber = 5
ThirdNumber = 6

if firstNumber < secondNumber < ThirdNumber: #原来还可以这样写
    print("The Condition is True")
else:
    print("The Condition is False")


"""
comparison operator again
"""

if firstNumber< secondNumber and secondNumber<ThirdNumber: #这是个传统写法
    print("The Comparison Expression is True ")