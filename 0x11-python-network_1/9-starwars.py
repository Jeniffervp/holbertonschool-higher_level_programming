#!/usr/bin/python3
""" script to find the id and name inside a json file with one paremeter """
from sys import argv
import requests

if __name__ == "__main__":

    page = 'https://swapi.co/api/people'
    request = requests.post(page, params={'search': argv[1]})
    search = request.json()
    counting = search.get('count')
    print("Number of results: {}".format(counting))

    for response in search.get('results'):
        print(response.get('name'))
