#!/usr/bin/python3
""" lists all cities and his states """
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
    round1 = session_1.query(City).order_by(City.id)

    for new in round1:
        print("{}: {} -> {}".format(new.id, new.name, new.state.name))
    session_1.close()
