# 5. In the Book class, create a property named price
# such that the price of a book cannot be less than 50 or more than 1000.

class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f'{self.isbn:20s}{self.title:20s}{self.author:10s}{self.publisher:5s}'
              f'{self.pages:5d}{self.price:5d}{self.copies:5d}')

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        self.copies -= 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError("The price should be between 50 and 1000 only")


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 50, 6)

book1.price = 100
book1.display()
