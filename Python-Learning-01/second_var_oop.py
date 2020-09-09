#!/Users/tony/anaconda3/bin/python3

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


emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Jiang', 60000)
emp_3 = Employee('James', 'Li', 80000)

Employee.set_raise_amt(1.07)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)
