#!/Users/tony/anaconda3/bin/python3

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age. ')
