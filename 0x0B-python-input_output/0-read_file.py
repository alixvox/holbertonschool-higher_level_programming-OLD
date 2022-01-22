#!/usr/bin/python3
"""
This module contains method read_file.
"""


def read_file(filename=""):
    """
    read_file() reads a file with str filename.
    """

    with open(filename) as f:
        print(f.read())
