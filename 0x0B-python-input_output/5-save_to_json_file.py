#!/usr/bin/python3
"""
save to json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file -  writes an Object to a text file:
    Args:
        my_obj:
        filename:
    Return:json file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
