#!/usr/bin/python3
# define class rectangle

class rectangle:
    """rectangle represented"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        @property
        def width(self):
           
            return self._width
        
        @width.setter
        def width(self, value):
           
            if type(value is not int:
                    raise TypeError("width must be an integer")
                    if value < 0:
                    raise ValueError("width must be >= 0")
                    self._width = Value
        @property
        def height(self):
        
        return self._height
        
        @height.setter
        def height(self, value):
        
        if type(value) is not int:
        raise TypeError("height must be an integer")
        if value < 0:
        raise ValueError("height must be >= 0")
        self._height = value
