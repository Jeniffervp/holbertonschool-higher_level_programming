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
    poin.execute("SELECT id, name FROM states \
    WHERE name LIKE %s ORDER BY id ASC", (argv[4],))

    for order_to_print in poin:
        print(order_to_print)

    poin.close()
