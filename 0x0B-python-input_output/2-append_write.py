#!/usr/bin/python3
"""this module contains the function append_write"""


def append_write(filename="", text=""):
    """this function opens and appends a file"""
    with open(filename, 'a', encoding="utf-8") as fileA:
        return fileA.write(text)
