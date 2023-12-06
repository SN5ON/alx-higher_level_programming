#!/usr/bin/python3
"""Defines a class-checking method"""


def is_same_class(obj, a_class):
    """Check if an object is an instance class
    """
    if type(obj) == a_class:
        return True
    return False
