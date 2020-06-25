# 2. In your Fraction class, write a private instance method _reduce that reduces a fraction to its lowest terms.
# To reduce a Fraction to its lowest terms you have to divide the numerator and denominator by the highest
# common factor.
# Call this method in __init__and also call it on the resultant fraction in methods multiply and add.


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

    # Reduces the Fraction to its lowest terms
    # To reduce the fraction we have to divide the numerator and denominator with HCF
    def _reduce(self):
        hcf_two_num = Fraction.hcf(self.nr, self.dr)
        self.nr //= hcf_two_num
        self.dr //= hcf_two_num

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


f2 = Fraction(3,4)
f2.show()