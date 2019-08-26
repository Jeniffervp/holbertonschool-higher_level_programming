#!/usr/bin/python3
""" script to post an email """
from sys import argv
import requests

if __name__ == "__main__":

    url_1 = argv[1]

    post_email = {'email': argv[2]}

    email = requests.post(url_1, post_email)

    print(email.text)
