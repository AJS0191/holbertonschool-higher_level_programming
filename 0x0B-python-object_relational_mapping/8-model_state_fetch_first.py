#!/usr/bin/python3
""" This module prints the names and id of states """


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
    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{}: {}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()
