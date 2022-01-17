#!/usr/bin/python3


"""Contains the print square fucntion"""
def print_square(size):
    """Prints a square with the '#' character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    for i in range(0, size):
        for k in range(0, size):
            print("#", end="")
        print("")
    