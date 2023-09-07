#!/usr/bin/python3
"""Defines the name-printing of function."""


def say_my_name(first_name, last_name=""):
    """Print my name.

    Args:
        first_name (str): first name to print.
        last_name (str): last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    # fist name must be an intege
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # last name must be an intege
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
