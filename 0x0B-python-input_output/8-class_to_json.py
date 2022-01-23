#!/usr/bin/python3
"""contains the function class to jason"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
