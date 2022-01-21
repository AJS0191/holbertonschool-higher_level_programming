#!/usr/bin/python3
"""this module contains the square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """the square class has an area method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size__ = size
        self.__width__ = size
        self.__height__ = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__width__, self.__height__)
