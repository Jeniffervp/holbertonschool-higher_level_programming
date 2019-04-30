#!/usr/bin/python3
for x in range(0, 9):
    for y in range(1, 10):
        if x == 8 and y == 9:
            print("{:d}{:d}".format(x, y), end="\n")
        elif x < y:
            print("{:d}{:d}".format(x, y), end=", ")
