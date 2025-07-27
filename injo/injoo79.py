from abc import ABC, abstractmethod
import math

# Base class
class Polygon(ABC):
        def __init__(self, name):
            self.__name = name # encapsulation

@abstractmethod
def area(self):
    pass

def get_name(self):
    return self.__name


# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width

def area(self):
    return self.__length * self.__width


# Square class
class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.__side = side

def area(self):
    return self.__side ** 2


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.__base = base
        self.__height = height

def area(self):
    return 0.5 * self.__base * self.__height


# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius

def area(self):
    return math.pi * self.__radius ** 2


# Function to display area of any polygon
def display_area(polygon):
    print(f"The area of the {polygon.get_name()} is: {polygon.area():.2f}")


# Example usage:
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    square = Square(4)
    triangle = Triangle(6, 3)
    circle = Circle(7)

display_area(rect)
display_area(square)
display_area(triangle)
display_area(circle)