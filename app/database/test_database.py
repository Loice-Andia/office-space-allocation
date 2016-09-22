import unittest
import mock
from app.database.amity_database import Database


class testDatabase(unittest.TestCase):
    """

    This is Test class for Database methods.
    It contains tests for the save_state and load_state methods.

    """

    def setUp(self):
        self.test_database = Database()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_database, Database,
            msg="Cannot create `Database` instance")

    @mock.patch('amity_database.Database.connect_to_db')
    def test_database_creation(self, mocked_connection):
        # Test database methods
        self.test_sample_database = mocked_connection(
            "test_database.db")
        mocked_connection.assert_called_once_with("test_database.db")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': [2]},
        'VALHALLA': {'is_office': True, 'occupants': [1]},
        'JADE': {'is_office': False, 'occupants': [1]}})
    @mock.patch.dict('app.person.personClass.people_data', {
        1: {'name': 'OLUWAFEMI SULE', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'LOICE ANDIA', 'is_fellow': False, 'accomodation': 'N'}})
    @mock.patch('amity_database.Database.connect_to_db')
    def test_database_save_state_method(self, mocked_connection):
        # Test methods for saving to the database
        mocked_connection("test_database.db")
        self.test_save_people = self.test_database.save_people(
            mocked_connection)
        self.assertNotEqual(self.test_save_people,
                            "Failed", msg="People not added to database")

        self.test_save_rooms = self.test_database.save_rooms(
            mocked_connection)
        self.assertNotEqual(self.test_save_rooms,
                            "Failed", msg="Rooms not added to database")

        self.test_save_allocations = self.test_database.save_allocations(
            mocked_connection)
        self.assertNotEqual(self.test_save_allocations,
                            "Failed", msg="Allocations not added to database")

        self.test_save_state_with_dbname = self.test_database.save_state({
            "--db": "test_database.db"})
        mocked_connection.assert_called_once_with("test_database.db")

        self.test_save_state_failure = self.test_database.save_state({
            "--db": ""})
        self.assertRaises(Exception, self.test_save_state_failure,
                          msg="Exception not raised")

    @mock.patch('amity_database.Database.connect_to_db')
    def test_save_state_without_db_name(self, mocked_connection):
        mocked_connection("amity.db")
        self.test_database.save_state({"--db": None})
        mocked_connection.assert_called_once_with("amity.db")

    @mock.patch('amity_database.Database.connect_to_db')
    def test_database_load_state_method(self, mocked_connection):
        # Test Load state methods
        mocked_connection("test_database.db")
        mocked_connection.assert_called_once_with("test_database.db")
        self.test_load_state = self.test_database.load_state({
            "<sqlite_database>": "test_database.db"})
        self.test_load_state_failure = self.test_database.load_state({
            "<sqlite_database>": ""})
        self.test_load_state_with_non_existing_db = self.test_database.load_state({
            "<sqlite_database>": "test.db"})
        self.assertEqual(self.test_load_state,
                         "Data successfully added",
                         msg="Data not added from the database")
        self.assertEqual(self.test_load_state_with_non_existing_db,
                         "test.db does not exist",
                         msg="Database Exists")
        self.assertRaises(Exception, self.test_load_state_failure,
                          msg="Exception not raised")


if __name__ == '__main__':
    unittest.main()
