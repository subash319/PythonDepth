# 4. Create a list named books that contains the 4 Book instance objects that you have
# created in question 2. Iterate over this list using a for loop and call display() for each object in the list.
#
# Write a list comprehension to create another list that contains title of books written by Jack.


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

# Iterate over this list using a for loop and call display() for each object in the list.

list_books = [book1, book2, book3, book4]
for book_obj in list_books:
    book_obj.display()

books_jack = [book_obj.title for book_obj in list_books if book_obj.author == 'Jack']
print(books_jack)