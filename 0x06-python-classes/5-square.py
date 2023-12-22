#!/usr/bin/python3
"""A class module"""
class Square:
    """Sets up a class named Square"""
    def __init__(self, size=0):
        """Initializes new instances
        Args:
        size: length of the square"""
        self.size = size

    @property
    def size(self):
        """Method to retreive attributes"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method for setting attributes"""
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """method prints the area of a square using #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
