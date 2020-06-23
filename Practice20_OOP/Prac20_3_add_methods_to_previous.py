# 3. For the Book class that you have created, write a method named in_stock that
# returns True if number of copies is more than zero, otherwise it returns False.
#
# Create another method named sell that decreases the number of copies by 1
# if the book is in stock, otherwise it prints the message that the book is out of stock.

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


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)
print('-' * 100)
book1.display()
book2.display()
book3.display()
book4.display()
for i in range(5):
    book3.sell()
book3.display()
print(book3.in_stock())
print('-' * 100)