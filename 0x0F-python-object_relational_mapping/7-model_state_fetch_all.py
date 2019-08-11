#!/usr/bin/python3
"""  lists all State objects from the database hbtn_0e_6_usa """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    sta = start()
    selec = sta.query(State).order_by(asc(State.id)).all()

    for x in selec:
        print("{}: {}".format(x.id, x.name))

    sta.close()
