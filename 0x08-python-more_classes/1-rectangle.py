#!/usr/bin/python3
"""module documentation"""


class Rectangle:
    """class that defines a rectangle with private width height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle, ensuring it is an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, ensuring it is integer non-negative."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
