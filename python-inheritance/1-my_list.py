#!/usr/bin/python3
"""
This module contains the class my_list
"""


class Mylist(list):
    """ the class inherits from list and sorts the list"""

    def print_sorted(self):
        """ Returns a sorted list(ascending)"""
        print(sorted(self))
