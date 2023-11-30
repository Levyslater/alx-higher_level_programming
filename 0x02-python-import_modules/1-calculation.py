#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    """My addition function"""

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))

    """My subtraction function"""

    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a, b)))

    """my multiplication function"""

    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(a, b)))

    """My division function"""

    a = 10
    b = 5

    print("{} / {} = {}".format(a, b, div(a, b)))
