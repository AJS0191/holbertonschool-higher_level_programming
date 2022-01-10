#!/usr/bin/python3


def uniq_add(my_list=[]):
    uSum = 0
    for i in range(0, (len(my_list))):
        if i == len(my_list) - 1:
            if sorted(my_list)[i] != sorted(my_list)[i - 1]:
                uSum = uSum + sorted(my_list)[i]
            else:
                break
        elif sorted(my_list)[i] != sorted(my_list)[i + 1]:
            uSum = uSum + sorted(my_list)[i]
        else:
            i + 1
    return uSum
