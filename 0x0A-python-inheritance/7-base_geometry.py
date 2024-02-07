#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """not area complete"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
