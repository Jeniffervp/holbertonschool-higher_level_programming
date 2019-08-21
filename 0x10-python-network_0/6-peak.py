#!/usr/bin/python3
""" that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds a peak """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return 0
    return list_of_integers[helper(
        list_of_integers, 0, len(list_of_integers) - 1)]


def helper(list_of_integers, first, last):
    """ function to do the recursive function """

    reach = last - first
    if reach == 1:
        if list_of_integers[first] > list_of_integers[last]:
            return first
        else:
            return last

    middle = first + reach // 2

    if list_of_integers[middle] < list_of_integers[middle + 1]:
        return helper(list_of_integers, middle, last)
    return helper(list_of_integers, first, middle)
