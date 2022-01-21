#!/usr/bin/python3
""" this module contains the write_file function"""


def write_file(filename="", text=""):
    """opens a file or creates it and writes specified text to it"""
    with open(filename, 'w', encoding="utf-8") as fileA:
        return fileA.write(text)
