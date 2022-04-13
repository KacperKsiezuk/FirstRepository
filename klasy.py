class Vehicle:
    pass

#

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

car_1 = Car("blue", 20000)
car_2 = Car("red", 30000)

print(car_1)
print(car_2)

#

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self, perimeter):
        return (2*self.length)+(2*self.width)
    def area(self, area):
        return self.length*self.width
    def __str__(self):
        return f"Length: {self.length}, Width: {self.width},\nPerimeter: {self.perimeter()}, Area: {self.area()}"

rectangle = Rectangle(7, 11)
print(rectangle)
