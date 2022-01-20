#!/usr/bin/python3
"""contains the my_list class inheriting from list"""


class MyList(list):
    """a child class of list"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        print("{}".format(sorted(self)))
