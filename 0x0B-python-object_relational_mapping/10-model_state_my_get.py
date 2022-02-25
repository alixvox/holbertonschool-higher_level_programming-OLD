#!/usr/bin/python3
""" Prints first state object from database hbtn_0e_6_usa """

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

    arg = [format(sys.argv[4])]

    record = session.query(State).filter(State.name.contains(arg))\
                                 .order_by(State.id).all()
    if (record):
        for el in record:
            print("{}".format(el.id))
    else:
        print("Not found")
    session.close()
