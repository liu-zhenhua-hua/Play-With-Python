#!/Users/tony/anaconda3/bin/python3

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age. ')

#=================================================================

print('=' * 90)

"""
startswith()
endswith()
"""

if 'Hello,world'.startswith('Hello'):
    print('The Condition is True ')
else:
    print('The Condition is False ')

#=================================================================

"""
join()
split() 
"""

