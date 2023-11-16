#!/usr/bin/python3
""" This module contains the class square
"""


class Square:
    """ This class defines attributes and methods for the 
    square object

    attributes:
    private size
    private position

    methods:
    getter methods
    setter methods
    area
    my_print
    """
    def __init__(self, size=0, position=(0, 0)):
        
        self.check_size(size)
        self.__size = size
        self.check_position
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.check_size(value)
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.check_position(value)
        self.__position = value

    def area(self):
        return (self.__Size ** 2)

    def my_print(self):
        if self.__Size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__Size):
            print(" " * self.__position[0], "#" * self.__Size, sep='')

    def check_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def check_position(self, value):
        if not (len(value) == 2 and isinstance(value, int)):
            raise TypeError("position must  be an integer of 2 positive integers")
