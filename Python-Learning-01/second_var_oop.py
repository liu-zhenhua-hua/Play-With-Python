#!/Users/tony/anaconda3/bin/python3
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtSql
import PyQt5.QtMultimedia
import PyQt5.QtMultimediaWidgets

class Employee:
    object_num = 0
    raise_amount = 1.04

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee.object_num += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def pay_raise(self):
        return self.salary * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    """
    也可以使用classmethod定义一个类的构造函数, 传统Python构造器的另一个选择
    """
    @classmethod
    def from_string_object(cls, object_str):
        firstname, lastname, salary = object_str.split('-')
        return cls(firstname, lastname, salary)

print("=======================================================================================")

emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Jiang', 60000)
emp_3 = Employee('James', 'Li', 80000)

# Employee.set_raise_amt(1.07)
#
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_3.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Job-80000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string_object(emp_str_1)
new_emp_2 = Employee.from_string_object(emp_str_2)
