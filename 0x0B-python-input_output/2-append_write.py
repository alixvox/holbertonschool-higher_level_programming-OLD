#!/usr/bin/python3
"""
This module contains method append_write.
"""


def append_write(filename="", text=""):
    """
    append_write appends a str text at the end of file filename.
    """

    with open (filename, 'a') as f:
        return f.write(text)