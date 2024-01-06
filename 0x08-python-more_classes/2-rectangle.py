#!/usr/bin/python3
"""A Rectangle module"""


class Rectangle:
    """A class named Rectangle"""
    def __init__(self, width=0, height=0):
        """Method initializes an instance once created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to retrieve attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method sets value for attribute width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """method to retrieve the value of attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method to set the value of attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Module returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Module returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
