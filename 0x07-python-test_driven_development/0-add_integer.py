#!/usr/bin/python3
""" this is module documentation"""


def add_integer(a, b=98):
    """
    Function to add two nums a, b
    if a, b float it casted to int
    else raise type error

    Args:
    a: int or float
    b: int or float

    Returns:
    an int sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "main":
    import doctest
    doctest.testfile(tests/0-add_integer.txt)
