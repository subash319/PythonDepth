# 1. This is a function to find the highest common factor of two numbers

# Make it a static method in the Fraction class that you had written in earlier exercise.

class Fraction:

    def __init__(self, nr, dr=1):
        self.nr = nr
        # making the denominator postive if it is negative
        self.dr = dr if dr >=0 else -dr

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self, f1):
        if isinstance(f1, int):
            return Fraction((self.nr*f1), self.dr)
        else:
            return Fraction((self.nr*f1.nr), (self.dr*f1.dr))

    def add(self, fa):
        if isinstance(fa, int):
            fa = Fraction(fa)
        return Fraction((self.nr * fa.dr + fa.nr * self.dr), (self.dr * fa.dr))

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()
print(Fraction.hcf(20, 15))
