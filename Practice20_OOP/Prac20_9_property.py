# 9. Suppose after some time, you want to give an additional 2% discount on a product, if its price is above 500.
# To incorporate this change, implement discount as a property in your Product class.

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return self.marked_price-(self.discount*0.01*self.marked_price)

    @property
    def discount(self):
           return self._discount+2 if self.marked_price > 500 else self._discount

    @discount.setter
    def discount(self,new_disc):
        self._discount = new_disc



p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)
print(f'p3:{p3.discount},p4:{p4.discount}')
p4.discount =10
print(f'p3:{p3.discount},p4:{p4.discount}')