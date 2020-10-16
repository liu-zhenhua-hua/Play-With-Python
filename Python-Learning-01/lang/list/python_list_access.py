#!/Users/tony/anaconda3/bin/python3


suppliers = ['Zeal','Zulu','Pens','Staples','flame','binders']

for i in range(len(suppliers)):
    print('Index ' + str(i) + 'in supplies is : ' + suppliers[i])



#==================================================
print('*' * 80)

myPets=['Zophie','Pooka','Fat-tail']
print('Enter a pet Name : ')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

#==================================================
#=== List Reference ===


