import os
from app.amity import my_amity
from app.amity.amityClass import rooms
from app.person.personClass import people_data
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database(object):
    """ Database class"""

    def __init__(self):
        self.db = None
        self.amity = my_amity

    def save_state(self, args):
        """
        Takes up an optional argument --db that specifies the
        database to store the data in rooms and people dictionary.
        Creates database and saves data.
        """
        # print args
        if args["--db"]:
            self.db_name = args["--db"]
        else:
            self.db_name = "amity.db"

        # Check if the database already exists, if it does delete existing.

        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        self.db = create_engine("sqlite:///" + self.db_name)

        try:
            session = sessionmaker()
            session.configure(bind=self.db)
            Base.metadata.create_all(self.db)

            storage_session = session()
            storage_session.add(self.save_people())
            storage_session.add(self.save_rooms())

            message = "Data has been stored in the " + self.db_name + " database"

        except:
            message = "Error saving data to " + self.db_name

        storage_session.commit()
        storage_session.close()

        print message
        return message

    def save_people(self):
        """
        Loads data from the people_data dict into the database
        """
        for role in people_data.keys():
            for identifier in people_data[role].keys():
                person_id = identifier
                name = people_data[role][identifier]['name']
                wants_accomodation = people_data[
                    role][identifier]['accomodation']
                if role is 'Staff':
                    is_staff = True
                    is_fellow = False
                elif role is 'Fellow':
                    is_staff = False
                    is_fellow = True

        people = People(person_id=person_id, name=name,
                        wants_accomodation=wants_accomodation,
                        is_staff=is_staff, is_fellow=is_fellow)
        return people

    def save_rooms(self):
        """
        Loads data from the rooms dict into the database
        """
        for room_type in rooms.keys():
            for room in rooms[room_type].keys():
                room_name = room
                room_type = room_type
        room_data = Rooms(room_name=room_name, room_type=room_type)
        return room_data

    def load_state(self, args):
        """
        Loads data from a database into the application
        """
        print args


class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    room_type = Column(String)


class People(Base):
    __tablename__ = 'people'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    wants_accomodation = Column(Boolean)
    is_staff = Column(Boolean)
    is_fellow = Column(Boolean)


class Allocations(Base):
    __tablename__ = 'allocations'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    occupant_id = Column(Integer, ForeignKey('people.person_id'))

    occupants = relationship(People)
    room = relationship(Rooms)
