#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            print("{:d}".format(matrix[x][y]), end = " ")
        print("")
