#!/usr/bin/python3
"""
This module contains one function, text_indentation.
"""


def text_indentation(text):
    """
    This function prints a string with 2 new lines after
    ``.``, ``?``, and ``:``.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char == '.' or char == '?' or char == ':':
            print("\n\n")
