#!/usr/bin/python3
""" This module contains the class Square """

from rectangle import Rectangle


class Square(Rectangle):
    """ a class that represents a circle
        :param size: represents the size of the rectangle
        :param x: represents the x coordinate
        :param y: represents the y coordinate
        :param id: uniquely represents the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns the size value"""
        return self.size

    @size.setter
    def size(self, value):
        """ sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of the square

        :return: The string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

