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
    new_state = State(name="California", cities=[City(name="San Francisco")])
    session_1.add(new_state)
    session_1.commit()
    session_1.close()
