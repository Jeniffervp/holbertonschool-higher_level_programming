#!/usr/bin/python3
""" script to fech an url status """
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        headers = resp.info()
        print("{}".format(headers.get("X-Request-Id")))
