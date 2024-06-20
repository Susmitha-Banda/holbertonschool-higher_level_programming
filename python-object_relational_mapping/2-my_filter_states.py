#!/usr/bin/python3
"""script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys


# this function will be called when the script is executed
def main():
    # get the command line args
    mysql_username = sys.argv[1]   # mysql username
    mysql_password = sys.argv[2]   # mysql password
    db_name = sys.argv[3]          # database name
    state_name = sys.argv[4]       # state name to search for

    # connect to the mysql database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # create a cursor object to interact witht he database
    cursor = db.cursor()
    # create the sql query
    query = (
        "SELECT * FROM states WHERE name = '{0}' "
        "ORDER BY id ASC".format(state_name)
    )
    # execute the query
    cursor.execute(query)
    # fetch all the rows from the executed query
    rows = cursor.fetchall()
    # loop through the rows and  print each one
    for row in rows:
        print(row)
    # close the cursor and db connection
    cursor.close()
    db.close()


# ensure the main function is call when the script is executed
if __name__ == "__main__":
    main()
