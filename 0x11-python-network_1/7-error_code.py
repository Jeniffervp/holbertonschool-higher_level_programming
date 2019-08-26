#!/usr/bin/python3
""" script to fech an url status """
from sys import argv
import requests

if __name__ == "__main__":

    req = requests.get(argv[1])

    stat = req.status_code

    if stat >= 400:
        print("Error code: {}".format(stat))

    else:
        print(req.text)
