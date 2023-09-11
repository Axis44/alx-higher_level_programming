#!/usr/bin/python3
"""Module defines containing same class method"""


def is_same_class(obj, a_class):
    """Returns:
    True: if object is an instance of specified class
    False: otherwise, not success"""
    return type(obj) == a_class
