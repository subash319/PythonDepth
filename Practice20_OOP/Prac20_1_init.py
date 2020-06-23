# 1. In the BankAccount class that you had created in the previous exercise,
# delete the set_details() method and create an __init__ method.

class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'Hello {self.name} your balance amount is {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


p1 = BankAccount('subash', 10000)
p2 = BankAccount('harry', 100000)
p1.display()
p2.display()
p1.withdraw(100)
p2.deposit(100)
p1.display()
p2.display()
p1.deposit(100)
p2.withdraw(100)
p1.display()
p2.display()
