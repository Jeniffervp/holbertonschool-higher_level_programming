#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as myfile:
        cont_line = 0
        while True:
            line = myfile.readline()
            if not line:
                break
            cont_line += 1
        return cont_line
