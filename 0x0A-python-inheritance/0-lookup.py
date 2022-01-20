#!/usr/bin/python3
"""this module contains the lookup function"""


def lookup(obj):
    """returns a list of available attributes and methods"""
    return str(dir(obj))
