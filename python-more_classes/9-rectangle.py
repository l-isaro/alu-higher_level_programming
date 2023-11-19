#!/usr/bin/python3
""" This module contains the class rectangle that 
has height and width
"""


class Rectangle:
    """ a class to represent a rectangle

    Attributes:
    width
    height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        '''method: __str__
        return: nice string representation of rectangle
        '''
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(width=self.__size, self.__height=size)
