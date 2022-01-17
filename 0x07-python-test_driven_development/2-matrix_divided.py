#!/usr/bin/python3


"""Contains a function that divides a matrix"""


def matrix_divided(matrix, div):
    """divides a matrix by a given number"""
    for i in range(0, len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
        for k in range(0, len(matrix[i])):
            temp = matrix[i]
            if type(temp[k]) is not int and type(temp[k]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(0, len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(div) is float:
        div = int(div)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newM = []
    for i in range(0, len(matrix)):
        matrixList = list(map(lambda x: round(x/div, 2), matrix[i]))
        newM.append(matrixList)
    return newM
