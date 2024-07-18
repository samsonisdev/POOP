# Practice Question 3:
# Define a Circle class to create a circle with radius in the constructor
# Define an area method of the class that calculates the area of the circle
# Define a perimeter method of the class that calculates the perimeter of the circle

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = ((22/7) * pow(self.radius, 2))
        return round(area, 2)

    def perimeter(self):
        peri = 2 * (22/7) * self.radius
        return round(peri, 2)


r = Circle(5)
print(r.area())
print(r.perimeter())