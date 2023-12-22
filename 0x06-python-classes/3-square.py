#!/usr/bin/python3
"""A class module"""


class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """Initialize new instances
        Args:
        size: length of the square"""
        self.__size = size

        if (type(size) != int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method returns area of a sqaure"""
        return (self.__size ** 2)
