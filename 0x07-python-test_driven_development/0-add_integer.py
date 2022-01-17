#!/usr/bin/python3


"""Contains the add function which adds to integers or floats"""


def add_integer(a, b=98):
    """Adds two integers or floats together;if no second int:98"""
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
