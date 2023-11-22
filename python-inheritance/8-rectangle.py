#!/usr/bin/python3
"""Module to create a class called BaseGeometry"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
