# 1. Write a class for implementing an infinite iterator that gives out Fibonacci numbers.


# class Fibonacci:
#
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         f = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return f
#
#
# x = Fibonacci()
# while next(x) <= 1000:
#     print(next(x), end = ' ')

class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        self.a, self.b = self.b, self.a + self.b
        return f


x = Fibonacci()

# while next(x) <= 50:
for i in x:
    if i >= 1000:
        break
    print(i, end = ' ')
