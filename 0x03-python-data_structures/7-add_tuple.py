#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    new_tuple = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    return new_tuple[:2]
