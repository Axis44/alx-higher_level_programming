#!/usr/bin/python3
"""Define MyList module"""


class MyList(list):
    """class of Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
