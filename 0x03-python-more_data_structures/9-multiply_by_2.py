#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newD = dict.fromkeys(list(a_dictionary))
    for key, value in a_dictionary.items():
        newD[key] = value * 2
    return newD
