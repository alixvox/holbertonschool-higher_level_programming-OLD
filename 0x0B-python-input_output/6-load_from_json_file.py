#!/usr/bin/python3
import json
"""
This module contains method load_from_json_file().
"""


def load_from_json_file(filename):
    """
    load_from_json_file(filename) returns an Object from a JSON file.
    """

    with open(filename) as f:
        return json.load(f)