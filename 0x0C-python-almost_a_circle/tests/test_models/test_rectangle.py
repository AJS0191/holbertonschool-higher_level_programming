#!/usr/bin/python3
"""this module contains the rectangle class"""


Base = __import__('models.base').base.Base


class Rectangle(Base):
    """Rectangle class defines a shape with positional arguments x,
    and y, as well as with a width and a height"""

    def int_validator(self, name, value):
        """validates values are integers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def des_validator(self, name, value):
        """validates that values are greater than 0"""
        if value < 1:
            raise ValueError("{} must be > 0".format(name))

    def pos_validator(self, name, value):
        """validate that positional values are greater than or equal to zero"""
        if not value >= 0:
            raise ValueError("{} must be >= 0".format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes an instance of the rectangle class
        it builds upon the Base class, it adds positional arguments
        as well as value arguments"""
        super().__init__(id)
        self.int_validator("width", width)
        self.des_validator("width", width)
        self.__width = width
        self.int_validator("height", height)
        self.des_validator("height", height)
        self.__height = height
        self.int_validator("x", x)
        self.pos_validator("x", x)
        self.__x = x
        self.int_validator("y", y)
        self.pos_validator("y", y)
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.des_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.des_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validator("x", value)
        self.pos_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validator("y", value)
        self.pos_validator("y", value)
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """displays the rectangle with'#' charaters, now taking
        into account positional arguments"""
        for a in range(self.__y):
            print('')
        for i in range(self.__height):
            for b in range(self.__x):
                print(' ', end="")
            for k in range(self.__width):
                print("#", end='')
            print('')

    def __str__(self):
        """the str value of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """updates self with new arguments with a no-keyword argument,
        the order being id, width, height, x, y"""
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.int_validator("width", args[1])
            self.des_validator("width", args[1])
            self.__width = args[1]
        if len(args) == 3:
            self.int_validator("height", args[2])
            self.des_validator("height", args[2])
            self.__height = args[2]
        if len(args) == 4:
            self.int_validator("x", args[3])
            self.pos_validator("x", args[3])
            self.__x = args[3]
        if len(args) == 5:
            self.int_validator("y", args[4])
            self.pos_validator("y", args[4])
            self.__y = args[4]
