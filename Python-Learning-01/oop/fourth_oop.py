#!/Users/tony/anaconda3/bin/python3


class Employee:

    object_number = 0
    raise_amount = 1.04

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee.object_number += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def pay_raise(self):
        return self.salary * Employee.raise_amount


emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Zhang', 60000)

print(Employee.object_number)

