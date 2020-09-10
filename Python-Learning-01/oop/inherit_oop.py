#!/Users/tony/anaconda3/bin/python3

class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)

    def get_age(self):
        return self.age

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname


class Employee(Person):

    def __init__(self, firstname, lastname, age, firm, salary, title, department):
        super().__init__(firstname, lastname, age)
        self.firm = firm
        self.salary = salary
        self.title = title
        self.department = department

    def base_info(self):
        return 'Firm: {}, Job Title: {}, Department : {}'.format(self.firm, self.title, self.department)

    def get_salary(self):
        return self.salary

    def get_firm(self):
        return self.firm

    def get_department(self):
        return self.department

"""
define a object of Employee class
"""
emp_1 = Employee('Tony', 'Liu', 30, 'Google', 50000, 'Developer', 'ITO-EAS')

"""
isinstance(), issubclass() 这两个内置对象
"""
print(isinstance(emp_1,Employee))
print(issubclass(Employee,Person))

print("User Full Name : " + emp_1.fullname())
print(emp_1.email())
print(emp_1.base_info())
print(emp_1.get_firm())
print(emp_1.get_department())