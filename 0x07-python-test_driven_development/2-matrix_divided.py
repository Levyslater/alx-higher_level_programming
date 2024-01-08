#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Function divides each element of a matrix with div
        Returns a new matrix with element products
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            all(isinstance(val, (int, float))for val in row)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = [len(row) for row in matrix]
    if len(set(row_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [
        [round(value / div, 2) for value in row]
        for row in matrix
    ]

    return new_matrix
