import unittest
from staffClass import Staff


class TestStaff(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_staff = Staff()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_staff, Staff, msg="Cannot create `Staff` instance")