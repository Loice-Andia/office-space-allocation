import unittest
import mock
from roomClass import Room


class TestRoom(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_room = Room()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_room, Room, msg="Cannot create `Room` instance")

    @mock.patch.dict('app.person.personClass.people_data', {
        1: {'name': 'JIMMY KAMAU', 'is_fellow': True, 'accomodation': 'Y'}})
    def test_getting_persons_name_from_people_data_dictionary(self):
        # Test getting of a person's name
        self.get_name = self.test_room.get_names(1)
        self.get_name_with_wrong_id = self.test_room.get_names(15)
        self.assertEqual(self.get_name, "JIMMY KAMAU",
                         msg="Wrong Person name retrieved")
        self.assertEqual(self.get_name_with_wrong_id,
                         "Person Does not exist", msg="Person Exists")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': [2]},
        'VALHALLA': {'is_office': True, 'occupants': [1]},
        'JADE': {'is_office': False, 'occupants': [1]}})
    @mock.patch.dict('app.person.personClass.people_data', {
        1: {'name': 'OLUWAFEMI SULE', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'LOICE ANDIA', 'is_fellow': False, 'accomodation': 'N'}})
    @mock.patch('roomClass.open')
    def test_print_allocations(self, mocked_open):
        # Test print allocations function
        self.print_allocations_without_filename = self.test_room.print_allocations({
            "-o": False, "<filename>": None})
        self.test_room.print_allocations({
            "-o": True, "<filename>": "test_allocations.txt"})

        mocked_open.assert_called_once_with("test_allocations.txt", 'wt')
        self.assertNotEqual(self.print_allocations_without_filename,
                            "", msg="Wrong data printed")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': []}})
    @mock.patch.dict('app.person.personClass.people_data', {
        1: {'name': 'JIMMY KAMAU', 'is_fellow': True, 'accomodation': 'Y'}})
    @mock.patch('roomClass.open')
    def test_print_unallocated(self, mocked_open):
        # Test print unallocated function
        self.print_unallocated_without_filename = self.test_room.print_unallocated({
            "-o": False, "<filename>": None})
        self.test_room.print_unallocated({
            "-o": True, "<filename>": "test_unallocated.txt"})
        self.assertIn("JIMMY KAMAU",
                      self.print_unallocated_without_filename,
                      msg="Wrong data printed")
        mocked_open.assert_called_once_with("test_unallocated.txt", 'wt')

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'JADE': {'is_office': False, 'occupants': [1]},
        'EMERALD': {'is_office': False, 'occupants': []}})
    @mock.patch.dict('app.person.personClass.people_data', {
        1: {'name': 'JIMMY KAMAU', 'is_fellow': True, 'accomodation': 'Y'}})
    def test_print_room(self):
        # Test print room function
        self.printing_of_non_existing_room = self.test_room.print_room({
            "<room_name>": "Midgar"})
        self.printing_of_existing_room = self.test_room.print_room({
            "<room_name>": "Jade"})
        self.printing_of_empty_room = self.test_room.print_room({
            "<room_name>": "Emerald"})
        self.assertEqual(self.printing_of_non_existing_room,
                         "MIDGAR Does Not Exist", msg="Room Exists")
        self.assertNotEqual(self.printing_of_existing_room,
                            "", msg="Room Does Not Exist")
        self.assertIn("No Occupants", self.printing_of_empty_room,
                      msg="Room has occupants")


if __name__ == '__main__':
    unittest.main()
