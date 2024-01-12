#!/usr/bin/python3
"""My module"""


class MyInt(int):
    """class that inverts '==' and '!='"""
    def __eq__(self, value):
        """changes default equality operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """changes the default inequality operator"""
        return super().__eq__(value)
