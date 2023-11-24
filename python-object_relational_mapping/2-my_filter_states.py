#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Function that lists all states from database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], db=sys.argv[4])

# Creating cursor object
    cur = db.cursor()

    # Executing MySql Query
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                 ORDER BY id".format(search))

    # Obtaining Query Result & prints the result in rows
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    # Clean Up
    cur.close()
    db.close()
