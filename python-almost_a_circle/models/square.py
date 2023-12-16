#!/usr/bin/python3
""" This module contains the class Square """

from models.rectangle import Rectangle


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
        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of size"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of the square

        :return: The string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ updates the attributes of the class"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """ returns a dictionary representation of rectangle"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
