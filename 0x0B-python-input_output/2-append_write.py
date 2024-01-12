#!/usr/bin/python3
"""My module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        appended_chars = f.write(text)
    return appended_chars
