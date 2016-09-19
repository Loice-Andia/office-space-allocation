import unittest
from amityClass import Amity, rooms


class TestAmity(unittest.TestCase):
    """

    This is Test class for Amity class and its methods.
    It contains tests for the get_room_type and create_room methods.

    """

    def setUp(self):
        self.test_amity = Amity()
        self.test_get_room_type = self.test_amity.get_room_type("O")

        self.test_create_single_room = self.test_amity.create_room(
            {"<room_name>": ["Krypton"]}, "O")

        # Test if a room is added twice
        self.test_adding_room_twice = self.test_amity.create_room(
            {"<room_name>": ["Krypton"]}, "O")

        # Test for creation of multiple offices
        self.test_amity.create_room(
            {"<room_name>": ["Valhalla", "Oculus"]}, "O")

        # Test for creation of multiple living spaces
        self.test_amity.create_room(
            {"<room_name>": ["Emerald", "Jade"]}, "L")

    def test_adding_rooms_twice(self):
        self.assertEqual(self.test_adding_room_twice,
                         "KRYPTON Exists\n",
                         msg="Room added twice")

    def test_creation_of_rooms(self):
        self.assertIn("KRYPTON", self.test_create_single_room,
                      msg="Room not created")
        self.assertDictContainsSubset({
            "VALHALLA": {"occupants": [], "is_office": True},
            "OCULUS": {"occupants": [], "is_office": True},
            "EMERALD": {"occupants": [], "is_office": False},
            "JADE": {"occupants": [], "is_office": False}},
            rooms, msg="Multiple Rooms were not created")


if __name__ == '__main__':
    unittest.main()
