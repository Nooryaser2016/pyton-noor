from abc import ABC, abstractmethod
import math


class Polygon(ABC):
    abstractmethod
def area(self):
    pass


class Rectangle(Polygon):
    def __init__(self, length, width):
     self.length = length
     self.width = width

def area(self):
   return self.length * self.width


class Square(Rectangle):
   def __init__(self, side):
      super().__init__(side, side)


class Triangle(Polygon):
   def __init__(self, base, height):
      self.base = base
      self.height = height

def area(self):
   return 0.5 * self.base * self.height

class Circle(Polygon):
   def __init__(self, radius):
      self.radius = radius

def area(self):
   return math.pi * self.radius ** 2



rectangle = Rectangle(10, 5)
square = Square(4)
triangle = Triangle(6, 3)
circle = Circle(7)


print("Area of Rectangle:", Rectangle.area())
print("Area of Square:", square.area())
print("Area of Triangle:", triangle.area())
print("Area of Circle:", circle.area())
