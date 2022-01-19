#!/usr/bin/python3
"""contains the whole of the rectangle class"""


class Rectangle:
    """class that represents rectangles, and contains info and methods
    string representation present"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)

    def __str__(self):
        strR = ""
        if self.width != 0 and self.height != 0:
            for i in range(0, self.__height):
                for k in range(0, self.__width):
                    strR = strR + "#"
                if i != self.height - 1:
                    strR = strR + "\n"
        return strR

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
    