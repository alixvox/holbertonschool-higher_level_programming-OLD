#!/usr/bin/python3
"""
This module adds all args to list, and saves it to a file.
"""
import sys
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
if exists("add_item.json"):
    argv_list = load_from_json_file("add_item.json")
else:
    argv_list = []
for i in sys.argv[1:]:
    argv_list.append(i)
save_to_json_file(argv_list, "add_item.json")
