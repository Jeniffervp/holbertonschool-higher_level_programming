#!/usr/bin/python3
""" lists all State objects that contain the letter a """
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    sta = start()
    a_state = State(name="Louisiana")
    sta.add(a_state)
    sta.commit()
    selec = sta.query(State).filter_by(
        name="Louisiana").first()

    if selec:
        print("{}".format(selec.id))
    else:
        print("Not found")

    sta.close()
