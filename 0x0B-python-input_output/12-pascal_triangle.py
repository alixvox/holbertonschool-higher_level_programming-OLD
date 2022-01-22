#!/usr/bin/python3
"""
This module contains method pascal_triangle().
"""


def pascal_triangle(n):
    """
    pascal_triangle(n) returns a list of lists of ints
    corresponding with pascal's triangle formula.
    """

    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        num_list = [int(x) for x in str(11**i)]
        my_list.append(num_list)
    return my_list
