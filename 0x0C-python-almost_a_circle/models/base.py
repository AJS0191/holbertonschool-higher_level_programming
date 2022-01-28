#!/usr/bin/python3
"""this module contains the base class for following files"""


class Base:
    """this class will be the base of all others"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
