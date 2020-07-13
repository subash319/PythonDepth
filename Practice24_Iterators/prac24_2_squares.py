# 2. Write two classes Squares and SquaresIterator to implement an iterable that gives squares of numbers and
# supports multiple scans.


class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return SquaresIterator(self)


class SquaresIterator:
    def __init__(self, source):
        self.source = source
        self.current = source.start

    def __next__(self):
        if self.current > self.source.stop:
            raise StopIteration
        else:
            sq = self.current * self.current
            self.current += 1
            return sq

x = Squares(1,10)

for i in x:
    print(i, end = ' ')
for i in x:
    print(i, end = ' ')