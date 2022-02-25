#!/usr/bin/python3
"""This module lists values in states where name = sys.argv[4]."""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
    passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE %s ORDER BY states.id ASC""", [format(sys.argv[4])])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
