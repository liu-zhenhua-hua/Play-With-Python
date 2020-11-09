#!/Users/tony/anaconda3/bin/python3


"""
Python's String Escape Characters
"""
spam = 'Say hi to Bob\'s monther' #Escape Characters

print(spam)

secondSpam = 'Let\'s learning Python\tProgramming Language'

print(secondSpam)

"""
place r before the beginning quotation mark of a String
to make it a raw String
"""

print(r'That is Carol\'s cat.') # 'That is Carol\'s cat.' will display

"""
Multiline Strings with Triple Quotes
三个单引号或者双引号, 可以引用多行文本
这也是作为多行注释来用
"""

thirdSpam='''
Multiline Strings with Triple Quotes
Python is Programming Language.
C++ is most useful Technical Skills
'''

print(thirdSpam)