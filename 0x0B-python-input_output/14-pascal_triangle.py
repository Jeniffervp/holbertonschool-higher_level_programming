#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    listo = [[1], [1, 1]]
    for i in range(1, n - 1):
        base = [1]
        for j in range(0, len(listo[i]) - 1):
            base.extend([listo[i][j] + listo[i][j + 1]])
        listo.append(base)
        base += [1]
    return listo
