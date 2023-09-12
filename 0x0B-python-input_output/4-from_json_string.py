#!/usr/bin/python3
"""
json string
"""
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object
    Args:
        my_str: json string to represent
    Return: the object
    """
    return json.loads(my_str)
