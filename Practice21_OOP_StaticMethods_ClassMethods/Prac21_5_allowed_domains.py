# 5. In the following Employee class, add a class variable named allowed_domains.
#
# allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
# Whenever an email is assigned, if the domain named is not in allowed_domains, raise a RuntimeError.

class Employee:

    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, add):
        domain = add.split('@')[1]
        if domain in Employee.allowed_domains:
            self._email = add
        else:
            raise RuntimeError('The domain is not allowed, Access is restricted')

    def display(self):
        print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@xmail.com')