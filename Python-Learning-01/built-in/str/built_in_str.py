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
让字符串儿(在长度为width)居中显示, 可以使用fill char(unicode也是可以的 '\u4E06')进行填充,默认是ASCII码的空格,
如果width的大小 小于或等于str, 方法返回字符串本身
"""
print(" Python is Short ".center(40,'*'))


"""
str.count(sub[, start[, end]]), 查找sub 在str中出现的次数, start, end 可以指定在一定的范围搜索
Return the number of non-overlapping occurrences of substring sub in the range [start, end]. 
Optional arguments start and end are interpreted as in slice notation.
"""
print("Python programming platform".count('n',0,6))

print("Python Programming Learning Plan".count('n'))




print("encoding-string".encode(encoding='utf-8'))

"""
str.endswith(suffix[, start[, end]]), str时候以suffix结尾, 这个suffix也可以是来自 a tuple of suffixes
看下面的例子, 同样的也可以通过 start, end 这两个参数指定搜索范围
"""
print("string".endswith('ng'))
print("string max".endswith(('ng','ag','maxg')))


"""
str.expandtabs(tabsize=8), 这个方法就是将tab 字符用更多的空格填充, 默认值是8
default is 8, giving tab positions at columns 0, 8, 16 and so on
"""
print("01\t02\t".expandtabs(18))

print("=============================================================================================")

"""
str.find(sub[,start[,end]]),
返回lowest 索引值, start, end设置查找范围, 如果没找到返回 -1
"""
print("Google V8 Engine".find("Python")) #return -1


print("Google".find('G',1,3)) # return -1, 在指定的区间没有找到'G'


