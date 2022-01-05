#!/usr/bin/python3

def pow(a, b):
    result = a
    if b > 1:
        for i in range(0, b - 1):
            result = result * a
        return result
    elif b == 0:
        return 1
    else:
        for j in range(0, -b - 1):
            result = result * a
        result = 1 / result
        return result
