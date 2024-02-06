#!/usr/bin/python3
"""Defines a class Rectangle from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class using BaseGeometry"""

    def __init__(self, width, height):
    """new rectangle in """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
