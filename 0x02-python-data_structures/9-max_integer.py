#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        x = len(my_list) - 1
        return sorted(my_list)[x]
    else:
        return None

    
