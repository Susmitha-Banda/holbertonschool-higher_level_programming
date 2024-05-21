#!/usr/bin/python3
"""creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """create an empty rectangle object."""

    # Class attribute to keep track of number of instances
    number_of_instances = 0
    # Class attribute to define the symbol for string representation
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        '''class method: creates a square, which is a type of rectangle
        '''
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __init__(self, width=0, height=0):
        """initialising a new rectangle
        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        # Increment the class attribute when a new instance is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        '''print the rectangle with the character stored in print_symbol'''
        if self.width == 0 or self.height == 0:
            return ""

    def __repr__(self):
        """Return a string representation of the rectangle for eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """method: __del__
           deletes instance of Rectangle class, and prints "bye" message
        """
        print("Bye rectangle...")
        # Decrement the class attribute when an instance is deleted
        Rectangle.number_of_instances -= 1
