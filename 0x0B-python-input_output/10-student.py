#!/usr/bin/python3
"""
This module contains class Student.
"""


class Student:
    """
    Student has str  first_name and last_name, and int age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization with str first_name, str last_name, and int age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json(self) returns the dictionary representation of self.
        """

        self_dict = {}
        if type(attrs) is list and all(isinstance(item, str) for item in attrs):
            for i in attrs:
                if hasattr(self, i):
                    self_dict.update({i: getattr(self, i)})
            return self_dict
        return self.__dict__
