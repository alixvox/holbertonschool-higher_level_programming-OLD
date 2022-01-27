#!/usr/bin/python3
"""
This module contains class Base.
"""


class Base:
    """
    A Base has an optional int id and a class attribute int __nb_objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization with an optional int id.
        Otherwise, __nb_objects is incremented
        and assigned to id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
