# 6. Write a program that inputs radius of a circle, and displays it area and circumference.
# Area of a circle = π * r * r
# Circumference = 2 * π * r
# where r = radius of circle and π = 3.14159

pi = 3.14
radius_circle = float(input("Enter the radius of the circle:"))
area_circle = pi * radius_circle * radius_circle
circumference_circle = pi * pi * radius_circle
print(f"For the radius {radius_circle} the area of circle and circumference are equal to {area_circle}, "
      f"{circumference_circle} respectively")