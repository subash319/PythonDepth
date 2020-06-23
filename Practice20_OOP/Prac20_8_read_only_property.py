# 8. For the following class Product, create a read only property named selling_price that is calculated
# by deducting discount from the marked_price. The instance variable discount represents discount in percent.

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return self.marked_price-(self.discount*0.01*self.marked_price)


p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)
print(p1.selling_price)
print(p2.selling_price)
print(p3.selling_price)
print(p4.selling_price)