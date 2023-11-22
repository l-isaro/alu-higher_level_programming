#!/usr/bin/python3
""" This module contains the class BaseGeometry """


class BaseGeometry:
    """ This class contains the method area"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
