#!/usr/bin/python3
""" list all the states from a data base starting with N"""
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
    order_to_print = "SELECT id, name FROM states \
    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    poin.execute(order_to_print)

    for order_to_print in poin:
        print(order_to_print)

    poin.close()
