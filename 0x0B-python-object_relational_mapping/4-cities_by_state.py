#!/usr/bin/python3
"""This script will return states names and their ids"""
import MySQLdb
import sys


def main():
    """lists states names and ids """
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
            print(row)
    cur.close
    db.close

if __name__ == "__main__":
    main()
