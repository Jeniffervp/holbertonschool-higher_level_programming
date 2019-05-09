#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    val = list(map(lambda a: a * 2, a_dictionary.values()))
    key = a_dictionary.keys()
    return dict(zip(key, val))
