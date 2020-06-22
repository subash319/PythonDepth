# Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.
#
# In the set_details method, create two instance variables : name and balance.
# The default value for balance should be zero. In the display method,
# display the values of these two instance variables.
#
# Both the methods withdraw and deposit have amount as parameter. Inside withdraw,
# subtract the amount from balance and inside deposit, add the amount to the balance.
#
# Create two instances of this class and call the methods on those instances.

class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'Hello {self.name} your balance amount is {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


p1 = BankAccount()
p2 = BankAccount()
p1.set_details('subash', 10000)
p2.set_details('harry', 100000)
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
