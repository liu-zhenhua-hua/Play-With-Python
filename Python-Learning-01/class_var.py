#!/Users/tony/anaconda3/bin/python3
class Student:
    def __init__(self, first, last, score, email):
        self.first = first
        self.last = last
        self.score = score
        self.email = email

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


student_1 = Student('Tony', 'Liu', 90, 'liu@gmail.com')
student_2 = Student('Mark', 'Li', 89, 'mark@gmail.com')
