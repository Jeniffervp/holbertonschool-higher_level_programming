#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
    if alpha % 2 != 0:
        alpha = alpha - 32
    else:
        alpha = alpha
    print("{:s}".format(chr(alpha)), end="")
