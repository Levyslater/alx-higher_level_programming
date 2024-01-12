#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """checks if 'obj' is an instance of 'a_class'
    or of a class that inherited from 'a_class'
    """
    return isinstance(obj, a_class)
