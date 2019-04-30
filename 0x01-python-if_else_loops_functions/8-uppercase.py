#!/usr/bin/python3
def uppercase(str):
    a = 0
    while a < len(str):
        if str[a].islower():
            b = ord(str[a]) - 32
        else:
            b = ord(str[a])
        if a != len(str):
            print("{:s}".format(chr(b)), end="")
        a += 1
    print("")
