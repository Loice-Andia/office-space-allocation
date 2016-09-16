import os
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

        # Test loading of people from a text file
        self.test_person.load_people({"<filename>": "try.txt"})

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

        self.test_allocate_office = self.test_person.add_person(sample_staff)

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
            "<person_identifier>": 10,
            "<new_room_name>": "Jade"})

        # Test getting of a person's name
        self.test_get_name = self.test_room.get_names(1)
        self.test_get_name_with_wrong_id = self.test_room.get_names(15)

        # Test print allocations function
        self.test_print_allocations_without_filename = self.test_room.print_allocations({
            "-o": False, "<filename>": None})
        self.test_print_allocations_with_filename = self.test_room.print_allocations({
            "-o": True, "<filename>": "test_allocations.txt"})

        # Test print unallocated function
        self.test_print_unallocated_without_filename = self.test_room.print_unallocated({
            "-o": False, "<filename>": None})
        self.test_print_unallocated_with_filename = self.test_room.print_unallocated({
            "-o": True, "<filename>": "test_unallocated.txt"})

        # Test print room function
        self.test_printing_of_non_existing_room = self.test_room.print_room({
            "<room_name>": "Midgar"})
        self.test_printing_of_existing_room = self.test_room.print_room({
            "<room_name>": "Jade"})
        self.test_printing_of_empty_room = self.test_room.print_room({
            "<room_name>": "Oculus"})

        # Test database methods
        self.test_sample_database = self.test_database.connect_to_db(
            "test_database.db")

        # Test methods for saving to the database
        self.test_save_people = self.test_database.save_people(
            self.test_sample_database)
        self.test_save_rooms = self.test_database.save_rooms(
            self.test_sample_database)
        self.test_save_allocations = self.test_database.save_allocations(
            self.test_sample_database)
        self.test_save_state_with_dbname = self.test_database.save_state({
            "--db": "test_database.db"})
        self.test_save_state_failure = self.test_database.save_state({
            "--db": ""})
        self.test_save_state_without_dbname = self.test_database.save_state({
            "--db": None})

        # Test Load state methods
        self.test_load_state = self.test_database.load_state({
            "<sqlite_database>": "test_database.db"})
        self.test_load_state_failure = self.test_database.load_state({
            "<sqlite_database>": ""})
        self.test_load_state_with_non_existing_db = self.test_database.load_state({
            "<sqlite_database>": "test.db"})

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

    def test_load_people_from_a_text_file(self):
        self.assertDictContainsSubset({
            2: {'name': "OLUWAFEMI SULE",
                'accomodation': 'Y',
                'is_fellow': True},
            3: {'name': "DOMINIC WALTERS",
                'accomodation': 'N',
                'is_fellow': False}
        }, people_data,
            msg="People from text file not added")

    def test_calling_add_person_twice_with_same_args(self):
        self.assertEqual(self.test_adding_person_twice,
                         "LOICE ANDIA Already Exists\n",
                         msg="Person added twice")

    def test_office_allocation_in_add_person(self):
        self.assertRaises(Exception, self.test_allocate_office,
                          msg="Person not allocated office")

    def test_allocation_of_office_and_living_space_when_adding_a_fellow(self):
        self.assertDictContainsSubset({
            "RUBY": {"occupants": [], "is_office": False}},
            rooms, msg="Person not allocated Living Space")

    def test_get_room_type_in_amity(self):
        self.assertEqual(self.test_get_room_type,
                         "O", msg="Room Type returned is not 'O' ")

    def test_create_room_in_amity(self):
        self.assertDictContainsSubset({
            "VALHALLA": {"occupants": [], "is_office": True},
            "OCULUS": {"occupants": [], "is_office": True},
            "EMERALD": {"occupants": [], "is_office": False}},
            rooms, msg="Multiple Rooms were not created")

    def test_reallocate_room(self):
        self.assertDictContainsSubset({
            "JADE": {"occupants": [10], "is_office": False}},
            rooms, msg="Person has not been reallocated")

    def test_getting_persons_name_from_people_data_dictionary(self):
        self.assertEqual(self.test_get_name, "LOICE ANDIA",
                         msg="Wrong Person name retrieved")
        self.assertEqual(self.test_get_name_with_wrong_id,
                         "Person Does not exist", msg="Person Exists")

    def test_print_allocations(self):
        self.assertNotEqual(self.test_print_allocations_without_filename,
                            "", msg="Wrong data printed")
        self.assertTrue(os.path.exists("test_allocations.txt"),
                        msg="File not created")

    def test_print_unallocated(self):
        self.assertNotEqual(self.test_print_unallocated_without_filename,
                            "", msg="Wrong data printed")
        self.assertTrue(os.path.exists("test_unallocated.txt"))

    def test_print_room(self):
        self.assertEqual(self.test_printing_of_non_existing_room,
                         "MIDGAR Does Not Exist", msg="Room Exists")
        self.assertNotEqual(self.test_printing_of_existing_room,
                            "", msg="Room Does Not Exist")
        self.assertIn(self.test_printing_of_empty_room,
                      "No Occupants", msg="Room has occupants")

    def test_database_creation(self):
        self.assertTrue(os.path.exists("test_database.db"),
                        msg="Database not created")

    def test_database_save_state_method(self):
        self.assertNotEqual(self.test_save_people,
                            "Failed", msg="People not added to database")
        self.assertNotEqual(self.test_save_rooms,
                            "Failed", msg="Rooms not added to database")
        self.assertNotEqual(self.test_save_allocations,
                            "Failed", msg="Allocations not added to database")
        self.assertTrue(os.path.exists("test_database.db"),
                        msg="Data not saved to database")
        self.assertRaises(Exception, self.test_save_state_failure,
                          msg="Exception not raised")
        self.assertTrue(os.path.exists("amity.db"),
                        msg="Data not saved to database")

    def test_database_load_state_method(self):
        self.assertEqual(self.test_load_state,
                         "Data successfully added",
                         msg="Data not added from the database")
        self.assertEqual(self.test_load_state_with_non_existing_db,
                         "test.db does not exist",
                         msg="Database Exists")
        self.assertRaises(Exception, self.test_load_state_failure,
                          msg="Exception not raised")

    def tearDown(self):
        os.remove("test_database.db")
        os.remove("test_allocations.txt")
        os.remove("test_unallocated.txt")
        os.remove('amity.db')


if __name__ == '__main__':
    unittest.main()
