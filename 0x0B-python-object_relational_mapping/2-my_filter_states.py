#!/usr/bin/python3
"""This script will return states names and their ids"""
import MySQLdb
import sys


def main():
    """lists specified states id and name"""
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", [format(args[4])])
    rows = cur.fetchall()
    for row in rows:
        if row[1] == args[4]:
            print(row)
    cur.close
    db.close

if __name__ == "__main__":
    main()
