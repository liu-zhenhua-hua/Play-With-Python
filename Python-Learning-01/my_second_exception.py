#!/Users/tony/anaconda3/bin/python3


def process_alist(alist,index):
    try:
        alist[index]
    except IndexError as indexError:
        print(indexError)
    except ArithmeticError as arithmeticError:
        print(arithmeticError)
    except: #这是try语句块最后一个except子句,它可以不指定任何异常类型, 这样就可以处理任何异常类型
        print("our process_alist method got error ")
    else: #如果try没有捕获到异常, 就会来到else子句当中  ----> else是可选的
        print("We are in the Exception 'ELSE' Statement Block ")
    finally: #finally 子句的部分是无论如何都会被执行 ------> finally子句也是可选的, finally 这里通常可以进行, 资源清理操作, 例如关闭数据库, 文件
        print("The Exception Block has been executed and Exit noramlly ")



myList = [67,88,190]

process_alist(myList,1)