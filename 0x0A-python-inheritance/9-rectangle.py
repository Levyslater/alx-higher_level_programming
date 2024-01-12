#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry
(7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """My rectangle class"""
    def __init__(self, width, height):
        """Initializes a new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation"""
        _str = "[" + str(self.__class__.__name__) + "] "
        _str += str(self.__width) + "/" + str(self.__height)
        return _str

    def area(self):
        """Return area of a triangle"""
        return self.__width * self.__height
