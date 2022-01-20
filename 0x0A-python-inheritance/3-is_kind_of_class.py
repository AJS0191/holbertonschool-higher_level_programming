#!/usr/bin/python3
"""This module contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    if a_class in type(obj).__bases__ or type(obj) is a_class:
        return True
    return False
