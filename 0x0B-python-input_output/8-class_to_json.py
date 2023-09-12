#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    """
        returns dictionary string with simple data structure.
    """
    return obj.__dict__
