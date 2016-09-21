import unittest
from officeClass import Office


class TestOffice(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_office = Office()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_office, Office, msg="Cannot create `Office` instance")
