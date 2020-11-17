#!/Users/tony/anaconda3/bin/python3


def strJust(justlength):
    return 'Hello'.rjust(justlength,'=')

def stripMethod(stripMessage):
    spam = stripMessage
    return spam.strip()


def rightStripMethod(stripMessage):
    spam = stripMessage.rstrip()
    return spam

def leftStripMethod(stripMessage):
    spam = stripMessage.lstrip()
    return spam

if __name__ == '__main__':
    print(strJust(20))
    #print('  Hello World  ')
    #print(stripMethod('  Hello World  '))
    print(rightStripMethod('   Hello   '))
    print(leftStripMethod('   Hello   '))
