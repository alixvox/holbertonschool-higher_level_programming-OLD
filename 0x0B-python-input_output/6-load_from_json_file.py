#!/usr/bin/python3
"""
This module contains method load_from_json_file().
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file(filename) returns an Object from a JSON file.
    """

    with open(filename) as f:
        return json.loads(f.read())
