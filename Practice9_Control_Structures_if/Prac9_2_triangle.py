# 2. Write a program that inputs the length of three sides of a triangle, and prints the perimeter of the triangle.
# It should also print whether the triangle is equilateral, isosceles or scalene.

# If there is no triangle possible with the given sides, then instead of printing the
# above things it should print 'No triangle possible with these sides'
#
# ( In an equilateral triangle, all sides are equal.
#
#   In an isosceles triangle, any two sides are equal.
#
#   In a scalene triangle, all three sides are unequal.
#
#   For a triangle to be possible with given sides, sum of any two sides should be greater than the third side. )

l1 = int(input('Enter the length of the first side:'))
l2 = int(input('Enter the length of the second side:'))
l3 = int(input('Enter the length of the third side:'))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('perimeter of the triangle:', l1+l2+l3)
    if l1 == l2 == l3:
        print("Its a equilateral triangle")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Its a isosceles triangle")
    else:
        print("Its a scalene triangle")
else:
    print("The triangle is not possible with the mentioned dimensions")
