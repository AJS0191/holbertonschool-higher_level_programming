#!/usr/bin/python
"""this module will contain the function load_from_json"""


import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as fileA:
        return json.load(fileA)
