#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Setting up connection to the database
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creates an Engine, which is how SQLAlchemy communicates with the database
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying
    query = session.query(State).filter(State.name.like("%a%")).all()

    # Printing
    for state in query:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
