#!/usr/bin/python3
""" script to fech an url status """
import requests

if __name__ == "__main__":
    result = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".
          format(type(result.text), result.text))
