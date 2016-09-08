import os
from app.amity import my_amity
from app.amity.amityClass import rooms
from app.person.personClass import people_data
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
        else:
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

            message = "Data has been stored in the " + self.db_name + " database"

        except:
            message = "Error saving data to " + self.db_name

        save_session.commit()
        save_session.close()

        print message
        return message

    def save_people(self, storage_session):
        """
        Loads data from the people_data dict into the database
        """
        try:
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
                    storage_session.add(people)
            return "Success"
        except:
            return "Failed"

    def save_rooms(self, storage_session):
        """
        Loads data from the rooms dict into the database
        """
        try:
            for room_type in rooms.keys():
                for room in rooms[room_type].keys():
                    room_name = room
                    room_type = room_type
                    room_data = Rooms(room_name=room_name, room_type=room_type)

                    storage_session.add(room_data)
            return "Success"
        except:
            return "Failed"

    def save_allocations(self, storage_session):
        """
        Loads data of room allocations into allocations table
        """
        try:
            for room_type in rooms.keys():
                for room in rooms[room_type].keys():
                    for identifier in rooms[room_type][room]:
                        occupant_id = identifier
                        room_name = room

                        allocation_data = Allocations(room_name=room_name,
                                                      occupant_id=occupant_id)
                        storage_session.add(allocation_data)

            return "Success"
        except:
            return "Failed"

    def load_state(self, args):
        """
        Loads data from a database into the application
        """
        import ipdb
        ipdb.set_trace()
        db_name = args["<sqlite_database>"]
        if os.path.exists(db_name):

            sess = self.connect_to_db(db_name)

            people_from_db = sess.query(People).all()
            rooms_from_db = sess.query(Rooms).all()
            allocations_from_db = sess.query(Allocations).all()

            self.load_people(people_from_db)
            self.load_rooms(rooms_from_db)
            self.load_allocations(allocations_from_db)

            print "Data successfully added"

            sess.commit()
            sess.close()
        else:
            print db_name + " does not exist"

        return "Success"

    def load_people(self, people_from_db):
        """
        Saves data to people dictionary
        """
        for person in people_from_db:
            if person.is_staff is True:
                people_data["Staff"].update({
                    person.person_id:
                    {'name': str(person.name), 'accomodation': str(
                        person.wants_accomodation)}
                })
            elif person.is_fellow is True:
                people_data["Fellow"].update({
                    person.person_id:
                    {'name': str(person.name), 'accomodation': str(
                        person.wants_accomodation)}
                })
            print person.name + " successfully added"
        return "Success"

    def load_rooms(self, rooms_from_db):
        """
        Saves data to rooms dictionary
        """
        for room in rooms_from_db:
            room_name = str(room.room_name)
            room_type = str(room.room_type)
            if room_type is 'Office':
                rooms['Office'].update({room_name: []})
            elif room_type is 'LivingSpace':
                rooms['LivingSpace'].update({room_name: []})
            print room.room_name + " successfully added"
        return "Success"

    def load_allocations(self, allocations_from_db):
        """
        Saves data to people dictionary
        """
        for allocation in allocations_from_db:
            for room_type in rooms.keys():
                if str(allocation.room_name) in rooms[room_type].keys():
                    rooms[room_type][str(allocation.room_name)].append(
                        allocation.occupant_id)
        return "Success"
