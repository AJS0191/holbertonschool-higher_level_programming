#!/usr/bin/python3
"""this module contains the trom_json_string function"""


import json


def from_json_string(my_str):
    """returns an object from a json encoded string"""
    return json.loads(my_str)
