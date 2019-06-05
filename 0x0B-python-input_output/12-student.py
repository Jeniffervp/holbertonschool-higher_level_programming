#!/usr/bin/python3
class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dicto = {}
            for key1, value in self.__dict__.items():
                for key2 in attrs:
                    if key2 == key1:
                        dicto.update({key1: value})
            return dicto
        else:
            return self.__dict__
