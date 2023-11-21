#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """class square with attributes."""

    def __init__(self, size=0):
        """
        Initialize a function for square,

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """gives current area of the square."""
        return (self.__size * self.__size)
