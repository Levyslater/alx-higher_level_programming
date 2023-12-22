#!/usr/bin/python3
"""A class module"""
class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """Initializes new objects
        Args:
        size: length of the square"""
        self.size = size

    @property
    def size(self):
        """Method retreives private property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method sets the private property"""
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """Method returns the area of a square"""
            return self.__size ** 2
