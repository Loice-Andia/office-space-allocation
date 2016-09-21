import os
import unittest
from roomClass import Room
from app.amity.amityClass import Amity
from app.person.personClass import Person


class TestRoom(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_amity = Amity()
        self.test_person = Person()
        self.test_room = Room()

        sample_fellow = {"<first_name>": "Jimmy",
                         "<last_name>": "Kamau",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.test_person.add_person(sample_fellow)

        self.test_amity.create_room(
            {"<room_name>": ["Valhalla", "Oculus"]}, "O")

        self.test_amity.create_room(
            {"<room_name>": ["Jade"]}, "L")
        self.test_person.load_people({"<filename>": "try.txt"})
        self.test_amity.create_room(
            {"<room_name>": ["Emerald"]}, "L")

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_room, Room, msg="Cannot create `Room` instance")

    def test_getting_persons_name_from_people_data_dictionary(self):
        # Test getting of a person's name
        self.get_name = self.test_room.get_names(1)
        self.get_name_with_wrong_id = self.test_room.get_names(15)
        self.assertEqual(self.get_name, "JIMMY KAMAU",
                         msg="Wrong Person name retrieved")
        self.assertEqual(self.get_name_with_wrong_id,
                         "Person Does not exist", msg="Person Exists")

    def test_print_allocations(self):
        # Test print allocations function
        self.print_allocations_without_filename = self.test_room.print_allocations({
            "-o": False, "<filename>": None})
        self.print_allocations_with_filename = self.test_room.print_allocations({
            "-o": True, "<filename>": "test_allocations.txt"})
        self.assertNotEqual(self.print_allocations_without_filename,
                            "", msg="Wrong data printed")
        self.assertTrue(os.path.exists("test_allocations.txt"),
                        msg="File not created")
        os.remove("test_allocations.txt")

    def test_print_unallocated(self):
        # Test print unallocated function
        self.print_unallocated_without_filename = self.test_room.print_unallocated({
            "-o": False, "<filename>": None})
        self.print_unallocated_with_filename = self.test_room.print_unallocated({
            "-o": True, "<filename>": "test_unallocated.txt"})
        self.assertIn("JIMMY KAMAU",
                      self.print_unallocated_without_filename,
                      msg="Wrong data printed")
        self.assertTrue(os.path.exists("test_unallocated.txt"))
        os.remove("test_unallocated.txt")

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
