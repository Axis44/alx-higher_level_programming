#!/usr/bin/python3
"""
load from json file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - loads the object from JSON file.
    Args:
        filename: name of the file
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
