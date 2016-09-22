import unittest
from livingspaceClass import LivingSpace


class TestLivingSpace(unittest.TestCase):
    """

    This is Test class for LivingSpace class and
    tests its initialiation

    """

    def setUp(self):
        self.test_living_space = LivingSpace()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_living_space, LivingSpace,
            msg="Cannot create `Living Space` instance")
