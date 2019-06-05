#!/usr/bin/python3
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

list_j = []

try:
    my_load = load_from_json_file("add_item.json")
    for a in my_load:
        list_j.append(a)

except:
    pass

for a in range(len(argv)):
    if a != 0:
        list_j.append(argv[a])

save_to_json_file(list_j, "add_item.json")
