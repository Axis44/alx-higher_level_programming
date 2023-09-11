#!/usr/bin/python3
"""Defines lookup module"""


def lookup(obj):
    """lookup method
    Returns: a list of available attributes and object"""
    return dir(obj)
