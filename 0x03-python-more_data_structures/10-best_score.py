#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        temp = []
        for x, y in a_dictionary.items():
            temp.append(y)
        i = 0
        for x, y in a_dictionary.items():
            if y == sorted(temp)[-1]:
                return x
    else:
        return None
