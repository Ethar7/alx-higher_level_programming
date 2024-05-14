#!/usr/bin/python3
"""
This module defines the Square class with private instance attribute size,
and a method to calculate the area of the square.
"""


class Square:
    """
    Represents a square with a private instance attribute size that is
    validated,
    and a public instance method to calculate the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square with optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the current square area.
        Returns:
            The area of the square.
        """
        return self.__size ** 2
