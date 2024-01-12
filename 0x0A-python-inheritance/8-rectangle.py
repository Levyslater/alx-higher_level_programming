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
