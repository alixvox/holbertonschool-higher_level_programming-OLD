#!/usr/bin/python3
import json
"""
This module contains method from_json_string().
"""


def from_json_string(my_str):
    """
    from_json_string(my_str) returns an object represented by a JSON str my_str.
    """

    return json.loads(my_str)