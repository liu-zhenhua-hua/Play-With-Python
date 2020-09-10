#!/Users/tony/anaconda3/bin/python3

class Employee:
    object_number = 0
    raise_amount = 1.04

    """
        Python类中, 只能定义一个
    """
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee.object_number += 1

    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)


    def pay_raise(self):
        return self.salary * self.raise_amount


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)


emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Han', 60000)
emp_3 = Employee('Jane', 'Doe', 70000)

emp_2.raise_amount = 1.08

print(emp_1.pay_raise())
print(emp_2.pay_raise())
print(emp_3.pay_raise())