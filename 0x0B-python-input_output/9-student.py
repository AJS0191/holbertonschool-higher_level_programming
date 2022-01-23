#!/usr/bin/python3
"""this module contains the class Student"""


class Student:
    """this is the student class it contains names and ages of students"""
    def __init__(self, first_name, last_name, age):
        """this initializes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
