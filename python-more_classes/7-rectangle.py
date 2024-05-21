#!/usr/bin/python3
"""creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """create an empty rectangle object."""

    # Class attribute to keep track of number of instances
    number_of_instances = 0
    # Class attribute to define the symbol for string representation
    print_symbol = "#"

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

        my_rectangle = ""
        for i in range(self.height):
            my_rectangle += str(self.print_symbol) * self.width
            if i < self.height - 1:
                my_rectangle += "\n"
        return my_rectangle

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
