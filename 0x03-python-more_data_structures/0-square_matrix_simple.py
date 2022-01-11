#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sqr = []
    for i in matrix:
        matrix_sqr.append(list(map(lambda x: x**2, i)))
    return matrix_sqr
