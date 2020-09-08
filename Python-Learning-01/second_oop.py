#!/Users/tony/anaconda3/bin/python3

class Employee:
    # def __int__(self): #Python的类只能包含一个__init__方法,
    #     self.firstName = ''
    #     self.firstName = ''
    #     self.salary = 0

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary





emp_1 = Employee('tony','liu',300)
emp_2 = Employee('mark','jiang',200)

print(emp_1)
print(emp_2)