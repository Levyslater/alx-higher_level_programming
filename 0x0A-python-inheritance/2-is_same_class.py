#!/usr/bin/python3
"""My module"""


def is_same_class(obj, a_class):
    """Returns true if "obj" is an instance of "a_class.
    Returns False otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
