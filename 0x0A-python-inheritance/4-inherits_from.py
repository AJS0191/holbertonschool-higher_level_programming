#!/usr/bin/python3
"""this module contains the inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if obj's class was inherited from a_class"""
    while obj is not type(obj):
        if a_class in type(obj).__bases__:
            return True
        obj = type(obj)
    return False
