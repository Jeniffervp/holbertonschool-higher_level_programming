#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as myfile:
        cont_line = 0
        while nb_lines <= 0 or nb_lines > cont_line:
            line = myfile.readline()
            if not line:
                break
                cont_line += 1
                print(line, end='')
