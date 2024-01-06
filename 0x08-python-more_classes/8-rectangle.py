#!/usr/bin/python3
"""A Rectangle module"""


class Rectangle:
    """A class named Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Method initializes an instance once created"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to retrieve attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method sets value for attribute width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """method to retrieve the value of attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method to set the value of attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Module returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Module returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """module returns string representation of rectangle with hashes"""
        if self.__width == 0 or self.__height == 0:
            return ''
        hashes = []
        for i in range(self.__height):
            for j in range(self.__width):
                hashes.append(str(self.print_symbol))
            if i != self.__height - 1:
                hashes.append("\n")
        return (''.join(hashes))

    def __repr__(self):
        """module returns a string representation of a rectangle"""
        return (
            "Rectangle(" + str(self.__width)
            + ", " + str(self.__height) + ")"
        )

    def __del__(self):
        """modle prints delete message for instances"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
