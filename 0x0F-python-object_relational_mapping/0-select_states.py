#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")
    
    # Create a cursor object
    c = db.cursor()
    
    # Execute the SQL query
    c.execute("SELECT id, name FROM states ORDER BY id ASC")
    
    # Fetch all the rows from the executed query
    rows = c.fetchall()
    
    # Print the fetched rows
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    c.close()
    db.close()
