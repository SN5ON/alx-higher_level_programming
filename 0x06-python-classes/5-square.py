#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """class square with attributes."""

    def __init__(self, size):
        """Initialize a function,

        for class square.
        """
        self.size = size

    @property
    def size(self):
        """set size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
