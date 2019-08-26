#!/usr/bin/python3
""" script to get the X-Request-ID in the response header """
import requests
from sys import argv

if __name__ == "__main__":
    head = requests.get(argv[1])
    print("{}".format(head.headers.get("X-Request-Id")))
