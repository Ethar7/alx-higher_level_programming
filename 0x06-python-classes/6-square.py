#!/usr/bin/python3
"""
This module defines the 'Square' class which models a geometric square with properties
like size and position. It includes methods to calculate the square's area and print
the square using ASCII art.
"""

class Square:
    """A class that defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square, must be an integer greater than or equal to 0.
            position (tuple): The position of the square as a tuple of 2 positive integers.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: The size of the square, must be an integer greater than or equal to 0."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square as a tuple of 2 positive integers."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, ensuring it's a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character to stdout."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
