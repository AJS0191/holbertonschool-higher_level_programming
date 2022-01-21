#!/usr/bin/python3
"""this module contains the read_file function"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as fileA:
        print(fileA.read())
