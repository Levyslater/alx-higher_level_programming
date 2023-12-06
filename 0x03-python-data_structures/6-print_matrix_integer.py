#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = ' '.join(map(str, row))
        print("{}".format(i))
