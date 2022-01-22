#!/usr/bin/python3
"""
This module contains method from_json_string().
"""
import json


def from_json_string(my_str):
    """
    from_json_string(my_str) returns an object
    represented by a JSON str my_str.
    """

    return json.loads(my_str)
