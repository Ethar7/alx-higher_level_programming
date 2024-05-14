#!/usr/bin/python3
"""
This module provides a MagicClass that performs geometric calculations.
"""
import math

class MagicClass:
    """
    A class that represents a geometric shape with methods to calculate
    area and circumference.
    """
    
    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius."""
        self.__check_radius(radius)
        self.__radius = radius

    def __check_radius(self, radius):
        """Check if the radius is a number (int or float)."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
