#!/usr/bin/python3
"""this module is about creating an abstract class named Shape using the ABC
package."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """creating an abstract class shape"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def permieter(self):
        pass


class Circle(Shape):
    """creating circle class inherits from Shape class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        '''area of a circle, 𝜋 × radius2 '''
        return ("math.pi * (self.radius ** 2)")

    def permieter(self):
        '''circumference of a circle is 2𝜋𝑟 '''
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """creating a Rectangle class inherits from shape class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def permieter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


# Testing with Circle and Rectangle instances
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    shape_info(rectangle)
