#!/Users/tony/anaconda3/bin/python3
class Employee:
    raise_amount = 1.04

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def pay_raise(self):
        return self.salary * self.raise_amount


emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Zhang', 60000)

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)