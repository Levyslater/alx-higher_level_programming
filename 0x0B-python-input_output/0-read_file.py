#!/usr/bin/python3
"""My module"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    print(data)
