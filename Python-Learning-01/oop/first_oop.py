#!/Users/tony/anaconda3/bin/python3

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

