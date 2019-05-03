#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for x in range(len(list)):
        if not list[x].startswith("__"):
            print(list[x])
