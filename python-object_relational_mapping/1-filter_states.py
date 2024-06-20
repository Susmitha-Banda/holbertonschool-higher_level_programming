#!/usr/bin/python3
"""
Lists all states with name starting with 'N' from the hbtn_0e_0_usa database
"""

import MySQLdb
import sys


# function to connect to mysql and fetch states starting with 'N'
def fetch_states_starting_with_N(username, password, database):
    # connect to MySQL
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)

    # create a cursor object
    cursor = db.cursor()

    # define the SQL query with a WHERE
    # clause to filter states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    # execute the query
    cursor.execute(query)

    # fetch all rows
    states = cursor.fetchall()

    # print results in the required format
    for state in states:
        print(state)

    # close cursor and connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python 1-filter_states.py"
              "<username>"
              "<password>"
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function to fetch and display states starting with 'N'
    fetch_states_starting_with_N(username, password, database)
