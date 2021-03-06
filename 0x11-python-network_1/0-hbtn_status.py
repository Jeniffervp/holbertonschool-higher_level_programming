#!/usr/bin/python3
""" script to fech an url status """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        result = resp.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
              format(type(result), result, result.decode('utf-8')))
