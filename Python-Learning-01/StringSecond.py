'''
Python String Program
'''

import string
print(string.whitespace)


"""
Python 的String是不可变的对象(immutable)
"""

print("abc\n",end="") #使用end="" 这个参数, print()函数不再添加


new_string = " ".join(["Python","is","a","Popular","Language"])

print(new_string)

new_str_again = "::-".join(["A","B","C","D"])

print(new_str_again)


myString = "   Hello     World\t\t   "
print(myString.split())

print("===============================================")

second_string = "www.python.org"
result = second_string.strip(".org")
print(result)

ss_str = "Mississippi"
print(ss_str.find("ss"))

print(ss_str.find("ss",3))

print("===============================================")

method_string = "Mississippi"
if method_string.startswith("Miss"):
    print("The String start with Oiss ")
else:
    print("The String did not start with Oiss ")

print("===============================================")

search_substr = "Mississippi"

if search_substr.startswith("M",0):
    print("The String start with M ")
else:
    print("No idea about it")