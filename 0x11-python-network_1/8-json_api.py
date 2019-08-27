#!/usr/bin/python3
""" script to find the id and name inside a json file with one paremeter """
from sys import argv
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    q = ""

    if len(argv) > 1:
        q = argv[1]
    param = {'q': q}

    request = requests.post(url, param)

    try:
        file_j = request.json()
    except:
        print("Not a valid JSON")

    else:
        if file_j:
            print("[{}] {}".format(file_j.get('id'), file_j.get('name')))
        else:
            print("No result")
