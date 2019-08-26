#!/usr/bin/python3
""" handle error code """
from sys import argv
from urllib import request, parse, error

if __name__ == "__main__":

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as resp:
            no_err = resp.read()
            print(no_err.decode('utf-8'))

    except error.HTTPError as err:
        print("Error code: ", err.code)
