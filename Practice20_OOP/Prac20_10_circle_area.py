# 10. Write a Circle class with an instance variable named radius and a method named area.
# Create two more attributes named diameter and circumference and make them behave as read only attributes.
#
# Perform data validation on radius, user should not be allowed to assign a negative value to it.
#
# For a circle
#
# diameter =  2 * radius
#
# circumference =  2 * 3.14 * radius
#
# area =  3.14 * radius * radius


class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def diameter(self):
        return 2*self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    @property
    def radius(self):
        print(self._radius)
        return self._radius


    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError("The radius should be a postive value")


c1 = Circle(2)
c2 = Circle(3)
print(c1.radius, c1.diameter, c1.circumference, c1.area() )
print(dir(Circle))
