#!/usr/bin/python3
""" adds Lousiana to the state table """


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ This will print the instance.id and instance.name in table state """
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="Louisiana")
    session.add(newState)
    addedState = session.query(State).filter_by(name='Louisiana').first()
    print(addedState.id)
    session.commit()
    session.close()
