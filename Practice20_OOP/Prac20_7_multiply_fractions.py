# 7. Define a method named multiply that multiples two Fraction instance objects.
# For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.
#
# Inside the method, create a new instance object that is the product of the two fractions and return it.
# Write your method in such a way that it supports multiplication of a Fraction by an integer also.
#
# Similarly define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is
# (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer.
#
# Test your fraction class with this code.

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
