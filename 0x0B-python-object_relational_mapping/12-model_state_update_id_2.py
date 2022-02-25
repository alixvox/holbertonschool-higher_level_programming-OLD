#!/usr/bin/python3
"""Prints first state object from database hbtn_0e_6_usa."""

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

    record = session.query(State).filter_by(id=2).first()
    record.name = 'New Mexico'
    session.commit()
    session.close()
