#!/Users/tony/anaconda3/bin/python3

"""
Python Continue or Break
"""

while True:
    print('Who are you ?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe, What is the password? (It is a fish.)')
    password = input()
    print('Type your Password ')
    if password == 'swordfish':
        break;
print("Access granted")

