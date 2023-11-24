#!/usr/bin/python3
""" This module conatins a function that writes to a text file"""


def write_file(filename="", text=""):
    """ This function writes a file and tells the number
    of characters added"""
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)
        f.read()
        return f.tell()
