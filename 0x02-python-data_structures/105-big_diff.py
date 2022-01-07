#!/usr/bin/python3


def big_diff(my_list=[]):
    if len(mylist) < 2:
        return 0
    return (sorted(my_list)[-1] - sorted(my_list)[0])
