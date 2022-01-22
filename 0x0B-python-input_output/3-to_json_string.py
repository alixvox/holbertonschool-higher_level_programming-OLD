#!/usr/bin/python3
"""
This module contains method to_json_string.
"""
import json


def to_json_string(my_obj):
    """
    to_json_string() returns the JSON  str representation of an object.
    """

    return json.dumps(my_obj)
