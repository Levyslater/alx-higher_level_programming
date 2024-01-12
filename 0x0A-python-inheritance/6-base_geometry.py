#!/usr/bin/python3
"""My module"""


class BaseGeometry:
    """My class that raises an exception"""
    def area(self):
        """Raises an exception with specified message"""
        raise Exception("area() is not implemented")
