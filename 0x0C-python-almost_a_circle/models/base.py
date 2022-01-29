#!/usr/bin/python3
"""
This module contains class Base.
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_dictionaries returns a JSON string representation
        of a dictionary, 'list_dictionaries'.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file writes the JSON string representation of
        a list of squares and rectangles, list_objs.
        """
        filename = cls.__name__ + ".json"
        dict_objs = []
        if list_objs:
            for item in list_objs:
                dict_objs.append(cls.to_dictionary(item))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(dict_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string returns a list of the json string representation
        json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create returns an instance with all attributes
        set to itself.
        """
        shape = cls(4, 4)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """
        load_from_file loads a list of objects from a json file.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return list_dicts
        with open(filename, 'r') as file:
            list_dicts = cls.from_json_string(file.read())
        list_objs = []
        for dict in list_dicts:
            list_objs.append(cls.create(**dict))
        return list_objs
