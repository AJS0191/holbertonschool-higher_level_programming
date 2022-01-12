#!/usr/bin/python3


def roman_to_int(roman_string):
    romanN = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    thisN = list(map(lambda x: romanN.get(x), roman_string))
    sumR = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(thisN) == 1:
        return thisN[0]
    for i in range(0, len(thisN)):
        if i != 0:
            if thisN[i] > thisN[i - 1]:
                sumR = ((thisN[i]) - (thisN[i - 1] * 2)) + sumR
            else:
                sumR = thisN[i] + sumR
        else:
            sumR = thisN[i] + sumR
    return sumR
