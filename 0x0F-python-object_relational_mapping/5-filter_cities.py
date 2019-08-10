#!/usr/bin/python3
""" list all the states from a data base that match name with argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn_table = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3])

    poin = conn_table.cursor()
    poin.execute("SELECT cities.name FROM cities \
    WHERE cities.state_id = (SELECT states.id FROM states \
    WHERE states.name = %s) ORDER BY cities.id ASC;",(argv[4],))

    to_print_1 = []

    for to_print in poin:
        to_print_1 += to_print
    print(", ".join(to_print_1))

    poin.close()
