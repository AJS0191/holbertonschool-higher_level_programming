#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newL = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            newL.insert(i, replace)
        else:
            newL.insert(i, my_list[i])
    return newL
