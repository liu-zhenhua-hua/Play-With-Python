#!/Users/tony/anaconda3/bin/python3


def formatStr(target,original):
    if target == '' or target == 'python':
        return
    else:
        target = 'This is a magic {}'.format(original)
        return target


def processStr(originalStr):
    if originalStr.isupper():
        print('The Whole String is Upper format ')
    else:
        print('The String is not Upper format ')


def processStrAgain(originalStr):
    if originalStr.isupper():
        print('The Whole String is Upper Format ')
    elif originalStr.islower():
        print('The Whole String is Lower Format ')
    else:
        print('No idea about it ')


if __name__ == '__main__':
    print(formatStr(',','Characters'))

    processStr('ZEAL')

    processStrAgain('98877')