#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from SQL injection"""

import MySQLdb
import sys

if __name__ == "__main__":
    # ensure the correct number of command line args are provided
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    # get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # connect to mysql database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )

        print("Connected to MySQL successfully")

        # create a cursor object to interact with the database
        cursor = db.cursor()

        # create a sql query using a parameterised query to prevent SQL injection
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        
        print("Executing query:", query % state_name)

        # execute the query with the provided state name
        cursor.execute(query, (state_name,))

        # fetch all rows from the executed query
        rows = cursor.fetchall()

        # loop through the rows and print each one
        for row in rows:
            print("({}, '{}')".format(row[0], row[1]))

        # close the cursor and db connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
