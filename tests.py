import unittest

from app.amity.amityClass import Amity, rooms
from app.person.fellowClass import Fellow
from app.person.personClass import Person
from app.person.staffClass import Staff
from app.rooms.livingspaceClass import LivingSpace
from app.rooms.officeClass import Office
from app.rooms.roomClass import Room
from app.database.amity_database import Database
from app.database.models import *


class TestClasses(unittest.TestCase):
    """Class to test class initialization"""

    def setUp(self):
        self.test_amity = Amity()
        self.test_fellow = Fellow()
        self.test_staff = Staff()
        self.test_person = Person()
        self.test_room = Room()
        self.test_office = Office()
        self.test_livingspace = LivingSpace()
        self.test_database = Database()
        self.test_get_room_type = self.test_amity.get_room_type("O")

        # Test for creation of multiple offices
        self.test_amity.create_room(
            {"<room_name>": ["Valhalla", "Oculus"]}, "O")

        # Test for creation of multiple living spaces
        self.test_amity.create_room(
            {"<room_name>": ["Jade", "Emerald"]}, "L")

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_amity, Amity, msg="Cannot create `Amity` instance")
        self.assertIsInstance(
            self.test_livingspace, LivingSpace,
            msg="Cannot create `LivingSpace` instance")
        self.assertIsInstance(
            self.test_office, Office, msg="Cannot create `Office` instance")
        self.assertIsInstance(
            self.test_room, Room, msg="Cannot create `Room` instance")
        self.assertIsInstance(
            self.test_fellow, Fellow, msg="Cannot create `Fellow` instance")
        self.assertIsInstance(
            self.test_person, Person, msg="Cannot create `Person` instance")
        self.assertIsInstance(
            self.test_staff, Staff, msg="Cannot create `Staff` instance")
        self.assertIsInstance(
            self.test_database, Database,
            msg="Cannot create `Database` instance")

    def test_get_room_type_in_amity(self):
        self.assertEqual(self.test_get_room_type,
                         "O", msg="Room Type returned is not 'O' ")

    def test_create_room_in_amity(self):
        self.assertDictEqual({"Valhalla": {"occupants": [], "is_office": True},
                              "Oculus": {"occupants": [], "is_office": True},
                              "Jade": {"occupants": [], "is_office": False},
                              "Emerald": {"occupants": [], "is_office": False}},
                             rooms, msg="Rooms were not created")

    def test_add_person_in_person(self):
        pass


if __name__ == '__main__':
    unittest.main()
