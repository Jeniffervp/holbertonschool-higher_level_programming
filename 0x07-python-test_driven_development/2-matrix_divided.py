#!/usr/bin/python3
""" matrix_divided - divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Recieve two parameters matrix and div
    check the matrix and the div for possible errors
    traverse the matrix to divide
    after that append the results to new matrix
    and finally return the new matrix
    """
    error_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    temp = []
    if type(matrix) != list:
        raise TypeError(error_matrix)
    length = len(matrix[0])
    for x in matrix:
        if type(x) != list or not len(matrix):
            raise TypeError(error_matrix)
        if len(x) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if type(y) != int and type(y) != float:
                raise TypeError(error_matrix)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for x in matrix:
        temp = list(map(lambda a: round(a / div, 2), x))
        new_matrix.append(temp)
    return new_matrix
