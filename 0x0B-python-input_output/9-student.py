#!/usr/bin/python3
"""
This module contains class Student.
"""


class Student:
    """
    Student has str first_name and last_name, and int age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization with str first_name, str last_name, and int age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json(self) returns the dictionary representation of self.
        """

        return self.__dict__
