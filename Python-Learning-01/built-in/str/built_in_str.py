#!/Users/tony/anaconda3/bin/python

"""
built-in str
    class str(object=b'', encoding='utf-8', errors='strict')
    str -> return a string version of object

    如果既没有给出encoding 也没有给出errors 这两个参数 str(object) 将返回object.__str__(), 如果object中没有这个
    __str__()方法, 则调用repr(object)
"""

"""
str.capitalize(), 字符串首字母大写, 字符串余下部分是小写
Return a copy of the string with its first character capitalized and the rest lowercased. 
"""
print("employee".capitalize())
print("dOuble".capitalize()) #输出 Double


"""
str.center(width,[fillchar])
让字符串儿(在长度为width)居中显示, 可以使用fill char进行填充,默认是ASCII码的空格,
如果width的大小 小于或等于str, 方法返回字符串本身
"""
print(" Python is Short ".center(40,'*'))
