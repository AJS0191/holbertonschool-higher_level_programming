#!/usr/bin/python3
"""This script will return states names and their ids"""
import MySQLdb
import sys


def main():
    """lists cities names in given state"""
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities JOIN states\
                 ON cities.state_id = states.id")
    rows = cur.fetchall()
    city_list = []
    for row in rows:
            if row[1] == args[4]:
                city_list.append(row[0])
    i = 0
    if len(city_list) > 1:
        for i in range(0, len(city_list) - 1):
            print("{}".format(city_list[i]), end=", ")
    i += 1
    print(city_list[i])
    cur.close
    db.close

if __name__ == "__main__":
    main()
