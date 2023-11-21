#!/usr/bin/python3
""" this module contains the method inherits_from()"""


def inherits_from(obj, a_class):
    """ returns true if the object is an instance of a class 
        that inherits from the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
