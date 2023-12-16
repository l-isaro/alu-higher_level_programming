#!/usr/bin/python3
""" This module contains the class base """
import json


class Base:
    """ a base class for all the other classes in this project
        parameters:
        id(int)"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ changes the list of dictionaries into a json string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
