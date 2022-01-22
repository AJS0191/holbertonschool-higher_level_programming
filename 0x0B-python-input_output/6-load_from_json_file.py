#!/usr/bin/python
"""this module will contain the function load_from_json"""


import json


def load_from_json_file(filename):
    """loads an object from a json type file"""
    with open(filename, 'r', encoding="utf-8") as fileA:
        return json.load(fileA)
