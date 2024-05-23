#!/usr/bin/python3
"""this is a module documentation"""


def lookup(obj):
    """
    function Returns a list of available attributes and methods of an object.

    Args:
        obj: Object whose attributes and methods are to be looked up.

    Returns:
        list: List of available attributes and methods.
    """
    return dir(obj)
