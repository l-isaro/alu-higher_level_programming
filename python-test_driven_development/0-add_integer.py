#!/usr/bin/python3
""" This module contains the function add """


def add_integer(a, b=98):
    """ Given two integers return the  sum

        :param a: int
        :param b: int
        :return: int
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")

    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
