#!/usr/bin/python3
""" this module contains the write_file function"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as fileA:
        return fileA.write(text)
