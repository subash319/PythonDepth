# 3. In the following class SalesPerson, add two class variables named total_revenue and names. The variable names
# should be a list that contains names of all salespersons and total_revenue should contain the total sales amount
# of all the salespersons.


class SalesPerson:

    # Class Variables adding- 1.names:should be list of all names
    # 2. total_revenue: Total sales amount of all the salespersons

    names = []
    total_revenue = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0

    def make_sale(self, money):
        self.sales_amount += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = SalesPerson('Bob', 25)
s2 = SalesPerson('Ted', 22)
s3 = SalesPerson('Jack', 27)

s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)

s1.show()
s2.show()
s3.show()
# printing the class variables

print(SalesPerson.names)
print(SalesPerson.total_revenue)