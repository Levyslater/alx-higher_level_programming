#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        _str = "[" + str(self.__class__.__name__) + "] "
        _str += str(self.__size) + "/" + str(self.__size)
        return _str
