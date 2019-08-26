#!/usr/bin/python3
""" script to post an email """
from sys import argv
from urllib import request, parse

if __name__ == "__main__":

    url_1 = argv[1]

    post_email = {'email': argv[2]}

    email = parse.urlencode(post_email)
    email = email.encode('utf-8')

    ask = request.Request(url_1, email)

    with request.urlopen(ask) as resp:
        email_ask = resp.read()
        print(email_ask.decode('utf-8'))
