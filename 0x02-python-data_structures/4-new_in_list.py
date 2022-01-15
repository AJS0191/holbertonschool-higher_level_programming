#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    if idx > len(my_list) - 1:
        return list_copy
    if idx < 0:
        return list_copy
    else:
        list_copy.pop(idx)
        list_copy.insert(idx, element)
        return list_copy
