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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ changes the list of dictionaries into a json string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    def save_to_file(cls, list_objs):
        """ writes json representation to a file """
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as file:
            file.write(cls.to_json_string(list_objs))
