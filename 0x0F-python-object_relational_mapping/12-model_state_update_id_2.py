#!/usr/bin/python3
""" lists all State objects that contain the letter a """
from sys import argv
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
    selec = sta.query(State).filter_by(id=2)
    for new in selec:
        new.name = 'New Mexico'
    sta.commit()
    sta.close()
