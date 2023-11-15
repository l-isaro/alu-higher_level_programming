#!/usr/bin/python3
""" This module contains the class square that defines 
a square object with size and area
"""


class Square:
    """ This class defines sqaure objects
    attributes:
    private size

    methods:
    getter
    setter
    area
    my_print
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

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)

    def check_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
