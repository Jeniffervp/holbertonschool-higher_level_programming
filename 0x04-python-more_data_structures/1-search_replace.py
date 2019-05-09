#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_2 = []
    for a in my_list:
        if a == search:
            list_2.append(replace)
        else:
            list_2.append(a)
    return list_2
