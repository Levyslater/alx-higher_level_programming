#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./<script_name>.py <username> <password> <database> <search_string>")
        sys.exit(1)

    username, password, database, search_string = (sys.argv[1],
            sys.argv[2], sys.argv[3], sys.argv[4])

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    try:
        _data = session.query(State).filter(State.name.
                like(f'%{search_string}%')).all()

        if _data:
            print(_data[0].id)
        else:
            print('Not found')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

