#!/usr/bin/python3
"""class inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class creates a new tectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the rectangle. Defaults to 0.
            id (int, optional): The unique ID of the rectangle. If not specified, a random integer will be generated.

        Raises:
            ValueError: If the width or height is less than or equal to zero.
            TypeError: If the width or height is not an integer.
            ValueError: If the x or y coordinate is less than zero.
            TypeError: If the x or y coordinate is not an integer.
        """
        super().__init__(id)
        if isinstance(width, int):
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
        if isinstance(x, int):
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
        if isinstance(y, int):
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        """Retreive value of width"""
        return self.__width
    @property
    def height(self):
        """Retreive value of height"""
        return self.__height
    @property
    def x(self):
        """Retreives value of x"""
        return self.__x
    @property
    def y(self):
        """Retreives value of y"""
        return self.__y
    @width.setter
    def width(self, value: int):
        """Sets value of width.

        Args:
            value (int): The new width value.

        Raises:
            ValueError: If the value is not a positive integer.

        """
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value: int):
        """Sets value of height.

        Args:
            value (int): The new height value.

        Raises:
            ValueError: If the value is not a positive integer.

        """
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
    @x.setter
    def x(self, value):
        """Sets value of x"""
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
    @y.setter
    def y(self, value):
        """Sets value of y"""
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            print('')
            return

        for i in range(self.__y):
            print('')

        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)


    def __str__(self):
        """Returns string representation of rectangle"""
        _string = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return _string

    def update(self, *args, **kwargs):
        """Updates rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """
        Returns:
            dict: A dictionary representation of the Rectangle instance, with keys "id", "width", "height", "x", and "y".
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
