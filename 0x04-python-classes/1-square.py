#!/usr/bin/python3


"""Contains a square class more specific than the other."""


class Square:
    """A Square has 4 angles, all 90 degrees"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
