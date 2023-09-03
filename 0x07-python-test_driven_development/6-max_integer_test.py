#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function must find and return max integer in the list of integers
        If the list is empty, function must return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    n = 1
    while n < len(list):
        if list[n] > result:
            result = list[n]
        n += 1
    return result
