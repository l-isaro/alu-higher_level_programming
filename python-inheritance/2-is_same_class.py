#!/usr/bin/python3
""" This module contains the function is_Same_class()"""

def is_same_class(obj, a_class):

    """checks if object is an instance of class provided"""

    if type(obj) == type(a_class):
        return True
    else:
        return False
