# 4. Write two classes Factorial and FactorialIterator to implement an iterable that gives Factorial of numbers
# and supports multiple scans.

class Factorial:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return FactorialIterator(self)


class FactorialIterator:

    def __init__(self, source):
        self.source = source
        self.current = self.source.start

    def __next__(self):

        if self.current > self.source.stop:
            raise StopIteration
        else:
            f = self.fact(self.current)
            self.current += 1
            return f

    def fact(self, number):
        if number == 1 or number == 0:
            return 1
        return number * self.fact(number-1)


x = Factorial(5,10)
for i in x:
    print(i, end=' ')
