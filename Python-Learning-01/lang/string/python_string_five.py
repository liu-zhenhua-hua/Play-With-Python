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
    elif originalStr.isalnum(): #isalnum() Return True if the String consists only of letters and numbers and is not blank
        print('The String only contain letters and numbers ')
    else:
        print('No idea about it ')


def checkStralnum(originalStr):
    if originalStr.isalnum():
        print('The String only contain letters and numbers ')
    else:
        return


if __name__ == '__main__':
    print(formatStr(',','Characters'))

    #processStr('ZEAL')
    #processStrAgain('98877')
    #processStrAgain('98798yiy8')

    checkStralnum(' ')