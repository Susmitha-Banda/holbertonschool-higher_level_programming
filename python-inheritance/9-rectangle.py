#!/usr/bin/python3
""" implements a Geometry class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """implementing rectangle class"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """defining area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle]" + str(self.__width) + "/" + str(self.__height))
