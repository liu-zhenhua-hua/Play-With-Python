#!/Users/tony/anaconda3/bin/python3

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def email_addr(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)

    def salar_info(self):
        return self.salary



emp_1 = Employee('Tony', 'Liu', 50000)
emp_2 = Employee('Mark', 'Jiang', 60000)

print(emp_1)
print(emp_2)