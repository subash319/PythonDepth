# 6. Make a class Fraction that contains two instance variables, nr and dr
# (nr stands for numerator and dr for denominator). Define an __init__ method that provides values
# for these instance variables. Make the denominator optional by providing a default argument of 1.
#
# In the __init__ method, make the denominator positive if it is negative.
# For example  -2/-3 should be changed to 2/3 and 2/-3 to -2/3.
#
# Write a method named show that prints numerator, then '/' and then the denominator.
#
# Make sure that you write this class as we will be using it to learn magic methods.


class Fraction:

    def __init__(self, nr, dr=1):
        self.nr = nr
        # making the denominator postive if it is negative
        self.dr = dr if dr >=0 else -dr

    def display(self):
        print(f'{self.nr}/{self.dr}')


f1 = Fraction(2, 3)
f2 = Fraction(-2, -3)
f1.display()
f2.display()
