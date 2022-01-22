#!/usr/bin/python3
"""this module will contain the function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """saves an object into a json type file"""
    with open(filename, 'w', encoding="utf-8",) as fileA:
        json.dump(my_obj, fileA, ensure_ascii=False)
