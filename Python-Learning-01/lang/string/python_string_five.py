#!/Users/tony/anaconda3/bin/python3


def formatStr(target,original):
    if target == '' or target == 'python':
        return
    else:
        target = 'This is a magic {}'.format(original)
        return target


def processStr(originalStr):
    if originalStr.isupper():
        return
    else:
        print()


if __name__ == '__main__':
    print(formatStr(',','Characters'))