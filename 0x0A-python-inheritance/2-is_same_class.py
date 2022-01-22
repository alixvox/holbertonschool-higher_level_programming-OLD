#!/usr/bin/python3
"""
This module contains method is_same_class.
"""


def is_same_class(obj, a_class):
    """
    is_same_class returns true if object obj
    is exactly an instance of class a_class.
    """

    return type(obj) == a_class
