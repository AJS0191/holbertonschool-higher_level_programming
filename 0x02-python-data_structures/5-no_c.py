#!/usr/bin/python


def no_c(my_string):
    if my_string.count('c') == 0 and my_string.count('C') == 0:
        return my_string

    else:
        new_string = ""
        for i in range(my_string.count('c')):
            for i in range(0, len(my_string)):
                if my_string[i] != 'c' and my_string[i] != 'C':
                    new_string = new_string + my_string[i]
    return new_string
