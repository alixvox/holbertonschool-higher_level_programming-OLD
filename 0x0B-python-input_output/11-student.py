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

        self_dict = self.__dict__.copy()
        if attrs and all(isinstance(item, str) for item in attrs):
            for i in self.__dict__.keys():
                if i not in attrs:
                    self_dict.pop(i)
        return self_dict

    def reload_from_json(self, json):
        """
        reload_from_json(self, json) uses dict json
        to replace self's attributes.
        """

        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json['age']
