#!/usr/bin/python3
"""My class module"""


class MyList(list):
    """My list class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
