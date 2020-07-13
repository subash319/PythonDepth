# 3. What will be the output of this code -


class Person:
    def greet(self):
        print('I am a Person')


class Teacher(Person):
    def greet(self):
        Person.greet(self)
        print('I am a Teacher')


class Student(Person):
    def greet(self):
        Person.greet(self)
        print('I am a Student')


class TeachingAssistant(Student, Teacher):
    def greet(self):
        super().greet()
        print('I am a Teaching Assistant')


x = TeachingAssistant()
x.greet()

# same explaination as previous one

# The output would be
# I'm a person
# I'm a Student
# I'm a Teaching Assistant