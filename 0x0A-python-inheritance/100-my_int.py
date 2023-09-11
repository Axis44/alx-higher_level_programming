#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """My class integer"""
    def __eq__(self, other):
        """Overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts != operator"""
        return int(self) == int(other)
