import unittest

from app.amity.amityClass import Amity, rooms
from app.person.fellowClass import Fellow
from app.person.personClass import Person, people_data
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

        # Test add person function in Person class without rooms
        sample_person = {"<first_name>": "Loice",
                         "<last_name>": "Andia",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.test_person.add_person(sample_person)

        # Test if a person is added twice
        self.test_adding_person_twice = self.test_person.add_person(
            sample_person)

        # Test for creation of a single room
        self.test_amity.create_room(
            {"<room_name>": ["Krypton"]}, "O")

        # Test add person and allocate office
        sample_staff = {"<first_name>": "John",
                        "<last_name>": "Doe",
                        "Fellow": False,
                        "Staff": True,
                        "<wants_accomodation>": None}

        self.test_person.add_person(sample_staff)

        # Test adding of a fellow and allocate office and living space
        self.test_amity.create_room(
            {"<room_name>": ["Ruby"]}, "L")

        sample_fellow = {"<first_name>": "Jimmy",
                         "<last_name>": "Kamau",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.test_person.add_person(sample_fellow)

        # Test for creation of multiple offices
        self.test_amity.create_room(
            {"<room_name>": ["Valhalla", "Oculus"]}, "O")

        # Test for creation of multiple living spaces
        self.test_amity.create_room(
            {"<room_name>": ["Jade", "Emerald"]}, "L")

        # Test reallocation of rooms
        self.test_reallocate = self.test_person.reallocate_person({
            "<person_identifier>": 3,
            "<new_room_name>": "Jade"})

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

    def test_add_person_in_person(self):
        self.assertDictContainsSubset({1: {
            'name': "LOICE ANDIA",
            'accomodation': 'Y',
            'is_fellow': True}}, people_data,
            msg="Person not created")

    def test_calling_add_person_twice_with_same_args(self):
        self.assertEqual(self.test_adding_person_twice,
                         "LOICE ANDIA Already Exists\n",
                         msg="Person added twice")

    def test_office_allocation_in_add_person(self):
        self.assertDictContainsSubset({
            "Krypton": {"occupants": [2], "is_office": True}},
            rooms, msg="Person not allocated office")

    def test_allocation_of_office_and_living_space_when_adding_a_fellow(self):
        self.assertDictContainsSubset({
            "Ruby": {"occupants": [], "is_office": False}},
            rooms, msg="Person not allocated Living Space")

    def test_get_room_type_in_amity(self):
        self.assertEqual(self.test_get_room_type,
                         "O", msg="Room Type returned is not 'O' ")

    def test_create_room_in_amity(self):
        self.assertDictContainsSubset({
            "Valhalla": {"occupants": [], "is_office": True},
            "Oculus": {"occupants": [], "is_office": True},
            "Emerald": {"occupants": [], "is_office": False}},
            rooms, msg="Multiple Rooms were not created")

    def test_reallocate_room(self):
        self.assertDictContainsSubset({
            "Jade": {"occupants": [3], "is_office": False}},
            rooms, msg="Person has not been reallocated")


if __name__ == '__main__':
    unittest.main()
