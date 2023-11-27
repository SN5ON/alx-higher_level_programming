#!/usr/bin/python3
# define class rectangle

class rectangle:
    """rectangle represented"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
            return self._width
        
    @width.setter
    def width(self, value):
           """setter for the private instance attribute width"""
            if type(value) is not int:
                    raise TypeError("width must be an integer")
                    if value < 0:
                    raise ValueError("width must be >= 0")
                    self._width = Value
    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self._height

    @height.setter
     def height(self, value):
     """getter for the private attribute height"""   
        if type(value) is not int:
        raise TypeError("height must be an integer")
        if value < 0:
        raise ValueError("height must be >= 0")
        self._height = value
