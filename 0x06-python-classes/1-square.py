#!/usr/bin/python3
"""Module for Square class with private attribute size."""

class Square:
    """Square class: Represents a square with a private attribute size."""
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private attribute

