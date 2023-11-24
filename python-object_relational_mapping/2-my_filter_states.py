#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], db=sys.argv[4])

# Creating cursor object
    cur = db.cursor()

# Executing MySql Query
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY id ASC".format(sys.argv[4]))

# Query Result & prints the result in rows
for row in cur.fetchall():
    if row[1][0] == 'N':
        print(row)

# Clean Up
db.close()
cur.close()
