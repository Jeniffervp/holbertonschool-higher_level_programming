#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF8") as myfile:
        for line in myfile:
            print(line, end='')
