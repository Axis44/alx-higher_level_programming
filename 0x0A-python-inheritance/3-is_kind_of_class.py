#!/usr/bin/python3
"""Module containing kind of class method"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a class that inherited from
    the specified class ; otherwise False no class """
    return isinstance(obj, a_class)
