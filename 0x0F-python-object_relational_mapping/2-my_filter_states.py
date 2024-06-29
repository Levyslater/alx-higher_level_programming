#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)
    
    # Get MySQL credentials and state name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    
    # Create a cursor object
    c = db.cursor()
    
    # Execute the SQL query to find states with the matching name
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(query, (state_name,))
    
    # Fetch all the rows from the executed query
    rows = c.fetchall()
    
    # Print the fetched rows
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    c.close()
    db.close()
