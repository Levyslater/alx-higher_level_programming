#!/usr/bin/python3
"""A class module"""


class Square:
    """A class named Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes new objects
        Args:
        size: square length
        position: Tuple defining spaces to print"""
        self.size = size
        self.__position = position

    @property
    def position(self):
        """Method retreives private property position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method sets up private property position"""
        if isinstance(self.__position, tuple) and \
                len(self.__position) == 2:
            if all(isinstance(var, int) and var > 0
                   for var in self.__position):
                self.__position == value
            else:
                raise TypeError("position must be a tuple \
                                of 2 positive integers")

    @property
    def size(self):
        """Method to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set size"""
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """"Method Returns area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Method prints area of a square
        using # and position arguments as spaces"""
        if self.size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
