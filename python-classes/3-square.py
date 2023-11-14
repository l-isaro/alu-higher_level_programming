#!/usr/bin/python3
""" This module conatins a class square
"""

class Square:
    """ This class defines objects of square
    attributes:
    private size
    
    methods:
    public area
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return(self.__size ** 2)
