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
    prev_list = [1]
    for i in range(n):
        my_list.append(prev_list)
        curr_list = []
        curr_list.append(prev_list[0])
        for i in range(len(prev_list) - 1):
            curr_list.append(prev_list[i] + prev_list[i + 1])
        curr_list.append(prev_list[-1])
        prev_list = curr_list
    return my_list
