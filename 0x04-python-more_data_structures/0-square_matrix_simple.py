#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    temp = []
    for a in matrix:
        for b in a:
            temp = list(map(lambda b: b * b, a))
        matrix2.append(temp)
    return matrix2
