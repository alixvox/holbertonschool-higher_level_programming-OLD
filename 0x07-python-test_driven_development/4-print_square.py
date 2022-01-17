#!/usr/bin/python3
"""
This module contains one funcion, print_square.
"""


def print_square(size):
    """
    This function prints a square with the character #.
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
