#!/Users/tony/anaconda3/bin/python3

def process_alist(alist,index):
    try:
        alist[index]
    except IndexError as indexError:
        print(indexError)
    except ArithmeticError as arithmeticError:
        print(arithmeticError)
    except:
        print("our process_alist method got error ")
    else: #如果try没有捕获到异常, 就会来到else子句当中
        print("We are in the Exception 'ELSE' Statement Block ")
    finally: #finally 子句的部分是无论如何都会被执行
        print("The Exception Block has been executed and Exit noramlly ")



myList = [67,88,190]

process_alist(myList,1)