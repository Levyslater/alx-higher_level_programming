#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None
    else:
        x = len(list_of_integers)
        index = 0
        for i in range(x):
            index = (index + i) % x
        return(list_of_integers[index])
