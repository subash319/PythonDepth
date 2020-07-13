# 4. In the following inheritance hierarchy we have written code to add 'S' to id of Student, 'T' to id of
# Teacher and both 'T' and 'S' to id of Teaching Assistant.
# What will be the output of this code. If the code does not work as intended, what changes we need to make.

class Person:

    def __init__(self, id):
        self.id = id


class Person:
    def __init__(self, id):
        self.id = id


class Teacher(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'T'


class Student(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'S'


class TeachingAssistant(Student, Teacher):
    def __init__(self, id):
        super().__init__(id)


x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)