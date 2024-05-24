#!/usr/bin/python3
"""this is module documentation"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    # Set the attribute
    setattr(obj, attr_name, attr_value)
