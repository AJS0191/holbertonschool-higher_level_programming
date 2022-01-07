#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        boolList = my_list.copy();
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                boolList[i] = True
            else:
                boolList[i] = False
    return boolList
