#!/usr/bin/python3
"""
This module contains one function, matrix_divided.
"""
def matrix_divided(matrix, div):
    """
    returns a matrix of ints divided by an int, div.
    """

    list_len = len(matrix[0])
    div_matrix = []
    for i in matrix:
        for num in i:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for x in range(len(matrix)):
        div_matrix.append([])
        for y in range(len(matrix[x])):
            float_div = matrix[x][y] / div
            div_matrix[x].append(round(float_div, 2))
    return div_matrix
