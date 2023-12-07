#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    k = 0
    new_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])
    for row in matrix:
        for i in row:
            res.append(i**2)
    for idx in range(0, rows):
        sub = []
        for jdx in range(0, columns):
            sub.append(res[k])
            k += 1
        new_matrix.append(sub)
    return new_matrix
