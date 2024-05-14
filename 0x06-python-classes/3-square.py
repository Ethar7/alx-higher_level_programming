#!/usr/bin/python3
"""Module for Square class with size validation."""


class Square:
    """Square class: Represents a square with a validated size attribute."""
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
        """Return the current square area."""
        return self.__size ** 2
