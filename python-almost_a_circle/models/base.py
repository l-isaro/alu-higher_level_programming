#!/usr/python3
""" This module contains the class base """


class Base:
    """ a base class for all the other classes in this project
        parameters:
        id(int)"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
