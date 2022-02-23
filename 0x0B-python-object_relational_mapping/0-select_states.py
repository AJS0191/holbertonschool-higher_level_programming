#!/usr/bin/python3
"""This script will return states names and their ids"""
import MySQLdb
import sys


def state_id_name():
    """lists states names and ids """
    args = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close
    db.close


if __name__ == "__main__":
    state_id_name()
