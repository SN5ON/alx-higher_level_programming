#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """class square with attributes."""

    def __init__(self, size=0):
        """Initialize a function,

        for class square
        """
        self.size = size

    @property
    def size(self):
        """setter of  size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """gets the area of the square."""
        return (self.__size * self.__size)
