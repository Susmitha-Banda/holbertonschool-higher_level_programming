#!/usr/bin/python3
"""creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """create an empty rectangle object."""

    def __init__(self, width=0, height=0):
        """initialising a new rectangle
        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

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

    """calculates the area of rectangle"""
    def area(self):
        """defines the area of rectangle"""
        return self.__width * self.__height

    """calculates the perimeter of rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''print the rectangle with the character "#'''
        if self.width == 0 or self.height == 0:
            return ""

        my_rectangle = ""
        for i in range(self.height):
            my_rectangle += self.width * "#"
            if i < self.height - 1:
                my_rectangle += "\n"
        return my_rectangle

    def __repr__(self):
        """Return a string representation of the rectangle for eval()"""
        return f"Rectangle({self.__width},{self.__height})"
