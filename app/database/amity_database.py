import os
from app.amity import my_amity
from app.amity.amityClass import rooms
from app.person.personClass import people_data
from app.rooms import my_room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


class Database(object):
    """ Database class"""

    def __init__(self):
        self.db = None
        self.amity = my_amity

    def connect_to_db(self, db_name):
        """
        Helper function to connect to database
        """
        self.db = create_engine("sqlite:///" + db_name)
        session = sessionmaker()
        session.configure(bind=self.db)
        Base.metadata.create_all(self.db)

        storage_session = session()
        return storage_session

    def save_state(self, args):
        """
        Takes up an optional argument --db that specifies the
        database to store the data in rooms and people dictionary.
        Creates database and saves data.
        """
        # print args
        if args["--db"]:
            self.db_name = args["--db"]
        self.db_name = "amity.db"

        # Check if the database already exists, if it does delete existing.
        # import ipdb
        # ipdb.set_trace()

        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        # self.db = create_engine("sqlite:///" + self.db_name)

        try:
            save_session = self.connect_to_db(self.db_name)
            self.save_people(save_session)
            self.save_rooms(save_session)
            self.save_allocations(save_session)

            message = "Data has been stored in the {} database".format(self.db_name)

        except:
            message = "Error saving data to {}".format(self.db_name)

        save_session.commit()
        save_session.close()

        return message

    def save_people(self, storage_session):
        """
        Loads data from the people_data dict into the database
        """
        try:
            for key, values in people_data.items():
                person_id = key
                name = values["name"]
                wants_accomodation = values["accomodation"]
                is_fellow = values["is_fellow"]

                people = People(person_id=person_id, name=name,
                                wants_accomodation=wants_accomodation,
                                is_fellow=is_fellow)
                storage_session.add(people)
                # find out what to return
            return people
        except:
            return "Failed"

    def save_rooms(self, storage_session):
        """
        Loads data from the rooms dict into the database
        """
        try:
            for key, values in rooms.items():
                room_name = key
                is_office = values["is_office"]
                room_data = Rooms(room_name=room_name, is_office=is_office)

                storage_session.add(room_data)

            return room_data
        except:
            return "Failed"

    def save_allocations(self, storage_session):
        """
        Loads data of room allocations into allocations table
        """
        try:
            for key, values in rooms.items():
                room_name = key
                for identifier in values["occupants"]:
                    occupant_id = identifier

                    allocation_data = Allocations(room_name=room_name,
                                                  occupant_id=occupant_id)
                    storage_session.add(allocation_data)

            return allocation_data
        except:
            return "Failed"

    def load_state(self, args):
        """
        Loads data from a database into the application
        """
        # import ipdb
        # ipdb.set_trace()
        db_name = args["<sqlite_database>"]
        if os.path.exists(db_name):

            sess = self.connect_to_db(db_name)

            try:
                people_from_db = sess.query(People).all()
                rooms_from_db = sess.query(Rooms).all()
                allocations_from_db = sess.query(Allocations).all()

                print(self.load_people(people_from_db))
                print(self.load_rooms(rooms_from_db))
                print(self.load_allocations(allocations_from_db))

                message = "Data successfully added"
            except:
                message = "No Data Added"

            sess.commit()
            sess.close()
        else:
            message = "{} does not exist".format(db_name)

        return message

    def load_people(self, people_from_db):
        """
        Saves data to people dictionary
        """
        message = ""
        for person in people_from_db:
            people_data.update({
                person.person_id:
                {'name': str(person.name),
                 'accomodation': str(person.wants_accomodation),
                 'is_fellow': bool(person.is_fellow)}
            })

            message += "{} successfully added\n".format(person.name)
        return message

    def load_rooms(self, rooms_from_db):
        """
        Saves data to rooms dictionary
        """
        message = ""
        for room in rooms_from_db:
            room_name = str(room.room_name)
            is_office = bool(room.is_office)

            rooms.update(
                {room_name: {"occupants": [], "is_office": is_office}})

            message += "{} successfully added\n".format(room_name)
        return message

    def load_allocations(self, allocations_from_db):
        """
        Saves data to people dictionary
        """
        message = ""
        for allocation in allocations_from_db:
            room = rooms.get(str(allocation.room_name), None)
            if room is None:
                message += "{} Not Created".format(str(allocation.room_name))
                return message
            room['occupants'].append(allocation.occupant_id)
            name = my_room.get_names(allocation.occupant_id)

            message += "{} successfully added to room {}\n".format(
                name.upper(), str(allocation.room_name))

        return message
