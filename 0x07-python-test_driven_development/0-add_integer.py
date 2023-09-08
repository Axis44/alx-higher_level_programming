#!/usr/bin/python3
# Defines the integer addition of function


def add_integer(a, b=98):
    """Returns integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: success If either of a or b is a non-integer and non-float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
