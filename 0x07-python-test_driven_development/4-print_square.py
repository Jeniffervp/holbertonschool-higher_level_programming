#!/usr/bin/python3
""" print_square - print a square with the character # """


def print_square(size):
    """
    Recieve parameter size as length
    first evaluate if type is not integer
    second evaluate if size is less than 0
    Finally: make the square with the size given
    print the square.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for i in range(size):
                print('#', end="")
            print()
