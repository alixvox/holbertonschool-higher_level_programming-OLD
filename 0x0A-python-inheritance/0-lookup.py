#!/usr/bin/python3
"""
This module contains lookup()
"""


def lookup(obj):
    """
    lookup() returns a list of an object obj's
    available attribues and methods.
    """
    return dir(obj)