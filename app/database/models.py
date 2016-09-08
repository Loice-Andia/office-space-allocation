from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    room_type = Column(String)


class People(Base):
    __tablename__ = 'people'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    wants_accomodation = Column(String)
    is_staff = Column(Boolean)
    is_fellow = Column(Boolean)


class Allocations(Base):
    __tablename__ = 'allocations'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    occupant_id = Column(Integer)

    # occupants = relationship(People)
    # room = relationship(Rooms)
