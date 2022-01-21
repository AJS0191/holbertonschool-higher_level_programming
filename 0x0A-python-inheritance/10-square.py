#!/busr/bin/python3
"""this module contains the square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size__ = size
        self.__width__ = size
        self.__height__ = size

    def area(self):
        return self.__size__ * self.__size__
