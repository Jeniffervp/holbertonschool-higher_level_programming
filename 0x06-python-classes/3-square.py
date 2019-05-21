#!/usr/bin/python3
class Square:
    def __init__(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        self.area = self.__size * self.__size
        return self.area
