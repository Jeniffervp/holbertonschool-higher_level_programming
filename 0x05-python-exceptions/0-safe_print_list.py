#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end='')
            cont += 1
        except:
            print("")
            return cont
    print("")
    return cont
