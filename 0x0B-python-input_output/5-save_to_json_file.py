#!/usr/bin/python3
"""
This module contains method save_to_json_file().
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file(my_obj, filename) writes an Object to a text file.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
