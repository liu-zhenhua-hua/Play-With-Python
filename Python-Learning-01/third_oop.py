#!/Users/tony/anaconda3/bin/python3

"""
define a class
"""

class Employee:
    def __int__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def fullname(self):
        return '{},{}'.format(self.firstName,self.lastName)


empA = Employee()