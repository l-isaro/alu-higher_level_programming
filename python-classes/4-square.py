#!/usr/bin/python3
""" This module contains the class square
"""


class Square:
    """ This class defines the square object

    attributes:
    private size

    methods:
    getter method
    setter method
    area
    """
    def __init__(self, size=0):

        self.check_size(size)

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.check_size(value)
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def check_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
