#!/usr/bin/python3
"""
This module contains method inherits_from.
"""


def inherits_from(obj, a_class):
    """
    inherits_from returns true if an object is
    an instance of a class inherited by that class.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
