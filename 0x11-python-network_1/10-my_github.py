#!/usr/bin/python3
""" scrip to authenticate and get the id of an user """
from sys import argv
import requests

if __name__ == "__main__":

    page = 'https://api.github.com/user'
    my_user = argv[1]
    my_psswd = argv[2]
    request = requests.get(page, auth=(my_user, my_psswd))
    search = request.json()
    print("{}".format(search.get('id')))
