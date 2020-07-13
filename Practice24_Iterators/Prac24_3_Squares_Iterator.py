# 3. Implement an iterator that gives squares of numbers using a single class.


class Squares:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            sq = self.current * self.current
            self.current += 1
            return sq



x = Squares(1,10)
print(sum(x))
for i in x:
    print(i, end = ' ')

