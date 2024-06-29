#!/usr/bin/python3
"""Script adds a new city and prints its id"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./<script_name>.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:
            {password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Add a new state 'Louisiana'
        add_state = State(name='Louisiana')
        session.add(add_state)
        session.commit()

        # Query the newly added state
        new_state = session.query(State).filter_by(name='Louisiana').first()
        if new_state:
            print(new_state.id)
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

