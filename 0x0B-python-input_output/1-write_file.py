#!/usr/bin/python3
"""
This module contains method write_file.
"""


def write_file(filename="", text=""):
    """
    write_file() writes a str text to file with str filename.
    """

    with open(filename, 'w') as f:
        return f.write(text)
