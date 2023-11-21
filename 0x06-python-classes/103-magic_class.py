#!/usr/bin/python3
"""class MagicClass matching the python bytecode provided"""

import math


class MagicClass:
    """class magicClass with attributes"""

    def __init__(self, radius=0):
        """Initialize of a function,
        for class magicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
