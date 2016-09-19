import os
import unittest

from app.amity.amityClass import Amity
from app.person.personClass import Person
from app.database.amity_database import Database


class TestClasses(unittest.TestCase):
    """Class to test class initialization"""

    def setUp(self):
        self.test_amity = Amity()
        self.test_person = Person()
        self.test_database = Database()

        self.test_amity.create_room(
            {"<room_name>": ["Valhalla", "Oculus"]}, "O")

        self.test_amity.create_room(
            {"<room_name>": ["Jade"]}, "L")
        self.test_person.load_people({"<filename>": "try.txt"})


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
            self.test_person, Person, msg="Cannot create `Person` instance")
        self.assertIsInstance(
            self.test_database, Database,
            msg="Cannot create `Database` instance")

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
        os.remove('amity.db')


if __name__ == '__main__':
    unittest.main()
