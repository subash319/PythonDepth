# 4. Add a class variable named domains to the following Employee class.
# Make this class variable a set and it should store all domain names used by employees.


class Employee:

    # Adding a class variable named domains
    # This class variable is a set
    domain = set()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Employee.domain.add(email.split('@')[1])
        # print((email.split('@')))


def display(self):
    print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@gmail.com')
e6 = Employee('Mike', 'mike@yahoo.com')

print(Employee.domain)