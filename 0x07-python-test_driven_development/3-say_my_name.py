#!/usr/bin/python3
""" say_my_name - prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """
    Recieve two variales "fist_name" and "last_name"
    first condition to check if first_name is not a string
    second condition to check if last_name is not a string
    and the last print My name is <first_name> <last_name>
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
