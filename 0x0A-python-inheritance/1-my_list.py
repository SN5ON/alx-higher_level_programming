#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """Pint sorted list"""
        print(sorted(self))
