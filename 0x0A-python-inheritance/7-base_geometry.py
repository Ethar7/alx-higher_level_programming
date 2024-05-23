#!/usr/bin/python3
"""this is a module documentation"""


class BaseGeometry:
    """this is class doc"""
    def area(self):
        """this is fuc doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is func doc"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
