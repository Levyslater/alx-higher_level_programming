#!/usr/bin/python3


class MyList(list):
    """My list class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
