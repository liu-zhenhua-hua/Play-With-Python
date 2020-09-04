'''
Python Tuple Program
'''

# pack and unpack
one,two,three,four = 1,2,3,4

print(one)


a = 16
b = 20

a,b = b,a

print(a)
print(b)

x = (1,2,3,4)

c,d,*e = x #这里*号的意思是, 将剩余的元素接收为列表, 没有剩余, 则带星号的元素会收到空列表

print(e)

alist = list(('a','b','c','d'))
print(alist)



