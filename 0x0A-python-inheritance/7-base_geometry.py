#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


class BaseGeometry():
    """
    BaseGeometry contains an unimplemented method area() and
    method integer_validator().
    """

    def area(self):
        """
        area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validation validates that int
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
