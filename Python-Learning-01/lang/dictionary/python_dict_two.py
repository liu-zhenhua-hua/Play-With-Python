#!/Users/tony/anaconda3/bin/python3


eggs = {'name':'Zophie','species':'cat','age':'8'}

list_eggs = list(eggs)
print(list_eggs)

'''
keys(), values(), items()
'''

spam = {'color':'red','age':43,'name':'Tick'}

for v in spam.values():
    print(v)

#=============================================================


for k in spam.keys():
    print(k)


print('=' * 90)

for i in spam.items():
    print(i)