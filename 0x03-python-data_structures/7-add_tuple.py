#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tup_val(tuple_a)
    y = tup_val(tuple_b)
    return ((x[0] + y[0], x[1] + y[1]))


def tup_val(tup=()):
    leng = len(tup)
    if leng <= 0:
        return ((0, 0))
    elif leng == 1:
        tup = list(tup)
        tup.append(0)
        tup = tuple(tup)
    return tup
