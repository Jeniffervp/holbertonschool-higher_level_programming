#!/usr/bin/python3
def add_attribute(obj, name, value):
    if isinstance(obj, (str, int, float, list, tuple, dict, bool, complex)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
