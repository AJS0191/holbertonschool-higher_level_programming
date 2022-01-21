#!/usr/bin/python3
"""this module contains the geometry class"""


class BaseGeometry:
    """the BaseGeometry class has the area and the integer_validator methods"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise \
                ValueError("{} must be greater than 0".format(name))
