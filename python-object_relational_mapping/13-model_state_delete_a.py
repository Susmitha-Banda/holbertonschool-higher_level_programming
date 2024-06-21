#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa.
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

    a = session.query(State).where(State.name.like('%a%')).all()

    for row in a:
        session.delete(row)

    session.commit()
