#!/usr/bin/python3
""" this module contains the method is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """returns true when object is an instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
