#!/Users/tony/anaconda3/bin/python3


spam = {'name':'Zophie','age':23}

if 'name' in spam.keys():
    print('True')

if 'Zophie' in spam.values():
    print('True')

if 'color' in spam.keys():
    print('False')


if 'color' not in spam.keys():
    print('True')


"""
下面的方式用来,判断一个值是否是dictionary中的key
"""
print('color' in spam)
print('Zophie' in spam)