#!/usr/bin/python3
"""Module adds new attribute if possible"""


def add_attribute(attrib, name, value):
    """Add a new attribute to an object if possible"""
    if hasattr(attrib, '__dict__') or (hasattr(attrib, '__slots__')
                                       and name in attrib.__slots__):
        setattr(attrib, name, value)
    else:
        raise TypeError("can't add new attribute")
