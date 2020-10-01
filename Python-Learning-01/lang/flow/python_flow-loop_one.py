#!/Users/tony/anaconda3/bin/python3

print("=" * 20 + "Loop Statement with Break " + "=" * 20)


name = ''

while True:
    print("Enter Your name : ")
    name = input()
    if name == 'Mark':
        break

print("Thank you")