#!/usr/bin/python3
"""My module"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        written_chars = f.write(text)
        return written_chars
