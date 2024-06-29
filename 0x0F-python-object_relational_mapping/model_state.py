#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of the Base class from declarative_base
Base = declarative_base()

# Define the State class that inherits from Base
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

# Function to create an engine and connect to the database
def connect_to_db(username, password, database):
    # Create an engine that connects to the MySQL server on localhost at port 3306
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    return engine

# Main execution
if __name__ == "__main__":
    import sys

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    engine = connect_to_db(mysql_username, mysql_password, database_name)

    # Create all tables in the database
    Base.metadata.create_all(engine)

