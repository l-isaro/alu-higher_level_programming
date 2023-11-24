#!/usr/bin/python3                                                                                                                                   
""" This module conatins a function that writes to a text file"""


def append_write(filename="", text=""):
    """ This function appends to a file and tells the number 
    of characters added"""
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
