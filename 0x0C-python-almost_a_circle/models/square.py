#!/usr/bin/python3
"""A module that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that creates a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the square. Defaults to 0.
            id (int, optional): The unique ID of the square. If not specified, a new ID will be generated. Defaults to None.

        Raises:
            ValueError: If the size is less than or equal to zero.
            TypeError: If the size is not an integer.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns:
            str: A string representation of the square object.
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            ValueError: If the size is less than or equal to zero.
            TypeError: If the size is not an integer.
        """
        if isinstance(size, int):
            if size > 0:
                self.width = size
                self.height = size
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """
        Updates the properties of the square object.

        Args:
            *args: Positional arguments. The order of the arguments is as follows: id, size, x, y.
            **kwargs: Keyword arguments. The keys of the dictionary are the attribute names and the values are the new values of the attributes.

        Raises:
            ValueError: If the size is less than or equal to zero.
            TypeError: If the size is not an integer.

        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            dict: A dictionary representation of the square object. The keys are "id", "x", "size", and "y".
        """
        return {"id": self.id, "x": self.x,
                "size": self.width, "y": self.y}            