#!/usr/bin/python3
""" lists all State objects that contain the letter a """
from sys import argv
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc, update
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    sta = start()
    for new, new2 in sta.query(State, City).join(
            City).order_by(asc(City.id)).all():
        print("{}: ({}) {}".format(new.name, new2.id, new2.name))
    sta.close()
