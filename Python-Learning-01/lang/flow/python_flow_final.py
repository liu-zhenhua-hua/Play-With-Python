#!/Users/tony/anaconda3/bin/python3

import sys

while True:
    print("Type exit to terminate program !")
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')