import unittest
from livingspaceClass import LivingSpace


class TestLivingSpace(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_living_space = LivingSpace()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_living_space, LivingSpace,
            msg="Cannot create `Living Space` instance")