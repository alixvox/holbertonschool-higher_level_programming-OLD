#!/usr/bin/python3
"""
This module contains method class_to_json().
"""


def class_to_json(obj):
    """
    class_to_json(obj) returns the dictionary description of an object.
    """

    return obj.__dict__