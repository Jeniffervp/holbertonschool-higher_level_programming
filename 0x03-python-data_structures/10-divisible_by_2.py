#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list2 = []
    for a in my_list:
        my_list2.append(a % 2 == 0)
    return my_list2
