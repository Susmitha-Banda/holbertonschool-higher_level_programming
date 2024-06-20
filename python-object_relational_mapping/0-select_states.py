#!/usr/bin/python3
""" Lists all states from the hbtn_0e_0_usa database"""

import MySQLdb
import sys

#function to connect to mysql and fetch states
def fetch_states(username, password, database):
    #connect to sql
    db = MySQLdb.connect(host='localhost',
                        user=username,
                        passwd=password,
                        db=database,
                        port=3306)
    #create a cursor object
    cursor = db.cursor()
    #define the sql query
    query = "SELECT * FROM states ORDER BY states.id ASC"
    #execute the query
    cursor.execute(query)
    #fetch all rows
    states = cursor.fetchall()
    #print results in the required format
    for state in states:
        print(state)
    #close cursor and connection
    cursor.close()
    db.close()

if __name__ == '__main__':    #This line checks if the script is being run directly by the Python interpreter.
# When a Python file is executed directly (not imported as a module), the special variable __name__ is set to '__main__'
    if len(sys.argv) != 4:
        print("Usage: python 0-select_states.py <username> <password> <database>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    #call function to fetch and display states
    fetch_states(username, password, database)
