#!/usr/bin/python3
""" lists all State objects that contain the letter a """
from sys import argv
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    start = sessionmaker()
    start.configure(bind=engine)
    session_1 = start()
    round1 = session_1.query(State).order_by(State.id)

    for new in round1:
        print("{}: {}".format(new.id, new.name))
        for new2 in new.cities:
            print("\t{}: {}".format(new2.id, new2.name))
    session_1.close()
