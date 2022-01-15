#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newM = []
    for i in range(0, (len(matrix))):
        listN = list(map(lambda x: x*x, matrix[i]))
        newM.insert(i, listN)
    return newM
