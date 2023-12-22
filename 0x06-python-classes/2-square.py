#!/usr/bin/python3
"""A class module """
class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """initializer method
        Args:
        size: Square length"""
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
