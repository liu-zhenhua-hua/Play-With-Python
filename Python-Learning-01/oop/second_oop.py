#!/Users/tony/anaconda3/bin/python3

class Employee:

    object_number = 0


    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        # self.email = firstname + '.'+ lastname + '@gmail.com'
        Employee.object_number += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, name):
        firstname,lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname
    """
    可以使用@property 装饰器, 使用这个装饰器定义一个方法, 我们访问这个方法,就像是访问类的属性一样
    访问这个方法的时候 instance.email 即可而不能是 email(), 这样会报错
    """
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)


emp_1 = Employee('Tony', 'Liu', 50000)
# emp_2 = Employee('Mark', 'Zhang', 60000)
# emp_3 = Employee('Jane', 'Doe', 70000)


# print(Employee.object_number)


emp_1.firstname = 'John'

# emp_1.fullname = 'Tony Liu' # fullname 也被@property装饰器修饰, 但是不能通过这个方式为属性赋值, 如果想要赋值,要采用另外一种方式

emp_1.fullname = 'Tim Zhang'

print(emp_1.firstname)
# print(emp_1.email()) #这样调用被@property 装饰器修饰的方法会报错
print(emp_1.email)
print(emp_1.fullname)

