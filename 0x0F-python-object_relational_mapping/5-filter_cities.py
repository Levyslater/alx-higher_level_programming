#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_0_usa.
Results must be sorted in ascending order by cities.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
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
    
    # Execute the SQL query with JOIN to get city id, city name, and state name
    query = """
    SELECT cities.id, cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    c.execute(query, (state_name,))
    
    # Fetch all the rows from the executed query
    rows = c.fetchall()
    
    # Print the fetched rows
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    c.close()
    db.close()

