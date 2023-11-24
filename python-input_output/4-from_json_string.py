#!/usr/bin/python3
""" This module contains a function to_json_string"""


import json


def from_json_string(my_str):
    """ This function returns the JSON representation
    of an object """
    return json.load(my_str)
