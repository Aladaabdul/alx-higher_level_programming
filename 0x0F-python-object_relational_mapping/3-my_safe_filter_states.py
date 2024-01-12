#!/usr/bin/python3
"""a script that takes in an argument and displays all values"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )

    state = sys.argv[4]
    cur = db.cursor()

    cur.execute(
            "SELECT * FROM states " +
            "WHERE name LIKE %s", (state, )
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
