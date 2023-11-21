#!/usr/bin/python3
"""class square with parameters"""


class Square:
    """class square with attributes of size"""

    def __init__(self, size=0):
        """Initialize a new function, with parameter size  set to 0."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
