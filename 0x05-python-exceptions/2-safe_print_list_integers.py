#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end='')
            cont += 1
        except (TypeError, ValueError):
            continue
    print("")
    return cont
