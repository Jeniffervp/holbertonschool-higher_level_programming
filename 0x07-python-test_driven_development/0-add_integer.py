#!/usr/bin/python3
""" add_integer - function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Recieve two marameters a and b
    The first conditional evaluate if "a" is not a integer or a float
    The second conditional evaluate if "b" is not a integer or a float
    And the last return the sum of "a" and "b" cast to integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
