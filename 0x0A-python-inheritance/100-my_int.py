#!/usr/bin/python3
class MyInt(int):

    def __init__(self, value):
        self.value = value
        int.__init__(self)

    def __eq__(self, n):
        return self.value != n

    def __ne__(self, n):
        return not self == n
