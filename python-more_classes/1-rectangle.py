#!/usr/bin/python3
""" This module contains an empty class rectangle
"""


class Rectangle:
    """ a class to represent a rectangle

    Attributes:
    width
    height
    """
    def __init__(self, width=0, height=0):
        self.check_width(width)
        self.__width = width
        self.check_height(height)
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_height(value)
        self.__height = value

    def check_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def check_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
