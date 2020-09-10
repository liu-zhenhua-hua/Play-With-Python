#!/Users/tony/anaconda3/bin/python3

class Employee:
    raise_amount_value = 1.04
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    """
    @classmethod 修饰的方法, 是绑定在类上的, 不是与与具体的类的实例相关
    那么该函数, 只能访问类的属性(类变量), 不能获取实例的数据属性
    """
    @classmethod
    def raise_rate(cls,amount_rate):
        cls.raise_amount_value = cls.raise_amount_value + amount_rate

    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)

    def raise_amount(self):
        return self.salary * Employee.raise_amount_value

    """
    @staticmethod 静态方法只是名义上归属于类管理, 不能使用类变量和实例变量, 我们可以把它
    看成类的工具包, 注意下面就是一个定义好的静态变量, 我们既没有传入"self",也没有传入"cls"
    """
    @staticmethod
    def calculate_days():
        print("@staticmethod -> ")

emp_1 = Employee('Tony', 'Liu', 50000)

emp_1.raise_rate(2)
print(emp_1.raise_amount_value)

print(emp_1.raise_amount())


