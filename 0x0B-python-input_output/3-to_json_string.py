#!/usr/bin/python3
"""this module holds the to_json_string function"""


import json


def to_json_string(my_obj):
    """ this function returns a json representation of my_obj"""
    return json.dumps(my_obj)
