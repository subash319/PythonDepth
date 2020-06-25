# 7. Class variables with immutable values can be used as defaults for instance variables.
# In the following BankAccount class, add an instance variable named bank in the __init__method.
# Add a class variable bank_name that will be used as default argument in the __init__  method for bank parameter.


class BankAccount:
    bank_name = 'SBI'

    def __init__(self, name, balance=0, bank = bank_name):
        self.name = name
        self.balance = balance
        self.bankname = bank

    def display(self):
        print(self.name, self.balance,self.bankname)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


a1 = BankAccount('Mike', 200,'HDFC')
a2 = BankAccount('Tom')

a1.display()
a2.display()
