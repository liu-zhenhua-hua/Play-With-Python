#!/Users/tony/anaconda3/bin/python3

class Employee:
    def __init__(self,first,last,salary): #pay a attention __init__
        self.first = first
        self.last = last
        self.salary = salary

    def fullname(self):
        return '{},{}'.format(self.first,self.last)


# empA = Employee('Tony','Liu',500)

empA = Employee('Tony','Liu',900)
print(empA.fullname())
print(Employee.fullname(empA))