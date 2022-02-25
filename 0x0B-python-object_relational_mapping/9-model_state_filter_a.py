#!/usr/bin/python3
"""Prints first state object from database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for record in session.query(State).filter(State.name.contains('a'))\
                                      .order_by(State.id):
        print("{}: {}".format(record.id, record.name))
    session.close()
