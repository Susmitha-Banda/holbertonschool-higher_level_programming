#!/usr/bin/python3
"""Lists all the objects in the State table with name that contain 'a'
within the hbtn_0e_6_usa database using SQLalchemy.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all the state names with 'a'
    a = session.query(State).where(State.name.like('%a%')).all()

    for row in a:
        print("{}: {}".format(row.id, row.name))
