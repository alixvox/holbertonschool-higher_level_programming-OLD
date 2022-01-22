#!/usr/bin/python3
"""
This module contains method is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class returns true if object obj
    is an instance of class a_class or a
    subclass of a_class.
    """

    return isinstance(obj, a_class)
